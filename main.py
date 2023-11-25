import os
import sys
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from dotenv import load_dotenv
from start import router

load_dotenv(".env")


async def main() -> None:
    bot = Bot(token=os.getenv("TOKEN"), parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher()
    dp.include_router(router)
    commands = [
        BotCommand(command="/start", description="Botni ishga tushurish uchun bosing!!!")
    ]
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except Exception:
        logging.info("Bot stopped!!!")
