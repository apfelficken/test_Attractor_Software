from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from webapp.forms import CategoryForm
from webapp.models import Category, Article


class CategoryListView(ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    model = Category

    def get_queryset(self):
        return Category.objects.filter(parent_id=None)


class CategoryArticleView(DetailView):
    template_name = 'category/category_detail.html'
    model = Category
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_category = self.get_object()
        child_categories = Category.objects.filter(parent_id=current_category.id)
        articles = Article.objects.filter(category=current_category)
        child_category_articles = Article.objects.filter(category__in=child_categories)

        context['articles'] = articles
        context['child_category_articles'] = child_category_articles

        return context


class CategoryAddView(CreateView):
    template_name = "category/category_create.html"
    model = Category
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('webapp:categories_list')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/category_update.html'
    form_class = CategoryForm
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('webapp:category_detail', kwargs={'pk': self.object.pk})


class CategoryDeleteView(DeleteView):
    template_name = 'category/category_delete.html'
    model = Category
    context_object_name = 'category'
    success_url = reverse_lazy('webapp:categories_list')
