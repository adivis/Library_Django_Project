from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.form import RegistrationForm, AccountAuthenticationForm

def registration_view(request):
	context={}

	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email,password=raw_password)
			login(request, account)

			return redirect('home')

		else:
			context['registration_form'] = form

	else:
		#means its a get request and they are visiting registration for the 1st time
		form = RegistrationForm()
		context['registration_form'] = form

	return render(request, 'account/register.html', context)

def logout_view(request):
	logout(request)
	return redirect('home')
	

def login_view(request):
	context = {}
	user = request.user

	#if user is already login no need to go to login screen
	if user.is_authenticated:
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			#if user obj exist it means they are successfully autheticated
			if user:
				login(request, user)
				return redirect('home')

	#haven't attempted to login yet
	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request,'account/login.html', context)


def must_authenticate(request):
	return render(request, 'account/must_authenticate.html',{})