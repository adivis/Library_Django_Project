from django.shortcuts import render, redirect
from Book.models import Book
from Book.form import BookForm
from account.models import Account

def home_screen_view(request):

	context = {}
	user = request.user

	if user.is_authenticated:
		books = Book.objects.filter(account_user=user)
		context['books'] = books

	return render(request, "Book/home.html",context)

def form_screen_view(request):
	context = {}
	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form = BookForm(request.POST or None)

	if form.is_valid():
		obj = form.save(commit=False)
		account_user = Account.objects.filter(email=user.email).first()
		obj.account_user = account_user
		obj.save()
		form = BookForm()


	context = {}
	context['form'] = form
	return render(request, "Book/form.html", context)