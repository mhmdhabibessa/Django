from django.shortcuts import render, HttpResponse,request
def index1(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")


def index(request):
    return render(request, second_app/hello.html)    