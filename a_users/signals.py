from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404


# Creates a Profile when a user signs up
@receiver(post_save, sender=User)       
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user = user,
            email = user.email
        )
        
# Updates the Email on the User when changed in Profile       
@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    if created == False:
        user = get_object_or_404(User, id=profile.user.id)
        user.email = profile.email
        user.save()
        
        
# Updates the Email on the Profile when changed in User        
@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    if created == False:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()