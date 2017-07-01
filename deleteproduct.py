import os
from slugify import slugify

import shopify
import math
from shopify import Product
shop_url = "https://%s:%s@dans-daily-deals.myshopify.com/admin" % ('1cc67033ddfda73bbdf799798fabe9dc', '6c9663bcdabfecf9ab0ffe2658b6f64f')

shopify.ShopifyResource.set_site(shop_url)


shop = shopify.Shop.current

products_count = shopify.Product.count(published_status='published')

limit = 50
pages = math.ceil(products_count / limit)

variants_data = []
x=0
print(pages)
for i in range(1, pages + 1):
    products = shopify.Product.find(limit=limit, page=i, published_status='published')
    for product in products:
        Product=product
        Product.destroy()
        print(product)
        print(x)
        x=x+1


def get_all_resources(resource, **kwargs):
    resource_count = resource.count(**kwargs)
    resources = []
    if resource_count > 0:
        for page in range(1, ((resource_count-1) // 250) + 2):
            kwargs.update({"limit" : 250, "page" : page})
            resources.extend(resource.find(**kwargs))
    return resources

