from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from common_lib import resource_utils
from resource.models import CompetitionResource


@login_required(login_url='/account/login')
@permission_required('account.manager', login_url='/account/permission_denied')



def resource_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('select_file')
        file_show_name = request.POST.get('file_show_name')
        file_type = request.POST.get('file_type')
        error_msg = upload_file_error(file, file_show_name, file_type)
        if error_msg == {}:
            file.name = resource_utils.random_file_name(file.name)
            CompetitionResource.objects.all().create(
                file=file,
                file_size=file.size,
                file_name=file.name,
                file_show_name=file_show_name,
                type=file_type,
            )
        return render(request, 'manager_hint.html', {'msg': '上传文件成功！',
                                                  'url': '/manager/resource/upload',
                                                  'btn_msg': '继续上传'})

    return render(request, 'resource/upload.html', {'feature': 'upload',
                                                    'choice_file_type': CompetitionResource.ChoiceFileType})


def upload_file_error(file, file_show_name, file_type):
    error_msg = {}
    if file is None:
        error_msg['file'] = '上传文件不能为空'
    if file_show_name is None:
        error_msg['file_show_name'] = '请输入文件名'
    if file_type is None:
        error_msg['file_type'] = '请选择文件类型'
    return error_msg

