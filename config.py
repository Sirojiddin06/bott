from aiogram import Bot
from database.db import DatabaseConfig

# Правильный способ указать прокси (если он ОБЯЗАТЕЛЬНО нужен):
# from aiogram.client.session.aiohttp import AiohttpSession
# session = AiohttpSession(proxy='http://proxy_url:port') 
# Bot_Tokken = Bot(token='ВАШ_ТОКЕН', session=session)

# Создаем бота БЕЗ прокси для начала (убедитесь, что соединение работает)
Bot_Tokken = Bot(token='8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU')

db = DatabaseConfig(
    user='postgres',
    password='858006',
    db_name='soft_bot',
    host='localhost',
    port=5432
)









# from aiogram import Bot
# from database.db import DatabaseConfig
# # from aiohttp

# proxy_url = "socks5://127.0.0.1:1080"  # например, если у тебя локальный Shadowsocks

# Bot_Tokken = Bot('8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU', proxy = proxy_url)
# # 8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU
# # Group_id = 
# db = DatabaseConfig(
#     user = 'postgres',
#     password='858006',
#     db_name = 'soft_bot',
#     host = 'localhost',
#     port = 5432
# )