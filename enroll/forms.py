from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['Name', 'Email', 'Phone', 'Password']
        error_messages = {"Name": {"required": "please give name here"}}
        widgets = {
            'Name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Name.."}),
            'Email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email.."}),
            'Phone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Phone no.."}),
            'Password': forms.PasswordInput(render_value=True, attrs={"class": "form-control", "placeholder": "Enter Password.."}),
        }

    def clean(self):
        cleaned_data = super().clean()
        valpas = self.cleaned_data['Password']
        if len(valpas) < 6:
            raise forms.ValidationError("please enter some big")
