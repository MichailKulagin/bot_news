import requests
from bs4 import BeautifulSoup
import time
import pyautogui

url = "https://www.mk.ru/news/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

sulka = soup.find_all("a", {'class' : 'news-listing__item-link'})
title = soup.find_all("h3", {'class' : 'news-listing__item-title'})
time_list = soup.find_all("span", {'class' : 'news-listing__item-time'})


sulka_list = []

for link in sulka:
    sulka_list.append(link.get('href'))
    #print(link.get('href'))
    #print("Всего ссылок",len(sulka_list))


title_list = []
def news_vse():
    index = 0
    while index < len(title):
        title_list.append(title[index].text)
        
        try:
            print(time_list[index].text,title[index].text,":>", sulka_list[index] )
        except:
            print("Ничего не найдено")
        
        index = index + 1

def news_10():
    index = 0
    while index <= 9:
        title_list.append(title[index].text)
        
        try:
            print(time_list[index].text,title[index].text,":>", sulka_list[index] )
        except:
            print("Ничего не найдено")
        
        index = index + 1

while True:
    otvet = input("Введит 1-Все новости, 2-10 новостей: ")
    if otvet == "1":
        news_vse()
    elif otvet == "2":
        news_10()
    else:
        print("Неверный ввод")
    


    



