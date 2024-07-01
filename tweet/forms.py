from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ['text','photo']
        


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
class UserLoginForm(forms.ModelForm):
    password = forms.CharField( widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email','password')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
