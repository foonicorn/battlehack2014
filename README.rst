battlehack
===============================

Installation
------------

.. code-block:: bash

    $ Create your virtualenv (recommended, use virtualenvwrapper)
    $ virtualenv env

    $ # Activate Environment and install
    $ source env/bin/activate
    $ make devinstall

    $ # run tests
    $ make tests


Development settings
--------------------

Create a new file named ``settings.py`` in the ``src/battlehack`` folder with the following content.

.. code-block:: python

    from battlehack.conf.dev_settings import *

And adapt the settings to your environment.


Setup the database
------------------

.. code-block:: bash

    $ python src/manage.py syncdb --migrate --noinput


Staring the server & superuser
------------------------------

.. code-block:: bash

    $ # Create a new super user
    $ python src/manage.py createsuperuser

Now you can run the webserver and start using the site.

.. code-block:: bash

   $ python src/manage.py runserver

This starts a local webserver on `localhost:8000 <http://localhost:8000/>`_. To
view the administration interface visit `/admin/ <http://localhost:8000/admin/>`_
