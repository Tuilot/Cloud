import math

from django.shortcuts import render

from common_lib import paginations
from resource.models import CompetitionResource


def more(request):
    resource_type = request.GET.get('type')
    search = request.GET.get('search', default='')
    page = request.GET.get('page', default=1)
    current_page = int(page)
    per_page_count = 20
    if resource_type is None:
        resource_type = 'rank'
    type_list = CompetitionResource.ChoiceFileType
    file_type_text = ''
    is_valid_type = False
    for key, value in type_list:
        if key == resource_type:
            is_valid_type = True
            file_type_text = value
            break

    if not is_valid_type:
        return render(request, '404_page.html', {'error_msg': '未找到该类型资源',
                                                 'url': '/',
                                                 'btn_msg': '返回首页'})
    resources = CompetitionResource.objects.all().filter(type__exact=resource_type,
                                                         file_show_name__contains=search)
    resources_count = resources.count()
    page_count = max(math.ceil(resources_count / per_page_count), 1)
    resource_list = resources[(current_page - 1) * per_page_count: current_page * per_page_count]
    args = {'type': resource_type}
    if search is not '':
        args['search'] = search
    pagination = paginations.get_pagination(current_page, page_count, '', args)
    has_file = True
    if len(resources) == 0:
        has_file = False
    return render(request, 'more.html', {'resources': resource_list,
                                         'all_resource_type': CompetitionResource.ChoiceFileType,
                                         'resource_type': resource_type,
                                         'file_type_text': file_type_text,
                                         'has_file': has_file,
                                         'pagination': pagination,})
