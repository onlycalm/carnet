##
# @file ecu.py
# @brief ECU device.
# @details None.
# @author Calm
# @date 2023-05-13
# @version v1.0.0
# @copyright Calm
#

from log import *
from doip import *

class cEcu:
    def __init__(self):
        LogTr("Enter cEcu.__init__()")

        self.Doip = cDoipSer()

        LogTr("Exit cEcu.__init__()")

    def Ota(self):
        LogTr("Enter cEcu.Ota()")

        self.Doip.Lsn()

        while True:
            if self.Doip.IsRecvBufMty() == False:
                RecvMsg = self.Doip.Recv()
                LogDbg(f"RecvMsg: {RecvMsg}")

                Hdr, Pl = self.Doip.Msg.PrsMsg(RecvMsg)
                LogDbg(f"Hdr = {Hdr}")
                LogDbg(f"Pl = {Pl}")

                ProtoVer, InvProtoVer, PlTyp, PlLen = self.Doip.Msg.Hdr.PrsHdr(Hdr)
                LogDbg(f"ProtoVer = {ProtoVer}")
                LogDbg(f"InvProtoVer = {InvProtoVer}")
                LogDbg(f"PlTyp = {PlTyp}")
                LogDbg(f"PlLen = {PlLen}")

                if PlTyp == self.Doip.MsgPset.Hdr.PlTyp.RteActReq:
                    LogTr("Routing activation request.")

                    SrcAdr, ActTyp, Rsv, OemSpec = self.Doip.Msg.Pl.PrsPlRteActReq(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"ActTyp = {ActTyp}")
                    LogDbg(f"Rsv = {Rsv}")
                    LogDbg(f"OemSpec = {OemSpec}")
                    self.Doip.TgtAdr = SrcAdr
                    LogDbg(f"self.Doip.TgtAdr = {self.Doip.TgtAdr}")

                    self.Doip.RespRteAct()
                elif PlTyp == self.Doip.MsgPset.Hdr.PlTyp.DiagMsg:
                    LogTr("Diagnostic message.")

                    SrcAdr, TgtAdr, UsrDat = self.Doip.Msg.Pl.PrsPlDiag(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"TgtAdr = {TgtAdr}")
                    LogDbg(f"UsrDat = {UsrDat}")

                    self.Doip.PosAckDiagMsg("00")

        LogTr("Exit cEcu.Ota()")
