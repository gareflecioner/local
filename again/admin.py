from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Album

admin.site.register(Album)
admin.site.register(Author)
admin.site.register(Genre)
