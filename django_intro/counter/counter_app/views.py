from django.shortcuts import render, HttpResponse,redirect

def counter(request):
    if 'counter' in request.session:
        counter = request.session.get('counter', 1)
        request.session['counter'] = counter + 1
    return render(request, 'index.html')

   