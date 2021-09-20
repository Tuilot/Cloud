from django.shortcuts import render
from django.utils.timezone import now

# from contest_calendar.models import Contest
from manager.models import Announcement
from resource.models import CompetitionResource


def index(request):
    resources = CompetitionResource.objects.all()[:15]
    # contests = Contest.objects.filter(start_time__gt=now())[:15]
    announcements = Announcement.objects.all()
    announcement = None
    if announcements.exists():
        announcement = announcements[0]
    data = {
        'resources': resources,
        # 'contests': contests,
        'announcement': announcement
    }
    return render(request, 'index.html', data)
