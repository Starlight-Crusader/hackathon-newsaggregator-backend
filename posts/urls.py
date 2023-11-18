from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_posts),
    path('delete', views.drop_posts),
    path('get-all', views.get_all_posts),
    path('get-filtered', views.get_filtered_posts),
    path('get-post/<int:post_id>', views.get_post),
]