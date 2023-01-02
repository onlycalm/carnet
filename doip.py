import socket
from log import *

class Doip:
    def __init__(self, SrcIpAdr = "127.0.0.1", TgtIpAdr = "127.0.0.1", SrcPt = 9999, TgtPt = 13400, SrcAdr = 0x0E00, TgtAdr = 0xE000):
        LogTr("Enter Doip.__init__()")

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

        LogTr("Exit Doip.__init__()")

    def Conn(self):
        LogTr("Enter Doip.Conn()")

        if self.ConnSta == False:
            LogTr("Connecting to a doip entity.")
            #Tcp socket client.
            self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
            self.Sock.bind((self.SrcIpAdr, self.SrcPt))
            LogScs("Socket binding succeeded.")
            self.Sock.connect((self.TgtIpAdr, self.TgtPt))
            LogScs("Socket connection succeeded.")
            self.ConnSta = True
        else:
            LogWrn("Connected doip entity!")

        LogTr("Exit Doip.Conn()")

    def DisConn(self):
        LogTr("Enter Doip.DisConn()")

        if self.ConnSta == True:
            self.Sock.shutdown(socket.SHUT_RDWR)
            self.Sock.close()
            self.Sk = None
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit Doip.DisConn()")

    def Snd(self, Msg):
        LogTr("Enter Doip.Snd()")

        if self.ConnSta == True:
            self.Sock.send(bytes.fromhex(Msg))
            LogInf("Doip send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit Doip.Snd()")

    def Recv(self):
        LogTr("Enter Doip.Recv()")

        if self.ConnSta == True:
            Msg = self.Sock.recv(1024).hex().upper()
            print(Msg)
            #LogInf("Doip recv: " + Msg)
        else:
            LogErr("Socket not connected, receiving failed.")

        LogTr("Exit Doip.Recv()")

        return Msg

    def ReqRteAct(self):
        LogTr("Enter Doip.ReqRteAct()")

        PlMsg = self.Msg.AssemPlMsgRteActReq(self.SrcAdr, 0x00000000)
        LogDbg(f"PlMsg = {PlMsg}")
        SndMsg = self.Msg.AssemMsg(self.Msg.MsgPset.ProtoVer["2012"], self.Msg.MsgPset.PlTyp["RteActReq"], PlMsg)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit Doip.ReqRteAct()")

    def RespRteAct(self):
        LogTr("Enter Doip.RespRteAct()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        self.Msg.DisassyMsg(RecvMsg)
        self.Msg.DisassyPlMsgRteActResp(self.Msg.PlMsg)

        if self.RteActRespCode == self.Msg.MsgPset.RteActRespCode["RteScsAct"]:
            LogTr("Route activation succeeded.")
            self.TstrLgAdr = self.Msg.TstrLgAdr
            LogDbg(f"self.TstrLgAdr = {self.TstrLgAdr}")
            self.DoipEntyLgAdr = self.Msg.DoipEntyLgAdr
            LogDbg(f"self.DoipEntyLgAdr = {self.DoipEntyLgAdr}")
        else:
            LogTr("Route activation failed.")

        LogTr("Exit Doip.RespRteAct()")

    def ReqDiag(self, UsrDat):
        LogTr("Enter Doip.ReqDiag()")

        PlMsg = self.Msg.AssemPlMsgDiag(self.SrcAdr, self.TgtAdr, UsrDat)
        LogDbg(f"PlMsg = {PlMsg}")
        SndMsg = self.Msg.AssemMsg(self.Msg.MsgPset.ProtoVer["2012"], self.Msg.MsgPset.PlTyp["DiagMsg"], PlMsg)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit Doip.ReqDiag()")

    def RespDiag(self):
        LogTr("Enter Doip.RespDiag()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        self.Msg.DisassyMsg(RecvMsg)
        self.Msg.DisassyPlMsgDiag(self.Msg.PlMsg)

        if self.PlTyp == self.Msg.MsgPset.PlTyp["DiagMsgPosAck"]:
            LogTr("Diagnostic normal response.")
        else:
            LogTr("Abnormal response of diagnosis.")

        LogTr("Exit Doip.RespDiag()")

class MsgPset:
    def __init__(self):
        LogTr("Enter MsgPset.__init__()")

        #ISO 13400-2-2012.
        #Doip message structure.
        #Protocol version.
        #Pos = 0, Len = 1.
        self.ProtoVer = {
            "2010" : 0x01, #0x01: DoIP ISO/DIS 13400-2:2010.
            "2012" : 0x02, #0x02: DoIP ISO 13400-2:2012.
            "Vin"  : 0xFF  #0xFF: default value for vehicle identification request message.
        }
        LogDbg(f"self.ProtoVer = {self.ProtoVer}")

        #Inverse protocol version.
        #Pos = 1, Len = 1.

        #Payload type(GH_PT).
        #Pos = 2, Len = 2.
        self.PlTyp = {
            "GenDoipHdrNegAck"   : 0x0000, #Generic DoIP header negative acknowledge.
            "VehIdReqMsg"        : 0x0001, #Vehicle identification request message.
            "VehIdReqMsgWithVin" : 0x0003, #Vehicle identification request message with VIN.
            "VehAnncMsg"         : 0x0004, #Vehicle announcement message/vehicle identification response message.
            "RteActReq"          : 0x0005, #Routing activation request.
            "RteActResp"         : 0x0006, #Routing activation response.
            "AlvChkReq"          : 0x0007, #Alive check request.
            "AlvChkResp"         : 0x0008, #Alive check response.
            "DoipEntyStsReq"     : 0x4001, #DoIP entity status request.
            "DoipEntyStsResp"    : 0x4002, #DoIP entity status response.
            "DiagPwrMdInfoReq"   : 0x4003, #Diagnostic power mode information response.
            "DiagPwrMdInfoResp"  : 0x4004, #Diagnostic power mode information request.
            "DiagMsg"            : 0x8001, #Diagnostic message.
            "DiagMsgPosAck"      : 0x8002, #Diagnostic message positive acknowledegment.
            "DiagMsgNegAck"      : 0x8003  #Diagnostic message negative acknowledgement.
        }
        LogDbg(f"self.PlTyp = {self.PlTyp}")

        #Payload length(GH_PT).
        #Pos = 4, Len = 4.
        #PlLen

        #Payload type specific message content.
        #Pos = 8, Len = ....
        #PlMsg

        #Payload type routing activation request.
        #Routine activation request activation types.
        self.ActTyp = {
            "Dflt"     : 0x00, #Default.
            "WwhObd"   : 0x01, #WWH-OBD.
            "CntrlSec" : 0xE0  #Central security.
        }
        LogDbg(f"self.ActTyp = {self.ActTyp}")

        #Routine activation response code value.
        self.RteActRespCode = {
            "UnKSrcAdr"       : 0x00, #Routine activation denied due to unknown source address.
            "SockRegAct"      : 0x01, #Routine activation denied bacause all concurrently
                                      #supported TCP_DATA socket are registered and active.
            "SaDiffAlrAct"    : 0x02, #Routine activation denied because an SA different from the
                                      #table connection entry was received on the already
                                      #activated TCP_DATA socket.
            "SaAlrRegActDiff" : 0x03, #Routine activation denied because the SA is already
                                      #registered and active on a different TCP_DATA socket.
            "MisAuthn"        : 0x04, #Routine activation denied due to missing authentication.
            "RejConf"         : 0x05, #Routine activation denied due to rejected confirmation.
            "UnsptRteAct"     : 0x06, #Routine activation denied due to unsupported routing activation type.
            "RteScsAct"       : 0x10, #Routing successfuly activated.
            "RteWilAct"       : 0x11  #Routing will be activated; confirmation required.
        }
        LogDbg(f"self.RteActRespCode = {self.RteActRespCode}")

        #Diagnostic message positive acknowledge codes.
        self.PosAckCode = {
            "RteCor" : 0x00 #Routing confirmation acknowledge (ACK) message indicating that
                            #the diagnostic message was correctly received, processed and put
                            #into the transmission buffer of the destination network.
        }

        #Diagnostic message negative acknowledge codes.
        self.NegAckCode = {
            "InvSrcAdr"     : 0x02, #Invalid source address.
            "UnkTgtAdr"     : 0x03, #Unknown target address.
            "DiagMsgLrg"    : 0x04, #Diagnostic message too large.
            "OtMem"         : 0x05, #Out of memory.
            "TgtUnreach"    : 0x06, #Target unreachable.
            "UnkNet"        : 0x07, #Unknown network.
            "TransProtoErr" : 0x08, #Transport protocol error.
        }

        LogTr("Exit MsgPset.__init__()")

class Msg:
    def __init__(self):
        LogTr("Enter Msg.__init__()")

        self.MsgPset = MsgPset()
        self.ProtoVer = self.MsgPset.ProtoVer["Vin"]
        LogDbg("self.ProtoVer = 0x%02X" % self.ProtoVer)
        self.InvProtoVer = (~self.ProtoVer & 0xFF)
        LogDbg("self.InvProtoVer = 0x%02X" % self.InvProtoVer)
        self.PlTyp = self.MsgPset.PlTyp["GenDoipHdrNegAck"]
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

    def AssemPlMsgRteActReq(self, SrcAdr, OemSpec):
        LogTr("Enter Msg.AssemPlMsgRteActReq()")

        self.SrcAdr = SrcAdr
        LogDbg("self.SrcAdr = 0x%04X" % self.SrcAdr)
        self.OemSpec = OemSpec
        LogDbg("self.OemSpec = 0x%08X" % self.OemSpec)

        PlMsg = "%04X" % self.SrcAdr +\
                "%02X" % self.MsgPset.ActTyp["Dflt"] +\
                "%08X" % (0x00000000) +\
                "%08X" % self.OemSpec
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
        #Rsv = PlMsg[10:18]
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
