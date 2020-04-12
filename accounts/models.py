from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    Image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


#def create_profile(sender, **kwargs):
    #user = kwargs["instance"]
    #if kwargs["created"]:
        #user_profile = UserProfile(user=user)
        #user_profile.save()

#post_save.connect(create_profile,sender = User)
