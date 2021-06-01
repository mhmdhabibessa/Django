from django.shortcuts import redirect, render,HttpResponse
from books_app.models import *
# Create your views here.
def index(request):
    context={
        'x':Books.objects.all()
            }
    return render(request,"index.html",context)
def addbook(request):
    Books.objects.create(titel=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')
def viewbook(request,id):
    context={
        'book':Books.objects.get(id=id),
        'z':Authors.objects.all()
    }
    
    
    return render(request,"view.html",context)
def authors(request):
    context={
        'x':Authors.objects.all()
    }
    return render(request,"authors.html",context)
def author(request,id):
    x=Authors.objects.get(id=id)
    z=Books.objects.all()
    context={
        'x':x,
        'z':z
    }
    return render(request,"author.html",context)
def addauthor(request):
    Authors.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],notes=request.POST['notes'])
    return redirect('/')
def addbookauthor(request,id):
    x=Authors.objects.get(id=id)
    i=request.POST['id']
    x.author.add(Book.objects.get(id=i))
    return redirect('/authors/'+str(id))
def addauthorbook(request,id):
    x=Book.objects.get(id=id)
    i=request.POST['id']
    x.publishers.add(Authors.objects.get(id=i))
    return redirect('/books/'+str(id))