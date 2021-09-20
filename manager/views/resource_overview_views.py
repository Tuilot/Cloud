from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from common_lib.tool_utils import get_pagination
from resource.models import CompetitionResource


@login_required(login_url='/account/login')
@permission_required('account.manager', login_url='/account/permission_denied')
def resource_overview(request):
    page = request.GET.get('page', default=1)
    page = int(page)
    resource_count = len(CompetitionResource.objects.all())
    pagination = get_pagination(page, (resource_count + 14) // 15)
    resources = CompetitionResource.objects.all()[page * 15 - 15: page * 15]
    return render(request, 'resource/overview.html', {'feature': 'overview',
                                                      'resources': resources,
                                                      'pagination': pagination})

