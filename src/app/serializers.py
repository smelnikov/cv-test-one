from rest_framework import serializers

from . import models


class Application(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = (
            'id',
            'key',
            'name',
            'custom_data',
            'created'
        )
        read_only_fields = (
            'id',
            'key',
            'created'
        )
