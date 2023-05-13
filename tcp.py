##
# @file tcp.py
# @brief Tcp.
# @details None.
# @author Calm
# @date 2023-05-13
# @version v1.0.0
# @copyright Calm
#

import sys
import socket
from log import *

class cTcpSer:
    def __init__(self, LocIpAdr = "127.0.0.1", LocPt = 9999):
        LogTr("Enter cTcpSer.__init__()")

        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #allows different sockets to reuse ipaddress.
        LogDbg(f"self.Sock = {self.Sock}")
        self.LocIpAdr = LocIpAdr
        LogDbg(f"self.LocIpAdr = {self.LocIpAdr}")
        self.RmtIpAdr = None
        LogDbg(f"self.RmtIpAdr = {self.RmtIpAdr}")
        self.LocPt = LocPt
        LogDbg(f"self.LocPt = {self.LocPt}")
        self.RmtPt = None
        LogDbg(f"self.RmtPt = {self.RmtPt}")
        self.ConnSta = False
        LogDbg(f"self.ConnSta = {self.ConnSta}")
        self.ConnHdl = None
        LogDbg(f"self.ConnHdl = {self.ConnHdl}")

        self.Sock.settimeout(10) #Tcp timeout is 10s.
        self.Sock.setblocking(True) #True: Blocking, False: Non-blocking.

        LogTr("Exit cTcpSer.__init__()")

    def Lsn(self):
        LogTr("Enter cTcpSer.Lsn()")

        self.Sock.bind((self.LocIpAdr, self.LocPt))
        LogTr("Listening.")
        self.Sock.listen(1) #Maximum connections.
        self.ConnHdl, (self.RmtIpAdr, self.RmtPt) = self.Sock.accept()
        LogDbg(f"self.RmtIpAdr = {self.RmtIpAdr}")
        LogDbg(f"self.RmtPt = {self.RmtPt}")
        LogTr("Accepted socket.")
        self.ConnSta = True

        LogTr("Exit cTcpSer.Lsn()")

    def DisConn(self):
        LogTr("Enter cTcpSer.DisConn()")

        if self.ConnSta == True:
            self.Sock.shutdown(socket.SHUT_RDWR)
            self.Sock.close()
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cTcpSer.DisConn()")

    def Snd(self, Msg):
        LogTr("Enter cTcpSer.Snd()")

        if self.ConnSta == True:
            self.ConnHdl.send(bytes.fromhex(Msg))
            LogInf("Tcp send: " + Msg)
        else:
            LogErr("Socket not connected.")

        LogTr("Exit cTcpSer.Snd()")

    def Recv(self):
        LogTr("Enter cTcpSer.Recv()")

        if self.ConnSta == True:
            Msg = self.ConnHdl.recv(1024).hex().upper()
            LogInf("Tcp recv: " + Msg)
        else:
            Msg = ""
            LogErr("Socket not connected.")

        LogTr("Exit cTcpSer.Recv()")

        return Msg

    def IsRecvBufMty(self):
        #LogTr("Enter cTcpSer.IsRecvBufMty()")

        if self.ConnSta == True:
            if self.ConnHdl.recv(1024, socket.MSG_PEEK) == b'':
                Rtn = True
            else:
                LogTr("Receive cache is not empty.")
                Rtn = False
        else:
            Rtn = None
            LogErr("Socket not connected.")

        #LogTr("Exit cTcpSer.IsRecvBufMty()")

        return Rtn

class cTcpClt:
    def __init__(self, LocIpAdr = "127.0.0.1", RmtIpAdr = "127.0.0.1", LocPt = 9998, RmtPt = 9999):
        LogTr("Enter cTcpClt.__init__()")

        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #allows different sockets to reuse ipaddress.
        LogDbg(f"self.Sock = {self.Sock}")
        self.LocIpAdr = LocIpAdr
        LogDbg(f"self.LocIpAdr = {self.LocIpAdr}")
        self.RmtIpAdr = RmtIpAdr
        LogDbg(f"self.RmtIpAdr = {self.RmtIpAdr}")
        self.LocPt = LocPt
        LogDbg(f"self.LocPt = {self.LocPt}")
        self.RmtPt = RmtPt
        LogDbg(f"self.RmtPt = {self.RmtPt}")
        self.ConnSta = False
        LogDbg(f"self.ConnSta = {self.ConnSta}")

        self.Sock.settimeout(10) #Tcp timeout is 10s.
        self.Sock.setblocking(True) #True: Blocking, False: Non-blocking.

        LogTr("Exit cTcpClt.__init__()")

    def Conn(self):
        LogTr("Enter cTcpClt.Conn()")

        ConnRst = False

        if self.ConnSta == False:
            try:
                self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
                self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allows different sockets to reuse ipaddress.
                self.Sock.bind((self.LocIpAdr, self.LocPt))
            except:
                LogErr("Socket bind failed.")
            else:
                LogScs("Socket binding succeeded.")

                try:
                    self.Sock.connect((self.RmtIpAdr, self.RmtPt))
                except:
                    LogErr("Socket connect failed.")
                else:
                    LogScs("Socket connection succeeded.")
                    self.ConnSta = True
                    ConnRst = True
        else:
            LogErr("Connected tcp socket.")

        LogTr("Exit cTcpClt.Conn()")

        return ConnRst

    def DisConn(self):
        LogTr("Enter cTcpClt.DisConn()")

        DisConnRst = False

        if self.ConnSta == True:
            try:
                self.Sock.shutdown(socket.SHUT_RDWR)
            except:
                LogErr("Socket shutdown failed.")
            else:
                LogScs("Socket shutdown succeeded.")

                try:
                    self.Sock.close()
                except:
                    LogErr("Socket close failed.")
                else:
                    LogScs("Socket close succeeded.")
                    self.ConnSta = False
                    DisConnRst = True
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cTcpClt.DisConn()")

        return DisConnRst

    def Snd(self, Msg):
        LogTr("Enter cTcpClt.Snd()")

        if self.ConnSta == True:
            self.Sock.send(bytes.fromhex(Msg))
            LogInf("Tcp send: " + Msg)
        else:
            LogErr("Socket not connected.")

        LogTr("Exit cTcpClt.Snd()")

    def Recv(self):
        LogTr("Enter cTcpClt.Recv()")

        if self.ConnSta == True:
            Msg = self.Sock.recv(1024).hex().upper()
            LogInf("Tcp recv: " + Msg)
        else:
            Msg = ""
            LogErr("Socket not connected.")

        LogTr("Exit cTcpClt.Recv()")

        return Msg

    def IsRecvBufMty(self):
        #LogTr("Enter cTcpClt.IsRecvBufMty()")

        if self.ConnSta == True:
            if self.Sock.recv(1024, socket.MSG_PEEK) == "":
                Rtn = True
            else:
                LogTr("Receive cache is not empty.")
                Rtn = False
        else:
            Rtn = None
            LogErr("Socket not connected.")

        #LogTr("Exit cTcpClt.IsRecvBufMty()")

        return Rtn

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        LogTr("Test tcp server.")

        TcpSer = cTcpSer()
        TcpSer.Lsn()

        while True:
            if TcpSer.IsRecvBufMty() == False:
                Msg = TcpSer.Recv()
                LogDbg(f"Recv: {Msg}")
                TcpSer.Snd("BB")

        TcpSer.DisConn()
    elif sys.argv[1] == "-Clt":
        LogTr("Test tcp client.")

        TcpClt = cTcpClt()
        TcpClt.Conn()
        TcpClt.Snd("AA")

        while True:
            if TcpClt.IsRecvBufMty() == False:
                Msg = TcpClt.Recv()
                LogDbg(f"Recv: {Msg}")
                TcpClt.Snd("AA")

        TcpClt.DisConn()
