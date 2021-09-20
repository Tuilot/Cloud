from django.contrib.contenttypes.models import ContentType
from django.db import models

from account.models import Account


class LikeDetail(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    op_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FavoriteDetail(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    op_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

