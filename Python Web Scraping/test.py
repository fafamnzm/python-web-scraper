from bs4 import BeautifulSoup as bs


#res = './test.html'

with open('./test.html', 'r') as f:
    res = f.read()

scrape = bs(res, 'html.parser')
part = []

#print(everything)
#part = scrape.body
#part = scrape.head
#part = scrape.head.title

#print with find()
#part = scrape.find('div')

#find with fins_all() or findAll()
#part = scrape.findAll('div')

#find with id
#part = scrape.findAll(id='sec-1')

#find with class
#part = scrape.findAll(class_='stuff')

#find with attribute
#part = scrape.find(attrs={"header-hello":"howdyPartner"})
#or
#part = scrape.find_all(attrs={"header-hello":"howdyPartner"})

#find using select with id
#part = scrape.select('#sec-1')

#find using select with class name
#part = scrape.select('.thing')

#using get_text()
#part = scrape.select(".thing")[0].get_text()

#nor let's get all
""" for thing in scrape.select('.thing'):
    part += thing
    #print(thing) """

#navigating to the desired destination:
#part = scrape.body.contents[1].contents[1].next_sibling.next_sibling
#part = scrape.body.contents[1].contents[1].find_next_sibling() 
#part = scrape.find(class_='thing').find_parent()
#part = scrape.find('h2').find_next_siblings('p') #this one gives a list of all
part = scrape.find('h2').find_next_sibling('p').get_text()



print(part)
