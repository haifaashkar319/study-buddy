# from django.shortcuts import render,redirect
# from decimal import Decimal
# from .models import user
# from django.http import HttpResponse
# import bcrypt


# # Create your views here.
# def HomePage(request, *args, **kwargs):
#     #return HttpResponse("<h1> hello world</h1> ")
#     return render(request,"HomePage.html", {})

# def sign_up(request,*args, **kwargs):
#     salt = bcrypt.gensalt()
#     if request.method=='POST':
#         First_Name= request.POST.get('firstName')
#         Last_Name =request.POST.get('lastName')
#         GPA = request.POST.get('gpa')
#         Major=request.POST.get('major')
#         email= request.POST.get('email')
#         phonenumber= request.POST.get('phonenumber')
#         password= request.POST.get('password')
#         password_confirmed= request.POST.get('password-confirmed')
#         user.password = make_password(user.password)
#         # salt = bcrypt.gensalt()
#         # hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

#         if(password!= password_confirmed):
#             return HttpResponse('Password not matching')

#         if (GPA> str(4.3)) :
#             return HttpResponse('Error, GPA is not acceptable bla bla')
#         else:
#              new_user= user(First_Name=First_Name, Last_Name=Last_Name, GPA=GPA, Major="Majorless",email=email, password= password, PhoneNumber= phonenumber) 
#              new_user.save(using='sign_up_pages_db')
             
#              #new_user.save() saves in default db


#     return render (request, "Sign_up.html", {})



# # password = "user_password"
# # salt = bcrypt.gensalt()
# # hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

from django.contrib.auth.hashers import make_password 
from django.shortcuts import render, redirect
from .models import user
from django.http import HttpResponse


def HomePage(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world</h1> ")
    return render(request,"HomePage.html", {})

def sign_up(request, *args, **kwargs):
    if request.method == 'POST':
       
        First_Name = request.POST.get('firstName')
        Last_Name = request.POST.get('lastName')
        GPA = request.POST.get('gpa')
        gender = request.POST.get('selectedGender')
        Major = request.POST.get('major')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        password_confirmed = request.POST.get('password-confirmed')
        

        if password != password_confirmed:
            return HttpResponse('Password not matching')


        hashed_password = make_password(password)

        if float(GPA) > 4.3:
            return HttpResponse('Error, GPA is not acceptable')

        else:
            new_user = user(
            First_Name=First_Name,
            Last_Name=Last_Name,
            GPA=GPA,
            Gender=gender,
            Major=Major,
            email=email,
            password=hashed_password, 
            PhoneNumber=phonenumber
        )
        new_user.save(using='sign_up_pages_db')
        request.session['user_id'] = new_user.id
        return redirect('/feed/')

    

    return render(request, "Sign_up.html", {})
