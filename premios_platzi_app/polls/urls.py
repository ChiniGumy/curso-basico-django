from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name="index"),
    #ex: /polls/

    path('<int:question_id>/detail/sdasdasd/aaaa/aaaaa', views.detail, name="detail"),
    #ex: /polls/5/

    path('<int:question_id>/results', views.results, name="results"),
    #ex: /polls/5/results

    path('<int:question_id>/votes', views.votes, name="votes")
    #ex: /polls/5/votes

]
