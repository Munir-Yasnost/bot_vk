import os
from dotenv import load_dotenv
from vkbottle import Bot
from vkbottle.bot import Message
import random
from datetime import datetime

load_dotenv()

TOKEN = os.getenv('VK_TOKEN')
bot = Bot(token = TOKEN)


@bot.on.message()
async def smart_bot(message:Message):
    text = message.text.lower()
    # await message.answer(f'Твой ID: {message.from_id}. А длина твоего сообщения: {len(text)} символов ')

# ЭХО-БОТ
    if 'секрет' in text or 'пароль' in text:
        await message.answer( "Я никому не скажу! 🤫")
    else:
        await message.answer(text)

# СЧИТАЕТ КОЛ-ВО СЛОВ
    # text = text.split()
    # if len(text) <= 3:
    #     await message.answer(f'Краткость - сетра таланта!\nКол-во слов: {len(text)}')

    # elif len(text) > 10:
    #     await message.answer(f'Ого, целую книгу написал!\nКол-во слов: {len(text)}')

    # else:
    #     await message.answer(f'Вот, нормальное сообщение!\nКол-во слов: {len(text)}')

# ОБЫЧНОЕ ОБЩЕНИЕ 
    # if 'привет' in text:
    #     await message.answer('Привет! Рад тебя видеть')

    # elif 'пока' in text:
    #     await message.answer('До скорой встречи!')

    # elif 'который час' in text or 'время' in text:
    #     cur_time = datetime.now().strftime('%H:%M')
    #     await message.answer(f'сейчас {cur_time}')

    # else:
    #     await message.answer("Я тебя не понимаю")


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