from shopify import Product
import shopify


shop_url = "https://%s:%s@dans-daily-deals.myshopify.com/admin" % ('461824c0a06d4be0e94851deeabc3965', '9bb4f551ba4888c9199b7a9509f0e872')

shopify.ShopifyResource.set_site(shop_url)

new_product = Product()

pid = 0

new_product.vendor = "Vendor"
new_product.title = "New Product"
new_product.product_type = "Chocolate bar"
new_product.body_html = "some html"

image_filename = "http://fthumb.approvedfood.co.uk/thumbs/75/1000/296/1/src_images/hersheys_creamy_milk_chocolate_with_almonds_43g.jpg"

image1 = shopify.Image()
image1.src = image_filename
print(image1.src)
new_product.images = [image1]

success = new_product.save()  # returns false if the record is invalid
new_product.attributes['variants'][0].attributes['barcode']='12345'
new_product.attributes['variants'][0].attributes['compare_at_price']='12345'
new_product.attributes['variants'][0].attributes['grams']=12345
new_product.attributes['variants'][0].attributes['inventory_quantity']=10
new_product.attributes['variants'][0].attributes['price']='12345'
new_product.attributes['variants'][0].attributes['sku']='12345'
new_product.attributes['variants'][0].attributes['taxable']=True
new_product.attributes['variants'][0].attributes['title']='12345'
new_product.attributes['variants'][0].attributes['weight']=1.0
new_product.attributes['variants'][0].attributes['weight_unit']='kg'
new_product.attributes['variants'][0].attributes['inventory_management']='shopify'
#inventory-management>shopify

success = new_product.save()
print(success)
'''
pid = new_product.id
#product3 = P.Product()
product3 = shopify.Product.find(int(pid))


#new_product.add_variant(new_variant)

success = product3.save()
print(product3.errors)









'''
