# from typing_extensions import Required
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from crmapp.forms import PurchasesForm, InvoiceForm, ProductsAndServicesForm, TransactionForm
from crm.models import Sales, Purchases, ProductsAndServices, Transaction
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
    context_dict = {'Sales': sales_list, 'Purchases': Purchases_list,
                    'ProductandServices': PNS_list, 'Transaction': Trans_list}

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
def purchases(request):
    if request.method == 'POST':
        form = PurchasesForm(request.POST)
        if form.is_valid():
            # obj = Purchases()  # gets new object
            # obj.companyID = form.cleaned_data['companyID']
            # obj.businessID = form.cleaned_data['businessID']
            # obj.itemID = form.cleaned_data['itemID']
            # # does nothing, just trigger the validation
            # obj.status = form.cleaned_data['status']
            # obj.save() 
            form.save()
            return HttpResponseRedirect('purchases')

    else:
        form = PurchasesForm()
    context = {'form':form }
    return render(request, 'purchases.html', context)

@login_required
def invoices(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            # Items = ProductsAndServices()
            # obj = Sales() #gets new object
            # obj.companyID = form.cleaned_data['companyID']
            # obj.businessID = form.cleaned_data['businessID']
            # # obj.items  = form.cleaned_data['items']
            # items = ProductsAndServices.objects.filter()
            # obj.items.set(form.cleaned_data['items'])
            # # obj.items = Items.objects.filter(itemID=inst)
            # obj.status = form.cleaned_data['status']
            # #finally save the object in db
            # obj.save()
            form.save()
            return HttpResponseRedirect('invoices')
    else:
        form =InvoiceForm()
    context = {'form':form }
    return render(request, 'invoice.html', context)

def update_invoices(request, salesID):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Sales, salesID=salesID)

    # pass the object as instance in form
    form = InvoiceForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/update_sales/"+salesID)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_invoices.html", context)


@login_required
def view_invoices(request):
    context = {}

    context["dataset"] = Sales.objects.all()

    return render(request, 'view_invoice.html', context)

@login_required
def delete_invoices(request, salesID):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Sales, salesID=salesID)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("view_invoices")

    return render(request, "delete_sales.html", context)

@login_required
def productandservice(request):
    if request.method == 'POST':
        form = ProductsAndServicesForm(request.POST)
        if form.is_valid():
            # obj = ProductsAndServices()  # gets new object
            # obj.itemID = form.cleaned_data['itemID']
            # obj.psName = form.cleaned_data['psName']
            # obj.isProduct = form.cleaned_data['isProduct']
            # obj.itemDescription = form.cleaned_data['itemDescription']
            # obj.rate = form.cleaned_data['rate']
            # obj.save()
            form.save()
            return HttpResponseRedirect('productandservice')
    else:
        form = ProductsAndServicesForm()

    context = {'form': form}

    return render(request, 'productandservice.html', context)


@login_required
def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            obj = Transaction()  # gets new object
            obj.transactionID = form.cleaned_data['transactionID']
            obj.billID = form.cleaned_data['billID']
            obj.date = form.cleaned_data['date']
            obj.debit = form.cleaned_data['debit']
            obj.credit = form.cleaned_data['credit']
            ##
            obj.save()
            return HttpResponseRedirect('transaction')

    else:
        form = TransactionForm()

    return render(request, 'transaction.html', {'form': form})