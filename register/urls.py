from django.conf.urls import url
from .views import CreateUserView

urlpatterns = [
    url(
       regex=r'^$',
       view=CreateUserView.as_view(),
       name='user_create'
    ),
]

