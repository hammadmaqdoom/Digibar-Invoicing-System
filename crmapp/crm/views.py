# from typing_extensions import Required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from crmapp.forms import PurchasesForm,InvoiceForm,ProductsAndServicesForm , TransactionForm
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
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form =InvoiceForm()
    
    return render(request, 'invoice.html', {'form': form})

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
def productandservice(request):                                        
    if request.method == 'POST':
        form =  ProductsAndServicesForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ProductsAndServicesForm()
    
    return render(request, 'productandservice.html', {'form': form})


@login_required
def transaction(request):                                         
    if request.method == 'POST':
        form =  TransactionForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = TransactionForm()
    
    return render(request, 'transaction.html', {'form': form})