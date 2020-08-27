from django.db import models
from django.core.validators import FileExtensionValidator

import uuid
import os


def image_save_path(instance, file_name: str):
    extension = file_name.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return os.path.join('uploads/news/', filename)


class News(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    image = models.ImageField(
        upload_to=image_save_path, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])]
    )
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    subcategory = models.ForeignKey('subcategory.Subcategory', on_delete=models.CASCADE, related_name='news_list')
    views = models.IntegerField()

    def __str__(self):
        return self.title
