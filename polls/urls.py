from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_poll),
    path('approve/<int:user_id>', views.approve_poll),
    path('drop', views.approve_poll),
    
]