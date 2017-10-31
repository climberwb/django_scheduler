from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$",views.schedule_list, name="list"),
    url(r"^schedule/(?P<schedule_id>\d+)/$",views.schedule_show, name="show"),
    url(r"^schedule/(?P<schedule_id>\d+)/activities/(?P<activity_id>\d+)$",views.activity_delete, name="activity-delete"),
    url(r"^schedule/(?P<schedule_id>\d+)/activities/$",views.activity_create, name="activity-create"),
]