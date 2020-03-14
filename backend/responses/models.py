from dataclasses import dataclass

from django.db import models
from django_extensions.db.models import TimeStampedModel


@dataclass
class Status:
    active = 'active'
    delete = 'delete'


status = Status()
status_choices = (
        ('active', status.active),
        ('delete', status.delete),
    )


class Response(TimeStampedModel):
    status = models.TextField(choices=status_choices)


class Answer(TimeStampedModel):
    value = models.TextField(null=True, blank=True)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
