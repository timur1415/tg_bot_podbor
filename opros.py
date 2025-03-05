from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)


from states import GET_MONEY, GET_ROST, GET_VES, GET_SHUES


async def position(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['1-2-3', '4-5']]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="я бот по подбору баскетбольных кроссовок выбери свою позицию",
        reply_markup=markup,
    )
    return GET_MONEY


async def money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['средний', 'высокий']]
    markup = ReplyKeyboardMarkup(keyboard)
    text_user = update.effective_message.text
    context.user_data["ves"] = text_user
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="выбери свой бюджет", reply_markup=markup
    )
    return GET_ROST


async def rost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["position"] = update.effective_message.text
    keyboard = [["до 180см", "выше 180см"]]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="какой у тебя рост", reply_markup=markup
    )
    return GET_VES


async def ves(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["rost"] = update.effective_message.text
    keyboard = [["до 100кг", "больше 100кг"]]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="какой у тебя вес", reply_markup=markup
    )
    return GET_SHUES
