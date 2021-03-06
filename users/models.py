from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(verbose_name='Image', blank=True, null=True, upload_to='profile/',
                                        default='default.jpg')
    phone = models.IntegerField(default='01000000000')

    def __str__(self):
        return 'profile of' + self.user.username
