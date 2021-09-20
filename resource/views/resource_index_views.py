from django.shortcuts import render

from resource.models import CompetitionResource


def resource(request):
    resource_set = []
    type_list = CompetitionResource.ChoiceFileType
    search = request.GET.get('search', default='')
    for key, value in type_list:
        resource_type = key
        resource_list = CompetitionResource.objects.all().filter(type__exact=resource_type,file_show_name__contains=search)[:10]
        data = {
            'resource_list': resource_list,
            'resource_type': resource_type,
            'resource_type_text': value
        }
        resource_set.append(data)
    return render(request, 'resource.html', {'resource_set': resource_set})

