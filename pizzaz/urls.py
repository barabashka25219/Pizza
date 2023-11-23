from django.urls import path, include
from . import views

app_name = 'pizzaz'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzaz_overview', views.pizzaz_overview, name='pizzaz_overview'),
]
