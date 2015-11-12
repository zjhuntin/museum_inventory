# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CheckInLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('checkin_time', models.DateTimeField(default=datetime.datetime(2015, 11, 10, 21, 37, 6, 608232))),
                ('checkin_ID', models.ForeignKey(to='inventory.Borrower')),
            ],
        ),
        migrations.CreateModel(
            name='CheckOutLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('checkout_time', models.DateTimeField(default=datetime.datetime(2015, 11, 10, 21, 37, 6, 607562))),
                ('checkin_time', models.DateTimeField(null=True)),
                ('checkin_ID', models.ForeignKey(to='inventory.Borrower', null=True, blank=True)),
                ('checkout_ID', models.ForeignKey(to='inventory.Borrower', related_name='Returner')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tool_name', models.CharField(max_length=255)),
                ('tool_type', models.CharField(max_length=255)),
                ('tool_group', models.CharField(max_length=255)),
                ('qr_code', models.CharField(null=True, max_length=255, default=None)),
                ('checked_out', models.BooleanField(default=False)),
                ('working_status', models.CharField(max_length=255, default='w', choices=[('w', 'Working'), ('m', 'Being Maintenanced'), ('b', 'Broken')])),
            ],
        ),
        migrations.AddField(
            model_name='checkoutlog',
            name='tool_id',
            field=models.ForeignKey(to='inventory.Tool'),
        ),
        migrations.AddField(
            model_name='checkinlog',
            name='tool_id',
            field=models.ForeignKey(to='inventory.Tool'),
        ),
    ]
