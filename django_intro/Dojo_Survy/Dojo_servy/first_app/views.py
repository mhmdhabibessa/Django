from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')


def index2(request):
    name = request.POST['name']
    location = request.POST['location']
    lang= request.POST['fav']
    comment= request.POST['comment']

    context = {
        'name2' : name,
        'location': location,
        'lang' : lang , 
        'comment': comment }
    print(context)
    return render(request, 'result.html',context)
