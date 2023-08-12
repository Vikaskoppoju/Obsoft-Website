from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import *
from .models import *
# Create your forms here.


# class NewUserForm(UserCreationForm):

# 	class Meta:
# 		model = Userform
# 		fields = ("username", "email","Designation","DateofJoinning","Biometricid","password")
# 		widgets = {
# 			 'DateofJoinning':DateInput(attrs={'type':'date'}),
			 
# 		}

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()

# from .models import Person

# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ['name', 'age', 'email']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    # active = forms.BooleanField(initial=True, required=False)  # Add "active" field

    class Meta:
        model = CustomUser
        fields = ['username','Designation', 'Biometricid','branch','hod','dept_id', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class LoginForm(AuthenticationForm):
    # You can add custom fields if needed

    class Meta:
        model = CustomUser