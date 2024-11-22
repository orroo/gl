from django.shortcuts import render

from.models import *
from passagerapp.models import *

from django.views.generic import CreateView , ListView , UpdateView , DeleteView
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

class usercreateview(CreateView): 
    model = user
    template_name='user/form.html'
    form_class=userform
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
    
    user1= user.objects.get(cin=ide)
    
    return render(request,"user/details.html",{"obj":user1})

    

class userupdateview(UpdateView): 
    model = user
    template_name='user/form.html'
    form_class=upuserform
    success_url= reverse_lazy('user_list')



     
     
class Deleteuser(DeleteView):
    
    model=user
    template_name="user/delete.html"
    success_url=reverse_lazy('user_list')


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
