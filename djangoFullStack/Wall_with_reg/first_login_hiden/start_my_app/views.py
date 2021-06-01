from django.shortcuts import render,redirect
from .models import*
import bcrypt

def index(request):
    if 'new_user' in request.session:
        return  redirect('/welcom')
    return render(request,'home.html')
    
def login(request):
    first_name = request.POST['first_name']
    password = request.POST['password']
    user = User.objects.filter(first_name=first_name).first()
    print(user.password)
    if bcrypt.checkpw(password.encode(), user.password.encode()):
        if 'first' not in request.session:
            request.session['first'] = first_name
        return redirect("/page_one")
    else:
        return redirect('/')
    

def page_one(request):
    data = {
        'x': Book.objects.all()
    }
    return render(request, 'page_one.html',data)


def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    confm_password = request.POST['confm_password']
    if password==confm_password:
        pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user=User.objects.create(first_name = first_name,last_name =last_name , password = pw, email  = email,confm_password=confm_password)
        if 'first' not in request.session:
            request.session['first'] = first_name
            request.session['id'] = user.id
        return redirect('/welcom')

    return redirect("/")   

def welcom(request):
    if 'first' in request.session:
        first_name = request.session['first']
        essa={
            "first_name":first_name
        }
        return render(request,"welcom.html",essa)

    return redirect("/")

def log_out(request):
    request.session.clear()
    return redirect("/")   


def add_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['description'])

    return redirect('page_one')

