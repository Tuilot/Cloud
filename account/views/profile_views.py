from django.contrib.auth.decorators import login_required

from account.forms import EditUserInfoForm
from account.models import Account
from django.shortcuts import render, redirect


@login_required(login_url='/account/login')
def profile(request):
    user_id = request.user.id
    try:
        user_info = Account.objects.all().get(id__exact=user_id)
    except:
        return render(request, 'hint.html', {'msg': 'no such user!'})

    data = {
        'user_info': user_info,
        'page_type': 'profile'
    }
    return render(request, 'user_center/profile.html', data)


@login_required(login_url='/account/login')
def edit_user_info(request):
    user_id = request.user.id
    try:
        user_info = Account.objects.get(id__exact=user_id)
    except:
        return render(request, 'hint.html', {'msg': 'no such user!'})
    if request.method == 'POST':
        form = EditUserInfoForm(request.POST)
        if form.is_valid():
            user_info.username = form.data.get('edit_username')
            user_info.email = form.data.get('edit_email')
            user_info.phone_number = form.data.get('edit_phone_number')
            user_info.school = form.data.get('edit_school')
            user_info.real_name = form.data.get('edit_real_name')
            user_info.motto = form.data.get('edit_motto')
            user_info.sex = form.data.get('edit_sex')
            user_info.save()
            return redirect('profile')
        else:
            data = {
                'user_info': user_info,
                'page_type': 'edit_user_info',
                'form': form
            }
            return render(request, 'user_center/edit_user_info.html', data)
    else:
        data = {
            'user_info': user_info,
            'page_type': 'edit_user_info'
        }
        return render(request, 'user_center/edit_user_info.html', data)
