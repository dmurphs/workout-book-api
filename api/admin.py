from django.contrib import admin
from .models import Workout, Lift, LiftEntry, RunEntry

admin.site.register(Workout)
admin.site.register(Lift)
admin.site.register(LiftEntry)
admin.site.register(RunEntry)