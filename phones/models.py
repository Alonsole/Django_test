from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.BigIntegerField(null=True)
    image = models.URLField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, editable=False)

