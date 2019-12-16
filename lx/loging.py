# import logging
# logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d')
# '''
# logging中可以选择很多消息级别，如debug、info、warning、error以及critical、
# 可以设置不同的日志等级，用于控制日志的输出，
# 日志等级：使用范围
# FATAL：致命错误
# CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
# ERROR：发生错误时，如IO操作失败或者连接问题
# WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误
# INFO：处理请求或者状态变化等日常事务
# DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态

# filename：指定日志文件名；
# filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
# format：指定输出的格式和内容，format可以输出很多有用的信息
# datefmt：指定时间格式，同time.strftime()；
# level：设置日志级别，默认为logging.WARNNING；
# stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；

# format参数：
# %(levelno)s：打印日志级别的数值
# %(levelname)s：打印日志级别的名称
# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s：打印当前执行程序名
# %(funcName)s：打印日志的当前函数
# %(lineno)d：打印日志的当前行号
# %(asctime)s：打印日志的时间
# %(thread)d：打印线程ID
# %(threadName)s：打印线程名称
# %(process)d：打印进程ID
# %(message)s：打印日志信息
# '''



# logger = logging.getLogger(__name__)

# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")


# 输出日志到文件
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")



#同时输出到文件以及屏幕
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")

'''
可以发现，logging有一个日志处理的主对象，其他处理方式都是通过addHandler添加进去，logging中包含的handler主要有如下几种，

handler名称：位置；作用

StreamHandler：logging.StreamHandler；日志输出到流，可以是sys.stderr，sys.stdout或者文件
FileHandler：logging.FileHandler；日志输出到文件
BaseRotatingHandler：logging.handlers.BaseRotatingHandler；基本的日志回滚方式
RotatingHandler：logging.handlers.RotatingHandler；日志回滚方式，支持日志文件最大数量和日志文件回滚
TimeRotatingHandler：logging.handlers.TimeRotatingHandler；日志回滚方式，在一定时间区域内回滚日志文件
SocketHandler：logging.handlers.SocketHandler；远程输出日志到TCP/IP sockets
DatagramHandler：logging.handlers.DatagramHandler；远程输出日志到UDP sockets
SMTPHandler：logging.handlers.SMTPHandler；远程输出日志到邮件地址
SysLogHandler：logging.handlers.SysLogHandler；日志输出到syslog
NTEventLogHandler：logging.handlers.NTEventLogHandler；远程输出日志到Windows NT/2000/XP的事件日志
MemoryHandler：logging.handlers.MemoryHandler；日志输出到内存中的指定buffer
HTTPHandler：logging.handlers.HTTPHandler；通过"GET"或者"POST"远程输出到HTTP服务器
'''


# #固定日志文件大小
# import logging
# from logging.handlers import RotatingFileHandler
# logger = logging.getLogger(__name__)
# logger.setLevel(level = logging.INFO)
# #定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
# rHandler = RotatingFileHandler("log.txt",maxBytes = 1*1024,backupCount = 3)
# rHandler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# rHandler.setFormatter(formatter)

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(formatter)

# logger.addHandler(rHandler)
# logger.addHandler(console)

# logger.info("Start print log")
# logger.debug("Do something")
# logger.warning("Something maybe fail.")
# logger.info("Finish")












