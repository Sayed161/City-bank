from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from .constant import ACCOUNT_TYPE,GENDER


class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='accounts',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=255,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateTimeField(null=True,blank=True)
    gender = models.CharField(max_length=15,choices=GENDER)	
    initial_deposit_date = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    bank_rupt = models.BooleanField(default=False)
    street_address = models.CharField(max_length=255,null=True)
    def __str__(self) -> str:
        return str(self.account_no)

