from django.shortcuts import render
from .models import boy

# Create your views here.
def index (request):
    ur = boy.objects.all().order_by('-id')
    return render (request,'lov/index.html',{'ur':ur})
