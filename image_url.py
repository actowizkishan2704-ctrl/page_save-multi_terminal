import os
import gzip
from lxml import html
from rich import print
import json
from parsel import Selector
import re
import requests


folder_path = r"C:\Users\kishan.prajapati\Desktop\actowiz_work\9-06 day task sitemap & page save\all_urls_response1"
all_img_url=[]
count=0

# for file in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, file)

#     try:
#         # Try reading as gzip
#         with gzip.open(file_path, "rt", encoding="utf-8") as f:
#             data = f.read()

#     except gzip.BadGzipFile:
#         # print(f"Not a gzip file: {file}")

#         # Read normal file
#         with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
#             data = f.read()

#         # Convert to gzip
#         with gzip.open(file_path, "wt", encoding="utf-8") as gz:
#             gz.write(data)
# #     html_content=html.fromstring(data)

def res_image(url, retries = 3):
  for attempt in range(retries):
    try:
      return requests.get(url=url, timeout=20000)
    except Exception as e:
      if attempt > retries:
        return str(e)

for file in os.listdir(folder_path):
  with gzip.open(fr"./all_urls_response1/{file}", 'rt', encoding='utf-8') as f:
      data = f.read()
      
  file_name = file.split('.html')[0]
  
  if not file.split('.html')[0] in os.listdir('all_images'):
    os.mkdir(f'./all_images/{file_name}')
  else:
    print('folder already exists')

  html_content =html.fromstring(data)
  image_urls=html_content.xpath("//div[contains(@class,'product-gallery__media snap-center')]//img/@src")
  
  for image_url in dict.fromkeys(image_urls):
    url = "https:" + image_url
    print(url)
    image_name = re.search(r'(\d+_*[a-z0-9A-Z])', url).group(1)
    if image_name + ".png" not in os.listdir(f'./all_images/{file_name}/'):
      res = res_image(url=url)
      with open(f"./all_images/{file_name}/{image_name}.png", 'wb') as f:
        f.write(res.content)
    else:
      print("image already exists")