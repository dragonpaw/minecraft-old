.. 

dpminecraft
======================

Quickstart
----------

To bootstrap the project::

    virtualenv dpminecraft
    source dpminecraft/bin/activate
    cd path/to/dpminecraft/repository
    pip install -r requirements.pip
    pip install -e .
    cp dpminecraft/settings/local.py.example dpminecraft/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
