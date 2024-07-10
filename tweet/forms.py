from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['text', 'photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def check_email(self):
            user_email = self.cleaned_data.get('email')
            if User.objects.filter(email=user_email).exists():
                raise forms.ValidationError('This email is already in use')
            return user_email


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = User
        fields = ('username', 'password')
