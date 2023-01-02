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

    Tester = doip.Doip("127.0.0.2", "127.0.0.1", 9998, 9999)
    Tester.Conn()
    Tester.ReqRteAct()
    Tester.RespRteAct()
    Tester.ReqDiag("1003")
    Tester.RespDiag()

    LogTr("Exit main().")

if __name__ == "__main__":
    main()
