from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField



class Profile(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        pass

    def delete_profile(self):
        pass

    def update_profile(self):
        pass


class Comment(models.Model):
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text

    def save_comment(self):
        pass

    def delete_comment(self):
        pass

    def update_comment(self):
        pass

class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.ForeignKey(Comment, default='')

    def __str__(self):
        return self.image_name

    def save_image(self):
        pass

    def delete_image(self):
        pass

    def update_caption(self):
        pass







