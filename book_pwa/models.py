from django.contrib.auth import get_user_model
from django.db import models

from .managers import MyManager

User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Genres"


RATE_CHOICES = [
    ("1", "*"),
    ("2", "* *"),
    ("3", "* * *"),
    ("4", "* * * *"),
    ("5", "* * * * *"),
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    rating = models.CharField(
        max_length=10, choices=RATE_CHOICES, default=RATE_CHOICES[4]
    )  # star rating

    def __str__(self):
        rate = RATE_CHOICES[int(self.rating) - 1]
        return rate[1]


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    reviews = models.ManyToManyField(Review)
    objects = models.Manager()
    admin_books = MyManager()
