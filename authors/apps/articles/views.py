from django.shortcuts import render
from rest_framework.views import APIView
from .models import Articles
from .serializers import CreateArticlesSerializer,GetAllArticlesSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
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
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data ={"Error":"No Articles found"},
                            status=status.HTTP_404_NOT_FOUND)
