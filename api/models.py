from django.db import models

"""
Model wich represent a payable (p. ex. Light, Light service, YYYY-MM-DD, 800.00, Pe, 986482736485968452).
"""
class Payables(models.Model):
    STATUS = (
        ('pe', 'Pending'),
        ('pa', 'Paid'),
        ('ca', 'Canceled'),
    )
    service_type = models.TextField(max_length=100)
    service_description = models.TextField(max_length=200)
    expiration_date = models.DateField(auto_now_add=True)
    service_amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_status = models.CharField(max_length=2, choices=STATUS)
    barcode = models.CharField(max_length=18, unique=True)


"""
Model wich represent a transaction (p. ex. dc, 1578459635872495, YYYY-MM-DD, 800.00, 986482736485968452).
"""
class Transactions(models.Model):
    STATUS = (
        ('dc', 'debit_card'),
        ('cc', 'credit_card'),
        ('ca', 'cash'),
    )
    barcode = models.OneToOneField(Payables, on_delete=models.CASCADE, primary_key=True)
    payment_method = models.CharField(max_length=2, choices=STATUS)
    card = models.CharField(max_length=16)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
