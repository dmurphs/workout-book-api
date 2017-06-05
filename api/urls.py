from django.conf.urls import url
from .views import CreateLiftView, ListLiftsView, DetailLiftView, UpdateLiftView

urlpatterns = [
    url(
       regex=r'^create_lift',
       view=CreateLiftView.as_view(),
       name='create_workout'
    ),
    url(
        regex=r'^list_lifts',
        view=ListLiftsView.as_view(),
        name='list_workouts'
    ),
    url(
        regex=r'^lift_detail/(?P<pk>\d+)',
        view=DetailLiftView.as_view(),
        name='workout_detail'
    ),
    url(
        regex=r'^update_lift/(?P<pk>\d+)',
        view=UpdateLiftView.as_view(),
        name='update_workout'
    )
]