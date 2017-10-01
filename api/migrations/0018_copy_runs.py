from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def copy_run_info(apps, schema_editor):

    RunEntry = apps.get_model('api', 'RunEntry')
    Run = apps.get_model('api', 'Run')

    run_entries = RunEntry.objects.all()

    for run_entry in run_entries:
        user = run_entry.workout.user
        distance = run_entry.distance
        elevation_delta = run_entry.elevation_delta
        name = 'Run - {0} miles, {1} feet elevation change'.format(distance, elevation_delta)

        related_run, _ = Run.objects.get_or_create(
            user=user,
            name=name,
            distance=distance,
            elevation_delta=elevation_delta)

        run_entry.run = related_run
        run_entry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_runentry_run'),
    ]

    operations = [
        migrations.RunPython(copy_run_info)
    ]