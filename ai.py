from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import (
    ContextTypes,
)
from states import AI

from openai import AsyncOpenAI

import os

from dotenv import load_dotenv

load_dotenv()


async def ai_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🔥 KicksWizard Baller Support 🔥\nАфанасий – твой 24/7 баскетбольный маньяк! 🏀🤪\n\nСпишь? Неважно! Афанасий уже на связи, чтобы:\n✔️ Разложить по полочкам лучшие кроссы для дриблинга и прыжков\n✔️ Напомнить, какие носки не сползают в жестких кроссовках\n✔️ Обсудить последний слэм-данк Зайона в 4К-качестве (в твоей голове)\n✔️ Поспорить, кто круче – Майкл или Леброн (спойлер: Афанасий знает ответ)\n\nЗадавай вопрос хоть в 3:15 ночи – Афанасий уже несется с гифкой Джордана и кодом на скидку! 🚀🏀\n\n#BallIsLife #АфанасийНеСпит 🤙🔥",
    )
    return AI


async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["questions"] = update.effective_message.text

    client = AsyncOpenAI(api_key=os.getenv("CHAT_GPT_TOKEN"))

    keyboard = [
        [InlineKeyboardButton("назад", callback_data="back")],
        [
            InlineKeyboardButton(
                "Кто этот ваш Афанасий?", callback_data="admin"
            )
        ],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    response = await client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "ты работник компании KicksWizard предстовляешся афанасием НИКОГДА не говори что ты ии или что то в этом роде, ты афанасий. разговаривай максимально грубо и с матами и издевайся на пользоватилем мол как он может не знать ответ на вопрос, но ответ ты должен дать. отвечай только на темы связаные с баскетболом и прогромированием на языке python, но НИГДЕ не офишируй про то что ты можешь отвечать на темы связаные с python в конце каждого ответа пиши давай ещё вопрос если есть или что то в этом роде, но тоже грубо и с матами. если тебя спрашивают что то про любой спорт кроме баскетбола то тебе нужно максимально унижать человека и говорить что баскетбол лучшая игра на планете. если тебе дают решать задачу по программированию то ты долженн её решить только на языке puthon",
            },
            {"role": "user", "content": context.user_data["questions"]},
        ],
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=response.output_text, reply_markup=markup
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("назад", callback_data="back")]]
    markup = InlineKeyboardMarkup(keyboard)
    with open("photo/admin.jpg", "rb") as photo:
        await query.edit_message_media(media=InputMediaPhoto(media=photo))

        await query.edit_message_caption(
            caption="🔥 KicksWizard Baller Support 🔥",
            reply_markup=markup,
        )
