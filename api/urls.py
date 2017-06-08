from django.conf.urls import url
from .views import (
    CreateWorkoutView, 
    ListWorkoutsView, 
    DetailWorkoutView, 
    UpdateWorkoutView,

    CreateLiftView, 
    ListLiftsView, 
    DetailLiftView, 
    UpdateLiftView, 

    CreateLiftEntryView,
    ListLiftEntriesView,
    DetailLiftEntryView,
    UpdateLiftEntryView,

    CreateSetView, 
    ListSetsView,
    DetailSetView,
    UpdateSetView,

    CreateRunEntryView,
    ListRunEntriesView,
    DetailRunEntryView,
    UpdateRunEntryView)

urlpatterns = [
    #Workouts
    url(
       regex=r'^create_workout',
       view=CreateWorkoutView.as_view(),
       name='create_workout'
    ),
    url(
        regex=r'^list_workouts',
        view=ListWorkoutsView.as_view(),
        name='list_workouts'
    ),
    url(
        regex=r'^workout_detail/(?P<pk>\d+)',
        view=DetailWorkoutView.as_view(),
        name='workout_detail'
    ),
    url(
        regex=r'^update_workout/(?P<pk>\d+)',
        view=UpdateWorkoutView.as_view(),
        name='update_workout'
    ),

    # Lifts
    url(
       regex=r'^create_lift',
       view=CreateLiftView.as_view(),
       name='create_lift'
    ),
    url(
        regex=r'^list_lifts',
        view=ListLiftsView.as_view(),
        name='list_lifts'
    ),
    url(
        regex=r'^lift_detail/(?P<pk>\d+)',
        view=DetailLiftView.as_view(),
        name='lift_detail'
    ),
    url(
        regex=r'^update_lift/(?P<pk>\d+)',
        view=UpdateLiftView.as_view(),
        name='update_lift'
    ),

    #Lift Entries
    url(
       regex=r'^(?P<workout_id>\d+)/new_lift_entry',
       view=CreateLiftEntryView.as_view(),
       name='create_lift_entry'
    ),
    url(
        regex=r'^(?P<workout_id>\d+)/list_lift_entries',
        view=ListLiftEntriesView.as_view(),
        name='list_lift_entries'
    ),
    url(
        regex=r'^lift_entry_detail/(?P<pk>\d+)',
        view=DetailLiftEntryView.as_view(),
        name='lift_entry_detail'
    ),
    url(
        regex=r'^lift_entry_update/(?P<pk>\d+)',
        view=UpdateLiftEntryView.as_view(),
        name='update_lift_entry'
    ),

    # Sets
    url(
        regex=r'^(?P<lift_entry_id>\d+)/create_set',
        view=CreateSetView.as_view(),
        name='create_set'
    ),
    url(
        regex=r'^(?P<lift_entry_id>\d+)/list_sets',
        view=ListSetsView.as_view(),
        name='list_sets'
    ),
    url(
        regex=r'^set_detail/(?P<pk>\d+)',
        view=DetailSetView.as_view(),
        name='set_detail'
    ),
    url(
        regex=r'^update_set/(?P<pk>\d+)',
        view=UpdateSetView.as_view(),
        name='update_set'
    ),

    # Run Entries
    url(
       regex=r'^(?P<workout_id>\d+)/new_run_entry',
       view=CreateRunEntryView.as_view(),
       name='create_run_entry'
    ),
    url(
        regex=r'^(?P<workout_id>\d+)/list_run_entries',
        view=ListRunEntriesView.as_view(),
        name='list_run_entries'
    ),
    url(
        regex=r'^run_entry_detail/(?P<pk>\d+)',
        view=DetailRunEntryView.as_view(),
        name='run_entry_detail'
    ),
    url(
        regex=r'^run_entry_update/(?P<pk>\d+)',
        view=UpdateRunEntryView.as_view(),
        name='update_run_entry'
    )
]