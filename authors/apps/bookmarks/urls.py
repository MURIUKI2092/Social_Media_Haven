from django.urls import path

from .views import *

urlpatterns = [
    path("bookmark/create",MakeBookmarkView.as_view(),name="create_comments"),
    path("bookmark/single",GetSingleBookmark.as_view(),name="single_comment"),
    path("bookmarks/all",GetALLBookMarkedArticles.as_view(),name="all_comments"),
    path("bookmark/delete",DeleteBookMarkedArticle.as_view(),name="delete_comment"),
    
]