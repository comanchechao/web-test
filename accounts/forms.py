from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super(SignupForm, self).save(commit=False)
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']
            user.email = cleaned_data['email']

            if commit:
                user.save()

                return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','birth_date')
