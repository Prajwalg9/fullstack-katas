Django Request Flow: manage.py → Project URLs → App URLs → Views

This document explains how Django connects the views of app1 using urls.py of app1 and how everything is triggered through manage.py.

1️⃣ Role of manage.py

manage.py is the entry point of a Django project.

What it does:

Starts the development server

Runs migrations

Executes Django management commands

Example:
python manage.py runserver


When this command is run:

Django starts a server

Waits for HTTP requests (e.g. browser requests)

2️⃣ How a Request Starts (Browser → Django)

Example URL typed in browser:

http://127.0.0.1:8000/app1/home/

Request Flow Begins:
Browser → Django Server (manage.py)

3️⃣ Project-Level urls.py

After receiving a request, Django first checks the project-level urls.py.

📁 Project Structure

myproject/
│── myproject/
│   ├── urls.py
│── app1/
│   ├── views.py
│   ├── urls.py
│── manage.py

myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),  # connects app1
]

Explanation:

'app1/' is the base route

include('app1.urls') tells Django:

“If URL starts with app1/, go to app1/urls.py”

4️⃣ App-Level urls.py (app1)

📁 Location

app1/urls.py

Code:
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
]

Explanation:

home/ → calls views.home

about/ → calls views.about

These URLs are relative to app1/

So full URLs become:

/app1/home/
/app1/about/

5️⃣ Views of app1

📁 Location

app1/views.py

Code:
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to App1 Home Page")

def about(request):
    return HttpResponse("About App1")

Explanation:

View functions receive an HTTP request

They return an HTTP response

Django executes the function matched by the URL

6️⃣ Complete Request Flow (Step-by-Step)
1. Browser sends request: /app1/home/
2. manage.py server receives request
3. Django checks myproject/urls.py
4. 'app1/' matched → redirects to app1/urls.py
5. 'home/' matched → views.home is called
6. home() returns HttpResponse
7. Browser displays response

7️⃣ Visual Flow Diagram
Browser
   ↓
manage.py (server)
   ↓
myproject/urls.py
   ↓ include()
app1/urls.py
   ↓
app1/views.py
   ↓
HttpResponse → Browser

8️⃣ Why Use App-Level urls.py?

✅ Clean project structure
✅ Easy to manage large applications
✅ Reusable apps
✅ Better separation of concerns

9️⃣ Summary

manage.py starts Django

Project urls.py routes requests to apps

App urls.py maps URLs to views

Views handle logic and return responses

✅ Key Rule to Remember

Django never directly calls views — URLs always control access to views