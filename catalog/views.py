from django.shortcuts import redirect, render, HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# Create your views here.

def dashboard(request):
    return render(request, 'catalog/dashboard.html')

"""
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

"""

def profile(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        idNumber = request.POST.get("idNumber")
        department = request.POST.get("department")
        designation = request.POST.get("designation")
        gender = request.POST.get("gender")
        category = request.POST.get("category")
        
        print(email, phone, idNumber, department, designation, gender, category)
        
        return redirect("/catalog/dashboard")
    
    else:
        return render(request, "catalog/profile.html")