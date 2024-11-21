from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', passagercreateview.as_view() , name='passager_create'),
    path('list/', passagerlistview.as_view() , name='passager_list'),
    path('details/<str:ide>', detailsConf , name="passager_details"),
    path('update/<str:pk>', passagerupdateview.as_view() , name="passager_update"),
    path('delete/<str:pk>', Deletepassager.as_view() , name="passager_delete"),
    path('search/', searchpassagerlistview.as_view(), name='passager_search'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ?search=<str:passagername>