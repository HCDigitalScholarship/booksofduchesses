from django.contrib.gis import admin
from django.contrib.gis.db import models 
from .models import Tag, Author, Owner, DateOwned, Book, Location, Text
from mapwidgets.widgets import GooglePointFieldWidget
from books_app.forms import *


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['name']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = LocationAdminForm
        else:
            self.form = LocationAdminForm
        return super(LocationAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Location, LocationAdmin)


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    autocomplete_fields = ['language', 'author', 'owner','library']


admin.site.register(Book, BookAdmin)


class TextAdmin(admin.ModelAdmin):
    autocomplete_fields = ['book', 'tags']



admin.site.register(Text, TextAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = TagAdminForm
        else:
            self.form = TagAdminForm
        return super(TagAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Tag, TagAdmin)
# Register your models here.


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['book_date']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = OwnerAdminForm
        else:
            self.form = OwnerAdminForm
        return super(OwnerAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Owner, OwnerAdmin)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = AuthorAdminForm
        else:
            self.form = AuthorAdminForm
        return super(AuthorAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Author, AuthorAdmin)


class DateOwnedAdmin(admin.ModelAdmin):
    search_fields =['Date owned']
    autocomplete_fields = ['book_owned']

admin.site.register(DateOwned, DateOwnedAdmin)

class BooksLanguageAdmin(admin.ModelAdmin):
    search_fields = ['books_language']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = BooksLanguageAdminForm
        else:
            self.form = BooksLanguageAdminForm
        return super(BooksLanguageAdmin, self).get_form(request, obj, **kwargs)



admin.site.register(BooksLanguage, BooksLanguageAdmin)
