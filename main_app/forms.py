from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


# Extending this so we have more fields in the signup page
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        # 5:06 


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('current_city', 'user_img')
