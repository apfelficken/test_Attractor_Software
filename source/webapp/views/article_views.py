from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 3


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    model = Article


class ArticleAddView(CreateView):
    template_name = "article/article_create.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('webapp:article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('webapp:article_list')
