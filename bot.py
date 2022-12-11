import telebot
from telebot import types

token = '5981615351:AAGtUjZ_uj-dxhZx5GYZ10g5OiXjw51hdvo'

MypyBot = telebot.TeleBot(token, parse_mode = None)

@MypyBot.message_handler(commands=['start'])
def start_message(message):
    MypyBot.send_message(message.chat.id,"Привет, ты попал на тест Карьерного сервиса StudentRT")
    MypyBot.send_message(message.chat.id,"Напиши сферу, в которой хочешь найти работу, а я тебе помогу найти подходящие вакансии")
    MypyBot.send_message(message.chat.id,"Сферы: фотограф, стажёр 1С, повар")

# @MypyBot.message_handler(commands=['button'])
# def button_message(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1=types.KeyboardButton("Программирование")
#     item2=types.KeyboardButton("Менеджмент")
#     item3=types.KeyboardButton("Курьер")
#     markup.add(item1, item2, item3) 
#     Mypybot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@MypyBot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="фотограф":
        MypyBot.send_message(message.chat.id,"https://vk.com/doc154140164_651909376?hash=qxzaw4hJvkBeM5HlKkOikjZBeV56Ert8obEjvq2pzbc&dl=PfsFnrZUcN7dIiLfoA6wORdWEoWgyX3sRdzCV7rFgDc")
    if message.text=="стажёр 1С":
        MypyBot.send_message(message.chat.id,"https://vk.com/doc154140164_651909431?hash=On6ztMBL4S3MZxn1xKYzdZ8Rq5clO28HR5KOUc05xMs&dl=QIZwlih4CIPBuhjBT85sv1SPuw0VqkZlPymEICgoRzz")
    if message.text=="повар":
        MypyBot.send_message(message.chat.id,"https://vk.com/doc154140164_651909432?hash=ZPKju6SFbhZ6nKLtgxKRHP7wUj2EwNFQoCAJFhzgzxk&dl=EqZoA0mUiOQZmn0zy32zPKlLueeyfZYglFrnfmqlnyT")

MypyBot.polling()