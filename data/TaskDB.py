import aiosqlite
from support import TIME

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
                f"""INSERT INTO orders (task, description, lead_time, address, price, telephone_number,time_created, status) VALUES ("{self.task}", "{self.description}", "{self.lead_time}", "{self.address}", "{self.price}", "{self.telephone_number}","{self.time_created}", "{self.status}")"""
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

    @staticmethod
    async def completed_task(id_task, user_id):
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT master FROM orders WHERE id = ?", (id_task,)) as cursor:
                master = await cursor.fetchone()
                if master[0] == user_id:
                    time_completed = TIME.strftime("%H:%M %d.%m.%Y")
                    await db.execute(
                        f"UPDATE orders SET status='1', time_completed='{time_completed}' WHERE id='{id_task}'"
                    )
                    await db.commit()

    @staticmethod
    async def get_task_info(id_task):
        async with aiosqlite.connect(path_db) as db:
            async with db.execute("SELECT * FROM orders WHERE id = ?", (id_task,)) as cursor:
                data = await cursor.fetchall()
                data = data[0]
                task, address, telephone, time_completed = data[1], data[4], data[6], data[9]
                return task, address, telephone, time_completed

