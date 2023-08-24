import requests
from bs4 import BeautifulSoup
import time
import pyautogui

url = "https://www.mk.ru/news/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")


while True:


    sulka = soup.find_all("a", {'class' : 'news-listing__item-link'})
    title = soup.find_all("h3", {'class' : 'news-listing__item-title'})
    time_list = soup.find_all("span", {'class' : 'news-listing__item-time'})


    sulka_list = []

    for link in sulka:
        sulka_list.append(link.get('href'))
        #print(link.get('href'))
        #print("Всего ссылок",len(sulka_list))


    title_list = []
    index = 0
    while index < len(title):
        title_list.append(title[index].text)
        """
        try:
            print(time_list[index].text,title[index].text,":>", sulka_list[index] )
        except:
            print("Ничего не найдено")
        """
        index = index + 1

    with open("news_time.txt", "r") as file:
        txt_time = file.read()
        if txt_time != time_list[0].text:
            with open("news_time.txt", "w") as file:
                file.write(time_list[0].text)
                print("Вписано время в файл", time_list[0].text)
            print(time_list[0].text,title[0].text,":>", sulka_list[0])
        else:
            print("Время не изменилось")

    pyautogui.moveTo(1104, 452)
    time.sleep(0.5)
    pyautogui.moveTo(1059, 484)

    time.sleep(60)
    



