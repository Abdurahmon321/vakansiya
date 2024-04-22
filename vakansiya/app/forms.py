from django.contrib.auth.models import User

from . models import UserProfile, Vakansiya, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["firstname", "lastname", "phone", "mobile", "address", "email", "img"]


class UserSignupForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError(_("Parol kamida 8 ta belgidan iborat bo'lishi lozim"))
        return password1

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "from-control"
    }))


class VakansiyaForm(forms.ModelForm):
    class Meta:
        model = Vakansiya
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        fields = ["text"]

