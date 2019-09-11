from django.shortcuts import render

from .models import Questions, Choice


def index(request):
    latestQuestionList = Questions.objects.order_by('-pub_date')[:5]
    context = {"latestQuestionList": latestQuestionList}
    return render(request, 'vote/index.html', context)
