from django.shortcuts import render
from .models import Stations
# Create your views here.
def home(request):
    stations=Stations.objects.filter(is_active=True)
    return render(request,'home.html',{'stations':stations})