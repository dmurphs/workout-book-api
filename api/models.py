from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    is_active = models.BooleanField(default=True)
    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        abstract = True

class Lift(Base):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    description = models.TextField()

class LiftEntry(Base):
    lift = models.ForeignKey(Lift)

    notes = models.TextField()
    duration = models.DurationField()

    class Meta:
        verbose_name_plural = "Lift Entries"

class Set(Base):
    log_entry = models.ForeignKey(LiftEntry)

    set_num = models.SmallIntegerField()
    num_reps = models.SmallIntegerField()

class RunEntry(Base):
    notes = models.TextField()
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    elevation_delta = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = "Run Entries"
