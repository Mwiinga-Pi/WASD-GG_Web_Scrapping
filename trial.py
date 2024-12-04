import requests
from bs4 import BeautifulSoup
import selenium

r = requests.get('https://fiftytwofour.org/sponsor?page=6')
print(r.content)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify()) # Prints all html from a page
s = soup.find_all('div', class_='runnner-campaign-card')
content = s
# print(s)