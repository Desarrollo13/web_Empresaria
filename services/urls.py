from django.urls import path
from . import views

urlpatterns = [
    # Path de services
  
    path("services/", views.services, name="services"),
    
]
