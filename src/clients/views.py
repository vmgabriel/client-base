"""Module for views"""

# Libraries
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User

# Forms
from src.clients.forms import SignupForm


class ClientDetailView(LoginRequiredMixin, DetailView):
    """user detail view."""

    template_name = 'clients/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        context['posts'] = []
        return context


class LoginView(auth_views.LoginView):
    """login view."""
    template_name = 'clients/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """logout view."""
    template_name = 'clients/logged_out.html'


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'clients/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)
