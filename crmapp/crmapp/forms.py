from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from crm.models import Company, Purchases, Sales, Transaction, ProductsAndServices, Business
# from django.contrib.auth.forms import UserCreationForm

# Create your forms here.


class CompanyForm(forms.ModelForm):  # modelForm
    class Meta():
        model = Company
        fields = ('companyName', 'companyEmail','companyPhoneNumber')

# class Users(forms.Form):
#     userName = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=64)
#     ACCESS_LEVEL = (
#         ('admin', 'Admin'),
#         ('business', 'Business'),
#         ('compuser', 'CompanyUser'),
#     )
#     accessLevel = forms.MultipleChoiceField(choices=ACCESS_LEVEL)
#     companyID = forms.ForeignKey(Company, on_delete=forms.CASCADE)


class BusinessForm(forms.ModelForm):
    class Meta():
        model = Business
        fields = ('businessID', 'businessName','organisationType', 'businessType', 'currency')

# class CompanyUsers(forms.Form):
#     businessID = forms.ForeignKey(Business, on_delete=forms.CASCADE)
#     companyID = forms.ForeignKey(Company, on_delete=forms.CASCADE)
#     USER_TYPE = (
#         ('S', 'Sales'),
#         ('P', 'Purchases')
#     )
#     userType = forms.CharField(max_length=1, choices=USER_TYPE)
#     def __str__(self):
#         return str(self.userID)


class ProductsAndServicesForm(forms.ModelForm):
    class Meta():
        model = ProductsAndServices
        fields = ('itemID', 'psName', 'isProduct', 'itemDescription', 'rate')


class InvoiceForm(forms.ModelForm):  # add fields
    items = forms.ModelMultipleChoiceField(
        queryset = ProductsAndServices.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    class Meta():
        model = Sales
        fields = ('salesID', 'companyID', 'businessID', 'items', 'status')

class PurchasesForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset = ProductsAndServices.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    class Meta():
        model = Purchases
        fields = ('billID', 'companyID', 'businessID', 'items','status')


class TransactionForm(forms.ModelForm):

    class Meta():
        model = Transaction
        fields = ('transactionID', 'billID','salesID', 'date', 'debit', 'credit')


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)
