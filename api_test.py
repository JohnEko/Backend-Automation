from woocommerce import API
from time import sleep
#import pandas as pd



wcapi = API(
    url="http://mystore.local/",
    consumer_key="WC_KEYS",
    consumer_secret="WC_SECRET",
    version="wc/v3",
    timeout=sleep(5)
)

r = wcapi.get("products")
print(r.json())


