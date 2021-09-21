from django.urls import path

from manager.views import manager_index_views, resource_overview_views, resource_upload_views, \
    account_manage_views

urlpatterns = [
    path('', manager_index_views.manager, name='manager'),
    # path('oj_info/', oj_info_views.oj_info, name='oj_info'),
    path('resource/', resource_overview_views.resource_overview, name='resource_manage'),
    path('resource/overview/', resource_overview_views.resource_overview, name='resource_overview'),
    path('resource/upload/', resource_upload_views.resource_upload, name='resource_upload'),
    path('account/', account_manage_views.account_manage, name='account_manage'),

    # path('timed_task/', timed_task_views.timed_task, name='timed_task'),
    # path('announcement/', announcement_views.announcement, name='edit_announcement'),
]
