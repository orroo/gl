# catalogue/views.py
from django.shortcuts import render
from .models import Offre
from django.views.generic import ListView, DetailView
from rest_framework import generics
from .serializer import OffreSerializer
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views import View
from django.db import transaction
from .models import Offre
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from conducteurapp.models import *



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

        # Recherche par mot-clé
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        # Filtrage par prix
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        # Tri des offres
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_desc':
            queryset = queryset.order_by('-price')

        return queryset

class OffreDetailView(DetailView):
    model = Offre
    template_name = 'Catalogueapp/Catalogue_detail.html'
    context_object_name = 'offre'
 

from django.shortcuts import render
from django.http import JsonResponse

class BuyOffreView(View):
    def post(self, request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Vous devez être connecté pour acheter cette offre.")
        
        # Retrieve the offer
        print(kwargs['pk'])
        user = request.user
        if isinstance(user, conducteur):
            print("ccccccccc")

        offre = Offre.objects.get(id=kwargs['pk'])
        context = {
                'offre': offre,
                'message': f"Félicitations ! Vous avez acheté l'offre '{offre.title}' avec succès.",
        }
            # Render the success template
        return render(request, 'Catalogueapp/congratulations.html', context)
        
        # try :

        # c=conducteur.objects.get(mail=request.user.mail)
            
        # except conducteur.DoesNotExist:
        #     JsonResponse({'success': False, 'message': "conducteur n'existe pas"}, status=400)




        
        # print(c.nb_jetons-offre.price )
        
        # # Check if the user has enough tokens
        # if c.nb_jetons < offre.price:
        #     return JsonResponse({'success': False, 'message': "Pas assez de jetons"}, status=400)

        # # Process the purchase atomically
        # try:
        #     with transaction.atomic():
        #         # Deduct the price from the user's tokens
        #         request.user.nb_jetons -= offre.price
        #         request.user.save()
                
        #         # Assign the offer's owner to the current user
        #         offre.owner = request.user
        #         offre.save()

        #     # Prepare context for the success page
        #     context = {
        #         'offre': offre,
        #         'message': f"Félicitations ! Vous avez acheté l'offre '{offre.title}' avec succès.",
        #     }
        #     # Render the success template
        #     return render(request, 'Catalogueapp/congratulations.html', context)

        # except Exception as e:
        #     # Handle potential errors
        #     return JsonResponse({'success': False, 'message': f"Une erreur s'est produite: {str(e)}"}, status=500)
