from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone #make sure to set the timezone 

# Create your models here.
class UserProfile(models.Model):
	# this line links UserProfile to a user model instance
	user = models.OneToOneField(User)
	# here we can add aditional attributes 
	'''
	Includes these attributes:
	Username, Password, Email address, firstname, surname
	'''

class Post(models.Model):
    title = models.CharField(max_length=40)
    link = models.URLField(max_length=120, null = True, default = None)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    show = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)
    user = models.ForeignKey(User, default = 1) # adds a FK

    # this is a custom save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = timezone.now()
        # self.user = user
        if not self.id:
            self.created_at = timezone.now()
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    link = models.URLField(max_length=120, null = True, default = None)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(editable=False)
    show = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)
    user = models.ForeignKey(User) # adds a FK for user 
    post = models.ForeignKey(Post) # adds a FK for th epost it is attached to

    # this is a custom save method
    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        # self.user = user
        if not self.id:
            self.created_at = timezone.now()
        super(Comment, self).save(*args, **kwargs)



