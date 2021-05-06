from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.all_books, name='books'),
    path('add_book', views.add_book, name='add-book'),
    path('update_book/<book_id>', views.update_book, name='update-book'),
    path('delete_book/<book_id>', views.delete_book, name='delete-book'),
    path('users', views.all_user, name='users'),
    path('add_user', views.add_user, name='add-user'),
    path('update_user/<user_id>', views.update_user, name='update-user'),
    path('delete_user/<user_id>', views.delete_user, name='delete-user'),
    path('authors', views.all_author, name='authors'),
    path('add_author', views.add_author, name='add-author'),
    path('authors/<author_id>', views.author_book, name='author-book'),
    path('update_author/<author_id>', views.update_author, name='update-author'),
    path('delete_author/<author_id>', views.delete_author, name='delete-author'),
    path('lenders', views.all_lender, name='lenders'),
    path('add_lender', views.add_lender, name='add-lender')
]
