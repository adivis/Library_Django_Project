from django.db import models
from django.conf import settings
# Create your models here.

class Book (models.Model):
	title = models.CharField(max_length=100)
	author_name = models.CharField(max_length=50)
	ISBN = models.CharField(max_length=20)
	release_date = models.DateField()

	#delete things associate with it but not account
	account_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default="")

	def __str__(self):
		return self.title
