##
# @file doip.py
# @brief Doip protocol.
# @details None.
# @author Calm
# @date 2023-05-13
# @version v1.0.0
# @copyright Calm
#

import sys
import tcp
from exc import *
from log import *

class cMsgPset:
    # ISO 13400-2-2012.
    # Doip message structure.

    class cHdr:
        # Protocol version.
        # Pos = 0, Len = 1.
        class cProtoVer:
            def __init__(self):
                LogTr("Enter cProtoVer.__init__()")

                self.Rsv = "00" # 0x00: Reserved.
                LogDbg(f"self.Rsv = {self.Rsv}")
                self.v2010 = "01" # 0x01: DoIP ISO/DIS 13400-2:2010.
                LogDbg(f"self.v2010 = {self.v2010}")
                self.v2012 = "02" # 0x02: DoIP ISO 13400-2:2012.
                LogDbg(f"self.v2012 = {self.v2012}")
                self.IsoRsv = "03~FE" # 0x03~0xFE: reserved by this part of ISO 13400.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.Vin = "FF" # 0xFF: Default value for vehicle identification request message.
                LogDbg(f"self.Vin = {self.Vin}")

                LogTr("Exit cProtoVer.__init__()")

        # Inverse protocol version.
        # Pos = 1, Len = 1.
        class cInvProtoVer:
            def __init__(self):
                LogTr("Enter cInvProtoVer.__init__()")

                self.Rsv = "FF" #0xFF: Reserved.
                LogDbg(f"self.Rsv = {self.Rsv}")
                self.v2010 = "FE" # 0xFE: DoIP ISO/DIS 13400-2:2010.
                LogDbg(f"self.v2010 = {self.v2010}")
                self.v2012 = "FD" # 0xFD: DoIP ISO 13400-2:2012.
                LogDbg(f"self.v2012 = {self.v2012}")
                self.Rsv = "01~FC" # 0x01~0xFC: reserved by this part of ISO 13400.
                LogDbg(f"self.Rsv = {self.Rsv}")
                self.Vin = "00" # 0x00: Default value for vehicle identification request message.
                LogDbg(f"self.Vin = {self.Vin}")

                LogTr("Exit cInvProtoVer.__init__()")

        # Payload type(GH_PT).
        # Pos = 2, Len = 2.
        class cPlTyp:
            def __init__(self):
                LogTr("Enter cPlTyp.__init__()")

                # Mandatory.
                self.GenDoipHdrNegAck = "0000" # 0x0000: Generic DoIP header negative acknowledge.
                LogDbg(f"self.GenDoipHdrNegAck = {self.GenDoipHdrNegAck}")
                self.VehIdReqMsg = "0001" # 0x0001: Vehicle identification request message.
                LogDbg(f"self.VehIdReqMsg = {self.VehIdReqMsg}")

                # Optional.
                self.VehIdReqMsgEid = "0002" # 0x0002: Vehicle identification request message with EID.
                LogDbg(f"self.VehIdReqMsgEid = {self.VehIdReqMsgEid}")

                # Mandatory.
                self.VehIdReqMsgWithVin = "0003" # 0x0003: Vehicle identification request message with VIN.
                LogDbg(f"self.VehIdReqMsgWithVin = {self.VehIdReqMsgWithVin}")
                self.VehAnncMsg = "0004" # 0x0004: Vehicle announcement message/vehicle identification response message.
                LogDbg(f"self.VehAnncMsg = {self.VehAnncMsg}")
                self.RteActReq = "0005" # 0x0005: Routing activation request.
                LogDbg(f"self.RteActReq = {self.RteActReq}")
                self.RteActResp = "0006" # 0x0006: Routing activation response.
                LogDbg(f"self.RteActResp = {self.RteActResp}")
                self.AlvChkReq = "0007" # 0x0007: Alive check request.
                LogDbg(f"self.AlvChkReq = {self.AlvChkReq}")
                self.AlvChkResp = "0008" # 0x0008: Alive check response.
                LogDbg(f"self.AlvChkResp = {self.AlvChkResp}")

                # Reserve.
                self.IsoRsv = "0009~4000" # 0x0009~0x4000: Reserved by this of ISO 13400.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                # Optional.
                self.DoipEntyStsReq = "4001" # 0x4001: DoIP entity status request.
                LogDbg(f"self.DoipEntyStsReq = {self.DoipEntyStsReq}")
                self.DoipEntyStsResp = "4002" # 0x4002: DoIP entity status response.
                LogDbg(f"self.DoipEntyStsResp = {self.DoipEntyStsResp}")

                # Mandatory.
                self.DiagPwrMdInfoReq = "4003" # 0x4003: Diagnostic power mode information response.
                LogDbg(f"self.DiagPwrMdInfoReq = {self.DiagPwrMdInfoReq}")
                self.DiagPwrMdInfoResp = "4004" # 0x4004: Diagnostic power mode information request.
                LogDbg(f"self.DiagPwrMdInfoResp = {self.DiagPwrMdInfoResp}")

                # Reserve.
                self.IsoRsv1 = "4005~8000" # 0x4005~0x8000: Reserved by this of ISO 13400.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                # Mandatory.
                self.DiagMsg = "8001" # 0x8001: Diagnostic message.
                LogDbg(f"self.DiagMsg = {self.DiagMsg}")
                self.DiagMsgPosAck = "8002" # 0x8002: Diagnostic message positive acknowledegment.
                LogDbg(f"self.DiagMsgPosAck = {self.DiagMsgPosAck}")
                self.DiagMsgNegAck = "8003" # 0x8003: Diagnostic message negative acknowledgement.
                LogDbg(f"self.DiagMsgNegAck = {self.DiagMsgNegAck}")

                # Reserve.
                self.IsoRsv2 = "8004~EFFF" # 0x8004~0xEFFF: Reserved by this of ISO 13400.
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                # Optional.
                self.MfrRsv = "F000~FFFF" # 0xF000~0xFFFF: Reserved for manufacturer-specific use.
                LogDbg(f"self.MfrRsv = {self.MfrRsv}")

                LogTr("Exit cPlTyp.__init__()")

        def __init__(self):
            LogTr("Enter cHdr.__init__()")

            self.ProtoVer = self.cProtoVer()
            self.InvProtoVer = self.cInvProtoVer()
            self.PlTyp = self.cPlTyp()

            LogTr("Exit cHdr.__init__()")

    class cPl:
        class cRteActReq:
            class cActTyp:
                def __init__(self):
                    LogTr("Enter cActTyp.__init__()")

                    # Mandatory.
                    self.Dflt = "00" # 0x00: Default.
                    LogDbg(f"self.Dflt = {self.Dflt}")
                    self.WwhObd = "01" # 0x01: WWH-OBD.
                    LogDbg(f"self.WwhObd = {self.WwhObd}")

                    # Reserve.
                    self.IsoRsv = "02~DF" # 0x02~0xDF: ISO/SAE reserved.
                    LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                    # Optional.
                    self.CntrlSec = "E0" # 0xE0: Central security.
                    LogDbg(f"self.CntrlSec = {self.CntrlSec}")
                    self.OemSpec = "E1~FF" # 0xE1~0xFF: Available for additional OEM-specific use.
                    LogDbg(f"self.OemSpec = {self.OemSpec}")

                    LogTr("Exit cActTyp.__init__()")

            class cRsv:
                def __init__(self):
                    LogTr("Enter cActTyp.__init__()")

                    self.Dflt = "00000000" # 0x00000000: Default
                    LogDbg(f"self.Dflt = {self.Dflt}")

                    LogTr("Exit cActTyp.__init__()")

            def __init__(self):
                LogTr("Enter cRteActReq.__init__()")

                self.ActTyp = self.cActTyp()
                self.Rsv = self.cRsv()

                LogTr("Exit cRteActReq.__init__()")

        class cRteActResp:
            class cRteActRespCode:
                def __init__(self):
                    LogTr("Enter cRteActRespCode.__init__()")

                    # Mandatory.
                    self.UnKSrcAdr = "00" # 0x00: Routine activation denied due to unknown source address.
                    LogDbg(f"self.UnKSrcAdr = {self.UnKSrcAdr}")
                    self.SockRegAct = "01" # 0x01: Routine activation denied bacause all concurrently
                                           # supported TCP_DATA socket are registered and active.
                    LogDbg(f"self.SockRegAct = {self.SockRegAct}")
                    self.SaDiffAlrAct = "02" # 0x02: Routine activation denied because an SA different from the
                                             # table connection entry was received on the already
                                             # activated TCP_DATA socket.
                    LogDbg(f"self.SaDiffAlrAct = {self.SaDiffAlrAct}")
                    self.SaAlrRegActDiff = "03" # 0x03: Routine activation denied because the SA is already
                                                # registered and active on a different TCP_DATA socket.
                    LogDbg(f"self.SaAlrRegActDiff = {self.SaAlrRegActDiff}")

                    # Optional.
                    self.MisAuthn = "04" # 0x04: Routine activation denied due to missing authentication.
                    LogDbg(f"self.MisAuthn = {self.MisAuthn}")
                    self.RejConf = "05" # 0x05: Routine activation denied due to rejected confirmation.
                    LogDbg(f"self.RejConf = {self.RejConf}")

                    # Mandatory.
                    self.UnsptRteAct = "06" # 0x06: Routine activation denied due to unsupported routing activation type.
                    LogDbg(f"self.UnsptRteAct = {self.UnsptRteAct}")

                    # Reserve.
                    self.IsoRsv = "07~0F" # 0x07~0x0F: Reserved by this part of ISO 13400.
                    LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                    # Mandatory.
                    self.RteScsAct = "10" # 0x10: Routing successfuly activated.
                    LogDbg(f"self.RteScsAct = {self.RteScsAct}")

                    # Optional.
                    self.RteWilAct = "11"  # 0x11: Routing will be activated; confirmation required.
                    LogDbg(f"self.RteWilAct = {self.RteWilAct}")

                    # Reserve.
                    self.IsoRsv1 = "12~DF" # 0x12~0xDF: Reserved by this part of ISO 13400.
                    LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                    # Optional.
                    self.VehMfrSpec = "E0~FF" # 0xE0~0xFE: Vehicle-manufacturer specific.
                    LogDbg(f"self.VehMfrSpec = {self.VehMfrSpec}")

                    # Reserve.
                    self.IsoRsv2 = "FF" # 0xFF: Reserved by this part of ISO 13400.
                    LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                    LogTr("Exit cRteActRespCode.__init__()")

            class cRsv:
                def __init__(self):
                    LogTr("Enter cRteActRespCode.__init__()")

                    self.Dflt = "00000000" # 0x00000000: Default
                    LogDbg(f"self.Dflt = {self.Dflt}")

                    LogTr("Exit cRteActRespCode.__init__()")

            def __init__(self):
                LogTr("Enter cRteActResp.__init__()")

                self.RteActRespCode = self.cRteActRespCode()
                self.Rsv = self.cRsv()

                LogTr("Exit cRteActResp.__init__()")

        class cDiagMsg:
            class cPosAckCode:
                def __init__(self):
                    LogTr("Enter cPosAckCode.__init__()")

                    # Mandatory.
                    self.RteCor = "00" # 0x00: Routing confirmation acknowledge (ACK) message indicating that
                                       # the diagnostic message was correctly received, processed and put
                                       # into the transmission buffer of the destination network.
                    LogDbg(f"self.RteCor = {self.RteCor}")

                    # Reserve.
                    self.IsoRsv = "01~FF" # 0x01~0xFF: Reserved by this part of ISO 13400.
                    LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                    LogTr("Exit cPosAckCode.__init__()")

            class cNegAckCode:
                def __init__(self):
                    LogTr("Enter cNegAckCode.__init__()")

                    # Reserve.
                    self.IsoRsv = "00~01" # 0x00~0x01: Reserved by this part of ISO 13400.
                    LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                    # Mandatory.
                    self.InvSrcAdr = "02" # 0x02: Invalid source address.
                    LogDbg(f"self.InvSrcAdr = {self.InvSrcAdr}")
                    self.UnkTgtAdr = "03" # 0x03: Unknown target address.
                    LogDbg(f"self.UnkTgtAdr = {self.UnkTgtAdr}")
                    self.DiagMsgLrg = "04" # 0x04: Diagnostic message too large.
                    LogDbg(f"self.DiagMsgLrg = {self.DiagMsgLrg}")
                    self.OtMem = "05" # 0x05: Out of memory.
                    LogDbg(f"self.OtMem = {self.OtMem}")

                    # Optional.
                    self.TgtUnreach = "06" # 0x06: Target unreachable.
                    LogDbg(f"self.TgtUnreach = {self.TgtUnreach}")
                    self.UnkNet = "07" # 0x07: Unknown network.
                    LogDbg(f"self.UnkNet = {self.UnkNet}")
                    self.TransProtoErr = "08" # 0x08: Transport protocol error.
                    LogDbg(f"self.TransProtoErr = {self.TransProtoErr}")

                    # Reserve.
                    self.IsoRsv1 = "09~FF" # 0x09~0xFF: Reserved by this part of ISO 13400.
                    LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                    LogTr("Exit cNegAckCode.__init__()")

            def __init__(self):
                LogTr("Enter cDiagMsg.__init__()")

                self.PosAckCode = self.cPosAckCode()
                self.NegAckCode = self.cNegAckCode()

                LogTr("Exit cDiagMsg.__init__()")

        def __init__(self):
            LogTr("Enter cPl.__init__()")

            self.RteActReq = self.cRteActReq()
            self.RteActResp = self.cRteActResp()
            self.DiagMsg = self.cDiagMsg()

            LogTr("Exit cPl.__init__()")

    def __init__(self):
        LogTr("Enter cMsgPset.__init__()")

        self.Hdr = self.cHdr()
        self.Pl = self.cPl()

        LogTr("Exit cMsgPset.__init__()")

class cMsg:
    # ISO 13400-2-2012.
    # Doip message structure.

    class cHdr:
        def __init__(self):
            LogTr("Enter cHdr.__init__()")

            pass

            LogTr("Exit cHdr.__init__()")

        def AssemHdr(self, ProtoVer, PlTyp, PlLen):
            LogTr("Enter cHdr.AssemHdr()")

            LogDbg(f"ProtoVer = {ProtoVer}")
            LogDbg(f"PlTyp = {PlTyp}")
            LogDbg(f"PlLen = {PlLen}")

            InvProtoVer = "%02X" % (~int(ProtoVer, 16) & 0xFF)
            LogDbg(f"InvProtoVer = {InvProtoVer}")
            Hdr = ProtoVer + InvProtoVer + PlTyp + PlLen
            LogDbg(f"Hdr = {Hdr}")

            LogTr("Exit cHdr.AssemHdr()")

            return Hdr

        def PrsHdr(self, Hdr):
            LogTr("Enter cHdr.PrsHdr()")

            LogDbg(f"Hdr = {Hdr}")

            ProtoVer = Hdr[0:2]
            LogDbg(f"ProtoVer = {ProtoVer}")
            InvProtoVer = Hdr[2:4]
            LogDbg(f"InvProtoVer = {InvProtoVer}")
            PlTyp = Hdr[4:8]
            LogDbg(f"PlTyp = {PlTyp}")
            PlLen = Hdr[8:16]
            LogDbg(f"PlLen = {PlLen}")

            LogTr("Exit cHdr.PrsHdr()")

            return ProtoVer, InvProtoVer, PlTyp, PlLen

    class cPl:
        def __init__(self):
            LogTr("Enter cPl.__init__()")

            pass

            LogTr("Exit cPl.__init__()")

        def AssemPlRteActReq(self, SrcAdr, ActTyp, Rsv, OemSpec = ""):
            LogTr("Enter cPl.AssemPlRteActReq()")

            # External test equipment address information.
            # Mandatory.
            LogDbg(f"SrcAdr = {SrcAdr}")
            LogDbg(f"ActTyp = {ActTyp}")
            LogDbg(f"Rsv = {Rsv}")

            # Reserved and OEM specific data.
            # Optional.
            LogDbg(f"OemSpec = {OemSpec}")

            Pl = SrcAdr + ActTyp + Rsv + OemSpec
            LogDbg(f"Pl = {Pl}")

            LogTr("Exit cPl.AssemPlRteActReq()")

            return Pl

        def AssemPlRteActResp(self, TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec = ""):
            LogTr("Enter cPl.AssemPlRteActResp()")

            # External test equipment address information.
            # Mandatory.
            LogDbg(f"TstrLgAdr = {TstrLgAdr}")

            # Routing activation status information.
            # Mandatory.
            LogDbg(f"EntyLgAdr = {EntyLgAdr}")
            LogDbg(f"RteActRespCode = {RteActRespCode}")
            LogDbg(f"Rsv = {Rsv}")

            # Optional.
            LogDbg(f"OemSpec = {OemSpec}")

            Pl = TstrLgAdr + EntyLgAdr + RteActRespCode + Rsv + OemSpec
            LogTr(f"Pl = {Pl}")

            LogTr("Exit cPl.AssemPlRteActResp()")

            return Pl

        def PrsPlRteActReq(self, Pl):
            LogTr("Enter cPl.PrsPlRteActReq()")

            LogDbg(f"Pl = {Pl}")

            # External test equipment address information.
            # Mandatory.
            SrcAdr = Pl[0:4]
            LogDbg(f"SrcAdr = {SrcAdr}")
            ActTyp = Pl[4:6]
            LogDbg(f"ActTyp = {ActTyp}")
            Rsv = Pl[6:14]
            LogDbg(f"Rsv = {Rsv}")

            # Reserved and OEM specific data.
            # Optional.
            OemSpec = Pl[14:22]
            LogDbg(f"OemSpec = {OemSpec}")

            LogTr("Exit cPl.PrsPlRteActReq()")

            return SrcAdr, ActTyp, Rsv, OemSpec

        def PrsPlRteActResp(self, Pl):
            LogTr("Enter cPl.PrsPlRteActResp()")

            LogDbg(f"Pl = {Pl}")

            # External test equipment address information.
            # Mandatory.
            TstrLgAdr = Pl[0:4]
            LogDbg(f"TstrLgAdr = {TstrLgAdr}")

            # Routing activation status information.
            # Mandatory.
            EntyLgAdr = Pl[4:8]
            LogDbg(f"EntyLgAdr = {EntyLgAdr}")
            RteActRespCode = Pl[8:10]
            LogDbg(f"RteActRespCode = {RteActRespCode}")
            Rsv = Pl[10:18]
            LogDbg(f"Rsv = {Rsv}")

            # Optional.
            OemSpec = Pl[18:26]
            LogDbg(f"OemSpec = {OemSpec}")

            LogTr("Exit cPl.PrsPlRteActResp()")

            return TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec

        def AssemPlDiag(self, SrcAdr, TgtAdr, UsrDat):
            LogTr("Enter cPl.AssemPlDiag()")

            # Logical address information.
            # Mandatory.
            LogDbg(f"SrcAdr = {SrcAdr}")
            LogDbg(f"TgtAdr = {TgtAdr}")

            # Diagnostic message data.
            # Mandatory.
            LogDbg(f"UsrDat = {UsrDat}")

            Pl = SrcAdr + TgtAdr + UsrDat
            LogDbg(f"Pl = {Pl}")

            LogTr("Exit cPl.AssemPlDiag()")

            return Pl

        def PrsPlDiag(self, Pl):
            LogTr("Enter cPl.PrsPlDiag()")

            # Logical address information.
            # Mandatory.
            SrcAdr = Pl[0:4]
            LogDbg(f"SrcAdr = {SrcAdr}")
            TgtAdr = Pl[4:8]
            LogDbg(f"TgtAdr = {TgtAdr}")

            # Diagnostic message data.
            # Mandatory.
            UsrDat = Pl[8:]
            LogDbg("UsrDat = {UsrDat}")

            LogTr("Exit cPl.PrsPlDiag()")

            return SrcAdr, TgtAdr, UsrDat

        def PrsPlPosDiag(self, Pl):
            LogTr("Enter cPl.PrsPlPosDiag()")

            # Logical address information.
            # Mandatory.
            SrcAdr = Pl[0:4]
            LogDbg(f"SrcAdr = {SrcAdr}")
            TgtAdr = Pl[4:8]
            LogDbg(f"TgtAdr = {TgtAdr}")

            # Diagnostic message acknowledge information.
            # Mandatory.
            AckCode = Pl[8:10]
            LogDbg(f"AckCode = {AckCode}")

            # Optional.
            DiagMsg = Pl[10:]
            LogDbg(f"DiagMsg = {DiagMsg}")

            LogTr("Exit cPl.PrsPlPosDiag()")

            return SrcAdr, TgtAdr, AckCode, DiagMsg

        def PrsPlNegDiag(self, Pl):
            LogTr("Enter cPl.PrsPlNegDiag()")

            # Logical address information.
            # Mandatory.
            SrcAdr = Pl[0:4]
            LogDbg(f"SrcAdr = {SrcAdr}")
            TgtAdr = Pl[4:8]
            LogDbg(f"TgtAdr = {TgtAdr}")

            # Diagnostic message acknowledge information.
            # Mandatory.
            NackCode = Pl[8:10]
            LogDbg(f"NackCode = {NackCode}")

            # Optional.
            DiagMsg = Pl[10:]
            LogDbg(f"DiagMsg = {DiagMsg}")

            LogTr("Exit cPl.PrsPlNegDiag()")

            return SrcAdr, TgtAdr, NackCode, DiagMsg

    def __init__(self):
        LogTr("Enter cMsg.__init__()")

        self.Hdr = self.cHdr()
        LogDbg(f"self.Hdr = {self.Hdr}")
        self.Pl = self.cPl()
        LogDbg(f"self.Pl = {self.Pl}")

        LogTr("Exit cMsg.__init__()")

    def AssemMsg(self, Hdr, Pl):
        LogTr("Enter cMsg.AssemMsg()")

        Msg = Hdr + Pl
        LogDbg(f"Msg = {Msg}")

        LogTr("Exit cMsg.AssemMsg()")

        return Msg

    def PrsMsg(self, Msg):
        LogTr("Enter cMsg.PrsMsg()")

        if len(Msg) // 2 < 8:
            raise DatLenErr

        Hdr = Msg[0:16]
        LogDbg(f"Hdr = {Hdr}")
        Pl = Msg[16:]
        LogDbg(f"Pl = {Pl}")

        LogTr("Exit cMsg.PrsMsg()")

        return Hdr, Pl

class cDoipSer:
    def __init__(self, SrcIpAdr = "127.0.0.1", SrcPt = 13400, SrcAdr = "1000", FunSrcAdr = "E000"):
        LogTr("Enter cDoipSer.__init__()")

        LogDbg(f"SrcIpAdr = {SrcIpAdr}")
        LogDbg(f"SrcPt = {SrcIpAdr}")
        LogDbg(f"SrcAdr = {SrcAdr}")
        LogDbg(f"FunSrcAdr = {FunSrcAdr}")

        self.SrcIpAdr = SrcIpAdr
        LogDbg(f"self.SrcIpAdr = {self.SrcIpAdr}")
        self.SrcPt = SrcPt
        LogDbg(f"self.SrcPt = {self.SrcPt}")
        self.SrcAdr = SrcAdr
        LogDbg(f"self.SrcAdr = {SrcAdr}")
        self.FunSrcAdr = FunSrcAdr
        LogDbg(f"self.FunSrcAdr = {FunSrcAdr}")
        self.TgtAdr = ""
        LogDbg(f"self.TgtAdr = {self.TgtAdr}")
        self.ConnSta = False # Connect status. True: connected, False: not connected.
        LogDbg(f"self.ConnSta = {self.ConnSta}")
        self.Msg = cMsg()
        self.MsgPset = cMsgPset()
        self.TcpSer = tcp.cTcpSer(SrcIpAdr, SrcPt)

        LogTr("Exit cDoipSer.__init__()")

    def Lsn(self):
        LogTr("Enter cDoipSer.Lsn()")

        self.TcpSer.Lsn()
        self.ConnSta = True

        LogTr("Exit cDoipSer.Lsn()")

    def DisConn(self):
        LogTr("Enter cDoipSer.DisConn()")

        if self.ConnSta == True:
            self.TcpSer.DisConn()
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cDoipSer.DisConn()")

    def Snd(self, Msg):
        LogTr("Enter cDoipSer.Snd()")

        if self.ConnSta == True:
            self.TcpSer.Snd(Msg)
            LogInf("Doip send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cDoipSer.Snd()")

    def Recv(self):
        LogTr("Enter cDoipSer.Recv()")

        if self.ConnSta == True:
            Msg = self.TcpSer.Recv()
            LogInf("Doip recv: " + Msg)
        else:
            Msg = ""
            LogErr("Socket not connected, receiving failed.")

        LogTr("Exit cDoipSer.Recv()")

        return Msg

    def IsRecvBufMty(self):
        # LogTr("Enter cDoipSer.IsRecvBufMty()")

        if self.ConnSta == True:
            RecvBufSta = self.TcpSer.IsRecvBufMty()
        else:
            RecvBufSta = None
            LogErr("Socket not connected.")

        # LogTr("Exit cDoipSer.IsRecvBufMty()")

        return RecvBufSta

    def RespRteAct(self):
        LogTr("Enter cDoipSer.RespRteAct()")

        Pl = self.Msg.Pl.AssemPlRteActResp(self.TgtAdr,
                                           self.SrcAdr,
                                           self.MsgPset.Pl.RteActResp.RteActRespCode.RteScsAct,
                                           self.MsgPset.Pl.RteActResp.Rsv.Dflt)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.RteActResp,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.RespRteAct()")

    def PosAckDiagMsg(self, AckCode):
        LogTr("Enter cDoipSer.PosAckDiagMsg()")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, AckCode)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsgPosAck,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.PosAckDiagMsg()")

    def NegAckDiagMsg(self, NegAckCode):
        LogTr("Enter cDoipSer.NegAckDiagMsg()")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, NegAckCode)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsgNegAck,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.NegAckDiagMsg()")

class cDoipClt:
    def __init__(self, SrcIpAdr = "127.0.0.1", TgtIpAdr = "127.0.0.1", SrcPt = 9999, TgtPt = 13400, SrcAdr = "0E00", TgtAdr = "1000", FunTgtAdr = "E000"):
        LogTr("Enter cDoipClt.__init__()")

        LogDbg(f"SrcIpAdr = {SrcIpAdr}")
        LogDbg(f"TgtIpAdr = {TgtIpAdr}")
        LogDbg(f"SrcPt = {TgtPt}")
        LogDbg(f"SrcAdr = {SrcAdr}")
        LogDbg(f"TgtAdr = {TgtAdr}")
        LogDbg(f"FunTgtAdr = {FunTgtAdr}")

        self.SrcIpAdr = SrcIpAdr
        LogDbg(f"self.SrcIpAdr = {self.SrcIpAdr}")
        self.TgtIpAdr = TgtIpAdr
        LogDbg(f"self.TgtIpAdr = {self.TgtIpAdr}")
        self.SrcPt = SrcPt
        LogDbg(f"self.SrcPt = {self.SrcPt}")
        self.TgtPt = TgtPt
        LogDbg(f"self.TgtPt = {self.TgtPt}")
        self.SrcAdr = SrcAdr
        LogDbg(f"self.SrcAdr = {SrcAdr}")
        self.TgtAdr = TgtAdr
        LogDbg(f"self.TgtAdr = {self.TgtAdr}")
        self.FunTgtAdr = FunTgtAdr
        LogDbg(f"self.FunTgtAdr = {self.FunTgtAdr}")
        self.ConnSta = False # Connect status. True: connected, False: not connected.
        LogDbg(f"self.ConnSta = {self.ConnSta}")
        self.Msg = cMsg()
        self.MsgPset = cMsgPset()
        self.TcpClt = tcp.cTcpClt(SrcIpAdr, TgtIpAdr, SrcPt, TgtPt)

        LogTr("Exit cDoipClt.__init__()")

    def Conn(self):
        LogTr("Enter cDoipClt.Conn()")

        ConnRst = False

        if self.ConnSta == False:
            if self.TcpClt.Conn():
                LogScs("Socket connection succeeded.")
                self.ConnSta = True
                ConnRst = True
            else:
                LogErr("Socket connect failed.")
        else:
            LogErr("Connected doip entity!")

        LogTr("Exit cDoipClt.Conn()")

        return ConnRst

    def DisConn(self):
        LogTr("Enter cDoipClt.DisConn()")

        DisConnRst = False

        if self.ConnSta == True:
            if self.TcpClt.DisConn():
                LogScs("Socket connection disconnected.")
                self.ConnSta = False
                DisConnRst = True
            else:
                LogErr("Socket disconnection failed.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cDoipClt.DisConn()")

        return DisConnRst

    def Snd(self, Msg):
        LogTr("Enter cDoipClt.Snd()")

        if self.ConnSta == True:
            self.TcpClt.Snd(Msg)
            LogInf("Doip send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cDoipClt.Snd()")

    def Recv(self):
        LogTr("Enter cDoipClt.Recv()")

        if self.ConnSta == True:
            Msg = self.TcpClt.Recv()
            LogInf("Doip recv: " + Msg)
        else:
            Msg = ""
            LogErr("Socket not connected, receiving failed.")

        LogTr("Exit cDoipClt.Recv()")

        return Msg

    def ReqRteAct(self):
        LogTr("Enter cDoipClt.ReqRteAct()")

        Pl = self.Msg.Pl.AssemPlRteActReq(self.SrcAdr,
                                          self.MsgPset.Pl.RteActReq.ActTyp.Dflt,
                                          self.MsgPset.Pl.RteActReq.Rsv.Dflt)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.RteActReq,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipClt.ReqRteAct()")

    def RespRteAct(self):
        LogTr("Enter cDoipClt.RespRteAct()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        Hdr, Pl = self.Msg.PrsMsg(RecvMsg)
        LogDbg(f"Hdr = {Hdr}")
        LogDbg(f"Pl = {Pl}")
        ProtoVer, InvProtoVer, PlTyp, PlLen = self.Msg.Hdr.PrsHdr(Hdr)
        LogDbg(f"ProtoVer = {ProtoVer}")
        LogDbg(f"InvProtoVer = {InvProtoVer}")
        LogDbg(f"PlTyp = {PlTyp}")
        LogDbg(f"PlLen = {PlLen}")
        TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec = self.Msg.Pl.PrsPlRteActResp(Pl)
        LogDbg(f"TstrLgAdr = {TstrLgAdr}")
        LogDbg(f"EntyLgAdr = {EntyLgAdr}")
        LogDbg(f"RteActRespCode = {RteActRespCode}")
        LogDbg(f"Rsv = {Rsv}")
        LogDbg(f"OemSpec = {OemSpec}")

        if RteActRespCode == self.MsgPset.Pl.RteActResp.RteActRespCode.RteScsAct:
            LogTr("Route activation succeeded.")
        else:
            LogTr("Route activation failed.")

        LogTr("Exit cDoipClt.RespRteAct()")

        return PlTyp, RteActRespCode

    def ReqDiag(self, UsrDat):
        LogTr("Enter cDoipClt.ReqDiag()")

        LogDbg(f"UsrDat = {UsrDat}")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, UsrDat)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsg,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipClt.ReqDiag()")

    def RespDiag(self):
        LogTr("Enter cDoipClt.RespDiag()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        Hdr, Pl = self.Msg.PrsMsg(RecvMsg)
        LogDbg(f"Hdr = {Hdr}")
        LogDbg(f"Pl = {Pl}")
        ProtoVer, InvProtoVer, PlTyp, PlLen = self.Msg.Hdr.PrsHdr(Hdr)
        LogDbg(f"ProtoVer = {ProtoVer}")
        LogDbg(f"InvProtoVer = {InvProtoVer}")
        LogDbg(f"PlTyp = {PlTyp}")
        LogDbg(f"PlLen = {PlLen}")
        SrcAdr, TgtAdr, AckCode, DiagMsg = self.Msg.Pl.PrsPlPosDiag(Pl)
        LogDbg(f"SrcAdr = {SrcAdr}")
        LogDbg(f"TgtAdr = {TgtAdr}")
        LogDbg(f"AckCode = {AckCode}")
        LogDbg(f"DiagMsg = {DiagMsg}")

        if PlTyp == self.MsgPset.Hdr.PlTyp.DiagMsgPosAck:
            LogTr("Diagnostic normal response.")
        else:
            LogTr("Abnormal response of diagnosis.")

        LogTr("Exit cDoipClt.RespDiag()")

        return PlTyp, AckCode

    def IsRecvBufMty(self):
        # LogTr("Enter cDoipClt.IsRecvBufMty()")

        if self.ConnSta == True:
            Rtn = self.TcpClt.IsRecvBufMty()
        else:
            Rtn = None
            LogErr("Socket not connected.")

        # LogTr("Exit cDoipClt.IsRecvBufMty()")

        return Rtn

def ImitEcu():
    LogTr("Enter ImitEcu().")

    Ecu = cDoipSer()
    Ecu.Lsn()

    while True:
        if Ecu.IsRecvBufMty() == False:
            RecvMsg = Ecu.Recv()
            LogDbg(f"RecvMsg: {RecvMsg}")

            if RecvMsg != "":
                Hdr, Pl = Ecu.Msg.PrsMsg(RecvMsg)
                LogDbg(f"Hdr = {Hdr}")
                LogDbg(f"Pl = {Pl}")

                ProtoVer, InvProtoVer, PlTyp, PlLen = Ecu.Msg.Hdr.PrsHdr(Hdr)
                LogDbg(f"ProtoVer = {ProtoVer}")
                LogDbg(f"InvProtoVer = {InvProtoVer}")
                LogDbg(f"PlTyp = {PlTyp}")
                LogDbg(f"PlLen = {PlLen}")

                if PlTyp == Ecu.MsgPset.Hdr.PlTyp.RteActReq:
                    LogTr("Routing activation request.")
                    SrcAdr, ActTyp, Rsv, OemSpec = Ecu.Msg.Pl.PrsPlRteActReq(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"ActTyp = {ActTyp}")
                    LogDbg(f"Rsv = {Rsv}")
                    LogDbg(f"OemSpec = {OemSpec}")
                    Ecu.TgtAdr = SrcAdr
                    LogDbg(f"Ecu.TgtAdr = {Ecu.TgtAdr}")

                    Ecu.RespRteAct()
                elif PlTyp == Ecu.MsgPset.Hdr.PlTyp.DiagMsg:
                    LogTr("Diagnostic message.")
                    SrcAdr, TgtAdr, AckCode, DiagMsg = Ecu.Msg.Pl.PrsPlDiag(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"TgtAdr = {TgtAdr}")
                    LogDbg(f"UsrDat = {UsrDat}")

                    Ecu.PosAckDiagMsg("00")

    LogTr("Exit ImitEcu().")

def ImitTstr():
    LogTr("Enter ImitTstr().")

    Tstr = cDoipClt()
    Tstr.Conn()
    Tstr.ReqRteAct()
    Tstr.RespRteAct()
    Tstr.ReqDiag("1003")
    Tstr.RespDiag()

    LogTr("Exit ImitTstr().")

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        ImitEcu()
    elif sys.argv[1] == "-Clt":
        ImitTstr()
