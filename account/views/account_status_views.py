from django.shortcuts import render, redirect
from django.contrib import auth

from account.forms import RegistrationForm, LoginForm
from account.models import Account
from common_lib.account_utils import getNewId, calc_md5


def login(request):
    if not request.user.is_anonymous:
        return render(request, 'hint.html', {'msg': '您已登陆',
                                             'url': '/',
                                             'btn_msg': '前往首页'})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user_info = Account.objects.get(email__exact=email)
                if user_info.username == 'superuser' and user_info.is_superuser is False:
                    user_info.is_superuser = True
                    user_info.save()
                request.session['user_id'] = user_info.id
                request.session['email'] = user_info.id
                request.session['user_name'] = user_info.username
                auth.login(request, Account.objects.all().get(id__exact=user_info.id))
            except:
                request.session['email'] = form.cleaned_data.get('email')
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = Account.objects.create(
                id=getNewId(),
                username=username,
                email=email,
                password=calc_md5(password),
            )
            return render(request, 'register.html', {'register_message': '注册成功，现在你可以登陆了！'})

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def logout(request):
    auth.logout(request)
    request.session.clear()
    return redirect('login')
