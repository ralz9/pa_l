import requests
import csv
from bs4 import BeautifulSoup as BS
URL = 'https://svetofor.info/sotovye-telefony-i-aksessuary/vse-smartfony/smartfony-s-podderzhkoy-4g-ru/'

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html , 'lxml')
    return soup

def get_data(soup):
    phones = soup.find_all('div' , class_ = 'ty-column4')    
    
    list_data = []
    for phon in phones:
        title = phon.find('a' , class_ = 'product-title').text.strip()
        image = phon.find('img' , class_ = 'ty-pict').get('data-ssrc')
        price = phon.find('span' , class_ = 'ty-price-update').text.strip()
        
        list_data.append({
            'title':title,
            'price': price,
            'image': image
        })
    return list_data

def write_csv(data):
    with open('phones.csv' , 'a')as file:
        names = ['title' , 'price' , 'image']
        write = csv.DictWriter(file, delimiter=',' , fieldnames=names)
        write.writerows(data)

def main():
    html = get_html(URL)
    soup = get_soup(html)
    data = get_data(soup)
    write_csv(data)
    # print(data)
if __name__ == '__main_':
    main()
#


