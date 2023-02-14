from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

class TestUserOperations(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_user_url='http://127.0.0.1:8000/users/create'
        self.user_data ={
    "first_name":"James",
     "last_name":"Maina", 
     "email":"maina@gmail.com",
     "username":"Maina",
     "user_password":"12345678",
     "phone_number":"07453621774"
}
    print("Haleluhya!!")
        
    def test_create_user(self):
        response = self.client.post(self.post_user_url, data=self.user_data,format='json', follow=True)
        print(response,"response")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)