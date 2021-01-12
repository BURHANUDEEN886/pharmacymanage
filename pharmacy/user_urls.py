from django.urls import path

from pharmacy.user_views import IndexView, ViewMedicine,  \
    Medicine_details, AddFeedback

urlpatterns = [

    path('',IndexView.as_view()),
    path('view_medicine',ViewMedicine.as_view()),
    path('medicine_details',Medicine_details.as_view()),

    path('add_feedback',AddFeedback.as_view()),


]
def urls():
    return urlpatterns,'user','user'