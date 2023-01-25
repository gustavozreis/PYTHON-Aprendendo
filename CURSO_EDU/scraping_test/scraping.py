from bs4 import BeautifulSoup
import requests
import re

def get_document_html(url):
    response = requests.get(url)
    return response.text

url_to_scrape = 'http://www.pudim.com.br'

html_document = get_document_html(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

soup_test = soup.title.decode_contents()

soup.find('class="email"')

# print(soup.prettify())
print(soup.find(id="email"))