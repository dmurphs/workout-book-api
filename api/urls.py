from django.conf.urls import url
from .views import CreateWorkoutView, ListWorkoutsView, DetailWorkoutView, UpdateWorkoutView, CreateLiftView

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
]