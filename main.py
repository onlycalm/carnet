##
# @file main.py
# @brief 入口文件。
# @details 无
# @author Calm
# @date 2022-12-28
# @version v1.0.0
# @copyright Calm
#

import sys
import atexit
from log import *
from doip import *

def ImitEcu():
    LogTr("Enter ImitEcu().")

    Ecu = cDoipSer()
    atexit.register(Ecu.DisConn)
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

                    Ecu.RespDiag("1101")

    LogTr("Exit ImitEcu().")

def ImitTstr():
    LogTr("Enter ImitTstr().")

    Tstr = cDoipClt()
    atexit.register(Tstr.DisConn)

    if Tstr.Conn():
        LogScs("Tcp connection succeeded.")

        Tstr.ReqRteAct()
        PlTyp, RteActRespCode = Tstr.RespRteAct()
        Tstr.ReqDiag("1003")
        Tstr.RespDiag()
    else:
        LogErr("Tcp connect failed.")

    LogTr("Exit ImitTstr().")

def main():
    LogTr("Enter main().")

    if sys.argv[1] == "-Ser":
        ImitEcu()
    elif sys.argv[1] == "-Clt":
        ImitTstr()

    LogTr("Exit main().")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        LogScs("Keyboard Interrupt. Exit program operation.")
