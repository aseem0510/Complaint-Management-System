from django.shortcuts import redirect, render, HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    return render(request, 'catalog/dashboard.html')

def changePassword(request):
    
    if request.method == "POST":
        
        username = request.POST.get("username")
        currPassword = request.POST.get("currPassword")
        newPassword = request.POST.get("newPassword")
        confPassword = request.POST.get("confPassword")
        
        
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=currPassword)

        if user is not None:
                
            if newPassword == confPassword:
                
                user.set_password(newPassword)
                user.save()
                
                messages.success(request, "Password Change !!")
                return redirect("/catalog/changePassword")
            
            else:
                print("Passwords doesn't match")
        
        else:
            print("Wrong Current Password")
    
    else:
        return render(request, 'catalog/changePassword.html')
