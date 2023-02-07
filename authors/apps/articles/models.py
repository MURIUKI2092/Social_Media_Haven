from django.db import models
import uuid
from authors.apps.users.models import Users
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Articles(models.Model):
    id = models.AutoField(primary_key=True,default =1)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    body=models.TextField()
    image_url=models.TextField()
    author=models.ForeignKey(Users,on_delete=models.CASCADE,to_field="uuid")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = ArrayField(models.CharField(max_length=20), default=list)
    flag = models.CharField(max_length=150, default="")
    
    
    class meta:
        db_table = 'articles'
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    


class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Articles,on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    like=models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class meta:
        db_table = 'likes'
    
