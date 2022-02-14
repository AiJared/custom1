from django.db.models.signals import post_save
from django.dispatch import receiver

from Accounts.models import User, Teacher, Student

@receiver(post_save, sender=User)
def create_users(sender,instance, created, **kwargs):
    if created:
        if instance.is_student:
            Student.objects.update_or_create(user=instance)
        elif instance.is_teacher:
            Teacher.objects.update_or_create(user=instance)
# Will enable us to create profiles for our users