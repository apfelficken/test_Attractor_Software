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


class CategoryArticleView(DetailView, MultipleObjectMixin):
    template_name = 'category/category_detail.html'
    model = Category
    paginate_by = 3

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(category=self.get_object())
        context = super(CategoryArticleView, self).get_context_data(object_list=object_list, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
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
