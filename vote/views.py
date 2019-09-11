from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect
from .models import Questions, Choice


def index(request):
    # we're getting all list order by decending
    latestQuestionList = Questions.objects.order_by('-pub_date')[:8]
    context = {"latestQuestionList": latestQuestionList}
    return render(request, 'vote/index.html', context)


def detail(request, questionId):
    try:
        questionId = Questions.objects.get(pk=questionId)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "vote/detail.html", {"questionId": questionId})


def results(request, questionId):
    # the questionId above should much url <int:questionId>
   # here we find question Id
    id = get_object_or_404(Questions, pk=questionId)
    return render(request, 'vote/results.html', {"id": id})


def vote(request, id):
    # the id above should much url <int:id>
    # here we find question Id
    questionId = get_object_or_404(Questions, pk=id)
    try:
        # here we're storing choice selected by the user
        selectedChoice = questionId.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoestNotExist):
        # if user didn't choice we'll redirect to detail same page and show errors
        return render(request, "vote/detail.html", {"questionId": questionId, "error_message": "you didn't select a choice"})
    else:
        # if the users selects a choice we'll increase vote for that specific choice and save it to the database
        selectedChoice.vote += 1
        selectedChoice.save()
        # finally after saving to the database will will redirect user to results page
        return HttpResponseRedirect(reverse("vote:results", args=(questionId.id,)))
