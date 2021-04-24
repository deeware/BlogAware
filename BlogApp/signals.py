from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Author


@receiver(post_save,sender=User)
def create_author(sender, instance, created, **kwargs):
	if created:
		Author.objects.create(user=instance)
		print('Profile created')

#post_save.connect(create_author,sender=User)

@receiver(post_save,sender=User)
def update_author(sender, instance, created, **kwargs):
	if created == False :
		instance.author.save()
		print('Profile updated')

#post_save.connect(create_author,sender=User)



