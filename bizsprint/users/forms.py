
from django import forms

from .models import SignUp
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')



class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=False)
    message = forms.CharField(required=True, widget=forms.Textarea)
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               validators=[must_be_empty]
                               )


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        # if email != verify:
        #     raise forms.ValidationError("Please enter the same email")



class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')

        # if not extension == "com":
        #     raise forms.ValidationError("Please use a valid .com email address")
        # return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # write validation code.
        return full_name
