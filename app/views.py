from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def all_books(request):
    book_list = Book.objects.all()
    return render(request, 'app/book_list.html', {
        'book_list': book_list,
    })
