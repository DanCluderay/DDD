import requests
import json
import shopify
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


def get_all_orders():
    'this function gets all the orders'

    od=requests.get(urlstart + "/orders.json",auth=(keyp,passp))

    jsondata2:dict
    jsondata2 = dict(json.loads(od.text))

    j:dict  =jsondata2['orders'][0]
    billaddress=j['billing_address']
    shippingaddress=j['shipping_address']
    customerdetails = j['customer']
    c=j.__len__()
    shopify_Order_id:int=0
    Orderref_str:str=''
    Orderref_int: int = 0
    UserID:int=0
    OrderWeight:float=0.0
    UserEmail:str=''
    FirstName:str=''
    SecondName:str=''
    OrderTotal:float=0.0
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
            pass
        elif key == 'contact_email':
            pass
        elif key == 'created_at':
            pass
        elif key == 'currency':
            pass
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
        elif key == '':
            pass
    print('hell yea')
get_all_products()
get_all_orders()

