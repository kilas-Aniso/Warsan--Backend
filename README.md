
# WARSAN-BACKEND

 Rajo Management System is a Django-based web application that aims to streamline the management of location data, immunization records, and child population information. It provides efficient location management, accurate immunization records, and enhanced healthcare worker management, ultimately improving the effectiveness of immunization programs.

 It is written in Django 4.2.4 and Python 3.9


# MAIN FEATURES

-Location Management
-Comprehensive Data Capture
-Accurate Immunization Records
-Population Monitoring
-Healthcare Worker Management
- forms and templates

# USAGE

If your project is already in an existing python3 virtualenv first install django by running

Existing virtual env

`$ pip install django`
`$ django-admin.py startproject \`

This assumes that python3 is linked to valid installation of python 3 and that pip is installed and pip3is valid for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

`$ pip3 install django`

And then:

`$ python3 -m django startproject \`



After that just install the local dependencies, run migrations, and start the server.



# Getting Started

First clone the repository from Github and switch to the new directory:


`$ git clone https://github.com/akirachix/Warsan-Backend.git`

`$ cd Warsan-Backend`

Activate the virtualenv for your project.

Install project dependencies:

`$ pip install -r requirements/local.txt`
Then simply apply the migrations:

`$ python manage.py migrate`
You can now run the development server:

`$ python manage.py runserver`