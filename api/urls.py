from django.conf.urls import url
from .views import (
    CreateLiftView, 
    ListLiftsView, 
    DetailLiftView, 
    UpdateLiftView, 
    CreateSetView, 
    ListSetsView,
    DetailSetView,
    UpdateSetView)

urlpatterns = [
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
        regex=r'^create_set',
        view=CreateSetView.as_view(),
        name='create_set'
    ),
    url(
        regex=r'^list_sets',
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
]