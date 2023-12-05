from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import CustomerInvoice
from .models import Customer,Invoice,Product,Detail
from django.db.models import Sum,F
from decimal import Decimal


# Create your views here.

@api_view(['GET'])
def get_customer_invoice(request):
    if 'invoice_number' not in request.data or 'client_id' not in request.data:
        return Response({"message": "Both invoice_number y client_id are required."}, status=status.HTTP_400_BAD_REQUEST)

    invoice_number = request.data['invoice_number']
    client_id = request.data['client_id']

    try:
        invoice = Invoice.objects.get(invoice_number=invoice_number, client_id=client_id)

        details = Detail.objects.filter(invoice_number=invoice_number)

        item_count = details.count()

        total = details.aggregate(total=Sum(F('amount') * F('price')))['total']

        if total>1000000 and item_count>5:
            total = total - (total * Decimal('0.1'))
        return Response({"Invoice total": total}, status=status.HTTP_200_OK)
    
    except Invoice.DoesNotExist:
        print("Invoice not found")
        return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)


