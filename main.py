import logging
import asyncio
from aiogram import Dispatcher
from handlers import start, give_task
from bot import bot, on_startup


async def main():
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(give_task.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), on_startup=await on_startup())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())