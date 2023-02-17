from django.shortcuts import render

# Create your views here.

from .models import Bookmark
from ..users.models import Users
from ..articles.models import Articles
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

class MakeBookmarkView(APIView):
    def get(self, request, *args, **kwargs):
        incoming_data = request.data
        user = incoming_data.get('user_uuid')
        article=incoming_data.get('article_uuid')
        ## check whether the user and the articles exists to record a bookmark
        user =Users.objects.get(uuid=user)
        article=Articles.objects.get(uuid=article)
        if user and article:
            try:
                serializer = bookmarkSerializer(data = incoming_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msg":"success","data":serializer.data},status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
            except Exception as e:
                print("An Error occured while creating a bookmark")
        
        pass