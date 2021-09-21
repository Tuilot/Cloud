# from django.contrib.contenttypes.models import ContentType
# from django.db import models
#
# from account.models import Account
#
#
#
# class FavoriteDetail(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     op_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#
#
# class ArticleFavoriteDetail(FavoriteDetail):
#     article = models.ForeignKey(ProblemArticle, on_delete=models.CASCADE)
#
#
# class DiscussionFavoriteDetail(LikeDetail):
#     discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
