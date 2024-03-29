import aiosqlite

path_db = "data/DB.db"


class MasterDB:
    id: int
    name: str
    family: str
    status: str
    telephone_number: int

    @staticmethod
    async def del_master(id):
        async with aiosqlite.connect(path_db) as db:
            await db.execute(f'DELETE FROM master WHERE id="{id}"')
            await db.commit()

    @staticmethod
    async def all_user():
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT id FROM master") as cursor:
                master_id = await cursor.fetchall()
                master_id = master_id if master_id else []
                return master_id

    async def add_user(self):
        async with aiosqlite.connect(path_db) as db:
            await db.execute(
                f"""INSERT INTO master (id, status, name, family, telephone_number) VALUES ("{self.id}", "{self.status}", "{self.name}", "{self.family}", "{self.telephone_number}")"""
            )
            await db.commit()

    @staticmethod
    async def get_status(master_id):
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT status FROM master WHERE id = ?", (master_id,)) as cursor:
                status = await cursor.fetchone()
                return status[0] if status else []

    @staticmethod
    async def get_master_name(id):
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT name, family FROM master WHERE id = ?", (id,)) as cursor:
                name, family = await cursor.fetchone()
                return name, family
