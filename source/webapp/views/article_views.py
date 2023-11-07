from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article/article_list.html'
    context_object_name = 'articles'
    model = Article
    paginate_by = 3


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article/article_detail.html'
    model = Article


class ArticleAddView(LoginRequiredMixin, CreateView):
    template_name = "article/article_create.html"
    model = Article
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:article_list')


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('webapp:article_list')
