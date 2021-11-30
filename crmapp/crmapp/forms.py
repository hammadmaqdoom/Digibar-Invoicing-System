from django import forms
from crm.models import Company ,Purchases, Sales , Transaction ,ProductsAndServices, Business
# from django.contrib.auth.forms import UserCreationForm

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='', max_length=100)

# Create your forms here.

class Company(forms.Form):#modelForm
    class Meta():
        model = Company
        fields = ('companyName','companyEmail','companyPhoneNumber','is_client')
 
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


class Business(forms.Form): ####
    class Meta():
        model = Business
        fields = ('businessID','businessName','organisationType','businessType','currency')

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
        fields = ('itemID','psName','isProduct','itemDescription','rate')
    

class InvoiceForm(forms.ModelForm): # add fields
    class Meta():
        model = Sales
        fields = ('salesID','companyID','businessID','items','status')

# class ItemSaleForm(forms.ModelForm): # add fields
#     class Meta():
#         model = Item_sale
#         fields = ('itemsaleID','salesID','itemID')
    
    
   
class PurchasesForm(forms.ModelForm):

    class Meta():
        model = Purchases
        fields = ('billID','companyID','businessID','itemID','status')
   


class TransactionForm(forms.ModelForm):

    class Meta():
        model = Transaction
        fields = ('transactionID','billID','salesID','date','debit','credit')



# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)