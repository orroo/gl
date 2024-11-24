from django.shortcuts import render

def default_view(request):
    return render(request, 'default.html')

def choix_view (request):
    return render(request, 'choix.html')

def choix2_view(request):
    return render(request, 'choix2.html')

def welcome_view(request):
    return render(request, 'index.html')