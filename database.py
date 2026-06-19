import aiosqlite

DB_NAME = "antigbot.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS allowed_bots (
                chat_id INTEGER,
                bot_username TEXT,
                PRIMARY KEY (chat_id, bot_username)
            )
        """)
        await db.commit()

async def allow_bot(chat_id: int, bot_username: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO allowed_bots (chat_id, bot_username) VALUES (?, ?)",
            (chat_id, bot_username)
        )
        await db.commit()

async def remove_bot(chat_id: int, bot_username: str) -> int:
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "DELETE FROM allowed_bots WHERE chat_id = ? AND bot_username = ?",
            (chat_id, bot_username)
        )
        await db.commit()
        return cursor.rowcount

async def get_allowed_bots(chat_id: int) -> list:
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT bot_username FROM allowed_bots WHERE chat_id = ?", (chat_id,))
        rows = await cursor.fetchall()
        return [row[0] for row in rows]