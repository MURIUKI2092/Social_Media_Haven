from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
import json
class TestUserOperations(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_user_url='http://127.0.0.1:8000/users/create'
        self.get_user_url='http://127.0.0.1:8000/users/single'
        self.update_user_url='http://127.0.0.1:8000/users/update'
        self.delete_user_url='http://127.0.0.1:8000/users/delete'
        self.user_data ={
    "first_name":"James",
     "last_name":"Maina", 
     "email":"maina@gmail.com",
     "username":"Maina",
     "user_password":"12345678",
     "phone_number":"07453621774"
}
        self.update_data={
    "first_name":"Jimmy",
     "last_name":"Maina", 
     "email":"maina@gmail.com",
     "username":"Maina",
     "user_password":"12345678",
     "phone_number":"07453621770"
            
        }
        
    def test_create_user(self):
        response = self.client.post(self.post_user_url, data=self.user_data,format='json', follow=True)
        print("++++>>>",json.loads(response.content))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_user(self):
        user = self.client.post(self.post_user_url, data=self.user_data,format='json', follow=True)
        user_data =json.loads(user.content)
        response = self.client.put(self.update_user_url.format(user=user_data), data=self.update_data,format='json',follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_single_user(self):
        user = self.client.post(self.post_user_url, data=self.user_data, format='json', follow=True)
        user_data_ = json.loads(user.content)
        email = user_data_['email']
        print(email)
        request_data = {'email': email}
        response = self.client.get(self.get_user_url, data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_single_user(self):
        user = self.client.post(self.post_user_url, data=self.user_data, format='json', follow=True)
        user_data_ = json.loads(user.content)
        email = user_data_['email']
        print(email)
        request_data = {'email': email}
        response = self.client.delete(self.delete_user_url,data=request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
            