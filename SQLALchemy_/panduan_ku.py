from sqlalchemy import create_engine


class Ku_Name():
    def panduan_ku(url,ku_name):
        try:
            engine = create_engine(url)
            conn = engine.connect()
            conn.execute("create database %s"%ku_name)
            conn.close()
        except Exception as e:
            
            return e