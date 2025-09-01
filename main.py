import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncpg
from keyboards.admin_keyboards import admin_keyboards
from keyboards.user_keyboards import user_keyboards

# Импортируем класс User
from database.users import User

from config import db
from config import Bot_Tokken

dp = Dispatcher()

# dp.include_router(admin_router)

@dp.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    if msg.from_user.last_name:
        fullname = msg.from_user.first_name + ' ' + msg.from_user.last_name
    else:
        fullname = msg.from_user.first_name

    user = User(msg.from_user.id, msg.from_user.username, fullname, db)
    if not await user.get_user():
        await user.save()
    # Исправлена синтаксическая ошибка (print await -> await)
    status = await user.check_status()
    print(status)
    keyboard = admin_keyboards if status else user_keyboards

    await msg.answer('Bot start working!', reply_markup=keyboard)


@dp.message(Command('select'))
async def cmd_select(msg: types.Message) -> None:
    async with db.pool.acquire() as conn:
        result = await conn.fetch('select * from orders')
    await msg.answer(text="Data from databese: \n{}".format(result))

@dp.message(Command('insert'))
async def cmd_insert(msg: types.Message) -> None:
    try:
        splitted_msg = msg.text.split(' ')
        product = splitted_msg[1]
        price = float(splitted_msg[2])
        quantity = int(splitted_msg[3])
    except (ValueError, IndexError):
        await msg.answer('Invalid Input. Please use /insert <product> <price> <quantity>')
        return # Добавлен return для выхода из функции при ошибке

    async with db.pool.acquire() as conn:
        # Исправлены кавычки с """ на '''
        await conn.execute('''
                insert into orders (product, price, quantity)
                values($1,$2,$3)        
''', product, price, quantity)
    await msg.answer(text="Data inserted successfully!")

@dp.message(Command('edit'))
async def cmd_edit(msg: types.Message) -> None:
    try:
        splitted_msg = msg.text.split(' ')
        order_id = int(splitted_msg[1])
        new_product = splitted_msg[2]
        new_price = float(splitted_msg[3])
        new_quantity = int(splitted_msg[4])
    except (ValueError, IndexError):
        await msg.answer('Invalid Input. Please use /edit <id> <new_product> <new_price> <new_quantity>')
        return

    # Исправлен SQL-запрос в соответствии со схемой БД (id, а не order_id)
    async with db.pool.acquire() as conn:
        await conn.execute('''
            update orders
            set product = $1, price = $2, quantity = $3
            where id = $4
''', new_product, new_price, new_quantity, order_id)
    await msg.answer(text="Data updated successfully! Use /select to see the changes")

@dp.message(Command('delete'))
async def cmd_delete(msg: types.Message) -> None:
    try:
        order_id = int(msg.text.split(' ')[1])
    except(ValueError, IndexError):
        await msg.answer('Invalid Input. Please use /delete <id>')
        return

    # Исправлен SQL-запрос в соответствии со схемой БД (id, а не order_id)
    async with db.pool.acquire() as conn:
        await conn.execute('delete from orders where id = $1', order_id)

    await msg.answer(text='Data deleted successfully!')
    
async def main():
    await db.connect()
    await db.create_tables()
    bot = Bot_Tokken
    await dp.start_polling(bot)
    # await db.close() # Эта строка никогда не выполнится, так как start_polling работает бесконечно

if __name__ == '__main__':
    asyncio.run(main())









# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# import asyncpg
# from keyboards.admin_keyboards import admin_keyboards
# from keyboards.user_keyboards import user_keyboards

# from config import db
# from config import Bot_Tokken

# dp = Dispatcher()

# # dp.include_router(admin_router)

# @dp.message(Command('start'))
# async def cmd_start(msg: types.Message) -> None:
#     if msg.from_user.last_name:
#         fullname = msg.from_user.first_name + ' ' + msg.from_user.last_name
#     else:
#         fullname = msg.from_user.first_name

#     # await msg.answer(text="Hello guys I am a crud bot for goods")
#     user = User(msg.from_user.id, msg.from_user.username, fullname, db)
#     if not await user.get_user():
#         await user.save()
#     print(await user.check_status())
#     keyboard = admin_keyboards if await user.check_status() else user_keyboards

#     await msg.answer('Bot start working!', reply_markup=keyboard)


# @dp.message(Command('select'))
# async def cmd_select(msg: types.Message) -> None:
#     async with db.pool.acquire() as conn:
#         result = await conn.fetch('select * from orders')
#     # conn = psycopg2.connect(db)
#     # cursor = conn.cursor()
#     # cursor.execute('select * from orders')
#     # result = cursor.fetchall()
#     # cursor.close()
#     # conn.close()
#     await msg.answer(text="Data from databese: \n{}".format(result))

# @dp.message(Command('insert'))
# async def cmd_insert(msg: types.Message) -> None:
#     try:
#         splitted_msg = msg.text.split(' ')
#         product = splitted_msg[1]
#         price = float(splitted_msg[2])
#         quantity = int(splitted_msg[3])
#     except (ValueError, IndexError):
#         await msg.answer('Invalid Input. Please use /insert <product> <price> <quantity>')

#     async with db.pool.acquire() as conn:
#         await conn.execute(""""
#                 insert into orders (product, price, quantity)
#                 values($1,$2,$3)        
# """, product, price, quantity)
# #     conn = psycopg2.connect(db)
# #     cursor = conn.cursor()

# #     cursor.execute("""
# #         insert into orders (product, price, quantity)
# #         values(%s, %s, %s)
# # """, (product, price, quantity))

# #     conn.commit()
# #     cursor.close()
# #     conn.close()
#     await msg.answer(text="Data inserted successfully!")

# @dp.message(Command('edit'))
# async def cmd_edit(msg: types.Message) -> None:
#     try:
#         splitted_msg = msg.text.split(' ')
#         order_id = int(splitted_msg[1])
#         new_product = splitted_msg[2]
#         new_price = float(msg.text.split(' ')[3])
#         new_quantity = int(msg.text.split(' ')[4])
#     except (ValueError, IndexError):
#         await msg.answer('Invalid Input. Please use /edit <order_id> <new_product> <new_price> <new_quantity>')


#     async with db.pool.acquire() as conn:
#         conn.execute("""
#             update orders
#             set product = %s, price = %s, quantity = %s
#             where order_id = %s
# """, (new_product, new_price, new_quantity, order_id))
#     # conn = psycopg2.connect(db)
#     # cursor = conn.cursor()

# #     cursor.execute("""
# #         update orders
# #         set product = %s, price = %s, quantity = %s
# #         where order_id = %s
# # """, (new_product, new_price, new_quantity, order_id))

#     # conn.commit()
#     # cursor.close()
#     # conn.close()
#     await msg.answer(text="Data updated successfully! Use /select to see the changes")

# @dp.message(Command('delete'))
# async def cmd_delete(msg: types.Message)-> None:
#     try:
#         order_id = int(msg.text.split(' ')[1])
#     except(ValueError, IndexError):
#         await msg.answer('Invalid Input. Please use /delete <order_id>')
#         return

#     async with db.pool.acquire() as conn:
#         await conn.execute('delete from orders where order_id = $1', order_id)
#     # conn = psycopg2.connect(db)
#     # cursor = conn.cursor()
#     # cursor.execute('delete from orders where order_id = %s', (order_id))

#     # conn.commit()
#     # cursor.close()
#     # conn.close()

#     await msg.answer(text='Data deleted successfully!')
    
# async def main():
#     await db.connect()
#     await db.create_tables()
#     await dp.start_polling(Bot_Tokken)
#     await db.close()


# if __name__ == '__main__':
#     asyncio.run(main())
