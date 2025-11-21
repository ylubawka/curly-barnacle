import telebot
import os 
from random import choice
from settings import TG_API_TOKEN

bot = telebot.TeleBot(TG_API_TOKEN)

@bot.message_handler(commands=["start"])
def start_commands(message):
    text = (
        f"привет {message.from_user.first_name}!/n"
        "напиши /mem и я отправлю мем если хочешь мем с животными напиши /pet"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands= ["mem"])
def start_commands(message):
    random_mem = choice(os.listdir("images"))
    with open(f'images/{random_mem}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands= ["pet"])
def start_commands(message):
    random_mem2 = choice(os.listdir("imagespet"))
    with open(f'imagespet/{random_mem2}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

bot.infinity_polling()
