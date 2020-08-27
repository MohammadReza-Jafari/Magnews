from django.db import models


class Subcategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='subcategories')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
