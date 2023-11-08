from django.urls import reverse
from django.test import TestCase
from http import HTTPStatus
from webapp.models import Article, Category
from django.contrib.auth import get_user_model


class ArticleTest(TestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user1 = User.objects.create_user('user1', password='password1')
        self.client.force_login(self.user1)

        self.category = Category.objects.create(
            title='test1'
        )

        self.article = Article.objects.create(
            category=self.category,
            user_id=self.user1,
            title='test_data',
            description='test_data'
        )

    def test_article_create(self):
        data1 = {
            'category': self.category,
            'user_id': self.user1,
            'title': 'test_data1',
            'description': 'test_data1'
        }

        url = reverse('webapp:article_create')
        response = self.client.post(url, data=data1)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_article_update(self):
        data1 = {
            'category': self.category,
            'user_id': self.user1,
            'title': 'test_data2',
            'description': 'lorem'
        }

        url = reverse('webapp:article_update', kwargs={'pk': self.article.pk})
        response = self.client.post(url, data=data1)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_article_list(self):
        url = reverse('webapp:article_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_article_detail(self):
        url = reverse('webapp:article_detail', kwargs={'pk': self.article.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_article_delete(self):
        url = reverse('webapp:article_delete', kwargs={'pk': self.article.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class CategoryTest(TestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user1 = User.objects.create_user('user1', password='password1')
        self.client.force_login(self.user1)

        self.category = Category.objects.create(
            title='test1'
        )

        self.category1 = Category.objects.create(
            title='test2',
            parent_id=self.category
        )

        self.category2 = Category.objects.create(
            title='test5',
            parent_id=self.category
        )

    def test_category_create(self):
        data1 = {
            'title': 'test3',
        }

        data2 = {
            'title': 'test4',
            'parent_id': self.category1
        }

        url = reverse('webapp:category_create')
        response = self.client.post(url, data=data1)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        response1 = self.client.post(url, data=data2)
        self.assertEqual(response1.status_code, HTTPStatus.OK)

    def test_category_update(self):
        data1 = {
            'title': 'test3',
            'parent_id': self.category2
        }

        url = reverse('webapp:category_update', kwargs={'pk': self.category.pk})
        response = self.client.post(url, data=data1)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_category_list(self):
        url = reverse('webapp:categories_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_category_detail(self):
        url = reverse('webapp:category_detail', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_category_delete(self):
        url = reverse('webapp:category_delete', kwargs={'pk': self.category.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
