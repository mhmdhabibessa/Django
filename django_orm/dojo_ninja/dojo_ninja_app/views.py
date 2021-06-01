from django.shortcuts import render,HttpResponse,redirect
from .models import dojos,ninja

def index(request):

    context = {
        "dojos_count": dojos.objects.all() ,
        'ninjas_count':ninja.objects.all()

     }

   
    return render(request, "index.html", context)

def show(request):

    new_dojos = dojos.objects.create(name=request.POST['name'],city= request.POST['city'],state=request.POST['state'])
    return redirect('/')

    

def show2(request):
    print(request.POST)
    ninja.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],
    dojo_id_ninja = dojos.objects.get(id=request.POST['select']))
    return redirect('/')