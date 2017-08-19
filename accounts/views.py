from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CustomPasswordChangeForm, CustomUserChangeForm, CustomUserCreationForm


# 
def get_queryset_for_detail_edit_delete(self):
    if self.request.user.is_superuser:
        return User.objects.filter(pk=self.kwargs['pk'])
    else:
        return User.objects.filter(pk=self.request.user.id)


class IndexView(ListView):
    template_name = 'accounts/index.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('id')
        else:
            return User.objects.filter(pk=self.request.user.id)


class NewView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/new.html'
    success_url = './login'


class DetailView(DetailView):
    template_name = 'accounts/detail.html'

    def get_queryset(self):
        return get_queryset_for_detail_edit_delete(self)


class EditView(UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'accounts/edit.html'

    def get_queryset(self):
        return get_queryset_for_detail_edit_delete(self)

    def get_success_url(self):
        return '../' + self.kwargs['pk']


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/edit_password.html'

    def get_success_url(self):
        return '../' + str(self.request.user.id)


class DeleteView(DeleteView):
    template_name = 'accounts/user_confirm_delete.html'
    success_url = '../'

    def get_queryset(self):
        return get_queryset_for_detail_edit_delete(self)