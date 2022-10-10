from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    Address = models.CharField(max_length = 200)
    County = models.CharField(max_length = 150)
    State = models.CharField(max_length = 150)
    City = models.CharField(max_length = 150)
    zip_code = models.CharField(max_length = 10)
    title = models.CharField(max_length = 150)
    # date_time = models.DateTimeField(default= datetime.now())
    profile_img = models.FileField()


    def __str__(self):
        return self.title

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created = False,**kwargs):
    if created:
        Token.objects.create(user = instance)

    

