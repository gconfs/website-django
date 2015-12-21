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

Once you have a working and activated virtualenv you can clone this repository.

    :::console
    cd /path/to/your/virtualenv
    # using ssh:
    git clone git@bitbucket.org:gconfs/gconfs-website.git
    # using https:
    git clone https://bitbucket.org/gconfs/gconfs-website.git

### Deployment for development:

    :::console
    # Install the projects requirements
    pip install -r requirements.txt
    # Create the database and populate the tables
    ./manage.py migrate
    # Launch the website
    ./manage.py runserver
    # Enjoy, Test., start working.


### Deployment for production:

    :::console
    # Execute the deployment script
    ./deploy.sh

If you ever need to change the settings, the website configuration can be
found in gconfs\_website/prod.py

### Adjust the configuration to your needs:

* If you use the contact form, create a file gconfs\_website/smtp.py and fill
  it using the default values in gconfs\_website/settings.py
* You will also need recaptcha settings for the form to work. Create a file
  gconfs\_website/captcha.py and fill it accordingly.

## Work on the website:

First you need to activate the virtualenv.

    :::console
    # if you use virtualenvwrapper:
    workon my_env
    # if you use pew:
    pew workon my_env

You can find the issues that need to be resolved [here](https://bitbucket.org/prologin/site/issues?status=new&status=open)
