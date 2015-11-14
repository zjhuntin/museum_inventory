from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Borrower(models.Model):
    user_id = models.OneToOneField(User, primary_key=True)


class Tool(models.Model):
    tool_type = models.CharField(max_length=255)
    tool_name = models.CharField(max_length=255, null=True)
    tool_group = models.CharField(max_length=255)
    checked_out = models.BooleanField(default=False)
    working_status  = models.CharField(max_length=255)

    def __str__(self):
        return "{0}".format(tool_name)

    def save(self, *args, **kwargs):
        self.tool_name = self.get_tool_name(self.tool_type)
        super(Tool, self).save(*args, **kwargs)

    def get_tool_name(self, type):
        count = Tool.filter(tool_type=type).all().count()
        if count == 0:
            return (type + '_1')
        else:
            return (type + (count + '_' + str(count + 1)))

class ToolManager(models.Manager):
    def get_type_count(self, type):
        return super(ToolManager, self).get_queryset().filter(tool_type =type).count()


class CheckOutLog(models.Model):
    tool_id = models.ForeignKey(Tool)
    checkout_ID = models.ForeignKey(Borrower)
    checkin_ID = models.ForeignKey(Borrower)
    checkout_time = models.DateTimeField(default=datetime.now())
    checkin_time = models.DateTimeField(blank=True, default=None)
