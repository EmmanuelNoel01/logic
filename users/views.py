from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from .forms import SenderForm
# Create your views here.
# def home(request):

#     return render(request, 'home.html')

def index(request):
  return render(request, 'index.html')


#   def login(request):
#     return render(request,'login.html')

def sender(request):
    if request.method == 'POST':
        form = SenderForm(request.POST)
        if form.is_valid():
            sender = form.save()
            # Do something with the saved sender object
    else:
        form = SenderForm()
    
    return render(request, 'sender.html', {'form': form})

    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Perform any additional actions after successful registration
            return redirect('success')  # Replace 'success' with the URL name of your success page
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})
