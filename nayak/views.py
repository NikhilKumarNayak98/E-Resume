from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import *
# Create your views here.

def index(request):
    profile=Tbloptions.objects.all()
    experience=Tblcommonmasters.objects.filter(type='experience')
    education=Tblcommonmasters.objects.filter(type='education')
    project=Tblcommonmasters.objects.filter(type='projects')
    award=Tblcommonmasters.objects.filter(type='award')




    allprod={'profile':profile,'experience':experience,'education':education,'myproject':project,'award':award}

    # print(profile)
    return render(request,"MyApp/index.html",allprod)
    # return HttpResponse(experience)
