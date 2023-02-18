from rest_framework import serializers
from .models import Articles
from ..users.serializers import RequiredUserSerializer

class CreateArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ( 'title', 'description', 'body','image_url', 'author',)
        
class GetAllArticlesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Articles
        fields = '__all__'
        
    author =RequiredUserSerializer()
        
class UpdateArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields=('title','description','body','image_url')
        extra_kwargs = {'uuid': {'read_only': True, 'required': True}}
        
class  RequiredArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articles
        fields =('title','description','body','image_url')