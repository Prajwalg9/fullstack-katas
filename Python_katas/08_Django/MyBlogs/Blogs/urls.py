from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('Blogs',views.Blogs),
    path('Blogs/Python',views.PythonBlog),
    path('Blogs/java',views.JavaBlog)
]