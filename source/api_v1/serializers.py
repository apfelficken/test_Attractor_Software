from rest_framework import serializers
from webapp.models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    user = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = Article
        fields = ['id', 'category', 'user', 'title', 'description', 'image']


class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'parent_category']
