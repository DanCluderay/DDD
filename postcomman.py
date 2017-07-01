import requests
url2 = 'https://461824c0a06d4be0e94851deeabc3965:9bb4f551ba4888c9199b7a9509f0e872@dans-daily-deals.myshopify.com/admin/products.json'
get_response = requests.get(url=url2)
print(get_response)
