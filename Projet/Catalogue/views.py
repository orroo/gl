# catalogue/views.py
from django.shortcuts import render
from .models import Offre
from django.views.generic import ListView, DetailView
from rest_framework import generics
from .serializer import OffreSerializer
from django.core.paginator import Paginator
from django.db.models import Q



class Offredetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

class Offrelist(generics.ListCreateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

class OffreListView(ListView):
    model = Offre
    context_object_name = 'list'  # Utilisez 'list' pour correspondre au template
    template_name = 'Catalogueapp/Catalogue_list.html'
    paginate_by = 6  # Nombre d'offres par page
    def get_queryset(self):
        queryset = Offre.objects.all()
        query = self.request.GET.get('q')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class OffreDetailView(DetailView):
    model = Offre
    template_name = 'Catalogueapp/Catalogue_detail.html'
    context_object_name = 'offre'
    
    


