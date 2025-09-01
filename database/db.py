import asyncpg


class DatabaseConfig:

    def __init__(self, user, password, db_name, port=5432, host='localhost'):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = port
        self.host = host
        self.pool = None

    async def connect(self):
        try:
            self.pool = await asyncpg.create_pool(
                user=self.user,
                password=self.password,
                database=self.db_name,
                port=self.port,
                host=self.host
            )
        except Exception as e:
            print('Error from connect:', e)

    async def close(self):
        await self.pool.close()

    async def create_tables(self):
        try:
            async with self.pool.acquire() as conn:
                await conn.execute("""
            CREATE TABLE orders (
                id SERIAL PRIMARY KEY,
                product varchar(200),
                price float,
                quantity smallint
            );

            CREATE TABLE categories (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                telegram_id INT,
                fullname varchar(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE questions (
                id SERIAL PRIMARY KEY,
                category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
                question_text TEXT NOT NULL,
                option_a VARCHAR(255) NOT NULL,
                option_b VARCHAR(255) NOT NULL,
                option_c VARCHAR(255) NOT NULL,
                option_d VARCHAR(255) NOT NULL,
                correct_option CHAR(1) CHECK (correct_option IN ('A', 'B', 'C', 'D')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE results (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
                score INTEGER NOT NULL CHECK (score >= 0 AND score <= 100),
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
    """)
        except Exception as e:
            print('Error from tables:', e)


