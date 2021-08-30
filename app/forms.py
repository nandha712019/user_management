from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["address", "email", "first_name", "id", "last_name", "salary"]


class PasswordForm(forms.Form):
    old_password = forms.CharField()
    new_password = forms.CharField(min_length=6)
    confirm_password = forms.CharField(min_length=6)
