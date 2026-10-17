import os
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
import random

load_dotenv()

TOKEN = os.getenv('VK_TOKEN')
bot = Bot(token = TOKEN)


@bot.on.message()
async def smart_bot(message:Message):
    text = message.text.lower()

    if 'привет' in text:
        await message.answer('Привет! Рад тебя видеть')
    elif 'пока' in text or 'пока!' in text:
        await message.answer('До скорой встречи!')
    elif 'помощь' in text:
        await message.answer('Давай я тебе помогу, опиши свою проблему')
    else:
        await message.answer("Я тебя не понимаю")


@bot.on.message(text=['кубик', 'Кубик'])
async def square(message:Message):
    await message.answer(random.randint(1, 6))


@bot.on.message(text=['кубик 2', 'Кубик 2'])
async def square_2(message:Message):
    await message.answer(random.randint(1, 6) + random.randint(1, 6))


@bot.on.message(text=['Заказ', 'заказ'])
async def take_answer(message:Message):
    await message.answer("Ваш заказ готовится! \nЕсли вас инетресует когда ваш заказ приготовится напишите *время*")
    @bot.on.message(text=['Время', 'время'])
    async def time(message:Message):
        await message.answer(f"Время ожидания: {random.randint(5, 15)} минут")
        

bot.run()