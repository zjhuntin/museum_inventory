from django.db import models
from django.db.contrib.auth.models import User

# Create your models here.
class Tool(models.Model):
    tool_name = models.CharField(max_length=255)
    tool_type = models.CharField(max_length=255)
    tool_group = models.CharField(max_length=255)
    qr_code = models.CharField(max_length=255)
    checked_out = models.BooleanField(default=False)
    working_status  = models.CharField(max_length=255)

    def __str__(self):
        return "{0}".format(tool_name)

class CheckOutLog(models.Model):
    tool_id = models.ForeignKey(Tool)
    checkout_ID = models.ForeignKey(Staff)
    checkin_ID = models.ForeignKey(Staff)
    checkout_time = models.DateTimeField(default=datetime.datetime.now)
    checkin_time = models.DateTimeField(blank=True, default=None)


class Staff(models.Model):
    user_id = models.OneToOneField(User, primary_key=True)
