from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.all_books, name='books'),
    path('add_book', views.add_book, name='add-book'),
    path('update_book/<book_id>', views.update_book, name='update-book'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('Lenders', views.all_lender, name='lender'),
]
