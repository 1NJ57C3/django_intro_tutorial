# Django 4.2 Official Tutorial

This repository contains my code-along and notes to Django 5.1's official tutorial found in their documentation [here](https://docs.djangoproject.com/en/5.1/intro/tutorial01/).

## Installation

### Requirements
- Python 3.12.5  
- Python PIP (included with Python 3.4 and later by default)  
- Python venv (included with Python 3.3 and later by deafult)

### Cloning the repository
Assuming you have [Git](https://git-scm.com) installed and configured `git clone` command with the appropriate remote URL for your method of GitHub user authentication.  
Alternatively, this repo can be downloaded as a ZIP file by clicking the "Download ZIP" link in the <button style="font-size: 14px; height: 32px; color: #ffffff; background: #2E9A40; padding: 0px 12px; border-radius: 6px;">&lsaquo;&rsaquo; Code &triangledown;</button> menu on this project's webpage on GitHub.  

### Setting up a virtual environment
To control software dependencies and ensure program behaviors are consistent across different computers, Python uses virtual environments. There are many popular tools for this, but I will be using [`venv`](https://docs.python.org/3/library/venv.html) because it comes with Python.  
  
Using your CLI, navigate to this project's root folder and run the following commands:  
```shell
$ python -m venv venv
# to create the virtual environment  
$ source venv/bin/activate
# to activate the virtual environment  
```
If there were no issues, you should now see `(venv)` in front of your command prompt:  
```shell
(venv) user@machine: ~/current/working/directory$
```
To deactivate the virtual environment, simply use the `deactivate` command.  

### Installing dependencies (requirements.txt or Pipfile)
With the Virtual Environment activated, run the following command:  
```shell
$ python -m pip install -r requirements.txt
```
This will install this project's dependencies into the Virtual Environment that you have created for this project.

## Usage
To run migrations and spool up the server, run the following commands:
```shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
By default, this will run the Django project at port 8000. A different port number or IP address can be used if provided at the end of the `runserver` command as an argument.  
  
It is probably worth noting that Django's [`runserver`](https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-runserver) is meant to be used strictly as a development tool. Per the [install guide](https://docs.djangoproject.com/en/5.1/topics/install/), `Apachi` and `mod_wsgi` should be used instead for production.  
  
<!-- ## Configuration
Any necessary environment variables or configuration files (e.g., .env, settings).   -->
  
## License
MIT, probably?  
  
## Credits
Credits to [Django](https://djangoproject.com) official documentation author(s) for the tutorial that this project is based on.  