from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^clients/$', views.clients_list, name='clients_list'),
    re_path(r'^funds/$', views.funds_list, name='funds_list'),
    re_path(r'^contracts/$', views.contracts_list, name='contracts_list'),
    re_path(r'^clients/new/$', views.clients_new, name='clients_new'),
    re_path(r'^funds/new/$', views.funds_new, name='funds_new'),
    re_path(r'^contracts/new/$', views.contracts_new, name='contracts_new'),
]
