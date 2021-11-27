# from typing_extensions import Required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    sales_list = Sales.objects.order_by('salesID')[:5]
    Purchases_list = Purchases.objects.order_by('billID')[:5]
    PNS_list = ProductsAndServices.objects.order_by('itemID')[:5]
    Trans_list = Transaction.objects.order_by('transactionID')[:5]
    context_dict = {'Sales': sales_list,'Purchases': Purchases_list,'ProductandServices': PNS_list,'Transaction': Trans_list}

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
            obj = Sales() #gets new object
            obj.companyID = form.cleaned_data['companyID']
            obj.businessID = form.cleaned_data['businessID']
            obj.itemID = form.cleaned_data['itemID']
            obj.status = form.cleaned_data['status']
            #finally save the object in db
            obj.save()
            return HttpResponseRedirect('invoices')
    else:
        form =InvoiceForm()

    context = {'form':form, }
    
    return render(request, 'invoice.html', context)

@login_required
def view_invoices(request):                                        
    context ={}

    context["dataset"] = Sales.objects.all()
    
    return render(request, 'view_invoice.html', context)

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