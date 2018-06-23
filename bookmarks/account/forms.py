from django import forms
from django.contrib.auth.models import User
from .models import Profile


# create login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)      # renders an HTML password element


# create registration form
class UserRegistrationForm(forms.ModelForm):

    def __init__(self):
        super(UserRegistrationForm, self).__init__()
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False

    # create password field
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Enter password again')

    class Meta:

        # include username, password, and email field of the User model defined by django
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    # validate the password entries
    def clean_password2(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')

        if User.objects.filter(email=cleaned_data['email']).count() != 0:
            raise forms.ValidationError('User account with that email already exists.')

        return cleaned_data['password2']


# allow user to edit base user class
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# allow users to edit custom user class aka Profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

