import requests
from bs4 import BeautifulSoup

print("Rozetka Parser 2000.")
print
url = 'http://rozetka.com.ua/mobile-phones/c80003/preset=budget_smartphones/'
print(url)

headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
      }

proxies = {
    'http': 'socks5://127.0.0.1:9150',
    'https': 'socks5://127.0.0.1:9150'
}

r = requests.get(url, headers=headers, proxies=proxies)

print (r.status_code)
print ("REQUEST:")
print (r.request.headers)
print ("RESPONSE:")
print (r.headers)

fp = r.content

soup = BeautifulSoup(fp, "lxml")
catalog_list = soup.find('div', {'id': 'catalog_goods_block'})
items = catalog_list.find_all('div', {'class': 'g-i-tile g-i-tile-catalog'})

for item in items:
    item_link = item.find('div', {'class': 'g-i-tile-i-title clearfix'}).find('a').get('href')
    item_name = item.find('div', {'class': 'g-i-tile-i-title clearfix'}).find('a').text
    item_price = item.find('div', {'class': 'g-price-uah'})
    item_img = item.findAll('img')[1].get('src')
    print item_name
    print item_link
    print item_price
    print item_img
    
raw_input("Pres any key.")