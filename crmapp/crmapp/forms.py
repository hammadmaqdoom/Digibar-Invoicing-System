from django import forms
from crm.models import Purchases, Sales
# from django.contrib.auth.forms import UserCreationForm

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='', max_length=100)

# Create your forms here.

class Company(forms.Form):
    companyName = forms.CharField(label='Company', max_length=64)
    companyEmail = forms.EmailField(label='Email')
    companyPhoneNumber = forms.IntegerField(label='Number')
    is_client = forms.BooleanField()

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


class Business(forms.Form):
    businessName = forms.CharField(label='Business Name', max_length=64)
    ORGANISATION_TYPE = (
        ('SP', 'SoleProprietor'),
        ('P', 'Partnership'),
        ('PL', 'PrivateLimited'),
        ('PBL', 'PublicLimited')
    )
    organisationType = forms.MultipleChoiceField(choices=ORGANISATION_TYPE)
    businessType = forms.MultipleChoiceField(label='Business Type')
    CUREN = (
        ('PKR', 'Pakistani Ruppee'),
        ('USD', 'United States Dollar'),
        ('EUR', 'Euro'),
        ('AED', 'Dirham'),
        ('CAD', 'Canadian Dollar'),
        ('AUD', 'Australian Dollar')
    )
    currency = forms.MultipleChoiceField(choices=CUREN)

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

class ProductsAndServices(forms.Form):
    
    psName = forms.CharField(label='Name')
    isProduct = forms.BooleanField()
    itemDescription = forms.CharField(label='Item description')
    rate = forms.IntegerField(label='Rate')
    

class Sales(forms.Form):
    STAT = (
        ('A', 'Approved'),
        ('NA', 'NotApproved')
    )
    status = forms.MultipleChoiceField(choices=STAT)


class PurchasesForm(forms.Form):
    businessID = forms.IntegerField()
    itemID = forms.IntegerField()
    STAT = (
        ('A', 'Approved'),
        ('NA', 'NotApproved')
    )
    status = forms.MultipleChoiceField(choices=STAT)


class Transaction(forms.Form):
    # date = forms.DateTimeField()
    debit = forms.IntegerField(label='Debit Amount')
    credit = forms.IntegerField(label='Credit Amount')



# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)