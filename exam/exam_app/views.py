from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import*


def index (request):
    
    return render(request,'index.html')

def registration_validation (post_data):
    return models.registration_validation(post_data)

def login_validator(post_data):
    return models.login_validator(post_data)


def regestration(request):
    if request.method == 'POST':   
        first_name=request.POST['first']
        last_name=request.POST['last']
        email=request.POST['email']
        password=request.POST['passwod'] 
        confirm_password=request.POST['cpw']
        errors = models.registration_validation(request.POST)
        if len(errors) > 0:
            request.session["bool"]=True
            request.session["bool1"]=False
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = create_user(first_name, last_name,email,password)
        request.session['id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
    return redirect('/welcome')

def login(request):
    if request.method == 'POST': 
        logemail=request.POST['email']
        logpassword=request.POST['passwod']
        errors = login_validator(request.POST)
        if len(errors) > 0:
            request.session["bool"]=False
            request.session["bool1"]=True
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = get_user(logemail, logpassword)
        if user: 
            request.session['id'] = user.id
            print(request.session['id'])

            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect ('/welcome')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
# def welcome(request):
#     context = {
#         user= request.session
#         'all_user': 
#     }

#     return render(request, 'welcome.html')
def show(request):
    return render(request, 'show.html')


def welcome(request):
    context = {
        'all_thought':Thought.objects.all(),
        'all_user': User.objects.all()
    }


    return render (request,'welcome.html',context)


def add_thro(request):
    u_id = request.session['id']
    user = Thought.objects.get(id=u_id)
    thought=request.POST['thought']
    Thought.objects.create(thought=thought ,user_thought=user)
    return redirect('/welcome')




# def add_book(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         desc = request.POST['desc']
#         models.create_book(title , desc , request.session['id'])
#         return redirect('/welcome')
#     return redirect('/')

# def add_fav(request,book_id):
#     if 'id' in request.session:
#         models.add_fav_book(request.session['id'],book_id)
#         return redirect('/welcome')
#     return redirect('/')
