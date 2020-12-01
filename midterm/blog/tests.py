from django.test import TestCase
from django.test import Client


class PostingTest(TestCase):
    def test_user_posting(self):
        c = Client()

        response = c.post('http://127.0.0.1:8000/blog/post/',
                          {'title': 'hello blog', 'content': 'Posting Test'})
        self.assertEqual(Post.objects.count(), 1)

    def tearDown(self):
        post = Post.objects.get(title='hello blog')
        post.delete()


class ModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='hello blog', content='Model Test')

    def test_model(self):
        t = Post.objects.count()
        self.assertEqual(t, 1)

    def tearDown(self):
        post = Post.objects.get(title='hello blog')
        post.delete()
