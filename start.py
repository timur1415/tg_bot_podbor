from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ContextTypes,
)
from states import MAIN_MENU
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton('магазин', callback_data= 'magaz')], [InlineKeyboardButton('подбор',callback_data='podbor')]]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='выбери что хочешь делать', reply_markup=markup
    )
    
    client = OpenAI(api_key=os.getenv('CHAT_GPT_TOKEN'))

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "Talk like a pirate."
            },
            {
                "role": "user",
                "content": "Что делать в баскетболе, если я лось"
            }
        ]
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response.output_text)


    return MAIN_MENU