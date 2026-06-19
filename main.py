import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ChatMemberStatus
from database import init_db, allow_bot, remove_bot, get_allowed_bots

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def is_admin(message: types.Message) -> bool:
    if message.sender_chat and message.sender_chat.id == message.chat.id:
        return True
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in [ChatMemberStatus.CREATOR, ChatMemberStatus.ADMINISTRATOR]

@dp.message(Command("allow"))
async def add_exception(message: types.Message):
    if message.chat.type in ["group", "supergroup"] and not await is_admin(message):
        return

    args = message.text.split()
    if len(args) < 2:
        await message.reply("⚠️ Please provide a bot username.\nExample: `/allow @bot_username`", parse_mode="Markdown")
        return

    target = args[1].replace("@", "").lower()
    await allow_bot(message.chat.id, target)
    await message.reply(f"✅ Bot `@{target}` is now allowed to operate in this group.", parse_mode="Markdown")

@dp.message(Command("remove"))
async def remove_exception(message: types.Message):
    if message.chat.type in ["group", "supergroup"] and not await is_admin(message):
        return

    args = message.text.split()
    if len(args) < 2:
        await message.reply("⚠️ Please provide a bot username.\nExample: `/remove @bot_username`", parse_mode="Markdown")
        return

    target = args[1].replace("@", "").lower()
    deleted_count = await remove_bot(message.chat.id, target)

    if deleted_count > 0:
        await message.reply(f"🗑 Bot `@{target}` has been removed from the allowed list.", parse_mode="Markdown")
    else:
        await message.reply(f"ℹ️ Bot `@{target}` was not in the allowed list.", parse_mode="Markdown")

@dp.message(Command("list"))
async def list_exceptions(message: types.Message):
    if message.chat.type in ["group", "supergroup"] and not await is_admin(message):
        return

    allowed_bots = await get_allowed_bots(message.chat.id)
    if not allowed_bots:
        await message.reply("📋 There are no allowed bots in this group. All guest bots will be deleted.")
        return

    text = "📋 **Allowed Bots:**\n\n"
    for b in allowed_bots:
        text += f"🔸 `@{b}`\n"

    await message.reply(text, parse_mode="Markdown")

@dp.message(F.from_user.is_bot)
async def handle_bot_messages(message: types.Message):
    me = await bot.get_me()
    if message.from_user.id == me.id:
        return

    bot_username = message.from_user.username.lower() if message.from_user.username else ""
    allowed_bots = await get_allowed_bots(message.chat.id)

    if bot_username not in allowed_bots:
        try:
            await message.delete()
            if message.reply_to_message:
                await message.reply_to_message.delete()
        except Exception:
            pass

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())