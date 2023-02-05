from django.urls import path

from .views import *

app_name ="articles"

urlpatterns = [
    path("articles/create",CreateSingleArticleView.as_view(),name="create_articles"),
    path("articles/all",AllArticlesView.as_view(),name="all_articles"),
    
]