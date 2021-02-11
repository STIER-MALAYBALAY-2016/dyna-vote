from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django.core.validators import ValidationError
from django import forms

MALE = "MALE"
FEMALE = "FEMALE"

GENDER = (
    (MALE, MALE),
    (FEMALE, FEMALE)
)

class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True,label='Email',error_messages={'exists': 'Oops! Email already exist'})
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    phone_no = forms.CharField(required=True,error_messages={'invalid': 'Oops! Invalid Number','invalid_length':'Must 11 digit in length'})
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","first_name","last_name","gender","address","phone_no", "email", "password1", "password2")
        widgets = {
                'gender':forms.Select(choices=GENDER,attrs={'class':'form-control'}),
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

    def clean_contact_number(self):
        if User.objects.filter(phone_no=self.cleaned_data['phone_no']).exists():
            raise ValidationError(self.fields['phone_no'].error_messages['exists'])
        elif not self.cleaned_data['phone_no'].startswith('09'):
            raise ValidationError(self.fields['phone_no'].error_messages['invalid'])
        elif not len(self.cleaned_data['phone_no']) == 11:
            raise ValidationError(self.fields['phone_no'].error_messages['invalid_length'])
        return "+63{}".format(self.cleaned_data['phone_no'][1:11])
