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
            self.Doip.ReqDiag("1003")
            self.Doip.RespDiag()

        LogTr("Exit cTstr.Ota()")
