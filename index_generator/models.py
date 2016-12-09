from django.db import models
from library.models import Library
from sample.models import Sample


class Pool(models.Model):
    name = models.CharField('Name', max_length=200, unique=True)
    libraries = models.ManyToManyField(Library, blank=True)
    samples = models.ManyToManyField(Sample, blank=True)
    size = models.PositiveSmallIntegerField('Pool Size', default=0, blank=True)
    file = models.FileField(upload_to='pools/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name