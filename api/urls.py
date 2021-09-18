
from django.urls import path
from .views import *


urlpatterns = [
    path(
        'v1/payables/<str:filter>/<str:type>/',
        PayablesView,
        name='payables'
    ),
    path(
        'v1/payables/',
        PayablesView,
        name='payables'
    ),
    path(
        'v1/transactions/',
        TransactionsView,
        name='transactions'
    ),
    path(
        'v1/transactions/<str:start_date>/<str:end_date>/',
        TransactionsView,
        name='transactions'
    )
]