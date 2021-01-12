from django.urls import path

from pharmacy.admin_views import IndexView, ApproveView, RejectView, NewUsersView, UsersView, \
    PharmacyView, View_Feedback, AddMedicineView, View_Medicine, UpdateMedicine, RemoveMedicine, PharmacyReg, Medicine_details, View

urlpatterns = [

    path('',IndexView.as_view()),
    path('View',View.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),

    path('newusers',NewUsersView.as_view()),
    path('users',UsersView.as_view()),
    path('pharmacy',PharmacyView.as_view()),
    path('view_feedback',View_Feedback.as_view()),
    path('add_medicine',AddMedicineView.as_view()),
    path('view_medicine',View_Medicine.as_view()),
    path('update',UpdateMedicine.as_view()),
    path('remove',RemoveMedicine.as_view()),
    path('pharmacyreg',PharmacyReg.as_view()),

    path('medicine_details',Medicine_details.as_view()),



]
def urls():
    return (urlpatterns,'admin','admin')