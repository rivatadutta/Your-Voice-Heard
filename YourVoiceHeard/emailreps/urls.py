from django.urls import path

from . import views

app_name = 'emailreps'
urlpatterns = [
    path('', views.index, name='index'),
    #path('emailofficials', views.contact_reps, name='contact_reps'),
    #path('aboutsenators', views.senator_page, name='SenatorPage'),
    #path('aboutreps', views.reps_page, name='RepsPage'),
    path('makeissue', views.make_issue, name='make_issue'),
    path('postissue', views.add_issue, name='post_issue'),
    path('ice', views.ice, name='ice'),
    path('blm', views.blm, name='blm'),
    path('proposeissues', views.proposeissues, name='proposeissues'),
    path('caofficals', views.caofficals, name='caofficals'),
    path('2020elections', views.elections2020, name='2020elections'),
    path('climatechange', views.climatechange, name='climatechange'),
    path('yemen', views.yemen, name='yemen'),
    ]
