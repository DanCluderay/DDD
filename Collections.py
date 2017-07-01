import os
from slugify import slugify

import shopify
from shopify import Variant
shop_url = "https://%s:%s@dans-daily-deals.myshopify.com/admin" % ('1cc67033ddfda73bbdf799798fabe9dc', '6c9663bcdabfecf9ab0ffe2658b6f64f')

shopify.ShopifyResource.set_site(shop_url)


shop = shopify.Shop.current

# Get a specific product
#product = shopify.Product.find(179761209)

# Create a new product



#get all products from approved food
import pandas as pd
import pymysql
from sqlalchemy import create_engine

#engine = create_engine('mysql+pymysql://lh4:approved2010@10.1.1.6/myticket')
engine = create_engine('mysql+pymysql://root:v#jPJ2Eb&Shv@46.37.182.203/approvedfood')

datatable = pd.read_sql_query('SELECT products.id, products.STOCK_LEVEL, products.FULL_NAME, products.CATS, products.PRICE, products.RRP_PRICE, products.BB_DATE, products.name_mid, products.brand, products.promo_prefix, products.promo_suffix, products.weight2 FROM approvedfood.products products WHERE products.STOCK_LEVEL > 10000', engine)
datatable.head()
t = pd.DataFrame(datatable)
for index, row in t.iterrows():
    #print(row['DISPLAY_NAME'])
    new_product = shopify.Product()
    new_product.ID = row['id']
    new_product.title = row['FULL_NAME']
    new_product.product_type = "Snowboard"
    new_product.vendor = row['brand']
    new_variant = Variant({"title": "v2", "option1": "Blue", "option2": "L"})
    new_product.add_variant=[new_variant]

    repn=str(row['brand'] + ' ' + row['name_mid'] + row['weight2']).replace(' ','_')
    image_filename = "http://fthumb.approvedfood.co.uk/thumbs/75/1000/296/1/src_images/" + repn + ".jpg"
    #image_filename = "http://fthumb.approvedfood.co.uk/thumbs/75/1000/296/1/src_images/hersheys_creamy_milk_chocolate_with_almonds_43g.jpg"

    image1 = shopify.Image()
    image1.src = image_filename

    new_product.images = [image1]
    success = new_product.save()  # returns false if the record is invalid

    #int(row['products.STOCK_LEVEL'])
    newID =row['id']
    #product = shopify.Product.find(newID)
