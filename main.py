import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackQueryHandler,
    PicklePersistence,
)


from states import (
    GET_POZITION,
    GET_MONEY,
    GET_ROST,
    GET_SHUES,
    MAIN_MENU,
    MAGAZ,
    AI,
)

from opros import position, rost, money

from shues import shues

from start import start

from magaz import magaz

from ai import ai_start, ai, admin

import os

from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    persistence = PicklePersistence(filepath="podbor_bot") 
    application = ApplicationBuilder().token(os.getenv("TOKEN")).persistence(persistence).build()   

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [
                CallbackQueryHandler(position, pattern="^podbor$"),
                CallbackQueryHandler(magaz, pattern="^magaz$"),
                CallbackQueryHandler(ai_start, pattern="^ai$"),
            ],
            MAGAZ: [
                CallbackQueryHandler(start, pattern="^exit$"),
                CallbackQueryHandler(magaz)
            ],
            AI: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, ai),
                CallbackQueryHandler(start, pattern="^back$"),
                CallbackQueryHandler(admin, pattern='^admin$')
            ],
            
            GET_POZITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, position)],
            GET_MONEY: [MessageHandler(filters.TEXT & ~filters.COMMAND, money)],
            GET_ROST: [MessageHandler(filters.TEXT & ~filters.COMMAND, rost)],
            GET_SHUES: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, shues),
                CallbackQueryHandler(start, pattern="exit"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
        name="podbor_bot",
        persistent=True,
    )

    application.add_handler(conv_handler)
    application.run_polling()
