from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

blogg={
    "Python":"<h1>PythonBlog</h1>",
    "Java":"<h1>JavaBlog</h1>",
    "regex":'<h2 style="color:blue;">RegexBlog</h2>'
}

def Home(request):
    return HttpResponse("<h1>Home Page of Blogs Website</h1>")

def Blogs(request):
    return HttpResponse("<h1>Blogs Posts:</h1>\n<ul><li>PythonBlog</li><li>JavaBlog</li></ul>")

res=""
def blog(request,blog):
    global res
    try:
        res=blogg[blog]
    except KeyError:
        return render(request,'404.html', status=404)
    else:
        return HttpResponse(res)