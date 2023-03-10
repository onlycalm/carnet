##
# @file log.py
# @brief log模块。
# @details 无
# @author Calm
# @date 2021-09-01
# @version v1.0.0
# @copyright Calm
#

import sys
from loguru import logger

logger.remove(handler_id = None) #清除设置。
#log输出到终端。
logger.add(sys.stderr, format = "{time:YYYY-MM-DD HH:mm:ss.SSS} [{level}] {module}:{function}:{line} - {message}",
           level = "TRACE", enqueue = True)
#log输出到文件。
logger.add("./log/{time:YYYY-MM-DD}.log",
           format = "{time:YYYY-MM-DD HH:mm:ss.SSS} [{level}] {module}:{function}:{line} - {message}",
           level = "DEBUG", rotation = "00:00", retention = "1 months", compression = "zip",
           encoding = "utf-8", enqueue = True)

LogCrt = logger.critical #Lv50。
LogErr = logger.error    #Lv40。
LogWrn = logger.warning  #Lv30。
LogScs = logger.success  #Lv25。
LogInf = logger.info     #Lv20。
LogDbg = logger.debug    #Lv10。
LogTr = logger.trace     #Lv5。
Log = logger.log         #指定等级。
