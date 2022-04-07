import os
import telebot


bot = telebot.TeleBot("5125894111:AAHi4fyy79K1SYU8DMzH6vMBHoI8F9AOn_c")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "HI i'am avishka's assistant bot ")


@bot.message_handler(commands=["cmd"])
def send_message(message):
  bot.send_message(message.chat.id, "cmd can get command list")



bot.polling()