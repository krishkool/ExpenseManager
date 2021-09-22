from django.db import models

# Create your models here.
class ExpenseManage(models.Model):
    Name = models.CharField(max_length=25)
    Amount  = models.DecimalField(max_digits=7, decimal_places=2)
    Description = models.TextField()
    Date     = models.DateField()

    def __str__(self):
        return self.Name

class BalanceManage(models.Model):
    Balance = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.Balance