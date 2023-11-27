from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):

	email = forms.EmailField(max_length=60, help_text="Required.")

	class Meta:
		model = Account
		fields = ('email','username','password1','password2')

class AccountAuthenticationForm(ModelForm):
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

		#before the form get excute clean method will run
	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")
			
