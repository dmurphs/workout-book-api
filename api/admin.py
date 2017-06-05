from django.contrib import admin
from .models import Lift, LiftEntry, RunEntry

admin.site.register(Lift)
admin.site.register(LiftEntry)
admin.site.register(RunEntry)