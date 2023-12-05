from django.urls import path
from . import views

urlpatterns = [
    path('get_customer_invoice',views.get_customer_invoice,name='get_customer_invoice'),
]