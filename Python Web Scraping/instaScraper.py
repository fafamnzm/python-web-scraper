import requests as req
from bs4 import BeautifulSoup as bs
from csv import writer


def instaScraper(username):
    part = []
    url = 'https://www.instagram.com/' + str(username)
    res = req.get(url)
    
    if res.status_code == 200:
        fileName = str(username) + '.csv'
        with open(fileName, 'w') as csv_file:
            csv_writer = writer(csv_file)
            header = ['Account Owner Name', "Account's details"]
            csv_writer.writerow(header)
                
            scrape = bs(res.text, 'html.parser')

            secondTag = scrape.find('meta', attrs={'property':'og:title'}).attrs['content']
            accountOwnerName = secondTag.split("(")[0]

            tag = scrape.find('meta', attrs={'name':'description'}).attrs['content']
            details = tag.split("-")[0]
            csv_writer.writerow([accountOwnerName, details])
            
            print(
                accountOwnerName, ": ",
                details
                )
    else:
        print("404 status\ncheck the user name")    

username = 'fafa.mnzm'

instaScraper(username)