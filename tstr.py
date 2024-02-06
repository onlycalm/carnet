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
from uds import *

class cTstr:
    def __init__(self):
        LogTr("Enter cTstr.__init__()")

        self.UdsClt = cUdsClt()

        LogTr("Exit cTstr.__init__()")

    def Ota(self):
        LogTr("Enter cTstr.Ota()")

        if self.UdsClt.DoipClt.Conn():
            LogScs("Tcp connection succeeded.")

            self.UdsClt.DoipClt.ReqRteAct()
            PlTyp, RteActRespCode = self.UdsClt.DoipClt.RespRteAct()
            LogDbg(f"PlTyp = {PlTyp}")
            LogDbg(f"RteActRespCode = {RteActRespCode}")
            self.UdsClt.DoipClt.ReqDiag("1003")
            self.UdsClt.DoipClt.RespDiag()

        LogTr("Exit cTstr.Ota()")
