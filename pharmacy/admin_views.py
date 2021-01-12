from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

from pharmacy.models import Pharmacy, User_info, Complaint, Medicine, UserType, Booking, MedBook


class IndexView(TemplateView):
    template_name = 'admin/index.html'


    def get_context_data(self, **kwargs):
      context = super(IndexView, self).get_context_data(**kwargs)
      count = MedBook.objects.filter(status='Out of Stock').count()
      context['count'] = count
      return context



class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})


class NewUsersView(TemplateView):
    template_name = 'admin/new_users.html'

    def get_context_data(self, **kwargs):
        context = super(NewUsersView,self).get_context_data(**kwargs)
        student = User_info.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context['user'] =  student
        return context




class UsersView(TemplateView):
    template_name = 'admin/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(UsersView,self).get_context_data(**kwargs)
        student = User_info.objects.filter(user__last_name='1',user__is_staff='0')
        context['user'] =  student
        return context


class PharmacyView(TemplateView):
    template_name = 'admin/pharmacy_list.html'

    def get_context_data(self, **kwargs):
        context = super(PharmacyView,self).get_context_data(**kwargs)
        pharmacy = Pharmacy.objects.filter(user__last_name='1',user__is_staff='1')
        context['pharmacy'] =  pharmacy
        return context

class View_Feedback(TemplateView):
    template_name = 'admin/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(View_Feedback,self).get_context_data(**kwargs)
        feed = Complaint.objects.all()
        context['feed'] =  feed
        return context

class AddMedicineView(TemplateView):
    template_name = 'admin/add_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(AddMedicineView,self).get_context_data(**kwargs)
        pharmacy = Pharmacy.objects.filter(user__last_name='1',user__is_staff='1')
        context['pharmacy'] = pharmacy
        return context

    def post(self,request,*args,**kwargs):
        user = request.POST['pharmacy']
        pharmacy = Pharmacy.objects.get(pk=user)
        medicine = Medicine()
        medicine.user = pharmacy
        medicine.name = request.POST['name']
        medicine.half_date = request.POST['expdate']
        medicine.exp_date = 'Null'
        medicine.description = request.POST['description']
        medicine.medtype = request.POST['type']
        medicine.companyname = request.POST['company']
        medicine.t_quantity = request.POST['qty']

        q = request.POST['qty']
        print(q)
        qt = int(q)/2
        medicine.half_qty = int(qt)
        medicine.image = request.FILES['image']
        medicine.price = request.POST['price']
        medicine.save()

        return render(request,'admin/index.html',{'message':" Medicine Added"})


class View_Medicine(TemplateView):
    template_name = 'admin/view_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(View_Medicine,self).get_context_data(**kwargs)
        medicine = Medicine.objects.all()
        context['medicine'] = medicine
        return context

class Medicine_details(TemplateView):
 template_name = 'admin/medicine_details.html'

 def get_context_data(self, **kwargs):
     context = super(Medicine_details, self).get_context_data(**kwargs)
     id = self.request.GET['id']
     context['medicine'] = Medicine.objects.get(pk=id)
     return context

class UpdateMedicine(TemplateView):
    template_name = 'admin/update_medicine.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateMedicine,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        pharmacy = Pharmacy.objects.filter(user__last_name='1',user__is_staff='1')
        context['pharmacy'] = pharmacy
        context['medicine'] = Medicine.objects.get(pk=id)
        return context

    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        user = request.POST['pharmacy']
        pharmacy = Pharmacy.objects.get(pk=user)
        medicine = Medicine.objects.get(pk=id)
        medicine.name = request.POST['name']
        medicine.description = request.POST['description']
        medicine.medtype = request.POST['type']
        medicine.companyname = request.POST['company']
        medicine.user = pharmacy
        medicine.price = request.POST['price']
        medicine.save()
        return render(request,'admin/index.html',{'message':" Medicine Updated"})
class RemoveMedicine(View):
   def dispatch(self, request, *args, **kwargs):
       id = request.GET['id']
       medicine = Medicine.objects.get(pk=id)
       medicine.delete()
       return render(request,'admin/index.html',{'message':" Medicine  Removed"})


class PharmacyReg(TemplateView):
    template_name = 'admin/add_pharmacy.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name='1',is_staff='1')
             user.save()
             reg = Pharmacy()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "pharmacy"
             usertype.save()
             return redirect('pharmacyreg')
        except:
             messages = "Enter Another Username"
             return render(request,'admin/index.html',{'messages':messages})




