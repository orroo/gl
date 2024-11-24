from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', conducteurcreateview.as_view() , name='conducteur_create'),
    path('list/', conducteurlistview.as_view() , name='conducteur_list'),
    path('details/<int:ide>', detailsConf , name="conducteur_details"),
    path('update/<int:pk>', conducteurupdateview.as_view() , name="conducteur_update"),
    path('delete/<int:pk>', Deleteconducteur.as_view() , name="conducteur_delete"),
    path('search/', searchconducteurlistview.as_view(), name='conducteur_search'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ?search=<str:conducteurname>