import aiosqlite

path_db = "data/Db.db"


class TaskDB:
    id: int
    task: str
    description: str
    lead_time: str
    address: str
    price: str
    telephone_number: str
    master: str
    time_created: str
    status: int

    async def add_task(self):
        async with aiosqlite.connect(path_db) as db:
            await db.execute(
                f"""INSERT INTO orders (task, description, lead_time, address, price, telephone_number) VALUES ("{self.task}", "{self.description}", "{self.lead_time}", "{self.address}", "{self.price}", "{self.telephone_number}")"""
            )
            await db.commit()
            id = await db.execute(
                "SELECT last_insert_rowid()"
            )
            return await id.fetchone()

    async def get_telephone_number(self, id):
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT telephone_number FROM orders WHERE id = ?", (id,)) as cursor:
                tp = await cursor.fetchone()
                return tp[0]

    async def add_id_master_in_taskdb(self, id_task, user_id):
        async with aiosqlite.connect(path_db) as db:
            await db.execute(f"UPDATE orders SET master='{user_id}' WHERE id='{id_task}'")
            await db.commit()