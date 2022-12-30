from django import template
register=template.Library()
import math
@register.simple_tag
def sale_price(price,product_discount):
    sale_price=price-(price*product_discount/100)
    return math.floor(sale_price)

@register.simple_tag
def progressbar(availability,qty):
    counter=availability*(100/qty)
    return counter
