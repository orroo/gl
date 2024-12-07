from django.shortcuts import render

from.models import *
from django.views.generic import CreateView , ListView , UpdateView , DeleteView
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

class conducteurcreateview(CreateView): 
    model = conducteur
    template_name='conducteur/form.html'
    form_class=cform
    success_url= reverse_lazy('user_login')


class conducteurlistview(ListView): 
    model = conducteur
    template_name='conducteur/list.html'
    context_object_name='list'



# class conducteurDetailview(DetailView):
#     model=conducteur
#     template_name="conducteur/details.html"
#     context_object_name="obj"




def detailsConf(request,ide):
    
    conducteur1= conducteur.objects.get(id=ide)
    
    return render(request,"conducteur/details.html",{"obj":conducteur1})

    

class conducteurupdateview(UpdateView): 
    model = conducteur
    template_name='conducteur/form.html'
    form_class=upcform
    success_url= reverse_lazy('profile')



     
     
class Deleteconducteur(DeleteView):
    
    model=conducteur
    template_name="conducteur/delete.html"
    success_url=reverse_lazy('welcome')


class searchconducteurlistview(ListView): 
    model = conducteur
    template_name='conducteur/list.html'
    context_object_name='list'
    def get_queryset(self):
    #    result = super(searchconducteurlistview, self).get_queryset()
       query = self.request.GET.get('search') 
       print(f"Search query: {query}")
       if query:
          result = conducteur.objects.filter(username__icontains=query)
       else:
           result = None
       return result
