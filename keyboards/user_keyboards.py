from aiogram.types import (ReplyKeyboardMarkup,
                            KeyboardButton,
                            InlineKeyboardMarkup,
                            InlineKeyboardButton
                            )

user_keyboards = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text = 'Add goods_user'),
               KeyboardButton(text = 'Get all goods_user')],
              [KeyboardButton(text = 'Update goods_user'),
               KeyboardButton(text='Delete goods_user')]], resize_keyboard= True
)

