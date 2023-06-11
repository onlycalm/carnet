##
# @file tstr.py
# @brief Tester.
# @details None.
# @author Calm
# @date 2023-05-13
# @version v1.0.0
# @copyright Calm
#

from log import *
from doip import *

class cTstr:
    def __init__(self):
        LogTr("Enter cTstr.__init__()")

        self.Doip = cDoipClt()

        LogTr("Exit cTstr.__init__()")

    def Ota(self):
        LogTr("Enter cTstr.Ota()")

        if self.Doip.Conn():
            LogScs("Tcp connection succeeded.")

            self.Doip.ReqRteAct()
            PlTyp, RteActRespCode = self.Doip.RespRteAct()
            LogDbg("PlTyp = 0x%04X" % PlTyp)
            LogDbg("RteActRespCode = 0x%04X" % RteActRespCode)
            self.Doip.ReqDiag("1003")
            self.Doip.RespDiag()

        LogTr("Exit cTstr.Ota()")
