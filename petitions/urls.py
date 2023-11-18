from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_petition),
    path('approve/<int:petition_id>', views.approve_petition),
    path('vote/<int:petition_id>', views.count_sub),
    path('drop', views.drop_petitions),  
]