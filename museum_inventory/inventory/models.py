from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

working_states = [('w', 'Working'), ('m', 'Being Maintenced'),
                  ('b', 'Broken')]

class Tool(models.Model):
    tool_name = models.CharField(max_length=255)
    tool_type = models.CharField(max_length=255)
    tool_group = models.CharField(max_length=255)
    qr_code = models.CharField(max_length=255)
    checked_out = models.BooleanField(default=False)
    working_status  = models.CharField(max_length=255,
                                       choices=working_states,
                                       default='w')

    def __str__(self):
        return "{0}".format(tool_name)

class ToolManager(models.Manager):
    def create_tool(self):
        return super(ToolManager, self).get_queryset().filter()

class Borrower(models.Model):
    user_id = models.OneToOneField(User, primary_key=True)

class CheckOutLog(models.Model):
    tool_id = models.ForeignKey(Tool)
    checkout_ID = models.ForeignKey(Borrower, related_name='Checker_Outer')
    checkin_ID = models.ForeignKey(Borrower, null=True, blank=True)
    checkout_time = models.DateTimeField(default=datetime.now())
    checkin_time = models.DateTimeField(null=True)

class CheckInLog(models.Model):
    tool_id = models.ForeignKey(Tool)
    checkin_ID = models.ForeignKey(Borrower)
    checkin_time = models.DateTimeField(default=datetime.now())
