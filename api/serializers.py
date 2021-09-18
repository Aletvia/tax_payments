from .models import Payables, Transactions
from rest_framework import serializers

class SerializedPayable(serializers.ModelSerializer):

    class Meta:
        model = Payables
        fields = '__all__'
        
    def create(self, validated_data):
        """
        Create and return a new `Payable` instance, given the validated data.
        """
        return Payables.objects.create(**validated_data)

class SerializedTransaction(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'
        
    def create(self, validated_data):
        """
        Create and return a new `Transaction` instance, given the validated data.
        """
        return Transactions.objects.create(**validated_data)