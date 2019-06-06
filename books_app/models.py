from django.db import models
import datetime

# Create your models here.

class Tag(models.Model):
	tag = models.CharField(max_length=200)

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	owner = models.ManyToManyField('Owner', blank=True)
	type = models.CharField(max_length=200)
	date = models.CharField(max_length=30)
	language = models.CharField(max_length=30)
	def __str__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Owner(models.Model):
	name = models.CharField(max_length=200)
	book_date = models.ManyToManyField('DateOwned', blank=True)
	#location = models.CharField(max_length=200) #This can be updated to include a location as a field
	def __str__(self):
		return self.name

class DateOwned(models.Model):
	#owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	#book_owned = models.ForeignKey(Book, on_delete=models.CASCADE)
	dateowned = models.DateTimeField()
