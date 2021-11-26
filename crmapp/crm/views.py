# from typing_extensions import Required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from crmapp.forms import PurchasesForm,InvoiceForm,ProductsAndServicesForm , TransactionForm
from crm.models import Sales, Purchases, ProductsAndServices,Transaction
# Create your views here.

def index(request):
    return render(request, 'home.html', {})

def landinglogin(request):
    return render(request, 'land.html', {})

@login_required
def dashboard(request):

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    sales_list = Sales.objects.order_by('businessID')[:5]
    #context_dict = {'Sales': sales_list}
    Purchases_list = Purchases.objects.order_by('businessID')[:5]
    PNS_list = ProductsAndServices.objects.order_by('psName')[:5]
    context_dict = {'Sales': sales_list,'Purchases': Purchases_list,'Product and Services': PNS_list}

    # Render the response and send it back
    return render(request, 'dashboard.html', context_dict)

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