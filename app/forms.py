from django import forms
from django.forms import ModelForm
from .models import Book, Lender, Author


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


class UserForm(ModelForm):
    class Meta:
        model = Lender
        fields = (
            'first_name',
            'last_name',
            'phone',
            'group',
        )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone': 'Phone',
            'group': 'Group',
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = (
            'name',
        )
        labels = {
            'name': 'Author Name',
        }
