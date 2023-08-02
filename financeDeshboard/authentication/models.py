
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfileManager(models.Manager):
         pass

class UserProfile(models.Model):
         #user = models.OneToOneField(User)
        #  user = models.OneToOneField(User, on_delete=models.CASCADE)
         description = models.CharField(max_length=100, default='')
         city        = models.CharField(max_length=100, default='')
         adress        = models.CharField(max_length=100, default='')
         country     = models.CharField(max_length=100, default='')
         postal_code = models.IntegerField(max_length=100,default=0)
        #  website     = models.URLField(default='')
         phoneNumber = models.IntegerField(default=0)
        #  image       = models.ImageField(upload_to='profile_image' , blank=True)


         def __str__(self):
                 return self.user.username


def createProfile(sender, **kwargs):
         if kwargs['created']:
                 user_profile = UserProfile.objects.created(user=kwargs['instance'])

         post_save.connect(createProfile, sender=User)