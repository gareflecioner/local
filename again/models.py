from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Album(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('album-detail', args=[str(self.id)])

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):

        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):

        return '%s %s' % (self.first_name, self.last_name)
