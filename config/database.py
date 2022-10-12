from sqlalchemy import create_engine, MetaData, inspect


DB_URL = 'mysql+pymysql://root:root@localhost:3306/first_db'


engine = create_engine(DB_URL)


connection = engine.connect()

meta = MetaData()
meta.bind = connection
