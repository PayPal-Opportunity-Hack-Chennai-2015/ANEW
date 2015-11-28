from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(u'',
                       url(r'^$', views.index, name=u'index'),
                       url(r'^dashboard$', views.dashboard, name=u'dashboard'),
                       url(r'^logout$', views.logout, name=u'logout'),
                       )
