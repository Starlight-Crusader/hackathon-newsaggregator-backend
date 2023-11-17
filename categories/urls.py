from django.urls import path
from . import views

urlpatterns = [
    path('init', views.initialize_categories),
    path('get', views.get_categories),
]