from django.shortcuts import render

# Create your views here.
def my_view(request):
    
    return render(request, 'index.html')


def my_view_404(request):
    
    return render(request, '404.html')


def my_view_about(request):
    
    return render(request, 'about.html')

def my_view_blog(request):
    
    return render(request, 'blog.html')

def my_view_cars(request):
    
    return render(request, 'cars.html')


def my_view_contact(request):
    
    return render(request, 'contact.html')


def my_view_feature(request):
    
    return render(request, 'feature.html')




def my_view_service(request):
    
    return render(request, 'service.html')


def my_view_team(request):
    
    return render(request, 'team.html')




def my_view_testimonial(request):
    
    return render(request, 'testimonial.html')




def my_view_form(request):
    
    return render(request, 'user/form.html')