from django.shortcuts import redirect, render, HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# Create your views here.

def dashboard(request):
    return render(request, 'catalog/dashboard.html')

def changePassword(request):
    
    if request.method == "POST":
        
        username = request.POST.get("username")
        currPassword = request.POST.get("currPassword")
        newPassword = request.POST.get("newPassword")
        confPassword = request.POST.get("confPassword")
        
        u = authenticate(username=username, password=currPassword)

        if u is not None:
                
            if newPassword == confPassword:
                
                u.set_password(newPassword)
                u.save()
                
                messages.success(request, "Password Change !!")
                
                return redirect("/catalog/changePassword")
            
            else:
                messages.warning(request, "Passwords doesn't match")
                
                return redirect("/catalog/changePassword")
        
        else:
            messages.warning(request, "Wrong Current Password")
            
            return redirect("/catalog/changePassword")
    
    else:
        
        
        return render(request, 'catalog/changePassword.html')
