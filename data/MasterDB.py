import aiosqlite

path_db = "data/Db.db"


class MasterDB:
    id: int
    name: str
    family: str
    telephone_number: int

    @staticmethod
    async def all_user():
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT id FROM master") as cursor:
                master_id = await cursor.fetchall()
                master_id = master_id[0]
                return master_id




