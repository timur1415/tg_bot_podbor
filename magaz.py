from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import (
    ContextTypes,
)
from states import MAGAZ

from tovari import GOODS_INFO


async def magaz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("👈🏿", callback_data="left"),
            InlineKeyboardButton("👉🏿", callback_data="right"),
        ],
        [InlineKeyboardButton('выход', callback_data="exit")]
    ]

    if query.data == "magaz":
        context.user_data["n_page"] = 1
    elif query.data == "left":
        context.user_data["n_page"] -= 1
    elif query.data == "right":
        context.user_data["n_page"] += 1

    if context.user_data.get("n_page"):
        n_page = context.user_data.get("n_page")
    else:
        context.user_data["n_page"] = 1
        n_page = context.user_data.get("n_page")
    
    if n_page > 9:
        n_page = 9

    with open(GOODS_INFO[n_page]["photo"], "rb") as photo:

        await query.edit_message_media(media=InputMediaPhoto(media=photo))

        await query.edit_message_caption(
        caption=f"{GOODS_INFO[n_page]['name']} - хорошие кроссовки, которые подходят игрокам играющим на позиции {GOODS_INFO[n_page]['position']} номера. {GOODS_INFO[n_page]['name']} подойдут тем кто расчитывает на {GOODS_INFO[n_page]['money']} бюджет.\n\n что бы купить обратись по ссылке 👇🏿 \n\n {GOODS_INFO[n_page]['url']}",
        reply_markup= InlineKeyboardMarkup(keyboard))

    return MAGAZ
