from django.db import models
from django.utils import timezone
import datetime


class WorkingHours(models.Model):
    work_begins = models.BooleanField()
    work_ends = models.BooleanField()
    time = models.DateTimeField()
    employee_id = models.IntegerField(max_length=32)


