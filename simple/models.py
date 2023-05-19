from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    summary = models.CharField(max_length=50)
    isbn = models.CharField(max_length=15)

    def __str__(self):
        return self.title