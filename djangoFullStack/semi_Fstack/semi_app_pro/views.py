
from django.shortcuts import render, HttpResponse,redirect,HttpResponse
from semi_app_pro.models import TVshown ,BlogManager
from django.contrib import messages


  

def show_tow(request,id):
    context = {
        'this_show':TVshown.objects.get(id=id)
    }        
    return render(request,'home.html',context)
def page(request):
    return render(request, 'index.html')

def home_tow(request,id):
    this_show = TVshown.objects.create(title=request.POST['title'],network= request.POST['networke'],relaied_time=request.POST['time'],discripton=request.POST['discripton'])
    
    context = {
        'this_show':this_show
    }
    return redirect('/data',context)
def home(request):
    context = {
        'all_count' : TVshown.objects.all() 
    }
    return render(request,'home.html',context)

def add(request):
    errors = TVshown.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/<int:id>/edit')
    else:
        this_show = TVshown.objects.create(title=request.POST['title'],network= request.POST['networke'],relaied_time=request.POST['time'],discripton=request.POST['discripton'])
    context = {
        'this_show':this_show
    }
    return render(request,'home.html',context)

def data(request):
    return render(request, 'home.html')

def tabels(request):
    context = {
        'all_count' : TVshown.objects.all() 
    }
    return render(request, 'tabel.html',context)    


def edit(request,id):

    # this_show=TVshown.objects.get(id=id)
    # this_show.title = request.POST['title']
    # this_show.network = request.POST['networke']
    # this_show.relaied_time =request.POST['time']
    # this_show.discripton = request.POST['discripton']
    # this_show.save()
    # context = {
    #     'this_show':this_show
    # }  
    context = {
        'this_show':TVshown.objects.get(id=id)
    }
    return render(request, 'update.html',context)

def go_back(request):
    return redirect('/tabels')

def delete(request,id):
    this_show = TVshown.objects.get(id=id)
    this_show.delete()

    return redirect('/tabels')
def update(request,id):
    this_show=TVshown.objects.get(id=id)
    this_show.title = request.POST['title']
    this_show.network = request.POST['networke']
    this_show.relaied_time =request.POST['time']
    this_show.discripton = request.POST['discripton']
    this_show.save()
    # context = {
    #     'this_show':this_show
    # }  

    redirect('/create') 
