from django.urls import path
from django.conf.urls import include
from crm import views

# app_name = "crm"

urlpatterns = [
    path('', views.index, name='index'), 
    path('userlogin', views.userlogin, name = 'userlogin'),
    # path('usersignup', views.usersignup, name = 'usersignup'),
    path('quotations', views.quotations, name = 'quotations'),
    path('invoices', views.invoices, name = 'invoices'),
    path('purchases', views.purchases, name = 'purchases'),
    path('productandservice', views.productandservice, name = 'productandservice'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("land", views.landinglogin, name='land'),
    path("transaction", views.transaction, name='transaction'),
    path("view_invoices",views.view_invoices, name='view_invoices'),
    path('<id>/delete_sales', views.delete_view, name='delete_views' )

]

