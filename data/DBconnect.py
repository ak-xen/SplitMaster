from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine(f'sqlite:///data/DB.db', echo=True)


class Base(DeclarativeBase):
    pass


class TaskDB(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    description = Column(String)
    lead_time = Column(String)
    address = Column(String)
    price = Column(Integer)
    telephone_number = Column(Integer)
    master = Column(String)
    time_created = Column(String)
    is_took = Column(Integer)


Session = sessionmaker(autoflush=False, bind=engine)


# d = {
#     'task': "split",
#     'address': 'zalupovo',
#     'is_took': 0,
#     'time_created': "22.03.022",
# }
# with Session(autoflush=False, bind=engine) as db:
#     task = TaskDB(**d)
#     db.add(task)
#     db.commit()
#

async def add_task(task: dict):
    with Session(autoflush=False, bind=engine) as db:
        record = TaskDB(**task)
        db.add(record)
        db.commit()
