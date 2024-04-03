from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visitors_in_storage = []
    visitor_now_in_storage = Visit.objects.filter(leaved_at=None)
    for visit in visitor_now_in_storage:
        duration = visit.get_duration()
        formatted_time = visit.format_duration(duration)
        is_strange = visit.is_visit_long(duration)
        visitor = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': formatted_time,
            'is_strange': is_strange,
        }
        visitors_in_storage.append(visitor)
    context = {'non_closed_visits': visitors_in_storage,
               }
    return render(request, 'storage_information.html', context)


