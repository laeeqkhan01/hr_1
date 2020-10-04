from django.shortcuts import render, get_object_or_404
from django.http      import HttpResponse
from .models          import Worker

# Create your views here.

def homePage(request):
    allWorkers = Worker.objects.all()
    return render(request, 'personnel/homePage.html', {'allWorkers': allWorkers})

def worker_detail(request, pk):
    wrkrDetail = get_object_or_404(Worker, pk=pk)
    return render(request, 'personnel/worker_detail.html', {'wrkrDetail': wrkrDetail})
