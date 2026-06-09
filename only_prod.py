import requests
from lxml import html
from rich import  print
import time
import json
import gzip
import re

cookies = {
    'localization': 'IN',
    '_shopify_y': 'c69beb4a-f7e0-46a0-9718-7971162392ec',
    'WISHLIST_TOTAL': '0',
    'WISHLIST_PRODUCTS_IDS': '{}',
    'WISHLIST_PRODUCTS_IDS_SET': '1',
    'WISHLIST_UUID': 'null',
    'WISHLIST_IP_ADDRESS': '45.114.65.131',
    '_shopify_s': 'c765777e-5948-4e04-a8f1-911a8db14bc4',
    '_shopify_analytics': ':AZ5KPb9TAAEA1IZM28YhCZiigIQEHOR4G_gM8SVGdkzzl3Z3jd7BtflapjYVOMTgRL7CqHixeD-IrNFrRfrOnVl2Avqk8uzHp4inxG4YD8CtaQ:',
    '_shopify_marketing': ':AZ5KPb9UAAEAH88f8HwR2tDt6ovjMuaa18HiPidmP6I5SM4NHlXVoyF1frCfFstiDUwtH6eDnXCIQacczAqDKI75Gvw:',
    '_shopify_essential': ':AZ5KPb8_AAEA3fiIrIcYONC6Q-DWyKCS5cUWhFuGWwmyuNgc599249Tk9RgLy2zEgKza360T69vL74VNwb_yn3nFJBVOBAo-ceIgOHSCO9U73nuE5EGy1oPqbfY5YZWEUKabqD39mSDR-sSu5zZL_B3sC00bWOi-uPzQ80LVu7L0CsAlXxAFRKolShfhI_nDUaLjr1sbyVRfHFRLzJbIh9Rl_iO2jZ8F_xzA-zbbyOhbrLQ8numNItPtiTPg6n35a3JZ4vl9L2dyZZuT2N-MTnwY7LJI9382X2UFx_u0mxCDHzI8vAt3qVD5ONRwW4uJMKgRR8ZlgRGDhQSyzYanbko4QdGGLd0UtgT02xq9po_iMbuk_cQ9y8L7RM-W_jigp55-atr-77Xjh46Zh-327yMXOfZ8AescawdRAFVCgV1WbPEIlFxHhRXCyFuX6ODZFk0A:',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
     'cookie': 'localization=IN; _shopify_y=c69beb4a-f7e0-46a0-9718-7971162392ec; WISHLIST_TOTAL=0; WISHLIST_PRODUCTS_IDS={}; WISHLIST_PRODUCTS_IDS_SET=1; WISHLIST_UUID=null; WISHLIST_IP_ADDRESS=45.114.65.131; _shopify_s=c765777e-5948-4e04-a8f1-911a8db14bc4; _shopify_analytics=:AZ5KPb9TAAEA1IZM28YhCZiigIQEHOR4G_gM8SVGdkzzl3Z3jd7BtflapjYVOMTgRL7CqHixeD-IrNFrRfrOnVl2Avqk8uzHp4inxG4YD8CtaQ:; _shopify_marketing=:AZ5KPb9UAAEAH88f8HwR2tDt6ovjMuaa18HiPidmP6I5SM4NHlXVoyF1frCfFstiDUwtH6eDnXCIQacczAqDKI75Gvw:; _shopify_essential=:AZ5KPb8_AAEA3fiIrIcYONC6Q-DWyKCS5cUWhFuGWwmyuNgc599249Tk9RgLy2zEgKza360T69vL74VNwb_yn3nFJBVOBAo-ceIgOHSCO9U73nuE5EGy1oPqbfY5YZWEUKabqD39mSDR-sSu5zZL_B3sC00bWOi-uPzQ80LVu7L0CsAlXxAFRKolShfhI_nDUaLjr1sbyVRfHFRLzJbIh9Rl_iO2jZ8F_xzA-zbbyOhbrLQ8numNItPtiTPg6n35a3JZ4vl9L2dyZZuT2N-MTnwY7LJI9382X2UFx_u0mxCDHzI8vAt3qVD5ONRwW4uJMKgRR8ZlgRGDhQSyzYanbko4QdGGLd0UtgT02xq9po_iMbuk_cQ9y8L7RM-W_jigp55-atr-77Xjh46Zh-327yMXOfZ8AescawdRAFVCgV1WbPEIlFxHhRXCyFuX6ODZFk0A:',
}

requests_data = [
    {
        "url": "https://www.only.in/sitemap_products_1.xml",
        "params": {
            "from": "8954882785494",
            "to": "9019441643734"
        }
    },
    {
        "url": "https://www.only.in/sitemap_products_2.xml",
        "params": {
            "from": "9019441709270",
            "to": "9374929912022"}}
    ]
all_urls=[]
start_time=time.time()
for item in requests_data:
    response = requests.get(item["url"],item["params"], cookies=cookies, headers=headers)
    html_content=html.fromstring(response.content)
    urls=html_content.xpath("//url/loc/text()")
    print(f"Found {len(urls)} URLs")
    all_urls.extend(urls)
    
with gzip.open("urls.json.gz", "wt") as f:
    json.dump(all_urls, f, indent=4)

print("Total URLs:", len((all_urls)))



# for url in all_urls[1:]:
#     response=requests.get(url,timeout=20000)
#     product_id=re.search(r'(\d+)',url).group(1)
    
#     with gzip.open(fr"all_urls_response/product_{product_id}.html.gz",'w') as f:
#         f.write(response.content)
# end_time=time.time()
# print(f"\nTotal Time Taken: {end_time - start_time:.2f} seconds")





