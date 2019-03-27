# 重写logging模块
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import time
 
class Logger:
    logname = time.strftime("%y-%m-%d", time.localtime())
    file_name = '%s.log'%logname
    backup = 5
    console_out_level = 'WARNING'
    file_out_level = 'DEBUG'
    fmt = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s:%(message)s")
    log_path = R"test_cc_HT\Flie\loging"
 
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
 
    def get_logger(self):
        if not self.logger.handlers:
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(self.fmt)
            console_handle.setLevel(self.console_out_level)
            self.logger.addHandler(console_handle)
 
            file_handle = TimedRotatingFileHandler(
                filename=os.path.join(
                    self.log_path,
                    self.file_name),
                when='D',
                interval=1,
                backupCount=self.backup,
                delay=True,
                encoding='utf-8')
            file_handle.setFormatter(self.fmt)
            file_handle.setLevel(self.file_out_level)
            self.logger.addHandler(file_handle)
        return self.logger
 
    def debug(self, msg):
        self.logger.debug(msg)
 
    def info(self, msg):
        self.logger.info(msg)
 
    def warning(self, msg):
        self.logger.warning(msg)
 
    def error(self, msg):
        self.logger.error(msg)


if __name__ == "__main__":
    Logger = Logger(logger_name='当前模块---》test')
    log = Logger.get_logger()
    log.info('——————————》》》23232321!!')
    log.debug('-------->>>123213!!!!002')
    log.error('#####错误！！')
    
