from django.shortcuts import render, HttpResponse,redirect

def counter(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else: 
        request.session['counter'] =0
    
    return render(request, 'index.html')

# def distroy(request):
#     del request.session['counter']

#     return render(request, 'index.html')


def distroy_sestion(request):
    del request.session['counter']

    return render(request, 'index.html')