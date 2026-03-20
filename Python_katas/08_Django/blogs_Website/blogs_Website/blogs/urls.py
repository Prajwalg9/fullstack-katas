from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),        # home/dashboard
    path('login/', views.login_view, name='login'),        # login page
    path('register/', views.register_view, name='register'), # register
    path('logout/', views.logout_view, name='logout'), 
    path('post/<str:blog>/', views.post_detail, name='post_detail'),
]
