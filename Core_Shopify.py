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

def create_mt_order(shopifyorderid,userid=0):
    sqlstring='INSERT INTO `orders` (`ID`, `liquid_id`, `USER_ID`, `session_id`, `USER_INFO`, `ITEMS`, `DELIVERY_ADDRESS`, `DELIVERY_NOTE`, `ORDER_DATE`, `hORDER_DATE`, `CHARGE`, `SHIP_CHARGE`, `gross_basket`, `gross_ship`, `SHIP_METHOD`, `PAY_METHOD`, `PAY_ID`, `ORDER_STATUS`, `DISCOUNT_CODE`, `DISCOUNT_AMOUNT`, `DISCOUNT_ARRAY`, `ACCEPT_SUBSTITUTES`, `STOCK_REDUCED`, `CREDIT_USED`, `CREDIT_APPLIED`, `shipping_discount_used`, `shipping_expected_from`, `shipping_expected_to`, `txn_id`, `cart_uniqid`, `affiliate_id`, `affiliate_spend`, `affiliate_spend_applied`, `ORDER_EXPIRE`, `rec_done`, `paypal_form`, `paypal_items`, `tracking_url`, `carrier`, `shipref`, `debug_summary`, `sec_ip_address`, `sec_http_agent_id`, `sec_http_agent`, `parent_order_id`, `reminder1_sent`, `reminder2_sent`, `priority`, `picker_id`, `picked_by`, `pick_position`, `pick_valid`, `priority_pick`, `affiliate_por_id`, `vp_converted`, `currency`, `currency_rate`, `payment`, `biz_id`, `ship_boost_priority`, `ship_boost_paid`, `food_bank_id`) VALUES (NULL, 0, ' + str(userid) + ', ' + str(shopifyorderid) +', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'0\', \'\', \'\', \'0\', \'0.00\', \'0.00\', \'0.00\', \'0000-00-00 00:00:00.000000\', \'0000-00-00 00:00:00.000000\', NULL, NULL, \'\', \'0.00\', \'0\', \'0\', \'0\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'0\', \'0\', '', \'0\', \'0\', \'0\', '', \'0\', \'GBP\', \'1\', \'1\', \'1\', \'1\', \'0.00\', \'1\'), (NULL, \'0\', '', '', '', '', '', '', '', '', '', '', \'-1.00\', \'-1.00\', '', '', '', '', '', \'0.000000\', '', '', \'0\', \'0.00\', \'0\', \'0.00\', \'0000-00-00 00:00:00.000000\', \'0000-00-00 00:00:00.000000\', NULL, NULL, '', \'0.00\', \'0\', \'0\', \'0\', '', '', '', '', '', '', '', '', '', \'0\', '', '', \'0\', \'0\', '', \'0\', \'0\', \'0\', '', \'0\', \'GBP\', \'1\', \'0\', \'4\', \'0\', \'0.00\', \'0\');'
