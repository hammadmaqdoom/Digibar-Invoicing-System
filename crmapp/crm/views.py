# from typing_extensions import Required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from crmapp.forms import PurchasesForm
# Create your views here.

def index(request):
    return render(request, 'home.html', {})

def landinglogin(request):
    return render(request, 'land.html', {})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})

def userlogin(request):
    return HttpResponse("User Login Page")

# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "signup.html",
#             {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse("dashboard"))

@login_required
def quotations(request):
    return HttpResponse("Quotations")

@login_required
def invoices(request):
    return HttpResponse("invoices")

@login_required
def purchases(request):
    if request.method == 'POST':
        form = PurchasesForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = PurchasesForm()
    
    return render(request, 'purchases.html', {'form': form})

@login_required
def productservices(request):
    return HttpResponse("productservices")