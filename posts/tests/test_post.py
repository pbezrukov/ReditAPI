import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from posts.models import Post
from posts.serializers import PostSerializer

client = Client()


class GetPostTest(TestCase):
    def setUp(self):
        self.casper = Post.objects.create(text='Casper')
        self.muff = Post.objects.create(text='Muffin')

    def test_get_all_posts(self):
        response = client.get(reverse('post'))
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_one_valid_post(self):
        response = client.get(
            reverse('get_delete_update_post', kwargs={'pk': self.casper.pk}))
        single_post = Post.objects.get(pk=self.casper.pk)
        serializer = PostSerializer(single_post)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data, serializer.data)

    def test_get_one_invalid_post(self):
        response = client.get(
            reverse('get_delete_update_post', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreatePostTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'text': 'gfgfdhjasgfdjashgfdjs'
        }
        self.invalid_data = {
            'post': '321312'
        }

    def test_create_post_valid_data(self):
        response_post = client.post(reverse('post'), data=json.dumps(self.valid_data), content_type='application/json')
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)
        response_get = client.get(reverse('post'))
        get_post = Post.objects.all()
        serializer = PostSerializer(get_post, many=True)
        self.assertEqual(response_get.data['results'], serializer.data)

    def test_create_post_invalid_data(self):
        response_post = client.post(reverse('post'), data=json.dumps(self.invalid_data), content_type='application/json')
        self.assertEqual(response_post.status_code, status.HTTP_400_BAD_REQUEST)
