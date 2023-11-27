from django.forms import ModelForm
from Book.models import Book

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title','author_name','ISBN','release_date']
