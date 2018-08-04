import bs4
import requests
from bs4 import BeautifulSoup as soup
import sqlite3
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

my_url = ['https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/', 
'https://magicseaweed.com/2nd-Beach-Sachuest-Beach-Surf-Report/846/']
# opening up connecting, grabbing the page

for url in my_url:

	uClient = uReq(url)
# this will offload our content in'to a variable
	page_html = uClient.read()
# closes our client
	uClient.close()

# html parsing
	page_soup = soup(page_html, "html.parser")

	datex = page_soup.findAll('div', class_=re.compile("table-responsive-xs"))

	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS Tracks(WaveSize TEXT, Beach TEXT, WebSource TEXT)')


	for date in datex:
		datetime = date.find('a', class_='row-title background-gray-lighter')

	print(datetime)




