from django.shortcuts import render

from.models import *
from django.views.generic import CreateView , ListView , UpdateView , DeleteView
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

class passagercreateview(CreateView): 
    model = passager
    template_name='passager/form.html'
    form_class=pform
    success_url= reverse_lazy('welcome')


class passagerlistview(ListView): 
    model = passager
    template_name='passager/list.html'
    context_object_name='list'



# class passagerDetailview(DetailView):
#     model=passager
#     template_name="passager/details.html"
#     context_object_name="obj"




def detailsConf(request,ide):
    
    passager1= passager.objects.get(id=ide)
    
    return render(request,"passager/details.html",{"obj":passager1})

    

class passagerupdateview(UpdateView): 
    model = passager
    template_name='passager/form.html'
    form_class=pform
    success_url= reverse_lazy('welcome')



     
     
class Deletepassager(DeleteView):
    
    model=passager
    template_name="passager/delete.html"
    success_url=reverse_lazy('welcome')


class searchpassagerlistview(ListView): 
    model = passager
    template_name='passager/list.html'
    context_object_name='list'
    def get_queryset(self):
    #    result = super(searchpassagerlistview, self).get_queryset()
       query = self.request.GET.get('search') 
       print(f"Search query: {query}")
       if query:
          result = passager.objects.filter(username__icontains=query)
       else:
           result = None
       return result
