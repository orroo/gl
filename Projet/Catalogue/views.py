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
    
    

'''
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Offre
from conducteurapp.models import conducteur

def acheter_offre(request, offre_id):
    # Vérifie si l'utilisateur est connecté
    if not request.user.is_authenticated:
        messages.error(request, "Vous devez être connecté pour acheter une offre.")
        return redirect('login')  # Redirigez vers la page de connexion

    # Assure-toi que l'utilisateur est un conducteur
    try:
        conducteur_instance = request.user.conducteur
    except AttributeError:
        messages.error(request, "Vous devez être un conducteur pour acheter une offre.")
        return redirect('offre_list')  # Redirige vers la liste des offres

    # Récupère l'offre demandée
    offre = get_object_or_404(Offre, id=offre_id)

    # Vérifie si le conducteur a déjà acheté l'offre
    if offre in conducteur_instance.offres_achetees.all():
        messages.error(request, "Vous avez déjà acheté cette offre.")
        return redirect('offre_detail', offre_id=offre.id)

    # Vérifie si le conducteur a suffisamment de jetons
    if conducteur_instance.nb_jetons < offre.price:
        messages.error(request, "Vous n'avez pas assez de jetons pour acheter cette offre.")
        return redirect('offre_detail', offre_id=offre.id)

    # Déduis le prix de l'offre des jetons du conducteur
    conducteur_instance.nb_jetons -= offre.price
    conducteur_instance.save()

    # Ajoute l'offre à la liste des offres achetées
    conducteur_instance.offres_achetees.add(offre)

    # Message de confirmation
    messages.success(request, f"Félicitations ! Vous avez acheté l'offre '{offre.title}'.")

    return redirect('offre_detail', offre_id=offre.id)
'''
