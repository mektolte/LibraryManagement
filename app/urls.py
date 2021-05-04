from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.all_books, name='books'),
]
