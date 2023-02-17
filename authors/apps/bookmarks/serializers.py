from rest_framework import serializers
from .models import Bookmark

## all serializers for Bookmark are defined here
class bookmarkSerializer(serializers.Serializer):
    class Meta:
        model=Bookmark
        fields =('user_uuid','article_uuid')