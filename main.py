import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackQueryHandler,
)


from states import GET_POZITION, GET_MONEY, GET_ROST, GET_SHUES, MAIN_MENU, MAGAZ

from opros import position, rost, money

from shues import shues

from start import start

from magaz import magaz

import os

from dotenv import load_dotenv
load_dotenv()



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token(os.getenv("TOKEN"))
        .build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CallbackQueryHandler(position, pattern="^podbor$"),
                CallbackQueryHandler(magaz, pattern="^magaz$"),
            ],
            MAGAZ: [CallbackQueryHandler(magaz)],
            GET_POZITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, position)],
            GET_MONEY: [MessageHandler(filters.TEXT & ~filters.COMMAND, money)],
            GET_ROST: [MessageHandler(filters.TEXT & ~filters.COMMAND, rost)],
            GET_SHUES: [MessageHandler(filters.TEXT & ~filters.COMMAND, shues)],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.run_polling()