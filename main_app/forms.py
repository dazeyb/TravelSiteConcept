from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


# Extending this so we have more fields in the signup page
class SignUpForm(UserCreationForm):
    # username = forms.CharField(max_length=100, help_text='')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserProfileForm(forms.ModelForm):         # 5:06

    class Meta:
        model = UserProfile
        fields = ('current_city',)
