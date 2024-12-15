from django.shortcuts import render ,redirect,get_object_or_404

from.models import *
from passagerapp.models import *

from django.views.generic import CreateView , ListView , UpdateView , DeleteView 

from django.contrib.auth.views import LoginView
from .forms import *
from django.urls import reverse_lazy ,reverse
# Create your views here.
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail

import secrets
import string 


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

class usercreateview(CreateView): 
    model = user
    template_name='user/form.html'
    form_class=uform
    success_url= reverse_lazy('user_list')



class userlistview(ListView): 
    model = user
    template_name='user/list.html'
    context_object_name='list'
    def get_queryset(self):
        # Return all users including those from subclasses
        return user.objects.all()



# class userDetailview(DetailView):
#     model=user
#     template_name="user/details.html"
#     context_object_name="obj"





def detailsConf(request,ide):
    
    user1= user.objects.get(id=ide)
    
    return render(request,"user/details.html",{"obj":user1})



@login_required
def profile_check(request):
    if request.user.role== "conducteur":
        user1= conducteur.objects.get(id=request.user.id)
        return render(request,"conducteur/details.html",{"obj":user1})
    elif request.user.role== "passager":
        user1= passager.objects.get(id=request.user.id)
        return render(request,"passager/details.html",{"obj":user1})
    else :
        user1= user.objects.get(id=request.user.id)
        return render(request,"user/details.html",{"obj":user1})

from django.contrib.auth.hashers import make_password
def reset_password(request):
    input_mail = request.GET.get('mail')  # Get the email from the query parameter
    form = resetform()  # Initialize the form (outside the POST block to prevent re-initialization)
    
    if request.method == 'POST':
        form = resetform(request.POST)  # Create a form instance with POST data
        print('post')
        if form.is_valid():
            print("valid")
            try:
                # Get the user by email
                userup = user.objects.get(mail=input_mail)
                userup.password = make_password(form.cleaned_data['password1'])  # Hash the new password
                userup.save()  # Save the updated user
                return redirect('user_login')  # Redirect to login page

            except user.DoesNotExist:
                # If no user is found with that email, return to the form with the same email and no errors
                print('user error')
                return render(request, "reset.html", {"form": form})
            
    print('method')

    # If method is GET or form is invalid, re-render the form
    return render(request, "reset.html", {"form": form})
# def reset_password(request):
#     input_mail = request.GET.get ('mail')
#     if request.method =='POST':
#         form = resetform(request.POST)
#         if form.is_valid() :
#             mail = request.POST.get('MAIL')
#             try : 
#                 userup =user.objects.get(mail=mail)
#                 userup.password = make_password(request.POST.get('password1'))
#                 userup.save()
#                 return redirect('user_login') 
#             except : 
#                 form = resetform()
#                 return render(request,"reset.html",{"form":form,"mail":input_mail})

#     else :
#         form = resetform()
#     return render(request,"reset.html",{"form":form,"mail":input_mail})



def generate_alphanumeric_code(length=6):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(secrets.choice(characters) for _ in range(length))

def mail_code(request):
    input_mail = request.GET.get ('mail')
    code = generate_alphanumeric_code()
    send_mail(
        subject="Subject here",
        message= "Here is your code : "+code,
        from_email="omarriahi2003@gmail.com",
        recipient_list=["orro5aryasora@gmail.com",input_mail],
        fail_silently=False,
    )
    return render(request,"code_check.html",{"vcode":code,"mail":input_mail})


def mailing(request):
    if request.method == 'POST':
        input_mail = request.POST.get ('MAIL')
        print(input_mail)
        # userc=get_object_or_404(user, mail=input_mail)
        # try :
        userc=user.objects.get(mail=input_mail)
        if userc is not None :
            url = reverse('mailcode')  # Reverse the URL name
            url_with_query = f"{url}?mail="+input_mail  # Add the query string
            return redirect(url_with_query)
                # code = generate_alphanumeric_code()
                # send_mail(
                #     subject="Subject here",
                #     message= "Here is your code : "+code,
                #     from_email="omarriahi2003@gmail.com",
                #     recipient_list=[input_mail],
                #     fail_silently=False,
                # )
                # return render(request,"code_check.html",{"vcode":code})
        # except :
            # return render(request,"mail_check.html",{"error":"mail doesn t exist"})
    return render(request,"mail_check.html")






# def login_view(request):
#     if request.method == 'POST':
#         form = loginform(request.POST)
#         mail=form.cleaned_data.get('mail')
#         pwd=form.cleaned_data.get('password')
#         userc=user.objects.get(mail=mail)
#         if userc is not None :
#             if u:
#                 # Proceed with successful login actions
#                 return redirect('home')  # Redirect to the homepage or another page
#     else:
#         form = loginform()

#     return render(request, 'login.html', {'form': form})


class userupdateview(UpdateView): 
    model = user
    template_name='user/form.html'
    form_class=upuserform
    success_url= reverse_lazy('welcome')



     
     
class Deleteuser(DeleteView):
    
    model=user
    template_name="user/delete.html"
    success_url=reverse_lazy('welcome')


class searchuserlistview(ListView): 
    model = user
    template_name='user/list.html'
    context_object_name='list'
    
    def get_queryset(self):
    #    result = super(searchuserlistview, self).get_queryset()
       query = self.request.GET.get('search') 
       print(f"Search query: {query}")
       if query:
          result = user.objects.filter(username__icontains=query)
       else:
           result = None
       return result



    
class Login(LoginView):
    template_name="login.html"
    form_class=loginform
  

# def login_view(request):
#     if request.method == 'POST':
#         form = loginform(request.POST)
#         mail=form.cleaned_data.get('mail')
#         pwd=form.cleaned_data.get('password')
#         userc=user.objects.get(mail=mail)
#         if userc is not None :
#             if u:
#                 # Proceed with successful login actions
#                 return redirect('home')  # Redirect to the homepage or another page
#     else:
#         form = loginform()

#     return render(request, 'login.html', {'form': form})
def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect to a desired page after logout, for example, the home page
    return redirect('home')  # Replace 'home' with your desired URL name or path