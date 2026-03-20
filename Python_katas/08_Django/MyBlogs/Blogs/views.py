from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("<h1>Home Page of Blogs Website</h1>")

def Blogs(request):
    return HttpResponse("<h1>Blogs Posts:</h1>\n<ul><li>PythonBlog</li><li>JavaBlog</li></ul>")

def PythonBlog(request):
    return HttpResponse("<h1>PythonBlog</h1>")

def JavaBlog(request):
    return HttpResponse("<h1>JavaBlog</h1>")