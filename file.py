import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lappyng_project.settings")
import django
django.setup()
from lappyng_app.models import *

# all_prod = []
# prod_dict = Products.objects.values('brand', 'id')
# brands = {product['brand'] for product in prod_dict}
# for brand in brands:
#     prod_brand = Products.objects.filter(brand=brand)
#     all_prod.append(prod_brand)

# data = {'key':all_prod}
# print(data['key']['title'])
# print(all_prod)


def discount_prize(prize, percent ):
    dis = prize - (prize * percent/100)
    return dis


print(discount_prize(70000, 50))
