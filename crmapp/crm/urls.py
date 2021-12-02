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
    path('businesses', views.businesses, name = 'businesses'),
    path('companies', views.companies, name = 'companies'),
    path('purchases', views.purchases, name = 'purchases'),
    path('productandservice', views.productandservice, name = 'productandservice'),
    path('dashboard', views.dashboard, name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("land", views.landinglogin, name='land'),
    path("transaction", views.transaction, name='transaction'),
    path("view_invoices",views.view_invoices, name='view_invoices'),
    path('delete_invoices/', views.delete_invoices, name='delete_invoices' ),
    path('update_invoices/', views.update_invoices, name='update_invoices' ),
    path("view_purchases",views.view_purchases, name='view_purchases'),
    path('delete_purchases/', views.delete_purchases, name='delete_purchases' ),
    path('update_purchases/', views.update_purchases, name='update_purchases' ),
    path('view_transactions', views.view_transactions, name='view_transactions' ),
    path('delete_transactions/', views.delete_transactions, name='delete_transactions' ),
    path('update_transactions/', views.update_transactions, name='update_transactions' ),
    path("view_productandservices", views.view_productandservices, name='view_productandservices' ),
    path('delete_productandservices/', views.delete_productandservices, name='delete_productandservices' ),
    path('update_productandservices/', views.update_productandservices, name='update_productandservices' ),
    path("view_companies", views.view_companies, name='view_companies' ),
    path('delete_companies/', views.delete_companies, name='delete_companies' ),
    path('update_companies/', views.update_companies, name='update_companies' ),
    path("view_businesses", views.view_businesses, name='view_businesses' ),
    path('delete_businesses/', views.delete_businesses, name='delete_businesses' ),
    path('update_businesses/', views.update_businesses, name='update_businesses' ),


]

