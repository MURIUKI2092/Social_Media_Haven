from rest_framework import serializers
from .models import Comments
from ..users.serializers import RequiredUserSerializer

## All serialzers required for the comments section
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=('comment_body','article','user')
        
class SingleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields ='__all__'
        
    user = RequiredUserSerializer()
    
class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=('comment_body',)        