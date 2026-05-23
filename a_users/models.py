from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    display_name = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.username
    
    @property
    def name(self):
        if self.display_name:
            name = self.display_name
        else:
            name = self.username 
        return name
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar.svg')
        return avatar
