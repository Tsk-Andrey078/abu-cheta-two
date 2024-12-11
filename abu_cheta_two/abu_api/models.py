from django.db import models

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=512)
    place_of_study = models.CharField(max_length=512)
    teacher_full_name = models.CharField(max_length=512, blank=True, null=True, default=None)
    teacher_phone = models.CharField(max_length=14, blank=True, null=True, default=None)
    stage_one = models.IntegerField(blank=True, null=True, default=None)
    stage_two = models.IntegerField(blank=True, null=True, default=None)

class ColichestvoDebilov(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField()