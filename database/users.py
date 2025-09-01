from database.db import DatabaseConfig

class User:
    def __init__(self, telegram_id, username, fullname, db: DatabaseConfig):
        self.telegram_id = telegram_id
        self.username = username
        self.fullname = fullname
        self.db = db

    async def save(self):
        try:
            async with self.db.pool.acquire() as conn:
                await conn.execute("""
                insert into users (telegram_id, username, fullname)
                values($1,$2,$3)
""", (self.telegram_id, self.username, self.fullname))
        except Exception as e:
            print('Errror from user save:', e)

    async def get_user(self) -> bool:
        try:
            async with self.db.pool.acquire() as conn:
                # Исправлен запрос: запрашиваем telegram_id для проверки существования
                user = await conn.fetchrow("""
        select telegram_id from users where telegram_id = $1
""", self.telegram_id)
                return user is not None
        except Exception as e:
            print('Error from get_user:', e)
            return False
    
    async def check_status(self):
        # В вашей БД НЕТ колонки is_staff!
        # Временно возвращаем False, чтобы клавиатура пользователя работала.
        # Вам нужно либо добавить этот столбец в БД, либо переписать логику.
        return False
        # try:
        #     async with self.db.pool.acquire() as conn:
        #         is_staff = await conn.fetchrow("""
        # select is_staff from users where telegram_id = $1;                
        # """, self.telegram_id)
        #         return is_staff['is_staff']
        # except Exception as e:
        #     print('Error from check status:', e)
        #     return False









# from itertools import tee
# from db import DatabaseConfig

# class User:
#     def __init__(self, telegram_id, username, fullname, db:DatabaseConfig):
#         self.telegram_id = telegram_id
#         self.username = username
#         self.fullname = fullname
#         self.db = db
#     async def save(self):
#         try:
#             async with self.db.pool.acquire() as conn:
#                 await conn.execute("""
#                 insert into users (telegram_id, username, fullname)
#                 values($1,$2,$3)
# """, (self.telegram_id, self.username, self.fullname))

#         except Exception as e:
#             print('Errror from user save:', e)

#     async def get_user(self) -> bool:
#         try:
#             async with self.db.pool.acquire() as conn:
#                 user = await conn.fetch("""
#         select id from users where telegram_id = $1
# """, self.telegram_id)
#                 return True if user else False
#         except Exception as e:
#             print('Error from get_user:', e)
    
#     async def check_status(self,):
#         try:
#             async with self.db.pool.acquire() as conn:
#                 is_staff = await conn.fetchrow("""
#         select is_staff from users where telegram_id = $1;                
# """, self.telegram_id)
#                 return is_staff['is_staff']
#         except Exception as e:
#             print('Error from check status:', e)