
from datetime import date, timedelta
from django.db.models import Count, Avg
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Payables, Transactions
from .serializers import SerializedPayable, SerializedTransaction

class PayablesView(APIView):
    """
        View dedicated to:
        - List all payables, filtered by payment status or service type.
        - Create a new payable.
    """
    
    def get( self, *args, **kwargs ):
        filter = kwargs.get('filter', '')
        type = kwargs.get('type', '')
        if filter == 'service':
            payables = Payables.objects.filter(service_type=type)
        elif filter == "unpaid":
            payables = Payables.objects.filter(payment_status=type)
        else:
            payables = Payables.objects.all()
        serializer_payables = SerializedPayable(payables, many=True)
        return JsonResponse(serializer_payables.data, status=200)

    def post( self, request ):
        try:
            serialized_payable = SerializedPayable( data = request.data )
            if serialized_payable.is_valid():
                serialized_payable.create()
                return JsonResponse(serialized_payable.data, status=201)
            return JsonResponse(serialized_payable.errors, status=400)
        except Exception as e:
            return JsonResponse(serialized_payable.errors, status=400)


class TransactionsView(APIView):
    """
        View dedicated to:
        - List of total amounts and transactions per day filtered by a period of time.
        - Create a new transaction.
    """
    def get( self, *args, **kwargs):
        transactions_per_day=[{}]
        try:
            start_date = date(kwargs.get('start_date', date.today()))
            end_date = date(kwargs.get('end_date', date.today()))
            for single_date in daterange(start_date, end_date):
                payment_day = single_date.strftime("%Y-%m-%d")
                transactions = Transactions.objects.filter(payment_date__gte=single_date).aggregate(
                    total_amount=Avg('amount'), transactions_number=Count())
                transactions_per_day.append({'payment_day':payment_day,
                                            'total_amount':transactions.total_amount,
                                            'transactions_number':transactions.transactions_number})
            return JsonResponse(transactions_per_day, status=200)
        except Exception as e:
            return JsonResponse(transactions_per_day, status=400)

    def post( self, request ):
        try:
            serialized_transaction = SerializedTransaction( data = request.data )
            if serialized_transaction.is_valid():
                serialized_transaction.create()
                return JsonResponse(serialized_transaction.data, status=201)
            return JsonResponse(serialized_transaction.errors, status=400)
        except Exception as e:
            return JsonResponse(serialized_transaction.errors, status=400)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)