from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from data import MasterDB


class IsUser(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user_id = event.__dict__['message'].__dict__['chat'].id
        all_masters = await MasterDB.MasterDB.all_user()
        if user_id in all_masters:
            return await handler(event, data)
