from django.contrib import admin

# import models
from .models import Book

#########################################################

# Register your models here.

# register Book
admin.site.register(Book)