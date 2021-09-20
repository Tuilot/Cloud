from django.shortcuts import render

from account.models import Account


def user_show_info(request, user_id):
    per_page_count = 40
    try:
        user_info = Account.objects.all().get(id__exact=user_id)
    except:
        return render(request, 'hint.html', {'msg': 'no such user!'})
    current_page = 1
    data = {
        'user_info': user_info,
        'page_type': 'profile',
    }
    return render(request, 'user_center/user_show_info.html', data)
