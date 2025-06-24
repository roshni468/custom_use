from django.shortcuts import render,redirect
from myApp.models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required






# signup page

def signup_page(req):
    if req.method =='POST':
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if password == confirm_password:
            CustomUserModel.objects.create_user(

                username=req.POST.get('username')
                full_name=req.POST.get('full_name')
                email=req.POST.get('email')
                mobile_number=req.POST.get('mobile_number')
                gender=req.POST.get('gender')
                age=req.POST.get('age')
                present_address=req.POST.get('present_address')
                permanent_address=req.POST.get('permanent_address')
                last_education_name=req.POST.get('last_education_name')
                nstitute_name=req.POST.get('institute_name')
                passing_year=req.POST.get('passing_year')
                grade=req.POST.get('grade')
                date_of_birth=req.POST.get('date_of_birth')
                profile_image=req.FIELS.get('profile_image')
                password=password
       

            )
            return redirect("login_page")

    return render(req,"signup_page.html")



# login page

def login_page(req):
    if req.method == 'POST':
        password=req.POST.get('password')
        username=req.POST.get('username')

        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
        return redirect('home_page')

    return render(req,"login_page.html")


# logout
def logout_page(req):
    logout(req)
    return redirect('login_page')


# homepage
def home_page(req):
    
    return render(req,"home_page.html")