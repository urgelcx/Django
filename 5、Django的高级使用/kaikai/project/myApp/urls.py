from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),


    url(r'^upfile/$', views.upfile),
    url(r'^savefile/$', views.savefile),


    url(r'^studentpage/(\d+)/$', views.studentpage),

    url(r'^ajaxstudents/$', views.ajaxstudents),
    url(r'^studentsinfo/$', views.studentsinfo),


    url(r'^edit/$', views.edit),

    url(r'^celery/$', views.celery),
]



