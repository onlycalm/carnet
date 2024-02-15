"""
@file tcp.py
@brief Tcp.
@details None.
@author Calm
@date 2023-05-13
@version v1.0.0
@copyright Calm
"""

import sys
import socket
from log import *

class cTcpSer:
    """
    @class cTcpSer
    @brief Tcp server class.
    @param[in] LocIpAdr Tcp server local ip address.
    - 127.0.0.1 Default value.
    @param[in] Tcp server locPt Local port.
    - 9999 Default value.
    @var self.Sock Tcp server socket object。
    @var self.LocIpAdr Tcp server local ip address.
    @var self.RmtIpAdr Tcp server remote ip address.
    @var self.LocPt Tcp server local port.
    @var self.RmtPt Tcp server remote port.
    @var self.ConnSta Tcp server connect status.
    @var self.ConnHdl Tcp server handle.
    """

    def __init__(self, LocIpAdr = "127.0.0.1", LocPt = 9999):
        """
        @fn __init__
        @brief Constructor for class cTcpSer.
        @details Initialize socket to block communication. TCP timeout of 10 seconds.
        @param[in] LocIpAdr Local ip address.
        - 127.0.0.1 Default value.
        @param[in] LocPt Local port.
        - 9999 Default value.
        @return None
        """

        LogTr("Enter cTcpSer.__init__()")

        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allows different sockets to reuse ipaddress.
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
        """
        @fn Lsn
        @brief Tcp server listening.
        @details The number of connections is 1. After connecting to the TCP client,
                 the TCP server will obtain the remote IP address and port number.
        @param None
        @return None
        """

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
        """
        @fn DisConn
        @brief TCP server disconnected.
        @param None
        @return The execution result of tcp server disconnection.
        @retval True Successfully disconnected tcp connection.
        @retval False Failed to disconnect tcp connection.
        """

        LogTr("Enter cTcpSer.DisConn()")

        if self.ConnSta == True:
            self.Sock.shutdown(socket.SHUT_RDWR)
            self.Sock.close()
            self.ConnSta = False
            DisConnRst = True
            LogScs("Socket connection disconnected.")
        else:
            DisConnRst = False
            LogErr("Socket disconnection failed.")

        LogTr("Exit cTcpSer.DisConn()")

        return DisConnRst

    def Snd(self, Msg):
        """
        @fn Snd
        @brief Tcp server send data.
        @param[in] Msg Send data. Format as hexadecimal string.
        @return Tcp service data sending result.
        @retval True Tcp service data sent correctly.
        @retval False Tcp service data sending failed.
        """

        LogTr("Enter cTcpSer.Snd()")

        if self.ConnSta == True:
            self.ConnHdl.send(bytes.fromhex(Msg))
            SndRst = True
            LogInf("Tcp send: " + Msg)
        else:
            SndRst = False
            LogErr("Socket not connected.")

        LogTr("Exit cTcpSer.Snd()")

        return SndRst

    def Recv(self):
        """
        @fn Recv
        @brief Tcp server receive data.
        @details Maximum reception of 1024 bytes.
        @param None
        @return Receive data. Format as hexadecimal string.
        """

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
        """
        @fn IsRecvBufMty
        @brief Determine if the receive cache is empty.
        @param None
        @return Receive cache non empty state.
        @retval True receive cache is empty.
        @retval False receive cache is empty.
        @retval None Receive cache check failed.
        """

        #LogTr("Enter cTcpSer.IsRecvBufMty()")

        if self.ConnSta == True:
            if self.ConnHdl.recv(1024, socket.MSG_PEEK) == b'':
                ChkRst = True
            else:
                LogTr("Receive cache is not empty.")
                ChkRst = False
        else:
            ChkRst = None
            LogErr("Socket not connected.")

        #LogTr("Exit cTcpSer.IsRecvBufMty()")

        return ChkRst

    def GetConnSta(self):
        """
        @fn GetConnSta
        @brief Get TCP connect state.
        @param None
        @return None
        """

        LogTr("Enter cTcpSer.GetConnSta()")

        ConnSta = self.ConnSta
        LogDbg(f"ConnSta = {self.ConnSta}")

        LogTr("Exit cTcpSer.GetConnSta()")

        return ConnSta

class cTcpClt:
    """
    @class cTcpClt
    @brief Tcp client class.
    @param[in] LocIpAdr Tcp client local ip address.
    - 127.0.0.1 Default value.
    @param[in] RmtIpAdr Tcp client remote ip address.
    - 127.0.0.1 Default value.
    @param[in] LocPt Tcp client local port.
    - 9998 Default value.
    @param[in] RmtPt Tcp client remote port.
    - 9999 Default value.
    @var self.Sock Tcp client socket object。
    @var self.LocIpAdr Tcp client local ip address.
    @var self.RmtIpAdr Tcp client remote ip address.
    @var self.LocPt Tcp client local port.
    @var self.RmtPt Tcp client remote port.
    @var self.ConnSta Tcp client connect status.
    """

    def __init__(self, LocIpAdr = "127.0.0.1", RmtIpAdr = "127.0.0.1", LocPt = 9998, RmtPt = 9999):
        """
        @fn __init__
        @brief Constructor for class cTcpClt.
        @details Initialize socket to block communication. TCP timeout of 10 seconds.
        @param[in] LocIpAdr Tcp client local ip address.
        - 127.0.0.1 Default value.
        @param[in] RmtIpAdr Tcp client remote ip address.
        - 127.0.0.1 Default value.
        @param[in] LocPt Tcp client local port.
        - 9998 Default value.
        @param[in] RmtPt Tcp client remote port.
        - 9999 Default value.
        @return None
        """

        LogTr("Enter cTcpClt.__init__()")

        self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
        self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allows different sockets to reuse ipaddress.
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
        """
        @fn Conn
        @brief Tcp client connected.
        @param None
        @return The execution result of tcp client connection.
        @retval True Successfully connected tcp connection.
        @retval False Failed to connect tcp connection.
        """

        LogTr("Enter cTcpClt.Conn()")

        if self.ConnSta == False:
            try:
                self.Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tcp socket.
                self.Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allows different sockets to reuse ipaddress.
                self.Sock.bind((self.LocIpAdr, self.LocPt))
            except:
                ConnRst = False
                LogErr("Socket bind failed.")
            else:
                LogScs("Socket binding succeeded.")

                try:
                    self.Sock.connect((self.RmtIpAdr, self.RmtPt))
                except:
                    ConnRst = False
                    LogErr("Socket connect failed.")
                else:
                    LogScs("Socket connection succeeded.")
                    self.ConnSta = True
                    ConnRst = True
        else:
            ConnRst = False
            LogErr("Connected tcp socket.")

        LogTr("Exit cTcpClt.Conn()")

        return ConnRst

    def DisConn(self):
        """
        @fn DisConn
        @brief Tcp client disconnected.
        @param None
        @return The execution result of tcp client disconnection.
        @retval True Tcp connection disconnected Successfully.
        @retval False Tcp connection disconnection failed.
        """

        LogTr("Enter cTcpClt.DisConn()")

        if self.ConnSta == True:
            try:
                self.Sock.shutdown(socket.SHUT_RDWR)
            except:
                DisConnRst = False
                LogErr("Socket shutdown failed.")
            else:
                LogScs("Socket shutdown succeeded.")

                try:
                    self.Sock.close()
                except:
                    DisConnRst = False
                    LogErr("Socket close failed.")
                else:
                    LogScs("Socket close succeeded.")
                    self.ConnSta = False
                    DisConnRst = True
        else:
            DisConnRst = False
            LogErr("Socket disconnection failed.")

        LogTr("Exit cTcpClt.DisConn()")

        return DisConnRst

    def Snd(self, Msg):
        """
        @fn Snd
        @brief Tcp client send data.
        @param[in] Msg Send data. Format as hexadecimal string.
        @return Tcp client data sending result.
        @retval True Tcp client data sent correctly.
        @retval False Tcp client data sending failed.
        """

        LogTr("Enter cTcpClt.Snd()")

        if self.ConnSta == True:
            self.Sock.send(bytes.fromhex(Msg))
            SndRst = True
            LogInf("Tcp send: " + Msg)
        else:
            SndRst = False
            LogErr("Socket not connected.")

        LogTr("Exit cTcpClt.Snd()")

        return SndRst

    def Recv(self):
        """
        @fn Recv
        @brief Tcp client receive data.
        @param None
        @return Receive data. Format as hexadecimal string.
        """

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
        """
        @fn IsRecvBufMty
        @brief Determine if the receive cache is empty.
        @param None
        @return Receive cache non empty state.
        @retval True receive cache is empty.
        @retval False receive cache is empty.
        @retval None Receive cache check failed.
        """

        #LogTr("Enter cTcpClt.IsRecvBufMty()")

        if self.ConnSta == True:
            if self.Sock.recv(1024, socket.MSG_PEEK) == "":
                ChkRst = True
            else:
                LogTr("Receive cache is not empty.")
                ChkRst = False
        else:
            ChkRst = None
            LogErr("Socket not connected.")

        #LogTr("Exit cTcpClt.IsRecvBufMty()")

        return ChkRst

    def GetConnSta(self):
        """
        @fn GetConnSta
        @brief Get TCP connect state.
        @param None
        @return None
        """

        LogTr("Enter cTcpClt.GetConnSta()")

        ConnSta = self.ConnSta
        LogDbg(f"ConnSta = {self.ConnSta}")

        LogTr("Exit cTcpClt.GetConnSta()")

        return ConnSta

def ImitTcpSer():
    """
    @fn ImitTcpSer
    @brief Imitate tcp server.
    @param None
    @return None
    """

    LogTr("Enter ImitTcpSer.")

    TcpSer = cTcpSer()
    TcpSer.Lsn()

    while True:
        if TcpSer.IsRecvBufMty() == False:
            Msg = TcpSer.Recv()
            LogDbg(f"Recv: {Msg}")
            TcpSer.Snd("BB")

    TcpSer.DisConn()

def ImitTcpClt():
    """
    @fn ImitTcpClt
    @brief Imitate tcp client.
    @param None
    @return None
    """

    LogTr("Enter ImitTcpClt.")

    TcpClt = cTcpClt()
    TcpClt.Conn()
    TcpClt.Snd("AA")

    while True:
        if TcpClt.IsRecvBufMty() == False:
            Msg = TcpClt.Recv()
            LogDbg(f"Recv: {Msg}")
            TcpClt.Snd("AA")

    TcpClt.DisConn()

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        ImitTcpSer()
    elif sys.argv[1] == "-Clt":
        ImitTcpClt()
