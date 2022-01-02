from django.shortcuts import redirect, render, HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from catalog.models import UserInfo

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
        
        # print(type(email), type(phone), type(idNumber), type(department), type(designation), type(gender), type(category))
        
        temp = request.user
        
        if email != "":
            temp.email = email
            temp.save()
        
        temp1 = temp.detail
        
        if temp is not None:
            
            if phone != "":
                temp1.phone = phone
            
            if idNumber != "":
                temp1.idNumber = idNumber
            
            if department != "":
                temp1.department = department
            
            if designation != "":
                temp1.designation = designation
            
            if gender != "":
                temp1.gender = gender
            
            if category != "":
                temp1.category = category
            
            temp1.save()
            
        else:
            u = UserInfo(phone=phone, idNumber=idNumber, department=department, designation=designation, gender=gender, category=category, user_Id=temp)
            u.save()
        
        messages.success(request, "Profile Updated!!")
        return redirect("/catalog/profile")
    
    else:
        return render(request, "catalog/profile.html")


def NewComplaint(request):
    
    if request.method == "POST":
        
        typeOfComplaint = request.POST.get("typeOfComplaint")
        complaintDetail = request.POST.get("complaintDetail")
        
        print(typeOfComplaint, complaintDetail)
        
        return redirect("/catalog/dashboard")
    
    else:
        return render(request, "catalog/NewComplaint.html")