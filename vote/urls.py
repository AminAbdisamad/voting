from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    # Home page for the app
    path('', views.index, name='index'),
    # detail specifc question detail page with id
    path('<int:questionId>', views.detail, name='detail'),
    # results page
    path('<int:questionId>/results', views.results, name='results'),
    # voting
    path('<int:id>/vote', views.vote, name='vote')
]
