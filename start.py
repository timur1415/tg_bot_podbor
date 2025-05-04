from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
)
from states import MAIN_MENU

import os

from dotenv import load_dotenv

load_dotenv()




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
    keyboard = [
        [InlineKeyboardButton("магазин", callback_data="magaz")],
        [InlineKeyboardButton("подбор", callback_data="podbor")],
        [InlineKeyboardButton('ответы на вопросы про баскет', callback_data="ai")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="выбери что хочешь делать",
        reply_markup=markup,
    )


    return MAIN_MENU
