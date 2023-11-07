from django.urls import path, include
from webapp.views import (CategoryListView, CategoryAddView, CategoryArticleView, CategoryUpdateView,
                          CategoryDeleteView, ArticleListView, ArticleDetailView, ArticleAddView, ArticleUpdateView,
                          ArticleDeleteView)

app_name = 'webapp'

category_urls = [
    path('', CategoryListView.as_view(), name='categories_list'),
    path('<int:pk>/', CategoryArticleView.as_view(), name='category_detail'),
    path('create/', CategoryAddView.as_view(), name='category_create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

]

article_urls = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleAddView.as_view(), name='article_create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),

]

urlpatterns = [
    path('category/', include(category_urls)),
    path('', include(article_urls))
]
