"""workout-book-api URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api/', include('api.urls'))
]
