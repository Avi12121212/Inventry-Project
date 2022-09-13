import random

from .mailsend import mailSend

from django.shortcuts import HttpResponse, render, redirect

from .models import Phone
from .models import We

# Create your views here.
otp = ""

# otp = ""
# for i in range(4):
#     otp += str(random.randint(0, 10))
# result = "correct"
# print(otp)

def index(request):
    return HttpResponse("hello")


def avi(request):
    return HttpResponse("hello avinash")


def phone(request):
    name = ''
    data = []
    data1 = []
    if request.GET:
        name = request.GET['phone']
        data = (Phone.objects.filter(phone=name))
    return render(request, "phone.html", {"phone": name, "data": data, "session": request.session.items()})


def login(request):
    data = []
    username = ""
    password = ""
    result = "wrong"
    if request.GET:
        email = request.GET["email"]
        password = request.GET["password"]
        data = We.objects.filter(email=email) & We.objects.filter(password=password)
        # print(len(data), "******")   this is only to check that data available or not
        if len(data) != 0:
            otp = ""
            for i in range(4):
                otp += str(random.randint(0, 10))
            result = "correct"
            print(otp)
            # print(data[0].getName())           getting name of user from model
            mailSend(email, "otpsend", otp, "akashavinash397@gmail.com")
            request.session["otp"] = otp
            return redirect('http://127.0.0.1:8000/otpfill/')

        else:
            return render(request, "invalide.html")
    return render(request, "user.html",
                  {"data": data, "r": result, "username": username,
                   "password": password})


def signup(request):
    if request.GET:
        email = request.GET["email"]
        name = request.GET["name"]
        username = request.GET["username"]
        password = request.GET["password"]
        data = We(name=name, username=username, password=password, email=email)
        data.save()
    return render(request, "signup.html")


def signout(request):
    return render(request, "signout.html")


def otp(request):
    otp = ""
    for i in range(4):
        otp += str(random.randint(0, 10))
    return HttpResponse(otp)

def otpfill(request):
    if request.GET:
        ot = int(request.GET['otp'])
        otp = int(request.session.get('otp'))
        print((ot))
        print((int(request.session.get('otp'))))
        if ot == otp:
            return redirect('http://127.0.0.1:8000/phone/')
        else:
            return HttpResponse("wrong otp")
    return render(request, "otpfill.html")
