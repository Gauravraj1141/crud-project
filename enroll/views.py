from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User
# Create your views here.


# def registeration(request):
#     if request.method == "POST":
#         formdata = UserForm(request.POST)
#         if formdata.is_valid():
#             print("validate")
#             nm = formdata.cleaned_data["Name"]
#             em = formdata.cleaned_data["Email"]
#             ph = formdata.cleaned_data["Phone"]
#             ps = formdata.cleaned_data["Password"]
#             adddata = User(Name=nm, Email=em, Phone=ph, Password=ps)
#             adddata.save()
#     else:
#         formdata = UserForm()
#     return render(request, "enroll/register.html", {"fm": formdata})

# it is short method

def registeration(request):
    if request.method == "POST":
        formdata = UserForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            formdata = UserForm()
    else:
        formdata = UserForm()

    data = User.objects.all()

    return render(request, "enroll/register.html", {"fm": formdata, "mydata": data})


def delete(request, user):
    if request.method == "POST":
        userdata = User.objects.get(Userid=user)
        userdata.delete()
        return HttpResponseRedirect("/")


def updates(request, upid):
    if request.method == "POST":
        userdata = User.objects.get(Userid=upid)
        updateddata = UserForm(request.POST, instance=userdata)
        if updateddata.is_valid():
            updateddata.save()
            status = True
            # return HttpResponseRedirect("/")
            context = {"fm": updateddata, "status": status}
            return render(request, "enroll/update.html", context)

    else:
        status = False
        userdata = User.objects.get(Userid=upid)
        myform = UserForm(instance=userdata)

    context = {"fm": myform, "status": status}

    return render(request, "enroll/update.html", context)
