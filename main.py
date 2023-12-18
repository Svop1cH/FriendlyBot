import telebot
import random
form tokbot import a
bot = telebot.TeleBot(a)

@bot.message_handler(commands=['start', 'help'])
def send_privet(message):
    bot.reply_to(message, "Привет! Я дружелюбный бот!")
    
@bot.message_handler(func=lambda message: message.text.lower() == 'как дела?')
def answer_how_are_you(message):
    answers = ["Я нормально, спасибо!", "Не плохо!", "Я отлично!"]
    bot.reply_to(message, random.choice(answers))
    
@bot.message_handler(func=lambda message: True)
def answer_other_messages(message):
    bot.reply_to(message, "Я тут!")
    
bot.polling()

#pip install pyTelegramBotAPI
