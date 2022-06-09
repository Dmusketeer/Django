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
├───.
├───.
│   └───
│       ├───
│       │   ├───
│       │   ├───
│       │   └───
│       ├───
│       │   ├───
│       │   ├───
│       │   ├───
│       │   │   └───

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


