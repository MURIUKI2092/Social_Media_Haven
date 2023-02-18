from django.shortcuts import render
from django.db import IntegrityError
# Create your views here.

from .models import Bookmark
from ..users.models import Users
from ..articles.models import Articles
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from ..articles.serializers import GetSingleArticleSerializer
from rest_framework import status
from django.core.exceptions import ValidationError

class MakeBookmarkView(APIView):
    def post(self, request, *args, **kwargs):
        incoming_data = request.data
        user = incoming_data.get('user')
        article = incoming_data.get('article')
        ## check whether the article exists
        print(Articles.objects.get(uuid=article))
        try:
            
            if Articles.objects.filter(uuid = article).exists() and Users.objects.filter(uuid=user):
                ## create the bookmark
                serializer = bookmarkSerializer(data = incoming_data)
                print("+++++++++>>>>>>>",serializer)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({"msg":"invalid data!!"},status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"Msg":" A Bookmark already exists!"})
class GetSingleBookmark(APIView):
    def get(self, request):
        incoming_data = request.data
        uuid= incoming_data.get('uuid')
        ## check whether the bookmark exists
        try:
            bookmark = Bookmark.objects.get(uuid=uuid)
            serializer_data = SingleBookmarkSerializer(bookmark)
            return Response({"msg":"success", "bookmark": serializer_data},status=status.HTTP_200_OK)
            
        except Bookmark.DoesNotExist:
            return Response(data={
                "msg":"Bookmark with those credentials does not exist"
            },status=status.HTTP_404_NOT_FOUND)
            
class DeleteBookMarkedArticle(APIView):
    def delete(self, request):
        incoming_data = request.data
        uuid = incoming_data.get("uuid")
        try:
            bookmark = Bookmark.objects.all()
            bookmark.delete()
            return Response (data ={"msg":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Bookmark.DoesNotExist:
            return Response(data ={"Error":"comment with those credentials not found!!"},status=status.HTTP_404_NOT_FOUND)
        
class GetALLBookMarkedArticles(APIView):
    def get(self, request):
        try:
            bookmarks = Bookmark.objects.all()
            serializer_data = SingleBookmarkSerializer(bookmarks,many=True)
            return Response({"msg":"success","bookmarks":serializer_data.data} ,status=status.HTTP_200_OK)
            
        except Bookmark.DoesNotExist:
            return Response(data ={"Error":"comment with those credentials not found!!"},status=status.HTTP_404_NOT_FOUND)