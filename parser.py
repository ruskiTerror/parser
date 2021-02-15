import requests
from bs4 import BeautifulSoup
url = "https://www.motorcyclespecs.co.za/bikes/bmw.htm"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find('table', id='table26')
tds = table.find_all('td', class_='auto-style12')
for a in tds:
    all_a = a.find('a', class_='auto-style4')
    if all_a:
        print (all_a.text.strip())
url = "https://www.motorcyclespecs.co.za/bikes/bmw2.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find('table', id='table41')
tds = table.find_all('td', class_='auto-style12')
for a in tds:
    all_a = a.find('a', class_='auto-style4')
    if all_a:
        print (all_a.text.strip())
url = "https://www.motorcyclespecs.co.za/bikes/bmw2.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
linkpage = soup.find_all('span', class_='auto-style10')
for i in linkpage:
    if i.find('a'):
       scraped_url =(i.find("a").get('href'))
baseurl = 'https://www.motorcyclespecs.co.za/bikes/'
for scrap_url in scraped_url:
    needed = baseurl + scrap_url
    response = requests.get(needed)
url = response
soup = BeautifulSoup(response.text, "lxml")
table = soup.find('table', id='table36')
tds = table.find_all('td', class_='auto-style14')
for a in tds:
    print(all_a.text.strip())