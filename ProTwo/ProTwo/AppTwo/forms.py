from django import forms
from django.core import validators
from AppTwo.models import UserProfileInfo
from django.contrib.auth.models import User

# Create your models here.

class UserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')

"""
class NewUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields='__all__'







class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()   #url = models.URLField( unique=True)
    verify_email= forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']

        if email!=vmail:

            raise forms.ValidationError("Emails need to match")
"""
