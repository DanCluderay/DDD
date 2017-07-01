import os
from slugify import slugify

import shopify
from shopify import Product
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

datatable = pd.read_sql_query('SELECT products.ID, products.LONG_DESC, products.STOCK_LEVEL, products.FULL_NAME, products.CATS, products.PRICE, products.RRP_PRICE, products.BB_DATE, products.name_mid, products.brand, products.promo_prefix, products.promo_suffix, products.SHIP_WEIGHT, products.weight2, products.BARCODE, products.PRICE_TIERS, products.deal_text, products.IMAGES, products.PRICE_SALE FROM approvedfood.products products WHERE products.STOCK_LEVEL > 10000', engine)
datatable.head()
t = pd.DataFrame(datatable)
for index, row in t.iterrows():
    #print(row['DISPLAY_NAME'])
    new_product = Product()

    new_product.ID = row['ID']
    new_product.title = row['FULL_NAME']
    new_product.product_type = "Snowboard"
    new_product.body_html=row['LONG_DESC']
    new_product.vendor = row['brand']


    #print(new_product.variant)
    repn=str(row['brand'] + ' ' + row['name_mid'] + ' ' + row['weight2']).replace(' ','_')
    image_filename = "http://fthumb.approvedfood.co.uk/thumbs/75/1000/296/1/src_images/" + repn + ".jpg"
    #image_filename = "http://fthumb.approvedfood.co.uk/thumbs/75/1000/296/1/src_images/hersheys_creamy_milk_chocolate_with_almonds_43g.jpg"

    image1 = shopify.Image()
    image1.src = image_filename
    print(image1.src)
    new_product.images = [image1]
    success = new_product.save()  # returns false if the record is invalid
    new_product.attributes['variants'][0].attributes['barcode'] = str(row['BARCODE'])
    new_product.attributes['variants'][0].attributes['compare_at_price'] = str(row['BARCODE'])
    #new_product.attributes['variants'][0].attributes['grams'] = 12345
    new_product.attributes['variants'][0].attributes['inventory_quantity'] = str(row['STOCK_LEVEL'])
    new_product.attributes['variants'][0].attributes['price'] = str(row['PRICE'])
    new_product.attributes['variants'][0].attributes['sku'] = str(row['ID'])
    new_product.attributes['variants'][0].attributes['taxable'] = True
    new_product.attributes['variants'][0].attributes['title'] = str(row['FULL_NAME'])
    new_product.attributes['variants'][0].attributes['weight'] = float(row['SHIP_WEIGHT'])
    new_product.attributes['variants'][0].attributes['weight_unit'] = 'kg'
    new_product.attributes['variants'][0].attributes['inventory_management'] = 'shopify'
    # inventory-management>shopify

    success = new_product.save()
