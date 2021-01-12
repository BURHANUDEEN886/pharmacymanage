from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View

from pharmacy.models import Medicine,Booking, MedBook


class IndexView(TemplateView):
    template_name = 'pharmacy/index.html'





