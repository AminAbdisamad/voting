from django.shortcuts import render

from .models import Questions, Choice


def index(request):
    return render(request, 'polls/index')
