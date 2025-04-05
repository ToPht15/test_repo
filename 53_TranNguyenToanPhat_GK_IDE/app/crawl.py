import requests
from bs4 import BeautifulSoup
from datetime import datetime

def crawl_web():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    url = 'https://www.24h.com.vn/gia-vang-hom-nay-c425.html'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    bang_gia = soup.find('table', class_='gia-vang-search-data-table')
    PNJ_HCM = bang_gia.find_all('tr')[5]
    buy_price = PNJ_HCM.find_all('td')[1].find_all('span')[0].get_text()
    sell_price = PNJ_HCM.find_all('td')[2].find_all('span')[0].get_text()
    data = {
        'timestamp': timestamp,
        'location': 'PNJ HCM',
        'buy_price': buy_price,
        'sell_price': sell_price
    }

    return data
