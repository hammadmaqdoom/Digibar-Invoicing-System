from django.db import models

# Create your models here.

class Company(models.Model):
    companyID = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=64)
    companyEmail = models.EmailField(max_length=254)
    companyPhoneNumber = models.IntegerField()
    # is_client = models.BooleanField(default=True)

    def __str__(self):
        return self.companyName


class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=1000)
    password = models.CharField(max_length=64)
    ACCESS_LEVEL = (
        ('admin', 'Admin'),
        ('business', 'Business'),
        ('compuser', 'CompanyUser'),
    )
    accessLevel = models.CharField(max_length=50, choices=ACCESS_LEVEL)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.userName


class Business(models.Model):
    businessID = models.AutoField(primary_key=True)
    businessName = models.CharField(max_length=64)
    ORGANISATION_TYPE = (
        ('SP', 'SoleProprietor'),
        ('P', 'Partnership'),
        ('PL', 'PrivateLimited'),
        ('PBL', 'PublicLimited')
    )
    organisationType = models.CharField(
        max_length=3, choices=ORGANISATION_TYPE)
    businessType = models.CharField(max_length=64)
    CUREN = (
        ('PKR', 'Pakistani Ruppee'),
        ('USD', 'United States Dollar'),
        ('EUR', 'Euro'),
        ('AED', 'Dirham'),
        ('CAD', 'Canadian Dollar'),
        ('AUD', 'Australian Dollar')
    )
    currency = models.CharField(max_length=3, choices=CUREN)

    def __str__(self):
        return self.businessName


class CompanyUsers(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    businessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    USER_TYPE = (
        ('S', 'Sales'),
        ('P', 'Purchases')
    )
    userType = models.CharField(max_length=1, choices=USER_TYPE)

    def __str__(self):
        return str(self.userID)


class ProductsAndServices(models.Model):
    itemID = models.AutoField(primary_key=True)
    psName = models.CharField(max_length=512)
    isProduct = models.BooleanField()
    itemDescription = models.CharField(max_length=500)
    rate = models.IntegerField()

    def __str__(self):
        return self.psName


class Sales(models.Model):
    salesID = models.AutoField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    businessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    # itemID = models.ForeignKey(ProductsAndServices, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductsAndServices)
    STAT = (
        ('A', 'Approved'),
        ('NA', 'NotApproved')
    )
    status = models.CharField(max_length=2, choices=STAT)

    def get_item_values(self):
        ret = ''
        print(self.items.all())
        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for item in self.items.all():
            ret = ret + item.psName + ', '
        # remove the last ',' and return the value.
        return ret[:-1]

    def get_total(self):
        total = 0
        print(self.items.all())
        
        for item in self.items.all():
            print(item.rate)
            total += item.rate
        return total

    def __str__(self):
        return str(self.salesID)


class Purchases(models.Model):
    billID = models.AutoField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    businessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    #itemID = models.ForeignKey(ProductsAndServices, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductsAndServices)
    STAT = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid')
    )
    status = models.CharField(max_length=64, choices=STAT)

    def get_item_values(self):
        ret = ''
        print(self.items.all())
        # use models.ManyToMany field's all() method to return all the Department objects that this employee belongs to.
        for item in self.items.all():
            ret = ret + item.psName + ', '
        # remove the last ',' and return the value.
        return ret[:-1]

    def get_total(self):
        total = 0
        print(self.items.all())
        
        for item in self.items.all():
            total += item.rate
        return total

    def __str__(self):
        return str(self.billID)


class Transaction(models.Model):
    transactionID = models.AutoField(primary_key=True)
    billID = models.ForeignKey(Purchases, on_delete=models.CASCADE)
    salesID = models.ForeignKey(Sales, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    debit = models.IntegerField()
    credit = models.IntegerField()

    def __str__(self):
        return str(self.transactionID)
