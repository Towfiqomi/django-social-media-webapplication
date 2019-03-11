from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.user.username} Profile'


# def create_profile(sender, **kwargs):
    # if kwargs['created']:
        # user_profile = Profile.objects.create(user=kwargs['instance'])


# post_save.connect(create_profile, sender=User)


