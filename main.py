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
from doip import *

def main():
    LogTr("Enter main().")
    Tester = cDoip()
    LogTr("Exit main().")

if __name__ == "__main__":
    main()
