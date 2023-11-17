from django.urls import path
from . import views

urlpatterns = [
    path('update-subs', views.update_subscriptions),
    path('update-email', views.update_email),
]