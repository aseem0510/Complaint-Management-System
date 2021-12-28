from django.shortcuts import render, redirect
# we have to import redirect to redirect to any desired page.....added manually

# we have to import User model table for registeration...added manually
# we have to import auth for login........added manually
from django.contrib.auth.models import User, auth

# importing it for displaying the message after the successful submission of entries, or for warnings
from django.contrib import messages

# Create your views here.

def registration(request):

    # if request is post then we fetch data and update database
    if request.method == "POST":

        # fetching data from register.html form

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # checking neccessary conditions

        if password1 == password2:

            # checking username already exists or not

            if User.objects.filter(username = username).exists():

                # displaying warning message if user entered already taken Username.
                messages.warning(request, "Username already taken by someone, Please enter Unique Username!!")

                return redirect("registration")

            # checking email already exists or not

            elif User.objects.filter(email=email).exists():

                # displaying warning message if user entered already taken Email.
                messages.warning(request, "This Email is belongs to someone else, Please enter your Unique Email!!")
                
                return redirect("registration")

            else:
                
                # creating new user and save it to database

                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                
                # displaying information message if user is successfully Register themself.
                messages.info(request, "You are Successfully Registered, For better experience with us you can Login with your Id!!")
                
                return redirect("login")

        else:

            # displaying warning message if user entered wrong password in confirm password input.
            messages.warning(request, "It seems that you entered two unmatching passwords, Please carefully enter your details!!")

            return redirect("registration")

                           

    # if request is GET then simply go to register.html form page
    else:
            
        return render(request, 'accounts/registration.html')


def login(request):

    # if request is post then we fetch data and update database

    if request.method == "POST":

        # fetching data from login.html form

        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # checking whether the user with given username and password exists or not

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:

            # if user exists then simply logged-in
            auth.login(request, user)

            # displaying success message if user successfully logged-in
            messages.info(request, "Welcome to CMS, How may we help you!!")
            
            return redirect("/catalog/dashboard")

        else:

            # displaying information message if user enter Invalid Credentials.
            messages.info(request, "Invalid Credentials, Please carefully enter your Credentials!!")
                
            return redirect("login")            


    # if request is GET then simply go to login.html form page
    else:    
        return render(request, 'accounts/login.html')



def logout(request):

    # simply logged-out the user
    auth.logout(request)

    # displaying success message on logout.
    messages.success(request, "You are Successfully logged-out, Thank you!!")
                
    return redirect("/")