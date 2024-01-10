from sqlalchemy import create_engine, ForeignKey
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
    master = Column(Integer)
    time_created = Column(String)
    status = Column(Integer)


class MasterDB(Base):
    __tablename__ = "master"

    id = Column(Integer, ForeignKey('orders.master'), primary_key=True)
    name = Column(String)
    family = Column(String)
    telephone_number = Column(String)


Session = sessionmaker(autoflush=False, bind=engine)


async def add_task(task: TaskDB):
    with Session(autoflush=False, bind=engine) as db:
        db.add(task)
        db.commit()
        return task.id


async def get_telephone_number(id_task):
    with Session(autoflush=False, bind=engine) as db:
        datas = db.query(TaskDB).filter(TaskDB.id == id_task).first()
        return datas.telephone_number


async def add_id_master_in_taskdb(id_task, user_id):
    with Session(autoflush=False, bind=engine) as db:
        datas = db.query(TaskDB).filter(TaskDB.id == id_task).first()
        datas.status = 1
        datas.master = user_id
        db.commit()
