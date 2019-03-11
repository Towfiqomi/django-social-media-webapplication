from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home2, name='home'),
    path('home/', views.home2, name='home2'),
]