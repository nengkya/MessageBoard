from django.test import TestCase
from .models import Post
from django.urls import reverse


#create your tests here
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'class PostModelTest(TestCase):')

    def test_text_content(self):
        post = Post.objects.get(id = 1)

        expected_object_name = f'{post.text}'

        self.assertEqual(expected_object_name, 'class PostModelTest(TestCase):')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text = "resp = self.client.get('/')")

    def test_view_url_exist_at_proper_location(self):
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('/home'))
