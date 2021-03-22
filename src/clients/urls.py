"""Users URLs."""

# Django
from django.urls import path

# View
from src.clients import views


urlpatterns = [
    # Management
    path(
        route='',
        view=views.ClientListView.as_view(),
        name='list'
    ),
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    # User
    path(
        route='<str:username>/',
        view=views.ClientDetailView.as_view(),
        name='detail'
    ),
    path(
        route='<str:username>/edit/',
        view=views.ClientEditView.as_view(),
        name='edit'
    )
]
