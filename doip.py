import tcp
from log import *

class cMsgPset:
    #ISO 13400-2-2012.
    #Doip message structure.

    class cHdr:
        #Protocol version.
        #Pos = 0, Len = 1.
        class cProtoVer:
            def __init__(self):
                LogTr("Enter cProtoVer.__init__()")

                self.Rsv = 0x00 #Reserved.
                LogDbg("self.Rsv = 0x%02X" % self.Rsv)
                self.v2010 = 0x01 #0x01: DoIP ISO/DIS 13400-2:2010.
                LogDbg("self.v2010 = 0x%02X" % self.v2010)
                self.v2012 = 0x02 #0x02: DoIP ISO 13400-2:2012.
                LogDbg("self.v2012 = 0x%02X" % self.v2012)
                self.IsoRsv = [x for x in range(0x03, 0xFF)] #0x03...0xFE: reserved by this part of ISO 13400.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.Vin = 0xFF #0xFF: Default value for vehicle identification request message.
                LogDbg("self.Vin = 0x%02X" % self.Vin)

                LogTr("Exit cProtoVer.__init__()")

        #Inverse protocol version.
        #Pos = 1, Len = 1.
        class cInvProtoVer:
            def __init__(self):
                LogTr("Enter cInvProtoVer.__init__()")

                self.Rsv = ~0x00 & 0xFF #Reserved.
                LogDbg("self.Rsv = 0x%02X" % self.Rsv)
                self.v2010 = ~0x01 & 0xFF #0x01: DoIP ISO/DIS 13400-2:2010.
                LogDbg("self.v2010 = 0x%02X" % self.v2010)
                self.v2012 = ~0x02 & 0xFF #0x02: DoIP ISO 13400-2:2012.
                LogDbg("self.v2012 = 0x%02X" % self.v2012)
                self.Rsv = [~x & 0xFF for x in range(0x03, 0xFF)] #0x03...0xFE: reserved by this part of ISO 13400.
                LogDbg(f"self.Rsv = {self.Rsv}")
                self.Vin = ~0xFF & 0xFF #0xFF: Default value for vehicle identification request message.
                LogDbg("self.Vin = 0x%02X" % self.Vin)

                LogTr("Exit cInvProtoVer.__init__()")

        #Payload type(GH_PT).
        #Pos = 2, Len = 2.
        class cPlTyp:
            def __init__(self):
                LogTr("Enter cPlTyp.__init__()")

                #Mandatory.
                self.GenDoipHdrNegAck = 0x0000 #Generic DoIP header negative acknowledge.
                LogDbg("self.GenDoipHdrNegAck = 0x%04X" % self.GenDoipHdrNegAck)
                self.VehIdReqMsg = 0x0001 #Vehicle identification request message.
                LogDbg("self.VehIdReqMsg = 0x%04X" % self.VehIdReqMsg)

                #Optional.
                self.VehIdReqMsgEid = 0x0001 #Vehicle identification request message with EID.
                LogDbg("self.VehIdReqMsgEid = 0x%04X" % self.VehIdReqMsgEid)

                #Mandatory.
                self.VehIdReqMsgWithVin = 0x0003 #Vehicle identification request message with VIN.
                LogDbg("self.VehIdReqMsgWithVin = 0x%04X" % self.VehIdReqMsgWithVin)
                self.VehAnncMsg = 0x0004 #Vehicle announcement message/vehicle identification response message.
                LogDbg("self.VehAnncMsg = 0x%04X" % self.VehAnncMsg)
                self.RteActReq = 0x0005 #Routing activation request.
                LogDbg("self.RteActReq = 0x%04X" % self.RteActReq)
                self.RteActResp = 0x0006 #Routing activation response.
                LogDbg("self.RteActResp = 0x%04X" % self.RteActResp)
                self.AlvChkReq = 0x0007 #Alive check request.
                LogDbg("self.AlvChkReq = 0x%04X" % self.AlvChkReq)
                self.AlvChkResp = 0x0008 #Alive check response.
                LogDbg("self.AlvChkResp = 0x%04X" % self.AlvChkResp)

                #Reserve.
                self.IsoRsv = [x for x in range(0x0009, 0x4001)] #0x0009 to 0x4000. Reserved by this of ISO 13400.
                LogDbg("self.IsoRsv = [0x0009, 0x4000]")

                #Optional.
                self.DoipEntyStsReq = 0x4001 #DoIP entity status request.
                LogDbg("self.DoipEntyStsReq = 0x%04X" % self.DoipEntyStsReq)
                self.DoipEntyStsResp = 0x4002 #DoIP entity status response.
                LogDbg("self.DoipEntyStsResp = 0x%04X" % self.DoipEntyStsResp)

                #Mandatory.
                self.DiagPwrMdInfoReq = 0x4003 #Diagnostic power mode information response.
                LogDbg("self.DiagPwrMdInfoReq = 0x%04X" % self.DiagPwrMdInfoReq)
                self.DiagPwrMdInfoResp = 0x4004 #Diagnostic power mode information request.
                LogDbg("self.DiagPwrMdInfoResp = 0x%04X" % self.DiagPwrMdInfoResp)

                #Reserve.
                self.IsoRsv1 = [x for x in range(0x4005, 0x8001)] #0x4005 to 0x8000. Reserved by this of ISO 13400.
                LogDbg("self.IsoRsv1 = [0x4005, 0x8000]")

                #Mandatory.
                self.DiagMsg = 0x8001 #Diagnostic message.
                LogDbg("self.DiagMsg = 0x%04X" % self.DiagMsg)
                self.DiagMsgPosAck = 0x8002 #Diagnostic message positive acknowledegment.
                LogDbg("self.DiagMsgPosAck = 0x%04X" % self.DiagMsgPosAck)
                self.DiagMsgNegAck = 0x8003  #Diagnostic message negative acknowledgement.
                LogDbg("self.DiagMsgNegAck = 0x%04X" % self.DiagMsgNegAck)

                #Reserve.
                self.IsoRsv1 = [x for x in range(0x8004, 0xF000)] #0x8004 to 0xEFFF. Reserved by this of ISO 13400.
                LogDbg("self.IsoRsv1 = [0x8004, 0xEFFF]")

                #Optional.
                self.MfrRsv = [x for x in range(0xF000, 0x10000)] #0xF000 to 0xFFFF. Reserved for manufacturer-specific use.
                LogDbg("self.MfrRsv = [0xF000, 0xFFFF]")

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

                    #Mandatory.
                    self.Dflt = 0x00 #Default.
                    LogDbg("self.Dflt = 0x%02X" % self.Dflt)
                    self.WwhObd = 0x01 #WWH-OBD.
                    LogDbg("self.WwhObd = 0x%02X" % self.WwhObd)

                    #Reserve.
                    self.IsoRsv = [x for x in range(0x02, 0xE0)] #0x02 to 0xDF. ISO/SAE reserved.
                    LogDbg("self.IsoRsv = [0x02, 0xDF]")

                    #Optional.
                    self.CntrlSec = 0xE0 #Central security.
                    LogDbg("self.CntrlSec = 0x%02X" % self.CntrlSec)
                    self.OemSpec = [x for x in range(0xE1, 0x100)] #0xE1 to 0xFF. Available for additional OEM-specific use.
                    LogDbg("self.OemSpec = [0xE1, 0xFF]")

                    LogTr("Exit cActTyp.__init__()")

            class cRsv:
                def __init__(self):
                    LogTr("Enter cActTyp.__init__()")

                    self.Dflt = 0x00000000 #Default
                    LogDbg("self.Dflt = 0x%08X" % self.Dflt)

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

                    #Mandatory.
                    self.UnKSrcAdr = 0x00 #Routine activation denied due to unknown source address.
                    LogDbg("self.UnKSrcAdr = 0x%02X" % self.UnKSrcAdr)
                    self.SockRegAct = 0x01 #Routine activation denied bacause all concurrently
                                            #supported TCP_DATA socket are registered and active.
                    LogDbg("self.SockRegAct = 0x%02X" % self.SockRegAct)
                    self.SaDiffAlrAct = 0x02 #Routine activation denied because an SA different from the
                                              #table connection entry was received on the already
                                              #activated TCP_DATA socket.
                    LogDbg("self.SaDiffAlrAct = 0x%02X" % self.SaDiffAlrAct)
                    self.SaAlrRegActDiff = 0x03 #Routine activation denied because the SA is already
                                                 #registered and active on a different TCP_DATA socket.
                    LogDbg("self.SaAlrRegActDiff = 0x%02X" % self.SaAlrRegActDiff)

                    #Optional.
                    self.MisAuthn = 0x04 #Routine activation denied due to missing authentication.
                    LogDbg("self.MisAuthn = 0x%02X" % self.MisAuthn)
                    self.RejConf = 0x05 #Routine activation denied due to rejected confirmation.
                    LogDbg("self.RejConf = 0x%02X" % self.RejConf)

                    #Mandatory.
                    self.UnsptRteAct = 0x06 #Routine activation denied due to unsupported routing activation type.
                    LogDbg("self.UnsptRteAct = 0x%02X" % self.UnsptRteAct)

                    #Reserve.
                    self.IsoRsv = [x for x in range(0x07, 0x10)] #0x07 to 0x0F. Reserved by this part of ISO 13400.
                    LogDbg("self.IsoRsv = [0x07, 0x0F]")

                    #Mandatory.
                    self.RteScsAct = 0x10 #Routing successfuly activated.
                    LogDbg("self.RteScsAct = 0x%02X" % self.RteScsAct)

                    #Optional.
                    self.RteWilAct = 0x11  #Routing will be activated; confirmation required.
                    LogDbg("self.RteWilAct = 0x%02X" % self.RteWilAct)

                    #Reserve.
                    self.IsoRsv1 = [x for x in range(0x12, 0xE0)] #0x12 to 0xDF. Reserved by this part of ISO 13400.
                    LogDbg("self.IsoRsv1 = [0x07, 0x0F]")

                    #Optional.
                    self.VehMfrSpec = [x for x in range(0xE0, 0xFF)] #0xE0 to 0xFE. Vehicle-manufacturer specific.
                    LogDbg("self.VehMfrSpec = [0xE0, 0xFF]")

                    #Reserve.
                    self.IsoRsv2 = 0xFF #Reserved by this part of ISO 13400.
                    LogDbg("self.IsoRsv2 = 0x%02X" % self.IsoRsv2)

                    LogTr("Exit cRteActRespCode.__init__()")

            class cRsv:
                def __init__(self):
                    LogTr("Enter cRteActRespCode.__init__()")

                    self.Dflt = 0x00000000 #Default
                    LogDbg("self.Dflt = 0x%08X" % self.Dflt)

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

                    #Mandatory.
                    self.RteCor = 0x00 #Routing confirmation acknowledge (ACK) message indicating that
                                       #the diagnostic message was correctly received, processed and put
                                       #into the transmission buffer of the destination network.
                    LogDbg("self.RteCor = 0x%02X" % self.RteCor)

                    #Reserve.
                    self.IsoRsv = [x for x in range(0x01, 0x100)] #0x01 to 0xFF. Reserved by this part of ISO 13400.
                    LogDbg("self.IsoRsv = [0x01, 0xFF]")

                    LogTr("Exit cPosAckCode.__init__()")

            class cNegAckCode:
                def __init__(self):
                    LogTr("Enter cNegAckCode.__init__()")

                    #Reserve.
                    self.IsoRsv = [x for x in range(0x00, 0x02)] #0x00 to 0x01. Reserved by this part of ISO 13400.
                    LogDbg("self.IsoRsv = [0x00, 0x01]")

                    #Mandatory.
                    self.InvSrcAdr = 0x02 #Invalid source address.
                    LogDbg("self.InvSrcAdr = 0x%02X" % self.InvSrcAdr)
                    self.UnkTgtAdr = 0x03 #Unknown target address.
                    LogDbg("self.UnkTgtAdr = 0x%02X" % self.UnkTgtAdr)
                    self.DiagMsgLrg = 0x04 #Diagnostic message too large.
                    LogDbg("self.DiagMsgLrg = 0x%02X" % self.DiagMsgLrg)
                    self.OtMem = 0x05 #Out of memory.
                    LogDbg("self.OtMem = 0x%02X" % self.OtMem)

                    #Optional.
                    self.TgtUnreach = 0x06 #Target unreachable.
                    LogDbg("self.TgtUnreach = 0x%02X" % self.TgtUnreach)
                    self.UnkNet = 0x07 #Unknown network.
                    LogDbg("self.UnkNet = 0x%02X" % self.UnkNet)
                    self.TransProtoErr = 0x08 #Transport protocol error.
                    LogDbg("self.TransProtoErr = 0x%02X" % self.TransProtoErr)

                    #Reserve.
                    self.IsoRsv1 = [x for x in range(0x09, 0x100)] #0x09 to 0xFF. Reserved by this part of ISO 13400.
                    LogDbg("self.IsoRsv1 = [0x09, 0xFF]")

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
    #ISO 13400-2-2012.
    #Doip message structure.

    class cHdr:
        def __init__(self):
            LogTr("Enter cHdr.__init__()")

            pass

            LogTr("Exit cHdr.__init__()")

        def AssemHdr(self, ProtoVer, PlTyp, PlLen):
            LogTr("Enter cHdr.AssemHdr()")

            LogDbg("ProtoVer = 0x%02X" % ProtoVer)
            InvProtoVer = (~ProtoVer & 0xFF)
            LogDbg("InvProtoVer = 0x%02X" % InvProtoVer)
            LogDbg("PlTyp = 0x%04X" % PlTyp)
            LogDbg(f"PlLen = {PlLen}")

            Hdr = "%02X" % ProtoVer +\
                  "%02X" % InvProtoVer +\
                  "%04X" % PlTyp +\
                  "%08X" % PlLen
            LogDbg(f"Hdr = {Hdr}")

            LogTr("Exit cHdr.AssemHdr()")

            return Hdr

        def PrsHdr(self, Hdr):
            LogTr("Enter cHdr.PrsHdr()")

            LogDbg(f"Hdr = {Hdr}")

            ProtoVer = int(Hdr[0:2], 16)
            LogDbg("ProtoVer = 0x%02X" % ProtoVer)
            InvProtoVer = int(Hdr[2:4], 16)
            LogDbg("InvProtoVer = 0x%02X" % InvProtoVer)
            PlTyp = int(Hdr[4:8], 16)
            LogDbg("PlTyp = 0x%04X" % PlTyp)
            PlLen = int(Hdr[8:16], 16)
            LogDbg(f"PlLen = {PlLen}")

            LogTr("Exit cHdr.PrsHdr()")

            return ProtoVer, InvProtoVer, PlTyp, PlLen

    class cPl:
        def __init__(self):
            LogTr("Enter cPl.__init__()")

            pass

            LogTr("Exit cPl.__init__()")

        def AssemPlRteActReq(self, SrcAdr, ActTyp, Rsv, OemSpec = None):
            LogTr("Enter cPl.AssemPlRteActReq()")

            #External test equipment address information.
            #Mandatory.
            LogDbg("SrcAdr = 0x%04X" % SrcAdr)
            LogDbg("ActTyp = 0x%02X" % ActTyp)
            LogDbg("Rsv = 0x%08X" % Rsv)

            #Reserved and OEM specific data.
            #Optional.
            LogDbg("OemSpec = " + "" if OemSpec == None else "%08X" % OemSpec)

            Pl = "%04X" % SrcAdr +\
                  "%02X" % ActTyp +\
                  "%08X" % Rsv +\
                  "" if OemSpec == None else "%08X" % OemSpec
            LogDbg(f"Pl = {Pl}")

            LogTr("Exit cPl.AssemPlRteActReq()")

            return Pl

        def AssemPlRteActResp(self, TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec = None):
            LogTr("Enter cPl.AssemPlRteActResp()")

            #External test equipment address information.
            #Mandatory.
            LogDbg("TstrLgAdr = 0x%04X" % TstrLgAdr)

            #Routing activation status information.
            #Mandatory.
            LogDbg("EntyLgAdr = 0x%04X" % EntyLgAdr)
            LogDbg("RteActRespCode = 0x%02X" % RteActRespCode)
            LogDbg("Rsv = 0x%08X" % Rsv)

            #Optional.
            LogDbg("OemSpec = " + "" if OemSpec == None else "%08X" % OemSpec)

            Pl = "%04X" % TstrLgAdr +\
                 "%04X" % EntyLgAdr +\
                 "%02X" % RteActRespCode +\
                 "%08X" % Rsv +\
                  "" if OemSpec == None else "%08X" % OemSpec
            LogTr(f"Pl = {Pl}")

            LogTr("Exit cPl.AssemPlRteActResp()")

            return Pl

        def PrsPlRteActReq(self, Pl):
            LogTr("Enter cPl.PrsPlRteActReq()")

            LogDbg(f"Pl = {Pl}")

            #External test equipment address information.
            #Mandatory.
            SrcAdr = int(Pl[0:4], 16)
            LogDbg("SrcAdr = 0x%04X" % SrcAdr)
            ActTyp = int(Pl[4:6], 16)
            LogDbg("ActTyp = 0x%02X" % ActTyp)
            Rsv = int(Pl[6:14], 16)
            LogDbg("Rsv = 0x%08X" % Rsv)

            #Reserved and OEM specific data.
            #Optional.
            OemSpec = None if Pl[14:22] == "" else "%08X" % int(Pl[14:22], 16)
            LogDbg("OemSpec = " + "" if OemSpec == None else "%08X" % OemSpec)

            LogTr("Exit cPl.PrsPlRteActReq()")

            return SrcAdr, ActTyp, Rsv, OemSpec

        def PrsPlRteActResp(self, Pl):
            LogTr("Enter cPl.PrsPlRteActResp()")

            LogDbg(f"Pl = {Pl}")

            #External test equipment address information.
            #Mandatory.
            TstrLgAdr = int(Pl[0:4], 16)
            LogDbg("TstrLgAdr = 0x%04X" % TstrLgAdr)

            #Routing activation status information.
            #Mandatory.
            EntyLgAdr = int(Pl[4:8], 16)
            LogDbg("EntyLgAdr = 0x%04X" % EntyLgAdr)
            RteActRespCode = int(Pl[8:10], 16)
            LogDbg("RteActRespCode = 0x%02X" % RteActRespCode)
            Rsv = int(Pl[10:18], 16)
            LogDbg("Rsv = 0x%08X" % Rsv)

            #Optional.
            OemSpec = None if Pl[18:26] == "" else "%08X" % int(Pl[18:26], 16)
            LogDbg("OemSpec = " + "" if OemSpec == None else "%08X" % OemSpec)

            LogTr("Exit cPl.PrsPlRteActResp()")

            return TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec

        def AssemPlDiag(self, SrcAdr, TgtAdr, UsrDat):
            LogTr("Enter cPl.AssemPlDiag()")

            #Logical address information.
            #Mandatory.
            LogDbg("SrcAdr = 0x%04X" % SrcAdr)
            LogDbg("TgtAdr = 0x%04X" % TgtAdr)

            #Diagnostic message data.
            #Mandatory.
            LogDbg("UsrDat = {UsrDat}")

            Pl = "%04X" % SrcAdr +\
                 "%04X" % TgtAdr +\
                 UsrDat
            LogDbg("Pl = {Pl}")

            LogTr("Exit cPl.AssemPlDiag()")

            return Pl

        def PrsPlDiag(self, Pl):
            LogTr("Enter cPl.PrsPlDiag()")

            #Logical address information.
            #Mandatory.
            SrcAdr = int(Pl[0:4], 16)
            LogDbg("SrcAdr = 0x%04X" % SrcAdr)
            TgtAdr = int(Pl[4:8], 16)
            LogDbg("TgtAdr = 0x%04X" % TgtAdr)

            #Diagnostic message acknowledge information.
            #Mandatory.
            AckCode = int(Pl[8:10], 16)
            LogDbg("AckCode = 0x%02X" % AckCode)

            #Optional.
            DiagMsg = None if Pl[10:] == "" else Pl[10:]
            LogDbg(f"DiagMsg = {DiagMsg}")

            LogTr("Exit cPl.PrsPlDiag()")

            return SrcAdr, TgtAdr, AckCode, DiagMsg

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

        Hdr = Msg[0:16]
        LogDbg(f"Hdr = {Hdr}")
        Pl = Msg[16:]
        LogDbg(f"Pl = {Pl}")

        LogTr("Exit cMsg.PrsMsg()")

        return Hdr, Pl

class cDoipSer:
    def __init__(self, SrcIpAdr = "127.0.0.1", SrcPt = 13400, SrcAdr = 0xE000,
                 TstrLgAdr = 0xE400, EntyLgAdr = 0x1005):
        LogTr("Enter cDoipSer.__init__()")

        self.SrcIpAdr = SrcIpAdr
        LogDbg(f"self.SrcIpAdr = {self.SrcIpAdr}")
        self.SrcPt = SrcPt
        LogDbg(f"self.SrcPt = {self.SrcPt}")
        self.SrcAdr = SrcAdr
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.TgtAdr = 0x0E00
        LogDbg("self.TgtAdr = 0x%04X" % self.TgtAdr)
        self.TstrLgAdr = TstrLgAdr
        LogDbg("self.TstrLgAdr = 0x%04X" % self.TstrLgAdr)
        self.EntyLgAdr = EntyLgAdr
        LogDbg("self.EntyLgAdr = 0x%04X" % self.EntyLgAdr)
        self.ConnSta = False #Connect status. True: connected, False: not connected.
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

    def IsRecvBufNone(self):
        #LogTr("Enter cDoipSer.IsRecvBufNone()")

        if self.ConnSta == True:
            RecvBufSta = self.TcpSer.IsRecvBufNone()
        else:
            RecvBufSta = None
            LogErr("Socket not connected.")

        #LogTr("Exit cDoipSer.IsRecvBufNone()")

        return RecvBufSta

    def RespRteAct(self):
        LogTr("Enter cDoipSer.RespRteAct()")

        Pl = self.Msg.Pl.AssemPlRteActResp(self.TstrLgAdr,
                                           self.EntyLgAdr,
                                           self.MsgPset.Pl.RteActResp.RteActRespCode.RteScsAct,
                                           self.MsgPset.Pl.RteActResp.Rsv.Dflt)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.RteActResp,
                                    len(Pl) // 2)
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.RespRteAct()")

    def RespDiag(self, UsrDat):
        LogTr("Enter cDoipSer.RespDiag()")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, UsrDat)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsg,
                                    len(Pl) // 2)
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.RespDiag()")

class cDoipClt:
    def __init__(self, SrcIpAdr = "127.0.0.1", TgtIpAdr = "127.0.0.1", SrcPt = 9999, TgtPt = 13400, SrcAdr = 0x0E00, TgtAdr = 0xE000):
        LogTr("Enter cDoipClt.__init__()")

        self.SrcIpAdr = SrcIpAdr
        LogDbg(f"self.SrcIpAdr = {self.SrcIpAdr}")
        self.TgtIpAdr = TgtIpAdr
        LogDbg(f"self.TgtIpAdr = {self.TgtIpAdr}")
        self.SrcPt = SrcPt
        LogDbg(f"self.SrcPt = {self.SrcPt}")
        self.TgtPt = TgtPt
        LogDbg(f"self.TgtPt = {self.TgtPt}")
        self.SrcAdr = SrcAdr
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.TgtAdr = TgtAdr
        LogDbg("self.TgtAdr = 0x%04X" % self.TgtAdr)
        self.ConnSta = False #Connect status. True: connected, False: not connected.
        LogDbg(f"self.ConnSta = {self.ConnSta}")
        self.Msg = cMsg()
        self.MsgPset = cMsgPset()
        self.TcpClt = tcp.cTcpClt(SrcIpAdr, TgtIpAdr, SrcPt, TgtPt)

        LogTr("Exit cDoipClt.__init__()")

    def Conn(self):
        LogTr("Enter cDoipClt.Conn()")

        if self.ConnSta == False:
            self.TcpClt.Conn()
            self.ConnSta = True
        else:
            LogWrn("Connected doip entity!")

        LogTr("Exit cDoipClt.Conn()")

    def DisConn(self):
        LogTr("Enter cDoipClt.DisConn()")

        if self.ConnSta == True:
            self.TcpClt.DisConn()
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cDoipClt.DisConn()")

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
                                    len(Pl) // 2)
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
        LogDbg("ProtoVer = 0x%02X" % ProtoVer)
        LogDbg("InvProtoVer = 0x%02X" % InvProtoVer)
        LogDbg("PlTyp = 0x%04X" % PlTyp)
        LogDbg(f"PlLen = {PlLen}")
        TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec = self.Msg.Pl.PrsPlRteActResp(Pl)
        LogDbg("TstrLgAdr = 0x%04X" % TstrLgAdr)
        LogDbg("EntyLgAdr = 0x%04X" % EntyLgAdr)
        LogDbg("RteActRespCode = 0x%02X" % RteActRespCode)
        LogDbg("Rsv = 0x%08X" % Rsv)

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
                                    len(Pl) // 2)
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
        LogDbg("ProtoVer = 0x%02X" % ProtoVer)
        LogDbg("InvProtoVer = 0x%02X" % InvProtoVer)
        LogDbg("PlTyp = 0x%04X" % PlTyp)
        LogDbg(f"PlLen = {PlLen}")
        SrcAdr, TgtAdr, AckCode, DiagMsg = self.Msg.Pl.PrsPlDiag(Pl)
        LogDbg("SrcAdr = 0x%04X" % SrcAdr)
        LogDbg("TgtAdr = 0x%04X" % TgtAdr)
        LogDbg("AckCode = 0x%02X" % AckCode)
        LogDbg("DiagMsg = " + "" if DiagMsg == None else "%0X" % DiagMsg)

        if PlTyp == self.MsgPset.Hdr.PlTyp.DiagMsgPosAck:
            LogTr("Diagnostic normal response.")
        else:
            LogTr("Abnormal response of diagnosis.")

        LogTr("Exit cDoipClt.RespDiag()")

        return PlTyp, AckCode

    def IsRecvBufNone(self):
        #LogTr("Enter cDoipClt.IsRecvBufNone()")

        if self.ConnSta == True:
            Rtn = self.TcpClt.IsRecvBufNone()
        else:
            Rtn = None
            LogErr("Socket not connected.")

        #LogTr("Exit cDoipClt.IsRecvBufNone()")

        return Rtn

def ImitEcu():
    LogTr("Test tcp server.")

    Ecu = cDoipSer()
    Ecu.Lsn()

    while True:
        if Ecu.IsRecvBufNone() == False:
            RecvMsg = Ecu.Recv()
            LogDbg(f"RecvMsg: {RecvMsg}")

            if RecvMsg != "":
                Hdr, Pl = Ecu.Msg.PrsMsg(RecvMsg)
                LogDbg(f"Hdr = {Hdr}")
                LogDbg(f"Pl = {Pl}")

                ProtoVer, InvProtoVer, PlTyp, PlLen = Ecu.Msg.Hdr.PrsHdr(Hdr)
                LogDbg("ProtoVer = 0x%02X" % ProtoVer)
                LogDbg("InvProtoVer = 0x%02X" % InvProtoVer)
                LogDbg("PlTyp = 0x%04X" % PlTyp)
                LogDbg(f"PlLen = {PlLen}")

                if PlTyp == Ecu.MsgPset.Hdr.PlTyp.RteActReq:
                    LogTr("Routing activation request.")
                    SrcAdr, ActTyp, Rsv, OemSpec = Ecu.Msg.Pl.PrsPlRteActReq(Pl)
                    LogDbg("SrcAdr = 0x%04X" % SrcAdr)
                    LogDbg("ActTyp = 0x%02X" % ActTyp)
                    LogDbg("Rsv = 0x%08X" % Rsv)
                    LogDbg("OemSpec = " + "" if OemSpec == None else "%08X" % OemSpec)
                    Ecu.TgtAdr = SrcAdr
                    LogDbg("Ecu.TgtAdr = 0x%04X" % Ecu.TgtAdr)

                    Ecu.RespRteAct()
                elif PlTyp == Ecu.MsgPset.Hdr.PlTyp.DiagMsg:
                    LogTr("Diagnostic message.")
                    SrcAdr, TgtAdr, AckCode, DiagMsg = Ecu.Msg.Pl.PrsPlDiag(Pl)
                    LogDbg("SrcAdr = 0x%04X" % SrcAdr)
                    LogDbg("TgtAdr = 0x%04X" % TgtAdr)
                    LogDbg("AckCode = 0x%02X" % AckCode)
                    LogDbg(f"DiagMsg = {DiagMsg}")

                    Ecu.RespDiag("AA")

def ImitTstr():
    LogTr("Test tcp client.")

    Tstr = cDoipClt()
    Tstr.Conn()
    Tstr.ReqRteAct()
    Tstr.RespRteAct()
    Tstr.ReqDiag("1003")
    Tstr.RespDiag()

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        ImitEcu()
    elif sys.argv[1] == "-Clt":
        ImitTstr()
