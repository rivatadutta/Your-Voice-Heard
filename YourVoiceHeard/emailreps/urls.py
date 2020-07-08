from django.urls import path

from . import views

app_name = 'emailreps'
urlpatterns = [
    path('', views.index, name='index'),
    path('emailofficials', views.contact_reps, name='contact_reps'),
    path('aboutsenators', views.senator_page, name='SenatorPage'),
    path('proposeissues', views.propose_vote_issues, name='propose_vote_issues'),
    path('aboutreps', views.reps_page, name='RepsPage'),
    path('makeissue', views.make_issue, name='make_issue'),
    path('postissue', views.add_issue, name='post_issue'),
]
