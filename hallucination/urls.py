from django.urls import path
from . import views

urlpatterns = [
    path('', views.vision_list, name='vision_list'),
]