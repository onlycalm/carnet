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
from uds import *

class cEcu:
    def __init__(self):
        LogTr("Enter cEcu.__init__()")

        self.UdsSer = cUdsSer()

        LogTr("Exit cEcu.__init__()")

    def Ota(self):
        LogTr("Enter cEcu.Ota()")

        self.UdsSer.Lsn()

        while True:
            if self.UdsSer.DoipSer.IsRecvBufMty() == False:
                RecvMsg = self.UdsSer.DoipSer.Recv()
                LogDbg(f"RecvMsg: {RecvMsg}")

                if RecvMsg != "":
                    Hdr, Pl = self.UdsSer.DoipSer.Msg.PrsMsg(RecvMsg)
                    LogDbg(f"Hdr = {Hdr}")
                    LogDbg(f"Pl = {Pl}")

                    ProtoVer, InvProtoVer, PlTyp, PlLen = self.UdsSer.DoipSer.Msg.Hdr.PrsHdr(Hdr)
                    LogDbg(f"ProtoVer = {ProtoVer}")
                    LogDbg(f"InvProtoVer = {InvProtoVer}")
                    LogDbg(f"PlTyp = {PlTyp}")
                    LogDbg(f"PlLen = {PlLen}")

                    if PlTyp == self.UdsSer.DoipSer.MsgPset.Hdr.PlTyp.RteActReq:
                        LogTr("Routing activation request.")
                        SrcAdr, ActTyp, Rsv, OemSpec = self.UdsSer.DoipSer.Msg.Pl.PrsPlRteActReq(Pl)
                        LogDbg(f"SrcAdr = {SrcAdr}")
                        LogDbg(f"ActTyp = {ActTyp}")
                        LogDbg(f"Rsv = {Rsv}")
                        LogDbg(f"OemSpec = {OemSpec}")
                        self.UdsSer.DoipSer.TgtAdr = SrcAdr
                        LogDbg(f"self.UdsSer.DoipSer.TgtAdr = {self.UdsSer.DoipSer.TgtAdr}")

                        self.UdsSer.DoipSer.RespRteAct()
                    elif PlTyp == self.UdsSer.DoipSer.MsgPset.Hdr.PlTyp.DiagMsg:
                        LogTr("Diagnostic message.")
                        SrcAdr, TgtAdr, UsrDat = self.UdsSer.DoipSer.Msg.Pl.PrsPlDiag(Pl)
                        LogDbg(f"SrcAdr = {SrcAdr}")
                        LogDbg(f"TgtAdr = {TgtAdr}")
                        LogDbg(f"UsrDat = {UsrDat}")

                        self.UdsSer.DoipSer.PosAckDiagMsg("00")

        LogTr("Exit cEcu.Ota()")
