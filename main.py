import logging
import asyncio
from aiogram import Dispatcher
from handlers import start, give_task, take_task, completed_job, add_user
from bot import bot, on_startup
from middlewares import IsUser


async def main():
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(give_task.router)
    dp.include_router(take_task.router)
    dp.include_router(completed_job.router)
    dp.include_router(add_user.router)
    dp.update.outer_middleware(IsUser.IsUser())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), on_startup=await on_startup())


if __name__ == '__main__':
    import data.DBcreate

    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
