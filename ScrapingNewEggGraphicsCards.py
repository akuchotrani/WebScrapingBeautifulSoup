import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
#opening the connection and grabbing the webpage
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parse the page as html 
page_soup = soup(page_html,"html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class": "item-container"})