from django.conf.urls.defaults import *
 
import views
 
urlpatterns = patterns('', 
 
    url(r'^list/$', views.hashes_list, name='hashes_list'),  
    url(r'^detail/(?P<id>\d+)/$', views.hashes_detail, name='hashes_detail'),  
    url(r'^new/$', views.hashes_create, name='hashes_create'),  
    url(r'^update/(?P<id>\d+)/$', views.hashes_update, name='hashes_update'),  
    url(r'^delete/(?P<id>\d+)/$', views.hashes_delete, name='hashes_delete'),  
)
