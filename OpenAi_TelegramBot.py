# import os
# import openai
# from aiogram import Bot, Dispatcher, executor, types
# from dotenv import load_dotenv

# load_dotenv()

# bot = Bot(token= os.getenv('TELEGRAM_TOKEN'))
# dp = Dispatcher(bot)

# openai.api_key = os.getenv('OPENAI_API')

# @dp.message_handler(commands=['start', 'help'])
# async def welcome(message: types.Message):
#     keyboard_markup = types.InlineKeyboardMarkup()
#     keyboard_markup.add(
#         types.InlineKeyboardButton("Haz una pregunta", callback_data="ask_question"),
#         types.InlineKeyboardButton("Grupo de soporte", url='https://t.me/+WjvHAogG5aZiNzIx')
#     )
#     await message.reply("¡Hola Bienvenid@!, soy QuantCoBot. ¿Qué te gustaría hacer?", reply_markup=keyboard_markup)

# @dp.callback_query_handler(lambda c: c.data == 'ask_question')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Por favor, realiza tu pregunta.')

# @dp.message_handler()
# async def gpt(message: types.Message):
#     keyboard_markup = types.InlineKeyboardMarkup()
#     keyboard_markup.add(
#         types.InlineKeyboardButton("Grupo de soporte", url='https://t.me/+WjvHAogG5aZiNzIx')
#     )
#     try:
#         response = openai.Completion.create(
#             model = 'text-davinci-003',
#             prompt = message.text,
#             temperature = 0.5,
#             max_tokens = 500,   
#             top_p = 1,
#         )
#         await message.reply(response.choices[0].text.strip(), reply_markup=keyboard_markup)
        
#     except openai.error.RateLimitError:
#         await message.reply("Lo siento, estoy sobrecargado en este momento. Por favor, inténtalo de nuevo más tarde o comunícate con nuestro grupo de soporte", reply_markup=keyboard_markup)
        
# if __name__ == '__main__':
#     executor.start_polling(dp)
import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import time

load_dotenv()

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)

openai.api_key = os.getenv('OPENAI_API')

# Definir la variable global last_request_time
last_request_time = 0
request_interval = 5  # Intervalo mínimo entre las solicitudes en segundos

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(
        types.InlineKeyboardButton("Haz una pregunta", callback_data="ask_question"),
        types.InlineKeyboardButton("Grupo de soporte", url='https://t.me/+WjvHAogG5aZiNzIx')
    )
    await message.reply("¡Hola Bienvenid@!, soy QuantCoBot. ¿Qué te gustaría hacer?", reply_markup=keyboard_markup)

@dp.callback_query_handler(lambda c: c.data == 'ask_question')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Por favor, realiza tu pregunta.')

@dp.message_handler()
async def gpt(message: types.Message):
    global last_request_time  # Declarar last_request_time como global

    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(
        types.InlineKeyboardButton("Grupo de soporte", url='https://t.me/+WjvHAogG5aZiNzIx')
    )
    try:
        current_time = time.time()
        time_since_last_request = current_time - last_request_time

        if time_since_last_request < request_interval:
            time_to_wait = request_interval - time_since_last_request
            time.sleep(time_to_wait)

        last_request_time = time.time()

        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=message.text,
            temperature=0.5,
            max_tokens=500,
            top_p=1
        )

        generated_text = response.choices[0].text.strip()

        # Verificar si el texto generado está relacionado con trading, brokers, inversiones o economía.
        if ('trading' in generated_text or 'brokers' in generated_text or 'inversiones' in generated_text or 'economía' in generated_text):
            await message.reply(generated_text, reply_markup=keyboard_markup)
        else:
            await message.reply("Lo siento, no tengo información sobre ese tema. ¿Hay algo más en lo que pueda ayudarte?", reply_markup=keyboard_markup)
    except openai.error.RateLimitError:
        await message.reply("Lo siento, estoy sobrecargado en este momento. Por favor, inténtalo de nuevo más tarde o comunícate con nuestro grupo de soporte", reply_markup=keyboard_markup)

if __name__ == '__main__':
    executor.start_polling(dp)
