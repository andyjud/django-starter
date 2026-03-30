from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance

    if not created:
        try:
            email_address = EmailAddress.objects.get(user=user, primary=True)
            if email_address.email != user.email:
                email_address.email = user.email
                email_address.verified = False
                email_address.save()
        except EmailAddress.DoesNotExist:
            # Create EmailAddress if missing
            EmailAddress.objects.create(
                user=user,
                email=user.email,
                primary=True,
                verified=False
            )
        
        
@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()