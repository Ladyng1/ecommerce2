from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Product


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter username",
        "class": "form-control"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Enter email",
        "class": "form-control"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control"
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Repeat password",
        "class": "form-control"
    }))


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter username",
        "class": "form-control"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter password",
        "class": "form-control"
    }))


# CRUD
class ProductRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "price", "description",
                  "is_sold", "stock", "image"]

        widgets = {
            "category": forms.Select(attrs={
                "class": "form-control"
            }),

            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "price": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control"
            }),

            "is_sold": forms.RadioSelect(attrs={
                "class": "form-control"
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),

            "stock": forms.TextInput(attrs={
                "class": "form-control"
            }),
        }
