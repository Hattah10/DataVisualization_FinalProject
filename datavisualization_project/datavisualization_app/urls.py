from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dengue'),
    path('projects/', views.education_model_view, name='education')
]
