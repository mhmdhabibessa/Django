import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect

from . import models
from .models import *



def root(request):
    if 'id' in request.session:
        return redirect('/thoughts')  
    return render(request, "index.html")



def login(request):
    if request.method == 'POST':
        email = request.POST['emaillogin']
        user = models.usercheckexist(email)
        errors = {}
        if user is None:
            errors['login'] = "User with similar email does not exist!"
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            password = request.POST['passwordlogin']
        if user is not None and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            messages.success(request, 'Successfully Logged In!')
            return redirect('/thoughts')  
        else:
            messages.error(request, "Invalid password or email!")
    return redirect('/')


def register(request):
    if request.method == "POST":
        errors = models.User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            firstname = request.POST['firstname']
            lastanme = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            passwordc = request.POST['confirmpassword']
            if password == passwordc:
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user = models.create_user(firstname, lastanme, email, hashed_password)
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                messages.success(request, 'Successfully Registered!')
                return redirect('/thoughts')  
    return redirect('/')


def welcome(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'thoughts.html')


def logout(request):
    request.session.clear()
    return redirect('/')


def thoughts(request):
    if 'id' in request.session:
        context = {
            'thoughts' : models.all_thoughts(),
            'current_user': models.get_user(request.session['id']),
        }
        return render(request, 'thoughts.html', context)
    return redirect('/')


def add_thought(request):
    if request.method == "POST":
        errors = models.Thoughts.objects.thoughts_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/thoughts')
        else:
                thought=  request.POST['thoug']
                user = request.session['id']
                models.new_thought(user, thought)
                return redirect('/')

def details(request, id):
    context = {
        'thought' : models.get_thought(id),
        'current_user': models.get_user(request.session['id']),
    }
    return render(request, 'showthought.html',context)

def like(request, id):
    
    current_user = models.get_user(request.session['id'])
    current_thought = models.get_thought(id)
    models.like(current_thought, current_user)
    return redirect('/thoughts/'+ str(id))

def unlike(request, id):
    
    current_user = models.get_user(request.session['id'])
    current_thought = models.get_thought(id)
    models.unlike(current_thought, current_user)
    return redirect('/thoughts/'+ str(id))

def delete(request, id):
    current_thought = models.get_thought(id)
    current_thought.delete()
    return redirect('/thoughts')
