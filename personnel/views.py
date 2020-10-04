from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Worker

# Create your views here.

def homePage(request):
    allWorkers = Worker.objects.all()
    return render(request, 'personnel/homePage.html', {'allWorkers': allWorkers})
