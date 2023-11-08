from django.urls import path
from api_v1.views import ArticleListAPIView, CategoryListAPIView

app_name = 'api_v1'

urlpatterns = [
    path('article/', ArticleListAPIView.as_view(), name='article_api'),
    path('category/', CategoryListAPIView.as_view(), name='category_api'),
]
