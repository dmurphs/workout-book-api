from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=50)
    description = models.TextField()

    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class Lift(models.Model):
    user = models.ForeignKey(User)
    
    name = models.CharField(max_length=50)
    description = models.TextField()

    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class LiftEntry(models.Model):
    workout = models.ForeignKey(Workout)
    lift = models.ForeignKey(Lift)

    notes = models.TextField()
    duration = models.DurationField()

    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Lift Entries"

class Set(models.Model):
    log_entry = models.ForeignKey(LiftEntry)

    set_num = models.SmallIntegerField()
    num_reps = models.SmallIntegerField()

    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class RunEntry(models.Model):
    workout = models.ForeignKey(Workout)

    notes = models.TextField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    elevation_delta = models.DecimalField(max_digits=7, decimal_places=2)

    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Run Entries"
