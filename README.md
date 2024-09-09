# Django 5.1 Official Tutorial

This repository contains my code-along and notes to Django 5.1's official tutorial found in their [documentation](https://docs.djangoproject.com/en/5.1/intro/tutorial01/). Although this project, with some modifications to configuration, may make it Windows compatible, it was written on WSL and MacOS.  

## Installation

### Requirements
- [Python](https://www.python.org/) 3.12.5  
  - Python PIP (included with Python 3.4 and later by default)  
  - Python venv (included with Python 3.3 and later by default)  
- [PostgreSQL](https://www.postgresql.org/) 14.13  

### Cloning the repository
Assuming you have [Git](https://git-scm.com) installed and configured, use the `git clone` command with the appropriate remote URL for your method of GitHub user authentication.  
Alternatively, this repo can be downloaded as a ZIP file by clicking the "Download ZIP" link in the <button style="font-size: 14px; height: 32px; color: #ffffff; background: #2E9A40; padding: 0px 12px; border-radius: 6px;">&lsaquo;&rsaquo; Code &triangledown;</button> menu on this project's webpage on GitHub.  

### Setting up a virtual environment
To control software dependencies and ensure program behaviors are consistent across different computers, Python uses virtual environments. There are many popular tools for this, but I will be using [`venv`](https://docs.python.org/3/library/venv.html) because it comes with Python.  

Using your CLI, navigate to this project's root folder and run the following commands:  

```shell
$ python -m venv venv
# Create the virtual environment  
$ source venv/bin/activate
# Activate the virtual environment  
```

If there were no issues, you should now see `(venv)` in front of your command prompt:  

```shell
(venv) user@machine: ~/current/working/directory$
```

To deactivate the virtual environment, simply use the `deactivate` command.  

### Installing Dependencies

With the Virtual Environment activated, run the following command:  

```shell
$ python -m pip install -r requirements.txt
```

This will install this project's dependencies into the Virtual Environment that you have created for this project.  

## Configuration

As most developers know, sensitive data (i.e. API keys, passwords, etc.) should never be hard-coded into a project, nor published. Unfortunately for you, this almost always means some additional setup.  

### Creating a Database

This application relies on `PostgreSQL` for the storage and retrieval of data. To create a database for this application, run the following in your command line:  

```shell
$ sudo -u postgres createdb desired_db_name
# Use your PostgreSQL username instead of `postgres` if appropriate
```

### Environmental Variables

One of the most commonly used methods to keep sensitive information hidden in software development is to write them into a file that is only stored locally in the developer's environment. This data is stored as a list of variable assignments, typically in a file named `.env`.  

A template file (*`.env.dist`*) is included in this repo. Default install values are used where possible. At a minimum, `DB_NAME` and `PASSWORD` will require adjustment.  

### Generating a Secret Key

Most backend frameworks, including Django, use a [secret key](https://docs.djangoproject.com/en/5.1/ref/settings/#secret-key) for cryptographic signatures. Without one, Django will refuse to run.  

There are many ways to generate or obtain such a key, including the Django method in this Python command. Simply copy and paste it into your command line, then its output to the value of `SECRET_KEY` into your `.env` file.  

```shell
$ python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Expected output: A string of 50 random characters
```

### Alternative to .env

A relatively simple alternative to using an `.env` file is to create and use a PostgreSQL password file [documentation](https://www.postgresql.org/docs/current/libpq-pgpass.html) in your home (`~/`) directory. This method is useful when managing multiple database configurations or avoiding `.env` files for security reasons.  

Create the file `~/.pgpass` with the following as its contents:  

```python
hostname:port:database:username:password
# Swap out these keywords with the appropriate values for your environment.
# For example:
# localhost:5432:your_db_name:postgres:your_postgres_user_password
```

Per the documentation, this file's permissions must disallow access to anyone but the owner, or it will be ignored. Run the following in the command line:  

```shell
$ chmod 0600 ~/.pgpass
```

Finally, navigate to this project's `settings.py` file then locate and replace the `DATABASES` section with the following:  

```json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'passfile': '.pgpass',
        },
    }
}
```

### PostgreSQL User Authentication
If you haven't previously used PostgreSQL, you may need to adjust [authentication methods](https://www.postgresql.org/docs/current/auth-methods.html) for local connection types in the [`pg_hba.conf`](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html) file. It can be [located](https://www.postgresql.org/docs/current/runtime-config-file-locations.html#GUC-HBA-FILE) by entering the following into your command line:  

```shell
$ sudo -u postgres psql -c 'show hba_file'
# Example output: /etc/postgresql/14/main/pg_hba.conf
# Reminder: `postgres` is the default PostgreSQL superuser and may differ from your installation
```

By design, the `pg_hba.conf` file can only be edited the PostgreSQL superuser or a user with higher permissions. Run the following in your command line:  

```shell
$ sudo desiredtexteditor location/of/pg_hba.conf
# Example input:
# $ sudo vim /etc/postgresql/14/main/pg_hba.conf
```

Once you have opened the file, look for the following section:  

```conf
# Database administrative login by Unix domain socket
local   all             postgres                                peer
```

Replace "peer" with either "password" or "md5" depending on your desired [password authentication](https://www.postgresql.org/docs/current/auth-password.html) method. Finally, save your changes and restart the PostgreSQL service by running the following command:  

```shell
$ sudo service postgresql restart
```

## Usage

By default, this will run the Django project at port 8000. A different port number or IP address can be used if provided at the end of the `runserver` command as an argument.  

It is probably worth noting that Django's [`runserver`](https://docs.djangoproject.com/en/5.1/ref/django-admin/#django-admin-runserver) command is meant to be used strictly as a development tool. Per the [install guide](https://docs.djangoproject.com/en/5.1/topics/install/), `Apachi` and `mod_wsgi` should be used instead for production.  

To run [migrations](https://docs.djangoproject.com/en/5.1/topics/migrations/) and spool up the server, run the following commands:  

```shell
$ python manage.py makemigrations
$ python manage.py migrate
# Make and run database migrations
$ python manage.py runserver
# Run the Django server
```

### [Django Admin](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#introducing-the-django-admin)

One of the bigger advantages that comes with using Django is that it automatically generates an admin interface for site managers.  

### Creating an Admin User (https://docs.djangoproject.com/en/5.1/intro/tutorial02/#creating-an-admin-user)

To access the admin panel, a user with admin permissions must first be created. In your commmand line, run the following:  

```shell
$ python manage.py createsuperuser
```

You will be prompted for a username, email address, and a password with confirmation. Once created, start the development server and navigate to localhost:8000/admin/ in a browser window. Log in to access the admin panel.  

<!-- ## Troubleshooting   -->

## License
MIT, probably?  

## Credits
Credits to [Django](https://djangoproject.com) official documentation author(s) for the tutorial that this project is based on.  