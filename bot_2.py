import os
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message

load_dotenv()

TOKEN = os.getenv('VK_TOKEN')
bot = Bot(token = TOKEN)
@bot.on.message(text='Привет')
async def greetings(message:Message):
    await message.answer('Привет! Все работает правильно')

@bot.on.message(text='Пока')
#TODO

bot.run()