from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'HTML/index.html')
    # or
    # html=render_to_string('HTML/index.html')
    # return HttpResponse(html)