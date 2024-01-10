from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine(f'sqlite:///C:/Users/Munhen/PycharmProjects/SplitMaster/data/DB.db', echo=True)


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
    status = Column(Integer)


Session = sessionmaker(autoflush=False, bind=engine)


async def add_task(task: dict):
    with Session(autoflush=False, bind=engine) as db:
        record = TaskDB(**task)
        db.add(record)
        db.commit()
        return record.id


async def get_telephone_number(id_task):
    with Session(autoflush=False, bind=engine) as db:
        datas = db.query(TaskDB).filter(TaskDB.id == id_task).first()
        return datas.telephone_number


async def change_status(id_task):
    with Session(autoflush=False, bind=engine) as db:
        datas = db.query(TaskDB).filter(TaskDB.id == id_task).first()
        datas.status = 1
        db.commit()