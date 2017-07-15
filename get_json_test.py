import requests
import json
import shopify
import Core_Shopify
from phpserialize import serialize, unserialize
keyp:str ="461824c0a06d4be0e94851deeabc3965"
passp:str  ="9bb4f551ba4888c9199b7a9509f0e872"
urlstart:str ="https://dans-daily-deals.myshopify.com/admin"

def get_latest_orders():
    o=requests.get(urlstart + '/orders.json?updated_at_min=2017-07-14 15:57:11 EDT -04:00',auth=(keyp,passp))
    print(o)
def get_all_products():
    pd=shopify.Product()
    pd = requests.get(urlstart + "/products/count.json",auth=(keyp,passp))

    print(pd)

def de_serialized(encoded_array):
    b = bytes(encoded_array, 'utf-8')
    data=unserialize(b)
    print(data)
    return data

def get_sample_order():
    import pandas as pd
    import pymysql
    from sqlalchemy import create_engine

    # engine = create_engine('mysql+pymysql://lh4:approved2010@10.1.1.6/myticket')
    engine = create_engine('mysql+pymysql://root:v#jPJ2Eb&Shv@46.37.182.203/approvedfood')

    datatable = pd.read_sql_query(
        'SELECT `ID`,`ITEMS` FROM `orders` WHERE `ID`=4627532',
        engine)
    datatable.head()
    t = pd.DataFrame(datatable)
    for index, row in t.iterrows():
        orderitems= row['ITEMS']
        d=de_serialized(orderitems)
        print(orderitems)

def get_all_orders():
    'this function gets all the orders'

    od=requests.get(urlstart + "/orders.json",auth=(keyp,passp))

    jsondata2:dict
    jsondata2 = dict(json.loads(od.text))

    j:dict  =jsondata2['orders'][1]#just looking at the second order that has a billing address

    if bool(j.get('confirmed','False'))== False:
        return

    billaddress:dict=j['billing_address']
    shippingaddress:dict=j['shipping_address']
    customerdetails:dict = j['customer']
    lineitems=j['line_items']
    af_lineitems =Core_Shopify.create_web_items(lineitems)
    c=j.__len__()
    shopify_Order_id:int=int(j.get('id',0))
    int_shopify_h_order_number:int(j.get('order_number',0))
    str_shopify_h_order_number:str=str(j.get('name',''))


    OrderWeight:float=float(j.get('total_weight',0.00))

    customeremail:str=str(customerdetails.get('email',''))
    shopify_customer_id:str=(customerdetails.get('id',''))
    address1:str=str(shippingaddress.get('address1',''))
    address2: str = str(shippingaddress.get('address2', ''))
    city: str = str(shippingaddress.get('city', ''))
    company: str = str(shippingaddress.get('company', ''))
    country: str = str(shippingaddress.get('country', ''))
    countrycode: str = str(shippingaddress.get('countrycode', ''))
    FirstName: str = str(shippingaddress.get('first_name', ''))
    SecondName: str = str(shippingaddress.get('last_name', ''))
    phone:str=str(shippingaddress.get('phone', ''))
    zip: str = str(shippingaddress.get('zip', ''))
    province:str=str(shippingaddress.get('province', ''))
    province_code: str = str(shippingaddress.get('province_code', ''))
    total_price:float=float(j.get('total_price',0.00))
    currency: str = str(j.get('currency','GBP'))
    orderdate:str = str(j.get('processed_at','1970-01-01 00:00:00:00'))



    order_note:str=str(j.get('note',''))
    basket_price:float=float(j.get('total_line_item_price',0.00))
    OrderToken:str =str(shippingaddress.get('token', ''))
    OrderTotalDiscounts:float=float(j.get('total_discounts',0.00))

    OrderTotalTax:float=float(j.get('total_tax',0.00))

    marketingokbool:bool=j['buyer_accepts_marketing']
    marketingok_val:str = '0'
    if marketingokbool==True:
        marketingok_val='1'
    else:
        marketingok_val='0'

    webUserID=Core_Shopify.create_web_user(shopifyuserid=shopify_customer_id, firstname=FirstName,secondname=SecondName,useremail=customeremail,line1=address1,line2=address2,phone=phone,marketingok=marketingok_val)
    print(webUserID)

    Core_Shopify.create_web_order(shopifyorderid=shopify_Order_id,userid=webUserID,shopitems=af_lineitems,horderdate='2016-01-01 00:00:00',deliveryaddress=address1,deliverynote=order_note,charge=total_price,shipcharge=0,gross_basket=basket_price,gross_ship=0.00 ,ship_method='New',txn_id='26',currency=currency,biz_id=10)
#get_sample_order()
#get_all_products()
#get_all_orders()
get_latest_orders()

