import requests
import json
import shopify
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import uuid


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



def get_web_dataset(sqlstring):
    'Returns a pandas dataset'
    engine = create_engine('mysql+pymysql://root:v#jPJ2Eb&Shv@46.37.182.203/approvedfood')
    datatable = pd.read_sql_query(sqlstring,engine)
    return datatable

def get_mt_dataset(sqlstring):
    engine = create_engine('mysql+pymysql://lh4:approved2010@10.1.1.6/myticket')
    datatable = pd.read_sql_query(sqlstring,engine)
    return datatable

def create_web_order(shopifyorderid='0',userid=0,userinfo='',shopitems='',horderdate='0000-00-00 00:00:00.000000',deliveryaddress='',deliverynote='',charge=0,shipcharge=0,gross_basket=0,gross_ship=0.00 ,ship_method='',pay_method='',payid='',order_status='',discount_code='',discount_amount=0.0,discountarray='',accept_substitues=0,stockreduced=0,creditused=0.00,creditapplied=0.00,shipping_discount_used=0.00,shipping_expected_from='0000-00-00 00:00:00.000000',shipping_expected_to='0000-00-00 00:00:00.000000',txn_id='',cart_uniqid='',affiliate_id='',affiliate_spend=0.00,affiliate_spend_applied=0.00,ORDER_EXPIRE=0,rec_done=0,paypal_form='',paypal_items='',tracking_url='',carrier='',shipref='',debug_summary='',sec_ip_address='',sec_http_agent_id='',sec_http_agent='',parent_order_id=0,reminder1_sent='',reminder2_sent='',priority=0,picked_by='',pick_position=0,pick_valid=0,priority_pick=0,affiliate_por_id='',vp_converted='',currency='GBP',currency_rate=0.00,payment=0,biz_id=4,ship_boost_priority=0,ship_boost_paid=0.00,food_bank_id=0):
    sqlstring='INSERT INTO `orders` (`ID`, `liquid_id`, `USER_ID`, `session_id`, `USER_INFO`, `ITEMS`, `DELIVERY_ADDRESS`, `DELIVERY_NOTE`, `ORDER_DATE`, `hORDER_DATE`, `CHARGE`, `SHIP_CHARGE`, `gross_basket`, `gross_ship`, `SHIP_METHOD`, `PAY_METHOD`, `PAY_ID`, `ORDER_STATUS`, `DISCOUNT_CODE`, `DISCOUNT_AMOUNT`, `DISCOUNT_ARRAY`, `ACCEPT_SUBSTITUTES`, `STOCK_REDUCED`, `CREDIT_USED`, `CREDIT_APPLIED`, `shipping_discount_used`, `shipping_expected_from`, `shipping_expected_to`, `txn_id`, `cart_uniqid`, `affiliate_id`, `affiliate_spend`, `affiliate_spend_applied`, `ORDER_EXPIRE`, `rec_done`, `paypal_form`, `paypal_items`, `tracking_url`, `carrier`, `shipref`, `debug_summary`, `sec_ip_address`, `sec_http_agent_id`, `sec_http_agent`, `parent_order_id`, `reminder1_sent`, `reminder2_sent`, `priority`, `picked_by`, `pick_position`, `pick_valid`, `priority_pick`, `affiliate_por_id`, `vp_converted`, `currency`, `currency_rate`, `payment`, `biz_id`, `ship_boost_priority`, `ship_boost_paid`, `food_bank_id`) VALUES (NULL, \'0\', \'' + str(userid) + '\',\'' + str(shopifyorderid) +'\',\'' + str(userinfo) + '\',\'' + str(shopitems) + '\',\'' + str(deliveryaddress) + '\',\'' + str(deliverynote) + '\', \'\',\'' + str(horderdate) + '\',\'' + str(charge ) + '\',\'' + str(shipcharge) + '\',\'' + str(gross_basket) + '\',\'' + str(gross_ship) + '\',\'' + str(ship_method) + '\',\'' + str(pay_method) + '\',\'' + str(payid) + '\',\'' + str(order_status) + '\',\'' + str(discount_code) + '\',\'' + str(discount_amount) + '\',\'' + str(discountarray) + '\',\'' + str(accept_substitues) + '\',\'' + str(stockreduced) + '\',\'' + str(creditused) + '\',\'' + str(creditapplied) + '\',\'' + str(shipping_discount_used) + '\',\'' + str(shipping_expected_from) + '\',\'' + str(shipping_expected_to) + '\',\'' + str(txn_id) + '\',\'' + str(cart_uniqid) + '\',\'' + str(affiliate_id) + '\',\'' + str(affiliate_spend) + '\',\'' + str(affiliate_spend_applied) + '\',\'' + str(ORDER_EXPIRE) + '\',\'' + str(rec_done) + '\',\'' + str(paypal_form) + '\',\'' + str(paypal_items) + '\',\'' + str(tracking_url) + '\',\'' + str(carrier) + '\',\'' + str(shipref) + '\',\'' + str(debug_summary) + '\',\'' + str(sec_ip_address) + '\',\'' + str(sec_http_agent_id) + '\',\'' + str(sec_http_agent) + '\',\'' + str(parent_order_id) + '\',\'' + str(reminder1_sent) + '\',\'' + str(reminder2_sent) + '\',\'' + str(priority) + '\',\'' + str(picked_by) + '\',\'' + str(pick_position) + '\',\'' + str(pick_valid) +  '\',\'' + str(priority_pick) + '\',\'' + str(affiliate_por_id) + '\',\'' + str(vp_converted) + '\',\'' + str(currency) + '\',\'' + str(currency_rate) + '\',\'' + str(payment) + '\',\'' + str(biz_id) + '\',\'' + str(ship_boost_priority) + '\',\'' + str(ship_boost_paid) + '\',\'' + str(food_bank_id) + '\')'
    print(sqlstring)

def create_web_items(itemsdictarray):
    #loop the items
    #build up the ID, qty and price variable
    totalLines= len(itemsdictarray)
    firstpart='a:' + str(totalLines) + ':{' #total number of items
    linecounter:int=0
    for dict_item in itemsdictarray:

        paramnumbers:int=15
        line_inst = 'i:' + str(linecounter) + ';a:' + str(paramnumbers) + ':'# example i:0;a:15:
        midpart:str=''
        for lineparam in range(0,paramnumbers):
            productid:int=0
            catid:int=0
            qty:int=0
            productname:str=''
            weight:float=0.00
            rrp:str=''
            if lineparam==0:
                #productID
                midpart='s:2:\"id\";i:' + str(productid)
            elif lineparam == 1:
                # catID
                midpart = midpart.__add__(';s:6:"cat_id";i:' + str(catid))
            elif lineparam == 2:
                # qty
                midpart = midpart.__add__(';s:3:"qty";i:' + str(qty))
            elif lineparam == 3:
                # weight
                weightlen=len(weight)
                midpart = midpart.__add__(';s:6:"weight";s:' + str(weightlen) + ':\"' + str(weight) + ')\"')
            elif lineparam == 4:
                #name
                productnamelen=len(productname)
                midpart = midpart.__add__(';s:4:"name";s:' + str(productnamelen) + ':\"' + str(productname) + ')\"')

            elif lineparam == 5:
                #rrp s:3:"rrp";s:4:"0.85"
                rrplen=len(rrp)
                midpart = midpart.__add__(';s:3:"rrp";s:' + str(rrplen) + ':\"' + str(rrp) + ')\"')
            elif lineparam == 6:
                pass
            elif lineparam == 7:
                pass
            elif lineparam == 8:
                pass
            elif lineparam == 9:
                pass
            elif lineparam == 10:
                pass
            elif lineparam == 11:
                pass
            elif lineparam == 12:
                pass
            elif lineparam == 13:
                pass
            elif lineparam == 14:
                pass





    linecounter+=1
