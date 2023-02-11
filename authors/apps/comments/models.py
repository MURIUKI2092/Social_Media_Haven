from django.db import models
import uuid
from authors.apps.users.models import Users
from authors.apps.articles.models import Articles
# Create your models here.
class Comments(models.Model):
    id = models.AutoField(primary_key=True,default =1)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    user=models.ForeignKey(Users,on_delete=models.CASCADE,to_field="uuid")
    comment_body=models.TextField()
    article =models.ForeignKey(Articles,on_delete=models.CASCADE,to_field="uuid")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
