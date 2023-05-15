import requests
from bs4 import BeautifulSoup

# URL of the webpage to be scraped
url = 'https://news.daum.net/digital#1'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links in the HTML content
links = soup.find_all('a', {'class': 'link_txt'})

# Loop through all the links and print the title of each link
for link in links:
    print(link.text.strip())
