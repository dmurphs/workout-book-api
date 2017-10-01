from django.contrib import admin
from .models import Lift, LiftEntry, Set, Run, RunEntry, Workout

admin.site.register(Lift)
admin.site.register(LiftEntry)
admin.site.register(Set)
admin.site.register(Run)
admin.site.register(RunEntry)
admin.site.register(Workout)