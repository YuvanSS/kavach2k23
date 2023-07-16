from bs4 import BeautifulSoup
import urllib.request
import re

parser = 'html.parser'
link = input()
response = urllib.request.urlopen(link)
result = BeautifulSoup(response, parser, from_encoding=response.info().get_param('charset'))

for link in result.find_all('a', href=True):
    onion_link = "\w+\.onion"
    linklist = re.findall(onion_link,link['href'])
    print(final_link)
    #print(linklist)
