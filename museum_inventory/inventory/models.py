from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

working_states = [('w', 'Working'), ('m', 'Being Maintenanced'),
                  ('b', 'Broken')]

class ToolManager(models.Manager):
    def create_tool(self, type, group):
        tool = self.create(type=type, name=self.get_name(type),
                           group=group)
        return tool

    def get_name(self, type):
        name = type + str(super(ToolManager, self)
        .get_queryset().filter(tool_type=type).count() + 1)
        return name

class Tool(models.Model):
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    group = models.CharField(max_length=255)
    qr_code = models.CharField(max_length=255, default=None, null=True)
    checked_out = models.BooleanField(default=False)
    working_status  = models.CharField(max_length=255,
                                       choices=working_states,
                                       default='w')

    manager = ToolManager()

    def __str__(self):
        return "{0}".format(tool_name)

    def get_latest_log(self):
        self.checkoutlog_set.last()

class Borrower(models.Model):
    user_id = models.OneToOneField(User, primary_key=True)

class CheckOutLog(models.Model):
    tool = models.ForeignKey(Tool)
    borrower = models.ForeignKey(Borrower, related_name='borrowed_logs')
    returner = models.ForeignKey(Borrower, null=True, blank=True,
                                   related_name='returned_logs')
    check_out_time = models.DateTimeField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True)
