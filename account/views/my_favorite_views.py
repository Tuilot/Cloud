# from django.shortcuts import render
#
# # from api.models import ArticleFavoriteDetail
# from common_lib.tool_utils import get_pagination
#
#
# def my_favorite(request):
#     page = request.GET.get('page', default=1)
#     page = int(page)
#     articles = query_my_favorite_articles(request.user, page)
#     article_page_count = (articles.count() + 9) // 10
#     article_pagination = get_pagination(page, article_page_count)
#     data = {
#         'articles': articles,
#         'article_pagination': article_pagination,
#     }
#     return render(request, 'my_favorite_article.html', data)
#
#
# # def query_my_favorite_articles(user, page):
# #     articles = ArticleFavoriteDetail.objects.filter(user=user)[(page - 1) * 10: page * 10]
# #     return articles
#
