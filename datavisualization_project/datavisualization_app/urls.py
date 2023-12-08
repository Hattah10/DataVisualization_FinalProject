from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('accounts/login/', views.logoutuser, name='logout'),
    path('home', views.index, name='index'),
    path('projects/', views.education_model_view, name='project3')
]
