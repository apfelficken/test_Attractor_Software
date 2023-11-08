from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from accounts.forms import UserForm, UserChangeForm


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


class UserAddView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

        next_url = self.request.POST.get('next')
        if next_url:
            return next_url

        return reverse('webapp:article_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/user_update.html'
    form_class = UserChangeForm
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'users/user_password_change.html'

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.request.user.pk})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'users/user_delete.html'
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('accounts:user_list')

    def get_object(self, queryset=None):
        return self.request.user
