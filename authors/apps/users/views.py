from django.shortcuts import render
from .serializers import UserSerializer,RegistrationSerializer,UpdateUserSerializer
from rest_framework.views import APIView
from .models import Users
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
# Create your views here.
class SingleUserView(APIView):
    """A class to get a single user using uuid"""
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        incoming_data = request.data
        print(incoming_data)
        # what to filter the users with
        uuid = incoming_data.get('uuid')
        #get the single user
        try:
            #single _user
            user = Users.objects.get(uuid=uuid)
            if user:
                
                #serialize the user
                serializer_data =self.serializer_class(user)
                return Response(serializer_data.data,status=status.HTTP_200_OK)
            else:
                return Response(data ={"Error":"A User with the uuid {} id not found".format(uuid)},
                            status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(data ={
                'code': 'bad_request',
                'message':"Invalid UUID!!"
            },status=status.HTTP_400_BAD_REQUEST)


class AllUsersView(APIView):
    """ A class to get all users in the database"""
    def get(self, request, *args, **kwargs):
        #get all users
        all_users =Users.objects.all()
        print("+++++",all_users)
        if all_users:
            serializer = UserSerializer(all_users,many=True)
            #return all users after serialization
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data ={"Error":"No users found"},
                            status=status.HTTP_404_NOT_FOUND)
            
class CreateUserView(APIView):
    """A class to create a new user"""
    def post(self, request):
        #get user data 
        incoming_data = request.data
        serializer = RegistrationSerializer(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class UpdateUserView(APIView):
    def put(self, request):
        incoming_data = request.data
        id = incoming_data.get("uuid")
        user = Users.objects.get(uuid =id)
        serializer = UpdateUserSerializer(user,data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DeleteUserView(APIView):
    def delete(self,request):
        id = request.data.get("uuid")
        
        try:
            user = Users.objects.get(uuid =id)
            user.delete()
            return Response(data ={"msg":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response(data ={"Error":"user with those credentials not found!!"},status=status.HTTP_404_NOT_FOUND)