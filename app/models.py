from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lender(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    group = models.ForeignKey(Group, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.isbn


class LendingInfo(models.Model):
    user = models.ForeignKey(Lender, blank=False, null=False, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=False, null=False, on_delete=models.CASCADE)
    checkout = models.TimeField('checkout')
    con_before = models.TextField(blank=True)
    checkin = models.TimeField('checkin')
    con_after = models.TextField(blank=True)

    def __str__(self):
        return self.id
