from django.urls import path, include
from . import views

app_name = 'pizzaz'

urlpatterns = [
    path('', views.index, name='index'),
]
