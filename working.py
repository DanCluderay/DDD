import os
from slugify import slugify

import shopify
from shopify import Product
from shopify import Variant
import Core_Shopify


def create_pricing_dict(price):
    PriceTierCount = int(price[2])
    print(PriceTierCount)
    loop_pos = 0
    sp = price.split(';')
    holdingstring: str = ''
    firstPT_QTY: int = 0
    firstPT_Val: float = 0.0
    secPT_QTY: float = 0
    secPT_Val: float = 0.0
    PTCount: int = 0
    for s in sp:
        if loop_pos == 2:
            # look for first qty
            spq = s.split(':')
            firstPT_QTY = int(spq[1])
            PTCount += 1
        if loop_pos == 4:
            # look for first qty
            spq = s.split(':')
            holdingstring = spq[2]
            firstPT_Val = float(holdingstring[1:-1])
        if loop_pos == 7:
            # look for first qty
            spq = s.split(':')
            secPT_QTY = int(spq[1])
            PTCount += 1
        if loop_pos == 9:
            # look for first qty
            spq = s.split(':')
            holdingstring = spq[2]
            secPT_Val = float(holdingstring[1:-1])
        loop_pos += 1

    dic_build = ''
    loop_dic = 0
    commaseperator: str = ','
    for loop_dic in range(0, PTCount):
        if dic_build == '':
            commaseperator = ''
        else:
            commaseperator = ','

        dic_build = dic_build + commaseperator + "'" + str(loop_dic) + "':{'num':" + str(0) + ",'qty':" + str(1) + ",'price':" + str(0.0) + ",'tiercount':" + str(PTCount) + "}"

    full_dict:dict = "{" + dic_build + "}"
    return full_dict




shop_url = "https://%s:%s@dans-daily-deals.myshopify.com/admin" % ('1cc67033ddfda73bbdf799798fabe9dc', '6c9663bcdabfecf9ab0ffe2658b6f64f')

shopify.ShopifyResource.set_site(shop_url)


shop = shopify.Shop.current

#get all products from approved food
import pandas as pd
import pymysql
from sqlalchemy import create_engine

#engine = create_engine('mysql+pymysql://lh4:approved2010@10.1.1.6/myticket')
engine = create_engine('mysql+pymysql://root:v#jPJ2Eb&Shv@46.37.182.203/approvedfood')

datatable = pd.read_sql_query('SELECT products.ID, products.LONG_DESC, products.STOCK_LEVEL, products.FULL_NAME, products.CATS, products.PRICE, products.RRP_PRICE, products.BB_DATE, products.name_mid, products.brand, products.promo_prefix, products.promo_suffix, products.SHIP_WEIGHT, products.weight2, products.BARCODE, products.PRICE_TIERS, products.deal_text, products.IMAGES, products.PRICE_SALE FROM approvedfood.products products WHERE products.STOCK_LEVEL > 5000', engine)
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
    im1=str(row['IMAGES'])
    im2= Core_Shopify.de_serialized(im1)
    filep= im2[0][b'file'].decode("utf-8")
    pt1 =  Core_Shopify.de_serialized(str(row['PRICE_TIERS']))


    image_filename = "http://fthumb.approvedfood.co.uk/thumbs/75/1000/1000/1/src_images/" + str(filep)

    image1 = shopify.Image()
    image1.src = image_filename
    print(image1.src)
    new_product.images = [image1]
    success = new_product.save()
    #From the price tiers work out the varient count
    p = row['PRICE_TIERS']

    d = create_pricing_dict(p)
    print(type(d))

    # returns false if the record is invalid
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
    success = new_product.save()
    '''
    
     vb=shopify.Variant()

    new_product.add_variant(vb)
    
    new_product.attributes['variants'][1].attributes['barcode'] = str(row['BARCODE'])
    new_product.attributes['variants'][1].attributes['compare_at_price'] = str(row['BARCODE'])
    # new_product.attributes['variants'][0].attributes['grams'] = 12345
    new_product.attributes['variants'][1].attributes['inventory_quantity'] = str(row['STOCK_LEVEL'])
    new_product.attributes['variants'][1].attributes['price'] = str(row['PRICE'])
    new_product.attributes['variants'][1].attributes['sku'] = str(row['ID'])
    new_product.attributes['variants'][1].attributes['taxable'] = True
    new_product.attributes['variants'][1].attributes['title'] = str(row['FULL_NAME'])
    new_product.attributes['variants'][1].attributes['weight'] = float(row['SHIP_WEIGHT'])
    new_product.attributes['variants'][1].attributes['weight_unit'] = 'kg'
    new_product.attributes['variants'][1].attributes['inventory_management'] = 'shopify'
    # inventory-management>shopify
    pricet=str(row['PRICE_TIERS'])
    #a:2:{i:0;a:2:{s:3:"qty";i:1;s:5:"price";s:4:"0.39";}i:1;a:2:{s:3:"qty";i:3;s:5:"price";s:4:"0.33";}}
    print(pricet)
    print(d)
    success = new_product.save()

    '''

