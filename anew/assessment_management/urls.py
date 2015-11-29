from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(u'',
                       url(r'^$', views.index, name=u'index'),
                       url(r'^dashboard$', views.dashboard, name=u'dashboard'),
                       url(r'^logout$', views.logout, name=u'logout'),
                       url(r'^line_chart/json/$', views.line_chart_json, name='line_chart_json'),
                       url(r'^column_highchart/json/$', views.column_highchart_json,
                           name='column_highchart_json'),
                       )
