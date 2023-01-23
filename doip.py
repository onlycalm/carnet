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

            def __init__(self):
                LogTr("Enter cRteActReq.__init__()")

                self.ActTyp = self.cActTyp()

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

            def __init__(self):
                LogTr("Enter cRteActResp.__init__()")

                self.RteActRespCode = self.cRteActRespCode()

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

class cPlRteActReq:
    def __init__(self):
        LogTr("Enter cPlRteActReq.__init__()")

        #Mandatory.
        self.SrcAdr = 0
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.ActTyp = 0
        LogDbg("self.ActTyp = 0x%02X" % self.ActTyp)
        self.IsoRsv = 0
        LogDbg("self.IsoRsv = 0x%08X" % self.IsoRsv)

        #Optional.
        self.OemRsv = 0
        LogDbg("self.OemRsv = 0x%08X" % self.OemRsv)

        LogTr("Exit cPlRteActReq.__init__()")

class cPlRteActResp:
    def __init__(self):
        LogTr("Enter cPlRteActResp.__init__()")

        #Mandatory.
        self.TstrLgAdr = 0
        LogDbg("self.TstrLgAdr = 0x%04X" % self.TstrLgAdr)
        self.DoipEntyLgAdr = 0
        LogDbg("self.DoipEntyLgAdr = 0x%04X" % self.DoipEntyLgAdr)
        self.RteActRespCode = 0
        LogDbg("self.RteActRespCode = 0x%02X" % self.RteActRespCode)
        self.IsoRsv = 0
        LogDbg("self.IsoRsv = 0x%08X" % self.IsoRsv)

        #Optional.
        self.OemRsv = None
        LogDbg(f"self.OemRsv = {self.OemRsv}")

        LogTr("Exit cPlRteActResp.__init__()")

class cPlDiag:
    def __init__(self):
        LogTr("Enter cPlDiag.__init__()")

        #Mandatory.
        self.SrcAdr = 0
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.TgtAdr = 0
        LogDbg("self.TgtAdr = 0x%04X" % self.TgtAdr)
        self.UsrDat = 0
        LogDbg(f"self.UsrDat = {self.UsrDat}")

        LogTr("Exit cPlDiag.__init__()")

class cPlDiagPosAck:
    def __init__(self):
        LogTr("Enter cPlDiagPosAck.__init__()")

        #Mandatory.
        self.SrcAdr = 0
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.TgtAdr = 0
        LogDbg("self.TgtAdr = 0x%04X" % self.TgtAdr)
        self.AckCode = 0
        LogDbg("self.AckCode = 0x%02X" % self.AckCode)

        #Optional.
        self.PreDiagMsg = None
        LogDbg(f"self.PreDiagMsg = {self.PreDiagMsg}")

        LogTr("Exit cPlDiagPosAck.__init__()")

class cMsg:
    #ISO 13400-2-2012.
    #Doip message structure.

    class cHdr:
        def __inti__(self, ProtoVer = 0x00, PlTyp = 0x00, PlLen = 0):
            LogTr("Enter cHdr.__init__()")

            self.ProtoVer = ProtoVer
            LogDbg("self.ProtoVer = 0x%02X" % self.ProtoVer)
            self.InvProtoVer = (~self.ProtoVer & 0xFF)
            LogDbg("self.InvProtoVer = 0x%02X" % self.InvProtoVer)
            self.PlTyp = PlTyp
            LogDbg("self.PlTyp = 0x%04X" % self.PlTyp)
            self.PlLen = PlLen
            LogDbg(f"self.PlLen = {self.PlLen}")

            LogTr("Exit cHdr.__init__()")

    def __init__(self, ProtoVer = 0x00, PlTyp = 0x00, PlLen = 0, Pl = ""):
        LogTr("Enter cMsg.__init__()")

        self.Hdr = self.cHdr(ProtoVer, PlTyp, PlLen)
        LogDbg(f"self.Hdr = {self.Hdr}")
        self.Pl = Pl
        LogDbg(f"self.Pl = {self.Pl}")

        LogTr("Exit cMsg.__init__()")

class cDoip:
    def __init__(self, SrcIpAdr = "127.0.0.1", TgtIpAdr = "127.0.0.1", SrcPt = 9999, TgtPt = 13400, SrcAdr = 0x0E00, TgtAdr = 0xE000):
        LogTr("Enter cDoip.__init__()")

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
        self.Msg = Msg()
        self.MsgPset = cMsgPset()
        self.TcpClt = tcp.cTcpClt()

        LogTr("Exit cDoip.__init__()")

    def Conn(self):
        LogTr("Enter cDoip.Conn()")

        if self.ConnSta == False:
            self.TcpClt.Conn()
            self.ConnSta = True
        else:
            LogWrn("Connected doip entity!")

        LogTr("Exit cDoip.Conn()")

    def DisConn(self):
        LogTr("Enter cDoip.DisConn()")

        if self.ConnSta == True:
            self.TcpClt.DisConn()
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cDoip.DisConn()")

    def Snd(self, Msg):
        LogTr("Enter cDoip.Snd()")

        if self.ConnSta == True:
            self.TcpClt.Snd(bytes.fromhex(Msg))
            LogInf("Doip send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cDoip.Snd()")

    def Recv(self):
        LogTr("Enter cDoip.Recv()")

        if self.ConnSta == True:
            Msg = self.TcpClt.Recv()
            LogInf("Doip recv: " + Msg)
        else:
            LogErr("Socket not connected, receiving failed.")

        LogTr("Exit cDoip.Recv()")

        return Msg

    def ReqRteAct(self):
        LogTr("Enter cDoip.ReqRteAct()")

        PlMsg = self.Msg.AssemPlMsgRteActReq(self.SrcAdr)
        LogDbg(f"PlMsg = {PlMsg}")
        SndMsg = self.Msg.AssemMsg(self.MsgPset.Hdr.ProtoVer.v2012, self.MsgPset.Hdr.PlTyp.RteActReq, PlMsg)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoip.ReqRteAct()")

    def RespRteAct(self):
        LogTr("Enter cDoip.RespRteAct()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        self.Msg.DisassyMsg(RecvMsg)
        self.Msg.DisassyPlMsgRteActResp(self.Msg.PlMsg)

        if self.RteActRespCode == self.MsgPset.Pl.RteActResp.RteActRespCode.RteScsAct:
            LogTr("Route activation succeeded.")
            self.TstrLgAdr = self.Msg.TstrLgAdr
            LogDbg(f"self.TstrLgAdr = {self.TstrLgAdr}")
            self.DoipEntyLgAdr = self.Msg.DoipEntyLgAdr
            LogDbg(f"self.DoipEntyLgAdr = {self.DoipEntyLgAdr}")
        else:
            LogTr("Route activation failed.")

        LogTr("Exit cDoip.RespRteAct()")

    def ReqDiag(self, UsrDat):
        LogTr("Enter cDoip.ReqDiag()")

        PlMsg = self.Msg.AssemPlMsgDiag(self.SrcAdr, self.TgtAdr, UsrDat)
        LogDbg(f"PlMsg = {PlMsg}")
        SndMsg = self.Msg.AssemMsg(self.MsgPset.Hdr.ProtoVer.v2012, self.MsgPset.Hdr.PlTyp.DiagMsg, PlMsg)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoip.ReqDiag()")

    def RespDiag(self):
        LogTr("Enter cDoip.RespDiag()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        self.Msg.DisassyMsg(RecvMsg)
        self.Msg.DisassyPlMsgDiag(self.Msg.PlMsg)

        if self.PlTyp == self.MsgPset.Hdr.PlTyp.DiagMsgPosAck:
            LogTr("Diagnostic normal response.")
        else:
            LogTr("Abnormal response of diagnosis.")

        LogTr("Exit cDoip.RespDiag()")

class Msg:
    def __init__(self):
        LogTr("Enter Msg.__init__()")

        self.MsgPset = cMsgPset()
        self.ProtoVer = self.MsgPset.Hdr.ProtoVer.Vin
        LogDbg("self.ProtoVer = 0x%02X" % self.ProtoVer)
        self.InvProtoVer = (~self.ProtoVer & 0xFF)
        LogDbg("self.InvProtoVer = 0x%02X" % self.InvProtoVer)
        self.PlTyp = self.MsgPset.Hdr.PlTyp.GenDoipHdrNegAck
        LogDbg("self.PlTyp = 0x%04X" % self.PlTyp)
        self.PlLen = 0
        LogDbg(f"self.PlLen = {self.PlLen}")
        self.PlMsg = ""
        LogDbg(f"self.PlMsg = {self.PlMsg}")

        self.Msg = ""
        LogDbg(f"self.Msg = {self.Msg}")

        LogTr("Exit Msg.__init__()")

    def AssemMsg(self, ProtoVer, PlTyp, PlMsg):
        LogTr("Enter Msg.AssemMsg()")

        self.ProtoVer = ProtoVer
        LogDbg("self.ProtoVer = 0x%02X" % self.ProtoVer)
        self.InvProtoVer = (~self.ProtoVer & 0xFF)
        LogDbg("self.InvProtoVer = 0x%02X" % self.InvProtoVer)
        self.PlTyp = PlTyp
        LogDbg("self.PlTyp = 0x%04X" % self.PlTyp)
        self.PlLen = int(len(PlMsg) / 2)
        LogDbg(f"self.PlLen = {self.PlLen}")
        self.PlMsg = PlMsg
        LogDbg(f"self.PlMsg = {self.PlMsg}")

        self.Msg = "%02X" % self.ProtoVer +\
                   "%02X" % self.InvProtoVer +\
                   "%04X" % self.PlTyp +\
                   "%08X" % self.PlLen +\
                   self.PlMsg
        LogDbg(f"Msg = {Msg}")

        LogTr("Exit Msg.AssemMsg()")

        return self.Msg

    def DisassyMsg(self, Msg):
        LogTr("Enter Msg.DisassyMsg()")

        self.ProtoVer = int(Msg[0:2], 16)
        LogDbg("self.ProtoVer = 0x%02X" % self.ProtoVer)
        self.InvProtoVer = int(Msg[2:4], 16)
        LogDbg("self.InvProtoVer = 0x%02X" % self.InvProtoVer)
        self.PlTyp = int(Msg[4:8], 16)
        LogDbg("self.PlTyp = 0x%04X" % self.PlTyp)
        self.PlLen = int(Msg[8:16], 16)
        LogDbg(f"self.PlLen = {self.PlLen}")
        self.PlMsg = Msg[16:]
        LogDbg(f"self.PlMsg = {self.PlMsg}")

        LogTr("Exit Msg.DisassyMsg()")

    def AssemPlMsgRteActReq(self, SrcAdr, OemSpec = None):
        LogTr("Enter Msg.AssemPlMsgRteActReq()")

        self.SrcAdr = SrcAdr
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)

        #Optional.
        self.OemSpec = OemSpec

        if self.OemSpec == None:
            LogDbg("self.OemSpec = {self.OemSpec}")
            StrOemSpec = ""
        else:
            LogDbg("self.OemSpec = 0x%08X" % self.OemSpec)
            StrOemSpec = "%08X" % self.OemSpec

        PlMsg = "%04X" % self.SrcAdr +\
                "%02X" % self.MsgPset.Pl.RteActReq.ActTyp.Dflt +\
                "%08X" % (0x00000000) +\
                StrOemSpec
        LogDbg(f"self.PlMsg = {self.PlMsg}")

        LogTr("Exit Msg.AssemPlMsgRteActReq()")

        return PlMsg

    def DisassyPlMsgRteActResp(self, PlMsg):
        LogTr("Enter Msg.DisassyPlMsgRteActResp()")

        self.TstrLgAdr = int(PlMsg[0:4], 16)
        LogDbg("self.TstrLgAdr = 0x%04X" % self.TstrLgAdr)
        self.DoipEntyLgAdr = int(PlMsg[4:8], 16)
        LogDbg("self.DoipEntyLgAdr = 0x%04X" % self.DoipEntyLgAdr)
        self.RteActRespCode = int(PlMsg[8:10], 16)
        LogDbg("self.RteActRespCode = 0x%02X" % self.RteActRespCode)
        #PlMsg[10:18] is reserved.
        self.OemSpec = int(PlMsg[18:26], 16)
        LogDbg("self.OemSpec = 0x%08X" % self.OemSpec)

        LogTr("Exit Msg.DisassyPlMsgRteActResp()")

    def AssemPlMsgDiag(self, SrcAdr, TgtAdr, UsrDat):
        LogTr("Enter Msg.AssemPlMsgDiag()")

        self.SrcAdr = SrcAdr
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.TgtAdr = TgtAdr
        LogDbg("self.TgtAdr = 0x%04X" % self.TgtAdr)
        self.UsrDat = UsrDat
        LogDbg(f"self.UsrDat = {self.UsrDat}")

        PlMsg = "%04X" % self.SrcAdr +\
                "%04X" % self.TgtAdr +\
                self.UsrDat

        LogTr("Exit Msg.AssemPlMsgDiag()")

        return PlMsg

    def DisassyPlMsgDiag(self, PlMsg):
        LogTr("Enter Msg.AssemPlMsgDiag()")

        self.SrcAdr = int(PlMsg[0:4], 16)
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.TgtAdr = int(PlMsg[4:8], 16)
        LogDbg("self.TgtAdr = 0x%04X" % self.TgtAdr)
        self.AckCode = int(PlMsg[8:10], 16)
        LogDbg("self.AckCode = 0x%02X" % self.AckCode)
        self.PreDiagMsg = PlMsg[10:]
        LogDbg(f"self.PreDiagMsg = {self.PreDiagMsg}")

        LogTr("Exit Msg.AssemPlMsgDiag()")

if __name__ == "__main__":
    LogTr("__main__")

    Tstr = cDoip("127.0.0.1", "127.0.0.1", 9998, 13400)
