from django.shortcuts import redirect, render, HttpResponse

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from catalog.models import UserInfo, ComplaintDetail


# importing for downloading the pdf

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa




# Create your views here.

def dashboard(request):
    
    temp = request.user
    
    comp = ComplaintDetail.objects.filter(user_Key=temp).all()
    
    submitted = 0
    inProgress = 0
    close = 0
    for i in comp:
        
        qq = i.remark
        qq = qq.lower()
        
        if qq == "submitted":
            submitted += 1
        
        elif qq == "in progress":
            inProgress += 1
        
        elif qq == "close":
            close += 1
    
    
    d = {"submitted": submitted, "inProgress": inProgress, "close": close}
        
    return render(request, 'catalog/dashboard.html', {"d": d})

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
        
        try:
            
            temp1 = temp.detail
            
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
            
        except:
            
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
        
        temp = request.user
        
        comp = ComplaintDetail(typeOfComplaint=typeOfComplaint, complaintDetail=complaintDetail, user_Key=temp)
        comp.save()
        
        messages.success(request, "Complaint Submitted!!")
        
        return redirect("/catalog/NewComplaint")
    
    else:
        return render(request, "catalog/NewComplaint.html")


def ComplaintHistory(request):
    
    temp = request.user
    
    comp = ComplaintDetail.objects.filter(user_Key=temp).all()
    
    d = dict()
    for i in comp:
        
        lst = [i.typeOfComplaint, i.complaintDetail, i.remark, i.complaintDate.date()]
        
        temp = dict()
        temp["typeOfComplaint"] = i.typeOfComplaint
        temp["complaintDetail"] = i.complaintDetail
        temp["remark"] = i.remark
        temp["complaintDate"] = i.complaintDate.date()
        
        d[i.id] = temp
        
    
    return render(request, "catalog/ComplaintHistory.html", {"d":d})


def render_pdf_view(request):
    
    # fetching data from database
    
    temp = request.user
    
    comp = ComplaintDetail.objects.filter(user_Key=temp).all()
    
    d = dict()
    for i in comp:
        
        lst = [i.typeOfComplaint, i.complaintDetail, i.remark, i.complaintDate.date()]
        
        temp = dict()
        temp["typeOfComplaint"] = i.typeOfComplaint
        temp["complaintDetail"] = i.complaintDetail
        temp["remark"] = i.remark
        temp["complaintDate"] = i.complaintDate.date()
        
        d[i.id] = temp
    
    
    temp = request.user
    
    # creating pdf
    
    template_path = 'catalog/DownloadPdf.html'
    
    try:
        temp1 = temp.detail
        context = {'d': d, 'temp': temp, 'temp1': temp1}
    
    except:
        context = {'d': d, 'temp': temp}
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    
    # if want only download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    # if display
    response['Content-Disposition'] = 'filename="Complaint.pdf"'
    
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response