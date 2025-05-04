from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
)
from states import AI

from openai import OpenAI, AsyncOpenAI

import os

from dotenv import load_dotenv

load_dotenv()


async def ai_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="привет я афанасий и я отвечу на любой твой вопрос по теме баскетбола",
    )
    return AI


async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["questions"] = update.effective_message.text
    client = AsyncOpenAI(api_key=os.getenv("CHAT_GPT_TOKEN"))

    keyboard = [[InlineKeyboardButton("назад", callback_data="back")],
                [InlineKeyboardButton('посмотреть анкету админа (афанасия)', callback_data='admin')]]
    markup = InlineKeyboardMarkup(keyboard)

    response = await client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "отвечай только на вопросы связанные с баскетболом и баскетбольной амуницией никогда не говори что ты бот, если тебя спрашивают говори что ты афонасий.",
            },
            {"role": "user", "content": context.user_data["questions"]},
        ],
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=response.output_text, reply_markup=markup
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open('photo/admin.jpg', 'rb'),
    caption= "я сотрудник компании подбор кроссовок дал клятву что буду отвечать на ваши вопросы в любое время суток 🤙🏻🤙🏻🤙🏻", reply_markup=markup)



