from django import forms
from django.forms import ModelForm
from .models import Book, Lender, Author, LendingInfo


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


class LenderForm(ModelForm):
    class Meta:
        model = LendingInfo
        fields = (
            'user',
            'book',
            'checkout',
            'con_before',
            'checkin',
            'con_after',
        )
        labels = {
            'user': 'Member',
            'book': 'Book',
            'checkout': 'Check Out Time | Example: YYYY-MM-DD HH:MM:SS',
            'con_before': 'Condition Before',
            'checkin': 'Check In Time | Example: YYYY-MM-DD HH:MM:SS',
            'con_after': 'Condition After',
        }
