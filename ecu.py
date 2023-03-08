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
                LogDbg("ProtoVer = 0x%02X" % ProtoVer)
                LogDbg("InvProtoVer = 0x%02X" % InvProtoVer)
                LogDbg("PlTyp = 0x%04X" % PlTyp)
                LogDbg(f"PlLen = {PlLen}")

                if PlTyp == self.Doip.MsgPset.Hdr.PlTyp.RteActReq:
                    LogTr("Routing activation request.")
                    SrcAdr, ActTyp, Rsv, OemSpec = self.Doip.Msg.Pl.PrsPlRteActReq(Pl)
                    LogDbg("SrcAdr = 0x%04X" % SrcAdr)
                    LogDbg("ActTyp = 0x%02X" % ActTyp)
                    LogDbg("Rsv = 0x%08X" % Rsv)
                    LogDbg("OemSpec = " + "" if OemSpec == None else "%08X" % OemSpec)
                    self.Doip.TgtAdr = SrcAdr
                    LogDbg("self.Doip.TgtAdr = 0x%04X" % self.Doip.TgtAdr)

                    self.Doip.RespRteAct()
                elif PlTyp == self.Doip.MsgPset.Hdr.PlTyp.DiagMsg:
                    LogTr("Diagnostic message.")
                    SrcAdr, TgtAdr, UsrDat = self.Doip.Msg.Pl.PrsPlDiag(Pl)
                    LogDbg("SrcAdr = 0x%04X" % SrcAdr)
                    LogDbg("TgtAdr = 0x%04X" % TgtAdr)
                    LogDbg(f"UsrDat = {UsrDat}")

                    self.Doip.RespDiag("1101")

        LogTr("Exit cEcu.Ota()")
