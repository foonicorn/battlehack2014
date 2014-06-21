#!/bin/bash

echo "Creating directories"
mkdir app bin run dumps web log

echo "Creating virtualenv"
virtualenv app/pyenv

echo "Cloning code"
git clone git@gitlab.moccu.com:moccu/battlehack-2014.git app/vcs

echo "Creating run scripts"
cat > bin/settings-test.sh<<"EOT"
APP=battlehack
HOME=/srv/battlehack-test
PYBIN=$HOME/app/pyenv/bin
APPDIR=$HOME/app/vcs/src

# NCPU=$(grep -c ^processor /proc/cpuinfo)
NCPU=1

CELERY_WORKER=$NCPU
GUN_WORKER=$((2 * $NCPU + 1))

export DJANGO_SETTINGS_MODULE=$APP.settings
export PYTHONPATH=$APPDIR:$PYTHONPATH
EOT

cat > bin/settings-live.sh<<"EOT"
APP=battlehack
HOME=/srv/battlehack-live
PYBIN=$HOME/app/pyenv/bin
APPDIR=$HOME/app/vcs/src

NCPU=$(grep -c ^processor /proc/cpuinfo)

CELERY_WORKER=$NCPU
GUN_WORKER=$((2 * $NCPU + 1))

export DJANGO_SETTINGS_MODULE=$APP.settings
export PYTHONPATH=$APPDIR:$PYTHONPATH
EOT

cat > bin/run.sh<<"EOT"
#!/bin/bash

source `dirname ${BASH_SOURCE[0]}`/settings.sh

GUN=$PYBIN/gunicorn
GUN_SOCK=unix:$HOME/run/gunicorn.sock

source $PYBIN/activate
exec $PYBIN/python $GUN -b $GUN_SOCK -k gevent -w $GUN_WORKER $APP.wsgi:application
EOT
chmod u+x bin/run.sh

cat > bin/worker.sh<<"EOT"
#!/bin/bash

source `dirname ${BASH_SOURCE[0]}`/settings.sh

source $PYBIN/activate
exec $PYBIN/python $APPDIR/manage.py celery worker -A battlehack -E -B -c $CELERY_WORKER
EOT
chmod u+x bin/worker.sh