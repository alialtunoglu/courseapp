from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return redirect('index')
def about(request):
    return render(request,'pages/about.html')
def contact(request):
    return render(request,'pages/contact.html')