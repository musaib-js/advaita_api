from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view()),
    path('sponsorcontact/', views.SponsorshipContactView.as_view()),
]
