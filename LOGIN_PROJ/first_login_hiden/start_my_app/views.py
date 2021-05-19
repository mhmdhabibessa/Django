from django.shortcuts import render, HttpResponse,redirect
def index(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':

        username = request.POST['username] 
        password = request.POST['pass'] 
        if user_name is not "":
            request.session['user_name']  = username 
            return redirect('/welcom')
        return HttpResponse(" yes we are done ")    
    return HttpResponse("test is the best to learn  ")        

def welcom(request): 
    full_name = request.session['user_name']
    return HttpResponse(" welcom " )        
