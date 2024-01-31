from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Book.models import Book

# Register your models here.
class BookAdmin(UserAdmin):
	list_display = ('title', 'author_name', 'ISBN', 'release_date')
	ordering = ["title"]
	search_fields = ('title', 'author_name')
	readonly_fields = ('ISBN', 'release_date')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Book, BookAdmin)