from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('Links_page', views.Links_page),
    path('Links_page/<slug:link>', views.Links, name='Links'),
]