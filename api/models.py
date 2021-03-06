from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    is_active = models.BooleanField(default=True)
    when_created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    when_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        abstract = True

class Workout(Base):
    user = models.ForeignKey(User)

    description = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        if self.description:
            return self.description
        else:
            return str(self.date)

class Lift(Base):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class LiftEntry(Base):
    workout = models.ForeignKey(Workout)
    lift = models.ForeignKey(Lift)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Lift: {0}, {1}, {2}'.format(str(self.workout),str(self.lift),self.when_created)

    class Meta:
        verbose_name_plural = 'Lift Entries'

class Set(Base):
    lift_entry = models.ForeignKey(LiftEntry)
    
    num_reps = models.SmallIntegerField()
    weight = models.SmallIntegerField(null=True)

class RunEntry(Base):
    workout = models.ForeignKey(Workout)

    notes = models.TextField(null=True, blank=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    elevation_delta = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return 'Run: {0}, {1}'.format(str(self.workout),self.when_created)

    class Meta:
        verbose_name_plural = 'Run Entries'
