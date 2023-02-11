from django.urls import path

from .views import *

app_name = "Users"
urlpatterns = [
    path("users/all",AllUsersView.as_view(),name="all_users"),
    path("users/single",SingleUserView.as_view(),name="single_user"),
    path("users/create",CreateUserView.as_view(),name="create_user"),
    path("users/update",UpdateUserView.as_view(),name="update_user"),
    path("users/delete",DeleteUserView.as_view(),name="delete_user"),
    path("users/login",LoginUserView.as_view(),name="login_user"),
]
