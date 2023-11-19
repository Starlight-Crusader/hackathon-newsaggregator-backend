from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:post_id>', views.create_poll),
    path('approve/<int:poll_id>', views.approve_poll),
    path('vote/<int:poll_id>/<int:option>', views.count_vote),
    path('drop', views.drop_polls),  
]