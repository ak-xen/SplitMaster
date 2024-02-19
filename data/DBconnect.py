import aiosqlite


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


path_db = "data/Db.db"
