
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate,login , logout
import os
from django.contrib.auth.models import User
def register(request):
    context = []

    if request.user.is_authenticated == True:
        return redirect(reverse("post_detail:home"))
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            if User.objects.get(username=username):
                context.append('این یوزرنیم استفاده شده ')
        except:
            if password1 == password2:
                user = User.objects.create_user(f'{username}', f"{email}", f"{password1}")
                user.save()
                user1 = authenticate(request, username=f"{username}", password=f"{password1}")
                login(request, user1)
                return redirect(reverse("post_detail:home"))
            else:
                context.append('پسورد ها مشابه نیستند     ')

            # return redirect("post_detail:home")
    return render(request, "account_app/register.html", context={"eroor":context})
def user_login(request):
    context = []
    if request.user.is_authenticated == True:
        return redirect(reverse("post_detail:home"))
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request ,username=f"{username}", password=f"{password}")
        if user is not None:
            login(request,user)
            return redirect(reverse("post_detail:home"))
        else:
            context.append("The username or password is incorrect ! ")
    return render(request, "account_app/login.html")
def user_logout(request):
    logout(request)
    return redirect("post_detail:home")
