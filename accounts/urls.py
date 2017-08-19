from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'accounts'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^new$', views.NewView.as_view(), name='new'),
    url(r'^(?P<pk>[0-9]+)$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', login_required(views.EditView.as_view()), name='edit'),
    url(r'^password/edit$', views.CustomPasswordChangeView.as_view(), name='edit_password'),     # login_required is no need
    url(r'^(?P<pk>[0-9]+)/delete$', login_required(views.DeleteView.as_view()), name='delete'),
    url(r'^login$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
]