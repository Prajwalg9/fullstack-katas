from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

Links_dict = {
    'Home': '<h2>Home Page<h2>',
    'About': '<h2>About Page<h2>',
    'Contact': '<h2>Contact Page<h2>',
    'Projects': '<h2>Project Page<h2>',
    'Skills': '<h2>Skill Page<h2>',
}
def index(request):
    return HttpResponse('<h1><a href="Links_page">Go to links Page</a></h1>')

def Links_page(request):
    res_links=""
    keys=list(Links_dict.keys())
    for key in keys:
        paths=reverse('Links', args=(key,))
        res_links += f'<li><a href="{paths}">{Links_dict[key]}</a></li>'
    res_data=f"<h1>Links Page:</h1><ul>{res_links}</ul>"
    return HttpResponse(res_data)

res=""
def Links(request,link):
    global res
    try:
        res=Links_dict[link]
        return HttpResponse(res)
    except KeyError:
        return HttpResponseNotFound("<h1>Link Not Found</h1>")
