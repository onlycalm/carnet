##
# @file main.py
# @brief 入口文件。
# @details 无
# @author Calm
# @date 2022-12-28
# @version v1.0.0
# @copyright Calm
#

import sys
from log import *
import doip

def main():
    LogTr("Enter main().")

    Tstr = doip.cDoip("127.0.0.1", "127.0.0.1", 9998, 13400)
    Tstr.Conn()
    Tstr.ReqRteAct()
    Tstr.RespRteAct()
    Tstr.ReqDiag("1003")
    Tstr.RespDiag()

    LogTr("Exit main().")

if __name__ == "__main__":
    main()
