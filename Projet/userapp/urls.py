from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404



urlpatterns = [
    path('create/', usercreateview.as_view() , name='user_create'),
    path('login/',Login.as_view() , name='user_login'),
    path('login_face/',login_face, name='login_face'),
    path('logout/',logout_view, name='user_logout'),
    path('profile/' , profile_check , name='profile'),

    
    # path('list/', userlistview.as_view() , name='user_list'),
    path('details/<int:ide>', detailsConf , name="user_details"),
    path('update/<int:pk>', userupdateview.as_view() , name="user_update"),
    path('delete/<int:pk>', Deleteuser.as_view() , name="user_delete"),
    # path('search/', searchuserlistview.as_view(), name='user_search'),


    path('mail/', mail_code , name="mailcode"),
    path('mailing/', mailing , name="mailing"),
    path('reset/', reset_password , name="reset_password"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ?search=<str:username>
handler404 = 'userapp.views.custom_404_view'