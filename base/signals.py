from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_user(sender, instance,created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  instance.profile.save()

@receiver(post_save, sender=Advocate)
def create_advocate(sender, instance,created, **kwargs):
  if created:
    AdvocateProfile.objects.create(advocate=instance)


@receiver(post_save, sender=Advocate)
def update_advocate(sender, instance, **kwargs):
   if hasattr(instance, 'advocateprofile'):
     instance.advocateprofile.save()