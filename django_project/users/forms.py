from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile # Imports Profile model from users/models.py

class UserRegisterForm(UserCreationForm): # Inherits from the user creation form
    email = forms.EmailField()

    class Meta: # Nested namespace for configurations.
        model = User # Model that will be affected.
        fields = ['username', 'email', 'password1', 'password2'] # Fields that will be shown on the form stored in a list.

class UserUpdateForm(forms.ModelForm): # Creates additional forms. # Creates model form to work with a specific database model. This is used to update our user model.
    email = forms.EmailField()

    class Meta: # Nested namespace for configurations. Allows update to username and email.
        model = User # Model that will be affected.
        fields = ['username', 'email'] # Fields that will be shown on the form stored in a list.

class ProfileUpdateForm(forms.ModelForm): # Inherits from forms.ModelForm
    
    class Meta: # Allows update to user profile and profile image.
        model = Profile
        fields = ['image']