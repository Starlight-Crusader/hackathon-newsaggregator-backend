from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_posts),
    path('delete', views.drop_posts),
    path('get', views.get_filtered_posts)
]