from __future__ import absolute_import, division, print_function, unicode_literals

from rest_framework import serializers

from .models import CarCollection


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCollection
        fields = "__all__"
