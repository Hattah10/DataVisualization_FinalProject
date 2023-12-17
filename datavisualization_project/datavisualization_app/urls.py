from django.urls import path
from . import views

urlpatterns = [    
    # path('home/', views.index, name='index'),

    # path('', views.loginuser, name='login'),
    # path('register', views.register, name='register'),
    # path('accounts/login/', views.logoutuser, name='logout'),
    path('', views.index, name='dengue'),
    path('projects/', views.education_model_view, name='education')
]
