from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(Costumer)
# admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)


@admin.register(LendingInfo)
class LendingInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'book',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
