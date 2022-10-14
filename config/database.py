from sqlalchemy import create_engine, MetaData, inspect


DB_URL = 'postgresql+psycopg2://dev_test:linuxc@localhost:5432/first_db'


engine = create_engine(DB_URL)


connection = engine.connect()

meta = MetaData()
meta.bind = connection
