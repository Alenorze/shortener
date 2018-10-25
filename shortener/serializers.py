from rest_framework import serializers

from .models import Url



class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['url', 'short_url']
        