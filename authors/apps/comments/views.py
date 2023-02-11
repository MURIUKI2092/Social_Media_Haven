from django.shortcuts import render
from .models import Comments
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .serializers import  *
# Create your views here.
class SingleCommentView(APIView):
    def get(self,request, *args, **kwargs):
        incoming_data = request.data
        uuid = incoming_data.get("comment_uuid")
        # filter comments with uuid
        try:
            comment = Comments.objects.get(uuid=uuid)
            if comment:
                #serialize the comments
                serializer_data = SingleCommentSerializer(comment)
                return Response({"msg":"Success","Comment":serializer_data.data},status=status.HTTP_200_OK)
            else:
                return Response(data ={"Error":"A comment with the uuid {} id not found".format(uuid)},
                            status=status.HTTP_404_NOT_FOUND)
            
        except ValidationError:
            return Response(data ={
                'code': 'bad_request',
                'message':"Invalid UUID!!"
            },status=status.HTTP_400_BAD_REQUEST)

        
        pass
    
class AllCommentsViews(APIView):
    def get(self, *args, **kwargs):
        comments = Comments.objects.all()
        if comments:
            serializer =SingleCommentSerializer(comments,many=True)
            return Response({"msg":"success","comments":serializer.data} ,status=status.HTTP_200_OK)
        else:
            return Response(data ={"Error":"No Comments found"},
                            status=status.HTTP_404_NOT_FOUND)
        
    
class AddCommentView(APIView):
    def post(self, request,*args, **kwargs):
        incoming_data = request.data
        serializer = CommentSerializer(data = incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"success","data":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UpdateCommentView(APIView):
    def put(self,request, *args, **kwargs):
        incoming_data = request.data
        #get the uuid to update the comment
        uuid = incoming_data.get('uuid')
        comment = Comments.objects.get(uuid=uuid)
        print(comment,"++++++")
        if comment:
            serializer = UpdateCommentSerializer(comment,data=incoming_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Updated successfully","data":serializer.data},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        pass
    
class DeleteCommentView(APIView):
    def delete(self,request, *args, **kwargs):
        incoming_data = request.data
        #get the uuid to delete a comment
        uuid = incoming_data.get('uuid')
        try:
            comment = Comments.objects.get(uuid=uuid)
            comment.delete()
            return Response(data ={"msg":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
            
        except Comments.DoesNotExist:
            return Response(data ={"Error":"comment with those credentials not found!!"},status=status.HTTP_404_NOT_FOUND)