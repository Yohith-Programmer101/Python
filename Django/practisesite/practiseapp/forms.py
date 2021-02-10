from django import forms
from .models import PractiseModel

class PractiseForm(forms.ModelForm):
    class Meta:
        model = PractiseModel
        fields = ["title", "description",]

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=200, label="User Name", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", required=True)
    user_name.widget.attrs["class"] = "form-controls is-valid"
    password.widget.attrs["class"] = "form-controls is-valid"