from django.shortcuts import render
from django.http import Http404
from .models import Questions, Choice


def index(request):
    latestQuestionList = Questions.objects.order_by('-pub_date')[:5]
    context = {"latestQuestionList": latestQuestionList}
    return render(request, 'vote/index.html', context)


def detail(request, id):
    try:
        questionId = Questions.objects.get(pk=id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "vote/detail.html", {"questionId": questionId})
