from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    number = models.DecimalField(max_digits=6, decimal_places=2)


def get_image_filename(instance, filename):
    number = instance.chapter.title
    slug = slugify(number)
    return f'chapter/{slug}-{filename}'


class Images(models.Model):
    chapter = models.ForeignKey(Chapter, default=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

