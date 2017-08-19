from django.conf.urls import url
from todo import views

urlpatterns = [
    # todo
    url(r'^todo/$', views.todo_list, name='todo_list'),   #
    url(r'^todo/list_no/$', views.todo_list_no, name='todo_list_no'),   #
    url(r'^todo/add/$', views.todo_edit, name='todo_add'),  #
    url(r'^todo/mod/(?P<todo_id>\d+)/$', views.todo_edit, name='todo_mod'),  #
    url(r'^todo/del/(?P<todo_id>\d+)/$', views.todo_del, name='todo_del'),   #
]