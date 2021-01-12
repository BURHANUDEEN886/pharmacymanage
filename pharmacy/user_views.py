from unittest.test import loader
from urllib import request

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from pharmacy.models import Medicine, Booking, User_info, Complaint, Pharmacy, MedBook
import datetime


class IndexView(TemplateView):
    template_name = 'user/index.html'



class ViewMedicine(TemplateView):
    template_name = 'user/store.html'
    def get_context_data(self, **kwargs):
        context = super(ViewMedicine,self).get_context_data(**kwargs)
        medicine = Medicine.objects.all()
        context['medicine'] = medicine
        return context

    def post(self, request, *args, **kwargs):
        # template = loader.get_template('user/store.html')
        search = self.request.POST['sr']
        medicine = Medicine.objects.filter(medtype=search)
        # return HttpResponse(template.render({"train": train}))
        return render(request,'user/store.html',{'medicine':medicine})


class Medicine_details(TemplateView):
 template_name = 'user/medicine_details.html'

 def get_context_data(self, **kwargs):
     context = super(Medicine_details, self).get_context_data(**kwargs)
     id = self.request.GET['id']
     context['medicine'] = Medicine.objects.get(pk=id)
     return context





class AddFeedback(TemplateView):
   template_name = 'user/add_feedback.html'

   def post(self, request, *args, **kwargs):
       user = User_info.objects.get(user=self.request.user.id)
       rate = request.POST['rate']
       complaint = request.POST['com']

       co = Complaint()
       co.complaint = complaint
       co.rate = rate
       co.user = user
       co.save()
       return render(request, 'user/index.html', {'message': "Feedback Posted.."})

