from django.urls import path
from .views import *

urlpatterns = [
    path('api/vendors-create/', VendorCreate.as_view(), name='vendor_create'),
    path('api/vendors-list/', VendorList.as_view(), name='vendor_list'),
    path('api/vendors-retrieve/<int:pk>/', VendorRetrieve.as_view(), name='vendor_retrieve'),
    path('api/vendors-update/<int:pk>/', VendorUpdate.as_view(), name='vendor_update'),
    path('api/vendors-delete/<int:pk>/', VendorDelete.as_view(), name='vendor_delete'),
    # Purchase Order Tracking api
    path('api/purchase_orders-create/', PurchaseOrderCreate.as_view(), name='order_create'),
    path('api/purchase_orders-list/', PurchaseOrderList.as_view(), name='order_list'),
    path('api/purchase_orders-retrieve/<int:pk>/', PurchaseOrderRetrieve.as_view(), name='order_retrieve'),
    path('api/purchase_orders-update/<int:pk>/', PurchaseOrderUpdate.as_view(), name='order_update'),
    path('api/purchase_orders-delete/<int:pk>/', PurchaseOrderDelete.as_view(), name='order_delete'),

    path('api/vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
    path('api/purchase_orders/<int:pk>/acknowledge/', PurchaseOrderAcknowledgmentView.as_view(),
         name='purchase-order-acknowledge'),
    path('historical_performance/', VendorHistoricalPerformanceView.as_view(), name='vendor-historical-performance'),
    path('api/performance-retrieve/<int:pk>/performance/', HistoricalPerformanceRetrieve.as_view(),
         name='historical_performance_retrieve'),
]
