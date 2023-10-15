##
# @file main.py
# @brief Entry file.
# @details None.
# @author Calm
# @date 2022-12-28
# @version v1.0.0
# @copyright Calm
#

import sys
import atexit
from log import *
from doip import *
from ecu import *
from tstr import *

def main():
    LogTr("Enter main().")

    if sys.argv[1] == "-Ser":
        LogTr("Ecu.")
        Ecu = cEcu()
        atexit.register(Ecu.UdsSer.DoipSer.DisConn) #Registering Callbacks. Exit terminal call callback function.
        Ecu.Ota()
    elif sys.argv[1] == "-Clt":
        LogTr("Tester.")
        Tstr = cTstr()
        atexit.register(Tstr.UdsClt.DoipClt.DisConn) #Registering Callbacks. Exit terminal call callback function.
        Tstr.Ota()

    LogTr("Exit main().")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        LogScs("Keyboard Interrupt. Exit program operation.")
