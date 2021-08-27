from django import forms
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["address", "email", "first_name", "id", "last_name", "salary"]


class PasswordForm(forms.Form):
    password=forms.CharField(min_length=6)

#address, date_joined, email, first_name, groups, id, is_active,
# is_staff, is_superuser, last_login, last_name, logentry,
# password, salary, user_permissions, username
