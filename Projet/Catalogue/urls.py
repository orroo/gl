'''from django.urls import path,include
from .views import *

urlpatterns = [
    # m1: path('list/', conferenceList, name='conference_list')# name is the name of the url, it must be unique, nhotou ena lena ay haja nheb 3liha
    # m2:
    path('list/', OffreListView.as_view(), name='Offre_list'),
    path('details/<int:pk>', OffreDetailView.as_view(), name='offre_details'),
     
]'''
# catalogue/urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('list', OffreListView.as_view(), name='offre_list'),  # Display list of offers at /catalogue/
    path('details/<int:pk>/',OffreDetailView.as_view(), name='offre_detail'),  # Display details of a specific offer
    path('Offres',Offrelist.as_view(), name='offres_list'),
    path('offre/<int:pk>/buy/', BuyOffreView.as_view(), name='buy_offre'),
]