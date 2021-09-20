"""Cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from Cloud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resource.urls')),
    # path('article/', include('article.urls')),
    path('api/', include('api.urls')),
    # path('mdeditor/', include('mdeditor.urls')),
    path('account/', include('account.urls')),
    # path('calendar/', include('contest_calendar.urls')),
    path('manager/', include('manager.urls')),
    path('resource/', include('resource.urls')),
    # path('comments/', include('comments.urls')),
    # path('discussions/', include('discussions.urls')),
    # path('reward/', include('reward.urls')),
    # path('message/', include('message.urls')),
    # path('recent/', include('recent.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)