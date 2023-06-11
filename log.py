##
# @file log.py
# @brief Log。
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
logger.add(sys.stderr, format = "<level>{time:YYYY-MM-DD HH:mm:ss.SSS} [{level}] {module}:{function}:{line} - {message}</level>",
           level = "TRACE", enqueue = True, colorize = True)
#log输出到文件。
logger.add("./log/{time:YYYY-MM-DD}.log",
           format = "{time:YYYY-MM-DD HH:mm:ss.SSS} [{level}] {module}:{function}:{line} - {message}",
           level = "TRACE", rotation = "00:00", retention = "1 months", compression = "zip",
           encoding = "utf-8", enqueue = True)

LogCrt = logger.critical #CRITICAL Lv50。
LogErr = logger.error    #ERROR Lv40。
LogWrn = logger.warning  #WARNING Lv30。
LogScs = logger.success  #SUCCESS Lv25。
LogInf = logger.info     #INFO Lv20。
LogDbg = logger.debug    #DEBUG Lv10。
LogTr = logger.trace     #TRACE Lv5。
Log = logger.log         #指定等级。
