from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password']


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
