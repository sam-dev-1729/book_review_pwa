from django.db import models


class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="admin")
