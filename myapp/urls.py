from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('price/',views.price,name='price'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('doctor-index/',views.doctor_index,name='doctor-index'),
    path('doctor-about/',views.doctor_about,name='doctor-about'),
    path('doctor-appointment/',views.doctor_appointment,name='doctor-appointment'),
    path('doctor-profile/',views.doctor_profile,name='doctor-profile'),
    path('book-appointment/<int:pk>/',views.book_appointment,name='book-appointment'),
    path('patient-appointment/',views.patient_appointment,name='patient-appointment'),
    path('patient-cancel-appointment/<int:pk>/',views.patient_cancel_appointment,name='patient-cancel-appointment'),
    path('doctor-attend-appointment/<int:pk>/',views.doctor_attend_appointment,name='doctor-attend-appointment'),
    path('doctor-pending-appointment',views.doctor_pending_appointment,name='doctor-pending-appointment'),
    path('doctor-attended-appointment',views.doctor_attended_appointment,name='doctor-attended-appointment'),
    path('doctor-cancelled-appointment',views.doctor_cancelled_appointment,name='doctor-cancelled-appointment'),
    path('patient-view-prescription/<int:pk>/',views.patient_view_prescription,name='patient-view-prescription'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('ajax/validate_email/',views.validate_email,name='validate_email'),
]