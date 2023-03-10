from django.shortcuts import render
from rest_framework.views import APIView
from .models import Articles
from .serializers import CreateArticlesSerializer,GetAllArticlesSerializer,UpdateArticlesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from ..users.serializers import UserSerializer
# Create your views here.
class CreateSingleArticleView(APIView):
    def post(self, request):
        #get user data
        incoming_data = request.data
        print("+++++",incoming_data)
        serializer = CreateArticlesSerializer(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
         
    
class AllArticlesView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Articles.objects.all()        
        if articles:
            serializer = GetAllArticlesSerializer(articles, many=True)
            return Response({"Articles":serializer.data} ,status=status.HTTP_200_OK)
        else:
            return Response(data ={"Error":"No Articles found"},
                            status=status.HTTP_404_NOT_FOUND)
            
class DeleteArticleView(APIView):
    def delete(self, request):
        incoming_data = request.get_json()
        article_uuid =incoming_data.get("article_uuid")
        if article_uuid:
            try:
                article = Articles.objects.get(uuid=article_uuid)
                article.delete()
                return Response(data ={"msg":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
            except Articles.DoesNotExist:
                return Response(data ={"Error":"Article with that uuid not found!!"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data ={"Error":"Article uuid required"},status=status.HTTP_409_CONFLICT)
            
class UpdateArticleView(APIView):
    def put(self,request):
        incoming_data = request.get_json()
        article_uuid= incoming_data.get("article_uuid") 
        if article_uuid:
            try:
                article = Articles.objects.get(uuid=article_uuid)
                serializer = UpdateArticlesSerializer(article,data=incoming_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data ={"msg":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
            except Articles.DoesNotExist:
                return Response(data ={"Error":"Article with that uuid not found!!"},status=status.HTTP_404_NOT_FOUND)
            
        else:
            return Response(data ={"Error":"Article uuid required"},status=status.HTTP_409_CONFLICT)
