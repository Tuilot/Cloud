from django.urls import path

from api import views

urlpatterns = [
    path('update_file_name/', views.update_file_name),
    path('set_permission/', views.set_permission, name='set_permission'),
    path('delete_resource/', views.delete_resource, name='delete_resource'),
    path('update_avatar/', views.update_avatar, name='update_avatar'),
]
