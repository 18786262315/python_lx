from sqlalchemy import create_engine
from Common import Log

Logger = Log.Logger(logger_name='检测库是否存在')
log = Logger.get_logger()

class Ku_Name:

    def Ku_(url,ku_name):
        try:
            engine = create_engine(url)
            conn = engine.connect()
            conn.execute("create database %s"%ku_name)
            conn.close()
            log.info("----->>数据库不存在---->>创建库")
        except Exception as e:
            log.info("----->>库已存在")
            return e