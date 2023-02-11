import jwt
from rest_framework import authentication,exceptions
from django.conf import settings
from .models import Users
# handles authentication
class JWTAuthentication(authentication.BaseAuthentication):
    #override authentication
    print("+++++++")
    def authenticate(self,request):
        authentication_data = authentication.get_authorization_header(request)
        print("+++++++>>>>>",authentication_data)
        if not authentication_data:
            return None
        #get token from the request headers
        prefix,token =authentication_data.decode('utf-8').split(' ')
        #decode the token
        print(token,">>>>>>")
        try:
            print(settings.JWT_SECRET_KEY,">>>>>+++++++")
            payload_data =jwt.decode(token,settings.JWT_SECRET_KEY)
            print("$$$$$",payload_data)
            user = Users.objects.get(username=payload_data['username'])
            return(user,token)
        #catch any arising exceptions
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Invalid Token!')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Token Expired!')
        
        return super().authenticate(request)
    