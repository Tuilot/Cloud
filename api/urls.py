from django.urls import path

from api import views

urlpatterns = [
    path('update_file_name/', views.update_file_name),
    # path('article_likes/', views.article_likes, name='article_likes'),
    # path('article_favorite/', views.article_favorite, name='article_favorite'),
    path('set_permission/', views.set_permission, name='set_permission'),
    # path('verify_blog_url/', views.verify_blog_url, name='verify_blog_url'),
    # path('verify_blog_identity/', views.verify_blog_identity, name='verify_blog_identity'),
    # path('ready_blog_move/', views.ready_blog_move, name='ready_blog_move'),
    # path('delete_draft/', views.delete_draft, name='delete_draft'),
    # path('delete_article/', views.delete_article, name='delete_article'),
    # path('delete_discussion/', views.delete_discussion, name='delete_discussion'),
    path('delete_resource/', views.delete_resource, name='delete_resource'),
    path('update_avatar/', views.update_avatar, name='update_avatar'),
    # path('set_oj_spider_state/', views.set_oj_spider_state, name='set_oj_spider_state'),
    # path('run_spider_task/', views.run_spider_task, name='run_spider_task'),
    # path('discussion_likes/', views.discussion_likes, name='discussion_likes'),
    # path('discussion_favorite/', views.discussion_favorite, name='discussion_favorite'),
    # path('query_spider_status/', views.query_spider_status, name='query_spider_status'),
    # path('follow/', views.follow, name='follow'),
]
