from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^tabledog/', views.tabledog),
    url(r'^insertdog/',views.insertpagedog),
    url(r'^insertdonedog/',views.insertdonedog),
    url(r'^dog(?P<pet_id>[0-9]+)/$', views.tableretrivedog),
    url(r'^updatedog(?P<pet_id>[0-9]+)/$',views.insertupdatedog),
    url(r'^deletedog(?P<pet_id>[0-9]+)/$',views.deleterecorddog),
    url(r'^deleatedonedog(?P<pet_id>[0-9]+)/$',views.deleterecorddog),

    url(r'^tablecat/', views.tablecat),
    url(r'^insertcat/',views.insertpagecat),
    url(r'^insertdonecat/',views.insertdonecat),
    url(r'^cat(?P<pet_id>[0-9]+)/$', views.tableretrivecat),
    url(r'^updatecat(?P<pet_id>[0-9]+)/$',views.insertupdatecat),
    url(r'^deletecat(?P<pet_id>[0-9]+)/$',views.deleterecordcat),
    url(r'^deleatedonecat(?P<pet_id>[0-9]+)/$',views.deleterecordcat),

    url(r'^tablerabbit/', views.tablerabbit),
    url(r'^insertrabbit/',views.insertpagerabbit),
    url(r'^insertdonerabbit/',views.insertdonerabbit),
    url(r'^rabbit(?P<pet_id>[0-9]+)/$', views.tableretriverabbit),
    url(r'^updaterabbit(?P<pet_id>[0-9]+)/$',views.insertupdaterabbit),
    url(r'^deleterabbit(?P<pet_id>[0-9]+)/$',views.deleterecordrabbit),
    url(r'^deleatedonerabbit(?P<pet_id>[0-9]+)/$',views.deleterecordrabbit),





]