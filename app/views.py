from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import BookForm


# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def all_books(request):
    book_list = Book.objects.all()
    return render(request, 'app/book_list.html', {
        'book_list': book_list,
    })


def add_book(request):
    form = BookForm
    submitted = False

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('books')
        else:
            form = BookForm(request.POST)
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'app/add_book.html', {
        'form': form,
        'submitted': submitted,
    })


def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books')

    return render(request, 'app/update_book.html', {
        'book': book,
        'form': form,
    })


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponse('Deleted')


def all_lender(request):
    lender_list = Lender.objects.all()
    return render(request, 'app/lender_list.html', {
        'lender_list': lender_list,
    })
