from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    person_visits = Visit.objects.filter(passcard=passcard)
    for visit in person_visits:
        duration = visit.get_duration()
        formatted_time = visit.format_duration(duration)
        visit_long = visit.is_visit_long(duration)
        this_passcard_visits = {
            'entered_at': visit.entered_at,
            'duration': formatted_time,
            'is_strange': visit_long
        }
        passcard_visits.append(this_passcard_visits)
    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_visits
    }
    return render(request, 'passcard_info.html', context)
