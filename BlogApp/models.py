from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField
# Create your models here.


from smartfields import fields

class Author(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	description = models.CharField(null=True,blank=True,max_length=1000)
	picture = fields.ImageField(default='default/Profile.png',null=True,blank=True,upload_to='profile/')

	linkedin = models.CharField(max_length=500,null=True,blank=True)
	facebook = models.CharField(max_length=500,null=True,blank=True)
	twitter = models.CharField(max_length=500,null=True,blank=True)
	github = models.CharField(max_length=500,null=True,blank=True)
	instagram = models.CharField(max_length=500,null=True,blank=True)
	youtube = models.CharField(max_length=500,null=True,blank=True)

	def __str__(self):
		return f"{self.user.username} Profile"

	class Meta:
		db_table="Author"

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

class Blog(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	dateCreated = models.DateTimeField(auto_now_add=True)

	CATEGORY = (
			('Technology', 'Technology'),
			('Fashion', 'Fashion'),
			('Nature','Nature'),
			('Food','Food'),
			('Travel','Travel'),
			('Music','Music'),
			('Lifestyle','Lifestyle'),
			('Fitness','Fitness'),
			('DIY','DIY'),
			('Sports','Sports'),
			('Finance','Finance'),
			('Political','Political'),
			('Parenting','Parenting'),
			('Business','Business'),
			('Personal','Personal'),
			('Movie','Movie'),
			('Automobile','Automobile'),
			('News','News'),
			('Pet','Pet'),
			('Gaming','Gaming'),
			('Other','Other')
			)

	title = models.CharField(max_length=100)
	category = models.CharField(max_length=50,choices = CATEGORY)
	description = models.CharField(max_length = 100,null=True)
	#content = models.TextField()
	content = RichTextField()
	references = models.CharField(max_length=500,blank=True,null=True)
	likes = models.ManyToManyField(User, related_name='blogpost_like')
	image = fields.ImageField(default='default/Other.jpg',null=True,blank=True,upload_to='blogImage/')

	def __str__(self):
		return self.title
	class Meta:
		db_table = "Blog"



class Subscribers(models.Model):
	email = models.EmailField(max_length=254,unique=True)
	class Meta:
		db_table = "Subscribers"