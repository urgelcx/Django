from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'index.html', views.index1),

    url(r'^attribles', views.attribles),

    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),

    url(r'^showregist/$', views.showregist),
    url(r'^showregist/regist/$', views.regist),


    url(r'^showresponse', views.showresponse),

    url(r'^cookietest', views.cookietest),

    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),



    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain),
    url(r'^quit/$', views.quit),
]