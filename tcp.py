import sys
import socket
from log import *

class cTcpSer:
    def __init__(self, LocIpAdr = "127.0.0.1", LocPt = 9999):
        LogTr("Enter cTcpSer.__init__()")

        self.Sock = None
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
        self.Conn = None
        LogDbg(f"self.Conn = {self.Conn}")

        LogTr("Exit cTcpSer.__init__()")

    def Lsn(self):
        LogTr("Enter cTcpSer.Lsn()")

        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        self.Sock.bind((self.LocIpAdr, self.LocPt))
        LogTr("Listening.")
        self.Sock.listen(5)
        self.Conn, (self.RmtIpAdr, self.RmtPt) = self.Sock.accept()
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
            self.Conn.send(bytes.fromhex(Msg))
            LogInf("Tcp send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cTcpSer.Snd()")

    def Recv(self):
        #LogTr("Enter cTcpSer.Recv()")

        if self.ConnSta == True:
            Msg = self.Conn.recv(1024).hex().upper()
            #LogInf("Doip recv: " + Msg)
        else:
            LogErr("Socket not connected.")

        #LogTr("Exit cTcpSer.Recv()")

        return Msg

class cTcpClt:
    def __init__(self, LocIpAdr = "127.0.0.1", RmtIpAdr = "127.0.0.1", LocPt = 9998, RmtPt = 9999):
        LogTr("Enter cTcpClt.__init__()")

        self.Sock = None
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
        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        LogScs("Create Socket succeeded.")

        LogTr("Exit cTcpClt.__init__()")

    def Conn(self):
        LogTr("Enter cTcpClt.Conn()")

        if self.ConnSta == False:
            self.Sock.bind((self.LocIpAdr, self.LocPt))
            LogScs("Socket binding succeeded.")
            self.Sock.connect((self.RmtIpAdr, self.RmtPt))
            LogScs("Socket connection succeeded.")
            self.ConnSta = True
        else:
            LogWrn("Connected tcp socket.")

        LogTr("Exit cTcpClt.Conn()")

    def DisConn(self):
        LogTr("Enter cTcpClt.DisConn()")

        if self.ConnSta == True:
            self.Sock.shutdown(socket.SHUT_RDWR)
            self.Sock.close()
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cTcpClt.DisConn()")

    def Snd(self, Msg):
        LogTr("Enter cTcpClt.Snd()")

        if self.ConnSta == True:
            self.Sock.send(bytes.fromhex(Msg))
            LogInf("Tcp send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cTcpClt.Snd()")

    def Recv(self):
        #LogTr("Enter cTcpClt.Recv()")

        if self.ConnSta == True:
            Msg = self.Sock.recv(1024).hex().upper()
            #LogInf("Doip recv: " + Msg)
        else:
            LogErr("Socket not connected, receiving failed.")

        #LogTr("Exit cTcpClt.Recv()")

        return Msg

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Clt":
        LogTr("Test tcp client.")

        TcpClt = cTcpClt()
        TcpClt.Conn()
        TcpClt.Snd("AA")

        for i in range(3):
            Msg = TcpClt.Recv()
            if Msg != "":
                LogDbg(Msg)
                TcpClt.Snd("AA")

        TcpClt.DisConn()
    elif sys.argv[1] == "-Ser":
        LogTr("Test tcp server.")

        TcpSer = cTcpSer()
        TcpSer.Lsn()

        while True:
            Msg = TcpSer.Recv()
            if Msg != "":
                LogDbg(Msg)
                TcpSer.Snd("BB")

        TcpSer.DisConn()
