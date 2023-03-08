from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #ex: /polls/

    path('<int:question_id>/', views.detail, name="index"),
    #ex: /polls/5/

    path('<int:question_id>/results', views.results, name="index"),
    #ex: /polls/5/results

    path('<int:question_id>/votes', views.votes, name="index")
    #ex: /polls/5/votes

]
