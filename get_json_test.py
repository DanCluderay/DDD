import requests
import json
import shopify
import Core_Shopify
from phpserialize import serialize, unserialize
keyp:str ="461824c0a06d4be0e94851deeabc3965"
passp:str  ="9bb4f551ba4888c9199b7a9509f0e872"
urlstart:str ="https://dans-daily-deals.myshopify.com/admin"

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
    billaddress:dict=j['billing_address']
    shippingaddress:dict=j['shipping_address']
    customerdetails:dict = j['customer']
    lineitems=j['line_items']
    af_lineitems =Core_Shopify.create_web_items(lineitems)
    c=j.__len__()
    shopify_Order_id:int=0
    Orderref_str:str=''
    Orderref_int: int = 0
    UserID:int=0
    OrderWeight:float=0.0

    customeremail:str=str(customerdetails.get('email',''))
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
    orderdate:str = str(j.get('created_at','1970-01-01 00:00:00:00'))



    OrderNote:str=''
    SubTotalPrice:float=0.0
    OrderToken:str =''
    OrderTotalDiscounts:float=0.0
    OrderTotalLineItemPrice:float=0.0
    OrderDate:str=''
    OrderPhone:str=''
    un_OrderNumber:str=''
    OrderType:str=''
    OrderTotalTax:float=0.0
    orderconfirmed:bool=False




    for key,val in j.items():
        print('key=' + key)
        if key=='browser_ip':
            pass
        elif key=='buyer_accepts_marketing':
            # something
            pass
        elif key == 'cancel_reason':
            pass
        elif key == 'cancelled_at':
            pass
        elif key == 'cart_token':
            pass
        elif key == 'checkout_id':
            pass
        elif key == 'checkout_token':
            pass
        elif key == 'closed_at':
            pass
        elif key == 'confirmed':
            orderconfirmed=bool(val)
        elif key == 'contact_email':
            customeremail=str(val)


        elif key == 'customer_locale':
            pass
        elif key == 'device_id':
            pass
        elif key == 'email':
            UserEmail=val
        elif key == 'financial_status':
            pass
        elif key=='first_name':
            FirstName=val
        elif key == 'fulfillment_status':
            pass
        elif key == 'gateway':
            pass
        elif key == 'id':
            shopify_Order_id=val
        elif key == 'landing_site':
            pass
        elif key == 'landing_site_ref':
            pass
        elif key == 'location_id':
            pass
        elif key == 'name':
            Orderref_str=val
        elif key == 'note':
            OrderNote=val
        elif key == 'number':
            un_OrderNumber=str(val)
        elif key == 'order_number':
            Orderref_int=val
        elif key == 'order_status_url':
            pass
        elif key == 'phone':
            OrderPhone=str(val)
        elif key == 'processed_at':
            OrderDate=str(val)
        elif key == 'processing_method':
            pass
        elif key == 'reference':
            pass
        elif key == 'referring_site':
            pass
        elif key=='last_name':
            SecondName=str(val)
        elif key == 'source_identifier':
            pass
        elif key == 'source_name':
            un_OrderNumber=str(un_OrderNumber)
        elif key == 'source_url':
            pass
        elif key == 'subtotal_price':
            SubTotalPrice=float(val)
        elif key == 'tags':
            pass
        elif key == 'taxes_included':
            pass
        elif key == 'test':
            pass
        elif key == 'token':
            OrderToken=str(val)
        elif key == 'total_discounts':
            OrderTotalDiscounts=float(val)
        elif key == 'total_line_items_price':
            OrderTotalLineItemPrice=float(val)
        elif key == 'total_price':
            OrderTotal=float(val)
        elif key == 'total_price_usd':
            pass
        elif key == 'total_tax':
            OrderTotalTax=float(val)
        elif key == 'total_weight':
            OrderWeight=float(val)
        elif key == 'updated_at':
            pass
        elif key == 'user_id':
            UserID=int(val)
        elif key == 'line_items':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
        elif key == '':
            pass
    print('hell yea')
    #Core_Shopify.create_mt_order(shopifyorderid='1',userid=2,userinfo='3',shopitems='4',horderdate='2016-01-01 00:00:00',deliveryaddress='6',deliverynote='7',charge=8,shipcharge=9,gross_basket=10,gross_ship=11.00 ,ship_method='12',pay_method='13',payid='14',order_status='15',discount_code='16',discount_amount=17.0,discountarray='18',accept_substitues=19,stockreduced=20,creditused=21.00,creditapplied=22.00,shipping_discount_used=23.00,shipping_expected_from='2024-02-02 00:00:00',shipping_expected_to='2025-01-01 00:00:00',txn_id='26',cart_uniqid='27',affiliate_id='28',affiliate_spend=29.00,affiliate_spend_applied=30.00,ORDER_EXPIRE=31,rec_done=32,paypal_form='33',paypal_items='34',tracking_url='35',carrier='36',shipref='37',debug_summary='38',sec_ip_address='39',sec_http_agent_id='40',sec_http_agent='41',parent_order_id=42,reminder1_sent='43',reminder2_sent='44',priority=45,picked_by='46',pick_position=47,pick_valid=48,priority_pick=49,affiliate_por_id='50',vp_converted='51',currency='GBP',currency_rate=53.00,payment=54,biz_id=55,ship_boost_priority=56,ship_boost_paid=57.00,food_bank_id=58)
#get_sample_order()
#get_all_products()
get_all_orders()

