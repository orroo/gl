from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', usercreateview.as_view() , name='user_create'),
    path('list/', userlistview.as_view() , name='user_list'),
    path('details/<str:ide>', detailsConf , name="user_details"),
    path('update/<str:pk>', userupdateview.as_view() , name="user_update"),
    path('delete/<str:pk>', Deleteuser.as_view() , name="user_delete"),
    path('search/', searchuserlistview.as_view(), name='user_search'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ?search=<str:username>