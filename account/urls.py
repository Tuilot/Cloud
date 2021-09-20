from django.urls import path

from account.views import profile_views, account_status_views, show_info_views, premissions_views, \
    my_favorite_views

urlpatterns = [
    path('login/', account_status_views.login, name='login'),
    path('register/', account_status_views.register, name='register'),
    path('logout/', account_status_views.logout, name='logout'),
    path('profile', profile_views.profile, name='profile'),
    path('edit/', profile_views.edit_user_info, name='edit_user_info'),
    path('profile/<str:user_id>', show_info_views.user_show_info, name='user_show_info'),
    path('permission_denied/', premissions_views.permission_denied, name='permission_denied'),
]
