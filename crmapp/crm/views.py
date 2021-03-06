# from typing_extensions import Required
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from crmapp.forms import SignUpForm, PurchasesForm, InvoiceForm, ProductsAndServicesForm, TransactionForm, BusinessForm, CompanyForm
from crm.models import Sales, Purchases, ProductsAndServices, Transaction, Business, Company
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignUpForm()
	return render (request=request, template_name="signup.html", context={"register_form":form})

def index(request):
    return render(request, 'home.html', {})

def landinglogin(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    business = Business.objects.all()

    context = {'username':username, 'businesses':business}
    return render(request, 'land.html', context)

@login_required
def dashboard(request):
    sales_list = Sales.objects.order_by('salesID')[:5]
    Purchases_list = Purchases.objects.order_by('billID')[:5]
    PNS_list = ProductsAndServices.objects.order_by('itemID')[:5]
    Trans_list = Transaction.objects.order_by('transactionID')[:5]
    companies_list = Company.objects.order_by('companyID')[:5]
    context_dict = {'Sales': sales_list, 'Purchases': Purchases_list,
                    'ProductandServices': PNS_list, 'Transaction': Trans_list, 'Companies': companies_list}

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
def businesses(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
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
            return HttpResponseRedirect('land')
    else:
        form =BusinessForm()
    context = {'form':form }
    return render(request, 'businesses.html', context)

@login_required
def view_businesses(request):
    context = {}

    context["dataset"] = Business.objects.all()

    return render(request, 'view_businesses.html', context)

@login_required
def update_businesses(request):
    context = {}
    
    id = request.GET.get('id','')

    # fetch the object related to passed id
    obj = get_object_or_404(Business, businessID=id)

    # pass the object as instance in form
    form = BusinessForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/update_businesses/?id="+id)

    # add form dictionary to context
    context["form"] = form
    return render(request, "update_businesses.html", context)

@login_required
def delete_businesses(request):
    context = {}
    # fetch the object related to passed id
    id = request.GET.get('id','')
    obj = get_object_or_404(Business, businessID=id)
    form = BusinessForm(request.POST or None, instance=obj)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
    if form.is_valid():
        form.save()
        return redirect("/delete_businesses/?id="+id)

    return render(request, "delete_businesses.html", context)


@login_required
def companies(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
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
            return HttpResponseRedirect('companies')
    else:
        form =CompanyForm()
    context = {'form':form }
    return render(request, 'companies.html', context)

@login_required
def view_companies(request):
    context = {}

    context["dataset"] = Company.objects.all()

    return render(request, 'view_companies.html', context)

@login_required
def update_companies(request):
    context = {}
    
    id = request.GET.get('id','')

    # fetch the object related to passed id
    obj = get_object_or_404(Company, companyID=id)

    # pass the object as instance in form
    form = CompanyForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/update_companies/?id="+id)

    # add form dictionary to context
    context["form"] = form
    return render(request, "update_companies.html", context)

@login_required
def delete_companies(request):
    context = {}
    # fetch the object related to passed id
    id = request.GET.get('id','')
    obj = get_object_or_404(Company, companyID=id)
    form = CompanyForm(request.POST or None, instance=obj)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
    if form.is_valid():
        form.save()
        return redirect("/delete_companies/?id="+id)

    return render(request, "delete_companies.html", context)


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



@login_required
def view_invoices(request):
    context = {}

    context["dataset"] = Sales.objects.all()

    return render(request, 'view_invoice.html', context)

@login_required
def update_invoices(request):
    context = {}
    
    id = request.GET.get('id','')

    # fetch the object related to passed id
    obj = get_object_or_404(Sales, salesID=id)

    # pass the object as instance in form
    form = InvoiceForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/update_invoices/?id="+id)

    # add form dictionary to context
    context["form"] = form
    return render(request, "update_invoices.html", context)

@login_required
def delete_invoices(request):
    context = {}
    # fetch the object related to passed id
    id = request.GET.get('id','')
    obj = get_object_or_404(Sales, salesID=id)
    form = InvoiceForm(request.POST or None, instance=obj)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
    if form.is_valid():
        form.save()
        return redirect("/delete_invoices/?id="+id)

    return render(request, "delete_invoices.html", context)

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
def view_purchases(request):
    context = {}

    context["dataset"] =Purchases.objects.all()

    return render(request, 'view_purchases.html', context)



@login_required
def update_purchases(request):
    context = {}
    
    id = request.GET.get('id','')

    # fetch the object related to passed id
    obj = get_object_or_404(Purchases, billID=id)

    # pass the object as instance in form
    form = PurchasesForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/update_purchases/?id="+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_purchases.html", context)

@login_required
def delete_purchases(request):
    context = {}
    # fetch the object related to passed id
    id = request.GET.get('id','')
    obj = get_object_or_404(Purchases, billID=id)
    form = PurchasesForm(request.POST or None, instance=obj)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("view_purchases")
    if form.is_valid():
        form.save()
        return redirect("/delete_purchases/?id="+id)
    context["form"] = form
    return render(request, "delete_purchases.html", context)

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
            # return HttpResponseRedirect('productandservice')
            return redirect(reverse("productandservice"))
    else:
        form = ProductsAndServicesForm()

    context = {'form': form}

    return render(request, 'productandservice.html', context)

@login_required
def view_productandservices(request):
    context = {}

    context["dataset"] = ProductsAndServices.objects.all()

    return render(request, 'view_productandservices.html', context)

@login_required
def update_productandservices(request):
    context = {}
    
    id = request.GET.get('id','')

    # fetch the object related to passed id
    obj = get_object_or_404(ProductsAndServices, itemID=id)

    # pass the object as instance in form
    form = ProductsAndServicesForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/update_productandservices/?id="+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_productandservices.html", context)

@login_required
def delete_productandservices(request):
    context = {}
    # fetch the object related to passed id
    id = request.GET.get('id','')
    obj = get_object_or_404(ProductsAndServices, itemID=id)
    form = ProductsAndServicesForm(request.POST or None, instance=obj)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        # return HttpResponseRedirect("view_purchases")
    if form.is_valid():
        form.save()
        return redirect("/delete_productandservices/?id="+id)
    context["form"] = form
    return render(request, "delete_productandservices.html", context)
    


@login_required
def transaction(request):
    # id = request.GET.get('id','')
    # obj = get_object_or_404(Company, companyID=id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
           # obj = Transaction()  # gets new object
            # obj.transactionID = form.cleaned_data['transactionID']
            # if 
            # obj.billID = form.cleaned_data['billID']
            
            # obj.salesID = form.cleaned_data['billID']
            # obj.date = form.cleaned_data['date']
            # obj.debit = form.cleaned_data['debit']
            # obj.credit = form.cleaned_data['credit']
            # ##
            # obj.save()
            form.save()
            return HttpResponseRedirect('transaction')

    else:
        form = TransactionForm()

    return render(request, 'transaction.html', {'form': form})

@login_required
def update_transactions(request):
    context = {}
    
    id = request.GET.get('id','')

    # fetch the object related to passed id
    obj = get_object_or_404(Transaction, transactionID=id)

    # pass the object as instance in form
    form = TransactionForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/update_transactions/?id="+id)

    # add form dictionary to context
    context["form"] = form
    return render(request, "update_transactions.html", context)


@login_required
def view_transactions(request):
    context = {}

    context["dataset"] =Transaction.objects.all()

    return render(request, 'view_transactions.html', context)

@login_required
def delete_transactions(request):
    context = {}
    # fetch the object related to passed id
    id = request.GET.get('id','')
    obj = get_object_or_404(Transaction, transactionID=id)
    form = TransactionForm(request.POST or None, instance=obj)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
    if form.is_valid():
        form.save()
        return redirect("/delete_transactions/?id="+id)

    return render(request, "delete_transactions.html", context)