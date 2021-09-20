from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required(login_url='/account/login')
@permission_required('account.manager', login_url='/account/permission_denied')
def manager(request):
    return render(request, 'manage_base.html')

