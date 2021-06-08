import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.espn.com/nba/draft/bestavailable/_/position/ovr/page/4").text

soup = BeautifulSoup(url, 'html.parser')

table = soup.find_all(class_='draftTable__playerInfo')

info_class = soup.find_all(class_='draftTable__playerInfo')

for info_class in table:
    name_class = info_class.find_all(class_='draftTable__headline draftTable__headline--player')
    for name in name_class:
        print(name.text)
