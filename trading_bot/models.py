from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userresume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False)
    reasone = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Apikeys(models.Model):
    api_key = models.TextField(null=True,max_length=1000, blank=True,default='hdtlbz2j74tym170')
    api_secret = models.TextField(null=True,max_length=1000, blank=True,default='cdh6zl7tjiokssi1acwt46nft3z6nxx1')
    access_token = models.TextField(null=True,max_length=1000)


    def __str__(self):
        return self.access_token

class User_stock_keys(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    api_key =  models.TextField(null=True,blank=True)
    api_secret = models.TextField(null=True,blank=True)
    access_token = models.TextField(null=True,blank=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile',on_delete=models.CASCADE)
    a_key = models.CharField(max_length=50, null=True,blank=True)



