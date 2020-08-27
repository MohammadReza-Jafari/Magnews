from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
