from django import forms
from Accounts.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction

class userSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username", "full_name")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do\'t match")
        return password1
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user