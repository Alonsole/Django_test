from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    price = models.BigIntegerField(null=True)
    image = models.CharField()
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField()
    slug = models.SlugField(editable=False)

