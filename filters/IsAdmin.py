from aiogram.filters import BaseFilter
from aiogram.types.message import Message

import potisepents
from data.MasterDB import MasterDB


class IsAdmin(BaseFilter):

    async def __call__(self, msg: Message):
        user = str(msg.from_user.id)
        status = await MasterDB.get_status(user)
        if status != 'admin' and user == potisepents.admin_id:
            await msg.answer('Только для админов!')
            return False
        return True
