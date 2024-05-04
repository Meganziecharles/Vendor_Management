# filters.py

import django_filters
from .models import PurchaseOrder


class PurchaseOrderFilter(django_filters.FilterSet):
    vendor_id = django_filters.NumberFilter(field_name='vendor__id')

    class Meta:
        model = PurchaseOrder
        fields = ['vendor_id']
