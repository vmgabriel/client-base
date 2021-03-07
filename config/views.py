"""View of the Page"""

# Libraries
from django.shortcuts import render


def home_view(request):
    """Home View page"""
    return render(
        request,
        'index.html',
        {
            'user': request.user
        }
    )
