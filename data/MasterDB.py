import aiosqlite

path_db = "data/Db.db"


class TaskDB:
    id: int
    name: str
    family: str
    telephone_number: int

    async def add_id_master_in_taskdb(self, id_task, user_id):
        async with aiosqlite.connect(path_db) as db:
            await db.execute(f"UPDATE orders SET master='{user_id}' WHERE id='{id_task}'")
