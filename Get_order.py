import os
from slugify import slugify

import shopify
from shopify import Product
from shopify import Variant



shop_url = "https://%s:%s@dans-daily-deals.myshopify.com/admin" % ('1cc67033ddfda73bbdf799798fabe9dc', '6c9663bcdabfecf9ab0ffe2658b6f64f')

shopify.ShopifyResource.set_site(shop_url)


shop = shopify.Shop.current
o:shopify.order
o=shopify.Order.find()

print(o)