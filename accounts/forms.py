import copy

from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


username = forms.RegexField(
    max_length = 8,
    min_length = 3,
    regex = r'^[a-z][a-zA-Z0-9]+$',
    error_messages = {
        'invalid': _('please enter your password head as charactor, and please 8-16 charactor.'),
    },
    widget = forms.TextInput(attrs={'placeholder': 'Username'}),
)

password = forms.RegexField(
    max_length = 16,
    min_length = 8,
    regex = r'^[a-zA-Z][a-zA-Z0-9]+$',
    error_messages = {
        'invalid': _('please enter your password head as charactor, and please 3-8 charactor.'),
    },
    widget = forms.PasswordInput,
)

email = forms.EmailField(
    required = True,
    widget = forms.TextInput(attrs={'placeholder': 'Email'}),
)

password1 = copy.deepcopy(password)
password1.widget.attrs['placeholder'] = 'Password'
password2 = copy.deepcopy(password)
password2.widget.attrs['placeholder'] = 'Password (again)'
new_password1 = copy.deepcopy(password)
new_password1.widget.attrs['placeholder'] = 'New Password'
new_password2 = copy.deepcopy(password)
new_password2.widget.attrs['placeholder'] = 'New Password (again)'
old_password = copy.deepcopy(password)
old_password.widget.attrs['placeholder'] = 'Old Password'

def email_duplicate_check(email):
    try:
        User._default_manager.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError(
        'Your address is already existing.'
    )


class CustomUserCreationForm(UserCreationForm):
    username = username
    password1 = password1
    password2 = password2
    email = email

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        return email_duplicate_check(email)


class CustomUserChangeForm(UserChangeForm):
    username = username
    email = email

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
        )

    def clean_email(self):
        user = self.instance      
        email = self.cleaned_data['email']
        if user.email == email:
            return email
        return email_duplicate_check(email)


class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = new_password1
    new_password2 = new_password2
    old_password = old_password