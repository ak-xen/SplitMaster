from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import  TelegramObject, Update

import potisepents
from data import MasterDB


class IsUser(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        user_id = event.event.from_user.id
        all_masters = await MasterDB.MasterDB.all_user()
        all_masters = map(lambda x: x[0], all_masters)
        if user_id in all_masters or user_id == int(potisepents.admin_id):
            return await handler(event, data)
