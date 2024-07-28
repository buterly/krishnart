from django.shortcuts import render, redirect
from krishnart.forms import Drawings as DrawingsForm
from .models import Drawings
import datetime
  

# Create your views here.

def index(request):
    data = {
        'drawings' : Drawings.objects.all()[:5]
    } 
    return render(request, 'index.html', data) 

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html')

def image_request(request):  

    if request.user.is_authenticated:
        if request.method == 'POST':  
            form = DrawingsForm(request.POST, request.FILES)  
            if form.is_valid():  
                drawing = form.save(commit=False)

                drawing.date = datetime.datetime.now(datetime.UTC) 
                drawing.save()

  
            # Getting the current instance object to display in the template  
                img_object = form.instance  
              
                return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
        else:  
            form = DrawingsForm()  
  
        return render(request, 'image_form.html', {'form': form})  

    else:
        return redirect('login')