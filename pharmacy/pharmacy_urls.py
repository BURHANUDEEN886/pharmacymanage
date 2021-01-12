from django.urls import path

from pharmacy.pharmacy_views import IndexView

urlpatterns = [
    path('',IndexView.as_view()),



]

def urls():
    return (urlpatterns,'pharamacy','pharamacy')

