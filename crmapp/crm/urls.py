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
    path('delete_invoices', views.delete_invoices, name='delete_invoices' ),
    path('update_invoices/', views.update_invoices, name='update_invoices' ),
    path("view_purchases",views.view_purchases, name='view_purchases'),
    path('delete_purchases/', views.delete_purchases, name='delete_purchases' ),
    path('update_purchases/', views.update_purchases, name='update_purchases' ),
<<<<<<< HEAD
    path('view_transactions/', views.view_transactions, name='view_transactions' ),
=======
    path('view_transactions', views.view_transactions, name='view_transactions' ),
>>>>>>> 7903cf6eb4a3b166ac0d0a805a90ec2d5632cc9a
    path('delete_transactions/', views.delete_transactions, name='delete_transactions' ),
    path('update_transactions/', views.update_transactions, name='update_transactions' ),


]

