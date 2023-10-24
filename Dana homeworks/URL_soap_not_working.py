#NOT WORKING

# TO BE FINALIZED :) --- how to refer to the right code in the result = soup.find_all, how to know what to refer to, how to find it all the time

import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/uk"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find_all('div', class_='aria-label')

for result in results:
    print(result.text)


