from django.contrib import admin
from .models import Company,Users,Business,CompanyUsers,ProductsAndServices,Sales,Purchases,Transaction
# Register your models here.

admin.site.register(Company)
admin.site.register(Users)
admin.site.register(Business)
admin.site.register(CompanyUsers)
admin.site.register(ProductsAndServices)
admin.site.register(Sales)
admin.site.register(Purchases)
admin.site.register(Transaction)