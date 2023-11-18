from django.urls import path
from . import views

urlpatterns = [
    path('init', views.initialize_tags),
    path('get', views.get_tags),
]