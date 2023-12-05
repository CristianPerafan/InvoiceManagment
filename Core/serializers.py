from rest_framework import serializers
from .models import Invoice


class CustomerInvoice(serializers.ModelSerializer):
    class Meta(object):
        model = Invoice
        fields = ('invoice_number', 'client_id')