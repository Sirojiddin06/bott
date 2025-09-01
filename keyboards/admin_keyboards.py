from aiogram.types import (ReplyKeyboardMarkup,
                            KeyboardButton,
                            InlineKeyboardMarkup,
                            InlineKeyboardButton
                            )

admin_keyboards = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text = 'Add goods'),
               KeyboardButton(text = 'Get all goods')],
              [KeyboardButton(text = 'Update goods'),
               KeyboardButton(text='Delete goods')]], resize_keyboard= True
)

