from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pages = models.CharField(max_length=50)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField(max_length=100)

    def __str__(self):
        return self.title + ' - ' + self.author
