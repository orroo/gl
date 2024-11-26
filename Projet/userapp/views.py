from django.shortcuts import render ,redirect

from.models import *
from passagerapp.models import *

from django.views.generic import CreateView , ListView , UpdateView , DeleteView 

from django.contrib.auth.views import LoginView
from .forms import *
from django.urls import reverse_lazy ,reverse
# Create your views here.
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

class usercreateview(CreateView): 
    model = user
    template_name='user/form.html'
    form_class=uform
    success_url= reverse_lazy('user_list')



class userlistview(ListView): 
    model = user
    template_name='user/list.html'
    context_object_name='list'
    def get_queryset(self):
        # Return all users including those from subclasses
        return user.objects.all()



# class userDetailview(DetailView):
#     model=user
#     template_name="user/details.html"
#     context_object_name="obj"


def detailsConf(request,ide):
    
    user1= user.objects.get(id=ide)
    
    return render(request,"user/details.html",{"obj":user1})



@login_required
def profile_check(request):
    if isinstance(request.user , conducteur):
        user1= conducteur.objects.get(id=request.user.id)
        return render(request,"conducteur/details.html",{"obj":user1})
    elif isinstance(request.user , passager):
        user1= passager.objects.get(id=request.user.id)
        return render(request,"conducteur/details.html",{"obj":user1})
    else :
        user1= user.objects.get(id=request.user.id)
        return render(request,"user/details.html",{"obj":user1})

    

class userupdateview(UpdateView): 
    model = user
    template_name='user/form.html'
    form_class=upuserform
    success_url= reverse_lazy('welcome')



     
     
class Deleteuser(DeleteView):
    
    model=user
    template_name="user/delete.html"
    success_url=reverse_lazy('welcome')


class searchuserlistview(ListView): 
    model = user
    template_name='user/list.html'
    context_object_name='list'
    
    def get_queryset(self):
    #    result = super(searchuserlistview, self).get_queryset()
       query = self.request.GET.get('search') 
       print(f"Search query: {query}")
       if query:
          result = user.objects.filter(username__icontains=query)
       else:
           result = None
       return result



    
class Login(LoginView):
    template_name="login.html"
    form_class=loginform
  

# def login_view(request):
#     if request.method == 'POST':
#         form = loginform(request.POST)
#         mail=form.cleaned_data.get('mail')
#         pwd=form.cleaned_data.get('password')
#         userc=user.objects.get(mail=mail)
#         if userc is not None :
#             if u:
#                 # Proceed with successful login actions
#                 return redirect('home')  # Redirect to the homepage or another page
#     else:
#         form = loginform()

#     return render(request, 'login.html', {'form': form})
def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect to a desired page after logout, for example, the home page
    return redirect('home')  # Replace 'home' with your desired URL name or path