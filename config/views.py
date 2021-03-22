"""View of the Page"""

# Libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect


def home_view(request):
    """Home View page"""
    if request.user.is_authenticated:
        return HttpResponseRedirect('/clients')
    return render(
        request,
        'index.html',
        {
            'user': request.user
        }
    )
