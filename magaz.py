from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ContextTypes,
)
from states import MAGAZ

async def magaz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton('👈🏿', callback_data='left'), InlineKeyboardButton('👉🏿', callback_data='right')]]
    markup = InlineKeyboardMarkup(keyboard)
    if query.data == 'magaz':
        context.user_data['n_page'] = 1
    elif query.data == 'left':
        context.user_data['n_page'] -= 1
    elif query.data == 'right':
        context.user_data['n_page'] += 1
        
    if context.user_data.get('n_page'):
        n_page = context.user_data.get('n_page')
    else:
        context.user_data['n_page'] = 1
        n_page = context.user_data.get('n_page')
    
    if context.user_data['n_page'] == 2:
        text = f'товар {n_page}'
        await query.edit_message_text(text=text, reply_markup=markup)

    return MAGAZ