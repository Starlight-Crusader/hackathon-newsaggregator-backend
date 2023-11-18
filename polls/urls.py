from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_poll),
    path('approve/<int:poll_id>', views.approve_poll),
    path('vote/<int:poll_id>/<int:option>', views.count_vote),
    path('drop', views.approve_poll),  
]