from django.urls import path

from common_lib import manager_utils

urlpatterns = [
    path('update_file_name/', manager_utils.update_file_name),
    path('set_permission/', manager_utils.set_permission, name='set_permission'),
    path('delete_resource/', manager_utils.delete_resource, name='delete_resource'),
    path('update_avatar/', manager_utils.update_avatar, name='update_avatar'),
]