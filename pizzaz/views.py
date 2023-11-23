from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizzaz/index.html')

def pizzaz_overview(request):
    pizzaz = Pizza.objects.order_by('-name')
    return render(request, 'pizzaz/pizzaz_overview.html', context={'pizzaz': pizzaz})