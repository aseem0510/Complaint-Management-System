from django.shortcuts import render, HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, 'catalog/dashboard.html')

def changePassword(request):
    return render(request, 'catalog/changePassword.html')
