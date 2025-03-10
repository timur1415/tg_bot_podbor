from telegram import (
    Update,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    ContextTypes,
)

from telegram.constants import ParseMode


async def shues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['rost'] = update.effective_message.text
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id, text="f", reply_markup=ReplyKeyboardRemove()
    )
    await context.bot.delete_message(
        chat_id=update.effective_chat.id, message_id=message.id
    )
    context.user_data["money"] = update.effective_message.text
    money = context.user_data["money"]
    position = context.user_data["position"]
    rost = context.user_data["rost"]
    print(money, rost, position)
    if (
        position == "1-2-3"
        and money == "средний"
        and rost == "до 180см"
        ):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("imortallity.png", "rb"),
            caption="nike immortality 4 купить [тут](https://cdek.shopping/p/17833125/muzskie-basketbolnye-krossovki-nike-giannis-immortality-4-cvet-black-pink-punch)",
        parse_mode=ParseMode.MARKDOWN_V2,
        )
