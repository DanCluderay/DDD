import requests
import json


#request = requests.Session(auth=('461824c0a06d4be0e94851deeabc3965', '9bb4f551ba4888c9199b7a9509f0e872'))
#print(json.loads(request.get('http://dans-daily-deals.myshopify.com/admin/assets.json').content))

response = requests.get( "https://dans-daily-deals.myshopify.com/admin/products/count.json",
                               auth=("461824c0a06d4be0e94851deeabc3965","9bb4f551ba4888c9199b7a9509f0e872"))
response.text