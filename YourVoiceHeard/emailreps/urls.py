from django.urls import path

from . import views

app_name = 'emailreps'
urlpatterns = [
    path('', views.index, name='index'),
    path('ice', views.ice, name='ice'),
    path('blm', views.blm, name='blm'),
    path('proposeissues', views.proposeissues, name='proposeissues'),
    path('climatechange', views.climatechange, name='climatechange'),
    path('yemen', views.yemen, name='yemen'),
    ]
