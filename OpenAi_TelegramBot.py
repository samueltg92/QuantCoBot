import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token= os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)

openai.api_key = os.getenv('OPENAI_API')

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
    keyboard_markup = types.InlineKeyboardMarkup()
    keyboard_markup.add(
        types.InlineKeyboardButton("Grupo de soporte", url='https://t.me/+WjvHAogG5aZiNzIx')
    )
    try:
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = message.text,
            temperature = 0.5,
            max_tokens = 500,   
            top_p = 1,
        )
        await message.reply(response.choices[0].text.strip(), reply_markup=keyboard_markup)
        
    except openai.error.RateLimitError:
        await message.reply("Lo siento, estoy sobrecargado en este momento. Por favor, inténtalo de nuevo más tarde o comunícate con nuestro grupo de soporte", reply_markup=keyboard_markup)
        
if __name__ == '__main__':
    executor.start_polling(dp)
