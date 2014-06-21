import os

from fabric.api import *


LIVE = {
    'name': 'battlehack-live',
    'host': '',
    'vhost_dir': '/srv/battlehack-live',
    'dumps_dir': '/srv/battlehack-live/dumps',
    'vcs_dir': '/srv/battlehack-live/app/vcs',
    'virtualenv': '/srv/battlehack-live/app/pyenv',
}


TESTING = {
    'name': 'battlehack-test',
    'host': '',
    'vhost_dir': '/srv/battlehack-test',
    'dumps_dir': '/srv/battlehack-test/dumps',
    'vcs_dir': '/srv/battlehack-test/app/vcs',
    'virtualenv': '/srv/battlehack-test/app/pyenv',
}


def live():
    env.vars = LIVE
    env.hosts = [LIVE['host']]
    env.use_ssh_config = True


def testing():
    env.vars = TESTING
    env.hosts = [TESTING['host']]
    env.use_ssh_config = True


def _manage(command):
    with prefix('source %s/bin/activate' % env.vars['virtualenv']):
        run('python %s/src/manage.py %s' % (env.vars['vcs_dir'], command))


def update():
    with cd(env.vars['vcs_dir']):
        run('git pull')


def update_full():
    update()
    requirements()
    static()
    migrate()
    restart()
    restart_worker()


def update_static():
    update()
    static()


def errorpages():
    run('mkdir -p %s/web/static/errors' % env.vars['vhost_dir'])
    run('cp %s/templates/500.html %s/web/static/errors/500.html' % (
        env.vars['vcs_dir'], env.vars['vhost_dir']))


def static():
    _manage('collectstatic --noinput -i src -i templates -i scss')
    _manage('compilejsi18n -d djangojs -l de')
    _manage('compress')
    errorpages()


def static_clear():
    _manage('collectstatic --noinput -c -i src -i templates -i scss')
    _manage('compilejsi18n -d djangojs -l de')
    _manage('compress')
    errorpages()


def migrate():
    dump()
    _manage('syncdb')
    _manage('migrate --all')
    _manage('validate')


def restart():
    run('sudo supervisorctl restart %s' % env.vars['name'])


def restart_worker():
    run('sudo supervisorctl restart %s-worker' % env.vars['name'])


def dump():
    with cd(env.vars['dumps_dir']):
        run('pg_dump > `date --rfc-3339=seconds | sed "s/ /_/g"`.sql')


def cleanup_pyc():
    with cd(env.vars['vcs_dir']):
        run('find . -name "*.py[co]" -delete')


def requirements():
    with prefix('source %s/bin/activate' % env.vars['virtualenv']):
        run('pip install -r %s' % os.path.join(
            env.vars['vcs_dir'], 'resources', 'requirements-server.txt'))