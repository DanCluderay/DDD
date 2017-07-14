import requests
import json
import shopify
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import uuid
import pymysql


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

def set_web_dataset(sqlstring):
    'Returns a pandas dataset'
    engine = create_engine('mysql+pymysql://root:v#jPJ2Eb&Shv@46.37.182.203/approvedfood')

    conn = pymysql.connect(host='46.37.182.203', port=3306, user='root', passwd='v#jPJ2Eb&Shv', db='approvedfood',autocommit=True)
    cur = conn.cursor()
    t=cur.execute(sqlstring)
    print(t)

def get_web_dataset(sqlstring):
    'Returns a pandas dataset'
    engine = create_engine('mysql+pymysql://root:v#jPJ2Eb&Shv@46.37.182.203/approvedfood')
    dt = pd.read_sql_query(sqlstring, engine)

    return dt

def get_mt_dataset(sqlstring):
    engine = create_engine('mysql+pymysql://lh4:approved2010@10.1.1.6/myticket')
    dt:pd
    try:
        dt = pd.read_sql_query(sqlstring,engine)
    finally:
        pass
    return dt

def create_web_user(shopifyuserid='',username='',useremail='',displayname='',title='', firstname='', secondname='', line1='', line2 ='', postcode='', town='', region='', company='',countrycode='0',phone='',mobile='',hearaboutus='', regdate='2000-01-01 00:00:00'):
    '''check to see if a the customer'''
    userdataid:str=''
    userid_sql = str('SELECT `ID` FROM `users` WHERE `user_data`=\'' + str(shopifyuserid) + '\'')
    dt = get_web_dataset(userid_sql)
    newcustomerid = int(dt.iloc[0]['ID'])
    if newcustomerid==0:
        userdataid=uuid.uuid4()
        sqlstring:str='INSERT INTO `users` (`ID`, `USER_NAME`, `USER_EMAIL`, `USER_PASS`, `USER_TYPE`, `DISPLAY_NAME`, `logged_in`, `DATE`, `TITLE`, `USER_FIRSTNAME`, `USER_SURNAME`, `LINE1`, `LINE2`, `POSTCODE`, `TOWN`, `region`, `company`, `COUNTRY`, `PHONE`, `MOBILE_PHONE`, `LISTS`, `STORE`, `SAGE_REF`, `HEAR_ABOUT_US`, `CREDIT`, `MARKETING_OK`, `referee_name`, `date_registered`, `registration_inbound_url`, `af_commissionlevel`, `affiliate_id`, `referer_id`, `is_affiliate`, `affiliate_status`, `postcode2`, `affiliate_credit`, `verified`, `strike_count`, `Deal_count`, `pay_google`, `default_shipmethod`, `fb_userid`, `fb_username`, `fb_blob`, `prefs`, `dupe_reason`, `dupe_id`, `per_item_limit`, `can_use_payflow`, `js_callback`, `user_data`, `user_data_id`, `ip_address`, `http_agent`, `http_accept`, `business_type`, `business_vat`, `business_regnum`, `business_size`, `business_turnover`, `order_count`, `user_email_checked`, `user_email_result`, `email_sent`, `email_open`, `email_bounce`, `email_read`, `email_deleted`, `email_bounce_reason`, `activation_key`, `activation_expires`, `secret_q`, `secret_a`, `nonce`, `interfinancial_params`, `reminder1_sent`, `reminder2_sent`, `CHECKOUT_REMINDERS`, `bypass_cc_enrolled`, `affiliate_scheme`, `affiliate_por_id`, `is_enabled`, `is_cash_affiliate`, `biz_id`, `mail_priority`, `access_level`) VALUES (NULL, \'' + username + '\', \'' + useremail + '\', \'\', \'0\', \'' + displayname + '\', \'2000-01-01 00:00:00\', CURRENT_TIMESTAMP, \'' + title + '\', \'' + firstname + '\', \'' + secondname + '\', \'' + line1 + '\', \'' + line2 + '\', \'' + postcode + '\', \'' + town + '\', \'' + region + '\', \'' + company + '\', \'' + countrycode + '\', \'' + phone + '\', \'' + mobile + '\', NULL, \'1\', \'NONE\', \'' + hearaboutus + '\', \'0.00\', \'1\', \'Shopify\', \'' + regdate + '\', \'reg inbound url\', \'\', \'\', \'\', \'0\', \'\', \'\', \'0.0\', \'0\', \'0\', \'0\', \'0\', \'\', \'0\', \'\', \'\', \'\', \'\', \'0\', \'30.00\', \'1\', \'0\', \'' + str(shopifyuserid) + '\', \'' + str(userdataid) + '\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'\', \'0\', \'1970-01-01 00:00:00\', \'\', \'0\', \'0\', \'0\', \'0\', \'0\', \'\', \'\', \'1970-01-01 00:00:00\', \'0\', NULL, \'\', \'\', \'1970-01-01 00:00:00\', \'1970-01-01 00:00:00\', \'1\', \'0\', \'0\', \'\', \'1\', \'0\', \'10\', \'100\', \'0\');'
        print(sqlstring)
        set_web_dataset(sqlstring)
    else:
        userdataid=shopifyuserid

    dt = get_web_dataset(userid_sql)
    newcustomerid = int(dt.iloc[0]['ID'])
    return newcustomerid

def create_web_order(shopifyorderid='0',userid=0,userinfo='',shopitems='',horderdate='0000-00-00 00:00:00.000000',deliveryaddress='',deliverynote='',charge=0,shipcharge=0,gross_basket=0,gross_ship=0.00 ,ship_method='',pay_method='',payid='',order_status='',discount_code='',discount_amount=0.0,discountarray='',accept_substitues=0,stockreduced=0,creditused=0.00,creditapplied=0.00,shipping_discount_used=0.00,shipping_expected_from='0000-00-00 00:00:00.000000',shipping_expected_to='0000-00-00 00:00:00.000000',txn_id='',cart_uniqid='',affiliate_id='',affiliate_spend=0.00,affiliate_spend_applied=0.00,ORDER_EXPIRE=0,rec_done=0,paypal_form='',paypal_items='',tracking_url='',carrier='',shipref='',debug_summary='',sec_ip_address='',sec_http_agent_id='',sec_http_agent='',parent_order_id=0,reminder1_sent='',reminder2_sent='',priority=0,picked_by='',pick_position=0,pick_valid=0,priority_pick=0,affiliate_por_id='',vp_converted='',currency='GBP',currency_rate=0.00,payment=0,biz_id=4,ship_boost_priority=0,ship_boost_paid=0.00,food_bank_id=0):
    sqlstring='INSERT INTO `orders` (`ID`, `liquid_id`, `USER_ID`, `session_id`, `USER_INFO`, `ITEMS`, `DELIVERY_ADDRESS`, `DELIVERY_NOTE`, `ORDER_DATE`, `hORDER_DATE`, `CHARGE`, `SHIP_CHARGE`, `gross_basket`, `gross_ship`, `SHIP_METHOD`, `PAY_METHOD`, `PAY_ID`, `ORDER_STATUS`, `DISCOUNT_CODE`, `DISCOUNT_AMOUNT`, `DISCOUNT_ARRAY`, `ACCEPT_SUBSTITUTES`, `STOCK_REDUCED`, `CREDIT_USED`, `CREDIT_APPLIED`, `shipping_discount_used`, `shipping_expected_from`, `shipping_expected_to`, `txn_id`, `cart_uniqid`, `affiliate_id`, `affiliate_spend`, `affiliate_spend_applied`, `ORDER_EXPIRE`, `rec_done`, `paypal_form`, `paypal_items`, `tracking_url`, `carrier`, `shipref`, `debug_summary`, `sec_ip_address`, `sec_http_agent_id`, `sec_http_agent`, `parent_order_id`, `reminder1_sent`, `reminder2_sent`, `priority`, `picked_by`, `pick_position`, `pick_valid`, `priority_pick`, `affiliate_por_id`, `vp_converted`, `currency`, `currency_rate`, `payment`, `biz_id`, `ship_boost_priority`, `ship_boost_paid`, `food_bank_id`) VALUES (NULL, \'0\', \'' + str(userid) + '\',\'' + str(shopifyorderid) +'\',\'' + str(userinfo) + '\',\'' + str(shopitems) + '\',\'' + str(deliveryaddress) + '\',\'' + str(deliverynote) + '\', \'\',\'' + str(horderdate) + '\',\'' + str(charge ) + '\',\'' + str(shipcharge) + '\',\'' + str(gross_basket) + '\',\'' + str(gross_ship) + '\',\'' + str(ship_method) + '\',\'' + str(pay_method) + '\',\'' + str(payid) + '\',\'' + str(order_status) + '\',\'' + str(discount_code) + '\',\'' + str(discount_amount) + '\',\'' + str(discountarray) + '\',\'' + str(accept_substitues) + '\',\'' + str(stockreduced) + '\',\'' + str(creditused) + '\',\'' + str(creditapplied) + '\',\'' + str(shipping_discount_used) + '\',\'' + str(shipping_expected_from) + '\',\'' + str(shipping_expected_to) + '\',\'' + str(txn_id) + '\',\'' + str(cart_uniqid) + '\',\'' + str(affiliate_id) + '\',\'' + str(affiliate_spend) + '\',\'' + str(affiliate_spend_applied) + '\',\'' + str(ORDER_EXPIRE) + '\',\'' + str(rec_done) + '\',\'' + str(paypal_form) + '\',\'' + str(paypal_items) + '\',\'' + str(tracking_url) + '\',\'' + str(carrier) + '\',\'' + str(shipref) + '\',\'' + str(debug_summary) + '\',\'' + str(sec_ip_address) + '\',\'' + str(sec_http_agent_id) + '\',\'' + str(sec_http_agent) + '\',\'' + str(parent_order_id) + '\',\'' + str(reminder1_sent) + '\',\'' + str(reminder2_sent) + '\',\'' + str(priority) + '\',\'' + str(picked_by) + '\',\'' + str(pick_position) + '\',\'' + str(pick_valid) +  '\',\'' + str(priority_pick) + '\',\'' + str(affiliate_por_id) + '\',\'' + str(vp_converted) + '\',\'' + str(currency) + '\',\'' + str(currency_rate) + '\',\'' + str(payment) + '\',\'' + str(biz_id) + '\',\'' + str(ship_boost_priority) + '\',\'' + str(ship_boost_paid) + '\',\'' + str(food_bank_id) + '\')'
    print(sqlstring)

def create_web_items(itemsdictarray):
    #loop the items
    #build up the ID, qty and price variable
    totalLines= len(itemsdictarray)
    firstpart='a:' + str(totalLines) + ':{' #total number of items
    linecounter:int=0
    line_inst:str=''
    for dict_item in itemsdictarray:

        paramnumbers:int=22
        line_inst = 'i:' + str(linecounter) + ';a:' + str(paramnumbers) + ':{'# example i:0;a:15:
        midpart:str=''
        for lineparam in range(0,paramnumbers):
            productid:int=111
            catid:int=111
            qty:int=111
            productname:str='this'
            weight:str='5'
            rrp:str='1.00'
            bbedate:str='1970-01-01 00:00:00'
            vatable:str='1'
            vattable_rate:str='1'
            shipping_discount:str='1'
            price_total:float=0.00
            price:float=0.00
            price_novat:float=0.00
            price_vattotal:float=0.00
            applied_price_total:float=0.00
            applied_shipping_discount:str='0.00'
            if lineparam==0:
                #productID
                midpart='s:2:\"id\";i:' + str(productid)
            elif lineparam == 1:
                # catID
                midpart = midpart.__add__(';s:6:\"cat_id\";i:' + str(catid))
            elif lineparam == 2:
                # qty
                midpart = midpart.__add__(';s:3:\"qty\";i:' + str(qty))
            elif lineparam == 3:
                # weight
                weightlen=len(weight)
                midpart = midpart.__add__(';s:6:\"weight\";s:' + str(weightlen) + ':\"' + str(weight) + '\"')
            elif lineparam == 4:
                #name
                productnamelen=len(productname)
                midpart = midpart.__add__(';s:4:\"name\";s:' + str(productnamelen) + ':\"' + str(productname) + '\"')

            elif lineparam == 5:
                #rrp s:3:"rrp";s:4:"0.85"
                rrplen=len(rrp)
                midpart = midpart.__add__(';s:3:\"rrp\";s:' + str(rrplen) + ':\"' + str(rrp) + '\"')
            elif lineparam == 6:
                #s:7:"bb_date";s:19:"2017-07-12 00:00:00"
                bbelen=len(bbedate)
                midpart = midpart.__add__(';s:7:\"bb_date\";s:' + str(bbelen) + ':\"' + str(bbedate) + '\"')
            elif lineparam == 7:
                #s:8:"vattable";s:1:"1"
                vatablelen=len(vatable)
                midpart = midpart.__add__(';s:8:\"vattable\";s:' + str(vatablelen) + ':\"' + str(vatable) + '\"')
            elif lineparam == 8:
                #s:13:"vattable_rate";s:4:"1.00"
                vatvalueratelen=len(vattable_rate)
                midpart = midpart.__add__(';s:13:\"vattable_rate\";s:' + str(vatvalueratelen) + ':\"' + str(vattable_rate) + '\"')
            elif lineparam == 9:
                #s:9:"blacklist";s:0:""
                midpart = midpart.__add__(';s:9:\"blacklist\";s:0:\"\"')
            elif lineparam == 10:
                #;s:17:"discount_template";N
                midpart = midpart.__add__(';s:17:\"discount_template\";N')
            elif lineparam == 11:
                #;s:17:"shipping_discount";s:4:"0.00"
                shippingdiscountlen=len(shipping_discount)
                midpart = midpart.__add__(';s:17:\"shipping_discount\";s:' + str(shippingdiscountlen) + ':\"' + str(shipping_discount) + '\"')
            elif lineparam == 12:
                #s:6:"fb_qty";i:0
                midpart = midpart.__add__(';s:6:\"fb_qty\";i:0')
            elif lineparam == 13:
                #s:6:"biz_id";s:1:"1"
                midpart = midpart.__add__(';s:6:\"biz_id\";s:1:\"1\"')
            elif lineparam == 14:
                #;s:11:"price_total";d:0.25
                midpart = midpart.__add__(';s:11:\"price_total\";d:' + str(price_total))
            elif lineparam == 15:
                #s:5:"price";d:0.25
                midpart = midpart.__add__(';s:5:\"price\";d:' + str(price))
            elif lineparam == 16:
                #;s:11:"price_novat";d:0.20999999999999999
                midpart = midpart.__add__(';s:11:\"price_novat\";d:' + str(price_novat))
            elif lineparam == 17:
                #;s:14:"price_vattotal";d:0.040000000000000001
                midpart = midpart.__add__(';s:14:\"price_vattotal\";d:' + str(price_vattotal))
            elif lineparam == 18:
                #a:8:{s:5:"range";s:2:"4+";s:4:"save";s:4:"0.04";s:8:"qty_from";i:4;s:6:"qty_to";i:0;s:3:"vat";d:0.25;s:5:"novat";d:0.20999999999999999;s:11:"vat_applied";d:0.040000000000000001;s:3:"qty";i:4;}
                pricet:str=';s:10:\"price_tier\";a:8:{s:5:\"range\";s:2:\"4+\";s:4:\"save\";s:4:\"0.04\";s:8:\"qty_from\";i:4;s:6:\"qty_to\";i:0;s:3:\"vat\";d:0.25;s:5:\"novat\";d:0.20999999999999999;s:11:\"vat_applied\";d:0.040000000000000001;s:3:\"qty\";i:4;}'
                midpart = midpart.__add__(pricet)
            elif lineparam == 19:
                #s:11:"applied_qty";i:4
                applied_qty:str='s:11:\"applied_qty\";i:4'
                midpart = midpart.__add__(applied_qty)
            elif lineparam == 20:
                #;s:19:"applied_price_total";d:0.25
                midpart = midpart.__add__(';s:19:\"applied_price_total\";d:' + str(applied_price_total))
            elif lineparam == 21:
                #s:25:"applied_shipping_discount";s:4:"0.00";}
                applied_shipping_discountlen = len(applied_shipping_discount)
                midpart = midpart.__add__(';s:25:\"applied_shipping_discount\";s:' + str(applied_shipping_discountlen) + ':\"' + str(applied_shipping_discount) + '\";}')
        line_inst = line_inst.__add__(midpart)
        line_inst = line_inst.__add__('}')

        linecounter+=1
    firstpart=firstpart.__add__(line_inst)
    return firstpart
