from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', usercreateview.as_view() , name='user_create'),
    path('login/',Login.as_view() , name='user_login'),
    path('logout/',logout_view, name='user_logout'),

    
    path('list/', userlistview.as_view() , name='user_list'),
    path('details/<int:ide>', detailsConf , name="user_details"),
    path('update/<int:pk>', userupdateview.as_view() , name="user_update"),
    path('delete/<int:pk>', Deleteuser.as_view() , name="user_delete"),
    path('search/', searchuserlistview.as_view(), name='user_search'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ?search=<str:username>