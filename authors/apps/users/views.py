from django.shortcuts import render
from .serializers import RequiredUserSerializer,RegistrationSerializer,UpdateUserSerializer,LoginSerializer
from rest_framework.views import APIView
from .models import Users
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from django.conf import settings
from django.contrib import auth
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import jwt
# Create your views here.
class SingleUserView(APIView):
    """A class to get a single user using uuid"""
    serializer_class = RequiredUserSerializer
    
    def get(self, request, *args, **kwargs):
        incoming_data = request.data
        print(incoming_data)
        # what to filter the users with
        email = incoming_data.get('email')
        #get the single user
        try:
            #single _user
            user = Users.objects.get(email=email)
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
            print("all_users",serializer)
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
        email = incoming_data.get("email")
        user = Users.objects.get(email =email)
        if user:
            serializer = UpdateUserSerializer(user,data=incoming_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data ={"Error":"User to update was not found!!"},status=status.HTTP_409_CONFLICT)
            
class DeleteUserView(APIView):
    def delete(self,request):
        id = request.data.get("uuid")
        
        try:
            user = Users.objects.get(uuid =id)
            user.delete()
            return Response(data ={"msg":"Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response(data ={"Error":"user with those credentials not found!!"},status=status.HTTP_404_NOT_FOUND)
        
class LoginUserView(GenericAPIView):
    serializer_class =LoginSerializer
    def post(self,request):
        incoming_data = request.data
        print("+++++++ hello")
        username = incoming_data.get("username")
        password = incoming_data.get("user_password")
        print("+++++++",username,password)
        user = auth.authenticate(username =username, password=password)
        print("<<<<<",user)
        
        if user:
            auth_token =jwt.encode({"username":user.username},settings.JWT_SECRET_KEY)
            serializer =self.serializer_class(user)
            
            data = {
                "user":serializer.data,
                "token":auth_token,
            }
            return Response(data,status=status.HTTP_200_OK)
        #when not authenticated
        return Response({'details':"Invalid credentials!!"},status=status.HTTP_401_UNAUTHORIZED)
    