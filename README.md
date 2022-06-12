# Django

## Testing Setup

**Enter in cmd :**

python version

```python
python --version
```
Python interpreter
```python
python
```
<hr>

check Django version

Enter the following commands At the prompt :

```python
import django
django.get_version()
exit()

        OR

django-admin --version
```
**Note:** we can also use quit() to exit python interpreter

check packages installed in vertual envirnoment:
```python
pip list
```

## Creating Your Django Project

```python
django-admin startproject sango

This command will invoke the django-admin.py script, which will set up a new Django project
called sango for you.


```bash
├───sango
│   └───sango
│       └───__init__.py
│       └───settings.py
│       └───urls.py
│       └───wsgi.py
│       └───asgi.py
│   └───manage.py
```

• __init__.py, a blank Python script whose presence indicates to the Python interpreter that
the directory is a Python package;

• settings.py, the place to store all of your Django project’s settings;

• urls.py, a Python script to store URL patterns for your project; and

• wsgi.py, a Python script used to help run your development server and deploy your project
to a production environment


```python
 python manage.py runserver
```
- Executing this command will launch Python, and instruct Django to initiate its lightweight
development server.
- open up your Web browser and enter the URL http://127.0.0.1:8000/.


**Note :**stop the development server -- CRTL + C


## Creating a Django Application

- A Django project is a collection of configurations and applications that together make up a given
Web application or website.
- A Django application exists to perform a particular task. You need to create specific applications that
are responsible for providing your site with particular kinds of functionality

To create the application sangoApp run the following command.

```python
python manage.py startapp sangoApp
```

sangoApp App directory will look like :

```bash
├───sango
│   └───sango
│       └───__init__.py
│       └───settings.py
│       └───urls.py
│       └───wsgi.py
│       └───asgi.py
│   └───manage.py
│   └───sangoApp
│       └───migrations
│           └───__init__.py
│       └───__init__.py
│       └───admin.py
│       └───apps.py
│       └───models.py
│       └───tests.py
│       └───views.py
```

• __init__.py, serving the exact same purpose as discussed previously;

• admin.py, where you can register your models so that you can benefit from some Django machinery which creates an admin interface for you;

• apps.py, that provides a place for any application specific configuration;

• models.py, a place to store your application’s data models - where you specify the entities and relationships between data;

• tests.py, where you can store a series of functions to test your application’s code;

• views.py, where you can store a series of functions that handle requests and return responses;
and

• migrations directory, which stores database specific information related to your models.



- views.py and models.py are the two files you will use for any given application, and form part of
the main architectural design pattern employed by Django, i.e. the Model-View-Template pattern.

- Before you can get started with creating your own models and views, you must first tell your Django
project about your new application’s existence. To do this, you need to modify the settings.py file,
contained within your project’s configuration directory. Open the file and find the INSTALLED_APPS list. Add the sangoApp application to the end of the list, which should then look like the following
example.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sangoApp',
]
```

## Creating a View

