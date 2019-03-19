from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),

    url(r'^students/$', views.students),

    url(r'^good/(\d+)/$', views.good, name="good"),

    url(r'^main/$', views.main),
    url(r'^detail/$', views.detail),

    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo),


    url(r'^verifycode/$', views.verifycode),
    url(r'^verifycodefile/$', views.verifycodefile),
    url(r'^verifycodecheck/$', views.verifycodecheck),
]