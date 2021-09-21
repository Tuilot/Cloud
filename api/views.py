import asyncio
from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.core import serializers
from django.http import JsonResponse
from account.models import Account, Follow
from manager.models import OjInfo
from common_lib import tool_utils, account_utils
from common_lib.tool_utils import get_pagination
from resource.models import CompetitionResource


@login_required(login_url='/account/login')
def update_file_name(request):
    file_id = int(request.GET.get('file_id'))
    new_file_name = request.GET.get('new_file_name')

    try:
        CompetitionResource.objects.all().filter(id=file_id).update(
            file_show_name=new_file_name,
        )
        data = {
            'file_name': new_file_name
        }
        return JsonResponse(data, content_type='application/json', safe=False)
    except:
        data = {
            'error': True
        }
        return JsonResponse(data, content_type='application/json', safe=False)



@login_required(login_url='/account/login')
def set_permission(request):
    user_id = request.POST.get('user_id')
    role = request.POST.get('role')
    try:
        user = Account.objects.get(id__exact=user_id)
        if role == 'manager':
            perm_manager = Permission.objects.get(codename__exact='manager')
            if user.has_perm('account.manager'):
                user.user_permissions.remove(perm_manager)
            else:
                user.user_permissions.add(perm_manager)
        else:
            user.is_superuser = not user.is_superuser
        user.save()

        data = {
            'is_manager': user.has_perm('account.manager'),
            'is_superuser': user.is_superuser
        }
        return JsonResponse(data, content_type='application/json', safe=False)
    except:
        return JsonResponse(None, content_type='application/json', safe=False)



@login_required(login_url='/account/login')
def delete_resource(request):
    resource_id = request.POST.get('resource_id')
    try:
        resource = CompetitionResource.objects.filter(id=resource_id)
        resource.delete()
    except:
        pass
    return JsonResponse(None, content_type='application/json', safe=False)


@login_required(login_url='/account/login')
def update_avatar(request):
    user_id = request.user.id
    avatar = request.FILES.get('avatar')
    avatar.name = account_utils.random_avatar_name(avatar.name)
    try:
        user = Account.objects.get(id=user_id)
        user.avatar = avatar
        user.save()
        data = {
            'result': 'success',
            'avatar_url': user.avatar.url
        }
        return JsonResponse(data, content_type='application/json', safe=False)
    except:
        pass
    return JsonResponse(None, content_type='application/json', safe=False)
