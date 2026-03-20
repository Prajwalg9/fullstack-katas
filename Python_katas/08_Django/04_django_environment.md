
# Django App Creation Guide

This guide explains how to create a Django project and app step by step on Windows.

---

## Prerequisites

Make sure the following are installed and working:

- Python 3.x  
- Django (installed via pip)

Check installation:
```bash
python --version
django-admin --version
````

---

## Step 1: Create a Django Project

Create a new project using:

```bash
django-admin startproject myproject
```

Move into the project directory:

```bash
cd myproject
```

Project structure:

```
myproject/
│── manage.py
│── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

---

## Step 2: Create a Django App

Inside the project folder (where `manage.py` exists), run:

```bash
python manage.py startapp myapp
```

App structure:

```
myapp/
│── migrations/
│── __init__.py
│── admin.py
│── apps.py
│── models.py
│── tests.py
└── views.py
```

---

## Step 3: Register the App

Open:

```
myproject/settings.py
```

Add the app inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'myapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

## Step 4: Run the Development Server

Start the Django server:

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

If the Django welcome page appears, the setup is successful.

---

## Key Concepts

* **Project**: The complete website
* **App**: A module or feature (blog, users, students, etc.)
* One project can contain **multiple apps**

---

## Common Mistakes to Avoid

* Running `startapp` outside the project folder
* Forgetting to add the app to `INSTALLED_APPS`
* Using `django` instead of `django-admin` or `python manage.py`

---

## Useful Commands

```bash
django-admin startproject projectname
python manage.py startapp appname
python manage.py runserver
```

---

## Next Steps

* Create views and URLs
* Create models and connect database
* Use Django Admin panel

Happy coding 🚀

```

---

If you want, I can also:
- Customize this README for **GitHub**
- Add **project description + screenshots**
- Convert it into **professional open-source format**

Just tell me 👍
```
