from telebot import TeleBot
from config import TELEGRAM_BOT_TOKEN
from config import WEATHER_API_KEY
from weather_data import WeatherData

bot = TeleBot(token=TELEGRAM_BOT_TOKEN)
weather_data = WeatherData(api_key=WEATHER_API_KEY)


@bot.message_handler(func=lambda city: city.text != '/start'
                                       and city.text != '/help')
def get_temperature(city):
    bot.send_message(chat_id=city.chat.id, text=weather_data.get_temperature_in_celsius(city.text))


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Hello, i can talk you temperature in your city,\n'
                          'for that you should to post me your city name')


bot.polling()
