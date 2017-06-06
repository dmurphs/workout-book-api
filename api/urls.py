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
    UpdateLiftEntryView


    # CreateSetView, 
    # ListSetsView,
    # DetailSetView,
    # UpdateSetView
    )

urlpatterns = [
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
    )

    # url(
    #     regex=r'^create_set',
    #     view=CreateSetView.as_view(),
    #     name='create_set'
    # ),
    # url(
    #     regex=r'^list_sets',
    #     view=ListSetsView.as_view(),
    #     name='list_sets'
    # ),
    # url(
    #     regex=r'^set_detail/(?P<pk>\d+)',
    #     view=DetailSetView.as_view(),
    #     name='set_detail'
    # ),
    # url(
    #     regex=r'^update_set/(?P<pk>\d+)',
    #     view=UpdateSetView.as_view(),
    #     name='update_set'
    # ),
]