from django.db import models
import datetime
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)


    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if self.leaved_at:
            time_duration = self.leaved_at - self.entered_at
        else:
            time_duration = localtime() - self.entered_at
        return time_duration.total_seconds()

    def format_duration(self, duration, unit_of_time=60):
        hours = round(duration // unit_of_time**2)
        minutes = round((duration % unit_of_time**2) // unit_of_time)
        return f" {hours}ч {minutes}м"

    def is_visit_long(self, duration, unit_of_time=60):
        duration_time = round(duration // unit_of_time)
        control_time = 60
        return not duration_time < control_time
