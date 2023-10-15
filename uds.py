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
    # ISO 14229-1-2013.
    # UDS message structure.

    class cSid:
        def __init__(self):
            LogTr("Enter cSid.__init__()")

            self.DiagSessCtrl = "10" # 0x10: Diagnostic session control.
            LogDbg(f"self.DiagSessCtrl = {self.DiagSessCtrl}")
            self.EcuRst = "11" # 0x11: ECU reset.
            LogDbg(f"self.EcuRst = {self.EcuRst}")
            self.SecAcc = "27" # 0x27: Security access.
            LogDbg(f"self.SecAcc = {self.SecAcc}")
            self.CommCtrl = "28" # 0x28: Communication control.
            LogDbg(f"self.CommCtrl = {self.CommCtrl}")
            self.TstrPrsnt = "3E" # 0x3E: Tester present.
            LogDbg(f"self.TstrPrsnt = {self.TstrPrsnt}")
            self.AccTmParam = "83" # 0x83: Access timing parameter.
            LogDbg(f"self.AccTmParam = {self.AccTmParam}")
            self.SecdDatTx = "84" # 0x84: Secured data transmission.
            LogDbg(f"self.SecdDatTx = {self.SecdDatTx}")
            self.CtrlDtcSet = "85" # 0x85: Ctrl DTC setting.
            LogDbg(f"self.CtrlDtcSet = {self.CtrlDtcSet}")
            self.RespOnEvt = "86" # 0x86: Response on event.
            LogDbg(f"self.RespOnEvt = {self.RespOnEvt}")
            self.LinkCtrl = "87" # 0x87: Link control.
            LogDbg(f"self.LinkCtrl = {self.LinkCtrl}")
            self.RdDatById = "22" # 0x22: Read data by identifier.
            LogDbg(f"self.RdDatById = {self.RdDatById}")
            self.RdMemoryByAddress = "23" # 0x23: Read memory by address.
            LogDbg(f"self.RdMemoryByAddress = {self.RdMemoryByAddress}")
            self.RdScalingDatById = "24" # 0x24: Read scaling data by identifier.
            LogDbg(f"self.RdScalingDatById = {self.RdScalingDatById}")
            self.RdDatByPerId = "2A" # 0x2A: Read data by periodic identifier.
            LogDbg(f"self.RdDatByPerId = {self.RdDatByPerId}")
            self.DynDefDatId = "2C" # 0x2C: Dynamically define data identifier.
            LogDbg(f"self.DynDefDatId = {self.DynDefDatId}")
            self.WrDatById = "2E" # 0x2E: Write data by identifier.
            LogDbg(f"self.WrDatById = {self.WrDatById}")
            self.WrMemByAdr = "3D" # 0x3D: Write memory by address.
            LogDbg(f"self.WrMemByAdr = {self.WrMemByAdr}")
            self.ClrDiagInfo = "14" # 0x14: Clear diagnostic information.
            LogDbg(f"self.ClrDiagInfo = {self.ClrDiagInfo}")
            self.RdDtcInfo = "19" # 0x19: Read DTC information.
            LogDbg(f"self.RdDtcInfo = {self.RdDtcInfo}")
            self.IoCtrlById = "2F" # 0x2F: Input out put control by identifier.
            LogDbg(f"self.IoCtrlById = {self.IoCtrlById}")
            self.RtCtrl = "31" # 0x31: Routine control.
            LogDbg(f"self.RtCtrl = {self.RtCtrl}")
            self.ReqDwnld = "34" # 0x34: Request download.
            LogDbg(f"self.ReqDwnld = {self.ReqDwnld}")
            self.ReqUpld = "35" # 0x35: Request upload.
            LogDbg(f"self.ReqUpld = {self.ReqUpld}")
            self.TxDat = "36" # 0x36: Transfer data.
            LogDbg(f"self.TxDat = {self.TxDat}")
            self.ReqTxEx = "37" # 0x37: Request transfer exit.
            LogDbg(f"self.ReqTxEx = {self.ReqTxEx}")
            self.ReqFileTx = "38" # 0x38: Request file transfer.
            LogDbg(f"self.ReqFileTx = {self.ReqFileTx}")

            LogTr("Exit cSid.__init__()")

    class cSubFun:
        class cDiagSessCtrl:
            def __init__(self):
                LogTr("Enter cDiagSessCtrl.__init__()")

                self.IsoRsv = "00" # 0x00: ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.Dflt = "01" # 0x01: defaultSession.
                LogDbg(f"self.Dflt = {self.Dflt}")
                self.ProgSess = "02" # 0x02: ProgrammingSession.
                LogDbg(f"self.ProgSess = {self.ProgSess}")
                self.ExtDiagSess = "03" # 0x03: extendedDiagnosticSession.
                LogDbg(f"self.ExtDiagSess = {self.ExtDiagSess}")
                self.SafSysDiagSess = "04" # 0x04: safetySystemDiagnosticSession.
                LogDbg(f"self.SafSysDiagSess = {self.SafSysDiagSess}")
                self.IsoRsv1 = "05~3F" # 0x05~3F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F" # 0x40~5F: vehicleManufacturerSpecific.
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E" # 0x60~7E: systemSupplierSpecific.
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F" # 0x7F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cDiagSessCtrl.__init__()")

        class cEcuRst:
            def __init__(self):
                LogTr("Enter cEcuRst.__init__()")

                self.IsoRsv = "00" # 0x00: ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.HrdRst = "01" # 0x01: hardReset.
                LogDbg(f"self.HrdRst = {self.HrdRst}")
                self.KeyOffOnRst = "02" # 0x02: keyOffOnReset.
                LogDbg(f"self.KeyOffOnRst = {self.KeyOffOnRst}")
                self.SftRst = "03" # 0x03: softReset.
                LogDbg(f"self.SftRst = {self.SftRst}")
                self.EnRpdPwSd = "04" # 0x04: enableRapidPowerShutDown.
                LogDbg(f"self.EnRpdPwSd = {self.EnRpdPwSd}")
                self.DisRpdPwSd = "05" # 0x05: disableRapidPowerShutDown.
                LogDbg(f"self.DisRpdPwSd = {self.DisRpdPwSd}")
                self.IsoRsv1 = "06~3F" # 0x06~3F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F" # 0x40~5F: vehicleManufacturerSpecific.
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E" # 0x60~7E: systemSupplierSpecific.
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F" # 0x7F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cEcuRst.__init__()")

        class cSecAcc:
            def __init__(self):
                LogTr("Enter cSecAcc.__init__()")

                self.IsoRsv = "00" # 0x00: ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.ReqSed = "01" # 0x01: requestSeed.
                LogDbg(f"self.ReqSed = {self.ReqSed}")
                self.SndKey = "02" # 0x02: sendKey.
                LogDbg(f"self.SndKey = {self.SndKey}")
                self.VhcReqSed = "03, 05, 07~41" # 0x03, 0x05, 0x07~41: requestSeed.
                LogDbg(f"self.VhcReqSed = {self.VhcReqSed}")
                self.VhcSndKey = "04, 06, 08~42" # 0x04, 0x06, 0x08~42: sendKey.
                LogDbg(f"self.VhcSndKey = {self.VhcSndKey}")
                self.IsoRsv1 = "43~5E" # 0x43~5E: ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.Iso26021 = "5F" # 0x5F: ISO26021-2 values.
                LogDbg(f"self.Iso26021 = {self.Iso26021}")
                self.Iso26021SndKey = "60" # 0x60: ISO26021-2 sendKey values.
                LogDbg(f"self.Iso26021SndKey = {self.Iso26021SndKey}")
                self.SysSplrSpec = "61~7E" # 0x61~7E: systemSupplierSpecific.
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F" # 0x7F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cSecAcc.__init__()")

        class cCommCtrl:
            def __init__(self):
                LogTr("Enter cCommCtrl.__init__()")

                self.EnRxTx = "00" # 0x00: enableRxAndTx.
                LogDbg(f"self.EnRxTx = {self.EnRxTx}")
                self.EnRxDisTx = "01" # 0x01: enableRxAndDisableTx.
                LogDbg(f"self.EnRxDisTx = {self.EnRxDisTx}")
                self.DisRxEnTx = "02" # 0x02: disableRxAndEnableTx.
                LogDbg(f"self.DisRxEnTx = {self.DisRxEnTx}")
                self.DisRxTx = "03" # 0x03: disableRxAndTx.
                LogDbg(f"self.DisRxTx = {self.DisRxTx}")
                self.EnRxDisTxWithEnhncAdrInfo = "04" # 0x04: enableRxAndDisableTxWithEnhancedAddressInformation.
                LogDbg(f"self.EnRxDisTxWithEnhncAdrInfo = {self.EnRxDisTxWithEnhncAdrInfo}")
                self.EnRxTxWithEnhncAdrInfo = "05" # 0x05: enableRxAndTxWithEnhancedAddressInformationa.
                LogDbg(f"self.EnRxTxWithEnhncAdrInfo = {self.EnRxTxWithEnhncAdrInfo}")
                self.IsoRsv = "06~3F" # 0x06~3F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.VhcMfrSpec = "40~5F" # 0x40~5F: vehicleManufacturerSpecific.
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E" # 0x60~7E: systemSupplierSpecific.
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv1 = "7F" # 0x7F: ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                LogTr("Exit cCommCtrl.__init__()")

        class cTstrPrsnt:
            def __init__(self):
                LogTr("Enter cTstrPrsnt.__init__()")

                self.ZSubFun = "00" # zeroSubFunction.
                LogDbg(f"self.ZSubFun = {self.ZSubFun}")
                self.IsoRsv = "01~7F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                LogTr("Exit cTstrPrsnt.__init__()")

        class cAccTmParam:
            def __init__(self):
                LogTr("Enter cAccTmParam.__init__()")

                self.IsoRsv = "00" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.RdExtdTmParamSet = "01" # readExtendedTimingParameterSet.
                LogDbg(f"self.RdExtdTmParamSet = {self.RdExtdTmParamSet}")
                self.SetTmParamToDfltVal = "02" # setTimingParametersToDefaultValues.
                LogDbg(f"self.SetTmParamToDfltVal = {self.SetTmParamToDfltVal}")
                self.RdCurrActTmParam = "03" # readCurrentlyActiveTimingParameters.
                LogDbg(f"self.RdCurrActTmParam = {self.RdCurrActTmParam}")
                self.SetTmParamToGvnVal = "04" # setTimingParametersToGivenValues.
                LogDbg(f"self.SetTmParamToGvnVal = {self.SetTmParamToGvnVal}")
                self.IsoRsv = "05~FF" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")

                LogTr("Exit cAccTmParam.__init__()")

        class cSecdDatTx:
            def __init__(self):
                LogTr("Enter cSecdDatTx.__init__()")

                self.IsoRsv = "00" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.On = "01" # on.
                LogDbg(f"self.On = {self.On}")
                self.Off = "02" # off.
                LogDbg(f"self.Off = {self.Off}")
                self.IsoRsv1 = "03~3F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F" # vehicleManufacturerSpecific.
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E" # systemSupplierSpecific.
                LogDbg(f"self.systemSupplierSpecific = {self.systemSupplierSpecific}")
                self.IsoRsv2 = "7F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cSecdDatTx.__init__()")

        class cCtrlDtcSet:
            def __init__(self):
                LogTr("Enter cCtrlDtcSet.__init__()")

                LogTr("Exit cCtrlDtcSet.__init__()")

        class cRespOnEvt:
            def __init__(self):
                LogTr("Enter cRespOnEvt.__init__()")

                self.StpRespOnEvt = "00" # stopResponseOnEvent.
                LogDbg(f"self.StpRespOnEvt = {self.StpRespOnEvt}")
                self.OnDtcStsChg = "01" # onDTCStatusChange.
                LogDbg(f"self.OnDtcStsChg = {self.OnDtcStsChg}")
                self.OnTmIntr = "02" # onTimerInterrupt.
                LogDbg(f"self.OnTmIntr = {self.OnTmIntr}")
                self.OnChgOfDatId = "03" # onChangeOfDataIdentifier.
                LogDbg(f"self.OnChgOfDatId = {self.OnChgOfDatId}")
                self.RptActEvt = "04" # reportActivatedEvents.
                LogDbg(f"self.RptActEvt = {self.RptActEvt}")
                self.StrtRespOnEvt = "05" # startResponseOnEvent.
                LogDbg(f"self.StrtRespOnEvt = {self.StrtRespOnEvt}")
                self.ClrRespOnEvt = "06" # clearResponseOnEvent.
                LogDbg(f"self.ClrRespOnEvt = {self.ClrRespOnEvt}")
                self.OnCompOfVal = "07" # onComparisonOfValues.
                LogDbg(f"self.OnCompOfVal = {self.OnCompOfVal}")
                self.IsoRsv = "08~1F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.VhcMfrSpec = "20~2F" # VehicleManufacturerSpecific.
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "30~3E" # SystemSupplierSpecific.
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv1 = "3F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")

                LogTr("Exit cRespOnEvt.__init__()")

        class cLnkCtrl:
            def __init__(self):
                LogTr("Enter cLnkCtrl.__init__()")

                self.IsoRsv = "00" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv = {self.IsoRsv}")
                self.VfyMoTransWFixParam = "01" # verifyModeTransitionWithFixedParameter.
                LogDbg(f"self.VfyMoTransWFixParam = {self.VfyMoTransWFixParam}")
                self.VfyMoTransWSpecParam = "02" # verifyModeTransitionWithSpecificParameter.
                LogDbg(f"self.VfyMoTransWSpecParam")
                self.TransMo = "03" # transitionMode.
                LogDbg(f"self.TransMo = {self.TransMo}")
                self.IsoRsv1 = "04~3F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv1 = {self.IsoRsv1}")
                self.VhcMfrSpec = "40~5F" # vehicleManufacturerSpecific.
                LogDbg(f"self.VhcMfrSpec = {self.VhcMfrSpec}")
                self.SysSplrSpec = "60~7E" # systemSupplierSpecific.
                LogDbg(f"self.SysSplrSpec = {self.SysSplrSpec}")
                self.IsoRsv2 = "7F" # ISOSAEReserved.
                LogDbg(f"self.IsoRsv2 = {self.IsoRsv2}")

                LogTr("Exit cLnkCtrl.__init__()")

        class cRdDatById:
            def __init__(self):
                LogTr("Enter cRdDatById.__init__()")

                LogTr("Exit cRdDatById.__init__()")

        class cRdMemByAdr:
            def __init__(self):
                LogTr("Enter cRdMemByAdr.__init__()")

                LogTr("Exit cRdMemByAdr.__init__()")

        class cRdScDatById:
            def __init__(self):
                LogTr("Enter cRdScDatById.__init__()")

                LogTr("Exit cRdScDatById.__init__()")

        class cRdDatByPerId:
            def __init__(self):
                LogTr("Enter cRdDatByPerId.__init__()")

                LogTr("Exit cRdDatByPerId.__init__()")

        class cDynDefDatId:
            def __init__(self):
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
            def __init__(self):
                LogTr("Enter cWrDatById.__init__()")

                LogTr("Exit cWrDatById.__init__()")

        class cWrMemByAdr:
            def __init__(self):
                LogTr("Enter cWrMemByAdr.__init__()")

                LogTr("Exit cWrMemByAdr.__init__()")

        class cClrDiagInfo:
            def __init__(self):
                LogTr("Enter cClrDiagInfo.__init__()")

                LogTr("Exit cClrDiagInfo.__init__()")

        class cRdDtcInfo:
            def __init__(self):
                LogTr("Enter cRdDtcInfo.__init__()")

                LogTr("Exit cRdDtcInfo.__init__()")

        class cIoCtrlById:
            def __init__(self):
                LogTr("Enter cIoCtrlById.__init__()")

                LogTr("Exit cIoCtrlById.__init__()")

        class cRtCtrl:
            def __init__(self):
                LogTr("Enter cRtCtrl.__init__()")

                LogTr("Exit cRtCtrl.__init__()")

        class cReqDwnld:
            def __init__(self):
                LogTr("Enter cReqDwnld.__init__()")

                LogTr("Exit cReqDwnld.__init__()")

        class cReqUpld:
            def __init__(self):
                LogTr("Enter cReqUpld.__init__()")

                LogTr("Exit cReqUpld.__init__()")

        class cTxDat:
            def __init__(self):
                LogTr("Enter cTxDat.__init__()")

                LogTr("Exit cTxDat.__init__()")

        class cReqTxEx:
            def __init__(self):
                LogTr("Enter cReqTxEx.__init__()")

                LogTr("Exit cReqTxEx.__init__()")

        class cReqFileTx:
            def __init__(self):
                LogTr("Enter cReqFileTx.__init__()")

                LogTr("Exit cReqFileTx.__init__()")

        def __init__(self):
            LogTr("Enter cSubFun.__init__()")

            self.DiagSessCtrl = self.cDiagSessCtrl()
            self.EcuRst = self.cEcuRst()
            self.SecAcc = self.cSecAcc()
            self.CommCtrl = self.cCommCtrl()
            self.TstrPrsnt = self.cTstrPrsnt()
            self.AccTmParam = self.cAccTmParam()
            self.SecdDatTx = self.cSecdDatTx()
            self.CtrlDtcSet = self.cCtrlDtcSet()
            self.RespOnEvt = self.cRespOnEvt()
            self.LnkCtrl = self.cLnkCtrl()
            self.RdDatById = self.cRdDatById()
            self.RdMemByAdr = self.cRdMemByAdr()
            self.RdScDatById = self.cRdScDatById()
            self.RdDatByPerId = self.cRdDatByPerId()
            self.DynDefDatId = self.cDynDefDatId()
            self.WrDatById = self.cWrDatById()
            self.WrMemByAdr = self.cWrMemByAdr()
            self.ClrDiagInfo = self.cClrDiagInfo()
            self.RdDtcInfo = self.cRdDtcInfo()
            self.IoCtrlById = self.cIoCtrlById()
            self.RtCtrl = self.cRtCtrl()
            self.ReqDwnld = self.cReqDwnld()
            self.ReqUpld = self.cReqUpld()
            self.TxDat = self.cTxDat()
            self.ReqTxEx = self.cReqTxEx()
            self.ReqFileTx = self.cReqFileTx()

            LogTr("Exit cSubFun.__init__()")

    class cNrc:
        class cDiagSessCtrl:
            def __init__(self):
                LogTr("Enter cDiagSessCtrl.__init__()")

                self.SubFunNSpt = "12" # 0x12: sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # 0x13: incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # 0x22: conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")

                LogTr("Exit cDiagSessCtrl.__init__()")

        class cEcuRst:
            def __init__(self):
                LogTr("Enter cEcuRst.__init__()")

                self.SubFunNSpt = "12" # 0x12: sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # 0x13: incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # 0x22: conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.SecAccD = "33" # 0x33: securityAccessDenied.
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cEcuRst.__init__()")

        class cSecAcc:
            def __init__(self):
                LogTr("Enter cSecAcc.__init__()")

                self.SubFunNSpt = "12" # 0x12: sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # 0x13: incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # 0x22: conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqSeqErr = "24" # 0x24: requestSequenceError.
                LogDbg(f"self.ReqSeqErr = {self.ReqSeqErr}")
                self.ReqOtRng = "31" # 0x31: requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.InvKey = "35" # 0x35: invalidKey.
                LogDbg(f"self.InvKey = {self.InvKey}")
                self.ExcNumAtpt = "36" # 0x36: exceededNumberOfAttempts.
                LogDbg(f"self.ExcNumAtpt = {self.ExcNumAtpt}")
                self.ReqTmDlyNExp = "37" # 0x37: requiredTimeDelayNotExpired.
                LogDbg(f"self.ReqTmDlyNExp = {self.ReqTmDlyNExp}")

                LogTr("Exit cSecAcc.__init__()")

        class cCommCtrl:
            def __init__(self):
                LogTr("Enter cSecAcc.__init__()")

                self.SubFunNSpt = "12" # 0x12: sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # 0x13: incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # 0x22: conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # 0x31: requestOutOfRange.

                LogTr("Exit cSecAcc.__init__()")

        class cTstrPrsnt:
            def __init__(self):
                LogTr("Enter cTstrPrsnt.__init__()")

                self.SubFunNSpt = "12" # 0x12: sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # 0x13: incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")

                LogTr("Exit cTstrPrsnt.__init__()")

        class cAccTmParam:
            def __init__(self):
                LogTr("Enter cAccTmParam.__init__()")

                self.SubFunNSpt = "12" # sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cAccTmParam.__init__()")

        class cSecdDatTx:
            def __init__(self):
                LogTr("Enter cSecdDatTx.__init__()")

                self.SubFunNSpt = "12" # sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cSecdDatTx.__init__()")

        class cCtrlDtcSet:
            def __init__(self):
                LogTr("Enter cCtrlDtcSet.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.RsvdByExtDatLnkSecDoc = "38~4F" # reservedByExtendedDataLinkSecurityDocument.
                LogDbg(f"self.RsvdByExtDatLnkSecDoc = {self.RsvdByExtDatLnkSecDoc}")

                LogTr("Exit cCtrlDtcSet.__init__()")

        class cRespOnEvt:
            def __init__(self):
                LogTr("Enter cRespOnEvt.__init__()")

                self.SubFunNSpt = "12" # sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cRespOnEvt.__init__()")

        class cLnkCtrl:
            def __init__(self):
                LogTr("Enter cLnkCtrl.__init__()")

                self.SubFunNSpt = "12" # sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqSeqErr = "24" # requestSequenceError.
                LogDbg(f"self.ReqSeqErr = {self.ReqSeqErr}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")

                LogTr("Exit cLnkCtrl.__init__()")

        class cRdDatById:
            def __init__(self):
                LogTr("Enter cRdDatById.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.RespTooLng = "14" # responseTooLong.
                LogDbg(f"self.RespTooLng = {self.RespTooLng}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33" # securityAccessDenied.
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cRdDatById.__init__()")

        class cRdMemByAdr:
            def __init__(self):
                LogTr("Enter cRdMemByAdr.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33" # SecurityAccessDenied.

                LogTr("Exit cRdMemByAdr.__init__()")

        class cRdScDatById:
            def __init__(self):
                LogTr("Enter cRdScDatById.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33" # securityAccessDenied.

                LogTr("Exit cRdScDatById.__init__()")

        class cRdDatByPerId:
            def __init__(self):
                LogTr("Enter cRdDatByPerId.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33" # securityAccessDenied.
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cRdDatByPerId.__init__()")

        class cDynDefDatId:
            def __init__(self):
                LogTr("Enter cDynDefDatId.__init__()")

                self.SubFunNSpt = "12" # sub-functionNotSupported.
                LogDbg(f"self.SubFunNSpt = {self.SubFunNSpt}")
                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect
                LogDbg(f"self.CndNCor = {self.CndNCor}")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33" # securityAccessDenied
                LogDbg(f"self.SecAccD = {self.SecAccD}")

                LogTr("Exit cDynDefDatId.__init__()")

        class cWrDatById:
            def __init__(self):
                LogTr("Enter cWrDatById.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = self.CndNCor")
                self.ReqOtRng = "31" # requestOutOfRange.
                LogDbg(f"self.ReqOtRng = {self.ReqOtRng}")
                self.SecAccD = "33" # securityAccessDenied.
                LogDbg(f"self.SecAccD = {self.SecAccD}")
                self.GenProgFail = "72" # generalProgrammingFailure.
                LogDbg(f"self.GenProgFail = {self.GenProgFail}")

                LogTr("Exit cWrDatById.__init__()")

        class cWrMemByAdr:
            def __init__(self):
                LogTr("Enter cWrMemByAdr.__init__()")

                self.IncorMsgLenOrInvFmt = "13" # incorrectMessageLengthOrInvalidFormat.
                LogDbg(f"self.IncorMsgLenOrInvFmt = {self.IncorMsgLenOrInvFmt}")
                self.CndNCor = "22" # conditionsNotCorrect.
                LogDbg(f"self.CndNCor = {self.CndNCor}")

                LogTr("Exit cWrMemByAdr.__init__()")

        def __init__(self):
            LogTr("Enter cNrc.__init__()")

            self.DiagSessCtrl = self.cDiagSessCtrl()
            self.EcuRst = self.cEcuRst()
            self.SecAcc = self.cSecAcc()
            self.CommCtrl = self.cCommCtrl()
            self.TstrPrsnt = self.cTstrPrsnt()
            self.AccTmParam = self.cAccTmParam()
            self.SecdDatTx = self.cSecdDatTx()
            self.CtrlDtcSet = self.cCtrlDtcSet()
            self.RespOnEvt = self.cRespOnEvt()
            self.LnkCtrl = self.cLnkCtrl()
            self.RdDatById = self.cRdDatById()
            self.RdMemByAdr = self.cRdMemByAdr()
            self.RdScDatById = self.cRdScDatById()
            self.RdDatByPerId = self.cRdDatByPerId()
            self.DynDefDatId = self.cDynDefDatId()
            self.WrDatById = self.cWrDatById()
            self.WrMemByAdr = self.cWrMemByAdr()
            self.ClrDiagInfo = self.cClrDiagInfo()
            self.RdDtcInfo = self.cRdDtcInfo()
            self.IoCtrlById = self.cIoCtrlById()
            self.RtCtrl = self.cRtCtrl()
            self.ReqDwnld = self.cReqDwnld()
            self.ReqUpld = self.cReqUpld()
            self.TxDat = self.cTxDat()
            self.ReqTxEx = self.cReqTxEx()
            self.ReqFileTx = self.cReqFileTx()

            LogTr("Exit cNrc.__init__()")

    def __init__(self):
        LogTr("Enter cMsgPset.__init__()")

        self.Ser = self.cSid()
        self.SubFun = self.cSubFun()
        self.Nrc = self.cNrc()

        LogTr("Exit cMsgPset.__init__()")

class cUdsSer:
    def __init__(self):
        LogTr("Enter cUdsSer.__init__()")

        self.DoipSer = cDoipSer()

        LogTr("Exit cUdsSer.__init__()")

    def Lsn(self):
        LogTr("Enter cUdsSer.Lsn()")

        self.DoipSer.Lsn()

        LogTr("Exit cUdsSer.Lsn()")

class cUdsClt:
    def __init__(self):
        LogTr("Enter cUdsClt.__init__()")

        self.DoipClt = cDoipClt()

        LogTr("Exit cUdsClt.__init__()")

    def Snd(self, Msg):
        LogTr("Enter cUdsClt.Snd()")

        self.DoipClt.ReqDiag(Msg)

        LogTr("Exit cUdsClt.Snd()")

    def Recv(self):
        LogTr("Enter cUdsClt.Recv()")

        return self.DoipClt.RespDiag()

        LogTr("Exit cUdsClt.Recv()")

def ImitUdsSer():
    LogTr("Enter ImitUdsSer")

    Ecu = cUdsSer()
    Ecu.Lsn()

    while True:
        if Ecu.DoipSer.IsRecvBufMty() == False:
            RecvMsg = Ecu.DoipSer.Recv()
            LogDbg(f"RecvMsg: {RecvMsg}")

            if RecvMsg != "":
                Hdr, Pl = Ecu.DoipSer.Msg.PrsMsg(RecvMsg)
                LogDbg(f"Hdr = {Hdr}")
                LogDbg(f"Pl = {Pl}")

                ProtoVer, InvProtoVer, PlTyp, PlLen = Ecu.DoipSer.Msg.Hdr.PrsHdr(Hdr)
                LogDbg(f"ProtoVer = {ProtoVer}")
                LogDbg(f"InvProtoVer = {InvProtoVer}")
                LogDbg(f"PlTyp = {PlTyp}")
                LogDbg(f"PlLen = {PlLen}")

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
                    SrcAdr, TgtAdr, UsrDat = Ecu.DoipSer.Msg.Pl.PrsPlDiag(Pl)
                    LogDbg(f"SrcAdr = {SrcAdr}")
                    LogDbg(f"TgtAdr = {TgtAdr}")
                    LogDbg(f"UsrDat = {UsrDat}")

                    Ecu.DoipSer.PosAckDiagMsg("00")

    LogTr("Exit ImitUdsSer")

def ImitUdsClt():
    LogTr("Enter ImitUdsClt")

    Tstr = cUdsClt()
    Tstr.DoipClt.Conn()
    Tstr.DoipClt.ReqRteAct()
    Tstr.DoipClt.RespRteAct()
    Tstr.Snd("1003")
    Tstr.Recv()

    LogTr("Exit ImitUdsClt")

if __name__ == "__main__":
    LogTr("__main__")

    if sys.argv[1] == "-Ser":
        ImitUdsSer()
    elif sys.argv[1] == "-Clt":
        ImitUdsClt()
