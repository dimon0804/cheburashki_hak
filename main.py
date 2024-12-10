from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
import asyncio
import logging
from handlers import router

from config import BOT_TOKEN, DEBUG


async def main():
    default= DefaultBotProperties(parse_mode="HTML", link_preview_is_disabled=True)
    bot = Bot(token=BOT_TOKEN, default=default)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
# Установка команд бота
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить/Перезапустить бота")]
    await bot.set_my_commands(commands)

if __name__ == "__main__":
    try:
        if DEBUG:
            logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        pass