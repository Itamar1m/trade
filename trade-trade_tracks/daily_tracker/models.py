from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



class InfoField(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'


class FieldData(models.Model):
    info = models.ForeignKey(InfoField, related_name='field_datas',on_delete=models.CASCADE,null=True)
    amount = models.CharField(max_length=100)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE,null=True,related_name='field_datas')
    table=models.ForeignKey('UserCustomTable',on_delete=models.CASCADE,null=True,related_name='field_datas')
    date = models.ForeignKey('DateObject',on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.amount} -- {self.stock.symbol} -- {self.date}' 


class Stock(models.Model):
    symbol = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50,null=True,blank=True)
      
    # def __str__(self):
    #     return f'{self.symbol.upper()}'


class DateObject(models.Model):
    date= models.DateField(editable=True)

    # def __str__(self):
    #     return self.date


class UserCustomTableStocks(models.Model):
    date = models.ForeignKey(DateObject,on_delete=models.CASCADE)
    user_custom_table = models.ForeignKey('UserCustomTable',on_delete=models.CASCADE,related_name='row')
    stock = models.ForeignKey(Stock,on_delete=models.CASCADE)

    class Meta:
        ordering = ('date','stock__symbol')
    def stock_infos(self):
        return self.stock.field_datas.filter(date=self.date)


class UserCustomTable(models.Model):    
    name = models.CharField(max_length=50)
    stocks=models.ManyToManyField(Stock, blank=True,related_name='stocks',through=UserCustomTableStocks)
    infos = models.ManyToManyField(InfoField,related_name='field_table')
    profile = models.ForeignKey(User, on_delete=models.CASCADE,related_name="tables")

    def __str__(self):
        return f' User = { self.profile.username} : Table name = {self.name}' 









# Create your models here.
