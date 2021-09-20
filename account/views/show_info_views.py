from django.shortcuts import render

from account.models import Account
# from article.models import ProblemArticle


def user_show_info(request, user_id):
    per_page_count = 40
    try:
        user_info = Account.objects.all().get(id__exact=user_id)
    except:
        return render(request, 'hint.html', {'msg': 'no such user!'})
    current_page = 1
    # articles = ProblemArticle.objects.filter(author=user_info)[
    #            (current_page - 1) * per_page_count: current_page * per_page_count]
    data = {
        'user_info': user_info,
        'page_type': 'profile',
        # 'articles': articles,
    }
    return render(request, 'user_center/user_show_info.html', data)
