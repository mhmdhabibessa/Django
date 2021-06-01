# other imports
from django.shortcuts import redirect,render
from .models import users 
# show all of the data from a table
def index(request):
    context = {
    	"all_the_users": users.objects.all()
    }
    return render(request, "index.html", context)

def accec(request):
    newly_created_movie = users(first_name=request.POST['first_name'],
    last_name= request.POST['last_name'],
    email=request.POST['email'],
    age=request.POST['age'])
    newly_created_movie.save()
    return redirect('/')


def show(request,id): 
    context = { 
        
        "num" : users.objects.get(id=id)
        
    }
    return render(request,"index2.html",context)

