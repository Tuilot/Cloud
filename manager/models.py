import django.utils.timezone as timezone

from django.db import models


class OjInfo(models.Model):
    name = models.CharField(max_length=30, primary_key=True, default='OJ')
    pages = models.IntegerField(default=0)
    problems_count = models.IntegerField(default=0)
    url = models.CharField(max_length=1000, default='#')
    has_problem_spider = models.BooleanField(default=False)
    last_problem_spider_time = models.DateTimeField(default=timezone.now)
    has_contest_spider = models.BooleanField(default=False)
    last_contest_spider_time = models.DateTimeField(default=timezone.now)


class Announcement(models.Model):
    title = models.CharField(max_length=200, default='公告')
    content = models.CharField(max_length=1000, default='公告内容')
    releases_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-releases_time']
