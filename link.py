import re
import requests
from bs4 import BeautifulSoup

url = input() 
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the <a> tags
tags = soup.find_all('a')
h3_tags = [h3.get_text() for h3 in soup.find_all('h3')]
print("\nh3 Tags:")
print(h3_tags)
# Extract the tag names and links
for tag in tags:
    #tag_name = tag.text.strip()  # Extract the tag name and remove leading/trailing whitespaces
    tag_link = tag['href']  # Extract the tag link

    # Check if the link is an onion link
    if re.search(r'\.onion\b', tag_link):
        #print("Tag Name:", tag_name)
        print("Onion Link:", tag_link)
        print("-----------------------------------")

