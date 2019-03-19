from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/(\d+)$', views.detail),

    url(r'^grades/$', views.grades),
    url(r'^students/$', views.students),

    url(r'^grades/(\d+)$', views.gradesStudents),
]