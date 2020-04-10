from django.db import models
from . import managers

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stemped Model """

    created = models.DeteTimeField(auto_now_add=True)
    updated = models.DeteTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        abstarct = True