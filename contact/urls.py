from django.urls import path
from . import views

urlpatterns = [
      # path de contacto 
    path("", views.contact, name="contact"),   
   
]
