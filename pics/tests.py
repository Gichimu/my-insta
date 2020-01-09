from django.test import TestCase

from .models import Image, Profile, Comment

class PicsTestClass(TestCase):

    def setUp(self):
        self.test_profile = Profile(photo = 'me.jpg', bio = 'i am a beatiful individual')
        self.test_profile.save()
        self.test_image = Image(image = 'https://ucarecdn.com/b3b62048-ef96-400c-a46d-94cd4bedcf7e/', image_name = 'wow', image_caption = 'nice pic', likes = 2)
        self.test_image.save()
        self.test_comment = Comment(comment_text = 'this is a nice pic')
        self.test_comment.save()

    def test_save_profile(self):
        self.test_image.save_profile()
        self.assertEqual(self.test_profile.photo, 'me.jpg')

