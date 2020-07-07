from django.urls import path

from . import views

app_name = 'emailreps'
urlpatterns = [
    path('', views.index, name='index'),
    path('emailofficials', views.contact_reps, name='contact_reps'),
<<<<<<< HEAD
=======
    path('aboutsenators', views.senator_page, name='SenatorPage'),
    path('proposeissues', views.propose_vote_issues, name='propose_vote_issues'),
    path('aboutreps', views.reps_page, name='RepsPage'),
>>>>>>> 3e0fbdd97a75ce9a8b484d76e905e75146a2dd11
]
