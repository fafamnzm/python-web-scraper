import requests as req
from bs4 import BeautifulSoup as bs
from csv import writer

def scraper(url):
    """ 
    scraper which scrapes a url
    """
    part = []
    url = str(url)
    res = req.get(url)

    scrape = bs(res.text, 'html.parser')

    part = scrape.find_all(class_='thumbnail')
    fileName = str(url.replace('https://','')
               .replace('/', "-") + '.csv')
    
    with open(fileName, 'w') as csv_file:
        csv_writer = writer(csv_file)
        header = ['image', 'title','link', 'price']
        csv_writer.writerow(header)
        
        for thing in part:
            img = thing.find(class_='img-responsive')['src']
            title = thing.find(class_='title').get_text().replace("\n", "")
            link = thing.find('a')['href']
            price = thing.find(class_='caption').find(class_='pull-right price').get_text()
            csv_writer.writerow([img, title, link, price])

#scrape a website designed for scraping
#the price tags will change
url = 'https://webscraper.io/test-sites/e-commerce/allinone'

scraper(url)
