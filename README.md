# GConfs Website written in Django !

This website is written in **python 3**, using **Django 1.8.5**.

## Instructions for deployment:

### Requirements:

* systemd
* python 3.4+
* postgresql 8+
* virtualenv
* a wrapper to virtualenv (optional)

### Use a python 3 virtualenv:

It is strongly recommended to use a virualenv to isolate your production or
development environment from your system-wide python configuration.

To achieve this you can use the
[virtualenv](https://virtualenv.readthedocs.org/en/latest/) python package.

Or a wrapper around virtualenv:

* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
* [pew](https://github.com/berdario/pew)

Wrappers are a more convinient way to manage your virtualenvs.

### Clone this project:

Once you have a working virtualenv you can clone this repository.

    :::console
    # using ssh:
    git clone git@bitbucket.org:gconfs/gconfs-website.git
    # using https:
    git clone https://Corwin\_@bitbucket.org/gconfs/gconfs-website.git

### Deployment for development:

    :::console
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py runserver
    # Enjoy !

