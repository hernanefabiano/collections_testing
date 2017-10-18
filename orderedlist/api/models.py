from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import models


class CarCollection(models.Model):
    color = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    position = models.BigIntegerField()
