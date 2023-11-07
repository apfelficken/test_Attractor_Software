from django import forms
from webapp.models import Category, Article


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent_id']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'description', 'image']
