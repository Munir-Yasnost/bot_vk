import os
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
import random

load_dotenv()

TOKEN = os.getenv('VK_TOKEN')
bot = Bot(token = TOKEN)


greetings = ['привет', 'Привет', 'Привет!']
@bot.on.message(text=greetings)
async def greeting(message:Message):
    await message.answer('Привет! Рад тебя видеть')

goodbyes = ['пока', 'Пока', 'Пока!']
@bot.on.message(text=goodbyes)
async def goodbye(message:Message):
    await message.answer('До скорой встречи!')

kub = ['кубик', 'Кубик']
@bot.on.message(text=kub)
async def square(message:Message):
    await message.answer(random.randint(1, 6))

kub_2 = ['кубик 2', 'Кубик 2']
@bot.on.message(text=kub_2)
async def square_2(message:Message):
    await message.answer(random.randint(1, 6) + random.randint(1, 6))


bot.run()