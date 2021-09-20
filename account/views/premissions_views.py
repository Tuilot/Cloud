from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/account/login')
def permission_denied(request):
    return render(request, 'permission.html')

