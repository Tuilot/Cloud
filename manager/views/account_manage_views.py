from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from account.models import Account
from common_lib.tool_utils import get_pagination


@login_required(login_url='/account/login')
@permission_required('account.manager', login_url='/account/permission_denied')
def account_manage(request):
    per_page_count = 15

    account_count = Account.objects.count()
    page_count = (account_count + per_page_count - 1) // per_page_count
    page = request.GET.get('page', default=1)
    page = int(page)
    pagination = get_pagination(page, page_count)
    accounts = Account.objects.all()[(page - 1) * per_page_count: page * per_page_count]
    data = {
        'accounts': accounts,
        'pagination': pagination
    }
    return render(request, 'account_manage.html', data)
