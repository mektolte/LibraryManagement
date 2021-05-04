from django import forms
from django.forms import ModelForm
from .models import Book


# Book Form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = (
            'isbn',
            'title',
            'author',
            'publisher'
        )
        labels = {
            'isbn': 'ISBN',
            'title': 'Title',
            'author': 'Author',
            'publisher': 'Publisher'
        }
