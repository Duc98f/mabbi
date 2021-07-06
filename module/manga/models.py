from django.db import models
from django.urls import reverse


class TimeStampMixin(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return ""


# Create your models here.
class Manga(TimeStampMixin):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'tbl_manga'

    def __str__(self):
        return self.name


class Chapter(TimeStampMixin):
    name = models.CharField(max_length=255, null=True, blank=True, default='1.')
    manga = models.ForeignKey(Manga, null=True, blank=True, on_delete=models.DO_NOTHING,
                              related_name='chapter')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        db_table = 'tbl_chapter'

    def __str__(self):
        return str(self.name)


class Image(TimeStampMixin):
    image = models.ImageField(null=True, blank=True, upload_to='upload/images/%Y/%m/%d/')

    h = models.FloatField(null=True, blank=True, default=680)
    w = models.FloatField(null=True, blank=True, default=480)
    chapter = models.ForeignKey(Chapter, null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='image')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        db_table = 'tbl_image'

    @staticmethod
    def get_entity_name():
        return 'Image'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
