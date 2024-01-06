from django.db import models
from django.contrib.auth.models import User
from re import M

# Create your models here.

class Company(models.Model):
  company = models.CharField(max_length=200)
  bio = models.TextField(max_length=250, null=True, blank=True)

  def __str__(self):
    return self.company

class Advocate(models.Model):
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
  proflePic = models.ImageField(default='default.png', upload_to='Profile_pics' )
  username = models.CharField(max_length=200)
  bio = models.TextField(max_length=250, null=True, blank=True)

  def __str__(self):
    return self.username
  
class Profile(models.Model):
  user = models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
  advocate = models.OneToOneField(Advocate,  on_delete=models.CASCADE, null=True, blank=True)
  proflePic = models.ImageField(default='default.png', upload_to='Profile_pics' )

  def __str__(self):
    if self.user:
       return f'{self.user.username} Profile'
    elif self.advocate:
      return f'{self.advocate.username} Profile'
    else:
      return 'No User'

# return f'{self.user.username} Profile' 
   