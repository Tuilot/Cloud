from django.urls import path

from resource.views import resource_index_views, resource_list_views

urlpatterns = [
    path('', resource_index_views.resource, name='resource'),
    path('list/', resource_list_views.more, name='resource_more')
]
