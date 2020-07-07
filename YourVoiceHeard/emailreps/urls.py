from django.urls import path

from . import views

app_name = 'emailreps'
urlpatterns = [
    path('', views.index, name='index'),
    path('emailofficials', views.contact_reps, name='contact_reps'),
]
