from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ContextTypes,
)


from states import GET_MONEY, GET_ROST, GET_SHUES


async def position(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['1-2-3', '4-5']]
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="на какой позиции ты играешь?",
        reply_markup=markup,
    )
    return GET_MONEY


async def money(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['средний', 'высокий']]
    context.user_data["position"] = update.effective_message.text
    print(context.user_data["position"])
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="на какой бюджет ты расчитываешь?", reply_markup=markup
    )
    return GET_ROST


async def rost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["до 180см", "выше 180см"]]
    context.user_data['money'] = update.effective_message.text
    print(context.user_data['money'] )
    markup = ReplyKeyboardMarkup(keyboard)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="какой у тебя рост", reply_markup=markup
    )
    return GET_SHUES
