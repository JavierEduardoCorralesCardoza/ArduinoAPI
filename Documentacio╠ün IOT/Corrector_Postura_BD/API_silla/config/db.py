from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/corrector_de_postura")
#conn = engine.connect()
metadata = MetaData()
