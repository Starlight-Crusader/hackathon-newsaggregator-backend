from django.urls import path
from . import views

urlpatterns = [
    path('update-subs', views.update_subscriptions),
    path('update-email', views.update_email),
    path('update-verification/<int:user_id>', views.update_verification_status),
    path('drop-users', views.drop_all_users),
    path('profile', views.get_profile)
]