import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)


from states import GET_POZITION, GET_MONEY, GET_ROST, GET_VES, GET_SHUES

from opros import position, rost, ves, money

from shues import shues

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("7555800128:AAFEvynoqe_lP6zMlGTlLCuwu10nErf5cTo")
        .build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", position)],
        states={
            GET_POZITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, position)],
            GET_MONEY: [MessageHandler(filters.TEXT & ~filters.COMMAND, money)],
            GET_ROST: [MessageHandler(filters.TEXT & ~filters.COMMAND, rost)],
            GET_VES: [MessageHandler(filters.TEXT & ~filters.COMMAND, ves)],
            GET_SHUES: [MessageHandler(filters.TEXT & ~filters.COMMAND, shues)],
        },
        fallbacks=[CommandHandler("start", position)],
    )

    application.add_handler(conv_handler)
    application.run_polling()
