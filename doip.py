##
# @file doip.py
# @brief DoIP protocol.
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
    """
    @class cMsgPset
    @brief The preset value of DoIP message.
    @details ISO 13400-2-2012.
    @param None
    @var self.Hdr The header of a DoIP message.
    @var self.Pl The payload of a DoIP message.
    """

    class cHdr:
        """
        @fn cHdr
        @brief The preset value of DoIP header.
        @param None
        @var self.ProtoVer Protocol version number.
        @var self.InvProtoVer Inversion protocol version number.
        @var self.PlTyp Payload type.
        """

        class cProtoVer:
            """
            @class cProtoVer
            @brief The preset value of protocol version number.
            @details Pos = 0, Len = 1.
            @param None
            @var self.Rsv Reserved.
            - "00" Protocol definition value.
            @var self.v2010 DoIP ISO/DIS 13400-2:2010.
            - "01" Protocol definition value.
            @var self.v2012 DoIP ISO 13400-2:2012.
            - "02" Protocol definition value.
            @var self.IsoRsv Reserved by this part of ISO 13400.
            - "03~FE" Protocol definition value.
            @var self.Vin Vehicle identification request message.
            - "FF" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cProtoVer.
                @param None
                @return None
                """

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

        class cInvProtoVer:
            """
            @class cInvProtoVer
            @brief The preset value of reverse protocol version number.
            @details Pos = 1, Len = 1.
            @param None
            @var self.Rsv Reserved.
            - "FF" Protocol definition value.
            @var self.v2010 DoIP ISO/DIS 13400-2:2010.
            - "FE" Protocol definition value.
            @var self.v2012 DoIP ISO 13400-2:2012.
            - "FD" ProtoVer definition value.
            @var self.Rsv Reserved.
            - "01~FC" Protocol definition value.
            @var self.Vin Vehicle identification request message.
            - "00" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cInvProtoVer.
                @param None
                @return None
                """

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

        class cPlTyp:
            """
            @class cPlTyp
            @brief The preset value of payload messages.
            @details Pos = 2, Len = 2.
            @param None
            @var self.GenDoipHdrNegAck Generic DoIP header negative acknowledge. Mandatory.
            - "0000" Protocol definition value.
            @var self.VehIdReqMsg Vehicle identification request message. Mandatory.
            - "0001" Protocol definition value.
            @var self.VehIdReqMsgEid Vehicle identification request message with EID. Optional.
            - "0002" Protocol definition value.
            @var self.VehIdReqMsgWithVin Vehicle identification request message with VIN. Mandatory.
            - "0003" Protocol definition value.
            @var self.VehAnncMsg Vehicle announcement message/vehicle identification response message.
                                 Mandatory.
            - "0004" Protocol definition value.
            @var self.RteActReq Routing activation request. Mandatory.
            - "0005" Protocol definition value.
            @var self.RteActResp Routing activation response. Mandatory.
            - "0006" Protocol definition value.
            @var self.AlvChkReq Alive check request. Mandatory.
            - "0007" Protocol definition value.
            @var self.AlvChkResp Alive check response. Mandatory.
            - "0008" Protocol definition value.
            @var self.IsoRsv Reserved. Reserve.
            - "0009~4000" Protocol definition value.
            @var self.DoipEntyStsReq DoIP entity status request. Optional.
            - "4001" Protocol definition value.
            @var self.DoipEntyStsResp DoIP entity status response. Optional.
            - "4002" Protocol definition value.
            @var self.DiagPwrMdInfoReq Diagnostic power mode information request. Mandatory.
            - "4003" Protocol definition value.
            @var self.DiagPwrMdInfoResp Diagnostic powermode information response. Mandatory.
            - "4004" Protocol definition value.
            @var self.IsoRsv1 Reserved. Reserve.
            - "4005~8000"  Protocol definition value.
            @var self.DiagMsg Diagnostic message. Mandatory.
            - "8001" Protocol definition value.
            @var self.DiagMsgPosAck Diagnostic message positive acknowledegment. Mandatory.
            - "8002" Protocol definition value.
            @var self.DiagMsgNegAck Diagnostic message negative acknowledegment. Mandatory.
            - "8003" Protocol definition value.
            @var self.IsoRsv2 Reserved. Reserve.
            - "8004~EFFF" Protocol definition value.
            @var self.MfrRsv Reserve for manufacturer-specific use. Optional.
            - "F000~FFFF" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cPlTyp.
                @param None
                @return None
                """

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
                self.DiagPwrMdInfoReq = "4003" # 0x4003: Diagnostic power mode information request.
                LogDbg(f"self.DiagPwrMdInfoReq = {self.DiagPwrMdInfoReq}")
                self.DiagPwrMdInfoResp = "4004" # 0x4004: Diagnostic power mode information response.
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
            """
            @fn __init__
            @brief Constructor for class cHdr.
            @param None
            @return None
            """

            LogTr("Enter cHdr.__init__()")

            self.ProtoVer = self.cProtoVer()
            self.InvProtoVer = self.cInvProtoVer()
            self.PlTyp = self.cPlTyp()

            LogTr("Exit cHdr.__init__()")

    class cPl:
        """
        @class cPl
        @brief DoIP payload message structure.
        @param None
        @var self.RteActReq Routine activation request.
        @var self.RteActResp Routine activation response.
        @var self.DiagMsg Diagnostic message.
        """

        class cRteActReq:
            """
            @class cRteActReq
            @brief The preset value of route activation request message.
            @param None
            @var self.ActTyp Routine type.
            @var self.Rsv Reserved.
            """

            class cActTyp:
                """
                @class cActTyp
                @brief The preset value of active type.
                @param None
                @var self.Dflt Default. Mandatory.
                - "00" ProtoVer definition value.
                @var self.WwhObd WWH-OBD. Mandatory.
                - "01" ProtoVer definition value.
                @var self.IsoRsv ISO/SAE reserved. Reserve.
                - "02~DF" ProtoVer definition value.
                @var self.CntrlSec Central security. Optional.
                - "E0" ProtoVer definition value.
                @var self.OemSpec Available for additional OEM-specific use. Optional.
                - "E1~FF" ProtoVer definition value.
                """

                def __init__(self):
                    """
                    @fn __init__
                    @brief Constructor for class cActTyp.
                    @param None
                    @return None
                    """

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
                """
                @class cRsv
                @brief Default value.
                @param None
                @var self.Dflt Default value.
                - "00000000" ProtoVer definition value.
                """

                def __init__(self):
                    LogTr("Enter cRsv.__init__()")

                    self.Dflt = "00000000" # 0x00000000: Default
                    LogDbg(f"self.Dflt = {self.Dflt}")

                    LogTr("Exit cRsv.__init__()")

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRteActReq.
                @param None
                @return None
                """

                LogTr("Enter cRteActReq.__init__()")

                self.ActTyp = self.cActTyp()
                self.Rsv = self.cRsv()

                LogTr("Exit cRteActReq.__init__()")

        class cRteActResp:
            """
            @class cRteActResp
            @brief The preset value of route activation response message.
            @param None
            @var self.RteActRespCode Routine activation response code.
            @var self.Rsv Reserved.
            """

            class cRteActRespCode:
                """
                @class cRteActRespCode
                @brief The preset value of routing activation response code.
                @param None
                @var self.UnKSrcAdr Routine activation denied due to unknown source address. Mandatory. Mandatory.
                - "00" ProtoVer definition value.
                @var self.SockRegAct Routine activation denied because all concurrently supported TCP_DATA
                                     socket are registered and active. Mandatory.
                - "01" ProtoVer definition value.
                @var self.SaDiffAlrAct Routine activation denied because and SA different from the table
                                       connection entry was received on the already activation TCP_DATA
                                       socket. Mandatory.
                - "02" ProtoVer definition value.
                @var self.SaAlrRegActDiff Routine activation denied because the SA is already registered
                                          and active on a different TCP_DATA socket. Mandatory.
                - "03" ProtoVer definition value.
                @var self.MisAuthn Routine activation denied due to missing authentication. Optional.
                - "04" ProtoVer definition value.
                @var self.RejConf Routine activation denied due to rejected confirmation. Optional.
                - "05" ProtoVer definition value.
                @var self.UnsptRteAct Routine activation denied due to unsupported routing activation type. Mandatory.
                - "06" ProtoVer definition value.
                @var self.IsoRsv Reserved. Reserve.
                - "07~0F" ProtoVer definition value.
                @var self.RteScsAct Routine successfuly activation. Mandatory.
                - "10" ProtoVer definition value.
                @var self.RteWilAct Routine will be activation. Optional.
                - "11" ProtoVer definition value.
                @var self.IsoRsv1 Reserved. Reserve.
                - "12~DF" ProtoVer definition value.
                @var self.VehMfrSpec Vehicle-manufacturer specific. Optional.
                - "E0~FF" ProtoVer definition value.
                @var self.IsoRsv2 Reserved. Reserve.
                - "FF" ProtoVer definition value.
                """

                def __init__(self):
                    LogTr("Enter cRteActRespCode.__init__()")

                    # Mandatory.
                    self.UnKSrcAdr = "00" # 0x00: Routine activation denied due to unknown source address.
                    LogDbg(f"self.UnKSrcAdr = {self.UnKSrcAdr}")
                    self.SockRegAct = "01" # 0x01: Routine activation denied because all concurrently
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
                """
                @class cRsv
                @brief The preset value of Reserve.
                @param None
                @var self.Dflt Reserved.
                """

                def __init__(self):
                    """
                    @fn __init__
                    @brief Constructor for class cRsv.
                    @param None
                    @return None
                    """

                    LogTr("Enter cRsv.__init__()")

                    self.Dflt = "00000000" # 0x00000000: Default
                    LogDbg(f"self.Dflt = {self.Dflt}")

                    LogTr("Exit cRsv.__init__()")

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRteActResp.
                @param None
                @return None
                """

                LogTr("Enter cRteActResp.__init__()")

                self.RteActRespCode = self.cRteActRespCode()
                self.Rsv = self.cRsv()

                LogTr("Exit cRteActResp.__init__()")

        class cDiagMsg:
            """
            @class cDiagMsg
            @brief Diagnostic message.
            @param None
            @var self.PosAckCode Positive response code.
            @var self.NegAckCode Negative response code.
            """

            class cPosAckCode:
                """
                @class cPosAckCode
                @brief The preset value of positive acknowledge code.
                @param None
                @var self.RteCor Routing confirmation acknowledge (ACK) message indicating that the
                                 diagnostic message was correctly received, processed and put into
                                 the transmission buffer of the destination network.
                - "00" Protocol definition value.
                @var self.IsoRsv Reserved. Reserve.
                - "01~FF" Protocol definition value.
                """

                def __init__(self):
                    """
                    @fn __init__
                    @brief Constructor for class cPosAckCode.
                    @param None
                    @return None
                    """

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
                """
                @class cNegAckCode
                @brief The preset value of negative acknowledge code.
                @param None
                @var self.IsoRsv Reserved. Reserve. Reserve.
                - "00~01" Protocol definition value.
                @var self.InvSrcAdr Invalid source address. Mandatory.
                - "02" Protocol definition value.
                @var self.UnkTgtAdr Unknown target address. Mandatory.
                - "03" Protocol definition value.
                @var self.DiagMsgLrg Diagnostic message too large. Mandatory.
                - "04" Protocol definition value.
                @var self.OtMem Out of memory. Mandatory.
                - "05" Protocol definition value.
                @var self.TgtUnreach Target unreachable. Optional.
                - "06" Protocol definition value.
                @var self.UnkNet Unknown network. Optional.
                - "07" Protocol definition value.
                @var self.TransProtoErr Transport protocol error. Optional.
                - "08" Protocol definition value.
                @var self.IsoRsv1 Reserved. Reserve.
                - "09~FF" Protocol definition value.
                """

                def __init__(self):
                    """
                    @fn __init__
                    @brief Constructor for class cNegAckCode.
                    @param None
                    @return None
                    """

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
                """
                @fn __init__
                @brief Constructor for class cPosAckCode.
                @param None
                @return None
                """

                LogTr("Enter cDiagMsg.__init__()")

                self.PosAckCode = self.cPosAckCode()
                self.NegAckCode = self.cNegAckCode()

                LogTr("Exit cDiagMsg.__init__()")

        def __init__(self):
            """
            @fn __init__
            @brief Constructor for class cPl.
            @param None
            @return None
            """

            LogTr("Enter cPl.__init__()")

            self.RteActReq = self.cRteActReq()
            self.RteActResp = self.cRteActResp()
            self.DiagMsg = self.cDiagMsg()

            LogTr("Exit cPl.__init__()")

    def __init__(self):
        """
        @fn __init__
        @brief Constructor for class cMsgPset.
        @param None
        @return None
        """

        LogTr("Enter cMsgPset.__init__()")

        self.Hdr = self.cHdr()
        self.Pl = self.cPl()

        LogTr("Exit cMsgPset.__init__()")

class cMsg:
    """
    @class cMsg
    @brief DoIP message.
    @param None
    @var self.cHdr DoIP message header.
    @var self.cPl DoIP message payload.
    """

    class cHdr:
        """
        @class cHdr
        @brief DoIP header message processing.
        @param None
        @var None
        """

        def __init__(self):
            """
            @fn __init__
            @brief Constructor for class cHdr.
            @param None
            @return None
            """

            LogTr("Enter cHdr.__init__()")

            pass

            LogTr("Exit cHdr.__init__()")

        def AssemHdr(self, ProtoVer, PlTyp, PlLen):
            """
            @fn AssemHdr
            @brief Assembly header message.
            @param[in] ProtoVer Protocol version.
            @param[in] PlTyp Payload type.
            @param[in] PlLen Payload length.
            @return DoIP header message.
            """

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
            """
            @fn PrsHdr
            @brief Parsing DoIP header message.
            @param[in] Hdr DoIP header message.
            @return ProtoVer
            - ProtoVer Protocol version.
            @return InvProtoVer
            - InvProtoVer Inversion protocol version.
            @return PlTyp
            - PlTyp Payload type.
            @return PlLen
            - PlLen Payload length.
            """

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
        """
        @class cPl
        @brief DoIP payload message processing.
        @param None
        @var None
        """

        def __init__(self):
            """
            @fn __init__
            @brief Constructor for class cPl.
            @param None
            @return None
            """

            LogTr("Enter cPl.__init__()")

            pass

            LogTr("Exit cPl.__init__()")

        def AssemPlRteActReq(self, SrcAdr, ActTyp, Rsv, OemSpec = ""):
            """
            @fn AssemPlRteActReq
            @brief Assembly payload routing activation request.
            @param[in] SrcAdr Source address.
            @param[in] ActTyp Activation type.
            @param[in] Rsv Reserved.
            @param[in] OemSpec OEM-Specific.
            - "" Default value.
            @return Pl Payload message.
            """

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
            """
            @fn AssemPlRteActResp
            @brief Assembly payload routing activation response.
            @param[in] TstrLgAdr Tester logical address.
            @param[in] EntyLgAdr Entity logical address.
            @param[in] RteActRespCode Routing activation response code.
            @param[in] Rsv Reserved.
            @param[in] OemSpec OEM-Specific.
            - "" Default value.
            @return Pl Payload message.
            """

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
            """
            @fn PrsPlRteActReq
            @brief Parsing payload routing activation request.
            @param[in] Pl Payload message.
            @return SrcAdr Source address.
            @return ActTyp Activation type.
            @return Rsv Reserved.
            @return OemSpec OEM-Specific.
            """

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
            """
            @fn PrsPlRteActResp
            @brief Parsing payload activation response.
            @param[in] Pl Payload message.
            @return TstrLgAdr Tester logical address.
            @return EntyLgAdr Entity logical address.
            @return RteActRespCode Routing activation response code.
            @return Rsv Reserved.
            @return OemSpec OEM-Specific.
            """

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
            """
            @fn AssemPlDiag
            @brief Assembly payload diagnostic.
            @param[in] SrcAdr Source address.
            @param[in] TgtAdr Target address.
            @param[in] UsrDat User data.
            @return Pl Payload message.
            """

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
            """
            @fn PrsPlDiag
            @brief Parsing payload diagnostic.
            @param[in] Pl Payload message.
            @return SrcAdr Source address.
            @return TgtAdr Target address.
            @return UsrDat User data.
            """

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
            LogDbg(f"UsrDat = {UsrDat}")

            LogTr("Exit cPl.PrsPlDiag()")

            return SrcAdr, TgtAdr, UsrDat

        def PrsPlPosDiag(self, Pl):
            """
            @fn PrsPlPosDiag
            @brief Parsing payload positive diagnostic.
            @param[in] Pl Payload message.
            @return SrcAdr Source address.
            @return TgtAdr Target address.
            @return AckCode Acknowledge code.
            @return DiagMsg Diagnostic message.
            """

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
            """
            @fn PrsPlNegDiag
            @brief Parsing payload negative diagnostic.
            @param[in] Pl Payload message.
            @return SrcAdr Source address.
            @return TgtAdr Target address.
            @return NackCode Negative acknowledge code.
            @return DiagMsg Diagnostic message.
            """

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
        """
        @fn __init__
        @brief Constructor for class cMsg.
        @param None
        @return None
        """

        LogTr("Enter cMsg.__init__()")

        self.Hdr = self.cHdr()
        LogDbg(f"self.Hdr = {self.Hdr}")
        self.Pl = self.cPl()
        LogDbg(f"self.Pl = {self.Pl}")

        LogTr("Exit cMsg.__init__()")

    def AssemMsg(self, Hdr, Pl):
        """
        @fn AssemMsg
        @brief Assembly DoIP message
        @param[in] Hdr DoIP header.
        @param[in] Pl DoIP payload.
        @return Msg DoIP message.
        """

        LogTr("Enter cMsg.AssemMsg()")

        Msg = Hdr + Pl
        LogDbg(f"Msg = {Msg}")

        LogTr("Exit cMsg.AssemMsg()")

        return Msg

    def PrsMsg(self, Msg):
        """
        @fn PrsMsg
        @brief Parsing DoIP message.
        @param[in] Msg DoIP message.
        @return Hdr DoIP header.
        @return Pl DoIP payload.
        """

        LogTr("Enter cMsg.PrsMsg()")

        LogDbg(f"Msg = {Msg}")

        if len(Msg) // 2 < 8:
            raise DatLenErr

        Hdr = Msg[0:16]
        LogDbg(f"Hdr = {Hdr}")
        Pl = Msg[16:]
        LogDbg(f"Pl = {Pl}")

        LogTr("Exit cMsg.PrsMsg()")

        return Hdr, Pl

    def PrsPl(self, Msg):
        """
        @fn PrsPl
        @brief Parsing DoIP message. Get payload type and payload.
        @param[in] Msg DoIP message.
        @return PlTyp Payload type.
        @return Pl Payload.
        """

        LogTr("Enter cMsg.PrsPl")

        LogDbg(f"Msg = {Msg}")

        Hdr, Pl = self.PrsMsg(Msg)
        LogDbg(f"Hdr = {Hdr}")
        LogDbg(f"Pl = {Pl}")

        ProtoVer, InvProtoVer, PlTyp, PlLen = self.Hdr.PrsHdr(Hdr)
        LogDbg(f"ProtoVer = {ProtoVer}")
        LogDbg(f"InvProtoVer = {InvProtoVer}")
        LogDbg(f"PlTyp = {PlTyp}")
        LogDbg(f"PlLen = {PlLen}")

        LogTr("Exit cMsg.PrsPl")

        return PlTyp, Pl

class cDoipSer:
    """
    @class cDoipSer
    @brief DoIP server.
    @param[in] SrcIpAdr Source ip address.
    - "127.0.0.1" Default value.
    @param[in] SrcPt Source port.
    - 13400 Default value.
    @param[in] SrcAdr Source address.
    - "1000" Default value.
    @param[in] FunSrcAdr Function source address.
    - "E000" Default value.
    @var self.SrcIpAdr Source ip address.
    @var self.SrcPt Source port.
    @var self.SrcAdr Source address.
    @var self.FunSrcAdr Function source address.
    @var self.TgtAdr Target address.
    @var self.ConnSta Connect status.
    """

    def __init__(self, SrcIpAdr = "127.0.0.1", SrcPt = 13400, SrcAdr = "1000", FunSrcAdr = "E000"):
        """
        @fn __init__
        @brief Constructor for class cDoipSer.
        @param[in] SrcIpAdr Source ip address.
        - "127.0.0.1" Default value.
        @param[in] SrcPt Source port.
        - 13400 Default value.
        @param[in] SrcAdr Source address.
        - "1000" Default value.
        @param[in] FunSrcAdr Function source address.
        - "E000" Default value.
        @return None
        """

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
        LogDbg(f"self.Msg = {self.Msg}")
        self.MsgPset = cMsgPset()
        LogDbg(f"self.MsgPset = {self.MsgPset}")
        self.TcpSer = tcp.cTcpSer(SrcIpAdr, SrcPt)
        LogDbg(f"self.TcpSer = {self.TcpSer}")

        LogTr("Exit cDoipSer.__init__()")

    def LsnRteAct(self):
        """
        @fn LsnRteAct
        @brief Listen for route activation request.
        @param None
        @return None
        """

        LogTr("Enter cDoipSer.LsnRteAct()")

        self.TcpSer.Lsn()

        if self.TcpSer.GetConnSta() == True:
            LogTr("TCP socket connected.")
            RecvMsg = self.Recv()
            LogDbg(f"RecvMsg = {RecvMsg}")

            if RecvMsg != "":
                PlTyp, Pl = self.Msg.PrsPl(RecvMsg)
                LogDbg(f"PlTyp = {PlTyp}")
                LogDbg(f"Pl = {Pl}")

                if PlTyp == self.MsgPset.Hdr.PlTyp.RteActReq:
                    LogTr("Routing activation request.")
                    SrcAdr, ActTyp, Rsv, OemSpec = self.Msg.Pl.PrsPlRteActReq(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"ActTyp = {ActTyp}")
                    LogDbg(f"Rsv = {Rsv}")
                    LogDbg(f"OemSpec = {OemSpec}")
                    self.TgtAdr = SrcAdr
                    LogDbg(f"self.TgtAdr = {self.TgtAdr}")

                    self.RespRteAct()
                    self.ConnSta = True
                    LogDbg(f"self.ConnSta = {self.ConnSta}")

        LogTr("Exit cDoipSer.LsnRteAct()")

    def DisConn(self):
        """
        @fn DisConn
        @brief DoIP disconnect
        @param None
        @return None
        """

        LogTr("Enter cDoipSer.DisConn()")

        if self.ConnSta == True:
            self.TcpSer.DisConn()
            self.ConnSta = False
            LogScs("Socket connection disconnected.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cDoipSer.DisConn()")

    def Snd(self, Msg):
        """
        @fn Snd
        @brief Send DoIP message.
        @param[in] Msg DoIP message.
        @return None
        """

        LogTr("Enter cDoipSer.Snd()")

        if self.TcpSer.GetConnSta() == True:
            self.TcpSer.Snd(Msg)
            LogInf("DoIP send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cDoipSer.Snd()")

    def Recv(self):
        """
        @fn Recv
        @brief Receive DoIP message.
        @param None
        @return DoIP message.
        """

        LogTr("Enter cDoipSer.Recv()")

        if self.TcpSer.GetConnSta() == True:
            LogTr("Socket connected.")

            Msg = self.TcpSer.Recv()
            LogInf("DoIP recv: " + Msg)
        else:
            Msg = ""
            LogErr("Socket not connected, receiving failed.")

        LogTr("Exit cDoipSer.Recv()")

        return Msg

    def IsRecvBufMty(self):
        """
        @fn IsRecvBufMty
        @brief Check if the UDS receive buffer is empty.
        @param None
        @return Receive buffer status.
        @retval DoIP receive buffer is empty.
        @retval DoIP receive buffer is non empty.
        """

        # LogTr("Enter cDoipSer.IsRecvBufMty()")

        if self.ConnSta == True:
            BufSta = self.TcpSer.IsRecvBufMty()
        else:
            BufSta = None
            LogErr("Socket not connected.")

        # LogTr("Exit cDoipSer.IsRecvBufMty()")

        return BufSta

    def RespRteAct(self):
        """
        @fn RespRteAct
        @brief Response routing active.
        @param None
        @return None
        """

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

    def RespPosDiag(self, AckCode):
        """
        @fn RespPosDiag
        @brief Positive acknowledge diagnostic message.
        @param[in] AckCode Acknowledge code.
        @return None
        """

        LogTr("Enter cDoipSer.RespPosDiag()")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, AckCode)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsgPosAck,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.RespPosDiag()")

    def RespNegDiag(self, NegAckCode):
        """
        @fn RespNegDiag
        @brief Negative acknowledge diagnostic message.
        @param[in] NegAckCode Negative acknowledge code.
        @return None
        """

        LogTr("Enter cDoipSer.RespNegDiag()")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, NegAckCode)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsgNegAck,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.RespNegDiag()")

    def RespDiagMsg(self, UsrDat):
        """
        @fn RespDiagMsg
        @brief Response diagnostic message.
        @param[in] UsrDat Contains the actual diagnostic data.
        @return None
        """

        LogTr("Enter cDoipSer.RespDiagMsg")

        Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, UsrDat)
        LogDbg(f"Pl = {Pl}")
        Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                    self.MsgPset.Hdr.PlTyp.DiagMsg,
                                    "%08X" % (len(Pl) // 2))
        LogDbg(f"Hdr = {Hdr}")
        SndMsg = self.Msg.AssemMsg(Hdr, Pl)
        LogDbg(f"SndMsg = {SndMsg}")
        self.Snd(SndMsg)

        LogTr("Exit cDoipSer.RespDiagMsg")

class cDoipClt:
    """
    @class cDoipClt
    @brief DoIP client.
    @param[in] SrcIpAdr Source ip address.
    - "127.0.0.1" Default value.
    @param[in] TgtIpAdr Target ip address.
    - "127.0.0.1" Default value.
    @param[in] SrcPt Source port.
    - 9999 Default value.
    @param[in] TgtPt Target port.
    - 13400 Default value.
    @param[in] SrcAdr Source address.
    - "0E00" Default value.
    @param[in] TgtAdr Target address.
    - "1000" Default value.
    @param[in] FunTgtAdr Function target address.
    - "E000" Default value.
    @var self.SrcIpAdr Source ip address.
    @var self.TgtIpAdr Target ip address.
    @var self.SrcPt Source port.
    @var self.TgtPt Target port.
    @var self.SrcAdr Source address.
    @var self.TgtAdr Target address.
    @var self.FunTgtAdr Function target address.
    @var self.RteActSta Routine active status.
    """

    def __init__(self, SrcIpAdr = "127.0.0.1", TgtIpAdr = "127.0.0.1", SrcPt = 9999, TgtPt = 13400, SrcAdr = "0E00", TgtAdr = "1000", FunTgtAdr = "E000"):
        """
        @fn __init__
        @brief Constructor for class cDoipClt.
        @param[in] SrcAdr Source address.
        - "127.0.0.1" Default value.
        @param[in] TgtIpAdr Target ip address.
        - "127.0.0.1" Default value.
        @param[in] SrcPt Source port.
        - 9999 Default value.
        @param[in] TgtPt Target port.
        - 13400 Default value.
        @param[in] SrcAdr Source address.
        - "0E00" Default value.
        @param[in] TgtAdr Target address.
        - "1000" Default value.
        @param[in] FunTgtAdr Function target address.
        - "E000" Default value.
        @return None
        """

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
        self.RteActSta = False # Routine active status. True: connected, False: not connected.
        LogDbg(f"self.RteActSta = {self.RteActSta}")
        self.Msg = cMsg()
        LogDbg(f"self.Msg = {self.Msg}")
        self.MsgPset = cMsgPset()
        LogDbg(f"self.MsgPset = {self.MsgPset}")
        self.TcpClt = tcp.cTcpClt(SrcIpAdr, TgtIpAdr, SrcPt, TgtPt)
        LogTr(f"self.TcpClt = {self.TcpClt}")

        LogTr("Exit cDoipClt.__init__()")

    def DisConn(self):
        """
        @fn DisConn
        @brief DoIP disconnect.
        @param None
        @return DisConnRst The resulte of disconnect.
        @retval False Socket disconnect failed.
        @retval True Socket disconnect succeeded.
        """

        LogTr("Enter cDoipClt.DisConn()")

        DisConnRst = False

        if self.RteActSta == True:
            if self.TcpClt.DisConn():
                LogScs("Socket connection disconnected.")
                self.RteActSta = False
                DisConnRst = True
            else:
                LogErr("Socket disconnection failed.")
        else:
            LogErr("Socket disconnection failed.")

        LogTr("Exit cDoipClt.DisConn()")

        return DisConnRst

    def Snd(self, Msg):
        """
        @fn Snd
        @brief Send DoIP message.
        @param[in] Msg DoIP message.
        @return None
        """

        LogTr("Enter cDoipClt.Snd()")

        if self.TcpClt.GetConnSta() == True:
            LogTr("Socket connected.")

            self.TcpClt.Snd(Msg)
            LogInf("DoIP send: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cDoipClt.Snd()")

    def Recv(self):
        """
        @fn Recv
        @brief Receive DoIP message.
        @param None
        @return DoIP message.
        """

        LogTr("Enter cDoipClt.Recv()")

        if self.TcpClt.GetConnSta() == True:
            LogTr("Socket connected.")

            Msg = self.TcpClt.Recv()
            LogInf("DoIP recv: " + Msg)
        else:
            LogErr("Socket not connected, sending failed.")

        LogTr("Exit cDoipClt.Recv()")

        return Msg

    def ReqRteAct(self):
        """
        @fn ReqRteAct
        @brief Request routing activation.
        @param None
        @return None
        """

        LogTr("Enter cDoipClt.ReqRteAct()")

        if self.TcpClt.Conn():
            LogScs("Socket connection succeeded.")

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
            LogTr("Request routing activation.")
            ReqRst = True
        else:
            LogErr("Socket connect failed.")
            ReqRst = False

        LogTr("Exit cDoipClt.ReqRteAct()")

        return ReqRst

    def RespRteAct(self):
        """
        @fn RespRteAct
        @brief Response routing activation.
        @param None
        @return None
        """

        LogTr("Enter cDoipClt.RespRteAct()")

        RecvMsg = self.Recv()
        LogDbg(f"RecvMsg = {RecvMsg}")
        PlTyp, Pl = self.Msg.PrsPl(RecvMsg)
        TstrLgAdr, EntyLgAdr, RteActRespCode, Rsv, OemSpec = self.Msg.Pl.PrsPlRteActResp(Pl)
        LogDbg(f"TstrLgAdr = {TstrLgAdr}")
        LogDbg(f"EntyLgAdr = {EntyLgAdr}")
        LogDbg(f"RteActRespCode = {RteActRespCode}")
        LogDbg(f"Rsv = {Rsv}")
        LogDbg(f"OemSpec = {OemSpec}")

        if RteActRespCode == self.MsgPset.Pl.RteActResp.RteActRespCode.RteScsAct:
            LogTr("Route activation succeeded.")

            self.RteActSta = True
            LogDbg(f"self.RteActSta = {self.RteActSta}")
        else:
            LogTr("Route activation failed.")

            self.RteActSta = False
            LogDbg(f"self.RteActSta = {self.RteActSta}")

        LogTr("Exit cDoipClt.RespRteAct()")

        return PlTyp, RteActRespCode

    def ReqDiag(self, UsrDat):
        """
        @fn ReqDiag
        @brief Request diagnosis.
        @param[in] UsrDat User data.
        @return None
        """

        LogTr("Enter cDoipClt.ReqDiag()")

        LogDbg(f"UsrDat = {UsrDat}")

        if self.RteActSta == True:
            LogTr("Request diagnosis.")

            Pl = self.Msg.Pl.AssemPlDiag(self.SrcAdr, self.TgtAdr, UsrDat)
            LogDbg(f"Pl = {Pl}")
            Hdr = self.Msg.Hdr.AssemHdr(self.MsgPset.Hdr.ProtoVer.v2012,
                                        self.MsgPset.Hdr.PlTyp.DiagMsg,
                                        "%08X" % (len(Pl) // 2))
            LogDbg(f"Hdr = {Hdr}")
            SndMsg = self.Msg.AssemMsg(Hdr, Pl)
            LogDbg(f"SndMsg = {SndMsg}")
            self.Snd(SndMsg)
            ReqRst = True
        else:
            LogTr("Request diagnosis failed.")

            ReqRst = False

        LogTr("Exit cDoipClt.ReqDiag()")

        return ReqRst

    def RespAckDiag(self):
        """
        @fn RespAckDiag
        @brief Response diagnosis. May be a positive or negative response. Waiting for message reception.
        @param None
        @return PlTyp Payload type.
        @return AckCode Acknowledge code.
        """

        LogTr("Enter cDoipClt.RespAckDiag()")

        if self.RteActSta == True:
            LogTr("Response diagnosis response.")

            RecvMsg = self.Recv()
            LogDbg(f"RecvMsg = {RecvMsg}")
            PlTyp, Pl = self.Msg.PrsPl(RecvMsg)
            SrcAdr, TgtAdr, AckCode, DiagMsg = self.Msg.Pl.PrsPlPosDiag(Pl)
            LogDbg(f"SrcAdr = {SrcAdr}")
            LogDbg(f"TgtAdr = {TgtAdr}")
            LogDbg(f"AckCode = {AckCode}")
            LogDbg(f"DiagMsg = {DiagMsg}")

            if PlTyp == self.MsgPset.Hdr.PlTyp.DiagMsgPosAck:
                LogTr("Positive diagnostic response.")
            elif PlTyp == self.MsgPset.Hdr.PlTyp.DiagMsgNegAck:
                LogTr("Negative diagnostic response.")
        else:
            LogTr("Response diagnosis response failed.")

        LogTr("Exit cDoipClt.RespAckDiag()")

        return PlTyp, AckCode

    def RespDiagMsg(self):
        """
        @fn RespDiagMsg
        @brief Response diagnosis message. Waiting for message reception.
        @param None
        @return PlTyp Payload type.
        @return AckCode Acknowledge code.
        """

        LogTr("Enter cDoipClt.RespDiagMsg()")

        if self.RteActSta == True:
            LogTr("Response diagnosis message.")

            RecvMsg = self.Recv()
            LogDbg(f"RecvMsg = {RecvMsg}")
            PlTyp, Pl = self.Msg.PrsPl(RecvMsg)
            SrcAdr, TgtAdr, UsrDat = self.Msg.Pl.PrsPlDiag(Pl)
            LogDbg(f"SrcAdr = {SrcAdr}")
            LogDbg(f"TgtAdr = {TgtAdr}")
            LogDbg(f"UsrDat = {UsrDat}")
        else:
            LogTr("Response diagnosis message failed.")

        LogTr("Exit cDoipClt.RespDiagMsg()")

        return PlTyp, UsrDat

    def IsRecvBufMty(self):
        """
        @fn IsRecvBufMty
        @brief Is receive buffer empty.
        @param None
        @return Rtn Receive buffer status.
        """

        # LogTr("Enter cDoipClt.IsRecvBufMty()")

        if self.RteActSta == True:
            Rtn = self.TcpClt.IsRecvBufMty()
        else:
            Rtn = None
            LogErr("Socket not connected.")

        # LogTr("Exit cDoipClt.IsRecvBufMty()")

        return Rtn

def ImitDoipSer():
    """
    @fn ImitDoipSer
    @brief Imitate DoIP server.
    @param None
    @return None
    """

    LogTr("Enter ImitDoipSer().")

    Ecu = cDoipSer()
    Ecu.LsnRteAct()

    while True:
        if Ecu.IsRecvBufMty() == False:
            RecvMsg = Ecu.Recv()
            LogDbg(f"RecvMsg: {RecvMsg}")

            if RecvMsg != "":
                PlTyp, Pl = Ecu.Msg.PrsPl(RecvMsg)

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
                    SrcAdr, TgtAdr, UsrDat = Ecu.Msg.Pl.PrsPlDiag(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"TgtAdr = {TgtAdr}")
                    LogDbg(f"UsrDat = {UsrDat}")

                    Ecu.RespPosDiag("00")
                    Ecu.RespDiagMsg("5003003201F4")

    LogTr("Exit ImitDoipSer().")

def ImitDoipClt():
    """
    @fn ImitDoipClt
    @brief Imitate DoIP client.
    @param None
    @return None
    """

    LogTr("Enter ImitDoipClt().")

    Tstr = cDoipClt()
    Tstr.ReqRteAct()
    Tstr.RespRteAct()
    Tstr.ReqDiag("1003")
    PlTyp, AckCode = Tstr.RespAckDiag()

    if PlTyp == Tstr.MsgPset.Hdr.PlTyp.DiagMsgPosAck:
        Tstr.RespDiagMsg()

    LogTr("Exit ImitDoipClt().")

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        ImitDoipSer()
    elif sys.argv[1] == "-Clt":
        ImitDoipClt()
