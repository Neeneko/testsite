from django.conf.urls import include, url
from django.contrib import admin

urlpatterns =   [
                    url(r'^board/', include('board.urls')),
                ]
