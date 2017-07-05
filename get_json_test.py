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



get_all_products()
get_all_orders()

