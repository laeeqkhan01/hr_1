from django.shortcuts import render, get_object_or_404, redirect
from django.http      import HttpResponse
from .models          import Worker
from .forms           import WorkerForm

# Create your views here.

def homePage(request):
    allWorkers = Worker.objects.all()
    return render(request, 'personnel/homePage.html', {'allWorkers': allWorkers})

def worker_detail(request, pk):
    wrkrDetail = get_object_or_404(Worker, pk=pk)
    return render(request, 'personnel/worker_detail.html', {'wrkrDetail': wrkrDetail})

def new_worker(request):
  # We come here twice, once at the time of rendering/displaying a blank form
  # and again when the submit button on the form is clicked.
  if request.method == "POST":  # Data received from the filled form
    recvdForm = WorkerForm(request.POST) #Create a form with POST data
    if recvdForm.is_valid():
      # Get the row entry without saving it in the table, so it can be edited.
      newEntry = recvdForm.save(commit=False)
      if newEntry.age > 100:
        newEntry.age = 100  # A demo editing.
      newEntry.save() # Now save in the table
      return redirect('worker_detail', pk=newEntry.pk) # This should match urls.py entry
    else:
      return HttpResponse("-----InValid Form data received -------")
  else: # Display blank form, so user can fill the new worker data
    wrkrForm = WorkerForm() # Create an empty form
    return render(request, 'personnel/wrkrDataForm.html', {'wrkrForm': wrkrForm})
