##
# @file uds.py
# @brief UDS protocol.
# @details None.
# @author Calm
# @date 2023-06-11
# @version v1.0.0
# @copyright Calm
#

import sys
from doip import *
from log import *

class cMsgPset:
    """
    @class cMsgPset
    @brief The preset value of cMsgPset.
    @details ISO 14229-1-2013.
    @param None
    @var self.Sid Service ID.
    @var self.SubFun Subfunction.
    @var self.Nrc Negative response code.
    """

    class cSid:
        """
        @class cSid
        @brief The preset value of cSid.
        @param None
        @var self.DiagSessCtrl Diagnostic session control.
        - "10" Protocol definition value.
        @var self.EcuRst Ecu reset.
        - "11" Protocol definition value.
        @var self.SecAcc Security access.
        - "27" Protocol definition value.
        @var self.CommCtrl Communication control.
        - "28" Protocol definition value.
        @var self.TstrPrsnt Tester present.
        - "3E" Protocol definition value.
        @var self.AccTmParam Access timing parameter.
        - "83" Protocol definition value.
        @var self.SecdDatTx Secured data transmission.
        - "84" Protocol definition value.
        @var self.CtrlDtcSet Control dtc setting.
        - "85" Protocol definition value.
        @var self.RespOnEvt Response on event.
        - "86" Protocol definition value.
        @var self.LinkCtrl Link control.
        - "87" Protocol definition value.
        @var self.RdDatById Read data by identifier.
        - "22" Protocol definition value.
        @var self.RdMemByAdr Read memory by address.
        - "23" Protocol definition value.
        @var self.RdScDatById Read scaling data by identifier.
        - "24" Protocol definition value.
        @var self.RdDatByPerId Read data by periodic identifier.
        - "2A" Protocol definition value.
        @var self.DynDefDatId Dynamically define data identifier.
        - "2C" Protocol definition value.
        @var self.WrDatById Write data by identifier.
        - "2E" Protocol definition value.
        @var self.WrMemByAdr Write memory by address.
        - "3D" Protocol definition value.
        @var self.ClrDiagInfo Clear diagnostic information.
        - "14" Protocol definition value.
        @var self.RdDtcInfo Read dtc information.
        - "19" Protocol definition value.
        @var self.IoCtrlById Input out put control by identifier.
        - "2F" Protocol definition value.
        @var self.RtCtrl Routine control.
        - "31" Protocol definition value.
        @var self.ReqDwnld Request download.
        - "34" Protocol definition value.
        @var self.ReqUpld Request upload.
        - "35" Protocol definition value.
        @var self.TxDat Transfer data.
        - "36" Protocol definition value.
        @var self.ReqTxEx Request transfer exit.
        - "37" Protocol definition value.
        @var self.ReqFileTx Request file transfer.
        - "38" Protocol definition value.
        """

        def __init__(self):
            """
            @fn __init__
            @brief Constructor for class cSid.
            @param None
            @return None
            """

            LogTr("Enter cSid.__init__()")

            self.DiagSessCtrl = "10"
            LogDbg(f"self.DiagSessCtrl = {self.DiagSessCtrl}")
            self.EcuRst = "11"
            LogDbg(f"self.EcuRst = {self.EcuRst}")
            self.SecAcc = "27"
            LogDbg(f"self.SecAcc = {self.SecAcc}")
            self.CommCtrl = "28"
            LogDbg(f"self.CommCtrl = {self.CommCtrl}")
            self.TstrPrsnt = "3E"
            LogDbg(f"self.TstrPrsnt = {self.TstrPrsnt}")
            self.AccTmParam = "83"
            LogDbg(f"self.AccTmParam = {self.AccTmParam}")
            self.SecdDatTx = "84"
            LogDbg(f"self.SecdDatTx = {self.SecdDatTx}")
            self.CtrlDtcSet = "85"
            LogDbg(f"self.CtrlDtcSet = {self.CtrlDtcSet}")
            self.RespOnEvt = "86"
            LogDbg(f"self.RespOnEvt = {self.RespOnEvt}")
            self.LinkCtrl = "87"
            LogDbg(f"self.LinkCtrl = {self.LinkCtrl}")
            self.RdDatById = "22"
            LogDbg(f"self.RdDatById = {self.RdDatById}")
            self.RdMemByAdr = "23"
            LogDbg(f"self.RdMemByAdr = {self.RdMemByAdr}")
            self.RdScDatById = "24"
            LogDbg(f"self.RdScDatById = {self.RdScDatById}")
            self.RdDatByPerId = "2A"
            LogDbg(f"self.RdDatByPerId = {self.RdDatByPerId}")
            self.DynDefDatId = "2C"
            LogDbg(f"self.DynDefDatId = {self.DynDefDatId}")
            self.WrDatById = "2E"
            LogDbg(f"self.WrDatById = {self.WrDatById}")
            self.WrMemByAdr = "3D"
            LogDbg(f"self.WrMemByAdr = {self.WrMemByAdr}")
            self.ClrDiagInfo = "14"
            LogDbg(f"self.ClrDiagInfo = {self.ClrDiagInfo}")
            self.RdDtcInfo = "19"
            LogDbg(f"self.RdDtcInfo = {self.RdDtcInfo}")
            self.IoCtrlById = "2F"
            LogDbg(f"self.IoCtrlById = {self.IoCtrlById}")
            self.RtCtrl = "31"
            LogDbg(f"self.RtCtrl = {self.RtCtrl}")
            self.ReqDwnld = "34"
            LogDbg(f"self.ReqDwnld = {self.ReqDwnld}")
            self.ReqUpld = "35"
            LogDbg(f"self.ReqUpld = {self.ReqUpld}")
            self.TxDat = "36"
            LogDbg(f"self.TxDat = {self.TxDat}")
            self.ReqTxEx = "37"
            LogDbg(f"self.ReqTxEx = {self.ReqTxEx}")
            self.ReqFileTx = "38"
            LogDbg(f"self.ReqFileTx = {self.ReqFileTx}")

            LogTr("Exit cSid.__init__()")

    class cSubFun:
        """
        @class cSubFun
        @brief The preset value of cSubFun.
        @param Non
        @var self.DiagSessCtrl Diagnostic session control.
        @var self.EcuRst ECU reset.
        @var self.SecAcc Security access.
        @var self.CommCtrl Communication control.
        @var self.TstrPrsnt Tester present.
        @var self.AccTmParam Access timing parameter.
        @var self.SecdDatTx Secured data transmission.
        @var self.CtrlDtcSet Control dtc setting.
        @var self.RespOnEvt Response on event.
        @var self.LinkCtrl Link control.
        @var self.RdDatById Read data by identifier.
        @var self.RdMemByAdr Read memory by address.
        @var self.RdScDatById Read scaling data by identifier.
        @var self.RdDatByPerId Read data by periodic identifier.
        @var self.DynDefDatId Dynamically define data identifier.
        @var self.WrDatById Write data by identifier.
        @var self.WrMemByAdr Write memory by address.
        @var self.ClrDiagInfo Clear diagnostic information.
        @var self.RdDtcInfo Read dtc information.
        @var self.IoCtrlById Input out put control by identifier.
        @var self.RtCtrl Routine control.
        @var self.ReqDwnld Request download.
        @var self.ReqUpld Request upload.
        @var self.TxDat Transfer data.
        @var self.ReqTxEx Request transfer exit.
        @var self.ReqFileTx Request file transfer.
        """

        class cDiagSessCtrl:
            """
            @class cDiagSessCtrl
            @brief The preset value of cDiagSessCtrl.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.DfltSess Default session.
            - "01" Protocol definition value.
            @var self.ProgSess Programming session.
            - "02" Protocol definition value.
            @var self.ExtDiagSess Externded diagnostic session.
            - "03" Protocol definition value.
            @var self.SafSysDiagSess Safety system diagnostic session.
            - "04" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "05~3F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "40~5F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "60~7E" Protocol definition value.
            @var self.IsoRsv2 ISO SAE reserved.
            - "7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cDiagSessCtrl.
                @param None
                @return None
                """

                LogTr("Enter cDiagSessCtrl.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.DfltSess = "01"
                LogDbg(f"self.DfltSess = {self.DfltSess}")
                self.ProgSess = "02"
                LogDbg(f"self.ProgSess = {self.ProgSess}")
                self.ExtDiagSess = "03"
                LogDbg(f"self.ExtDiagSess = {self.ExtDiagSess}")
                self.SafSysDiagSess = "04"
                LogDbg(f"self.SafSysDiagSess = {self.SafSysDiagSess}")
                self.IsoRsv1 = "05~3F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cDiagSessCtrl.__init__()")

        class cEcuRst:
            """
            @class cEcuRst
            @brief Constructor for class cEcuRst.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.HrdRst Hard reset.
            - "01" Protocol definition value.
            @var self.KeyOffOnRst Key off on reset.
            - "02" Protocol definition value.
            @var self.SftRst Soft reset.
            - "03" Protocol definition value.
            @var self.EnRpdPwSd Enable rapid power shutdown.
            - "04" Protocol definition value.
            @var self.DisRpdPwSd Disable rapid power shutdown.
            - "05" Protocol definition value.
            @var self.IsoRsv1 ISO reserved.
            - "06~3F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "40~5F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "60~7E" Protocol definition value.
            @var self.IsoRsv2 ISO reserved.
            - "7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cEcuRst.
                @param None
                @return None
                """

                LogTr("Enter cEcuRst.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.HrdRst = "01"
                LogDbg(f"self.HrdRst = {self.HrdRst}")
                self.KeyOffOnRst = "02"
                LogDbg(f"self.KeyOffOnRst = {self.KeyOffOnRst}")
                self.SftRst = "03"
                LogDbg(f"self.SftRst = {self.SftRst}")
                self.EnRpdPwSd = "04"
                LogDbg(f"self.EnRpdPwSd = {self.EnRpdPwSd}")
                self.DisRpdPwSd = "05"
                LogDbg(f"self.DisRpdPwSd = {self.DisRpdPwSd}")
                self.IsoRsv1 = "06~3F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cEcuRst.__init__()")

        class cSecAcc:
            """
            @class cSecAcc
            @brief The preset value of cSecAcc.
            @param None
            @var self.IsoRsv ISO reserved.
            - "00" Protocol definition value.
            @var self.ReqSed Request seed.
            - "01" Protocol definition value.
            @var self.SndKey Send key.
            - "02" Protocol definition value.
            @var self.ReqSed Request seed.
            - "03, 05, 07~41" Protocol definition value.
            @var self.SndKey Send key.
            - "04, 06, 08~42" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "43~5E" Protocol definition value.
            @var self.Iso26021 ISO 26021-2 values.
            - "5F" Protocol definition values.
            @var self.Iso26021SndKey ISO 26021-2 send key values.
            - "60" Protocol definition values.
            @var self.SysSplrSpec System supplier specific.
            - "61~7E" Protocol definition values.
            @var self.IsoRsv2 ISO SAE reserved.
            - "7F" Protocol definition values.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cSecAcc.
                @param None
                @return None
                """

                LogTr("Enter cSecAcc.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.ReqSed = "01"
                LogDbg(f"self.ReqSed = {self.ReqSed}")
                self.SndKey = "02"
                LogDbg(f"self.SndKey = {self.SndKey}")
                self.ReqSed = "03, 05, 07~41"
                LogDbg(f"self.ReqSed = {self.ReqSed}")
                self.SndKey = "04, 06, 08~42"
                LogDbg(f"self.SndKey = {self.SndKey}")
                self.IsoRsv1 = "43~5E"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.Iso26021 = "5F"
                LogDbg(f"self.Iso26021 = {self.Iso26021}")
                self.Iso26021SndKey = "60"
                LogDbg(f"self.Iso26021SndKey = {self.Iso26021SndKey}")
                self.SysSplrSpec = "61~7E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cSecAcc.__init__()")

        class cCommCtrl:
            """
            @class cCommCtrl
            @brief The preset value of cCommCtrl.
            @param None
            @var self.EnRxTx Enable rx and tx.
            - "00" Protocol definition value.
            @var self.EnRxDisTx Enable rx and Disable tx.
            - "01" Protocol definition value.
            @var self.DisRxEnTx Disable rx and enable tx.
            - "02" Protocol definition value.
            @var self.DisRxTx Disable rx and tx.
            - "03" Protocol definition value.
            @var self.EnRxDisTxWithEnhncAdrInfo Enable rx and disable tx with enhanced address information.
            - "04" Protocol definition value.
            @var self.EnRxTxWithEnhncAdrInfo Enable rx and tx with enhanced address information.
            - "05" Protocol definition value.
            @var self.ISO SAE reserved.
            - "06~3F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "40~5F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "60~7E" ProgSess definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "7F" ProgSess definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cCommCtrl.
                @param None
                @return None
                """

                LogTr("Enter cCommCtrl.__init__()")

                self.EnRxTx = "00"
                LogDbg(f"self.EnRxTx = {self.EnRxTx}")
                self.EnRxDisTx = "01"
                LogDbg(f"self.EnRxDisTx = {self.EnRxDisTx}")
                self.DisRxEnTx = "02"
                LogDbg(f"self.DisRxEnTx = {self.DisRxEnTx}")
                self.DisRxTx = "03"
                LogDbg(f"self.DisRxTx = {self.DisRxTx}")
                self.EnRxDisTxWithEnhncAdrInfo = "04"
                LogDbg(f"self.EnRxDisTxWithEnhncAdrInfo = {self.EnRxDisTxWithEnhncAdrInfo}")
                self.EnRxTxWithEnhncAdrInfo = "05"
                LogDbg(f"self.EnRxTxWithEnhncAdrInfo = {self.EnRxTxWithEnhncAdrInfo}")
                self.IsoRsv = "06~3F"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.VhcMfrSpec = "40~5F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv1 = "7F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                LogTr("Exit cCommCtrl.__init__()")

        class cTstrPrsnt:
            """
            @class cTstrPrsnt
            @brief Constructor for class cTstrPrsnt.
            @param None
            @var self.ZSubFun Zero Subfunction.
            - "00" ProgSess definition value.
            @var self.IsoRsv ISO SAE reserved.
            - "01~7F" ProgSess definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief 简述函数功能。
                @param None
                @return None
                """

                LogTr("Enter cTstrPrsnt.__init__()")

                self.ZSubFun = "00"
                LogDbg(f"self.ZSubFun = {self.ZSubFun}")
                self.IsoRsv = "01~7F"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                LogTr("Exit cTstrPrsnt.__init__()")

        class cAccTmParam:
            """
            @class cAccTmParam
            @brief Constructor for class cAccTmParam.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.RdExtdTmParamSet Read externded timing parameter set.
            - "01" Protocol definition value.
            @var self.SetTmParamToDfltVal Set timing parameter to Default values.
            - "02" Protocol definition values.
            @var self.RdCurrActTmParam Read currently active timing parameters.
            - "03" Protocol definition values.
            @var self.SetTmParamToGvnVal Set timing parameters to given values.
            - "04" Protocol definition values.
            @var self.IsoRsv ISO SAE reserved.
            - "05~FF" Protocol definition values.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cAccTmParam.
                @param None
                @return None
                """

                LogTr("Enter cAccTmParam.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.RdExtdTmParamSet = "01"
                LogDbg(f"self.RdExtdTmParamSet = {self.RdExtdTmParamSet}")
                self.SetTmParamToDfltVal = "02"
                LogDbg(f"self.SetTmParamToDfltVal = {self.SetTmParamToDfltVal}")
                self.RdCurrActTmParam = "03"
                LogDbg(f"self.RdCurrActTmParam = {self.RdCurrActTmParam}")
                self.SetTmParamToGvnVal = "04"
                LogDbg(f"self.SetTmParamToGvnVal = {self.SetTmParamToGvnVal}")
                self.IsoRsv = "05~FF"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                LogTr("Exit cAccTmParam.__init__()")

        class cSecdDatTx:
            """
            @class cSecdDatTx
            @brief The preset value of cSecdDatTx.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.On On.
            - "01" Protocol definition value.
            @var self.Off Off.
            - "02" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "03~3F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "40~5F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "60~7E" Protocol definition value.
            @var self.IsoRsv2 ISO SAE reserved.
            - "7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cSecdDatTx.
                @param None
                @return None
                """

                LogTr("Enter cSecdDatTx.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.On = "01"
                LogDbg(f"self.On = {self.On}")
                self.Off = "02"
                LogDbg(f"self.Off = {self.Off}")
                self.IsoRsv1 = "03~3F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E"
                LogDbg(f"self.systemSupplierSpecific = {self.systemSupplierSpecific}")
                self.IsoRsv2 = "7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cSecdDatTx.__init__()")

        class cCtrlDtcSet:
            """
            @class cCtrlDtcSet
            @brief The preset value of cCtrlDtcSet.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.On On.
            - "01" Protocol definition value.
            @var self.Off Off.
            - "02" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "03~3F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "40~5F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "60~7E" Protocol definition value.
            @var self.IsoRsv2 ISO SAE reserved.
            - "7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cCtrlDtcSet.
                @param None
                @return None
                """

                LogTr("Enter cCtrlDtcSet.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.On = "01"
                LogDbg(f"self.On = {self.On}")
                self.Off = "02"
                LogDbg(f"self.Off = {self.Off}")
                self.IsoRsv1 = "03~3F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cCtrlDtcSet.__init__()")

        class cRespOnEvt:
            """
            @class cRespOnEvt
            @brief The preset value of cRespOnEvt.
            @param None
            @var self.StpRespOnEvt Stop response on event.
            - "00" Protocol definition value.
            @var self.OnDtcStsChg On DTC status change.
            - "01" Protocol definition value.
            @var self.OnTmIntr On timer interrupt.
            - "02" Protocol definition value.
            @var self.OnChgOfDatId On change of data identifier.
            - "03" Protocol definition value.
            @var self.RptActEvt Report activated events.
            - "04" Protocol definition value.
            @var self.StrtRespOnEvt Start response on event.
            - "05" Protocol definition value.
            @var self.ClrRespOnEvt Clear response on event.
            - "06" Protocol definition value.
            @var self.OnCompOfVal On comparison of values.
            - "07" Protocol definition value.
            @var self.IsoRsv ISO SAE reserved.
            - "08~1F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "20~2F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "30~3E" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "3F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRespOnEvt.
                @param None
                @return None
                """

                LogTr("Enter cRespOnEvt.__init__()")

                self.StpRespOnEvt = "00"
                LogDbg(f"self.StpRespOnEvt = {self.StpRespOnEvt}")
                self.OnDtcStsChg = "01"
                LogDbg(f"self.OnDtcStsChg = {self.OnDtcStsChg}")
                self.OnTmIntr = "02"
                LogDbg(f"self.OnTmIntr = {self.OnTmIntr}")
                self.OnChgOfDatId = "03"
                LogDbg(f"self.OnChgOfDatId = {self.OnChgOfDatId}")
                self.RptActEvt = "04"
                LogDbg(f"self.RptActEvt = {self.RptActEvt}")
                self.StrtRespOnEvt = "05"
                LogDbg(f"self.StrtRespOnEvt = {self.StrtRespOnEvt}")
                self.ClrRespOnEvt = "06"
                LogDbg(f"self.ClrRespOnEvt = {self.ClrRespOnEvt}")
                self.OnCompOfVal = "07"
                LogDbg(f"self.OnCompOfVal = {self.OnCompOfVal}")
                self.IsoRsv = "08~1F"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.VhcMfrSpec = "20~2F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "30~3E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv1 = "3F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                LogTr("Exit cRespOnEvt.__init__()")

        class cLnkCtrl:
            """
            @class cLnkCtrl
            @brief The preset value of cLnkCtrl.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.VfyMoTransWFixParam Verify mode transition with fixed parameter.
            - "01" Protocol definition value.
            @var self.VfyMoTransWSpecParam Verify mode transition with specific parameter.
            - "02" Protocol definition value.
            @var self.TransMo Transition mode.
            - "03" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "04~3F" Protocol definition value.
            @var self.VhcMfrSpec Vehicle manufacturer specific.
            - "40~5F" Protocol definition value.
            @var self.SysSplrSpec System supplier specific.
            - "60~7E" Protocol definition value.
            @var self.IsoRsv2 ISO SAE reserved.
            - "7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cLnkCtrl.
                @param None
                @return None
                """

                LogTr("Enter cLnkCtrl.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.VfyMoTransWFixParam = "01"
                LogDbg(f"self.VfyMoTransWFixParam = {self.VfyMoTransWFixParam}")
                self.VfyMoTransWSpecParam = "02"
                LogDbg(f"self.VfyMoTransWSpecParam")
                self.TransMo = "03"
                LogDbg(f"self.TransMo = {self.TransMo}")
                self.IsoRsv1 = "04~3F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F"
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E"
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cLnkCtrl.__init__()")

        class cRdDatById:
            """
            @class cRdDatById
            @brief The preset value of cRdDatById.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdDatById.
                @param None
                @return None
                """

                LogTr("Enter cRdDatById.__init__()")

                LogTr("Exit cRdDatById.__init__()")

        class cRdMemByAdr:
            """
            @class cRdMemByAdr
            @brief The preset value of cRdMemByAdr.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdMemByAdr.
                @param None
                @return None
                """

                LogTr("Enter cRdMemByAdr.__init__()")

                LogTr("Exit cRdMemByAdr.__init__()")

        class cRdScDatById:
            """
            @class cRdScDatById
            @brief The preset value of cRdScDatById.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdScDatById.
                @param None
                @return None
                """

                LogTr("Enter cRdScDatById.__init__()")

                LogTr("Exit cRdScDatById.__init__()")

        class cRdDatByPerId:
            """
            @class cRdDatByPerId
            @brief The preset value of cRdDatByPerId.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdDatByPerId.
                @param None
                @return None
                """

                LogTr("Enter cRdDatByPerId.__init__()")

                LogTr("Exit cRdDatByPerId.__init__()")

        class cDynDefDatId:
            """
            @class cDynDefDatId
            @brief The preset value of cDynDefDatId.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.DefById Define by identifier.
            - "01" Protocol definition value.
            @var self.DefByMemAdr Define by memory address.
            - "02" Protocol definition value.
            @var self.ClrDynDefDatId Clear Dynamically defined identifier.
            - "03" Protocol definition value.
            @var self.ISO SAE reserved.
            - "04~7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cDynDefDatId.
                @param None
                @return None
                """

                LogTr("Enter cDynDefDatId.__init__()")

                self.IsoRsv = "00" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.DefById = "01" # defineByIdentifier.
                LogDbg(f"self.DefById = {self.DefById}")
                self.DefByMemAdr = "02" # defineByMemoryAddress.
                LogDbg(f"self.DefByMemAdr = {self.DefByMemAdr}")
                self.ClrDynDefDatId = "03" # clearDynamicallyDefineDataIdentifier.
                LogDbg(f"self.ClrDynDefDatId = {self.ClrDynDefDatId}")
                self.IsoRsv1 = "04~7F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                LogTr("Exit cDynDefDatId.__init__()")

        class cWrDatById:
            """
            @class cWrDatById
            @brief The preset value of cWrDatById.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cWrDatById.
                @param None
                @return None
                """

                LogTr("Enter cWrDatById.__init__()")

                LogTr("Exit cWrDatById.__init__()")

        class cWrMemByAdr:
            """
            @class cWrMemByAdr
            @brief The preset value of cWrMemByAdr.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cWrMemByAdr.
                @param None
                @return None
                """

                LogTr("Enter cWrMemByAdr.__init__()")

                LogTr("Exit cWrMemByAdr.__init__()")

        class cClrDiagInfo:
            """
            @class cClrDiagInfo
            @brief The preset value of cClrDiagInfo.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cClrDiagInfo.
                @param None
                @return None
                """

                LogTr("Enter cClrDiagInfo.__init__()")

                LogTr("Exit cClrDiagInfo.__init__()")

        class cRdDtcInfo:
            """
            @class cRdDtcInfo
            @brief The preset value of cRdDtcInfo
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.RptNumOfDtcByStaMsk Report DTC by status mask.
            - "01" Protocol definition value.
            @var self.RptDtcByStaMsk Report Report DTC by status mask.
            - "02" Protocol definition value.
            @var self.RptDtcSnpsId Report DTC Snapshot identifier.
            - "03" Protocol definition value.
            @var self.RptDtcSnpsRecByDtcNum Report DTC Snapshot record by DTC number.
            - "04" Protocol definition value.
            @var self.RptDtcStoDatByRecNum Report DTC stored data by record number.
            - "05" Protocol definition value.
            @var self.RptDtcExtDatRecByDtcNum Report DTC externded data record by DTC number.
            - "06" Protocol definition value.
            @var self.RptNumOfDtcBySevMskRec Report number of DTC by severity mask record.
            - "07" Protocol definition value.
            @var self.RptDtcBySevMskRec Report DTC by severity mask record.
            - "08" Protocol definition value.
            @var self.RptSevInfoOfDtc Report severity information of DTC.
            - "09" Protocol definition value.
            @var self.RptSptDtc Report supported DTC.
            - "0A" Protocol definition value.
            @var self.RptFstTstFailDtc Report first test failed DTC.
            - "0B" Protocol definition value.
            @var self.RptFstCfmDtc Report first confirmed DTC.
            - "0C" Protocol definition value.
            @var self.RptMstRecTstFailDtc Report most recent test failed DTC.
            - "0D" Protocol definition value.
            @var self.RptMstRecCfmDtc Report most recent confirmed DTC.
            - "0E" Protocol definition value.
            @var self.RptMirMemDtcByStaMsk Report mirror memory DTC by status mask.
            - "0F" Protocol definition value.
            @var self.RptMirMemDtcExtDatRecByDtcNum Report mirror memory DTC externded data record by DTC number.
            - "10" Protocol definition value.
            @var self.RptNumOfDtcByStaMsk Report number of DTC by status mask.
            - "11" Protocol definition value.
            @var self.RptNumOfEmisObdDtcByStaMsk Report number of emissions OBD DTC by status mask.
            - "12" Protocol definition value.
            @var self.RptEmisObdDtcByStaMsk Report emissions OBD DTC by status mask.
            - "13" Protocol definition value.
            @var self.RptDtcFltDetCnt Report DTC fault detection counter.
            - "14" Protocol definition value.
            @var self.RptDtcWithPermSta Report DTC with permanent status.
            - "15" Protocol definition value.
            @var self.RptDtcExtDatRecByRecNum Report DTC externded data record by record number.
            - "16" Protocol definition value.
            @var self.RptUsrDefMemDtcByStaMsk Report user define memory DTC by status mask.
            - "17" Protocol definition value.
            @var self.RptUsrDefMemDtcSnpsRecByDtcNum Report user define memory DTC snapshot record by DTC number.
            - "18" Protocol definition value.
            @var self.RptUsrDefMemDtcExtDatRecByDtcNum Report user define memory DTC externded data record by DTC number.
            - "19" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "1A~41" Protocol definition value.
            @var self.RptWwhObdDtcByMskRec Report WWH OBD DTC by mask record.
            - "42" Protocol definition value.
            @var self.IsoRsv2 ISO SAE reserved.
            - "43~54" Protocol definition value.
            @var self.RptWwhObdDtcWithPermSta Report WWH OBD DTC with permanent status.
            - "55" Protocol definition value.
            @var self.IsoRsv2 ISO SAE reserved.
            - "56~7F" Protocol definition value.
            """

            def __init__(self):
                LogTr("Enter cRdDtcInfo.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.Rsv}")
                self.RptNumOfDtcByStaMsk = "01"
                LogDbg(f"self.RptNumOfDtcByStaMsk = {self.RptNumOfDtcByStaMsk}")
                self.RptDtcByStaMsk = "02"
                LogDbg(f"self.RptDtcByStaMsk = {self.RptDtcByStaMsk}")
                self.RptDtcSnpsId = "03"
                LogDbg(f"self.RptDtcSnpsId = {self.RptDtcSnpsId}")
                self.RptDtcSnpsRecByDtcNum = "04"
                LogDbg(f"self.RptDtcSnpsRecByDtcNum = {self.RptDtcSnpsRecByDtcNum}")
                self.RptDtcStoDatByRecNum = "05"
                LogDbg(f"self.RptDtcStoDatByRecNum = {self.RptDtcStoDatByRecNum}")
                self.RptDtcExtDatRecByDtcNum = "06"
                LogDbg(f"self.RptDtcExtDatRecByDtcNum = {self.RptDtcExtDatRecByDtcNum}")
                self.RptNumOfDtcBySevMskRec = "07"
                LogDbg(f"self.RptNumOfDtcBySevMskRec = {self.RptNumOfDtcBySevMskRec}")
                self.RptDtcBySevMskRec = "08"
                LogDbg(f"self.RptDtcBySevMskRec = {self.RptDtcBySevMskRec}")
                self.RptSevInfoOfDtc = "09"
                LogDbg(f"self.RptSevInfoOfDtc = {self.RptSevInfoOfDtc}")
                self.RptSptDtc = "0A"
                LogDbg(f"self.RptSptDtc = {self.RptSptDtc}")
                self.RptFstTstFailDtc = "0B"
                LogDbg(f"self.RptFstTstFailDtc = {self.RptFstTstFailDtc}")
                self.RptFstCfmDtc = "0C"
                LogDbg(f"self.RptFstCfmDtc = {self.RptFstCfmDtc}")
                self.RptMstRecTstFailDtc = "0D"
                LogDbg(f"self.RptMstRecTstFailDtc = {self.RptMstRecTstFailDtc}")
                self.RptMstRecCfmDtc = "0E"
                LogDbg(f"self.RptMstRecCfmDtc = {self.RptMstRecCfmDtc}")
                self.RptMirMemDtcByStaMsk = "0F"
                LogDbg(f"self.RptMirMemDtcByStaMsk = {self.RptMirMemDtcByStaMsk}")
                self.RptMirMemDtcExtDatRecByDtcNum = "10"
                LogDbg(f"self.RptMirMemDtcExtDatRecByDtcNum = {self.RptMirMemDtcExtDatRecByDtcNum}")
                self.RptNumOfMirMemDtcByStaMsk = "11"
                LogDbg(f"self.RptNumOfMirMemDtcByStaMsk = {self.RptNumOfMirMemDtcByStaMsk}")
                self.RptNumOfEmisObdDtcByStaMsk = "12"
                LogDbg(f"self.RptNumOfEmisObdDtcByStaMsk = {self.RptNumOfEmisObdDtcByStaMsk}")
                self.RptEmisObdDtcByStaMsk = "13"
                LogDbg(f"self.RptEmisObdDtcByStaMsk = {self.RptEmisObdDtcByStaMsk}")
                self.RptDtcFltDetCnt = "14"
                LogDbg(f"self.RptDtcFltDetCnt = {self.RptDtcFltDetCnt}")
                self.RptDtcWithPermSta = "15"
                LogDbg(f"self.RptDtcWithPermSta = {self.RptDtcWithPermSta}")
                self.RptDtcExtDatRecByRecNum = "16"
                LogDbg(f"self.RptDtcExtDatRecByRecNum = {self.RptDtcExtDatRecByRecNum}")
                self.RptUsrDefMemDtcByStaMsk = "17"
                LogDbg(f"self.RptUsrDefMemDtcByStaMsk = {self.RptUsrDefMemDtcByStaMsk}")
                self.RptUsrDefMemDtcSnpsRecByDtcNum = "18"
                LogDbg(f"self.RptUsrDefMemDtcSnpsRecByDtcNum = {self.RptUsrDefMemDtcSnpsRecByDtcNum}")
                self.RptUsrDefMemDtcExtDatRecByDtcNum = "19"
                LogDbg(f"self.RptUsrDefMemDtcExtDatRecByDtcNum = {self.RptUsrDefMemDtcExtDatRecByDtcNum}")
                self.IsoRsv1 = "1A~41"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.RptWwhObdDtcByMskRec = "42"
                LogDbg(f"self.RptWwhObdDtcByMskRec = {self.RptWwhObdDtcByMskRec}")
                self.IsoRsv2 = "43~54"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")
                self.RptWwhObdDtcWithPermSta = "55"
                LogDbg(f"self.RptWwhObdDtcWithPermSta = {self.RptWwhObdDtcWithPermSta}")
                self.IsoRsv2 = "56~7F"
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cRdDtcInfo.__init__()")

        class cIoCtrlById:
            """
            @class cIoCtrlById
            @brief The preset value of cIoCtrlById.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cIoCtrlById.
                @param None
                @return None
                """

                LogTr("Enter cIoCtrlById.__init__()")

                LogTr("Exit cIoCtrlById.__init__()")

        class cRtCtrl:
            """
            @class cRtCtrl
            @brief The preset value of cRtCtrl.
            @param None
            @var self.IsoRsv ISO SAE reserved.
            - "00" Protocol definition value.
            @var self.StrtRt Start routine.
            - "01" Protocol definition value.
            @var self.StpRt Stop routine.
            - "02" Protocol definition value.
            @var self.ReqRtRst Request routine results.
            - "03" Protocol definition value.
            @var self.IsoRsv1 ISO SAE reserved.
            - "04~7F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRtCtrl.
                @param None
                @return None
                """

                LogTr("Enter cRtCtrl.__init__()")

                self.IsoRsv = "00"
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.StrtRt = "01"
                LogDbg(f"self.StrtRt = {self.StrtRt}")
                self.StpRt = "02"
                LogDbg(f"self.StpRt = {self.StpRt}")
                self.ReqRtRst = "03"
                LogDbg(f"self.ReqRtRst = {self.ReqRtRst}")
                self.IsoRsv1 = "04~7F"
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                LogTr("Exit cRtCtrl.__init__()")

        class cReqDwnld:
            """
            @class cReqDwnld
            @brief The preset value of cReqDwnld.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cReqDwnld.
                @param None
                @return None
                """

                LogTr("Enter cReqDwnld.__init__()")

                LogTr("Exit cReqDwnld.__init__()")

        class cReqUpld:
            """
            @class cReqUpld
            @brief The preset value of cReqUpld.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cReqUpld.
                @param None
                @return None
                """

                LogTr("Enter cReqUpld.__init__()")

                LogTr("Exit cReqUpld.__init__()")

        class cTxDat:
            """
            @class cTxDat
            @brief The preset value of cTxDat.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cTxDat.
                @param None
                @return None
                """

                LogTr("Enter cTxDat.__init__()")

                LogTr("Exit cTxDat.__init__()")

        class cReqTxEx:
            """
            @class cReqTxEx
            @brief The preset value of cReqTxEx.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cReqTxEx.
                @param None
                @return None
                """

                LogTr("Enter cReqTxEx.__init__()")

                LogTr("Exit cReqTxEx.__init__()")

        class cReqFileTx:
            """
            @class cReqFileTx
            @brief The preset value of cReqFileTx.
            @param None
            @var None
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cReqFileTx.
                @param None
                @return None
                """

                LogTr("Enter cReqFileTx.__init__()")

                LogTr("Exit cReqFileTx.__init__()")

        def __init__(self):
            """
            @fn cSubFun
            @brief Constructor for class cSubFun.
            @param None
            @return None
            """

            LogTr("Enter cSubFun.__init__()")

            self.DiagSessCtrl = self.cDiagSessCtrl()
            LogDbg(f"self.DiagSessCtrl = {self.DiagSessCtrl}")
            self.EcuRst = self.cEcuRst()
            LogDbg(f"self.EcuRst = {self.EcuRst}")
            self.SecAcc = self.cSecAcc()
            LogDbg(f"self.SecAcc = {self.SecAcc}")
            self.CommCtrl = self.cCommCtrl()
            LogDbg(f"self.CommCtrl = {self.CommCtrl}")
            self.TstrPrsnt = self.cTstrPrsnt()
            LogDbg(f"self.TstrPrsnt = {self.TstrPrsnt}")
            self.AccTmParam = self.cAccTmParam()
            LogDbg(f"self.AccTmParam = {self.AccTmParam}")
            self.SecdDatTx = self.cSecdDatTx()
            LogDbg(f"self.SecdDatTx = {self.SecdDatTx}")
            self.CtrlDtcSet = self.cCtrlDtcSet()
            LogDbg(f"self.CtrlDtcSet = {self.CtrlDtcSet}")
            self.RespOnEvt = self.cRespOnEvt()
            LogDbg(f"self.RespOnEvt = {self.RespOnEvt}")
            self.LnkCtrl = self.cLnkCtrl()
            LogDbg(f"self.LnkCtrl = {self.LnkCtrl}")
            self.RdDatById = self.cRdDatById()
            LogDbg(f"self.RdDatById = {self.RdDatById}")
            self.RdMemByAdr = self.cRdMemByAdr()
            LogDbg(f"self.RdMemByAdr = {self.RdMemByAdr}")
            self.RdScDatById = self.cRdScDatById()
            LogDbg(f"self.RdScDatById = {self.RdScDatById}")
            self.RdDatByPerId = self.cRdDatByPerId()
            LogDbg(f"self.RdDatByPerId = {self.RdDatByPerId}")
            self.DynDefDatId = self.cDynDefDatId()
            LogDbg(f"self.DynDefDatId = {self.DynDefDatId}")
            self.WrDatById = self.cWrDatById()
            LogDbg(f"self.WrDatById = {self.WrDatById}")
            self.WrMemByAdr = self.cWrMemByAdr()
            LogDbg(f"self.WrMemByAdr = self.WrMemByAdr")
            self.ClrDiagInfo = self.cClrDiagInfo()
            LogDbg(f"self.ClrDiagInfo = {self.ClrDiagInfo}")
            self.RdDtcInfo = self.cRdDtcInfo()
            LogDbg(f"self.RdDtcInfo = {self.RdDtcInfo}")
            self.IoCtrlById = self.cIoCtrlById()
            LogDbg(f"self.IoCtrlById = {self.IoCtrlById}")
            self.RtCtrl = self.cRtCtrl()
            LogDbg(f"self.RtCtrl = {self.RtCtrl}")
            self.ReqDwnld = self.cReqDwnld()
            LogDbg(f"self.ReqDwnld = {self.ReqDwnld}")
            self.ReqUpld = self.cReqUpld()
            LogDbg(f"self.ReqUpld = {self.ReqUpld}")
            self.TxDat = self.cTxDat()
            LogDbg(f"self.TxDat = {self.TxDat}")
            self.ReqTxEx = self.cReqTxEx()
            LogDbg(f"self.ReqTxEx = {self.ReqTxEx}")
            self.ReqFileTx = self.cReqFileTx()
            LogDbg(f"self.ReqFileTx = {self.ReqFileTx}")

            LogTr("Exit cSubFun.__init__()")

    class cNrc:
        """
        @class cNrc
        @brief The preset value of cNrc.
        @param None
        @var self.DiagSessCtrl Diagnostic session control.
        @var self.EcuRst Ecu reset.
        @var self.SecAcc Security access.
        @var self.CommCtrl Communication control.
        @var self.TstrPrsnt Tester present.
        @var self.AccTmParam Access timing parameter.
        @var self.SecdDatTx Secured data transmission.
        @var self.CtrlDtcSet Control dtc setting.
        @var self.RespOnEvt Response on event.
        @var self.LinkCtrl Link control.
        @var self.RdDatById Read data by identifier.
        @var self.RdMemByAdr Read memory by address.
        @var self.RdScDatById Read scaling data by identifier.
        @var self.RdDatByPerId Read data by periodic identifier.
        @var self.DynDefDatId Dynamically define data identifier.
        @var self.WrDatById Write data by identifier.
        @var self.WrMemByAdr Write memory by address.
        @var self.ClrDiagInfo Clear diagnostic information.
        @var self.RdDtcInfo Read dtc information.
        @var self.IoCtrlById Input out put control by identifier.
        @var self.RtCtrl Routine control.
        @var self.ReqDwnld Request download.
        @var self.ReqUpld Request upload.
        @var self.TxDat Transfer data.
        @var self.ReqTxEx Request transfer exit.
        @var self.ReqFileTx Request file transfer.
        """

        class cDiagSessCtrl:
            """
            @class cDiagSessCtrl
            @brief The preset value of cDiagSessCtrl.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Conditions not correct.
            - "22" Protocol definition value.
            """
            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cDiagSessCtrl.
                @param None
                @return None
                """

                LogTr("Enter cDiagSessCtrl.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")

                LogTr("Exit cDiagSessCtrl.__init__()")

        class cEcuRst:
            """
            @class cEcuRst
            @brief The preset value of cEcuRst.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cEcuRst.
                @param None
                @return None
                """

                LogTr("Enter cEcuRst.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cEcuRst.__init__()")

        class cSecAcc:
            """
            @class cSecAcc
            @brief The preset value of cSecAcc.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition negative correct.
            - "22" Protocol definition value.
            @var self.ReqSeqErr Request sequence error.
            - "24" Protocol definition value.
            @var self.ReqOtRng Request Out of range.
            - "31" Protocol definition value.
            @var self.InvKey Invalid key.
            - "35" Protocol definition value.
            @var self.Exceeded number of attempts.
            - "36" Protocol definition value.
            @var self.ReqTmDlyNExp Request time delay not expired.
            - "37" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cSecAcc.
                @param None
                @return None
                """

                LogTr("Enter cSecAcc.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqSeqErr = "24"
                LogDbg(f"self.ReqSeqErr = {self.ReqSeqErr}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.InvKey = "35"
                LogDbg(f"self.InvKey = {self.InvKey}")
                self.ExcNumAtpt = "36"
                LogDbg(f"self.ExcNumAtpt = {self.ExcNumAtpt}")
                self.ReqTmDlyNExp = "37"
                LogDbg(f"self.ReqTmDlyNExp = {self.ReqTmDlyNExp}")

                LogTr("Exit cSecAcc.__init__()")

        class cCommCtrl:
            """
            @class cCommCtrl
            @brief The preset value of cCommCtrl.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cCommCtrl.
                @param None
                @return None
                """

                LogTr("Enter cCommCtrl.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cCommCtrl.__init__()")

        class cTstrPrsnt:
            """
            @class cTstrPrsnt
            @brief The preset value of cTstrPrsnt.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cTstrPrsnt.
                @param None
                @return None
                """

                LogTr("Enter cTstrPrsnt.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")

                LogTr("Exit cTstrPrsnt.__init__()")

        class cAccTmParam:
            """
            @class cAccTmParam
            @brief The preset value of cAccTmParam.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cAccTmParam.
                @param None
                @return None
                """

                LogTr("Enter cAccTmParam.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cAccTmParam.__init__()")

        class cSecdDatTx:
            """
            @class cSecdDatTx
            @brief The preset value of cSecdDatTx.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.RsvdByExtDatLnkSecDoc Reserved by externded data link security document.
            - "38~4F" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cSecdDatTx.
                @param None
                @return None
                """

                LogTr("Enter cSecdDatTx.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.RsvdByExtDatLnkSecDoc = "38~4F"
                LogDbg(f"self.RsvdByExtDatLnkSecDoc = {self.RsvdByExtDatLnkSecDoc}")

                LogTr("Exit cSecdDatTx.__init__()")

        class cCtrlDtcSet:
            """
            @class cCtrlDtcSet
            @brief The preset value cCtrlDtcSet.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            """

            def __init__(self):
                """
                @fn cCtrlDtcSet
                @brief Constructor for class cCtrlDtcSet.
                @param None
                @return None
                """

                LogTr("Enter cCtrlDtcSet.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cCtrlDtcSet.__init__()")

        class cRespOnEvt:
            """
            @class cRespOnEvt
            @brief Constructor for class cRespOnEvt.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRespOnEvt.
                @param None
                @return None
                """

                LogTr("Enter cRespOnEvt.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cRespOnEvt.__init__()")

        class cLnkCtrl:
            """
            @class cLnkCtrl
            @brief The preset value of cLnkCtrl.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqSeqErr Request sequence error.
            - "24" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cLnkCtrl.
                @param None
                @return None
                """

                LogTr("Enter cLnkCtrl.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqSeqErr = "24"
                LogDbg(f"self.ReqSeqErr = {self.ReqSeqErr}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cLnkCtrl.__init__()")

        class cRdDatById:
            """
            @class cRdDatById
            @brief The preset value of cRdDatById.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.RespTooLng Response too length.
            - "14" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdDatById.
                @param None
                @return None
                """

                LogTr("Enter cRdDatById.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.RespTooLng = "14"
                LogDbg(f"self.RespTooLng = {self.RespTooLng}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cRdDatById.__init__()")

        class cRdMemByAdr:
            """
            @class cRdMemByAdr
            @brief The preset value of cRdMemByAdr.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdMemByAdr.
                @param None
                @return None
                """

                LogTr("Enter cRdMemByAdr.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cRdMemByAdr.__init__()")

        class cRdScDatById:
            """
            @class cRdScDatById
            @brief The preset value of cRdScDatById.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            """

            def __init__(self):
                """
                @fn cRdScDatById
                @brief Constructor for class cRdScDatById.
                @param None
                @return None
                """

                LogTr("Enter cRdScDatById.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cRdScDatById.__init__()")

        class cRdDatByPerId:
            """
            @class cRdDatByPerId
            @brief The preset value of cRdDatByPerId.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cRdDatByPerId.
                @param None
                @return None
                """

                LogTr("Enter cRdDatByPerId.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cRdDatByPerId.__init__()")

        class cDynDefDatId:
            """
            @class cDynDefDatId
            @brief The preset value of cDynDefDatId.
            @param None
            @var self.SubFunNSpt Subfunction not supported.
            - "12" Protocol definition value.
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cDynDefDatId.
                @param None
                @return None
                """

                LogTr("Enter cDynDefDatId.__init__()")

                self.SubFunNSpt = "12"
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cDynDefDatId.__init__()")

        class cWrDatById:
            """
            @class cWrDatById
            @brief The preset value of cWrDatById.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            @var self.GenProgFail General Programming failure.
            - "72" Protocol definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cWrDatById.
                @param None
                @return None
                """

                LogTr("Enter cWrDatById.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = self.CndNCor")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")
                self.GenProgFail = "72"
                LogDbg(f"self.GenProgFail = {self.GenProgFail}")

                LogTr("Exit cWrDatById.__init__()")

        class cWrMemByAdr:
            """
            @class cWrMemByAdr
            @brief The preset value of cWrMemByAdr.
            @param None
            @var self.IncorMsgLenOrInvFmt Incorrect message length or invalid format.
            - "13" Protocol definition value.
            @var self.CndNCor Condition not correct.
            - "22" Protocol definition value.
            @var self.ReqOtRng Request out of range.
            - "31" Protocol definition value.
            @var self.SecAccD Security access denied.
            - "33" Protocol definition value.
            @var self.GenProgFail General Programming failure.
            - "72" Programming definition value.
            """

            def __init__(self):
                """
                @fn __init__
                @brief Constructor for class cWrMemByAdr.
                @param None
                @return None
                """

                LogTr("Enter cWrMemByAdr.__init__()")

                self.IncorMsgLenOrInvFmt = "13"
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22"
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31"
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33"
                LogDbg(f"self.SecAccD = {self.SecAccD}")
                self.GenProgFail = "72"
                LogDbg(f"self.GenProgFail = {self.GenProgFail}")

                LogTr("Exit cWrMemByAdr.__init__()")

        def __init__(self):
            """
            @fn __init__
            @brief Constructor for class cNrc.
            @param None
            @return None
            """

            LogTr("Enter cNrc.__init__()")

            self.DiagSessCtrl = self.cDiagSessCtrl()
            LogDbg(f"self.DiagSessCtrl = {self.DiagSessCtrl}")
            self.EcuRst = self.cEcuRst()
            LogDbg(f"self.EcuRst = {self.EcuRst}")
            self.SecAcc = self.cSecAcc()
            LogDbg(f"self.SecAcc = {self.SecAcc}")
            self.CommCtrl = self.cCommCtrl()
            LogDbg(f"self.CommCtrl = {self.CommCtrl}")
            self.TstrPrsnt = self.cTstrPrsnt()
            LogDbg(f"self.TstrPrsnt = {self.TstrPrsnt}")
            self.AccTmParam = self.cAccTmParam()
            LogDbg(f"self.AccTmParam = {self.AccTmParam}")
            self.SecdDatTx = self.cSecdDatTx()
            LogDbg(f"self.SecdDatTx = {self.SecdDatTx}")
            self.CtrlDtcSet = self.cCtrlDtcSet()
            LogDbg(f"self.CtrlDtcSet = {self.CtrlDtcSet}")
            self.RespOnEvt = self.cRespOnEvt()
            LogDbg(f"self.RespOnEvt = {self.RespOnEvt}")
            self.LnkCtrl = self.cLnkCtrl()
            LogDbg(f"self.LnkCtrl = {self.LnkCtrl}")
            self.RdDatById = self.cRdDatById()
            LogDbg(f"self.RdDatById = {self.RdDatById}")
            self.RdMemByAdr = self.cRdMemByAdr()
            LogDbg(f"self.RdMemByAdr = {self.RdMemByAdr}")
            self.RdScDatById = self.cRdScDatById()
            LogDbg(f"self.RdScDatById = {self.RdScDatById}")
            self.RdDatByPerId = self.cRdDatByPerId()
            LogDbg(f"self.RdDatByPerId = {self.RdDatByPerId}")
            self.DynDefDatId = self.cDynDefDatId()
            LogDbg(f"self.DynDefDatId = {self.DynDefDatId}")
            self.WrDatById = self.cWrDatById()
            LogDbg(f"self.WrDatById = {self.WrDatById}")
            self.WrMemByAdr = self.cWrMemByAdr()
            LogDbg(f"self.WrMemByAdr = {self.WrMemByAdr}")
            self.ClrDiagInfo = self.cClrDiagInfo()
            LogDbg(f"self.ClrDiagInfo = {self.ClrDiagInfo}")
            self.RdDtcInfo = self.cRdDtcInfo()
            LogDbg(f"self.RdDtcInfo = {self.RdDtcInfo}")
            self.IoCtrlById = self.cIoCtrlById()
            LogDbg(f"self.IoCtrlById = {self.IoCtrlById}")
            self.RtCtrl = self.cRtCtrl()
            LogDbg(f"self.RtCtrl = {self.RtCtrl}")
            self.ReqDwnld = self.cReqDwnld()
            LogDbg(f"self.ReqDwnld = {self.ReqDwnld}")
            self.ReqUpld = self.cReqUpld()
            LogDbg(f"self.ReqUpld = {self.ReqUpld}")
            self.TxDat = self.cTxDat()
            LogDbg(f"self.TxDat = {self.TxDat}")
            self.ReqTxEx = self.cReqTxEx()
            LogDbg(f"self.ReqTxEx = {self.ReqTxEx}")
            self.ReqFileTx = self.cReqFileTx()
            LogDbg(f"self.ReqFileTx = {self.ReqFileTx}")

            LogTr("Exit cNrc.__init__()")

    def __init__(self):
        """
        @fn __init__
        @brief Constructor for class cMsgPset.
        @param None
        @return None
        """

        LogTr("Enter cMsgPset.__init__()")

        self.Sid = self.cSid()
        self.SubFun = self.cSubFun()
        self.Nrc = self.cNrc()

        LogTr("Exit cMsgPset.__init__()")

class cUdsSer:
    """
    @class cUdsSer
    @brief Constructor for class cUdsSer.
    @param None
    @var self.DoipSer DoIP server.
    """

    def __init__(self):
        """
        @fn __init__
        @brief Constructor for class cUdsSer.
        @param None
        @return None
        """

        LogTr("Enter cUdsSer.__init__()")

        self.DoipSer = cDoipSer()

        LogTr("Exit cUdsSer.__init__()")

    def IsRecvBufMty(self):
        """
        @fn IsRecvBufMty
        @brief Check if the UDS receive buffer is empty.
        @param None
        @return BufSta Receive buffer status.
        @retval True UDS receive buffer is empty.
        @retval False UDS receive buffer is non empty.
        """

        # LogTr("Enter cUdsSer.IsRecvBufMty()")

        BufSta = self.DoipSer.IsRecvBufMty()
        # LogDbg(f"BufSta = {BufSta}")

        # LogTr("Exit cUdsSer.IsRecvBufMty()")

        return BufSta

    def ReqDiag(self):
        """
        @fn ReqDiag
        @brief Get UDS request diagnostic message.
        @param None
        @return Msg UDS message.
        """

        LogTr("Enter cUdsSer.ReqDiag()")

        Msg = self.DoipSer.Recv()
        LogDbg(f"Msg = {Msg}")

        LogTr("Exit cUdsSer.ReqDiag()")

        return Msg

    def PrsMsg(self, Msg):
        """
        @fn PrsMsg
        @brief Parsing UDS message.
        @param Msg UDS message.
        @return PlTyp Payload type.
        @return Pl Payload.
        """

        LogTr("Enter cUdsSer.PrsMsg")

        LogDbg(f"Msg = {Msg}")

        PlTyp, Pl = self.DoipSer.Msg.PrsPl(Msg)
        LogDbg(f"PlTyp = {PlTyp}")
        LogDbg(f"Pl = {Pl}")

        LogTr("Exit cUdsSer.PrsMsg")

        return PlTyp, Pl

    def PrsPlDiag(self, Pl):
        """
        @fn PrsPlDiag
        @brief Parsing payload diagnostic.
        @param[in] Pl Payload message.
        @return SrcAdr Source address.
        @return TgtAdr Target address.
        @return UsrDat User data.
        """

        LogTr("Enter cUdsSer.PrsPlDiag")

        LogDbg(f"Pl = {Pl}")

        SrcAdr, TgtAdr, UsrDat = self.DoipSer.Msg.Pl.PrsPlDiag(Pl)
        LogDbg(f"SrcAdr = {SrcAdr}")
        LogDbg(f"TgtAdr = {TgtAdr}")
        LogDbg(f"UsrDat = {UsrDat}")

        LogTr("Exit cUdsSer.PrsPlDiag")

        return SrcAdr, TgtAdr, UsrDat

    def RespDiag(self, Msg):
        """
        @fn RespDiag
        @brief UDS response diagnostic message.
        @param[in] Msg Response diagnostic message.
        @return None
        """

        LogTr("Enter cUdsSer.RespDiag")

        LogDbg(f"Msg = {Msg}")

        self.DoipSer.RespPosDiag("00")
        self.DoipSer.RespDiagMsg(Msg)

        LogTr("Exit cUdsClt.RespDiag")

class cUdsClt:
    """
    @class cUdsClt
    @brief The preset value of cUdsClt.
    @param None
    @var self.DoipClt DoIP clent.
    """

    def __init__(self):
        """
        @fn __init__
        @brief Constructor for class cUdsClt
        @param None
        @return None
        """

        LogTr("Enter cUdsClt.__init__()")

        self.DoipClt = cDoipClt()

        LogTr("Exit cUdsClt.__init__()")

    def ReqDiag(self, Msg):
        """
        @fn ReqDiag
        @brief UDS client request diagnosis.
        @param Msg UDS send message.
        @return None
        """

        LogTr("Enter cUdsClt.ReqDiag()")

        self.DoipClt.ReqDiag(Msg)

        LogTr("Exit cUdsClt.ReqDiag()")

    def RespDiag(self):
        """
        @fn RespDiag
        @brief UDS client receive message.
        @param None
        @return Receive message.
        """

        LogTr("Enter cUdsClt.RespDiag()")

        PlTyp, AckCode = self.DoipClt.RespAckDiag()
        LogDbg(f"PlTyp = {PlTyp}")
        LogDbg(f"AckCode = {AckCode}")

        if PlTyp == self.DoipClt.MsgPset.Hdr.PlTyp.DiagMsgPosAck:
            LogTr("Positive diagnostic response.")

            PlTyp, UsrDat = self.DoipClt.RespDiagMsg()
            LogDbg(f"PlTyp = {PlTyp}")
            LogDbg(f"UsrDat = {UsrDat}")
        elif PlTyp == self.DoipClt.MsgPset.Hdr.PlTyp.DiagMsgNegAck:
            LogTr("Negative diagnostic response.")

            pass

        LogTr("Exit cUdsClt.RespDiag()")

        return PlTyp, AckCode, UsrDat

def ImitUdsSer():
    """
    @fn ImitUdsSer
    @brief Imitate UDS server.
    @param None
    @return None
    """

    LogTr("Enter ImitUdsSer.")

    Ecu = cUdsSer()
    Ecu.DoipSer.LsnRteAct()

    while True:
        if Ecu.IsRecvBufMty() == False:
            RecvMsg = Ecu.ReqDiag()
            LogDbg(f"RecvMsg: {RecvMsg}")

            if RecvMsg != "":
                PlTyp, Pl = Ecu.PrsMsg(RecvMsg)

                if PlTyp == Ecu.DoipSer.MsgPset.Hdr.PlTyp.RteActReq:
                    LogTr("Routing activation request.")
                    SrcAdr, ActTyp, Rsv, OemSpec = Ecu.DoipSer.Msg.Pl.PrsPlRteActReq(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"ActTyp = {ActTyp}")
                    LogDbg(f"Rsv = {Rsv}")
                    LogDbg(f"OemSpec = {OemSpec}")
                    Ecu.DoipSer.TgtAdr = SrcAdr
                    LogDbg(f"Ecu.DoipSer.TgtAdr = {Ecu.DoipSer.TgtAdr}")

                    Ecu.DoipSer.RespRteAct()
                elif PlTyp == Ecu.DoipSer.MsgPset.Hdr.PlTyp.DiagMsg:
                    LogTr("Diagnostic message.")
                    SrcAdr, TgtAdr, UsrDat = Ecu.PrsPlDiag(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"TgtAdr = {TgtAdr}")
                    LogDbg(f"UsrDat = {UsrDat}")

                    Ecu.RespDiag("5003003201F4")

    LogTr("Exit ImitUdsSer.")

def ImitUdsClt():
    """
    @fn ImitUdsClt
    @brief Imitate UDS client.
    @param None
    @return None
    """

    LogTr("Enter ImitUdsClt.")

    Tstr = cUdsClt()
    Tstr.DoipClt.ReqRteAct()
    Tstr.DoipClt.RespRteAct()
    Tstr.ReqDiag("1003")
    PlTyp, AckCode, UsrDat = Tstr.RespDiag()
    LogDbg(f"PlTyp = {PlTyp}")
    LogDbg(f"AckCode = {AckCode}")
    LogDbg(f"UsrDat = {UsrDat}")

    LogTr("Exit ImitUdsClt.")

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        ImitUdsSer()
    elif sys.argv[1] == "-Clt":
        ImitUdsClt()
