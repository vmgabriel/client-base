"""Module for views"""

# Libraries
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.views.generic.list import ListView

# Forms
from src.clients.forms import (
    SignupForm,
    ExtendClientEditForm,
)

# Models Clients and User
from src.clients.models import (
    Profile,
    User,
)


class ClientDetailView(LoginRequiredMixin, DetailView):
    """user detail view."""
    template_name = 'clients/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'client'


class ClientEditView(LoginRequiredMixin, UpdateView):
    """Client Edit View"""
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    template_name = 'clients/edit.html'
    success_url = reverse_lazy('clients:list')

    def get_object(self) -> Profile:
        """Get object for get obj based into User"""
        user = User.objects.get(username=self.kwargs['username'])
        return self.model.objects.get(user=user)


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
    success_url = reverse_lazy('clients:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    """List of Clients"""
    template_name = 'clients/list.html'
    model = Profile
    paginate_by = 100
