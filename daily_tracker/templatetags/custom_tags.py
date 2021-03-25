from django import template

register = template.Library()

@register.filter
def this_better_work(user_custom_table_stock,InfoField):
    return user_custom_table_stock.stock_infos().filter(info=InfoField).first()