import os
from aiogram import Bot
from database.db import DatabaseConfig

# Get configuration from environment variables
# BOT_TOKEN = os.environ.get('BOT_TOKEN', '8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU')
# DB_USER = os.environ.get('DB_USER', 'postgres')
# DB_PASSWORD = os.environ.get('DB_PASSWORD', '858006')
# DB_NAME = os.environ.get('DB_NAME', 'soft_bot')
# DB_HOST = os.environ.get('DB_HOST', 'localhost')
# DB_PORT = int(os.environ.get('DB_PORT', '5432'))

# Bot_Tokken = Bot(token=BOT_TOKEN)

# db = DatabaseConfig(
#     user=DB_USER,
#     password=DB_PASSWORD,
#     db_name=DB_NAME,
#     host=DB_HOST,
#     port=DB_PORT
# )


# Правильный способ указать прокси (если он ОБЯЗАТЕЛЬНО нужен):
# from aiogram.client.session.aiohttp import AiohttpSession
# session = AiohttpSession(proxy='http://proxy_url:port') 
# Bot_Tokken = Bot(token='ВАШ_ТОКЕН', session=session)

# Создаем бота БЕЗ прокси для начала (убедитесь, что соединение работает)
# Bot_Tokken = Bot(token='8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU')




# from aiogram import Bot
# from database.db import DatabaseConfig
# # from aiohttp

# proxy_url = "socks5://127.0.0.1:1080"  # например, если у тебя локальный Shadowsocks

Bot_Tokken = Bot('8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU', proxy = proxy_url)
# 8299427995:AAEWUFt-OmdEHOT0ZlPEoJi6mxutiiLmzCU
# Group_id = 
db = DatabaseConfig(
    user = 'hjjjjjjjj_user',
    password='opgBiUDpRLoFFIbeh5k82FIBB2Dhocjy',
    db_name = 'hjjjjjjjj',
    host = 'postgresql://hjjjjjjjj_user:opgBiUDpRLoFFIbeh5k82FIBB2Dhocjy@dpg-d2rfm6emcj7s73cklc1g-a/hjjjjjjjj',
    port = 5432
)