from aiogram.filters import BaseFilter
from aiogram.types.message import Message
from data.MasterDB import MasterDB


class IsAdmin(BaseFilter):

    async def __call__(self, msg: Message):
        user = str(msg.from_user.id)
        print(user)
        status = await MasterDB.get_status(user)
        if status != 'admin':
            await msg.answer('Только для админов!')
            return False
        return True
