from telegram import (
    Update,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ContextTypes,
)

from telegram.constants import ParseMode


async def shues(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton('выход', callback_data='exit')]]
    markup = InlineKeyboardMarkup(keyboard)

    context.user_data["rost"] = update.effective_message.text
    print(context.user_data["rost"])
    message = await context.bot.send_message(
        chat_id=update.effective_chat.id, text="f", reply_markup=ReplyKeyboardRemove()
    )
    await context.bot.delete_message(
        chat_id=update.effective_chat.id, message_id=message.id
    )
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
            photo=open("photo/imortallity.png", "rb"),
            caption="nike immortality 4\n\nкупить [тут](https://cdek.shopping/p/17833125/muzskie-basketbolnye-krossovki-nike-giannis-immortality-4-cvet-black-pink-punch)",
            parse_mode=ParseMode.MARKDOWN_V2,
        )
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/puma_all-pro.png", "rb"),
            caption="puma all pro nitro\n\nкупить [тут](https://cdek.shopping/p/10424519/muzskie-basketbolnye-krossovki-puma-all-pro-nitro-belyisinii)",
            parse_mode=ParseMode.MARKDOWN_V2, reply_markup=markup
        )
    elif (
        position == "1-2-3"
        and money == "высокий"
        and rost == "до 180см"
    ):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/nike_gt_cut.png", "rb"),
            caption="nike gt cut 2\n\nкупить [тут](https://cdek.shopping/p/4525949/nike-zoom-gt-cut-2-cernyi-yarko-malinovyi)",
            parse_mode=ParseMode.MARKDOWN_V2,
        )
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/anta_kai.png", "rb"),
            caption="anta kai 1\n\nкупить [тут](https://cdek.shopping/p/20994131/krossovki-anta-kai-1-11-games-sinii)",
            parse_mode=ParseMode.MARKDOWN_V2,
        )
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/nike_kd_17.png", "rb"),
            caption="nike kd 17\n\nкупить [тут](https://cdek.shopping/p/11024758/krossovki-nike-kd-17-ep-zeltyi)",
            parse_mode=ParseMode.MARKDOWN_V2, reply_markup=markup
        )
    elif (
        position == "4-5"
        and money == "средний"
        and rost == "до 180см"
        or rost == "выше 180см"
    ):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/nike_gt_hustle.png", "rb"),
            caption="nike air zoom gt hustle 2\n\nкупить [тут](https://cdek.shopping/p/11025377/krossovki-nike-air-zoom-gt-hustle-2-ep-belyi)",
            parse_mode=ParseMode.MARKDOWN_V2,
        )
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/jordan_luka.png", "rb"),
            caption="jordan luka 2\n\nкупить [тут](https://cdek.shopping/p/10422910/jordan-luka-2-basketbolnye-krossovki-muzskie-zelenyi)",
            parse_mode=ParseMode.MARKDOWN_V2,reply_markup=markup
        )
    elif (
        position == "4-5"
        and money == "высокий"
        and rost == "до 180см"
    ):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/nike_lebron.png", "rb"),
            caption="nike lebron 21  купить [тут](https://cdek.shopping/p/11024327/krossovki-nike-lebron-21-gs-raznocvetnyi)",
            parse_mode=ParseMode.MARKDOWN_V2,
        )
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("photo/nike_gt_jump.png", "rb"),
            caption="nike gt jump 1\n\nкупить [тут](https://cdek.shopping/p/11035142/krossovki-nike-air-zoom-gt-jump-raznocvetnyi)",
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=markup
        )
