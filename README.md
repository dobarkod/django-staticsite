# A reusable Django static site

This repository contains a Django project set up for simple static file
serving, while still taking advantage of Django templating, and making it
easy to add form processing (eg. for contact forms) and use other Django
features.

More info: http://goodcode.io/blog/django-staticsite/ ‎

## Quickstart

Clone the repository:

    git clone https://github.com/senko/django-staticsite.git

Create a new Python virtual environment and install required packages:

    mkvirtualenv --no-site-packages mysite
    pip install -r django-staticsite/requirements.txt

Run it:

    cd django-staticsite/staticsite
    python manage.py runserver

That's it! The repository comes with an example index.html and CSS taken from
purecess.io.

To add your content, put the HTML templates to `pages/templates` and
static assets to `pages/static`.

## Deploying to Heroku

If you already have Heroku app you want to deploy to, just add the Heroku
remote repository:

    git remote add heroku ...

If you're creating a new Heroku app:

    heroku apps:create mysite

In both cases, deployment (and later updates) are as easy as:

    git push heroku master:master

## License

Public domain. There isn't much to it, anyways, just a few config files.

