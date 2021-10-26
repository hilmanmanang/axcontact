from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.getContacts, name="contact"),
    path('contact/create/', views.createContact, name="create-contact"),
    path('contact/<str:pk>/update/', views.updateContact, name="update-contact"),
    path('contact/<str:pk>/delete/', views.deleteContact, name="delete-contact"),
    path('contact/<str:pk>', views.getContact, name="contact")
]
