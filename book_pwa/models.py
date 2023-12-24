from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ge"


class Review(models.Model):
    RATE_CHOICES = [
        (1, "*"),
        (2, "* *"),
        (3, "* * *"),
        (4, "* * * *"),
        (5, "* * * * *"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    rating = models.CharField(
        max_length=10, choices=RATE_CHOICES, default=RATE_CHOICES[4]
    )  # star rating


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    reviews = models.ManyToManyField(Review)
