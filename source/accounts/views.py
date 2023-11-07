from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from webapp.models import Article
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from accounts.forms import UserForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        articles = self.get_object().articles.all()
        return super().get_context_data(object_list=articles, **kwargs)


class UserAddView(LoginRequiredMixin, CreateView):
    template_name = "users/user_create.html"
    model = User
    form_class = UserForm

    def get_success_url(self):
        return reverse('accounts:user_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/user_update.html'
    form_class = UserForm
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'users/user_delete.html'
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('accounts:user_list')
