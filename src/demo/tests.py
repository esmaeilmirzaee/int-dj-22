from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='This is a new test', valid=True)

    def test_post_title(self):
        post = Post.objects.create(title='This is a new test', valid=True)
        self.assertEqual(post.title, 'This is a new test')
