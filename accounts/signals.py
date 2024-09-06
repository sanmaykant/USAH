from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import ProfessorProfile, StudentProfile

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'professor':
            ProfessorProfile.objects.create(user=instance)
        elif instance.user_type == 'student':
            StudentProfile.objects.create(user=instance)
