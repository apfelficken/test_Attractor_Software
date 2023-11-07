from django.urls import path
from webapp.views import CategoryListView, CategoryAddView, CategoryArticleView, CategoryUpdateView, CategoryDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories_list'),
    path('<int:pk>', CategoryArticleView.as_view(), name='category_detail'),
    path('create/', CategoryAddView.as_view(), name='category_create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
