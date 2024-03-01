from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from acharyaa.models import Contact, Enrollment, MembershipPlan, Gallery
# Create your views here.
def Home (request):
    return render(request, "index.html")

def services (request):
    return render(request, "services.html")

def about (request):
    return render(request, "about.html")

def signup(request):
     if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1 != pass2:
            messages.info(request,"password is not matching")
            return redirect('/signup')
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"PhoneNumber  is Taken")
                return redirect('/signup')
        except Exception:
            pass
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception:
            pass    

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
     
     return render(request,"signup.html")   

def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    return render(request,"handlelogin.html")         

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name, email=email, phonenumber=number, description=desc)
        myquery.save()

        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
    return render(request,"contact.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    context={"Membership":Membership}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        reference=request.POST.get('reference')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipPlan=member,Reference=reference)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')
    return render(request,"enroll.html",context)


def profile (request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    print(posts)
    context={"posts":posts}
    return render(request, "profile.html",context)


def gallery (request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request, "gallery.html",context)



            
         
                               

