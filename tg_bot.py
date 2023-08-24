from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import requests
from bs4 import BeautifulSoup

bot = Bot(token='6182876153:AAFggeI_rv6r35YpY6aMxwMFf7kfysb4BEc')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    start_buttons = ["Все новости", "10 последних новостей", "Последняя новость"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.reply("Лента новостей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
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
    
    index = 0
    while index < len(title):
        title_list.append(title[index].text)
        
        try:
            print(time_list[index].text,title[index].text,":>", sulka_list[index] )
            await message.reply(f"{time_list[index].text}\n"
                                f"{title[index].text}\n" 
                                f"{sulka_list[index]}")
        except:
            print("Ничего не найдено")
        
        index = index + 1
    

@dp.message_handler(Text(equals="10 последних новостей"))
async def get_10_news(message: types.Message):
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
    
    index = 0
    while index <= 9:
        title_list.append(title[index].text)
        
        try:
            print(time_list[index].text,title[index].text,":>", sulka_list[index] )
            await message.reply(f"{time_list[index].text}\n"
                                f"{title[index].text}\n" 
                                f"{sulka_list[index]}")
        except:
            print("Ничего не найдено")
        
        index = index + 1   

@dp.message_handler(Text(equals="Последняя новость"))
async def get_1_news(message: types.Message):
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
    
    index = 0
    while index <= 0:
        title_list.append(title[index].text)
        
        try:
            print(time_list[index].text,title[index].text,":>", sulka_list[index] )
            await message.reply(f"{time_list[index].text}\n"
                                f"{title[index].text}\n" 
                                f"{sulka_list[index]}")
        except:
            print("Ничего не найдено")
        
        index = index + 1   




if __name__ == '__main__':
    executor.start_polling(dp) 