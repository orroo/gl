from django.shortcuts import render
from .forms import RegistrationForm
from django.http import JsonResponse
from .models import Userauth
import logging
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Créer un logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

# def register_page(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')

#             # Vérification de l'existence du nom d'utilisateur
#             if Userauth.objects.filter(username=username).exists():
#                 error_message = f"Le nom d'utilisateur '{username}' est déjà pris."
#                 logger.error(f"Erreur dans le champ 'username': {error_message}")
#                 form.add_error('username', error_message)

#             # Vérification de l'existence de l'email
#             if Userauth.objects.filter(email=email).exists():
#                 error_message = f"L'adresse email '{email}' est déjà associée à un compte."
#                 logger.error(f"Erreur dans le champ 'email': {error_message}")
#                 form.add_error('email', error_message)

#             # Si des erreurs sont ajoutées au formulaire, renvoyer la même page avec erreurs
#             if form.errors:
#                 logger.error("Erreur: Données invalides. Veuillez vérifier le formulaire.")
#                 # return render(request, 'register.html', {'form': form}, status=400)
#             else:
#             # Création de l'utilisateur
#                 user = Userauth.objects.create_user(
#                     username=username,
#                     email=email,
#                     password=form.cleaned_data['password'],
#                     first_name=form.cleaned_data['first_name'],
#                     last_name=form.cleaned_data['last_name']
#                 )
#                 user.save()

#                 # Loguer le succès dans la console
#                 logger.info(f"Le compte de l'utilisateur '{username}' a été créé avec succès.")
#                 return render(request, 'login.html', {'success': "Votre compte a été créé avec succès."}, status=200)

#         # Si le formulaire est invalide, loguer les erreurs du formulaire
#         for field, errors in form.errors.items():
#             logger.error(f"Erreur dans le champ '{field}': {', '.join(errors)}")

#         logger.error("Erreur: Données invalides. Veuillez vérifier le formulaire.")
#         return render(request, 'register.html', {'form': form}, status=400)
#     return render(request, 'register.html', {'form': RegistrationForm()})
class register_page(CreateView): 
    model = Userauth
    template_name='register.html'
    form_class=RegistrationForm
    success_url= reverse_lazy('login_page')