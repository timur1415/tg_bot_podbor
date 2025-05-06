from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
)
from states import MAIN_MENU

from dotenv import load_dotenv

load_dotenv()




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
    keyboard = [
        [InlineKeyboardButton("🛒 В магазин 🛒", callback_data="magaz")],
        [InlineKeyboardButton("👟 Найти свою пару 👟", callback_data="podbor")],
        [InlineKeyboardButton('🔥 KicksWizard Baller Support 🔥', callback_data="ai")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="🔹 Магазин – свежие Nike, Jordan, Adidas и другие.\n\n🔹 Подбор кроссовок – найдём идеальную пару под твои запросы.\n\n🔹 Афанасий – ответит на любые вопросы о кроссах, баскетболе и не только🚀",
        reply_markup=markup,
    )


    return MAIN_MENU
