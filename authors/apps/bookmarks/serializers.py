from rest_framework import serializers
from .models import Bookmark
from ..users.serializers import RequiredUserSerializer
from ..articles.serializers import RequiredArticleSerializer

## all serializers for Bookmark are defined here
class bookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookmark
        fields =('user','article')
class SingleBookmarkSerializer(serializers.Serializer):
    
    class Meta:
        model = Bookmark
        fields ='__all__'
    user = RequiredUserSerializer()
    article = RequiredArticleSerializer()
    
    
        
        
        
    