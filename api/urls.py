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
       regex=r'^workout_create',
       view=CreateWorkoutView.as_view(),
       name='workout_create'
    ),
    url(
        regex=r'^workouts_list',
        view=ListWorkoutsView.as_view(),
        name='workouts_list'
    ),
    url(
        regex=r'^workout_detail/(?P<pk>\d+)',
        view=DetailWorkoutView.as_view(),
        name='workout_detail'
    ),
    url(
        regex=r'^workout_update/(?P<pk>\d+)',
        view=UpdateWorkoutView.as_view(),
        name='workout_update'
    ),

    # Lifts
    url(
       regex=r'^lift_create',
       view=CreateLiftView.as_view(),
       name='lift_create'
    ),
    url(
        regex=r'^lifts_list',
        view=ListLiftsView.as_view(),
        name='lifts_list'
    ),
    url(
        regex=r'^lift_detail/(?P<pk>\d+)',
        view=DetailLiftView.as_view(),
        name='lift_detail'
    ),
    url(
        regex=r'^lift_update/(?P<pk>\d+)',
        view=UpdateLiftView.as_view(),
        name='lift_update'
    ),

    #Lift Entries
    url(
       regex=r'^lift_entry_create/(?P<workout_id>\d+)',
       view=CreateLiftEntryView.as_view(),
       name='lift_entry_create'
    ),
    url(
        regex=r'^lift_entries_list/(?P<workout_id>\d+)',
        view=ListLiftEntriesView.as_view(),
        name='lift_entries_list'
    ),
    url(
        regex=r'^lift_entry_detail/(?P<pk>\d+)',
        view=DetailLiftEntryView.as_view(),
        name='lift_entry_detail'
    ),
    url(
        regex=r'^lift_entry_update/(?P<pk>\d+)',
        view=UpdateLiftEntryView.as_view(),
        name='lift_entry_update'
    ),

    # Sets
    url(
        regex=r'^set_create/(?P<lift_entry_id>\d+)',
        view=CreateSetView.as_view(),
        name='set_create'
    ),
    url(
        regex=r'^sets_list/(?P<lift_entry_id>\d+)',
        view=ListSetsView.as_view(),
        name='sets_list'
    ),
    url(
        regex=r'^set_detail/(?P<pk>\d+)',
        view=DetailSetView.as_view(),
        name='set_detail'
    ),
    url(
        regex=r'^set_update/(?P<pk>\d+)',
        view=UpdateSetView.as_view(),
        name='set_update'
    ),

    # Run Entries
    url(
       regex=r'^run_entry_create/(?P<workout_id>\d+)',
       view=CreateRunEntryView.as_view(),
       name='run_entry_create'
    ),
    url(
        regex=r'^run_entries_list/(?P<workout_id>\d+)',
        view=ListRunEntriesView.as_view(),
        name='run_entries_list'
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