from rest_framework import serializers
from .models import Users

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('uuid','username', 'email','is_active')
class LoginSerializer (serializers.ModelSerializer):
    class Meta:
        model=Users
        fields =('username','user_password')
class RequiredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'email')
               
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'email','username','user_password','phone_number')
        
        
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('uuid','first_name', 'last_name', 'email','username','phone_number')
        extra_kwargs = {'uuid': {'read_only': True, 'required': True}}