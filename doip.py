import socket
from log import *

class cDoip:
    def __init__(self, SrcIpAddr = "127.0.0.1", SrcPt = 13400, SrcAddr = 0x0E00, TgtAddr = 0xE000):
        LogTr("Enter cDoip.__init__()")
        self.SrcIpAddr = SrcIpAddr
        LogInf(f"self.SrcIpAddr = {self.SrcIpAddr}")
        self.SrcPt = SrcPt
        LogInf(f"self.SrcPt = {self.SrcPt}")
        self.SrcAddr = SrcAddr
        LogInf("self.SrcAddr = 0x%04X" % self.SrcAddr)
        self.TgtAddr = TgtAddr
        LogInf("self.TgtAddr = 0x%04X" % self.TgtAddr)
        self.ConnSta = False #Connect status. True: connected, False: not connected.
        LogInf(f"self.ConnSta = {self.ConnSta}")

        #Tcp socket client.
        self.Sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        self.Sk.bind((self.SrcIpAddr, self.SrcPt))
        LogTr("Exit cDoip.__init__()")

    def Conn(self)
        LogTr("Enter cDoip.Conn()")
        if self.ConnSta == False:
            LogTr("Connecting to a doip entity.")
            self.Sk =
            self.ConnSta = True
        else:
            LogWrn("Connected doip entity!")
        LogTr("Exit cDoip.Conn()")
