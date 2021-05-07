from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import UserForm, BookForm, AuthorForm, LenderForm


# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def all_books(request):
    book_list = Book.objects.all()
    return render(request, 'app/book_list.html', {
        'book_list': book_list,
    })


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'app/book_detail.html', {
        'book': book,
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
    return redirect('books')


def all_user(request):
    user_list = Lender.objects.all()
    return render(request, 'app/user_list.html', {
        'user_list': user_list,
    })


def add_user(request):
    form = UserForm
    submitted = False

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('users')
        else:
            form = BookForm(request.POST)
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'app/add_user.html', {
        'form': form,
        'submitted': submitted,
    })


def update_user(request, user_id):
    user = Lender.objects.get(pk=user_id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('users')

    return render(request, 'app/update_user.html', {
        'user': user,
        'form': form,
    })


def delete_user(request, user_id):
    user = Lender.objects.get(pk=user_id)
    user.delete()
    return redirect('users')


def all_author(request):
    author_list = Author.objects.all()
    return render(request, 'app/author_list.html', {
        'author_list': author_list,
    })


def author_book(request, author_id):
    author_detail = Author.objects.filter(pk=author_id)
    books = Book.objects.filter(author=author_id)
    return render(request, 'app/author_book.html', {
        'author_detail': author_detail,
        'books': books,
    })


def add_author(request):
    form = AuthorForm
    submitted = False

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('authors')
        else:
            form = AuthorForm(request.POST)
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'app/add_author.html', {
        'form': form,
        'submitted': submitted,
    })


def delete_author(request, author_id):
    user = Author.objects.get(pk=author_id)
    user.delete()
    return redirect('authors')


def update_author(request, author_id):
    user = Author.objects.get(pk=author_id)
    form = AuthorForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('authors')

    return render(request, 'app/update_author.html', {
        'user': user,
        'form': form,
    })


def all_lender(request):
    lender_list = LendingInfo.objects.all()
    return render(request, 'app/lenders.html', {
        'lender_list': lender_list,
    })


def add_lender(request):
    form = LenderForm
    submitted = False

    if request.method == 'POST':
        form = LenderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('lenders')
        else:
            form = LenderForm(request.POST)
            if 'submitted' in request.GET:
                submitted = True

    return render(request, 'app/add_lender.html', {
        'form': form,
        'submitted': submitted,
    })


def delete_lender(request, lender_id):
    user = LendingInfo.objects.get(pk=lender_id)
    user.delete()
    return redirect('lenders')


def update_lender(request, lender_id):
    user = LendingInfo.objects.get(pk=lender_id)
    form = LenderForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('lenders')

    return render(request, 'app/update_lender.html', {
        'user': user,
        'form': form,
    })


def search_bar(request):
    if request.method == "POST":
        searchnav = request.POST['searchnav']
        authors = Author.objects.filter(name__contains=searchnav)
        books = Book.objects.filter(name__contains=searchnav)
        lenders = Lender.objects.filter(name__contains=searchnav)
        return render(request, 'app/searched.html', {
            'searchnav': searchnav,
            'authors': authors,
            'books': books,
            'lenders': lenders,
        })
    else:
        return render(request, 'app/searched.html', {

        })
