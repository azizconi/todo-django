from django.db import models


class User(models.Model):
    title = models.CharField(max_length=255, default="Angelina")
    content = models.TextField(blank=True)
    isPublished = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    # user = models.('User', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name
