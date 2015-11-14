from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

working_states = [('w', 'Working'), ('m', 'Being Maintenanced'),
                  ('b', 'Broken')]

class ToolManager(models.Manager):
    def create_tool(self, type, group):
        tool = self.create(tool_type=type, tool_name=self.get_tool_name(type),
                           tool_group=group)
        return tool

    def get_tool_name(self, type):
        tool_name = type + str(super(ToolManager, self)
        .get_queryset().filter(tool_type=type).count() + 1)
        return tool_name

class Tool(models.Model):
    tool_type = models.CharField(max_length=255)
    tool_name = models.CharField(max_length=255, null=True)
    tool_group = models.CharField(max_length=255)
    qr_code = models.CharField(max_length=255, default=None, null=True)
    checked_out = models.BooleanField(default=False)
    working_status  = models.CharField(max_length=255,
                                       choices=working_states,
                                       default='w')

    manager = ToolManager()

    def __str__(self):
        return "{0}".format(tool_name)

class Borrower(models.Model):
    user_id = models.OneToOneField(User, primary_key=True)

class CheckOutLog(models.Model):
    tool_id = models.ForeignKey(Tool)
    checkout_ID = models.ForeignKey(Borrower)
    checkin_ID = models.ForeignKey(Borrower, null=True, blank=True,
                                   related_name='Returner')
    check_out_time = models.DateTimeField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True)
