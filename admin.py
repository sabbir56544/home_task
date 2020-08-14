from django.contrib import admin
from .models import Writer, Book, Publication

admin.site.register(Writer)
admin.site.register(Book)
admin.site.register(Publication)