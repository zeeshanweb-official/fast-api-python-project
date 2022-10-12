from sqlalchemy import Table, Column, Integer, String, inspect, select
from config.database import meta, engine

users = Table(
    "users", meta,
    Column('id', Integer(), primary_key=True, autoincrement=True),
    Column('name', String(100)),
    Column('email', String(255), unique=True),
    Column('password', String(1500))
)


def create_table_if_not_found(engine):
    ins = inspect(engine)
    ret = ins.dialect.has_table(engine.connect(), 'users')
    meta.create_all()


create_table_if_not_found(engine)
