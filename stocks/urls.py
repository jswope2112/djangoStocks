from django.conf.urls import url
from django.contrib import admin
from stocks.views import stock_create, stock_detail, stock_info, stock_update, stock_delete

urlpatterns = [
    url(r'^$', stock_info, name='list'),
    url(r'^create/$', stock_create, name='create'),
    url(r'^detail/$', stock_detail, name='detail'),
    url(r'^update/$', stock_update, name='update'),
    url(r'^delete/$', stock_delete, name='delete'),
]