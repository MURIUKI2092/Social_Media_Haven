from django.urls import path

from .views import *

urlpatterns = [
    path("comments/create",AddCommentView.as_view(),name="create_comments"),
    path("comments/single",SingleCommentView.as_view(),name="single_comment"),
    path("comments/all",AllCommentsViews.as_view(),name="all_comments"),
    path("comments/update",UpdateCommentView.as_view(),name="update_comment"),
    path("comments/delete",DeleteCommentView.as_view(),name="delete_comment"),
    
]