from django.urls import path
from . import views

  
app_name = 'krishnart'  
urlpatterns = [  
    path("", views.index, name="index"),
    path('upload', views.image_request, name="image-request"),

]
