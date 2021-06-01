from django.shortcuts import render, HttpResponse,redirect
from .models import User
def index(request):
    if 'new_user' in request.session:
        return  redirect('/welcom')
    return render(request,'home.html')

           
def login(request):
   
    username = request.POST['username']
    password = request.POST['password']
    users = User.objects.filter(username= username)

    if len(users) == 0 : 
        return redirect('/')

    user = users.first()
    if user.password != password:
        return redirect('/')

    context = {
                'show' : user
        }

        
    return render(request,'welcom.html',context)    




def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    address = request.POST ['address']
    User.objects.create(username = username, password = password, address= address, email  = email)
    data = {
        "username": username,
        "password": password,
        "address" : address,
        "email"   : email
        }
    request.session['new_user'] = data
    return redirect('/welcom')
    

def welcom(request):
    if 'new_user' in request.session:
        username = request.session['new_user']
        return render(request,"welcom.html")

    return redirect("/")

def log_out(request):
    if 'new_user' in request.session:
        request.session.clear()
    return redirect("/")   
