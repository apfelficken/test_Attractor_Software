from rest_framework.generics import ListAPIView
from api_v1.serializers import ArticleSerializer, CategorySerializer
from webapp.models import Article, Category


class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
