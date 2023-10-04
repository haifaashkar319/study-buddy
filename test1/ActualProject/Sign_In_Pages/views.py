from django.shortcuts import render, redirect
from .models import user
from django.http import HttpResponse
import bcrypt
from django.contrib import messages
from django.contrib.auth.hashers import check_password 


from django.contrib.auth import authenticate, login


def signIn(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_instance = user.objects.using('sign_up_pages_db').filter(email=email).first()
            if user_instance:
                hashed_password = str(user_instance.password)
                if check_password(password, hashed_password):
                    request.session['user_id'] = user_instance.id
                    return redirect('/feed/')  # Redirect to the feed page
                else:
                    return render(request, "error.html",{})
            else:
                messages.success(request, 'User not found.')
        except user.DoesNotExist:
            return render(request, "error.html",{"user not found"})
    
        if user.email!=email:
            return HttpResponse("User does not exist")
        
    
    return render(request, "sign_in.html", {})



# def signIn(request, *args, **kwargs):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             user_instance = user.objects.using('sign_up_pages_db').filter(email=email).first()
#             if user_instance:
#                 hashed_password = str(user_instance.password)
#                 if check_password(password, hashed_password):
#                     # Authenticate and log in the user
#                     authenticated_user = authenticate(request, email=email, password=password)
#                     if authenticated_user:
#                         login(request, authenticated_user)
#                         return redirect('/feed/')  # Redirect to the feed page on successful login
#                     else:
#                         return render(request, "error.html", {})
#                 else:
#                     return render(request, "error.html", {})
#             else:
#                 messages.success(request, 'User not found.')
#         except user.DoesNotExist:
#             return render(request, "error.html", {"user_not_found": True})

#     return render(request, "sign_in.html", {})


# from django.shortcuts import render, redirect
# from .models import user
# from django.http import HttpResponse
# import bcrypt

# def signIn(request, *args, **kwargs):
#     email = request.POST.get('email')
#     password = request.POST.get('password')

#     try:
#         user_instance = user.objects.using('sign_up_pages_db').get(email=email)
        
#         if str(password) == str(user_instance.password):
#             return render(request, "welcome.html", {})
#         else:
#             return render(request, "error.html", {"error_message": "Password is incorrect"})
    
#     except user.DoesNotExist:
        
#         return render(request, "error.html", {"error_message": "User not found"})

#     return render(request, "sign_in.html", {})
