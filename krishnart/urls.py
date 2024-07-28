from django.urls import path
from . import views

  
app_name = 'krishnart'  
urlpatterns = [  
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path('upload', views.image_request, name="image-request"),

]
