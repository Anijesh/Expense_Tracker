from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance=models.IntegerField(default=0)

    def __str__(self):
        return self(self.current_balance)
    
class TrackingHistory(models.Model):
    current_balance=models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    amount=models.IntegerField()
    expense_type=models.CharField(choices=(('CREDIT','CREDIT'),('DEBIT','DEBIT')),max_length=50)
    description =models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The amount is{self.amount} for expense type {self.expense_type}"
    
class RequestLogs(models.Model):
    request_info=models.TextField()
    request_type=models.CharField(max_length=100)
    request_method=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)