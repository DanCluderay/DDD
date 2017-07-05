import requests
import json
import shopify
keyp:str ="461824c0a06d4be0e94851deeabc3965"
passp:str  ="9bb4f551ba4888c9199b7a9509f0e872"
urlstart:str ="https://dans-daily-deals.myshopify.com/admin"

def get_all_products():
    pd=shopify.Product()
    pd = requests.get(urlstart + "/products/count.json",auth=(keyp,passp))

    print(pd)


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
    for key in j:
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
            pass
        elif key == 'financial_status':
            pass
        elif key == 'fulfillment_status':
            pass
        elif key == 'gateway':
            pass
        elif key == 'id':
            pass
        elif key == 'landing_site':
            pass
        elif key == 'landing_site_ref':
            pass
        elif key == 'location_id':
            pass
        elif key == 'name':
            pass
        elif key == 'note':
            pass
        elif key == 'number':
            pass
        elif key == 'order_number':
            pass
        elif key == 'order_status_url':
            pass
        elif key == 'phone':
            pass
        elif key == 'processed_at':
            pass
        elif key == 'processing_method':
            pass
        elif key == 'reference':
            pass
        elif key == 'referring_site':
            pass
        elif key == 'source_identifier':
            pass
        elif key == 'source_name':
            pass
        elif key == 'source_url':
            pass
        elif key == 'subtotal_price':
            pass
        elif key == 'tags':
            pass
        elif key == 'taxes_included':
            pass
        elif key == 'test':
            pass
        elif key == 'token':
            pass
        elif key == 'total_discounts':
            pass
        elif key == 'total_line_items_price':
            pass
        elif key == 'total_price':
            pass
        elif key == 'total_price_usd':
            pass
        elif key == 'total_tax':
            pass
        elif key == 'total_weight':
            pass
        elif key == 'updated_at':
            pass
        elif key == 'user_id':
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
        elif key == '':
            pass

get_all_products()
get_all_orders()

