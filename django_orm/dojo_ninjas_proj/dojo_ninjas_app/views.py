from django.shortcuts import render,HttpResponse,redirect
from .models import dojos

def index(request):

    context = {
        "dojos_count": dojos.objects.all() 
     }
    return render(request, "index.html", context)

def show(request):

    new_dojos = dojos(name=request.POST['name'],
    city= request.POST['city'],
    state=request.POST['state'])
    new_dojos.save()
    return redirect('/')



