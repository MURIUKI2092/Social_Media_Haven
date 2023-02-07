from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(db_index=True, unique=True)
    username=models.CharField(db_index=True, max_length=255, unique=True)
    user_password=models.CharField(max_length=255,null = True)
    phone_number =models.CharField(max_length=255,null = True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,unique=True)
    is_active = models.BooleanField(default=True)
    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users, this flag will always be
    # falsed.
    is_staff = models.BooleanField(default=False)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)
    
    class meta:
        db_table = 'users'
    
    def __str__(self):
        return self.email+" "
    # save user password as hash
    def save(self,*args,**kwargs):
        self.user_password = make_password(self.user_password)
        super(Users,self).save(*args,**kwargs)
        
    