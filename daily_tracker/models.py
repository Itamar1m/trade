from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class InfoField(models.Model):
    name = models.CharField(max_length=50)
    list_name=models.CharField(max_length=50,default="_")

    
    def __str__(self):
        return f'{self.name}'


class FieldData(models.Model):
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE,null=True)
    high_of_day = models.FloatField (default=0)
    low_of_day = models.FloatField (default=0)
    closing_price = models.FloatField (default=0) 
    open_price = models.FloatField (default=0)
    volume = models.PositiveIntegerField (default=0)
    datetime = models.DateField(default=now,editable=True)

    def __str__(self):
        return f' {self.stock} -- {self.datetime} ' 


class Stock(models.Model):
    symbol = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.symbol}'


class UserCustomTable(models.Model):    
    name = models.CharField(max_length=50)
    infos = models.ManyToManyField(InfoField,related_name='field_table')
    field_datas=models.ManyToManyField(FieldData)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,related_name="table")

    def __str__(self):
        return f' User = { self.profile.username} : Table name = {self.name}' 




# datetime_of_info_requested = 'datetimeobject'
# appl_info = [{'open':78, 'datetime': ''}]
# appl_stock = Stock.objects.get_or_create(code='APPL')[0]
# for info_dict in appl_info:
#     for key, value in info_dict.items():
#         if key == 'datetime':
#             continue
#         stockattr = StockAttribute.objects.get_or_create(name=key)[0]
#         StockInfo.objects.create(stock=appl_stock, info=stockattr, amount=value, datetime=datetime_of_info_requested)
#         
#        









# class InfoField(models.Model):
#     name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return f'{self.name}'


# class FieldData(models.Model):
#     name = models.ForeignKey(InfoField, related_name='field',on_delete=models.CASCADE,null=True)
#     amount = models.FloatField (default=0)
#     stock = models.ForeignKey('Stock', on_delete=models.CASCADE,null=True,related_name='field_data')
#     table=models.ForeignKey('UserCustomTable',on_delete=models.CASCADE,null=True,related_name='user_table')
#     datetime = models.DateField(default=now,editable=True)

#     def __str__(self):
#         return f'{self.amount} -- {self.name} -- {self.stock} -- {self.datetime}' 


# class Stock(models.Model):
#     symbol = models.CharField(max_length=50)
#     full_name = models.CharField(max_length=50)
      
#     def __str__(self):
#         return f'{self.symbol}'


# class UserCustomTable(models.Model):    
#     name = models.CharField(max_length=50)
#     stocks=models.ManyToManyField(Stock, blank=True,related_name='stocks')
#     infos = models.ManyToManyField(InfoField,related_name='field_table')
#     profile = models.ForeignKey(User, on_delete=models.CASCADE,related_name="table")

# #     def __str__(self):
# #         return f' User = { self.profile.username} : Table name = {self.name}' 




# datetime_of_info_requested = 'datetimeobject'





# class InfoField(models.Model):
#     name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return f'{self.name}'


# class FieldData(models.Model):
#     name = models.ForeignKey(InfoField, related_name='field',on_delete=models.CASCADE,null=True)
#     amount = models.PositiveIntegerField(default=0)
#     stock = models.ForeignKey('Stock', on_delete=models.CASCADE,null=True,related_name='field_data')
#     table=models.ForeignKey('UserCustomTable',on_delete=models.CASCADE,null=True,related_name='user_table')
#     datetime = models.DateField(default=now,editable=True)

#     def __str__(self):
#         return f'{self.amount} -- {self.name} -- {self.stock} -- {self.datetime}' 


# class Stock(models.Model):
#     symbol = models.CharField(max_length=50)
#     full_name = models.CharField(max_length=50)
      
#     def __str__(self):
#         return f'{self.symbol}'




# class UserCustomTable(models.Model):    
#     name = models.CharField(max_length=50)
#     stocks=models.ManyToManyField(Stock, blank=True,related_name='stocks')
#     infos = models.ManyToManyField(InfoField,related_name='field_table')
#     profile = models.ForeignKey(User, on_delete=models.CASCADE,related_name="table")

#     def __str__(self):
#         return f' User = { self.profile.username} : Table name = {self.name}' 









# Create your models here.
