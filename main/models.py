from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError

import re


def phone_number_validator(value):
    if not re.match(r'(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}', value):
        raise ValidationError(f'{value} is not a valid iran phone number!')


class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    set_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, validators=[phone_number_validator])
    link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.set_name}'
