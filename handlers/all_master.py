from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from data.MasterDB import MasterDB

router = Router()


@router.message(Command(commands=['allm']))
async def get_all_master(message: types.Message):
    all_master = await MasterDB.all_user()
    if all_master:
        msg = ''
        for i in all_master:
            name, family = await MasterDB.get_master_name(*i)
            msg += f'{i[0]}: {name} {family}\n'
        await message.answer(msg)
