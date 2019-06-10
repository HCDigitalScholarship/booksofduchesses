from django.shortcuts import render

from .models import Book

# Create your views here.

def index(request):

    books = open('/srv/booksofduchesses/books_app/csvs/books.csv', 'r')
    for line in books:
        line =  line.split(',')
        tmp = Book.objects.create()
        print(line)
        tmp.title = line[0]
        tmp.date_created = line[1]
        tmp.scribes = line[2]
        tmp.illuminators = line[3]
        tmp.digital_version = line[4]
        tmp.save()

    books.close()

    authors = open('/srv/booksofduchesses/books_app/csvs/authors.csv', 'r')
    for line in authors:
        line =  line.split(',')
        tmp = Author.objects.create()
        tmp.name = line[0]
        tmp.save()

    authors.close()

    owners = open('/srv/booksofduchesses/books_app/csvs/owners.csv', 'r')
    for line in owners:
        line =  line.split(',')
        tmp = Owner.objects.create()
        tmp.name = line[0]
        tmp.motto = line[1]
        tmp.symbol = line[2]
        tmp.save()

    owners.close()

    text = open('/srv/booksofduchesses/books_app/csvs/texts.csv', 'r')
    for line in text:
        line =  line.split(',')
        tmp = Text.objects.create()
        tmp.name = line[0]
        tmp.name_eng = line[1]
        tmp.save()

    text.close()
