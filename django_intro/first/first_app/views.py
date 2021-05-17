from django.shortcuts import render, HttpResponse,redirect

def root(request):
    return redirect('/blogs')
def index(request):
    return HttpResponse("placeholder to fill later") 
def new(request):
    return  HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')    

def show(request,number):
    return HttpResponse( f'placholder to display number:{number}')
def edit(request,number):
    return HttpResponse( f'placholder to edit bloge number:{number}')

def destroy(request,number):
    return redirect('/blogs/new')     