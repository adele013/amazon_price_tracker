import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = 'URL for amazon page you want to track'
EMAIL = 'your email'
APP_PASSWORD = 'Your Gmail App password'

response = requests.get(URL, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'gzip, deflate'})
html_page = response.text
soup = BeautifulSoup(html_page, 'lxml')
price = soup.find(name='span', class_='a-offscreen')
price_without_symbol = price.get_text().split('$')[1]
price_as_float = float(price_without_symbol)
print(price_as_float)

if price_as_float < 100:
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=EMAIL, password=APP_PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg='Subject: Amazon Price Drop!\n\nThe price for the item you'
                                                             'are looking at has gone below your set target price! Click '
                                                             'the link to check it out!\n'
                                                             f'{URL}')
    connection.close()