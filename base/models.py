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
  company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
  username = models.CharField(max_length=200)
  bio = models.TextField(max_length=250, null=True, blank=True)
  

  def __str__(self):
    return self.username
      
  
  
class Profile(models.Model):
  user = models.OneToOneField(User,  on_delete=models.CASCADE, null=True, blank=True)
  profilePic = models.ImageField(default='default.png', upload_to='profile_pics' )

  def __str__(self):
    return f'{self.user}'
   
    

class AdvocateProfile(models.Model):
  advocate = models.ForeignKey(Advocate,  on_delete=models.CASCADE, null=True, blank=True)
  profilePic = models.ImageField(default='default.png', upload_to='profile_pics')

  def __str__(self):
    return f'{self.advocate.username}'
 


class AdvocateAll(models.Model):
  advocates = models.ForeignKey(AdvocateProfile, on_delete=models.SET_NULL,null=True, blank=True)
  def __str__(self):
    return str(self.advocates)
   