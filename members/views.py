from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):

    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # print(username,password)

        user = authenticate(request, username=username, password=password)   

        if user is not None:
            login(request, user)
            return redirect('krishnart:image-request')
        else:
            messages.success(request,('There was an error, please try again...'))
            return redirect('login')
            

    else:
        print('hi')
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):    
    logout(request)
    # return redirect(request, 'krishnart:index') #login is name field defined in members/urls.py
    return render(request,'index.html')

