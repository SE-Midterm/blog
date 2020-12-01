from django.test import TestCase
from django.test import Client
from .models import Post


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


class HomePageTest(TestCase):
    def setUp(self):
        Post.objects.create(title='hello blog', content='Homepage Test')

    def test_homepage(self):
        postNum = Post.objects.count()
        self.assertEqual(postNum, 1)

    def tearDown(self):
        post = Post.objects.get(title='hello blog')
        post.delete()


class PostContentTest(TestCase):
    def setUp(self):
        Post.objects.create(title='hello blog', content='Post Content Test')

    def test_content(self):
        c = Client()
        post = Post.objects.first()
        response = c.get('http://127.0.0.1:8000/blog/post/%d/' % post.id)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        post = Post.objects.get(title='hello blog')
        post.delete()


class IntegrationTest(TestCase):
    def test_integration(self):
        c = Client()

        response = c.get('http://127.0.0.1:8000/blog/')
        self.assertEqual(response.status_code, 200)

        response = c.post('http://127.0.0.1:8000/blog/post/',
                          {'title': 'hello blog', 'content': 'blah blah blah'})
        self.assertEqual(Post.objects.count(), 1)

        post = Post.objects.first()
        response = c.get('http://127.0.0.1:8000/blog/post/%d/' % post.id)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        post = Post.objects.get(title='hello blog')
        post.delete()
