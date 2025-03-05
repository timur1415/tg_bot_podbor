from telegram import (
    Update,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    ContextTypes,
)

from telegram.constants import ParseMode


async def shues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id, text="f", reply_markup=ReplyKeyboardRemove()
    )
    await context.bot.delete_message(
        chat_id=update.effective_chat.id, message_id=message.id
    )
    text_user = update.effective_message.text
    context.user_data["money"] = text_user
    money = context.user_data["money"]
    position = context.user_data["position"]
    ves = context.user_data["ves"]
    rost = context.user_data["rost"]
    print(money, rost, ves, position)
    if (
        position == "1-2-3"
        and money == "средний"
        and ves == "до 100кг"
        and rost == "до 180см"
        or rost == "больше 180см"
    ):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("imortallity.png", "rb"),
            caption="nike immortality 4 купить [тут](https://cdek.shopping/p/17833125/muzskie-basketbolnye-krossovki-nike-giannis-immortality-4-cvet-black-pink-punch)",
        parse_mode=ParseMode.MARKDOWN_V2,
        )
