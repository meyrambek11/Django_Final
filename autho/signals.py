from django.db.models.signals import post_save
from django.dispatch import receiver

from autho.models import User, Profile


@receiver(post_save, sender=User)
def post_save_user(sender, instance: User, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=instance)
