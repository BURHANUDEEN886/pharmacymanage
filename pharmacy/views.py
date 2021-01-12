from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

from pharmacy.models import UserType, Pharmacy, User_info

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return redirect('/pharmacy')
            else:
                return render(request,'index.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'index.html',{'message':"Invalid Username or Password"})

class UserReg(TemplateView):
    template_name = 'userregistration.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name='0')
             user.save()
             reg = User_info()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "user"
             usertype.save()
             return redirect('userregistration')
        except:
             messages = "Enter Another Username"
             return render(request,'index.html',{'messages':messages})



