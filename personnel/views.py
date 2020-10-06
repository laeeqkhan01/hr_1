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

def worker_edit(request, pk):
  # We come here twice, once at the time of rendering/displaying a form filled
  # with data from table[pk], and again after submit button is clicke.
  if request.method == "POST":
    # Get the row from table corresp to this pk
    row = get_object_or_404(Worker, pk=pk)
    # Create a form from the POST values, corresp to above row
    form = WorkerForm(request.POST, instance=row)
    if form.is_valid():
      # Get editable version of the row object
      editable_row_obj = form.save(commit=False)
      if editable_row_obj.age > 100:
        editable_row_obj.age = 100  # Demo editing
      editable_row_obj.save() # Save the row in the table
      return HttpResponse("<h1>Data Saved in DB</h1>")
    else:
      return HttpResponse("<h1>Invalid Data received from the form</h1>")
  else:
    # Get the object from the table corresp to this pk.
    row = get_object_or_404(Worker, pk=pk)
    # Create a form with values from the selected row
    wrkrForm = WorkerForm(instance = row)
    return render(request, 'personnel/wrkrDataForm.html', {'wrkrForm' : wrkrForm})
