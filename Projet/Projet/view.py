from django.shortcuts import render
from django.http import HttpResponse
def default_view(request):
    return render(request, 'default.html')

def choix_view (request):
    return render(request, 'choix.html')

def choix2_view(request):
    return render(request, 'choix2.html')

def welcome_view(request):
    return render(request, 'index.html')

def my_view(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse("You are logged in!")
    else:
        return HttpResponse("You are not logged in.")