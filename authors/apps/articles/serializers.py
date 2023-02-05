from rest_framework import serializers
from .models import Articles

class CreateArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ( 'title', 'description', 'body','image_url', 'author',)
        
class GetAllArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'