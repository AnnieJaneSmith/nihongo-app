from django.conf.urls import url
from django.contrib import admin

from quiz_app import views


urlpatterns = [
    url(r'^(?P<id>\d+)/$', "quiz_app.views.quiz", name='quiz'),
]