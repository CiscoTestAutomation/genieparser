
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_snmp
from genie.libs.parser.iosxe.show_snmp import ShowSnmpMib


# =============================
# Unit test for 'show snmp mib'
# =============================
class test_show_snmp_mib(unittest.TestCase):

    '''Unit test for "show snmp mib" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {'aal5VccEntry': {'3': {}, '4': {}, '5': {}},
     'aarpEntry': {'1': {}, '2': {}, '3': {}},
     'adslAtucChanConfFastMaxTxRate': {},
     'adslAtucChanConfFastMinTxRate': {},
     'adslAtucChanConfInterleaveMaxTxRate': {},
     'adslAtucChanConfInterleaveMinTxRate': {},
     'adslAtucChanConfMaxInterleaveDelay': {},
     'adslAtucChanCorrectedBlks': {},
     'adslAtucChanCrcBlockLength': {},
     'adslAtucChanCurrTxRate': {},
     'adslAtucChanInterleaveDelay': {},
     'adslAtucChanIntervalCorrectedBlks': {},
     'adslAtucChanIntervalReceivedBlks': {},
     'adslAtucChanIntervalTransmittedBlks': {},
     'adslAtucChanIntervalUncorrectBlks': {},
     'adslAtucChanIntervalValidData': {},
     'adslAtucChanPerfCurr15MinCorrectedBlks': {},
     'adslAtucChanPerfCurr15MinReceivedBlks': {},
     'adslAtucChanPerfCurr15MinTimeElapsed': {},
     'adslAtucChanPerfCurr15MinTransmittedBlks': {},
     'adslAtucChanPerfCurr15MinUncorrectBlks': {},
     'adslAtucChanPerfCurr1DayCorrectedBlks': {},
     'adslAtucChanPerfCurr1DayReceivedBlks': {},
     'adslAtucChanPerfCurr1DayTimeElapsed': {},
     'adslAtucChanPerfCurr1DayTransmittedBlks': {},
     'adslAtucChanPerfCurr1DayUncorrectBlks': {},
     'adslAtucChanPerfInvalidIntervals': {},
     'adslAtucChanPerfPrev1DayCorrectedBlks': {},
     'adslAtucChanPerfPrev1DayMoniSecs': {},
     'adslAtucChanPerfPrev1DayReceivedBlks': {},
     'adslAtucChanPerfPrev1DayTransmittedBlks': {},
     'adslAtucChanPerfPrev1DayUncorrectBlks': {},
     'adslAtucChanPerfValidIntervals': {},
     'adslAtucChanPrevTxRate': {},
     'adslAtucChanReceivedBlks': {},
     'adslAtucChanTransmittedBlks': {},
     'adslAtucChanUncorrectBlks': {},
     'adslAtucConfDownshiftSnrMgn': {},
     'adslAtucConfMaxSnrMgn': {},
     'adslAtucConfMinDownshiftTime': {},
     'adslAtucConfMinSnrMgn': {},
     'adslAtucConfMinUpshiftTime': {},
     'adslAtucConfRateChanRatio': {},
     'adslAtucConfRateMode': {},
     'adslAtucConfTargetSnrMgn': {},
     'adslAtucConfUpshiftSnrMgn': {},
     'adslAtucCurrAtn': {},
     'adslAtucCurrAttainableRate': {},
     'adslAtucCurrOutputPwr': {},
     'adslAtucCurrSnrMgn': {},
     'adslAtucCurrStatus': {},
     'adslAtucDmtConfFastPath': {},
     'adslAtucDmtConfFreqBins': {},
     'adslAtucDmtConfInterleavePath': {},
     'adslAtucDmtFastPath': {},
     'adslAtucDmtInterleavePath': {},
     'adslAtucDmtIssue': {},
     'adslAtucDmtState': {},
     'adslAtucInitFailureTrapEnable': {},
     'adslAtucIntervalESs': {},
     'adslAtucIntervalInits': {},
     'adslAtucIntervalLofs': {},
     'adslAtucIntervalLols': {},
     'adslAtucIntervalLoss': {},
     'adslAtucIntervalLprs': {},
     'adslAtucIntervalValidData': {},
     'adslAtucInvSerialNumber': {},
     'adslAtucInvVendorID': {},
     'adslAtucInvVersionNumber': {},
     'adslAtucPerfCurr15MinESs': {},
     'adslAtucPerfCurr15MinInits': {},
     'adslAtucPerfCurr15MinLofs': {},
     'adslAtucPerfCurr15MinLols': {},
     'adslAtucPerfCurr15MinLoss': {},
     'adslAtucPerfCurr15MinLprs': {},
     'adslAtucPerfCurr15MinTimeElapsed': {},
     'adslAtucPerfCurr1DayESs': {},
     'adslAtucPerfCurr1DayInits': {},
     'adslAtucPerfCurr1DayLofs': {},
     'adslAtucPerfCurr1DayLols': {},
     'adslAtucPerfCurr1DayLoss': {},
     'adslAtucPerfCurr1DayLprs': {},
     'adslAtucPerfCurr1DayTimeElapsed': {},
     'adslAtucPerfESs': {},
     'adslAtucPerfInits': {},
     'adslAtucPerfInvalidIntervals': {},
     'adslAtucPerfLofs': {},
     'adslAtucPerfLols': {},
     'adslAtucPerfLoss': {},
     'adslAtucPerfLprs': {},
     'adslAtucPerfPrev1DayESs': {},
     'adslAtucPerfPrev1DayInits': {},
     'adslAtucPerfPrev1DayLofs': {},
     'adslAtucPerfPrev1DayLols': {},
     'adslAtucPerfPrev1DayLoss': {},
     'adslAtucPerfPrev1DayLprs': {},
     'adslAtucPerfPrev1DayMoniSecs': {},
     'adslAtucPerfValidIntervals': {},
     'adslAtucThresh15MinESs': {},
     'adslAtucThresh15MinLofs': {},
     'adslAtucThresh15MinLols': {},
     'adslAtucThresh15MinLoss': {},
     'adslAtucThresh15MinLprs': {},
     'adslAtucThreshFastRateDown': {},
     'adslAtucThreshFastRateUp': {},
     'adslAtucThreshInterleaveRateDown': {},
     'adslAtucThreshInterleaveRateUp': {},
     'adslAturChanConfFastMaxTxRate': {},
     'adslAturChanConfFastMinTxRate': {},
     'adslAturChanConfInterleaveMaxTxRate': {},
     'adslAturChanConfInterleaveMinTxRate': {},
     'adslAturChanConfMaxInterleaveDelay': {},
     'adslAturChanCorrectedBlks': {},
     'adslAturChanCrcBlockLength': {},
     'adslAturChanCurrTxRate': {},
     'adslAturChanInterleaveDelay': {},
     'adslAturChanIntervalCorrectedBlks': {},
     'adslAturChanIntervalReceivedBlks': {},
     'adslAturChanIntervalTransmittedBlks': {},
     'adslAturChanIntervalUncorrectBlks': {},
     'adslAturChanIntervalValidData': {},
     'adslAturChanPerfCurr15MinCorrectedBlks': {},
     'adslAturChanPerfCurr15MinReceivedBlks': {},
     'adslAturChanPerfCurr15MinTimeElapsed': {},
     'adslAturChanPerfCurr15MinTransmittedBlks': {},
     'adslAturChanPerfCurr15MinUncorrectBlks': {},
     'adslAturChanPerfCurr1DayCorrectedBlks': {},
     'adslAturChanPerfCurr1DayReceivedBlks': {},
     'adslAturChanPerfCurr1DayTimeElapsed': {},
     'adslAturChanPerfCurr1DayTransmittedBlks': {},
     'adslAturChanPerfCurr1DayUncorrectBlks': {},
     'adslAturChanPerfInvalidIntervals': {},
     'adslAturChanPerfPrev1DayCorrectedBlks': {},
     'adslAturChanPerfPrev1DayMoniSecs': {},
     'adslAturChanPerfPrev1DayReceivedBlks': {},
     'adslAturChanPerfPrev1DayTransmittedBlks': {},
     'adslAturChanPerfPrev1DayUncorrectBlks': {},
     'adslAturChanPerfValidIntervals': {},
     'adslAturChanPrevTxRate': {},
     'adslAturChanReceivedBlks': {},
     'adslAturChanTransmittedBlks': {},
     'adslAturChanUncorrectBlks': {},
     'adslAturConfDownshiftSnrMgn': {},
     'adslAturConfMaxSnrMgn': {},
     'adslAturConfMinDownshiftTime': {},
     'adslAturConfMinSnrMgn': {},
     'adslAturConfMinUpshiftTime': {},
     'adslAturConfRateChanRatio': {},
     'adslAturConfRateMode': {},
     'adslAturConfTargetSnrMgn': {},
     'adslAturConfUpshiftSnrMgn': {},
     'adslAturCurrAtn': {},
     'adslAturCurrAttainableRate': {},
     'adslAturCurrOutputPwr': {},
     'adslAturCurrSnrMgn': {},
     'adslAturCurrStatus': {},
     'adslAturDmtConfFastPath': {},
     'adslAturDmtConfFreqBins': {},
     'adslAturDmtConfInterleavePath': {},
     'adslAturDmtFastPath': {},
     'adslAturDmtInterleavePath': {},
     'adslAturDmtIssue': {},
     'adslAturDmtState': {},
     'adslAturIntervalESs': {},
     'adslAturIntervalLofs': {},
     'adslAturIntervalLoss': {},
     'adslAturIntervalLprs': {},
     'adslAturIntervalValidData': {},
     'adslAturInvSerialNumber': {},
     'adslAturInvVendorID': {},
     'adslAturInvVersionNumber': {},
     'adslAturPerfCurr15MinESs': {},
     'adslAturPerfCurr15MinLofs': {},
     'adslAturPerfCurr15MinLoss': {},
     'adslAturPerfCurr15MinLprs': {},
     'adslAturPerfCurr15MinTimeElapsed': {},
     'adslAturPerfCurr1DayESs': {},
     'adslAturPerfCurr1DayLofs': {},
     'adslAturPerfCurr1DayLoss': {},
     'adslAturPerfCurr1DayLprs': {},
     'adslAturPerfCurr1DayTimeElapsed': {},
     'adslAturPerfESs': {},
     'adslAturPerfInvalidIntervals': {},
     'adslAturPerfLofs': {},
     'adslAturPerfLoss': {},
     'adslAturPerfLprs': {},
     'adslAturPerfPrev1DayESs': {},
     'adslAturPerfPrev1DayLofs': {},
     'adslAturPerfPrev1DayLoss': {},
     'adslAturPerfPrev1DayLprs': {},
     'adslAturPerfPrev1DayMoniSecs': {},
     'adslAturPerfValidIntervals': {},
     'adslAturThresh15MinESs': {},
     'adslAturThresh15MinLofs': {},
     'adslAturThresh15MinLoss': {},
     'adslAturThresh15MinLprs': {},
     'adslAturThreshFastRateDown': {},
     'adslAturThreshFastRateUp': {},
     'adslAturThreshInterleaveRateDown': {},
     'adslAturThreshInterleaveRateUp': {},
     'adslLineAlarmConfProfile': {},
     'adslLineAlarmConfProfileRowStatus': {},
     'adslLineCoding': {},
     'adslLineConfProfile': {},
     'adslLineConfProfileRowStatus': {},
     'adslLineDmtConfEOC': {},
     'adslLineDmtConfMode': {},
     'adslLineDmtConfTrellis': {},
     'adslLineDmtEOC': {},
     'adslLineDmtTrellis': {},
     'adslLineSpecific': {},
     'adslLineType': {},
     'alarmEntry': {'1': {},
                    '10': {},
                    '11': {},
                    '12': {},
                    '2': {},
                    '3': {},
                    '4': {},
                    '5': {},
                    '6': {},
                    '7': {},
                    '8': {},
                    '9': {}},
     'alpsAscuA1': {},
     'alpsAscuA2': {},
     'alpsAscuAlarmsEnabled': {},
     'alpsAscuCktName': {},
     'alpsAscuDownReason': {},
     'alpsAscuDropsAscuDisabled': {},
     'alpsAscuDropsAscuDown': {},
     'alpsAscuDropsGarbledPkts': {},
     'alpsAscuEnabled': {},
     'alpsAscuEntry': {'20': {}},
     'alpsAscuFwdStatusOption': {},
     'alpsAscuInOctets': {},
     'alpsAscuInPackets': {},
     'alpsAscuMaxMsgLength': {},
     'alpsAscuOutOctets': {},
     'alpsAscuOutPackets': {},
     'alpsAscuRetryOption': {},
     'alpsAscuRowStatus': {},
     'alpsAscuState': {},
     'alpsCktAscuId': {},
     'alpsCktAscuIfIndex': {},
     'alpsCktAscuStatus': {},
     'alpsCktBaseAlarmsEnabled': {},
     'alpsCktBaseConnType': {},
     'alpsCktBaseCurrPeerConnId': {},
     'alpsCktBaseCurrentPeer': {},
     'alpsCktBaseDownReason': {},
     'alpsCktBaseDropsCktDisabled': {},
     'alpsCktBaseDropsLifeTimeExpd': {},
     'alpsCktBaseDropsQOverflow': {},
     'alpsCktBaseEnabled': {},
     'alpsCktBaseHostLinkNumber': {},
     'alpsCktBaseHostLinkType': {},
     'alpsCktBaseInOctets': {},
     'alpsCktBaseInPackets': {},
     'alpsCktBaseLifeTimeTimer': {},
     'alpsCktBaseLocalHld': {},
     'alpsCktBaseNumActiveAscus': {},
     'alpsCktBaseOutOctets': {},
     'alpsCktBaseOutPackets': {},
     'alpsCktBasePriPeerAddr': {},
     'alpsCktBaseRemHld': {},
     'alpsCktBaseRowStatus': {},
     'alpsCktBaseState': {},
     'alpsCktP1024Ax25LCN': {},
     'alpsCktP1024BackupPeerAddr': {},
     'alpsCktP1024DropsUnkAscu': {},
     'alpsCktP1024EmtoxX121': {},
     'alpsCktP1024IdleTimer': {},
     'alpsCktP1024InPktSize': {},
     'alpsCktP1024MatipCloseDelay': {},
     'alpsCktP1024OutPktSize': {},
     'alpsCktP1024RetryTimer': {},
     'alpsCktP1024RowStatus': {},
     'alpsCktP1024SvcMsgIntvl': {},
     'alpsCktP1024SvcMsgList': {},
     'alpsCktP1024WinIn': {},
     'alpsCktP1024WinOut': {},
     'alpsCktX25DropsVcReset': {},
     'alpsCktX25HostX121': {},
     'alpsCktX25IfIndex': {},
     'alpsCktX25LCN': {},
     'alpsCktX25RemoteX121': {},
     'alpsIfHLinkActiveCkts': {},
     'alpsIfHLinkAx25PvcDamp': {},
     'alpsIfHLinkEmtoxHostX121': {},
     'alpsIfHLinkX25ProtocolType': {},
     'alpsIfP1024CurrErrCnt': {},
     'alpsIfP1024EncapType': {},
     'alpsIfP1024Entry': {'11': {}, '12': {}, '13': {}},
     'alpsIfP1024GATimeout': {},
     'alpsIfP1024MaxErrCnt': {},
     'alpsIfP1024MaxRetrans': {},
     'alpsIfP1024MinGoodPollResp': {},
     'alpsIfP1024NumAscus': {},
     'alpsIfP1024PollPauseTimeout': {},
     'alpsIfP1024PollRespTimeout': {},
     'alpsIfP1024PollingRatio': {},
     'alpsIpAddress': {},
     'alpsPeerInCallsAcceptFlag': {},
     'alpsPeerKeepaliveMaxRetries': {},
     'alpsPeerKeepaliveTimeout': {},
     'alpsPeerLocalAtpPort': {},
     'alpsPeerLocalIpAddr': {},
     'alpsRemPeerAlarmsEnabled': {},
     'alpsRemPeerCfgActivation': {},
     'alpsRemPeerCfgAlarmsOn': {},
     'alpsRemPeerCfgIdleTimer': {},
     'alpsRemPeerCfgNoCircTimer': {},
     'alpsRemPeerCfgRowStatus': {},
     'alpsRemPeerCfgStatIntvl': {},
     'alpsRemPeerCfgStatRetry': {},
     'alpsRemPeerCfgTCPQLen': {},
     'alpsRemPeerConnActivation': {},
     'alpsRemPeerConnAlarmsOn': {},
     'alpsRemPeerConnCreation': {},
     'alpsRemPeerConnDownReason': {},
     'alpsRemPeerConnDropsGiant': {},
     'alpsRemPeerConnDropsQFull': {},
     'alpsRemPeerConnDropsUnreach': {},
     'alpsRemPeerConnDropsVersion': {},
     'alpsRemPeerConnForeignPort': {},
     'alpsRemPeerConnIdleTimer': {},
     'alpsRemPeerConnInOctets': {},
     'alpsRemPeerConnInPackets': {},
     'alpsRemPeerConnLastRxAny': {},
     'alpsRemPeerConnLastTxRx': {},
     'alpsRemPeerConnLocalPort': {},
     'alpsRemPeerConnNoCircTimer': {},
     'alpsRemPeerConnNumActCirc': {},
     'alpsRemPeerConnOutOctets': {},
     'alpsRemPeerConnOutPackets': {},
     'alpsRemPeerConnProtocol': {},
     'alpsRemPeerConnStatIntvl': {},
     'alpsRemPeerConnStatRetry': {},
     'alpsRemPeerConnState': {},
     'alpsRemPeerConnTCPQLen': {},
     'alpsRemPeerConnType': {},
     'alpsRemPeerConnUptime': {},
     'alpsRemPeerDropsGiant': {},
     'alpsRemPeerDropsPeerUnreach': {},
     'alpsRemPeerDropsQFull': {},
     'alpsRemPeerIdleTimer': {},
     'alpsRemPeerInOctets': {},
     'alpsRemPeerInPackets': {},
     'alpsRemPeerLocalPort': {},
     'alpsRemPeerNumActiveCkts': {},
     'alpsRemPeerOutOctets': {},
     'alpsRemPeerOutPackets': {},
     'alpsRemPeerRemotePort': {},
     'alpsRemPeerRowStatus': {},
     'alpsRemPeerState': {},
     'alpsRemPeerTCPQlen': {},
     'alpsRemPeerUptime': {},
     'alpsSvcMsg': {},
     'alpsSvcMsgRowStatus': {},
     'alpsX121ToIpTransRowStatus': {},
     'atEntry': {'1': {}, '2': {}, '3': {}},
     'atecho': {'1': {}, '2': {}},
     'atmCurrentlyFailingPVclTimeStamp': {},
     'atmForumUni.10.1.1.1': {},
     'atmForumUni.10.1.1.10': {},
     'atmForumUni.10.1.1.11': {},
     'atmForumUni.10.1.1.2': {},
     'atmForumUni.10.1.1.3': {},
     'atmForumUni.10.1.1.4': {},
     'atmForumUni.10.1.1.5': {},
     'atmForumUni.10.1.1.6': {},
     'atmForumUni.10.1.1.7': {},
     'atmForumUni.10.1.1.8': {},
     'atmForumUni.10.1.1.9': {},
     'atmForumUni.10.144.1.1': {},
     'atmForumUni.10.144.1.2': {},
     'atmForumUni.10.100.1.1': {},
     'atmForumUni.10.100.1.10': {},
     'atmForumUni.10.100.1.2': {},
     'atmForumUni.10.100.1.3': {},
     'atmForumUni.10.100.1.4': {},
     'atmForumUni.10.100.1.5': {},
     'atmForumUni.10.100.1.6': {},
     'atmForumUni.10.100.1.7': {},
     'atmForumUni.10.100.1.8': {},
     'atmForumUni.10.100.1.9': {},
     'atmInterfaceConfEntry': {'1': {},
                               '10': {},
                               '11': {},
                               '12': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'atmIntfCurrentlyDownToUpPVcls': {},
     'atmIntfCurrentlyFailingPVcls': {},
     'atmIntfCurrentlyOAMFailingPVcls': {},
     'atmIntfOAMFailedPVcls': {},
     'atmIntfPvcFailures': {},
     'atmIntfPvcFailuresTrapEnable': {},
     'atmIntfPvcNotificationInterval': {},
     'atmPVclHigherRangeValue': {},
     'atmPVclLowerRangeValue': {},
     'atmPVclRangeStatusChangeEnd': {},
     'atmPVclRangeStatusChangeStart': {},
     'atmPVclStatusChangeEnd': {},
     'atmPVclStatusChangeStart': {},
     'atmPVclStatusTransition': {},
     'atmPreviouslyFailedPVclInterval': {},
     'atmPreviouslyFailedPVclTimeStamp': {},
     'atmTrafficDescrParamEntry': {'2': {},
                                   '3': {},
                                   '4': {},
                                   '5': {},
                                   '6': {},
                                   '7': {},
                                   '8': {},
                                   '9': {}},
     'atmVclEntry': {'10': {},
                     '11': {},
                     '12': {},
                     '13': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'atmVplEntry': {'2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {}},
     'atmfAddressEntry': {'3': {}, '4': {}},
     'atmfAtmLayerEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'atmfAtmStatsEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'atmfNetPrefixEntry': {'3': {}},
     'atmfPhysicalGroup': {'2': {}, '4': {}},
     'atmfPortEntry': {'1': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {}},
     'atmfVccEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '22': {},
                      '23': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'atmfVpcEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'atportEntry': {'1': {},
                     '10': {},
                     '11': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'bcpConfigEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '14': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'bcpOperEntry': {'1': {}},
     'bgp4PathAttrASPathSegment': {},
     'bgp4PathAttrAggregatorAS': {},
     'bgp4PathAttrAggregatorAddr': {},
     'bgp4PathAttrAtomicAggregate': {},
     'bgp4PathAttrBest': {},
     'bgp4PathAttrCalcLocalPref': {},
     'bgp4PathAttrIpAddrPrefix': {},
     'bgp4PathAttrIpAddrPrefixLen': {},
     'bgp4PathAttrLocalPref': {},
     'bgp4PathAttrMultiExitDisc': {},
     'bgp4PathAttrNextHop': {},
     'bgp4PathAttrOrigin': {},
     'bgp4PathAttrPeer': {},
     'bgp4PathAttrUnknown': {},
     'bgpIdentifier': {},
     'bgpLocalAs': {},
     'bgpPeerAdminStatus': {},
     'bgpPeerConnectRetryInterval': {},
     'bgpPeerEntry': {'14': {}, '2': {}},
     'bgpPeerFsmEstablishedTime': {},
     'bgpPeerFsmEstablishedTransitions': {},
     'bgpPeerHoldTime': {},
     'bgpPeerHoldTimeConfigured': {},
     'bgpPeerIdentifier': {},
     'bgpPeerInTotalMessages': {},
     'bgpPeerInUpdateElapsedTime': {},
     'bgpPeerInUpdates': {},
     'bgpPeerKeepAlive': {},
     'bgpPeerKeepAliveConfigured': {},
     'bgpPeerLocalAddr': {},
     'bgpPeerLocalPort': {},
     'bgpPeerMinASOriginationInterval': {},
     'bgpPeerMinRouteAdvertisementInterval': {},
     'bgpPeerNegotiatedVersion': {},
     'bgpPeerOutTotalMessages': {},
     'bgpPeerOutUpdates': {},
     'bgpPeerRemoteAddr': {},
     'bgpPeerRemoteAs': {},
     'bgpPeerRemotePort': {},
     'bgpVersion': {},
     'bscCUEntry': {'10': {},
                    '11': {},
                    '2': {},
                    '3': {},
                    '4': {},
                    '5': {},
                    '6': {},
                    '7': {},
                    '8': {},
                    '9': {}},
     'bscExtAddressEntry': {'2': {}},
     'bscPortEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'bstunGlobal': {'1': {}, '2': {}, '3': {}, '4': {}},
     'bstunGroupEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'bstunPortEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'bstunRouteEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'cAal5VccEntry': {'1': {},
                       '10': {},
                       '11': {},
                       '12': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'cBootpHCCountDropNotServingSubnet': {},
     'cBootpHCCountDropUnknownClients': {},
     'cBootpHCCountInvalids': {},
     'cBootpHCCountReplies': {},
     'cBootpHCCountRequests': {},
     'cCallHistoryEntry': {'10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '16': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '20': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cCallHistoryIecEntry': {'2': {}},
     'cContextMappingEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'cContextMappingMIBObjects.2.1.1': {},
     'cContextMappingMIBObjects.2.1.2': {},
     'cContextMappingMIBObjects.2.1.3': {},
     'cDhcpv4HCCountAcks': {},
     'cDhcpv4HCCountDeclines': {},
     'cDhcpv4HCCountDiscovers': {},
     'cDhcpv4HCCountDropNotServingSubnet': {},
     'cDhcpv4HCCountDropUnknownClient': {},
     'cDhcpv4HCCountForcedRenews': {},
     'cDhcpv4HCCountInforms': {},
     'cDhcpv4HCCountInvalids': {},
     'cDhcpv4HCCountNaks': {},
     'cDhcpv4HCCountOffers': {},
     'cDhcpv4HCCountReleases': {},
     'cDhcpv4HCCountRequests': {},
     'cDhcpv4ServerClientAllowedProtocol': {},
     'cDhcpv4ServerClientClientId': {},
     'cDhcpv4ServerClientDomainName': {},
     'cDhcpv4ServerClientHostName': {},
     'cDhcpv4ServerClientLeaseType': {},
     'cDhcpv4ServerClientPhysicalAddress': {},
     'cDhcpv4ServerClientRange': {},
     'cDhcpv4ServerClientServedProtocol': {},
     'cDhcpv4ServerClientSubnetMask': {},
     'cDhcpv4ServerClientTimeRemaining': {},
     'cDhcpv4ServerDefaultRouterAddress': {},
     'cDhcpv4ServerIfLeaseLimit': {},
     'cDhcpv4ServerRangeInUse': {},
     'cDhcpv4ServerRangeOutstandingOffers': {},
     'cDhcpv4ServerRangeSubnetMask': {},
     'cDhcpv4ServerSharedNetFreeAddrHighThreshold': {},
     'cDhcpv4ServerSharedNetFreeAddrLowThreshold': {},
     'cDhcpv4ServerSharedNetFreeAddresses': {},
     'cDhcpv4ServerSharedNetReservedAddresses': {},
     'cDhcpv4ServerSharedNetTotalAddresses': {},
     'cDhcpv4ServerSubnetEndAddress': {},
     'cDhcpv4ServerSubnetFreeAddrHighThreshold': {},
     'cDhcpv4ServerSubnetFreeAddrLowThreshold': {},
     'cDhcpv4ServerSubnetFreeAddresses': {},
     'cDhcpv4ServerSubnetMask': {},
     'cDhcpv4ServerSubnetSharedNetworkName': {},
     'cDhcpv4ServerSubnetStartAddress': {},
     'cDhcpv4SrvSystemDescr': {},
     'cDhcpv4SrvSystemObjectID': {},
     'cEigrpAcksRcvd': {},
     'cEigrpAcksSent': {},
     'cEigrpAcksSuppressed': {},
     'cEigrpActive': {},
     'cEigrpAsRouterId': {},
     'cEigrpAsRouterIdType': {},
     'cEigrpAuthKeyChain': {},
     'cEigrpAuthMode': {},
     'cEigrpCRpkts': {},
     'cEigrpDestSuccessors': {},
     'cEigrpDistance': {},
     'cEigrpFdistance': {},
     'cEigrpHeadSerial': {},
     'cEigrpHelloInterval': {},
     'cEigrpHellosRcvd': {},
     'cEigrpHellosSent': {},
     'cEigrpHoldTime': {},
     'cEigrpInputQDrops': {},
     'cEigrpInputQHighMark': {},
     'cEigrpLastSeq': {},
     'cEigrpMFlowTimer': {},
     'cEigrpMcastExcepts': {},
     'cEigrpMeanSrtt': {},
     'cEigrpNbrCount': {},
     'cEigrpNextHopAddress': {},
     'cEigrpNextHopAddressType': {},
     'cEigrpNextHopInterface': {},
     'cEigrpNextSerial': {},
     'cEigrpOOSrvcd': {},
     'cEigrpPacingReliable': {},
     'cEigrpPacingUnreliable': {},
     'cEigrpPeerAddr': {},
     'cEigrpPeerAddrType': {},
     'cEigrpPeerCount': {},
     'cEigrpPeerIfIndex': {},
     'cEigrpPendingRoutes': {},
     'cEigrpPktsEnqueued': {},
     'cEigrpQueriesRcvd': {},
     'cEigrpQueriesSent': {},
     'cEigrpRMcasts': {},
     'cEigrpRUcasts': {},
     'cEigrpRepliesRcvd': {},
     'cEigrpRepliesSent': {},
     'cEigrpReportDistance': {},
     'cEigrpRetrans': {},
     'cEigrpRetransSent': {},
     'cEigrpRetries': {},
     'cEigrpRouteOriginAddr': {},
     'cEigrpRouteOriginAddrType': {},
     'cEigrpRouteOriginType': {},
     'cEigrpRto': {},
     'cEigrpSiaQueriesRcvd': {},
     'cEigrpSiaQueriesSent': {},
     'cEigrpSrtt': {},
     'cEigrpStuckInActive': {},
     'cEigrpTopoEntry': {'17': {}, '18': {}, '19': {}},
     'cEigrpTopoRoutes': {},
     'cEigrpUMcasts': {},
     'cEigrpUUcasts': {},
     'cEigrpUpTime': {},
     'cEigrpUpdatesRcvd': {},
     'cEigrpUpdatesSent': {},
     'cEigrpVersion': {},
     'cEigrpVpnName': {},
     'cEigrpXmitDummies': {},
     'cEigrpXmitNextSerial': {},
     'cEigrpXmitPendReplies': {},
     'cEigrpXmitReliableQ': {},
     'cEigrpXmitUnreliableQ': {},
     'cEtherCfmEventCode': {},
     'cEtherCfmEventDeleteRow': {},
     'cEtherCfmEventDomainName': {},
     'cEtherCfmEventLastChange': {},
     'cEtherCfmEventLclIfCount': {},
     'cEtherCfmEventLclMacAddress': {},
     'cEtherCfmEventLclMepCount': {},
     'cEtherCfmEventLclMepid': {},
     'cEtherCfmEventRmtMacAddress': {},
     'cEtherCfmEventRmtMepid': {},
     'cEtherCfmEventRmtPortState': {},
     'cEtherCfmEventRmtServiceId': {},
     'cEtherCfmEventServiceId': {},
     'cEtherCfmEventType': {},
     'cEtherCfmMaxEventIndex': {},
     'cHsrpExtIfEntry': {'1': {}, '2': {}},
     'cHsrpExtIfTrackedEntry': {'2': {}, '3': {}},
     'cHsrpExtSecAddrEntry': {'2': {}},
     'cHsrpGlobalConfig': {'1': {}},
     'cHsrpGrpEntry': {'10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '15': {},
                       '16': {},
                       '17': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'cIgmpFilterApplyStatus': {},
     'cIgmpFilterEditEndAddress': {},
     'cIgmpFilterEditEndAddressType': {},
     'cIgmpFilterEditOperation': {},
     'cIgmpFilterEditProfileAction': {},
     'cIgmpFilterEditProfileIndex': {},
     'cIgmpFilterEditSpinLock': {},
     'cIgmpFilterEditStartAddress': {},
     'cIgmpFilterEditStartAddressType': {},
     'cIgmpFilterEnable': {},
     'cIgmpFilterEndAddress': {},
     'cIgmpFilterEndAddressType': {},
     'cIgmpFilterInterfaceProfileIndex': {},
     'cIgmpFilterMaxProfiles': {},
     'cIgmpFilterProfileAction': {},
     'cIpLocalPoolAllocEntry': {'3': {}, '4': {}},
     'cIpLocalPoolConfigEntry': {'4': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'cIpLocalPoolGroupContainsEntry': {'2': {}},
     'cIpLocalPoolGroupEntry': {'1': {}, '2': {}},
     'cIpLocalPoolNotificationsEnable': {},
     'cIpLocalPoolStatsEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'cMTCommonMetricsBitmaps': {},
     'cMTCommonMetricsFlowCounter': {},
     'cMTCommonMetricsFlowDirection': {},
     'cMTCommonMetricsFlowSamplingStartTime': {},
     'cMTCommonMetricsIpByteRate': {},
     'cMTCommonMetricsIpDscp': {},
     'cMTCommonMetricsIpOctets': {},
     'cMTCommonMetricsIpPktCount': {},
     'cMTCommonMetricsIpPktDropped': {},
     'cMTCommonMetricsIpProtocol': {},
     'cMTCommonMetricsIpTtl': {},
     'cMTCommonMetricsLossMeasurement': {},
     'cMTCommonMetricsMediaStopOccurred': {},
     'cMTCommonMetricsRouteForward': {},
     'cMTFlowSpecifierDestAddr': {},
     'cMTFlowSpecifierDestAddrType': {},
     'cMTFlowSpecifierDestPort': {},
     'cMTFlowSpecifierIpProtocol': {},
     'cMTFlowSpecifierMetadataGlobalId': {},
     'cMTFlowSpecifierRowStatus': {},
     'cMTFlowSpecifierSourceAddr': {},
     'cMTFlowSpecifierSourceAddrType': {},
     'cMTFlowSpecifierSourcePort': {},
     'cMTHopStatsCollectionStatus': {},
     'cMTHopStatsEgressInterface': {},
     'cMTHopStatsIngressInterface': {},
     'cMTHopStatsMaskBitmaps': {},
     'cMTHopStatsMediatraceTtl': {},
     'cMTHopStatsName': {},
     'cMTInitiatorActiveSessions': {},
     'cMTInitiatorConfiguredSessions': {},
     'cMTInitiatorEnable': {},
     'cMTInitiatorInactiveSessions': {},
     'cMTInitiatorMaxSessions': {},
     'cMTInitiatorPendingSessions': {},
     'cMTInitiatorProtocolVersionMajor': {},
     'cMTInitiatorProtocolVersionMinor': {},
     'cMTInitiatorSoftwareVersionMajor': {},
     'cMTInitiatorSoftwareVersionMinor': {},
     'cMTInitiatorSourceAddress': {},
     'cMTInitiatorSourceAddressType': {},
     'cMTInitiatorSourceInterface': {},
     'cMTInterfaceBitmaps': {},
     'cMTInterfaceInDiscards': {},
     'cMTInterfaceInErrors': {},
     'cMTInterfaceInOctets': {},
     'cMTInterfaceInSpeed': {},
     'cMTInterfaceOutDiscards': {},
     'cMTInterfaceOutErrors': {},
     'cMTInterfaceOutOctets': {},
     'cMTInterfaceOutSpeed': {},
     'cMTMediaMonitorProfileInterval': {},
     'cMTMediaMonitorProfileMetric': {},
     'cMTMediaMonitorProfileRowStatus': {},
     'cMTMediaMonitorProfileRtpMaxDropout': {},
     'cMTMediaMonitorProfileRtpMaxReorder': {},
     'cMTMediaMonitorProfileRtpMinimalSequential': {},
     'cMTPathHopAddr': {},
     'cMTPathHopAddrType': {},
     'cMTPathHopAlternate1Addr': {},
     'cMTPathHopAlternate1AddrType': {},
     'cMTPathHopAlternate2Addr': {},
     'cMTPathHopAlternate2AddrType': {},
     'cMTPathHopAlternate3Addr': {},
     'cMTPathHopAlternate3AddrType': {},
     'cMTPathHopType': {},
     'cMTPathSpecifierDestAddr': {},
     'cMTPathSpecifierDestAddrType': {},
     'cMTPathSpecifierDestPort': {},
     'cMTPathSpecifierGatewayAddr': {},
     'cMTPathSpecifierGatewayAddrType': {},
     'cMTPathSpecifierGatewayVlanId': {},
     'cMTPathSpecifierIpProtocol': {},
     'cMTPathSpecifierMetadataGlobalId': {},
     'cMTPathSpecifierProtocolForDiscovery': {},
     'cMTPathSpecifierRowStatus': {},
     'cMTPathSpecifierSourceAddr': {},
     'cMTPathSpecifierSourceAddrType': {},
     'cMTPathSpecifierSourcePort': {},
     'cMTResponderActiveSessions': {},
     'cMTResponderEnable': {},
     'cMTResponderMaxSessions': {},
     'cMTRtpMetricsBitRate': {},
     'cMTRtpMetricsBitmaps': {},
     'cMTRtpMetricsExpectedPkts': {},
     'cMTRtpMetricsJitter': {},
     'cMTRtpMetricsLossPercent': {},
     'cMTRtpMetricsLostPktEvents': {},
     'cMTRtpMetricsLostPkts': {},
     'cMTRtpMetricsOctets': {},
     'cMTRtpMetricsPkts': {},
     'cMTScheduleEntryAgeout': {},
     'cMTScheduleLife': {},
     'cMTScheduleRecurring': {},
     'cMTScheduleRowStatus': {},
     'cMTScheduleStartTime': {},
     'cMTSessionFlowSpecifierName': {},
     'cMTSessionParamName': {},
     'cMTSessionParamsFrequency': {},
     'cMTSessionParamsHistoryBuckets': {},
     'cMTSessionParamsInactivityTimeout': {},
     'cMTSessionParamsResponseTimeout': {},
     'cMTSessionParamsRouteChangeReactiontime': {},
     'cMTSessionParamsRowStatus': {},
     'cMTSessionPathSpecifierName': {},
     'cMTSessionProfileName': {},
     'cMTSessionRequestStatsBitmaps': {},
     'cMTSessionRequestStatsMDAppName': {},
     'cMTSessionRequestStatsMDGlobalId': {},
     'cMTSessionRequestStatsMDMultiPartySessionId': {},
     'cMTSessionRequestStatsNumberOfErrorHops': {},
     'cMTSessionRequestStatsNumberOfMediatraceHops': {},
     'cMTSessionRequestStatsNumberOfNoDataRecordHops': {},
     'cMTSessionRequestStatsNumberOfNonMediatraceHops': {},
     'cMTSessionRequestStatsNumberOfValidHops': {},
     'cMTSessionRequestStatsRequestStatus': {},
     'cMTSessionRequestStatsRequestTimestamp': {},
     'cMTSessionRequestStatsRouteIndex': {},
     'cMTSessionRequestStatsTracerouteStatus': {},
     'cMTSessionRowStatus': {},
     'cMTSessionStatusBitmaps': {},
     'cMTSessionStatusGlobalSessionId': {},
     'cMTSessionStatusOperationState': {},
     'cMTSessionStatusOperationTimeToLive': {},
     'cMTSessionTraceRouteEnabled': {},
     'cMTSystemMetricBitmaps': {},
     'cMTSystemMetricCpuFiveMinutesUtilization': {},
     'cMTSystemMetricCpuOneMinuteUtilization': {},
     'cMTSystemMetricMemoryUtilization': {},
     'cMTSystemProfileMetric': {},
     'cMTSystemProfileRowStatus': {},
     'cMTTcpMetricBitmaps': {},
     'cMTTcpMetricConnectRoundTripDelay': {},
     'cMTTcpMetricLostEventCount': {},
     'cMTTcpMetricMediaByteCount': {},
     'cMTTraceRouteHopNumber': {},
     'cMTTraceRouteHopRtt': {},
     'cPeerSearchType': {},
     'cPppoeFwdedSessions': {},
     'cPppoePerInterfaceSessionLossPercent': {},
     'cPppoePerInterfaceSessionLossThreshold': {},
     'cPppoePtaSessions': {},
     'cPppoeSystemCurrSessions': {},
     'cPppoeSystemExceededSessionErrors': {},
     'cPppoeSystemHighWaterSessions': {},
     'cPppoeSystemMaxAllowedSessions': {},
     'cPppoeSystemPerMACSessionIWFlimit': {},
     'cPppoeSystemPerMACSessionlimit': {},
     'cPppoeSystemPerMacThrottleRatelimit': {},
     'cPppoeSystemPerVCThrottleRatelimit': {},
     'cPppoeSystemPerVClimit': {},
     'cPppoeSystemPerVLANlimit': {},
     'cPppoeSystemPerVLANthrottleRatelimit': {},
     'cPppoeSystemSessionLossPercent': {},
     'cPppoeSystemSessionLossThreshold': {},
     'cPppoeSystemSessionNotifyObjects': {'1': {},
                                          '2': {},
                                          '3': {},
                                          '4': {},
                                          '5': {}},
     'cPppoeSystemThresholdSessions': {},
     'cPppoeTotalSessions': {},
     'cPppoeTransSessions': {},
     'cPppoeVcCurrSessions': {},
     'cPppoeVcExceededSessionErrors': {},
     'cPppoeVcHighWaterSessions': {},
     'cPppoeVcMaxAllowedSessions': {},
     'cPppoeVcThresholdSessions': {},
     'cPtpClockCurrentDSMeanPathDelay': {},
     'cPtpClockCurrentDSOffsetFromMaster': {},
     'cPtpClockCurrentDSStepsRemoved': {},
     'cPtpClockDefaultDSClockIdentity': {},
     'cPtpClockDefaultDSPriority1': {},
     'cPtpClockDefaultDSPriority2': {},
     'cPtpClockDefaultDSQualityAccuracy': {},
     'cPtpClockDefaultDSQualityClass': {},
     'cPtpClockDefaultDSQualityOffset': {},
     'cPtpClockDefaultDSSlaveOnly': {},
     'cPtpClockDefaultDSTwoStepFlag': {},
     'cPtpClockInput1ppsEnabled': {},
     'cPtpClockInput1ppsInterface': {},
     'cPtpClockInputFrequencyEnabled': {},
     'cPtpClockOutput1ppsEnabled': {},
     'cPtpClockOutput1ppsInterface': {},
     'cPtpClockOutput1ppsOffsetEnabled': {},
     'cPtpClockOutput1ppsOffsetNegative': {},
     'cPtpClockOutput1ppsOffsetValue': {},
     'cPtpClockParentDSClockPhChRate': {},
     'cPtpClockParentDSGMClockIdentity': {},
     'cPtpClockParentDSGMClockPriority1': {},
     'cPtpClockParentDSGMClockPriority2': {},
     'cPtpClockParentDSGMClockQualityAccuracy': {},
     'cPtpClockParentDSGMClockQualityClass': {},
     'cPtpClockParentDSGMClockQualityOffset': {},
     'cPtpClockParentDSOffset': {},
     'cPtpClockParentDSParentPortIdentity': {},
     'cPtpClockParentDSParentStats': {},
     'cPtpClockPortAssociateAddress': {},
     'cPtpClockPortAssociateAddressType': {},
     'cPtpClockPortAssociateInErrors': {},
     'cPtpClockPortAssociateOutErrors': {},
     'cPtpClockPortAssociatePacketsReceived': {},
     'cPtpClockPortAssociatePacketsSent': {},
     'cPtpClockPortCurrentPeerAddress': {},
     'cPtpClockPortCurrentPeerAddressType': {},
     'cPtpClockPortDSAnnounceRctTimeout': {},
     'cPtpClockPortDSAnnouncementInterval': {},
     'cPtpClockPortDSDelayMech': {},
     'cPtpClockPortDSGrantDuration': {},
     'cPtpClockPortDSMinDelayReqInterval': {},
     'cPtpClockPortDSName': {},
     'cPtpClockPortDSPTPVersion': {},
     'cPtpClockPortDSPeerDelayReqInterval': {},
     'cPtpClockPortDSPeerMeanPathDelay': {},
     'cPtpClockPortDSPortIdentity': {},
     'cPtpClockPortDSSyncInterval': {},
     'cPtpClockPortName': {},
     'cPtpClockPortNumOfAssociatedPorts': {},
     'cPtpClockPortRole': {},
     'cPtpClockPortRunningEncapsulationType': {},
     'cPtpClockPortRunningIPversion': {},
     'cPtpClockPortRunningInterfaceIndex': {},
     'cPtpClockPortRunningName': {},
     'cPtpClockPortRunningPacketsReceived': {},
     'cPtpClockPortRunningPacketsSent': {},
     'cPtpClockPortRunningRole': {},
     'cPtpClockPortRunningRxMode': {},
     'cPtpClockPortRunningState': {},
     'cPtpClockPortRunningTxMode': {},
     'cPtpClockPortSyncOneStep': {},
     'cPtpClockPortTransDSFaultyFlag': {},
     'cPtpClockPortTransDSPeerMeanPathDelay': {},
     'cPtpClockPortTransDSPortIdentity': {},
     'cPtpClockPortTransDSlogMinPdelayReqInt': {},
     'cPtpClockRunningPacketsReceived': {},
     'cPtpClockRunningPacketsSent': {},
     'cPtpClockRunningState': {},
     'cPtpClockTODEnabled': {},
     'cPtpClockTODInterface': {},
     'cPtpClockTimePropertiesDSCurrentUTCOffset': {},
     'cPtpClockTimePropertiesDSCurrentUTCOffsetValid': {},
     'cPtpClockTimePropertiesDSFreqTraceable': {},
     'cPtpClockTimePropertiesDSLeap59': {},
     'cPtpClockTimePropertiesDSLeap61': {},
     'cPtpClockTimePropertiesDSPTPTimescale': {},
     'cPtpClockTimePropertiesDSSource': {},
     'cPtpClockTimePropertiesDSTimeTraceable': {},
     'cPtpClockTransDefaultDSClockIdentity': {},
     'cPtpClockTransDefaultDSDelay': {},
     'cPtpClockTransDefaultDSNumOfPorts': {},
     'cPtpClockTransDefaultDSPrimaryDomain': {},
     'cPtpDomainClockPortPhysicalInterfacesTotal': {},
     'cPtpDomainClockPortsTotal': {},
     'cPtpSystemDomainTotals': {},
     'cPtpSystemProfile': {},
     'cQIfEntry': {'1': {}, '2': {}, '3': {}},
     'cQRotationEntry': {'1': {}},
     'cQStatsEntry': {'2': {}, '3': {}, '4': {}},
     'cRFCfgAdminAction': {},
     'cRFCfgKeepaliveThresh': {},
     'cRFCfgKeepaliveThreshMax': {},
     'cRFCfgKeepaliveThreshMin': {},
     'cRFCfgKeepaliveTimer': {},
     'cRFCfgKeepaliveTimerMax': {},
     'cRFCfgKeepaliveTimerMin': {},
     'cRFCfgMaintenanceMode': {},
     'cRFCfgNotifTimer': {},
     'cRFCfgNotifTimerMax': {},
     'cRFCfgNotifTimerMin': {},
     'cRFCfgNotifsEnabled': {},
     'cRFCfgRedundancyMode': {},
     'cRFCfgRedundancyModeDescr': {},
     'cRFCfgRedundancyOperMode': {},
     'cRFCfgSplitMode': {},
     'cRFHistoryColdStarts': {},
     'cRFHistoryCurrActiveUnitId': {},
     'cRFHistoryPrevActiveUnitId': {},
     'cRFHistoryStandByAvailTime': {},
     'cRFHistorySwactTime': {},
     'cRFHistorySwitchOverReason': {},
     'cRFHistoryTableMaxLength': {},
     'cRFStatusDomainInstanceEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cRFStatusDuplexMode': {},
     'cRFStatusFailoverTime': {},
     'cRFStatusIssuFromVersion': {},
     'cRFStatusIssuState': {},
     'cRFStatusIssuStateRev1': {},
     'cRFStatusIssuToVersion': {},
     'cRFStatusLastSwactReasonCode': {},
     'cRFStatusManualSwactInhibit': {},
     'cRFStatusPeerStandByEntryTime': {},
     'cRFStatusPeerUnitId': {},
     'cRFStatusPeerUnitState': {},
     'cRFStatusPrimaryMode': {},
     'cRFStatusRFModeCapsModeDescr': {},
     'cRFStatusUnitId': {},
     'cRFStatusUnitState': {},
     'cSipCfgAaa': {'1': {}},
     'cSipCfgBase': {'1': {},
                     '10': {},
                     '11': {},
                     '13': {},
                     '14': {},
                     '15': {},
                     '16': {},
                     '17': {},
                     '18': {},
                     '19': {},
                     '2': {},
                     '20': {},
                     '21': {},
                     '22': {},
                     '23': {},
                     '24': {},
                     '25': {},
                     '26': {},
                     '27': {},
                     '28': {},
                     '29': {},
                     '3': {},
                     '30': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {}},
     'cSipCfgBase.12.1.2': {},
     'cSipCfgBase.9.1.2': {},
     'cSipCfgPeer': {'10': {},
                     '11': {},
                     '12': {},
                     '13': {},
                     '14': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'cSipCfgPeer.1.1.10': {},
     'cSipCfgPeer.1.1.11': {},
     'cSipCfgPeer.1.1.12': {},
     'cSipCfgPeer.1.1.13': {},
     'cSipCfgPeer.1.1.14': {},
     'cSipCfgPeer.1.1.15': {},
     'cSipCfgPeer.1.1.16': {},
     'cSipCfgPeer.1.1.17': {},
     'cSipCfgPeer.1.1.18': {},
     'cSipCfgPeer.1.1.2': {},
     'cSipCfgPeer.1.1.3': {},
     'cSipCfgPeer.1.1.4': {},
     'cSipCfgPeer.1.1.5': {},
     'cSipCfgPeer.1.1.6': {},
     'cSipCfgPeer.1.1.7': {},
     'cSipCfgPeer.1.1.8': {},
     'cSipCfgPeer.1.1.9': {},
     'cSipCfgRetry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'cSipCfgStatusCauseMap.1.1.2': {},
     'cSipCfgStatusCauseMap.1.1.3': {},
     'cSipCfgStatusCauseMap.2.1.2': {},
     'cSipCfgStatusCauseMap.2.1.3': {},
     'cSipCfgTimer': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'cSipStatsErrClient': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '2': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '26': {},
                            '27': {},
                            '28': {},
                            '29': {},
                            '3': {},
                            '30': {},
                            '31': {},
                            '32': {},
                            '33': {},
                            '34': {},
                            '35': {},
                            '36': {},
                            '37': {},
                            '38': {},
                            '39': {},
                            '4': {},
                            '40': {},
                            '41': {},
                            '42': {},
                            '43': {},
                            '44': {},
                            '45': {},
                            '46': {},
                            '47': {},
                            '48': {},
                            '49': {},
                            '5': {},
                            '50': {},
                            '51': {},
                            '52': {},
                            '53': {},
                            '54': {},
                            '55': {},
                            '56': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'cSipStatsErrServer': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'cSipStatsGlobalFail': {'1': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {}},
     'cSipStatsInfo': {'1': {},
                       '10': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'cSipStatsRedirect': {'1': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {}},
     'cSipStatsRetry': {'1': {},
                        '10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'cSipStatsSuccess': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cSipStatsSuccess.5.1.2': {},
     'cSipStatsSuccess.5.1.3': {},
     'cSipStatsTraffic': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '25': {},
                          '26': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'callActiveCallOrigin': {},
     'callActiveCallState': {},
     'callActiveChargedUnits': {},
     'callActiveConnectTime': {},
     'callActiveInfoType': {},
     'callActiveLogicalIfIndex': {},
     'callActivePeerAddress': {},
     'callActivePeerId': {},
     'callActivePeerIfIndex': {},
     'callActivePeerSubAddress': {},
     'callActiveReceiveBytes': {},
     'callActiveReceivePackets': {},
     'callActiveTransmitBytes': {},
     'callActiveTransmitPackets': {},
     'callHistoryCallOrigin': {},
     'callHistoryChargedUnits': {},
     'callHistoryConnectTime': {},
     'callHistoryDisconnectCause': {},
     'callHistoryDisconnectText': {},
     'callHistoryDisconnectTime': {},
     'callHistoryInfoType': {},
     'callHistoryLogicalIfIndex': {},
     'callHistoryPeerAddress': {},
     'callHistoryPeerId': {},
     'callHistoryPeerIfIndex': {},
     'callHistoryPeerSubAddress': {},
     'callHistoryReceiveBytes': {},
     'callHistoryReceivePackets': {},
     'callHistoryRetainTimer': {},
     'callHistoryTableMaxLength': {},
     'callHistoryTransmitBytes': {},
     'callHistoryTransmitPackets': {},
     'callHomeAlertGroupTypeEntry': {'2': {}, '3': {}, '4': {}},
     'callHomeDestEmailAddressEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'callHomeDestProfileEntry': {'2': {},
                                  '3': {},
                                  '4': {},
                                  '5': {},
                                  '6': {},
                                  '7': {},
                                  '8': {},
                                  '9': {}},
     'callHomeSwInventoryEntry': {'3': {}, '4': {}},
     'callHomeUserDefCmdEntry': {'2': {}, '3': {}},
     'caqQueuingParamsClassEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'caqQueuingParamsEntry': {'1': {}},
     'caqVccParamsEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '16': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'caqVpcParamsEntry': {'1': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cardIfIndexEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'cardTableEntry': {'1': {},
                        '10': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'casAcctIncorrectResponses': {},
     'casAcctPort': {},
     'casAcctRequestTimeouts': {},
     'casAcctRequests': {},
     'casAcctResponseTime': {},
     'casAcctServerErrorResponses': {},
     'casAcctTransactionFailures': {},
     'casAcctTransactionSuccesses': {},
     'casAcctUnexpectedResponses': {},
     'casAddress': {},
     'casAuthenIncorrectResponses': {},
     'casAuthenPort': {},
     'casAuthenRequestTimeouts': {},
     'casAuthenRequests': {},
     'casAuthenResponseTime': {},
     'casAuthenServerErrorResponses': {},
     'casAuthenTransactionFailures': {},
     'casAuthenTransactionSuccesses': {},
     'casAuthenUnexpectedResponses': {},
     'casAuthorIncorrectResponses': {},
     'casAuthorRequestTimeouts': {},
     'casAuthorRequests': {},
     'casAuthorResponseTime': {},
     'casAuthorServerErrorResponses': {},
     'casAuthorTransactionFailures': {},
     'casAuthorTransactionSuccesses': {},
     'casAuthorUnexpectedResponses': {},
     'casConfigRowStatus': {},
     'casCurrentStateDuration': {},
     'casDeadCount': {},
     'casKey': {},
     'casPreviousStateDuration': {},
     'casPriority': {},
     'casServerStateChangeEnable': {},
     'casState': {},
     'casTotalDeadTime': {},
     'catmDownPVclHigherRangeValue': {},
     'catmDownPVclLowerRangeValue': {},
     'catmDownPVclRangeEnd': {},
     'catmDownPVclRangeStart': {},
     'catmIntfAISRDIOAMFailedPVcls': {},
     'catmIntfAISRDIOAMRcovedPVcls': {},
     'catmIntfAnyOAMFailedPVcls': {},
     'catmIntfAnyOAMRcovedPVcls': {},
     'catmIntfCurAISRDIOAMFailingPVcls': {},
     'catmIntfCurAISRDIOAMRcovingPVcls': {},
     'catmIntfCurAnyOAMFailingPVcls': {},
     'catmIntfCurAnyOAMRcovingPVcls': {},
     'catmIntfCurEndAISRDIFailingPVcls': {},
     'catmIntfCurEndAISRDIRcovingPVcls': {},
     'catmIntfCurEndCCOAMFailingPVcls': {},
     'catmIntfCurEndCCOAMRcovingPVcls': {},
     'catmIntfCurSegAISRDIFailingPVcls': {},
     'catmIntfCurSegAISRDIRcovingPVcls': {},
     'catmIntfCurSegCCOAMFailingPVcls': {},
     'catmIntfCurSegCCOAMRcovingPVcls': {},
     'catmIntfCurrentOAMFailingPVcls': {},
     'catmIntfCurrentOAMRcovingPVcls': {},
     'catmIntfCurrentlyDownToUpPVcls': {},
     'catmIntfEndAISRDIFailedPVcls': {},
     'catmIntfEndAISRDIRcovedPVcls': {},
     'catmIntfEndCCOAMFailedPVcls': {},
     'catmIntfEndCCOAMRcovedPVcls': {},
     'catmIntfOAMFailedPVcls': {},
     'catmIntfOAMRcovedPVcls': {},
     'catmIntfSegAISRDIFailedPVcls': {},
     'catmIntfSegAISRDIRcovedPVcls': {},
     'catmIntfSegCCOAMFailedPVcls': {},
     'catmIntfSegCCOAMRcovedPVcls': {},
     'catmIntfTypeOfOAMFailure': {},
     'catmIntfTypeOfOAMRecover': {},
     'catmPVclAISRDIHigherRangeValue': {},
     'catmPVclAISRDILowerRangeValue': {},
     'catmPVclAISRDIRangeStatusChEnd': {},
     'catmPVclAISRDIRangeStatusChStart': {},
     'catmPVclAISRDIRangeStatusUpEnd': {},
     'catmPVclAISRDIRangeStatusUpStart': {},
     'catmPVclAISRDIStatusChangeEnd': {},
     'catmPVclAISRDIStatusChangeStart': {},
     'catmPVclAISRDIStatusTransition': {},
     'catmPVclAISRDIStatusUpEnd': {},
     'catmPVclAISRDIStatusUpStart': {},
     'catmPVclAISRDIStatusUpTransition': {},
     'catmPVclAISRDIUpHigherRangeValue': {},
     'catmPVclAISRDIUpLowerRangeValue': {},
     'catmPVclCurFailTime': {},
     'catmPVclCurRecoverTime': {},
     'catmPVclEndAISRDIHigherRngeValue': {},
     'catmPVclEndAISRDILowerRangeValue': {},
     'catmPVclEndAISRDIRangeStatChEnd': {},
     'catmPVclEndAISRDIRangeStatUpEnd': {},
     'catmPVclEndAISRDIRngeStatChStart': {},
     'catmPVclEndAISRDIRngeStatUpStart': {},
     'catmPVclEndAISRDIStatChangeEnd': {},
     'catmPVclEndAISRDIStatChangeStart': {},
     'catmPVclEndAISRDIStatTransition': {},
     'catmPVclEndAISRDIStatUpEnd': {},
     'catmPVclEndAISRDIStatUpStart': {},
     'catmPVclEndAISRDIStatUpTransit': {},
     'catmPVclEndAISRDIUpHigherRngeVal': {},
     'catmPVclEndAISRDIUpLowerRangeVal': {},
     'catmPVclEndCCHigherRangeValue': {},
     'catmPVclEndCCLowerRangeValue': {},
     'catmPVclEndCCRangeStatusChEnd': {},
     'catmPVclEndCCRangeStatusChStart': {},
     'catmPVclEndCCRangeStatusUpEnd': {},
     'catmPVclEndCCRangeStatusUpStart': {},
     'catmPVclEndCCStatusChangeEnd': {},
     'catmPVclEndCCStatusChangeStart': {},
     'catmPVclEndCCStatusTransition': {},
     'catmPVclEndCCStatusUpEnd': {},
     'catmPVclEndCCStatusUpStart': {},
     'catmPVclEndCCStatusUpTransition': {},
     'catmPVclEndCCUpHigherRangeValue': {},
     'catmPVclEndCCUpLowerRangeValue': {},
     'catmPVclFailureReason': {},
     'catmPVclHigherRangeValue': {},
     'catmPVclLowerRangeValue': {},
     'catmPVclPrevFailTime': {},
     'catmPVclPrevRecoverTime': {},
     'catmPVclRangeFailureReason': {},
     'catmPVclRangeRecoveryReason': {},
     'catmPVclRangeStatusChangeEnd': {},
     'catmPVclRangeStatusChangeStart': {},
     'catmPVclRangeStatusUpEnd': {},
     'catmPVclRangeStatusUpStart': {},
     'catmPVclRecoveryReason': {},
     'catmPVclSegAISRDIHigherRangeValue': {},
     'catmPVclSegAISRDILowerRangeValue': {},
     'catmPVclSegAISRDIRangeStatChEnd': {},
     'catmPVclSegAISRDIRangeStatChStart': {},
     'catmPVclSegAISRDIRangeStatUpEnd': {},
     'catmPVclSegAISRDIRngeStatUpStart': {},
     'catmPVclSegAISRDIStatChangeEnd': {},
     'catmPVclSegAISRDIStatChangeStart': {},
     'catmPVclSegAISRDIStatTransition': {},
     'catmPVclSegAISRDIStatUpEnd': {},
     'catmPVclSegAISRDIStatUpStart': {},
     'catmPVclSegAISRDIStatUpTransit': {},
     'catmPVclSegAISRDIUpHigherRngeVal': {},
     'catmPVclSegAISRDIUpLowerRangeVal': {},
     'catmPVclSegCCHigherRangeValue': {},
     'catmPVclSegCCLowerRangeValue': {},
     'catmPVclSegCCRangeStatusChEnd': {},
     'catmPVclSegCCRangeStatusChStart': {},
     'catmPVclSegCCRangeStatusUpEnd': {},
     'catmPVclSegCCRangeStatusUpStart': {},
     'catmPVclSegCCStatusChangeEnd': {},
     'catmPVclSegCCStatusChangeStart': {},
     'catmPVclSegCCStatusTransition': {},
     'catmPVclSegCCStatusUpEnd': {},
     'catmPVclSegCCStatusUpStart': {},
     'catmPVclSegCCStatusUpTransition': {},
     'catmPVclSegCCUpHigherRangeValue': {},
     'catmPVclSegCCUpLowerRangeValue': {},
     'catmPVclStatusChangeEnd': {},
     'catmPVclStatusChangeStart': {},
     'catmPVclStatusTransition': {},
     'catmPVclStatusUpEnd': {},
     'catmPVclStatusUpStart': {},
     'catmPVclStatusUpTransition': {},
     'catmPVclUpHigherRangeValue': {},
     'catmPVclUpLowerRangeValue': {},
     'catmPrevDownPVclRangeEnd': {},
     'catmPrevDownPVclRangeStart': {},
     'catmPrevUpPVclRangeEnd': {},
     'catmPrevUpPVclRangeStart': {},
     'catmUpPVclHigherRangeValue': {},
     'catmUpPVclLowerRangeValue': {},
     'catmUpPVclRangeEnd': {},
     'catmUpPVclRangeStart': {},
     'cbQosATMPVCPolicyEntry': {'1': {}},
     'cbQosCMCfgEntry': {'1': {}, '2': {}, '3': {}},
     'cbQosCMStatsEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '16': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '20': {},
                           '21': {},
                           '22': {},
                           '23': {},
                           '24': {},
                           '25': {},
                           '26': {},
                           '27': {},
                           '28': {},
                           '29': {},
                           '3': {},
                           '30': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cbQosEBCfgEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cbQosEBStatsEntry': {'1': {}, '2': {}, '3': {}},
     'cbQosFrameRelayPolicyEntry': {'1': {}},
     'cbQosIPHCCfgEntry': {'1': {}, '2': {}},
     'cbQosIPHCStatsEntry': {'1': {},
                             '10': {},
                             '11': {},
                             '12': {},
                             '13': {},
                             '14': {},
                             '15': {},
                             '16': {},
                             '17': {},
                             '18': {},
                             '19': {},
                             '2': {},
                             '20': {},
                             '21': {},
                             '22': {},
                             '23': {},
                             '24': {},
                             '25': {},
                             '26': {},
                             '27': {},
                             '28': {},
                             '29': {},
                             '3': {},
                             '30': {},
                             '31': {},
                             '32': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'cbQosInterfacePolicyEntry': {'1': {}},
     'cbQosMatchStmtCfgEntry': {'1': {}, '2': {}},
     'cbQosMatchStmtStatsEntry': {'1': {},
                                  '2': {},
                                  '3': {},
                                  '4': {},
                                  '5': {},
                                  '6': {},
                                  '7': {}},
     'cbQosObjectsEntry': {'2': {}, '3': {}, '4': {}},
     'cbQosPoliceActionCfgEntry': {'2': {},
                                   '3': {},
                                   '4': {},
                                   '5': {},
                                   '6': {},
                                   '7': {}},
     'cbQosPoliceCfgEntry': {'1': {},
                             '10': {},
                             '11': {},
                             '12': {},
                             '13': {},
                             '14': {},
                             '15': {},
                             '16': {},
                             '17': {},
                             '18': {},
                             '19': {},
                             '2': {},
                             '20': {},
                             '21': {},
                             '22': {},
                             '23': {},
                             '24': {},
                             '25': {},
                             '26': {},
                             '27': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'cbQosPoliceColorStatsEntry': {'1': {},
                                    '10': {},
                                    '11': {},
                                    '12': {},
                                    '13': {},
                                    '14': {},
                                    '15': {},
                                    '16': {},
                                    '17': {},
                                    '18': {},
                                    '2': {},
                                    '3': {},
                                    '4': {},
                                    '5': {},
                                    '6': {},
                                    '7': {},
                                    '8': {},
                                    '9': {}},
     'cbQosPoliceStatsEntry': {'1': {},
                               '10': {},
                               '11': {},
                               '12': {},
                               '13': {},
                               '14': {},
                               '15': {},
                               '16': {},
                               '17': {},
                               '18': {},
                               '19': {},
                               '2': {},
                               '20': {},
                               '21': {},
                               '22': {},
                               '23': {},
                               '24': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cbQosPolicyMapCfgEntry': {'1': {}, '2': {}},
     'cbQosQueueingCfgEntry': {'1': {},
                               '10': {},
                               '11': {},
                               '12': {},
                               '13': {},
                               '14': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cbQosQueueingStatsEntry': {'1': {},
                                 '10': {},
                                 '11': {},
                                 '12': {},
                                 '2': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {},
                                 '9': {}},
     'cbQosREDCfgEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cbQosREDClassCfgEntry': {'10': {},
                               '11': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cbQosREDClassStatsEntry': {'1': {},
                                 '10': {},
                                 '11': {},
                                 '12': {},
                                 '13': {},
                                 '14': {},
                                 '15': {},
                                 '16': {},
                                 '17': {},
                                 '18': {},
                                 '19': {},
                                 '2': {},
                                 '20': {},
                                 '21': {},
                                 '22': {},
                                 '23': {},
                                 '24': {},
                                 '25': {},
                                 '26': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {},
                                 '9': {}},
     'cbQosServicePolicyEntry': {'10': {},
                                 '11': {},
                                 '12': {},
                                 '13': {},
                                 '14': {},
                                 '15': {},
                                 '2': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {}},
     'cbQosSetCfgEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'cbQosSetStatsEntry': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'cbQosTSCfgEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'cbQosTSStatsEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cbQosTableMapCfgEntry': {'2': {}, '3': {}, '4': {}},
     'cbQosTableMapSetCfgEntry': {'1': {},
                                  '10': {},
                                  '11': {},
                                  '12': {},
                                  '2': {},
                                  '3': {},
                                  '4': {},
                                  '5': {},
                                  '6': {},
                                  '7': {},
                                  '8': {},
                                  '9': {}},
     'cbQosTableMapValueCfgEntry': {'2': {}},
     'cbQosVlanIndex': {},
     'cbfDefineFileTable.1.2': {},
     'cbfDefineFileTable.1.3': {},
     'cbfDefineFileTable.1.4': {},
     'cbfDefineFileTable.1.5': {},
     'cbfDefineFileTable.1.6': {},
     'cbfDefineFileTable.1.7': {},
     'cbfDefineObjectTable.1.2': {},
     'cbfDefineObjectTable.1.3': {},
     'cbfDefineObjectTable.1.4': {},
     'cbfDefineObjectTable.1.5': {},
     'cbfDefineObjectTable.1.6': {},
     'cbfDefineObjectTable.1.7': {},
     'cbfStatusFileTable.1.2': {},
     'cbfStatusFileTable.1.3': {},
     'cbfStatusFileTable.1.4': {},
     'cbgpGlobal': {'2': {}},
     'cbgpNotifsEnable': {},
     'cbgpPeer2AcceptedPrefixes': {},
     'cbgpPeer2AddrFamilyName': {},
     'cbgpPeer2AdminStatus': {},
     'cbgpPeer2AdvertisedPrefixes': {},
     'cbgpPeer2CapValue': {},
     'cbgpPeer2ConnectRetryInterval': {},
     'cbgpPeer2DeniedPrefixes': {},
     'cbgpPeer2FsmEstablishedTime': {},
     'cbgpPeer2FsmEstablishedTransitions': {},
     'cbgpPeer2HoldTime': {},
     'cbgpPeer2HoldTimeConfigured': {},
     'cbgpPeer2InTotalMessages': {},
     'cbgpPeer2InUpdateElapsedTime': {},
     'cbgpPeer2InUpdates': {},
     'cbgpPeer2KeepAlive': {},
     'cbgpPeer2KeepAliveConfigured': {},
     'cbgpPeer2LastError': {},
     'cbgpPeer2LastErrorTxt': {},
     'cbgpPeer2LocalAddr': {},
     'cbgpPeer2LocalAs': {},
     'cbgpPeer2LocalIdentifier': {},
     'cbgpPeer2LocalPort': {},
     'cbgpPeer2MinASOriginationInterval': {},
     'cbgpPeer2MinRouteAdvertisementInterval': {},
     'cbgpPeer2NegotiatedVersion': {},
     'cbgpPeer2OutTotalMessages': {},
     'cbgpPeer2OutUpdates': {},
     'cbgpPeer2PrefixAdminLimit': {},
     'cbgpPeer2PrefixClearThreshold': {},
     'cbgpPeer2PrefixThreshold': {},
     'cbgpPeer2PrevState': {},
     'cbgpPeer2RemoteAs': {},
     'cbgpPeer2RemoteIdentifier': {},
     'cbgpPeer2RemotePort': {},
     'cbgpPeer2State': {},
     'cbgpPeer2SuppressedPrefixes': {},
     'cbgpPeer2WithdrawnPrefixes': {},
     'cbgpPeerAcceptedPrefixes': {},
     'cbgpPeerAddrFamilyName': {},
     'cbgpPeerAddrFamilyPrefixEntry': {'3': {}, '4': {}, '5': {}},
     'cbgpPeerAdvertisedPrefixes': {},
     'cbgpPeerCapValue': {},
     'cbgpPeerDeniedPrefixes': {},
     'cbgpPeerEntry': {'7': {}, '8': {}},
     'cbgpPeerPrefixAccepted': {},
     'cbgpPeerPrefixAdvertised': {},
     'cbgpPeerPrefixDenied': {},
     'cbgpPeerPrefixLimit': {},
     'cbgpPeerPrefixSuppressed': {},
     'cbgpPeerPrefixWithdrawn': {},
     'cbgpPeerSuppressedPrefixes': {},
     'cbgpPeerWithdrawnPrefixes': {},
     'cbgpRouteASPathSegment': {},
     'cbgpRouteAggregatorAS': {},
     'cbgpRouteAggregatorAddr': {},
     'cbgpRouteAggregatorAddrType': {},
     'cbgpRouteAtomicAggregate': {},
     'cbgpRouteBest': {},
     'cbgpRouteLocalPref': {},
     'cbgpRouteLocalPrefPresent': {},
     'cbgpRouteMedPresent': {},
     'cbgpRouteMultiExitDisc': {},
     'cbgpRouteNextHop': {},
     'cbgpRouteOrigin': {},
     'cbgpRouteUnknownAttr': {},
     'cbpAcctEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ccCopyTable.1.10': {},
     'ccCopyTable.1.11': {},
     'ccCopyTable.1.12': {},
     'ccCopyTable.1.13': {},
     'ccCopyTable.1.14': {},
     'ccCopyTable.1.15': {},
     'ccCopyTable.1.16': {},
     'ccCopyTable.1.2': {},
     'ccCopyTable.1.3': {},
     'ccCopyTable.1.4': {},
     'ccCopyTable.1.5': {},
     'ccCopyTable.1.6': {},
     'ccCopyTable.1.7': {},
     'ccCopyTable.1.8': {},
     'ccCopyTable.1.9': {},
     'ccVoIPCallActivePolicyName': {},
     'ccapAppActiveInstances': {},
     'ccapAppCallType': {},
     'ccapAppDescr': {},
     'ccapAppEventLogging': {},
     'ccapAppGblActCurrentInstances': {},
     'ccapAppGblActHandoffInProgress': {},
     'ccapAppGblActIPInCallNowConn': {},
     'ccapAppGblActIPOutCallNowConn': {},
     'ccapAppGblActPSTNInCallNowConn': {},
     'ccapAppGblActPSTNOutCallNowConn': {},
     'ccapAppGblActPlaceCallInProgress': {},
     'ccapAppGblActPromptPlayActive': {},
     'ccapAppGblActRecordingActive': {},
     'ccapAppGblActTTSActive': {},
     'ccapAppGblEventLogging': {},
     'ccapAppGblEvtLogflush': {},
     'ccapAppGblHisAAAAuthenticateFailure': {},
     'ccapAppGblHisAAAAuthenticateSuccess': {},
     'ccapAppGblHisAAAAuthorizeFailure': {},
     'ccapAppGblHisAAAAuthorizeSuccess': {},
     'ccapAppGblHisASNLNotifReceived': {},
     'ccapAppGblHisASNLSubscriptionsFailed': {},
     'ccapAppGblHisASNLSubscriptionsSent': {},
     'ccapAppGblHisASNLSubscriptionsSuccess': {},
     'ccapAppGblHisASRAborted': {},
     'ccapAppGblHisASRAttempts': {},
     'ccapAppGblHisASRMatch': {},
     'ccapAppGblHisASRNoInput': {},
     'ccapAppGblHisASRNoMatch': {},
     'ccapAppGblHisDTMFAborted': {},
     'ccapAppGblHisDTMFAttempts': {},
     'ccapAppGblHisDTMFLongPound': {},
     'ccapAppGblHisDTMFMatch': {},
     'ccapAppGblHisDTMFNoInput': {},
     'ccapAppGblHisDTMFNoMatch': {},
     'ccapAppGblHisDocumentParseErrors': {},
     'ccapAppGblHisDocumentReadAttempts': {},
     'ccapAppGblHisDocumentReadFailures': {},
     'ccapAppGblHisDocumentReadSuccess': {},
     'ccapAppGblHisDocumentWriteAttempts': {},
     'ccapAppGblHisDocumentWriteFailures': {},
     'ccapAppGblHisDocumentWriteSuccess': {},
     'ccapAppGblHisIPInCallDiscNormal': {},
     'ccapAppGblHisIPInCallDiscSysErr': {},
     'ccapAppGblHisIPInCallDiscUsrErr': {},
     'ccapAppGblHisIPInCallHandOutRet': {},
     'ccapAppGblHisIPInCallHandedOut': {},
     'ccapAppGblHisIPInCallInHandoff': {},
     'ccapAppGblHisIPInCallInHandoffRet': {},
     'ccapAppGblHisIPInCallSetupInd': {},
     'ccapAppGblHisIPInCallTotConn': {},
     'ccapAppGblHisIPOutCallDiscNormal': {},
     'ccapAppGblHisIPOutCallDiscSysErr': {},
     'ccapAppGblHisIPOutCallDiscUsrErr': {},
     'ccapAppGblHisIPOutCallHandOutRet': {},
     'ccapAppGblHisIPOutCallHandedOut': {},
     'ccapAppGblHisIPOutCallInHandoff': {},
     'ccapAppGblHisIPOutCallInHandoffRet': {},
     'ccapAppGblHisIPOutCallSetupReq': {},
     'ccapAppGblHisIPOutCallTotConn': {},
     'ccapAppGblHisInHandoffCallback': {},
     'ccapAppGblHisInHandoffCallbackRet': {},
     'ccapAppGblHisInHandoffNoCallback': {},
     'ccapAppGblHisLastReset': {},
     'ccapAppGblHisOutHandoffCallback': {},
     'ccapAppGblHisOutHandoffCallbackRet': {},
     'ccapAppGblHisOutHandoffNoCallback': {},
     'ccapAppGblHisOutHandofffailures': {},
     'ccapAppGblHisPSTNInCallDiscNormal': {},
     'ccapAppGblHisPSTNInCallDiscSysErr': {},
     'ccapAppGblHisPSTNInCallDiscUsrErr': {},
     'ccapAppGblHisPSTNInCallHandOutRet': {},
     'ccapAppGblHisPSTNInCallHandedOut': {},
     'ccapAppGblHisPSTNInCallInHandoff': {},
     'ccapAppGblHisPSTNInCallInHandoffRet': {},
     'ccapAppGblHisPSTNInCallSetupInd': {},
     'ccapAppGblHisPSTNInCallTotConn': {},
     'ccapAppGblHisPSTNOutCallDiscNormal': {},
     'ccapAppGblHisPSTNOutCallDiscSysErr': {},
     'ccapAppGblHisPSTNOutCallDiscUsrErr': {},
     'ccapAppGblHisPSTNOutCallHandOutRet': {},
     'ccapAppGblHisPSTNOutCallHandedOut': {},
     'ccapAppGblHisPSTNOutCallInHandoff': {},
     'ccapAppGblHisPSTNOutCallInHandoffRet': {},
     'ccapAppGblHisPSTNOutCallSetupReq': {},
     'ccapAppGblHisPSTNOutCallTotConn': {},
     'ccapAppGblHisPlaceCallAttempts': {},
     'ccapAppGblHisPlaceCallFailure': {},
     'ccapAppGblHisPlaceCallSuccess': {},
     'ccapAppGblHisPromptPlayAttempts': {},
     'ccapAppGblHisPromptPlayDuration': {},
     'ccapAppGblHisPromptPlayFailed': {},
     'ccapAppGblHisPromptPlaySuccess': {},
     'ccapAppGblHisRecordingAttempts': {},
     'ccapAppGblHisRecordingDuration': {},
     'ccapAppGblHisRecordingFailed': {},
     'ccapAppGblHisRecordingSuccess': {},
     'ccapAppGblHisTTSAttempts': {},
     'ccapAppGblHisTTSFailed': {},
     'ccapAppGblHisTTSSuccess': {},
     'ccapAppGblHisTotalInstances': {},
     'ccapAppGblLastResetTime': {},
     'ccapAppGblStatsClear': {},
     'ccapAppGblStatsLogging': {},
     'ccapAppHandoffInProgress': {},
     'ccapAppIPInCallNowConn': {},
     'ccapAppIPOutCallNowConn': {},
     'ccapAppInstHisAAAAuthenticateFailure': {},
     'ccapAppInstHisAAAAuthenticateSuccess': {},
     'ccapAppInstHisAAAAuthorizeFailure': {},
     'ccapAppInstHisAAAAuthorizeSuccess': {},
     'ccapAppInstHisASNLNotifReceived': {},
     'ccapAppInstHisASNLSubscriptionsFailed': {},
     'ccapAppInstHisASNLSubscriptionsSent': {},
     'ccapAppInstHisASNLSubscriptionsSuccess': {},
     'ccapAppInstHisASRAborted': {},
     'ccapAppInstHisASRAttempts': {},
     'ccapAppInstHisASRMatch': {},
     'ccapAppInstHisASRNoInput': {},
     'ccapAppInstHisASRNoMatch': {},
     'ccapAppInstHisAppName': {},
     'ccapAppInstHisDTMFAborted': {},
     'ccapAppInstHisDTMFAttempts': {},
     'ccapAppInstHisDTMFLongPound': {},
     'ccapAppInstHisDTMFMatch': {},
     'ccapAppInstHisDTMFNoInput': {},
     'ccapAppInstHisDTMFNoMatch': {},
     'ccapAppInstHisDocumentParseErrors': {},
     'ccapAppInstHisDocumentReadAttempts': {},
     'ccapAppInstHisDocumentReadFailures': {},
     'ccapAppInstHisDocumentReadSuccess': {},
     'ccapAppInstHisDocumentWriteAttempts': {},
     'ccapAppInstHisDocumentWriteFailures': {},
     'ccapAppInstHisDocumentWriteSuccess': {},
     'ccapAppInstHisIPInCallDiscNormal': {},
     'ccapAppInstHisIPInCallDiscSysErr': {},
     'ccapAppInstHisIPInCallDiscUsrErr': {},
     'ccapAppInstHisIPInCallHandOutRet': {},
     'ccapAppInstHisIPInCallHandedOut': {},
     'ccapAppInstHisIPInCallInHandoff': {},
     'ccapAppInstHisIPInCallInHandoffRet': {},
     'ccapAppInstHisIPInCallSetupInd': {},
     'ccapAppInstHisIPInCallTotConn': {},
     'ccapAppInstHisIPOutCallDiscNormal': {},
     'ccapAppInstHisIPOutCallDiscSysErr': {},
     'ccapAppInstHisIPOutCallDiscUsrErr': {},
     'ccapAppInstHisIPOutCallHandOutRet': {},
     'ccapAppInstHisIPOutCallHandedOut': {},
     'ccapAppInstHisIPOutCallInHandoff': {},
     'ccapAppInstHisIPOutCallInHandoffRet': {},
     'ccapAppInstHisIPOutCallSetupReq': {},
     'ccapAppInstHisIPOutCallTotConn': {},
     'ccapAppInstHisInHandoffCallback': {},
     'ccapAppInstHisInHandoffCallbackRet': {},
     'ccapAppInstHisInHandoffNoCallback': {},
     'ccapAppInstHisOutHandoffCallback': {},
     'ccapAppInstHisOutHandoffCallbackRet': {},
     'ccapAppInstHisOutHandoffNoCallback': {},
     'ccapAppInstHisOutHandofffailures': {},
     'ccapAppInstHisPSTNInCallDiscNormal': {},
     'ccapAppInstHisPSTNInCallDiscSysErr': {},
     'ccapAppInstHisPSTNInCallDiscUsrErr': {},
     'ccapAppInstHisPSTNInCallHandOutRet': {},
     'ccapAppInstHisPSTNInCallHandedOut': {},
     'ccapAppInstHisPSTNInCallInHandoff': {},
     'ccapAppInstHisPSTNInCallInHandoffRet': {},
     'ccapAppInstHisPSTNInCallSetupInd': {},
     'ccapAppInstHisPSTNInCallTotConn': {},
     'ccapAppInstHisPSTNOutCallDiscNormal': {},
     'ccapAppInstHisPSTNOutCallDiscSysErr': {},
     'ccapAppInstHisPSTNOutCallDiscUsrErr': {},
     'ccapAppInstHisPSTNOutCallHandOutRet': {},
     'ccapAppInstHisPSTNOutCallHandedOut': {},
     'ccapAppInstHisPSTNOutCallInHandoff': {},
     'ccapAppInstHisPSTNOutCallInHandoffRet': {},
     'ccapAppInstHisPSTNOutCallSetupReq': {},
     'ccapAppInstHisPSTNOutCallTotConn': {},
     'ccapAppInstHisPlaceCallAttempts': {},
     'ccapAppInstHisPlaceCallFailure': {},
     'ccapAppInstHisPlaceCallSuccess': {},
     'ccapAppInstHisPromptPlayAttempts': {},
     'ccapAppInstHisPromptPlayDuration': {},
     'ccapAppInstHisPromptPlayFailed': {},
     'ccapAppInstHisPromptPlaySuccess': {},
     'ccapAppInstHisRecordingAttempts': {},
     'ccapAppInstHisRecordingDuration': {},
     'ccapAppInstHisRecordingFailed': {},
     'ccapAppInstHisRecordingSuccess': {},
     'ccapAppInstHisSessionID': {},
     'ccapAppInstHisTTSAttempts': {},
     'ccapAppInstHisTTSFailed': {},
     'ccapAppInstHisTTSSuccess': {},
     'ccapAppInstHistEvtLogging': {},
     'ccapAppIntfAAAMethodListEvtLog': {},
     'ccapAppIntfAAAMethodListLastResetTime': {},
     'ccapAppIntfAAAMethodListReadFailure': {},
     'ccapAppIntfAAAMethodListReadRequest': {},
     'ccapAppIntfAAAMethodListReadSuccess': {},
     'ccapAppIntfAAAMethodListStats': {},
     'ccapAppIntfASREvtLog': {},
     'ccapAppIntfASRLastResetTime': {},
     'ccapAppIntfASRReadFailure': {},
     'ccapAppIntfASRReadRequest': {},
     'ccapAppIntfASRReadSuccess': {},
     'ccapAppIntfASRStats': {},
     'ccapAppIntfFlashReadFailure': {},
     'ccapAppIntfFlashReadRequest': {},
     'ccapAppIntfFlashReadSuccess': {},
     'ccapAppIntfGblEventLogging': {},
     'ccapAppIntfGblEvtLogFlush': {},
     'ccapAppIntfGblLastResetTime': {},
     'ccapAppIntfGblStatsClear': {},
     'ccapAppIntfGblStatsLogging': {},
     'ccapAppIntfHTTPAvgXferRate': {},
     'ccapAppIntfHTTPEvtLog': {},
     'ccapAppIntfHTTPGetFailure': {},
     'ccapAppIntfHTTPGetRequest': {},
     'ccapAppIntfHTTPGetSuccess': {},
     'ccapAppIntfHTTPLastResetTime': {},
     'ccapAppIntfHTTPMaxXferRate': {},
     'ccapAppIntfHTTPMinXferRate': {},
     'ccapAppIntfHTTPPostFailure': {},
     'ccapAppIntfHTTPPostRequest': {},
     'ccapAppIntfHTTPPostSuccess': {},
     'ccapAppIntfHTTPRxBytes': {},
     'ccapAppIntfHTTPStats': {},
     'ccapAppIntfHTTPTxBytes': {},
     'ccapAppIntfRAMRecordReadRequest': {},
     'ccapAppIntfRAMRecordReadSuccess': {},
     'ccapAppIntfRAMRecordRequest': {},
     'ccapAppIntfRAMRecordSuccess': {},
     'ccapAppIntfRAMRecordiongFailure': {},
     'ccapAppIntfRAMRecordiongReadFailure': {},
     'ccapAppIntfRTSPAvgXferRate': {},
     'ccapAppIntfRTSPEvtLog': {},
     'ccapAppIntfRTSPLastResetTime': {},
     'ccapAppIntfRTSPMaxXferRate': {},
     'ccapAppIntfRTSPMinXferRate': {},
     'ccapAppIntfRTSPReadFailure': {},
     'ccapAppIntfRTSPReadRequest': {},
     'ccapAppIntfRTSPReadSuccess': {},
     'ccapAppIntfRTSPRxBytes': {},
     'ccapAppIntfRTSPStats': {},
     'ccapAppIntfRTSPTxBytes': {},
     'ccapAppIntfRTSPWriteFailure': {},
     'ccapAppIntfRTSPWriteRequest': {},
     'ccapAppIntfRTSPWriteSuccess': {},
     'ccapAppIntfSMTPAvgXferRate': {},
     'ccapAppIntfSMTPEvtLog': {},
     'ccapAppIntfSMTPLastResetTime': {},
     'ccapAppIntfSMTPMaxXferRate': {},
     'ccapAppIntfSMTPMinXferRate': {},
     'ccapAppIntfSMTPReadFailure': {},
     'ccapAppIntfSMTPReadRequest': {},
     'ccapAppIntfSMTPReadSuccess': {},
     'ccapAppIntfSMTPRxBytes': {},
     'ccapAppIntfSMTPStats': {},
     'ccapAppIntfSMTPTxBytes': {},
     'ccapAppIntfSMTPWriteFailure': {},
     'ccapAppIntfSMTPWriteRequest': {},
     'ccapAppIntfSMTPWriteSuccess': {},
     'ccapAppIntfTFTPAvgXferRate': {},
     'ccapAppIntfTFTPEvtLog': {},
     'ccapAppIntfTFTPLastResetTime': {},
     'ccapAppIntfTFTPMaxXferRate': {},
     'ccapAppIntfTFTPMinXferRate': {},
     'ccapAppIntfTFTPReadFailure': {},
     'ccapAppIntfTFTPReadRequest': {},
     'ccapAppIntfTFTPReadSuccess': {},
     'ccapAppIntfTFTPRxBytes': {},
     'ccapAppIntfTFTPStats': {},
     'ccapAppIntfTFTPTxBytes': {},
     'ccapAppIntfTFTPWriteFailure': {},
     'ccapAppIntfTFTPWriteRequest': {},
     'ccapAppIntfTFTPWriteSuccess': {},
     'ccapAppIntfTTSEvtLog': {},
     'ccapAppIntfTTSLastResetTime': {},
     'ccapAppIntfTTSReadFailure': {},
     'ccapAppIntfTTSReadRequest': {},
     'ccapAppIntfTTSReadSuccess': {},
     'ccapAppIntfTTSStats': {},
     'ccapAppLoadFailReason': {},
     'ccapAppLoadState': {},
     'ccapAppLocation': {},
     'ccapAppPSTNInCallNowConn': {},
     'ccapAppPSTNOutCallNowConn': {},
     'ccapAppPlaceCallInProgress': {},
     'ccapAppPromptPlayActive': {},
     'ccapAppRecordingActive': {},
     'ccapAppRowStatus': {},
     'ccapAppTTSActive': {},
     'ccapAppTypeHisAAAAuthenticateFailure': {},
     'ccapAppTypeHisAAAAuthenticateSuccess': {},
     'ccapAppTypeHisAAAAuthorizeFailure': {},
     'ccapAppTypeHisAAAAuthorizeSuccess': {},
     'ccapAppTypeHisASNLNotifReceived': {},
     'ccapAppTypeHisASNLSubscriptionsFailed': {},
     'ccapAppTypeHisASNLSubscriptionsSent': {},
     'ccapAppTypeHisASNLSubscriptionsSuccess': {},
     'ccapAppTypeHisASRAborted': {},
     'ccapAppTypeHisASRAttempts': {},
     'ccapAppTypeHisASRMatch': {},
     'ccapAppTypeHisASRNoInput': {},
     'ccapAppTypeHisASRNoMatch': {},
     'ccapAppTypeHisDTMFAborted': {},
     'ccapAppTypeHisDTMFAttempts': {},
     'ccapAppTypeHisDTMFLongPound': {},
     'ccapAppTypeHisDTMFMatch': {},
     'ccapAppTypeHisDTMFNoInput': {},
     'ccapAppTypeHisDTMFNoMatch': {},
     'ccapAppTypeHisDocumentParseErrors': {},
     'ccapAppTypeHisDocumentReadAttempts': {},
     'ccapAppTypeHisDocumentReadFailures': {},
     'ccapAppTypeHisDocumentReadSuccess': {},
     'ccapAppTypeHisDocumentWriteAttempts': {},
     'ccapAppTypeHisDocumentWriteFailures': {},
     'ccapAppTypeHisDocumentWriteSuccess': {},
     'ccapAppTypeHisEvtLogging': {},
     'ccapAppTypeHisIPInCallDiscNormal': {},
     'ccapAppTypeHisIPInCallDiscSysErr': {},
     'ccapAppTypeHisIPInCallDiscUsrErr': {},
     'ccapAppTypeHisIPInCallHandOutRet': {},
     'ccapAppTypeHisIPInCallHandedOut': {},
     'ccapAppTypeHisIPInCallInHandoff': {},
     'ccapAppTypeHisIPInCallInHandoffRet': {},
     'ccapAppTypeHisIPInCallSetupInd': {},
     'ccapAppTypeHisIPInCallTotConn': {},
     'ccapAppTypeHisIPOutCallDiscNormal': {},
     'ccapAppTypeHisIPOutCallDiscSysErr': {},
     'ccapAppTypeHisIPOutCallDiscUsrErr': {},
     'ccapAppTypeHisIPOutCallHandOutRet': {},
     'ccapAppTypeHisIPOutCallHandedOut': {},
     'ccapAppTypeHisIPOutCallInHandoff': {},
     'ccapAppTypeHisIPOutCallInHandoffRet': {},
     'ccapAppTypeHisIPOutCallSetupReq': {},
     'ccapAppTypeHisIPOutCallTotConn': {},
     'ccapAppTypeHisInHandoffCallback': {},
     'ccapAppTypeHisInHandoffCallbackRet': {},
     'ccapAppTypeHisInHandoffNoCallback': {},
     'ccapAppTypeHisLastResetTime': {},
     'ccapAppTypeHisOutHandoffCallback': {},
     'ccapAppTypeHisOutHandoffCallbackRet': {},
     'ccapAppTypeHisOutHandoffNoCallback': {},
     'ccapAppTypeHisOutHandofffailures': {},
     'ccapAppTypeHisPSTNInCallDiscNormal': {},
     'ccapAppTypeHisPSTNInCallDiscSysErr': {},
     'ccapAppTypeHisPSTNInCallDiscUsrErr': {},
     'ccapAppTypeHisPSTNInCallHandOutRet': {},
     'ccapAppTypeHisPSTNInCallHandedOut': {},
     'ccapAppTypeHisPSTNInCallInHandoff': {},
     'ccapAppTypeHisPSTNInCallInHandoffRet': {},
     'ccapAppTypeHisPSTNInCallSetupInd': {},
     'ccapAppTypeHisPSTNInCallTotConn': {},
     'ccapAppTypeHisPSTNOutCallDiscNormal': {},
     'ccapAppTypeHisPSTNOutCallDiscSysErr': {},
     'ccapAppTypeHisPSTNOutCallDiscUsrErr': {},
     'ccapAppTypeHisPSTNOutCallHandOutRet': {},
     'ccapAppTypeHisPSTNOutCallHandedOut': {},
     'ccapAppTypeHisPSTNOutCallInHandoff': {},
     'ccapAppTypeHisPSTNOutCallInHandoffRet': {},
     'ccapAppTypeHisPSTNOutCallSetupReq': {},
     'ccapAppTypeHisPSTNOutCallTotConn': {},
     'ccapAppTypeHisPlaceCallAttempts': {},
     'ccapAppTypeHisPlaceCallFailure': {},
     'ccapAppTypeHisPlaceCallSuccess': {},
     'ccapAppTypeHisPromptPlayAttempts': {},
     'ccapAppTypeHisPromptPlayDuration': {},
     'ccapAppTypeHisPromptPlayFailed': {},
     'ccapAppTypeHisPromptPlaySuccess': {},
     'ccapAppTypeHisRecordingAttempts': {},
     'ccapAppTypeHisRecordingDuration': {},
     'ccapAppTypeHisRecordingFailed': {},
     'ccapAppTypeHisRecordingSuccess': {},
     'ccapAppTypeHisTTSAttempts': {},
     'ccapAppTypeHisTTSFailed': {},
     'ccapAppTypeHisTTSSuccess': {},
     'ccarConfigAccIdx': {},
     'ccarConfigConformAction': {},
     'ccarConfigExceedAction': {},
     'ccarConfigExtLimit': {},
     'ccarConfigLimit': {},
     'ccarConfigRate': {},
     'ccarConfigType': {},
     'ccarStatCurBurst': {},
     'ccarStatFilteredBytes': {},
     'ccarStatFilteredBytesOverflow': {},
     'ccarStatFilteredPkts': {},
     'ccarStatFilteredPktsOverflow': {},
     'ccarStatHCFilteredBytes': {},
     'ccarStatHCFilteredPkts': {},
     'ccarStatHCSwitchedBytes': {},
     'ccarStatHCSwitchedPkts': {},
     'ccarStatSwitchedBytes': {},
     'ccarStatSwitchedBytesOverflow': {},
     'ccarStatSwitchedPkts': {},
     'ccarStatSwitchedPktsOverflow': {},
     'ccbptPolicyIdNext': {},
     'ccbptTargetTable.1.10': {},
     'ccbptTargetTable.1.6': {},
     'ccbptTargetTable.1.7': {},
     'ccbptTargetTable.1.8': {},
     'ccbptTargetTable.1.9': {},
     'ccbptTargetTableLastChange': {},
     'cciDescriptionEntry': {'1': {}, '2': {}},
     'ccmCLICfgRunConfNotifEnable': {},
     'ccmCLIHistoryCmdEntries': {},
     'ccmCLIHistoryCmdEntriesAllowed': {},
     'ccmCLIHistoryCommand': {},
     'ccmCLIHistoryMaxCmdEntries': {},
     'ccmCTID': {},
     'ccmCTIDLastChangeTime': {},
     'ccmCTIDRolledOverNotifEnable': {},
     'ccmCTIDWhoChanged': {},
     'ccmCallHomeAlertGroupCfg': {'3': {}, '5': {}},
     'ccmCallHomeConfiguration': {'1': {},
                                  '10': {},
                                  '11': {},
                                  '13': {},
                                  '15': {},
                                  '16': {},
                                  '17': {},
                                  '18': {},
                                  '19': {},
                                  '2': {},
                                  '20': {},
                                  '21': {},
                                  '23': {},
                                  '24': {},
                                  '27': {},
                                  '28': {},
                                  '29': {},
                                  '3': {},
                                  '34': {},
                                  '35': {},
                                  '36': {},
                                  '37': {},
                                  '38': {},
                                  '39': {},
                                  '4': {},
                                  '40': {},
                                  '5': {},
                                  '6': {},
                                  '7': {},
                                  '8': {},
                                  '9': {}},
     'ccmCallHomeDiagSignature': {'2': {}, '3': {}},
     'ccmCallHomeDiagSignatureInfoEntry': {'2': {},
                                           '3': {},
                                           '4': {},
                                           '5': {},
                                           '6': {},
                                           '7': {},
                                           '8': {}},
     'ccmCallHomeMessageSource': {'1': {}, '2': {}, '3': {}},
     'ccmCallHomeNotifConfig': {'1': {}},
     'ccmCallHomeReporting': {'1': {}},
     'ccmCallHomeSecurity': {'1': {}},
     'ccmCallHomeStats': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ccmCallHomeStatus': {'1': {}, '2': {}, '3': {}, '5': {}},
     'ccmCallHomeVrf': {'1': {}},
     'ccmDestProfileTestEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ccmEventAlertGroupEntry': {'1': {}, '2': {}},
     'ccmEventStatsEntry': {'10': {},
                            '11': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'ccmHistoryCLICmdEntriesBumped': {},
     'ccmHistoryEventCommandSource': {},
     'ccmHistoryEventCommandSourceAddrRev1': {},
     'ccmHistoryEventCommandSourceAddrType': {},
     'ccmHistoryEventCommandSourceAddress': {},
     'ccmHistoryEventConfigDestination': {},
     'ccmHistoryEventConfigSource': {},
     'ccmHistoryEventEntriesBumped': {},
     'ccmHistoryEventFile': {},
     'ccmHistoryEventRcpUser': {},
     'ccmHistoryEventServerAddrRev1': {},
     'ccmHistoryEventServerAddrType': {},
     'ccmHistoryEventServerAddress': {},
     'ccmHistoryEventTerminalLocation': {},
     'ccmHistoryEventTerminalNumber': {},
     'ccmHistoryEventTerminalType': {},
     'ccmHistoryEventTerminalUser': {},
     'ccmHistoryEventTime': {},
     'ccmHistoryEventVirtualHostName': {},
     'ccmHistoryMaxEventEntries': {},
     'ccmHistoryRunningLastChanged': {},
     'ccmHistoryRunningLastSaved': {},
     'ccmHistoryStartupLastChanged': {},
     'ccmOnDemandCliMsgControl': {'1': {},
                                  '2': {},
                                  '3': {},
                                  '4': {},
                                  '5': {},
                                  '6': {}},
     'ccmOnDemandMsgSendControl': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ccmPatternAlertGroupEntry': {'2': {}, '3': {}, '4': {}},
     'ccmPeriodicAlertGroupEntry': {'1': {},
                                    '2': {},
                                    '3': {},
                                    '4': {},
                                    '5': {},
                                    '6': {},
                                    '7': {}},
     'ccmPeriodicSwInventoryCfg': {'1': {}},
     'ccmSeverityAlertGroupEntry': {'1': {}},
     'ccmSmartCallHomeActions': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ccmSmtpServerStatusEntry': {'1': {}},
     'ccmSmtpServersEntry': {'3': {}, '4': {}, '5': {}, '6': {}},
     'cdeCircuitEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cdeFastEntry': {'10': {},
                      '11': {},
                      '12': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'cdeIfEntry': {'1': {}},
     'cdeNode': {'1': {},
                 '10': {},
                 '11': {},
                 '12': {},
                 '13': {},
                 '14': {},
                 '15': {},
                 '16': {},
                 '17': {},
                 '18': {},
                 '19': {},
                 '2': {},
                 '20': {},
                 '21': {},
                 '22': {},
                 '3': {},
                 '4': {},
                 '5': {},
                 '6': {},
                 '7': {},
                 '8': {},
                 '9': {}},
     'cdeTConnConfigEntry': {'1': {},
                             '10': {},
                             '11': {},
                             '12': {},
                             '13': {},
                             '14': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'cdeTConnDirectConfigEntry': {'1': {}, '2': {}, '3': {}},
     'cdeTConnOperEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'cdeTConnTcpConfigEntry': {'1': {}},
     'cdeTrapControl': {'1': {}, '2': {}},
     'cdlCivicAddrLocationStatus': {},
     'cdlCivicAddrLocationStorageType': {},
     'cdlCivicAddrLocationValue': {},
     'cdlCustomLocationStatus': {},
     'cdlCustomLocationStorageType': {},
     'cdlCustomLocationValue': {},
     'cdlGeoAltitude': {},
     'cdlGeoAltitudeResolution': {},
     'cdlGeoAltitudeType': {},
     'cdlGeoLatitude': {},
     'cdlGeoLatitudeResolution': {},
     'cdlGeoLongitude': {},
     'cdlGeoLongitudeResolution': {},
     'cdlGeoResolution': {},
     'cdlGeoStatus': {},
     'cdlGeoStorageType': {},
     'cdlKey': {},
     'cdlLocationCountryCode': {},
     'cdlLocationPreferWeightValue': {},
     'cdlLocationSubTypeCapability': {},
     'cdlLocationTargetIdentifier': {},
     'cdlLocationTargetType': {},
     'cdot3OamAdminState': {},
     'cdot3OamConfigRevision': {},
     'cdot3OamCriticalEventEnable': {},
     'cdot3OamDuplicateEventNotificationRx': {},
     'cdot3OamDuplicateEventNotificationTx': {},
     'cdot3OamDyingGaspEnable': {},
     'cdot3OamErrFrameEvNotifEnable': {},
     'cdot3OamErrFramePeriodEvNotifEnable': {},
     'cdot3OamErrFramePeriodThreshold': {},
     'cdot3OamErrFramePeriodWindow': {},
     'cdot3OamErrFrameSecsEvNotifEnable': {},
     'cdot3OamErrFrameSecsSummaryThreshold': {},
     'cdot3OamErrFrameSecsSummaryWindow': {},
     'cdot3OamErrFrameThreshold': {},
     'cdot3OamErrFrameWindow': {},
     'cdot3OamErrSymPeriodEvNotifEnable': {},
     'cdot3OamErrSymPeriodThresholdHi': {},
     'cdot3OamErrSymPeriodThresholdLo': {},
     'cdot3OamErrSymPeriodWindowHi': {},
     'cdot3OamErrSymPeriodWindowLo': {},
     'cdot3OamEventLogEventTotal': {},
     'cdot3OamEventLogLocation': {},
     'cdot3OamEventLogOui': {},
     'cdot3OamEventLogRunningTotal': {},
     'cdot3OamEventLogThresholdHi': {},
     'cdot3OamEventLogThresholdLo': {},
     'cdot3OamEventLogTimestamp': {},
     'cdot3OamEventLogType': {},
     'cdot3OamEventLogValue': {},
     'cdot3OamEventLogWindowHi': {},
     'cdot3OamEventLogWindowLo': {},
     'cdot3OamFramesLostDueToOam': {},
     'cdot3OamFunctionsSupported': {},
     'cdot3OamInformationRx': {},
     'cdot3OamInformationTx': {},
     'cdot3OamLoopbackControlRx': {},
     'cdot3OamLoopbackControlTx': {},
     'cdot3OamLoopbackIgnoreRx': {},
     'cdot3OamLoopbackStatus': {},
     'cdot3OamMaxOamPduSize': {},
     'cdot3OamMode': {},
     'cdot3OamOperStatus': {},
     'cdot3OamOrgSpecificRx': {},
     'cdot3OamOrgSpecificTx': {},
     'cdot3OamPeerConfigRevision': {},
     'cdot3OamPeerFunctionsSupported': {},
     'cdot3OamPeerMacAddress': {},
     'cdot3OamPeerMaxOamPduSize': {},
     'cdot3OamPeerMode': {},
     'cdot3OamPeerVendorInfo': {},
     'cdot3OamPeerVendorOui': {},
     'cdot3OamUniqueEventNotificationRx': {},
     'cdot3OamUniqueEventNotificationTx': {},
     'cdot3OamUnsupportedCodesRx': {},
     'cdot3OamUnsupportedCodesTx': {},
     'cdot3OamVariableRequestRx': {},
     'cdot3OamVariableRequestTx': {},
     'cdot3OamVariableResponseRx': {},
     'cdot3OamVariableResponseTx': {},
     'cdpCache.2.1.4': {},
     'cdpCache.2.1.5': {},
     'cdpCacheEntry': {'10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '15': {},
                       '16': {},
                       '17': {},
                       '18': {},
                       '19': {},
                       '20': {},
                       '21': {},
                       '22': {},
                       '23': {},
                       '24': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'cdpGlobal': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'cdpInterface.2.1.1': {},
     'cdpInterface.2.1.2': {},
     'cdpInterfaceEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'cdspActiveChannels': {},
     'cdspAlarms': {},
     'cdspCardIndex': {},
     'cdspCardLastHiWaterUtilization': {},
     'cdspCardLastResetTime': {},
     'cdspCardMaxChanPerDSP': {},
     'cdspCardResourceUtilization': {},
     'cdspCardState': {},
     'cdspCardVideoPoolUtilization': {},
     'cdspCardVideoPoolUtilizationThreshold': {},
     'cdspCodecTemplateSupported': {},
     'cdspCongestedDsp': {},
     'cdspCurrentAvlbCap': {},
     'cdspCurrentUtilCap': {},
     'cdspDspNum': {},
     'cdspDspSwitchOverThreshold': {},
     'cdspDspfarmObjects.5.1.10': {},
     'cdspDspfarmObjects.5.1.11': {},
     'cdspDspfarmObjects.5.1.2': {},
     'cdspDspfarmObjects.5.1.3': {},
     'cdspDspfarmObjects.5.1.4': {},
     'cdspDspfarmObjects.5.1.5': {},
     'cdspDspfarmObjects.5.1.6': {},
     'cdspDspfarmObjects.5.1.7': {},
     'cdspDspfarmObjects.5.1.8': {},
     'cdspDspfarmObjects.5.1.9': {},
     'cdspDtmfPowerLevel': {},
     'cdspDtmfPowerTwist': {},
     'cdspEnableOperStateNotification': {},
     'cdspFailedDsp': {},
     'cdspGlobMaxAvailTranscodeSess': {},
     'cdspGlobMaxConfTranscodeSess': {},
     'cdspInUseChannels': {},
     'cdspLastAlarmCause': {},
     'cdspLastAlarmCauseText': {},
     'cdspLastAlarmTime': {},
     'cdspMIBEnableCardStatusNotification': {},
     'cdspMtpProfileEntry': {'10': {},
                             '11': {},
                             '12': {},
                             '13': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'cdspMtpProfileMaxAvailHardSess': {},
     'cdspMtpProfileMaxConfHardSess': {},
     'cdspMtpProfileMaxConfSoftSess': {},
     'cdspMtpProfileRowStatus': {},
     'cdspNormalDsp': {},
     'cdspNumCongestionOccurrence': {},
     'cdspNx64Dsp': {},
     'cdspOperState': {},
     'cdspPktLossConcealment': {},
     'cdspRtcpControl': {},
     'cdspRtcpRecvMultiplier': {},
     'cdspRtcpTimerControl': {},
     'cdspRtcpTransInterval': {},
     'cdspRtcpXrControl': {},
     'cdspRtcpXrExtRfactor': {},
     'cdspRtcpXrGminDefault': {},
     'cdspRtcpXrTransMultiplier': {},
     'cdspRtpSidPayloadType': {},
     'cdspSigBearerChannelSplit': {},
     'cdspTotAvailMtpSess': {},
     'cdspTotAvailTranscodeSess': {},
     'cdspTotUnusedMtpSess': {},
     'cdspTotUnusedTranscodeSess': {},
     'cdspTotalChannels': {},
     'cdspTotalDsp': {},
     'cdspTranscodeProfileEntry': {'10': {},
                                   '11': {},
                                   '5': {},
                                   '6': {},
                                   '7': {},
                                   '8': {},
                                   '9': {}},
     'cdspTranscodeProfileMaxAvailSess': {},
     'cdspTranscodeProfileMaxConfSess': {},
     'cdspTranscodeProfileRowStatus': {},
     'cdspTransparentIpIp': {},
     'cdspVadAdaptive': {},
     'cdspVideoOutOfResourceNotificationEnable': {},
     'cdspVideoUsageNotificationEnable': {},
     'cdspVoiceModeIpIp': {},
     'cdspVqmControl': {},
     'cdspVqmThreshSES': {},
     'cdspXAvailableBearerBandwidth': {},
     'cdspXAvailableSigBandwidth': {},
     'cdspXNumberOfBearerCalls': {},
     'cdspXNumberOfSigCalls': {},
     'cdtCommonAddrPool': {},
     'cdtCommonDescr': {},
     'cdtCommonIpv4AccessGroup': {},
     'cdtCommonIpv4Unreachables': {},
     'cdtCommonIpv6AccessGroup': {},
     'cdtCommonIpv6Unreachables': {},
     'cdtCommonKeepaliveInt': {},
     'cdtCommonKeepaliveRetries': {},
     'cdtCommonSrvAcct': {},
     'cdtCommonSrvNetflow': {},
     'cdtCommonSrvQos': {},
     'cdtCommonSrvRedirect': {},
     'cdtCommonSrvSubControl': {},
     'cdtCommonValid': {},
     'cdtCommonVrf': {},
     'cdtEthernetBridgeDomain': {},
     'cdtEthernetIpv4PointToPoint': {},
     'cdtEthernetMacAddr': {},
     'cdtEthernetPppoeEnable': {},
     'cdtEthernetValid': {},
     'cdtIfCdpEnable': {},
     'cdtIfFlowMonitor': {},
     'cdtIfIpv4Mtu': {},
     'cdtIfIpv4SubEnable': {},
     'cdtIfIpv4TcpMssAdjust': {},
     'cdtIfIpv4Unnumbered': {},
     'cdtIfIpv4VerifyUniRpf': {},
     'cdtIfIpv4VerifyUniRpfAcl': {},
     'cdtIfIpv4VerifyUniRpfOpts': {},
     'cdtIfIpv6Enable': {},
     'cdtIfIpv6NdDadAttempts': {},
     'cdtIfIpv6NdNsInterval': {},
     'cdtIfIpv6NdOpts': {},
     'cdtIfIpv6NdPreferredLife': {},
     'cdtIfIpv6NdPrefix': {},
     'cdtIfIpv6NdPrefixLength': {},
     'cdtIfIpv6NdRaIntervalMax': {},
     'cdtIfIpv6NdRaIntervalMin': {},
     'cdtIfIpv6NdRaIntervalUnits': {},
     'cdtIfIpv6NdRaLife': {},
     'cdtIfIpv6NdReachableTime': {},
     'cdtIfIpv6NdRouterPreference': {},
     'cdtIfIpv6NdValidLife': {},
     'cdtIfIpv6SubEnable': {},
     'cdtIfIpv6TcpMssAdjust': {},
     'cdtIfIpv6VerifyUniRpf': {},
     'cdtIfIpv6VerifyUniRpfAcl': {},
     'cdtIfIpv6VerifyUniRpfOpts': {},
     'cdtIfMtu': {},
     'cdtIfValid': {},
     'cdtPppAccounting': {},
     'cdtPppAuthentication': {},
     'cdtPppAuthenticationMethods': {},
     'cdtPppAuthorization': {},
     'cdtPppChapHostname': {},
     'cdtPppChapOpts': {},
     'cdtPppChapPassword': {},
     'cdtPppEapIdentity': {},
     'cdtPppEapOpts': {},
     'cdtPppEapPassword': {},
     'cdtPppIpcpAddrOption': {},
     'cdtPppIpcpDnsOption': {},
     'cdtPppIpcpDnsPrimary': {},
     'cdtPppIpcpDnsSecondary': {},
     'cdtPppIpcpMask': {},
     'cdtPppIpcpMaskOption': {},
     'cdtPppIpcpWinsOption': {},
     'cdtPppIpcpWinsPrimary': {},
     'cdtPppIpcpWinsSecondary': {},
     'cdtPppLoopbackIgnore': {},
     'cdtPppMaxBadAuth': {},
     'cdtPppMaxConfigure': {},
     'cdtPppMaxFailure': {},
     'cdtPppMaxTerminate': {},
     'cdtPppMsChapV1Hostname': {},
     'cdtPppMsChapV1Opts': {},
     'cdtPppMsChapV1Password': {},
     'cdtPppMsChapV2Hostname': {},
     'cdtPppMsChapV2Opts': {},
     'cdtPppMsChapV2Password': {},
     'cdtPppPapOpts': {},
     'cdtPppPapPassword': {},
     'cdtPppPapUsername': {},
     'cdtPppPeerDefIpAddr': {},
     'cdtPppPeerDefIpAddrOpts': {},
     'cdtPppPeerDefIpAddrSrc': {},
     'cdtPppPeerIpAddrPoolName': {},
     'cdtPppPeerIpAddrPoolStatus': {},
     'cdtPppPeerIpAddrPoolStorage': {},
     'cdtPppTimeoutAuthentication': {},
     'cdtPppTimeoutRetry': {},
     'cdtPppValid': {},
     'cdtSrvMulticast': {},
     'cdtSrvNetworkSrv': {},
     'cdtSrvSgSrvGroup': {},
     'cdtSrvSgSrvType': {},
     'cdtSrvValid': {},
     'cdtSrvVpdnGroup': {},
     'cdtTemplateAssociationName': {},
     'cdtTemplateAssociationPrecedence': {},
     'cdtTemplateName': {},
     'cdtTemplateSrc': {},
     'cdtTemplateStatus': {},
     'cdtTemplateStorage': {},
     'cdtTemplateTargetStatus': {},
     'cdtTemplateTargetStorage': {},
     'cdtTemplateType': {},
     'cdtTemplateUsageCount': {},
     'cdtTemplateUsageTargetId': {},
     'cdtTemplateUsageTargetType': {},
     'ceAlarmCriticalCount': {},
     'ceAlarmCutOff': {},
     'ceAlarmDescrSeverity': {},
     'ceAlarmDescrText': {},
     'ceAlarmDescrVendorType': {},
     'ceAlarmFilterAlarmsEnabled': {},
     'ceAlarmFilterAlias': {},
     'ceAlarmFilterNotifiesEnabled': {},
     'ceAlarmFilterProfile': {},
     'ceAlarmFilterProfileIndexNext': {},
     'ceAlarmFilterStatus': {},
     'ceAlarmFilterSyslogEnabled': {},
     'ceAlarmHistAlarmType': {},
     'ceAlarmHistEntPhysicalIndex': {},
     'ceAlarmHistLastIndex': {},
     'ceAlarmHistSeverity': {},
     'ceAlarmHistTableSize': {},
     'ceAlarmHistTimeStamp': {},
     'ceAlarmHistType': {},
     'ceAlarmList': {},
     'ceAlarmMajorCount': {},
     'ceAlarmMinorCount': {},
     'ceAlarmNotifiesEnable': {},
     'ceAlarmSeverity': {},
     'ceAlarmSyslogEnable': {},
     'ceAssetAlias': {},
     'ceAssetCLEI': {},
     'ceAssetFirmwareID': {},
     'ceAssetFirmwareRevision': {},
     'ceAssetHardwareRevision': {},
     'ceAssetIsFRU': {},
     'ceAssetMfgAssyNumber': {},
     'ceAssetMfgAssyRevision': {},
     'ceAssetOEMString': {},
     'ceAssetOrderablePartNumber': {},
     'ceAssetSerialNumber': {},
     'ceAssetSoftwareID': {},
     'ceAssetSoftwareRevision': {},
     'ceAssetTag': {},
     'ceDiagEntityCurrentTestEntry': {'1': {}},
     'ceDiagEntityEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ceDiagErrorInfoEntry': {'2': {}},
     'ceDiagEventQueryEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'ceDiagEventResultEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'ceDiagEvents': {'1': {}, '2': {}, '3': {}},
     'ceDiagHMTestEntry': {'1': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {}},
     'ceDiagHealthMonitor': {'1': {}},
     'ceDiagNotificationControl': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ceDiagOnDemand': {'1': {}, '2': {}, '3': {}},
     'ceDiagOnDemandJobEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ceDiagScheduledJobEntry': {'2': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {}},
     'ceDiagTestCustomAttributeEntry': {'2': {}},
     'ceDiagTestInfoEntry': {'2': {}, '3': {}},
     'ceDiagTestPerfEntry': {'1': {},
                             '10': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'ceExtConfigRegNext': {},
     'ceExtConfigRegister': {},
     'ceExtEntBreakOutPortNotifEnable': {},
     'ceExtEntDoorNotifEnable': {},
     'ceExtEntityLEDColor': {},
     'ceExtHCProcessorRam': {},
     'ceExtKickstartImageList': {},
     'ceExtNVRAMSize': {},
     'ceExtNVRAMUsed': {},
     'ceExtNotificationControlObjects': {'3': {}},
     'ceExtProcessorRam': {},
     'ceExtProcessorRamOverflow': {},
     'ceExtSysBootImageList': {},
     'ceExtUSBModemIMEI': {},
     'ceExtUSBModemIMSI': {},
     'ceExtUSBModemServiceProvider': {},
     'ceExtUSBModemSignalStrength': {},
     'ceImage.1.1.2': {},
     'ceImage.1.1.3': {},
     'ceImage.1.1.4': {},
     'ceImage.1.1.5': {},
     'ceImage.1.1.6': {},
     'ceImage.1.1.7': {},
     'ceImageInstallableTable.1.2': {},
     'ceImageInstallableTable.1.3': {},
     'ceImageInstallableTable.1.4': {},
     'ceImageInstallableTable.1.5': {},
     'ceImageInstallableTable.1.6': {},
     'ceImageInstallableTable.1.7': {},
     'ceImageInstallableTable.1.8': {},
     'ceImageInstallableTable.1.9': {},
     'ceImageLocationTable.1.2': {},
     'ceImageLocationTable.1.3': {},
     'ceImageTags.1.1.2': {},
     'ceImageTags.1.1.3': {},
     'ceImageTags.1.1.4': {},
     'ceeDot3PauseExtAdminMode': {},
     'ceeDot3PauseExtOperMode': {},
     'ceeSubInterfaceCount': {},
     'ceemEventMapEntry': {'2': {}, '3': {}},
     'ceemHistory': {'1': {}},
     'ceemHistoryEventEntry': {'10': {},
                               '11': {},
                               '12': {},
                               '13': {},
                               '14': {},
                               '15': {},
                               '16': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'ceemHistoryLastEventEntry': {},
     'ceemRegisteredPolicyEntry': {'10': {},
                                   '11': {},
                                   '12': {},
                                   '13': {},
                                   '14': {},
                                   '15': {},
                                   '16': {},
                                   '17': {},
                                   '2': {},
                                   '3': {},
                                   '4': {},
                                   '5': {},
                                   '6': {},
                                   '7': {},
                                   '8': {},
                                   '9': {}},
     'cefAdjBytes': {},
     'cefAdjEncap': {},
     'cefAdjFixup': {},
     'cefAdjForwardingInfo': {},
     'cefAdjHCBytes': {},
     'cefAdjHCPkts': {},
     'cefAdjMTU': {},
     'cefAdjPkts': {},
     'cefAdjSource': {},
     'cefAdjSummaryComplete': {},
     'cefAdjSummaryFixup': {},
     'cefAdjSummaryIncomplete': {},
     'cefAdjSummaryRedirect': {},
     'cefCCCount': {},
     'cefCCEnabled': {},
     'cefCCGlobalAutoRepairDelay': {},
     'cefCCGlobalAutoRepairEnabled': {},
     'cefCCGlobalAutoRepairHoldDown': {},
     'cefCCGlobalErrorMsgEnabled': {},
     'cefCCGlobalFullScanAction': {},
     'cefCCGlobalFullScanStatus': {},
     'cefCCPeriod': {},
     'cefCCQueriesChecked': {},
     'cefCCQueriesIgnored': {},
     'cefCCQueriesIterated': {},
     'cefCCQueriesSent': {},
     'cefCfgAccountingMap': {},
     'cefCfgAdminState': {},
     'cefCfgDistributionAdminState': {},
     'cefCfgDistributionOperState': {},
     'cefCfgLoadSharingAlgorithm': {},
     'cefCfgLoadSharingID': {},
     'cefCfgOperState': {},
     'cefCfgTrafficStatsLoadInterval': {},
     'cefCfgTrafficStatsUpdateRate': {},
     'cefFESelectionAdjConnId': {},
     'cefFESelectionAdjInterface': {},
     'cefFESelectionAdjLinkType': {},
     'cefFESelectionAdjNextHopAddr': {},
     'cefFESelectionAdjNextHopAddrType': {},
     'cefFESelectionLabels': {},
     'cefFESelectionSpecial': {},
     'cefFESelectionVrfName': {},
     'cefFESelectionWeight': {},
     'cefFIBSummaryFwdPrefixes': {},
     'cefInconsistencyCCType': {},
     'cefInconsistencyEntity': {},
     'cefInconsistencyNotifEnable': {},
     'cefInconsistencyPrefixAddr': {},
     'cefInconsistencyPrefixLen': {},
     'cefInconsistencyPrefixType': {},
     'cefInconsistencyReason': {},
     'cefInconsistencyReset': {},
     'cefInconsistencyResetStatus': {},
     'cefInconsistencyVrfName': {},
     'cefIntLoadSharing': {},
     'cefIntNonrecursiveAccouting': {},
     'cefIntSwitchingState': {},
     'cefLMPrefixAddr': {},
     'cefLMPrefixLen': {},
     'cefLMPrefixRowStatus': {},
     'cefLMPrefixSpinLock': {},
     'cefLMPrefixState': {},
     'cefNotifThrottlingInterval': {},
     'cefPathInterface': {},
     'cefPathNextHopAddr': {},
     'cefPathRecurseVrfName': {},
     'cefPathType': {},
     'cefPeerFIBOperState': {},
     'cefPeerFIBStateChangeNotifEnable': {},
     'cefPeerNumberOfResets': {},
     'cefPeerOperState': {},
     'cefPeerStateChangeNotifEnable': {},
     'cefPrefixBytes': {},
     'cefPrefixExternalNRBytes': {},
     'cefPrefixExternalNRHCBytes': {},
     'cefPrefixExternalNRHCPkts': {},
     'cefPrefixExternalNRPkts': {},
     'cefPrefixForwardingInfo': {},
     'cefPrefixHCBytes': {},
     'cefPrefixHCPkts': {},
     'cefPrefixInternalNRBytes': {},
     'cefPrefixInternalNRHCBytes': {},
     'cefPrefixInternalNRHCPkts': {},
     'cefPrefixInternalNRPkts': {},
     'cefPrefixPkts': {},
     'cefResourceFailureNotifEnable': {},
     'cefResourceFailureReason': {},
     'cefResourceMemoryUsed': {},
     'cefStatsPrefixDeletes': {},
     'cefStatsPrefixElements': {},
     'cefStatsPrefixHCDeletes': {},
     'cefStatsPrefixHCElements': {},
     'cefStatsPrefixHCInserts': {},
     'cefStatsPrefixHCQueries': {},
     'cefStatsPrefixInserts': {},
     'cefStatsPrefixQueries': {},
     'cefSwitchingDrop': {},
     'cefSwitchingHCDrop': {},
     'cefSwitchingHCPunt': {},
     'cefSwitchingHCPunt2Host': {},
     'cefSwitchingPath': {},
     'cefSwitchingPunt': {},
     'cefSwitchingPunt2Host': {},
     'cefcFRUPowerStatusTable.1.1': {},
     'cefcFRUPowerStatusTable.1.2': {},
     'cefcFRUPowerStatusTable.1.3': {},
     'cefcFRUPowerStatusTable.1.4': {},
     'cefcFRUPowerStatusTable.1.5': {},
     'cefcFRUPowerSupplyGroupTable.1.1': {},
     'cefcFRUPowerSupplyGroupTable.1.2': {},
     'cefcFRUPowerSupplyGroupTable.1.3': {},
     'cefcFRUPowerSupplyGroupTable.1.4': {},
     'cefcFRUPowerSupplyGroupTable.1.5': {},
     'cefcFRUPowerSupplyGroupTable.1.6': {},
     'cefcFRUPowerSupplyGroupTable.1.7': {},
     'cefcFRUPowerSupplyValueTable.1.1': {},
     'cefcFRUPowerSupplyValueTable.1.2': {},
     'cefcFRUPowerSupplyValueTable.1.3': {},
     'cefcFRUPowerSupplyValueTable.1.4': {},
     'cefcMIBEnableStatusNotification': {},
     'cefcMaxDefaultInLinePower': {},
     'cefcModuleTable.1.1': {},
     'cefcModuleTable.1.2': {},
     'cefcModuleTable.1.3': {},
     'cefcModuleTable.1.4': {},
     'cefcModuleTable.1.5': {},
     'cefcModuleTable.1.6': {},
     'cefcModuleTable.1.7': {},
     'cefcModuleTable.1.8': {},
     'cempMIBObjects.2.1': {},
     'cempMemBufferCachePoolEntry': {'1': {},
                                     '2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {}},
     'cempMemBufferPoolEntry': {'10': {},
                                '11': {},
                                '12': {},
                                '13': {},
                                '16': {},
                                '17': {},
                                '18': {},
                                '19': {},
                                '2': {},
                                '20': {},
                                '21': {},
                                '22': {},
                                '3': {},
                                '4': {},
                                '5': {},
                                '6': {},
                                '7': {},
                                '8': {},
                                '9': {}},
     'cempMemPoolEntry': {'10': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'cepConfigFallingThreshold': {},
     'cepConfigPerfRange': {},
     'cepConfigRisingThreshold': {},
     'cepConfigThresholdNotifEnabled': {},
     'cepEntityLastReloadTime': {},
     'cepEntityNumReloads': {},
     'cepIntervalStatsCreateTime': {},
     'cepIntervalStatsMeasurement': {},
     'cepIntervalStatsRange': {},
     'cepIntervalStatsValidData': {},
     'cepIntervalTimeElapsed': {},
     'cepStatsAlgorithm': {},
     'cepStatsMeasurement': {},
     'cepThresholdNotifEnabled': {},
     'cepThroughputAvgRate': {},
     'cepThroughputInterval': {},
     'cepThroughputLevel': {},
     'cepThroughputLicensedBW': {},
     'cepThroughputNotifEnabled': {},
     'cepThroughputThreshold': {},
     'cepValidIntervalCount': {},
     'ceqfpFiveMinutesUtilAlgo': {},
     'ceqfpFiveSecondUtilAlgo': {},
     'ceqfpMemoryResCurrentFallingThresh': {},
     'ceqfpMemoryResCurrentRisingThresh': {},
     'ceqfpMemoryResFallingThreshold': {},
     'ceqfpMemoryResFree': {},
     'ceqfpMemoryResInUse': {},
     'ceqfpMemoryResLowFreeWatermark': {},
     'ceqfpMemoryResRisingThreshold': {},
     'ceqfpMemoryResThreshNotifEnabled': {},
     'ceqfpMemoryResTotal': {},
     'ceqfpMemoryResourceEntry': {'10': {},
                                  '11': {},
                                  '12': {},
                                  '13': {},
                                  '14': {},
                                  '15': {},
                                  '8': {},
                                  '9': {}},
     'ceqfpNumberSystemLoads': {},
     'ceqfpOneMinuteUtilAlgo': {},
     'ceqfpSixtyMinutesUtilAlgo': {},
     'ceqfpSystemLastLoadTime': {},
     'ceqfpSystemState': {},
     'ceqfpSystemTrafficDirection': {},
     'ceqfpThroughputAvgRate': {},
     'ceqfpThroughputLevel': {},
     'ceqfpThroughputLicensedBW': {},
     'ceqfpThroughputNotifEnabled': {},
     'ceqfpThroughputSamplePeriod': {},
     'ceqfpThroughputThreshold': {},
     'ceqfpUtilInputNonPriorityBitRate': {},
     'ceqfpUtilInputNonPriorityPktRate': {},
     'ceqfpUtilInputPriorityBitRate': {},
     'ceqfpUtilInputPriorityPktRate': {},
     'ceqfpUtilInputTotalBitRate': {},
     'ceqfpUtilInputTotalPktRate': {},
     'ceqfpUtilOutputNonPriorityBitRate': {},
     'ceqfpUtilOutputNonPriorityPktRate': {},
     'ceqfpUtilOutputPriorityBitRate': {},
     'ceqfpUtilOutputPriorityPktRate': {},
     'ceqfpUtilOutputTotalBitRate': {},
     'ceqfpUtilOutputTotalPktRate': {},
     'ceqfpUtilProcessingLoad': {},
     'cermConfigResGroupRowStatus': {},
     'cermConfigResGroupStorageType': {},
     'cermConfigResGroupUserRowStatus': {},
     'cermConfigResGroupUserStorageType': {},
     'cermConfigResGroupUserTypeName': {},
     'cermNotifsDirection': {},
     'cermNotifsEnabled': {},
     'cermNotifsPolicyName': {},
     'cermNotifsThresholdIsUserGlob': {},
     'cermNotifsThresholdSeverity': {},
     'cermNotifsThresholdValue': {},
     'cermPolicyApplyPolicyName': {},
     'cermPolicyApplyRowStatus': {},
     'cermPolicyApplyStorageType': {},
     'cermPolicyFallingInterval': {},
     'cermPolicyFallingThreshold': {},
     'cermPolicyIsGlobal': {},
     'cermPolicyLoggingEnabled': {},
     'cermPolicyResOwnerThreshRowStatus': {},
     'cermPolicyResOwnerThreshStorageType': {},
     'cermPolicyRisingInterval': {},
     'cermPolicyRisingThreshold': {},
     'cermPolicyRowStatus': {},
     'cermPolicySnmpNotifEnabled': {},
     'cermPolicyStorageType': {},
     'cermPolicyUserTypeName': {},
     'cermResGroupName': {},
     'cermResGroupResUserId': {},
     'cermResGroupUserInstanceCount': {},
     'cermResMonitorName': {},
     'cermResMonitorPolicyName': {},
     'cermResMonitorResPolicyName': {},
     'cermResOwnerMeasurementUnit': {},
     'cermResOwnerName': {},
     'cermResOwnerResGroupCount': {},
     'cermResOwnerResUserCount': {},
     'cermResOwnerSubTypeFallingInterval': {},
     'cermResOwnerSubTypeFallingThresh': {},
     'cermResOwnerSubTypeGlobNotifSeverity': {},
     'cermResOwnerSubTypeMaxUsage': {},
     'cermResOwnerSubTypeName': {},
     'cermResOwnerSubTypeRisingInterval': {},
     'cermResOwnerSubTypeRisingThresh': {},
     'cermResOwnerSubTypeUsage': {},
     'cermResOwnerSubTypeUsagePct': {},
     'cermResOwnerThreshIsConfigurable': {},
     'cermResUserName': {},
     'cermResUserOrGroupFallingInterval': {},
     'cermResUserOrGroupFallingThresh': {},
     'cermResUserOrGroupFlag': {},
     'cermResUserOrGroupGlobNotifSeverity': {},
     'cermResUserOrGroupMaxUsage': {},
     'cermResUserOrGroupNotifSeverity': {},
     'cermResUserOrGroupRisingInterval': {},
     'cermResUserOrGroupRisingThresh': {},
     'cermResUserOrGroupThreshFlag': {},
     'cermResUserOrGroupUsage': {},
     'cermResUserOrGroupUsagePct': {},
     'cermResUserPriority': {},
     'cermResUserResGroupId': {},
     'cermResUserTypeName': {},
     'cermResUserTypeResGroupCount': {},
     'cermResUserTypeResOwnerCount': {},
     'cermResUserTypeResOwnerId': {},
     'cermResUserTypeResUserCount': {},
     'cermScalarsGlobalPolicyName': {},
     'cevcEvcActiveUnis': {},
     'cevcEvcCfgUnis': {},
     'cevcEvcIdentifier': {},
     'cevcEvcLocalUniIfIndex': {},
     'cevcEvcNotifyEnabled': {},
     'cevcEvcOperStatus': {},
     'cevcEvcRowStatus': {},
     'cevcEvcStorageType': {},
     'cevcEvcType': {},
     'cevcEvcUniId': {},
     'cevcEvcUniOperStatus': {},
     'cevcMacAddress': {},
     'cevcMaxMacConfigLimit': {},
     'cevcMaxNumEvcs': {},
     'cevcNumCfgEvcs': {},
     'cevcPortL2ControlProtocolAction': {},
     'cevcPortMaxNumEVCs': {},
     'cevcPortMaxNumServiceInstances': {},
     'cevcPortMode': {},
     'cevcSIAdminStatus': {},
     'cevcSICEVlanEndingVlan': {},
     'cevcSICEVlanRowStatus': {},
     'cevcSICEVlanStorageType': {},
     'cevcSICreationType': {},
     'cevcSIEvcIndex': {},
     'cevcSIForwardBdNumber': {},
     'cevcSIForwardBdNumber1kBitmap': {},
     'cevcSIForwardBdNumber2kBitmap': {},
     'cevcSIForwardBdNumber3kBitmap': {},
     'cevcSIForwardBdNumber4kBitmap': {},
     'cevcSIForwardBdNumberBase': {},
     'cevcSIForwardBdRowStatus': {},
     'cevcSIForwardBdStorageType': {},
     'cevcSIForwardingType': {},
     'cevcSIID': {},
     'cevcSIL2ControlProtocolAction': {},
     'cevcSIMatchCriteriaType': {},
     'cevcSIMatchEncapEncapsulation': {},
     'cevcSIMatchEncapPayloadType': {},
     'cevcSIMatchEncapPayloadTypes': {},
     'cevcSIMatchEncapPrimaryCos': {},
     'cevcSIMatchEncapPriorityCos': {},
     'cevcSIMatchEncapRowStatus': {},
     'cevcSIMatchEncapSecondaryCos': {},
     'cevcSIMatchEncapStorageType': {},
     'cevcSIMatchEncapValid': {},
     'cevcSIMatchRowStatus': {},
     'cevcSIMatchStorageType': {},
     'cevcSIName': {},
     'cevcSIOperStatus': {},
     'cevcSIPrimaryVlanEndingVlan': {},
     'cevcSIPrimaryVlanRowStatus': {},
     'cevcSIPrimaryVlanStorageType': {},
     'cevcSIRowStatus': {},
     'cevcSISecondaryVlanEndingVlan': {},
     'cevcSISecondaryVlanRowStatus': {},
     'cevcSISecondaryVlanStorageType': {},
     'cevcSIStorageType': {},
     'cevcSITarget': {},
     'cevcSITargetType': {},
     'cevcSIType': {},
     'cevcSIVlanRewriteAction': {},
     'cevcSIVlanRewriteEncapsulation': {},
     'cevcSIVlanRewriteRowStatus': {},
     'cevcSIVlanRewriteStorageType': {},
     'cevcSIVlanRewriteSymmetric': {},
     'cevcSIVlanRewriteVlan1': {},
     'cevcSIVlanRewriteVlan2': {},
     'cevcUniCEVlanEvcEndingVlan': {},
     'cevcUniIdentifier': {},
     'cevcUniPortType': {},
     'cevcUniServiceAttributes': {},
     'cevcViolationCause': {},
     'cfcRequestTable.1.10': {},
     'cfcRequestTable.1.11': {},
     'cfcRequestTable.1.12': {},
     'cfcRequestTable.1.2': {},
     'cfcRequestTable.1.3': {},
     'cfcRequestTable.1.4': {},
     'cfcRequestTable.1.5': {},
     'cfcRequestTable.1.6': {},
     'cfcRequestTable.1.7': {},
     'cfcRequestTable.1.8': {},
     'cfcRequestTable.1.9': {},
     'cfmAlarmGroupConditionId': {},
     'cfmAlarmGroupConditionsProfile': {},
     'cfmAlarmGroupCurrentCount': {},
     'cfmAlarmGroupDescr': {},
     'cfmAlarmGroupFlowCount': {},
     'cfmAlarmGroupFlowId': {},
     'cfmAlarmGroupFlowSet': {},
     'cfmAlarmGroupFlowTableChanged': {},
     'cfmAlarmGroupRaised': {},
     'cfmAlarmGroupTableChanged': {},
     'cfmAlarmGroupThreshold': {},
     'cfmAlarmGroupThresholdUnits': {},
     'cfmAlarmHistoryConditionId': {},
     'cfmAlarmHistoryConditionsProfile': {},
     'cfmAlarmHistoryEntity': {},
     'cfmAlarmHistoryLastId': {},
     'cfmAlarmHistorySeverity': {},
     'cfmAlarmHistorySize': {},
     'cfmAlarmHistoryTime': {},
     'cfmAlarmHistoryType': {},
     'cfmConditionAlarm': {},
     'cfmConditionAlarmActions': {},
     'cfmConditionAlarmGroup': {},
     'cfmConditionAlarmSeverity': {},
     'cfmConditionDescr': {},
     'cfmConditionMonitoredElement': {},
     'cfmConditionSampleType': {},
     'cfmConditionSampleWindow': {},
     'cfmConditionTableChanged': {},
     'cfmConditionThreshFall': {},
     'cfmConditionThreshFallPrecision': {},
     'cfmConditionThreshFallScale': {},
     'cfmConditionThreshRise': {},
     'cfmConditionThreshRisePrecision': {},
     'cfmConditionThreshRiseScale': {},
     'cfmConditionType': {},
     'cfmFlowAdminStatus': {},
     'cfmFlowCreateTime': {},
     'cfmFlowDescr': {},
     'cfmFlowDirection': {},
     'cfmFlowDiscontinuityTime': {},
     'cfmFlowEgress': {},
     'cfmFlowEgressType': {},
     'cfmFlowExpirationTime': {},
     'cfmFlowIngress': {},
     'cfmFlowIngressType': {},
     'cfmFlowIpAddrDst': {},
     'cfmFlowIpAddrSrc': {},
     'cfmFlowIpAddrType': {},
     'cfmFlowIpEntry': {'10': {}, '8': {}, '9': {}},
     'cfmFlowIpHopLimit': {},
     'cfmFlowIpNext': {},
     'cfmFlowIpTableChanged': {},
     'cfmFlowIpTrafficClass': {},
     'cfmFlowIpValid': {},
     'cfmFlowL2InnerVlanCos': {},
     'cfmFlowL2InnerVlanId': {},
     'cfmFlowL2VlanCos': {},
     'cfmFlowL2VlanId': {},
     'cfmFlowL2VlanNext': {},
     'cfmFlowL2VlanTableChanged': {},
     'cfmFlowMetricsAlarmSeverity': {},
     'cfmFlowMetricsAlarms': {},
     'cfmFlowMetricsBitRate': {},
     'cfmFlowMetricsBitRateUnits': {},
     'cfmFlowMetricsCollected': {},
     'cfmFlowMetricsConditions': {},
     'cfmFlowMetricsConditionsProfile': {},
     'cfmFlowMetricsElapsedTime': {},
     'cfmFlowMetricsEntry': {'22': {},
                             '23': {},
                             '24': {},
                             '25': {},
                             '26': {},
                             '27': {},
                             '28': {},
                             '29': {}},
     'cfmFlowMetricsErrorSecs': {},
     'cfmFlowMetricsErrorSecsPrecision': {},
     'cfmFlowMetricsErrorSecsScale': {},
     'cfmFlowMetricsIntAlarmSeverity': {},
     'cfmFlowMetricsIntAlarms': {},
     'cfmFlowMetricsIntBitRate': {},
     'cfmFlowMetricsIntBitRateUnits': {},
     'cfmFlowMetricsIntConditions': {},
     'cfmFlowMetricsIntEntry': {'18': {},
                                '19': {},
                                '20': {},
                                '21': {},
                                '22': {},
                                '23': {},
                                '24': {},
                                '25': {},
                                '26': {},
                                '27': {},
                                '28': {}},
     'cfmFlowMetricsIntErrorSecs': {},
     'cfmFlowMetricsIntErrorSecsPrecision': {},
     'cfmFlowMetricsIntErrorSecsScale': {},
     'cfmFlowMetricsIntOctets': {},
     'cfmFlowMetricsIntPktRate': {},
     'cfmFlowMetricsIntPkts': {},
     'cfmFlowMetricsIntTime': {},
     'cfmFlowMetricsIntTransportAvailability': {},
     'cfmFlowMetricsIntTransportAvailabilityPrecision': {},
     'cfmFlowMetricsIntTransportAvailabilityScale': {},
     'cfmFlowMetricsIntValid': {},
     'cfmFlowMetricsIntervalTime': {},
     'cfmFlowMetricsIntervals': {},
     'cfmFlowMetricsInvalidIntervals': {},
     'cfmFlowMetricsMaxIntervals': {},
     'cfmFlowMetricsOctets': {},
     'cfmFlowMetricsPktRate': {},
     'cfmFlowMetricsPkts': {},
     'cfmFlowMetricsTableChanged': {},
     'cfmFlowMetricsTransportAvailability': {},
     'cfmFlowMetricsTransportAvailabilityPrecision': {},
     'cfmFlowMetricsTransportAvailabilityScale': {},
     'cfmFlowMonitorAlarmCriticalCount': {},
     'cfmFlowMonitorAlarmInfoCount': {},
     'cfmFlowMonitorAlarmMajorCount': {},
     'cfmFlowMonitorAlarmMinorCount': {},
     'cfmFlowMonitorAlarmSeverity': {},
     'cfmFlowMonitorAlarmWarningCount': {},
     'cfmFlowMonitorAlarms': {},
     'cfmFlowMonitorCaps': {},
     'cfmFlowMonitorConditions': {},
     'cfmFlowMonitorConditionsProfile': {},
     'cfmFlowMonitorDescr': {},
     'cfmFlowMonitorFlowCount': {},
     'cfmFlowMonitorTableChanged': {},
     'cfmFlowNext': {},
     'cfmFlowOperStatus': {},
     'cfmFlowRtpNext': {},
     'cfmFlowRtpPayloadType': {},
     'cfmFlowRtpSsrc': {},
     'cfmFlowRtpTableChanged': {},
     'cfmFlowRtpVersion': {},
     'cfmFlowTableChanged': {},
     'cfmFlowTcpNext': {},
     'cfmFlowTcpPortDst': {},
     'cfmFlowTcpPortSrc': {},
     'cfmFlowTcpTableChanged': {},
     'cfmFlowUdpNext': {},
     'cfmFlowUdpPortDst': {},
     'cfmFlowUdpPortSrc': {},
     'cfmFlowUdpTableChanged': {},
     'cfmFlows': {'14': {}},
     'cfmFlows.13.1.1': {},
     'cfmFlows.13.1.2': {},
     'cfmFlows.13.1.3': {},
     'cfmFlows.13.1.4': {},
     'cfmFlows.13.1.5': {},
     'cfmFlows.13.1.6': {},
     'cfmFlows.13.1.7': {},
     'cfmFlows.13.1.8': {},
     'cfmIpCbrMetricsCfgBitRate': {},
     'cfmIpCbrMetricsCfgMediaPktSize': {},
     'cfmIpCbrMetricsCfgRate': {},
     'cfmIpCbrMetricsCfgRateType': {},
     'cfmIpCbrMetricsEntry': {'10': {},
                              '11': {},
                              '12': {},
                              '13': {},
                              '14': {},
                              '15': {}},
     'cfmIpCbrMetricsIntDf': {},
     'cfmIpCbrMetricsIntDfPrecision': {},
     'cfmIpCbrMetricsIntDfScale': {},
     'cfmIpCbrMetricsIntEntry': {'13': {},
                                 '14': {},
                                 '15': {},
                                 '16': {},
                                 '17': {},
                                 '18': {}},
     'cfmIpCbrMetricsIntLostPkts': {},
     'cfmIpCbrMetricsIntMr': {},
     'cfmIpCbrMetricsIntMrUnits': {},
     'cfmIpCbrMetricsIntMrv': {},
     'cfmIpCbrMetricsIntMrvPrecision': {},
     'cfmIpCbrMetricsIntMrvScale': {},
     'cfmIpCbrMetricsIntValid': {},
     'cfmIpCbrMetricsIntVbMax': {},
     'cfmIpCbrMetricsIntVbMin': {},
     'cfmIpCbrMetricsLostPkts': {},
     'cfmIpCbrMetricsMrv': {},
     'cfmIpCbrMetricsMrvPrecision': {},
     'cfmIpCbrMetricsMrvScale': {},
     'cfmIpCbrMetricsTableChanged': {},
     'cfmIpCbrMetricsValid': {},
     'cfmMdiMetricsCfgBitRate': {},
     'cfmMdiMetricsCfgMediaPktSize': {},
     'cfmMdiMetricsCfgRate': {},
     'cfmMdiMetricsCfgRateType': {},
     'cfmMdiMetricsEntry': {'10': {}},
     'cfmMdiMetricsIntDf': {},
     'cfmMdiMetricsIntDfPrecision': {},
     'cfmMdiMetricsIntDfScale': {},
     'cfmMdiMetricsIntEntry': {'13': {}},
     'cfmMdiMetricsIntLostPkts': {},
     'cfmMdiMetricsIntMlr': {},
     'cfmMdiMetricsIntMlrPrecision': {},
     'cfmMdiMetricsIntMlrScale': {},
     'cfmMdiMetricsIntMr': {},
     'cfmMdiMetricsIntMrUnits': {},
     'cfmMdiMetricsIntValid': {},
     'cfmMdiMetricsIntVbMax': {},
     'cfmMdiMetricsIntVbMin': {},
     'cfmMdiMetricsLostPkts': {},
     'cfmMdiMetricsMlr': {},
     'cfmMdiMetricsMlrPrecision': {},
     'cfmMdiMetricsMlrScale': {},
     'cfmMdiMetricsTableChanged': {},
     'cfmMdiMetricsValid': {},
     'cfmMetadataFlowAllAttrPen': {},
     'cfmMetadataFlowAllAttrValue': {},
     'cfmMetadataFlowAttrType': {},
     'cfmMetadataFlowAttrValue': {},
     'cfmMetadataFlowDestAddr': {},
     'cfmMetadataFlowDestAddrType': {},
     'cfmMetadataFlowDestPort': {},
     'cfmMetadataFlowProtocolType': {},
     'cfmMetadataFlowSSRC': {},
     'cfmMetadataFlowSrcAddr': {},
     'cfmMetadataFlowSrcAddrType': {},
     'cfmMetadataFlowSrcPort': {},
     'cfmNotifyEnable': {},
     'cfmRtpMetricsAvgLD': {},
     'cfmRtpMetricsAvgLDPrecision': {},
     'cfmRtpMetricsAvgLDScale': {},
     'cfmRtpMetricsAvgLossDistance': {},
     'cfmRtpMetricsEntry': {'18': {},
                            '19': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '26': {},
                            '27': {},
                            '28': {},
                            '29': {},
                            '30': {},
                            '31': {}},
     'cfmRtpMetricsExpectedPkts': {},
     'cfmRtpMetricsFrac': {},
     'cfmRtpMetricsFracPrecision': {},
     'cfmRtpMetricsFracScale': {},
     'cfmRtpMetricsIntAvgLD': {},
     'cfmRtpMetricsIntAvgLDPrecision': {},
     'cfmRtpMetricsIntAvgLDScale': {},
     'cfmRtpMetricsIntAvgLossDistance': {},
     'cfmRtpMetricsIntEntry': {'21': {},
                               '22': {},
                               '23': {},
                               '24': {},
                               '25': {},
                               '26': {},
                               '27': {},
                               '28': {},
                               '29': {},
                               '30': {},
                               '31': {},
                               '32': {},
                               '33': {},
                               '34': {}},
     'cfmRtpMetricsIntExpectedPkts': {},
     'cfmRtpMetricsIntFrac': {},
     'cfmRtpMetricsIntFracPrecision': {},
     'cfmRtpMetricsIntFracScale': {},
     'cfmRtpMetricsIntJitter': {},
     'cfmRtpMetricsIntJitterPrecision': {},
     'cfmRtpMetricsIntJitterScale': {},
     'cfmRtpMetricsIntLIs': {},
     'cfmRtpMetricsIntLostPkts': {},
     'cfmRtpMetricsIntMaxJitter': {},
     'cfmRtpMetricsIntMaxJitterPrecision': {},
     'cfmRtpMetricsIntMaxJitterScale': {},
     'cfmRtpMetricsIntTransit': {},
     'cfmRtpMetricsIntTransitPrecision': {},
     'cfmRtpMetricsIntTransitScale': {},
     'cfmRtpMetricsIntValid': {},
     'cfmRtpMetricsJitter': {},
     'cfmRtpMetricsJitterPrecision': {},
     'cfmRtpMetricsJitterScale': {},
     'cfmRtpMetricsLIs': {},
     'cfmRtpMetricsLostPkts': {},
     'cfmRtpMetricsMaxJitter': {},
     'cfmRtpMetricsMaxJitterPrecision': {},
     'cfmRtpMetricsMaxJitterScale': {},
     'cfmRtpMetricsTableChanged': {},
     'cfmRtpMetricsValid': {},
     'cfrCircuitEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cfrConnectionEntry': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'cfrElmiEntry': {'1': {}, '2': {}, '3': {}},
     'cfrElmiNeighborEntry': {'1': {},
                              '2': {},
                              '3': {},
                              '4': {},
                              '5': {},
                              '6': {}},
     'cfrElmiObjs': {'1': {}},
     'cfrExtCircuitEntry': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '2': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '26': {},
                            '27': {},
                            '28': {},
                            '29': {},
                            '3': {},
                            '30': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'cfrFragEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'cfrLmiEntry': {'1': {},
                     '10': {},
                     '11': {},
                     '12': {},
                     '13': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'cfrMapEntry': {'1': {},
                     '10': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'cfrSvcEntry': {'1': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {}},
     'chassis': {'1': {},
                 '10': {},
                 '12': {},
                 '14': {},
                 '15': {},
                 '2': {},
                 '3': {},
                 '4': {},
                 '5': {},
                 '6': {},
                 '7': {},
                 '8': {},
                 '9': {}},
     'cieIfDot1dBaseMappingEntry': {'1': {}},
     'cieIfDot1qCustomEtherTypeEntry': {'1': {}, '2': {}},
     'cieIfInterfaceEntry': {'1': {},
                             '10': {},
                             '11': {},
                             '12': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'cieIfNameMappingEntry': {'2': {}},
     'cieIfPacketStatsEntry': {'1': {},
                               '10': {},
                               '11': {},
                               '12': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cieIfUtilEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ciiAreaAddrEntry': {'1': {}},
     'ciiCircEntry': {'10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '8': {},
                      '9': {}},
     'ciiCircLevelEntry': {'10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'ciiCircuitCounterEntry': {'10': {},
                                '2': {},
                                '3': {},
                                '5': {},
                                '6': {},
                                '7': {},
                                '8': {},
                                '9': {}},
     'ciiIPRAEntry': {'10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'ciiISAdjAreaAddrEntry': {'2': {}},
     'ciiISAdjEntry': {'10': {},
                       '11': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'ciiISAdjIPAddrEntry': {'2': {}, '3': {}},
     'ciiISAdjProtSuppEntry': {'1': {}},
     'ciiLSPSummaryEntry': {'3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'ciiLSPTLVEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'ciiManAreaAddrEntry': {'2': {}},
     'ciiPacketCounterEntry': {'3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'ciiRAEntry': {'11': {},
                    '2': {},
                    '3': {},
                    '4': {},
                    '5': {},
                    '6': {},
                    '7': {},
                    '8': {}},
     'ciiRedistributeAddrEntry': {'4': {}},
     'ciiRouterEntry': {'3': {}, '4': {}},
     'ciiSummAddrEntry': {'4': {}, '5': {}, '6': {}},
     'ciiSysLevelEntry': {'2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'ciiSysObject': {'1': {},
                      '10': {},
                      '11': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '8': {},
                      '9': {}},
     'ciiSysProtSuppEntry': {'2': {}},
     'ciiSystemCounterEntry': {'10': {},
                               '12': {},
                               '13': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cipMacEntry': {'3': {}, '4': {}},
     'cipMacFreeEntry': {'2': {}},
     'cipMacXEntry': {'1': {}, '2': {}},
     'cipPrecedenceEntry': {'3': {}, '4': {}},
     'cipPrecedenceXEntry': {'1': {}, '2': {}},
     'cipUrpfComputeInterval': {},
     'cipUrpfDropNotifyHoldDownTime': {},
     'cipUrpfDropRate': {},
     'cipUrpfDropRateWindow': {},
     'cipUrpfDrops': {},
     'cipUrpfIfCheckStrict': {},
     'cipUrpfIfDiscontinuityTime': {},
     'cipUrpfIfDropRate': {},
     'cipUrpfIfDropRateNotifyEnable': {},
     'cipUrpfIfDrops': {},
     'cipUrpfIfNotifyDrHoldDownReset': {},
     'cipUrpfIfNotifyDropRateThreshold': {},
     'cipUrpfIfSuppressedDrops': {},
     'cipUrpfIfVrfName': {},
     'cipUrpfIfWhichRouteTableID': {},
     'cipUrpfVrfIfDiscontinuityTime': {},
     'cipUrpfVrfIfDrops': {},
     'cipUrpfVrfName': {},
     'cipslaAutoGroupDescription': {},
     'cipslaAutoGroupDestEndPointName': {},
     'cipslaAutoGroupOperTemplateName': {},
     'cipslaAutoGroupOperType': {},
     'cipslaAutoGroupQoSEnable': {},
     'cipslaAutoGroupRowStatus': {},
     'cipslaAutoGroupSchedAgeout': {},
     'cipslaAutoGroupSchedInterval': {},
     'cipslaAutoGroupSchedLife': {},
     'cipslaAutoGroupSchedMaxInterval': {},
     'cipslaAutoGroupSchedMinInterval': {},
     'cipslaAutoGroupSchedPeriod': {},
     'cipslaAutoGroupSchedRowStatus': {},
     'cipslaAutoGroupSchedStartTime': {},
     'cipslaAutoGroupSchedStorageType': {},
     'cipslaAutoGroupSchedulerId': {},
     'cipslaAutoGroupStorageType': {},
     'cipslaAutoGroupType': {},
     'cipslaBaseEndPointDescription': {},
     'cipslaBaseEndPointRowStatus': {},
     'cipslaBaseEndPointStorageType': {},
     'cipslaIPEndPointADDestIPAgeout': {},
     'cipslaIPEndPointADDestPort': {},
     'cipslaIPEndPointADMeasureRetry': {},
     'cipslaIPEndPointADRowStatus': {},
     'cipslaIPEndPointADStorageType': {},
     'cipslaIPEndPointRowStatus': {},
     'cipslaIPEndPointStorageType': {},
     'cipslaPercentileJitterAvg': {},
     'cipslaPercentileJitterDS': {},
     'cipslaPercentileJitterSD': {},
     'cipslaPercentileLatestAvg': {},
     'cipslaPercentileLatestMax': {},
     'cipslaPercentileLatestMin': {},
     'cipslaPercentileLatestNum': {},
     'cipslaPercentileLatestSum': {},
     'cipslaPercentileLatestSum2': {},
     'cipslaPercentileOWDS': {},
     'cipslaPercentileOWSD': {},
     'cipslaPercentileRTT': {},
     'cipslaReactActionType': {},
     'cipslaReactRowStatus': {},
     'cipslaReactStorageType': {},
     'cipslaReactThresholdCountX': {},
     'cipslaReactThresholdCountY': {},
     'cipslaReactThresholdFalling': {},
     'cipslaReactThresholdRising': {},
     'cipslaReactThresholdType': {},
     'cipslaReactVar': {},
     'ciscoAtmIfPVCs': {},
     'ciscoBfdObjects.1.1': {},
     'ciscoBfdObjects.1.3': {},
     'ciscoBfdObjects.1.4': {},
     'ciscoBfdSessDiag': {},
     'ciscoBfdSessEntry': {'10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '16': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '20': {},
                           '21': {},
                           '22': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '9': {}},
     'ciscoBfdSessMapEntry': {'1': {}},
     'ciscoBfdSessPerfEntry': {'1': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'ciscoBulkFileMIB.1.1.1': {},
     'ciscoBulkFileMIB.1.1.2': {},
     'ciscoBulkFileMIB.1.1.3': {},
     'ciscoBulkFileMIB.1.1.4': {},
     'ciscoBulkFileMIB.1.1.5': {},
     'ciscoBulkFileMIB.1.1.6': {},
     'ciscoBulkFileMIB.1.1.7': {},
     'ciscoBulkFileMIB.1.1.8': {},
     'ciscoBulkFileMIB.1.2.1': {},
     'ciscoBulkFileMIB.1.2.2': {},
     'ciscoBulkFileMIB.1.2.3': {},
     'ciscoBulkFileMIB.1.2.4': {},
     'ciscoCBQosMIBObjects.10.4.1.1': {},
     'ciscoCBQosMIBObjects.10.4.1.2': {},
     'ciscoCBQosMIBObjects.10.69.1.3': {},
     'ciscoCBQosMIBObjects.10.69.1.4': {},
     'ciscoCBQosMIBObjects.10.69.1.5': {},
     'ciscoCBQosMIBObjects.10.136.1.1': {},
     'ciscoCBQosMIBObjects.10.205.1.1': {},
     'ciscoCBQosMIBObjects.10.205.1.10': {},
     'ciscoCBQosMIBObjects.10.205.1.11': {},
     'ciscoCBQosMIBObjects.10.205.1.12': {},
     'ciscoCBQosMIBObjects.10.205.1.2': {},
     'ciscoCBQosMIBObjects.10.205.1.3': {},
     'ciscoCBQosMIBObjects.10.205.1.4': {},
     'ciscoCBQosMIBObjects.10.205.1.5': {},
     'ciscoCBQosMIBObjects.10.205.1.6': {},
     'ciscoCBQosMIBObjects.10.205.1.7': {},
     'ciscoCBQosMIBObjects.10.205.1.8': {},
     'ciscoCBQosMIBObjects.10.205.1.9': {},
     'ciscoCallHistory': {'1': {}, '2': {}},
     'ciscoCallHistoryEntry': {'10': {},
                               '11': {},
                               '12': {},
                               '13': {},
                               '14': {},
                               '15': {},
                               '16': {},
                               '17': {},
                               '18': {},
                               '19': {},
                               '20': {},
                               '21': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'ciscoCallHomeMIB.1.13.1': {},
     'ciscoCallHomeMIB.1.13.2': {},
     'ciscoDlswCircuitEntry': {'10': {},
                               '11': {},
                               '12': {},
                               '13': {},
                               '14': {},
                               '15': {},
                               '16': {},
                               '17': {},
                               '18': {},
                               '19': {},
                               '20': {},
                               '21': {},
                               '22': {},
                               '23': {},
                               '24': {},
                               '25': {},
                               '26': {},
                               '27': {},
                               '28': {},
                               '29': {},
                               '3': {},
                               '30': {},
                               '31': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {}},
     'ciscoDlswCircuitStat': {'1': {}, '2': {}},
     'ciscoDlswIfEntry': {'1': {}, '2': {}, '3': {}},
     'ciscoDlswNode': {'1': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'ciscoDlswTConnConfigEntry': {'10': {},
                                   '11': {},
                                   '12': {},
                                   '13': {},
                                   '2': {},
                                   '3': {},
                                   '4': {},
                                   '5': {},
                                   '6': {},
                                   '7': {},
                                   '8': {},
                                   '9': {}},
     'ciscoDlswTConnOperEntry': {'10': {},
                                 '11': {},
                                 '12': {},
                                 '13': {},
                                 '14': {},
                                 '15': {},
                                 '16': {},
                                 '17': {},
                                 '18': {},
                                 '19': {},
                                 '2': {},
                                 '20': {},
                                 '21': {},
                                 '22': {},
                                 '23': {},
                                 '24': {},
                                 '25': {},
                                 '26': {},
                                 '27': {},
                                 '28': {},
                                 '29': {},
                                 '30': {},
                                 '31': {},
                                 '32': {},
                                 '33': {},
                                 '34': {},
                                 '35': {},
                                 '36': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {},
                                 '9': {}},
     'ciscoDlswTConnStat': {'1': {}, '2': {}, '3': {}},
     'ciscoDlswTConnTcpConfigEntry': {'1': {}, '2': {}, '3': {}},
     'ciscoDlswTConnTcpOperEntry': {'1': {}, '2': {}, '3': {}},
     'ciscoDlswTrapControl': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ciscoEntityDiagMIB.1.2.1': {},
     'ciscoEntityFRUControlMIB.1.1.5': {},
     'ciscoEntityFRUControlMIB.10.9.2.1.1': {},
     'ciscoEntityFRUControlMIB.10.9.2.1.2': {},
     'ciscoEntityFRUControlMIB.10.9.3.1.1': {},
     'ciscoEntityFRUControlMIB.1.3.2': {},
     'ciscoEntityFRUControlMIB.10.25.1.1.1': {},
     'ciscoEntityFRUControlMIB.10.36.1.1.1': {},
     'ciscoEntityFRUControlMIB.10.49.1.1.2': {},
     'ciscoEntityFRUControlMIB.10.49.2.1.2': {},
     'ciscoEntityFRUControlMIB.10.49.2.1.3': {},
     'ciscoEntityFRUControlMIB.10.64.1.1.1': {},
     'ciscoEntityFRUControlMIB.10.64.1.1.2': {},
     'ciscoEntityFRUControlMIB.10.64.2.1.1': {},
     'ciscoEntityFRUControlMIB.10.64.2.1.2': {},
     'ciscoEntityFRUControlMIB.10.64.3.1.1': {},
     'ciscoEntityFRUControlMIB.10.64.3.1.2': {},
     'ciscoEntityFRUControlMIB.10.64.4.1.2': {},
     'ciscoEntityFRUControlMIB.10.64.4.1.3': {},
     'ciscoEntityFRUControlMIB.10.64.4.1.4': {},
     'ciscoEntityFRUControlMIB.10.64.4.1.5': {},
     'ciscoEntityFRUControlMIB.10.81.1.1.1': {},
     'ciscoEntityFRUControlMIB.10.81.2.1.1': {},
     'ciscoExperiment.10.151.1.1.2': {},
     'ciscoExperiment.10.151.1.1.3': {},
     'ciscoExperiment.10.151.1.1.4': {},
     'ciscoExperiment.10.151.1.1.5': {},
     'ciscoExperiment.10.151.1.1.6': {},
     'ciscoExperiment.10.151.1.1.7': {},
     'ciscoExperiment.10.151.2.1.1': {},
     'ciscoExperiment.10.151.2.1.2': {},
     'ciscoExperiment.10.151.2.1.3': {},
     'ciscoExperiment.10.151.3.1.1': {},
     'ciscoExperiment.10.151.3.1.2': {},
     'ciscoExperiment.10.19.1.1.2': {},
     'ciscoExperiment.10.19.1.1.3': {},
     'ciscoExperiment.10.19.1.1.4': {},
     'ciscoExperiment.10.19.1.1.5': {},
     'ciscoExperiment.10.19.1.1.6': {},
     'ciscoExperiment.10.19.1.1.7': {},
     'ciscoExperiment.10.19.1.1.8': {},
     'ciscoExperiment.10.19.2.1.2': {},
     'ciscoExperiment.10.19.2.1.3': {},
     'ciscoExperiment.10.19.2.1.4': {},
     'ciscoExperiment.10.19.2.1.5': {},
     'ciscoExperiment.10.19.2.1.6': {},
     'ciscoExperiment.10.19.2.1.7': {},
     'ciscoExperiment.10.225.1.1.13': {},
     'ciscoExperiment.10.225.1.1.14': {},
     'ciscoFlashChipEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'ciscoFlashCopyEntry': {'10': {},
                             '11': {},
                             '12': {},
                             '13': {},
                             '14': {},
                             '15': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'ciscoFlashDevice': {'1': {}},
     'ciscoFlashDeviceEntry': {'10': {},
                               '11': {},
                               '12': {},
                               '13': {},
                               '14': {},
                               '15': {},
                               '16': {},
                               '17': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'ciscoFlashFileByTypeEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ciscoFlashFileEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'ciscoFlashMIB.1.4.1': {},
     'ciscoFlashMIB.1.4.2': {},
     'ciscoFlashMiscOpEntry': {'2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {}},
     'ciscoFlashPartitionEntry': {'10': {},
                                  '11': {},
                                  '12': {},
                                  '13': {},
                                  '14': {},
                                  '2': {},
                                  '3': {},
                                  '4': {},
                                  '5': {},
                                  '6': {},
                                  '7': {},
                                  '8': {},
                                  '9': {}},
     'ciscoFlashPartitioningEntry': {'2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {},
                                     '9': {}},
     'ciscoFtpClientMIB.1.1.1': {},
     'ciscoFtpClientMIB.1.1.2': {},
     'ciscoFtpClientMIB.1.1.3': {},
     'ciscoFtpClientMIB.1.1.4': {},
     'ciscoIfExtSystemConfig': {'1': {}},
     'ciscoImageEntry': {'2': {}},
     'ciscoIpMRoute': {'1': {}},
     'ciscoIpMRouteEntry': {'12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '26': {},
                            '27': {},
                            '28': {},
                            '30': {},
                            '31': {},
                            '32': {},
                            '33': {},
                            '34': {},
                            '35': {},
                            '36': {},
                            '37': {},
                            '38': {},
                            '39': {},
                            '40': {},
                            '41': {}},
     'ciscoIpMRouteHeartBeatEntry': {'2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {}},
     'ciscoIpMRouteInterfaceEntry': {'1': {},
                                     '2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {}},
     'ciscoIpMRouteNextHopEntry': {'10': {}, '11': {}, '9': {}},
     'ciscoMemoryPoolEntry': {'2': {},
                              '3': {},
                              '4': {},
                              '5': {},
                              '6': {},
                              '7': {}},
     'ciscoMgmt.10.196.3.1': {},
     'ciscoMgmt.10.196.3.10': {},
     'ciscoMgmt.10.196.3.2': {},
     'ciscoMgmt.10.196.3.3': {},
     'ciscoMgmt.10.196.3.4': {},
     'ciscoMgmt.10.196.3.5': {},
     'ciscoMgmt.10.196.3.6.1.10': {},
     'ciscoMgmt.10.196.3.6.1.11': {},
     'ciscoMgmt.10.196.3.6.1.12': {},
     'ciscoMgmt.10.196.3.6.1.13': {},
     'ciscoMgmt.10.196.3.6.1.14': {},
     'ciscoMgmt.10.196.3.6.1.15': {},
     'ciscoMgmt.10.196.3.6.1.16': {},
     'ciscoMgmt.10.196.3.6.1.17': {},
     'ciscoMgmt.10.196.3.6.1.18': {},
     'ciscoMgmt.10.196.3.6.1.19': {},
     'ciscoMgmt.10.196.3.6.1.2': {},
     'ciscoMgmt.10.196.3.6.1.20': {},
     'ciscoMgmt.10.196.3.6.1.21': {},
     'ciscoMgmt.10.196.3.6.1.22': {},
     'ciscoMgmt.10.196.3.6.1.23': {},
     'ciscoMgmt.10.196.3.6.1.24': {},
     'ciscoMgmt.10.196.3.6.1.25': {},
     'ciscoMgmt.10.196.3.6.1.3': {},
     'ciscoMgmt.10.196.3.6.1.4': {},
     'ciscoMgmt.10.196.3.6.1.5': {},
     'ciscoMgmt.10.196.3.6.1.6': {},
     'ciscoMgmt.10.196.3.6.1.7': {},
     'ciscoMgmt.10.196.3.6.1.8': {},
     'ciscoMgmt.10.196.3.6.1.9': {},
     'ciscoMgmt.10.196.3.7': {},
     'ciscoMgmt.10.196.3.8': {},
     'ciscoMgmt.10.196.3.9': {},
     'ciscoMgmt.10.196.4.1.1.10': {},
     'ciscoMgmt.10.196.4.1.1.2': {},
     'ciscoMgmt.10.196.4.1.1.3': {},
     'ciscoMgmt.10.196.4.1.1.4': {},
     'ciscoMgmt.10.196.4.1.1.5': {},
     'ciscoMgmt.10.196.4.1.1.6': {},
     'ciscoMgmt.10.196.4.1.1.7': {},
     'ciscoMgmt.10.196.4.1.1.8': {},
     'ciscoMgmt.10.196.4.1.1.9': {},
     'ciscoMgmt.10.196.4.2.1.2': {},
     'ciscoMgmt.10.84.1.1.1.2': {},
     'ciscoMgmt.10.84.1.1.1.3': {},
     'ciscoMgmt.10.84.1.1.1.4': {},
     'ciscoMgmt.10.84.1.1.1.5': {},
     'ciscoMgmt.10.84.1.1.1.6': {},
     'ciscoMgmt.10.84.1.1.1.7': {},
     'ciscoMgmt.10.84.1.1.1.8': {},
     'ciscoMgmt.10.84.1.1.1.9': {},
     'ciscoMgmt.10.84.2.1.1.1': {},
     'ciscoMgmt.10.84.2.1.1.2': {},
     'ciscoMgmt.10.84.2.1.1.3': {},
     'ciscoMgmt.10.84.2.1.1.4': {},
     'ciscoMgmt.10.84.2.1.1.5': {},
     'ciscoMgmt.10.84.2.1.1.6': {},
     'ciscoMgmt.10.84.2.1.1.7': {},
     'ciscoMgmt.10.84.2.1.1.8': {},
     'ciscoMgmt.10.84.2.1.1.9': {},
     'ciscoMgmt.10.84.2.2.1.1': {},
     'ciscoMgmt.10.84.2.2.1.2': {},
     'ciscoMgmt.10.84.3.1.1.2': {},
     'ciscoMgmt.10.84.3.1.1.3': {},
     'ciscoMgmt.10.84.3.1.1.4': {},
     'ciscoMgmt.10.84.3.1.1.5': {},
     'ciscoMgmt.10.84.4.1.1.3': {},
     'ciscoMgmt.10.84.4.1.1.4': {},
     'ciscoMgmt.10.84.4.1.1.5': {},
     'ciscoMgmt.10.84.4.1.1.6': {},
     'ciscoMgmt.10.84.4.1.1.7': {},
     'ciscoMgmt.10.84.4.2.1.3': {},
     'ciscoMgmt.10.84.4.2.1.4': {},
     'ciscoMgmt.10.84.4.2.1.5': {},
     'ciscoMgmt.10.84.4.2.1.6': {},
     'ciscoMgmt.10.84.4.2.1.7': {},
     'ciscoMgmt.10.84.4.3.1.3': {},
     'ciscoMgmt.10.84.4.3.1.4': {},
     'ciscoMgmt.10.84.4.3.1.5': {},
     'ciscoMgmt.10.84.4.3.1.6': {},
     'ciscoMgmt.10.84.4.3.1.7': {},
     'ciscoMgmt.172.16.84.1.1': {},
     'ciscoMgmt.172.16.115.1.1': {},
     'ciscoMgmt.172.16.115.1.10': {},
     'ciscoMgmt.172.16.115.1.11': {},
     'ciscoMgmt.172.16.115.1.12': {},
     'ciscoMgmt.172.16.115.1.2': {},
     'ciscoMgmt.172.16.115.1.3': {},
     'ciscoMgmt.172.16.115.1.4': {},
     'ciscoMgmt.172.16.115.1.5': {},
     'ciscoMgmt.172.16.115.1.6': {},
     'ciscoMgmt.172.16.115.1.7': {},
     'ciscoMgmt.172.16.115.1.8': {},
     'ciscoMgmt.172.16.115.1.9': {},
     'ciscoMgmt.172.16.151.1.1': {},
     'ciscoMgmt.172.16.151.1.2': {},
     'ciscoMgmt.172.16.94.1.1': {},
     'ciscoMgmt.172.16.120.1.1': {},
     'ciscoMgmt.172.16.120.1.2': {},
     'ciscoMgmt.172.16.136.1.1': {},
     'ciscoMgmt.172.16.136.1.2': {},
     'ciscoMgmt.172.16.154.1': {},
     'ciscoMgmt.172.16.154.2': {},
     'ciscoMgmt.172.16.154.3.1.2': {},
     'ciscoMgmt.172.16.154.3.1.3': {},
     'ciscoMgmt.172.16.154.3.1.4': {},
     'ciscoMgmt.172.16.154.3.1.5': {},
     'ciscoMgmt.172.16.154.3.1.6': {},
     'ciscoMgmt.172.16.154.3.1.7': {},
     'ciscoMgmt.172.16.154.3.1.8': {},
     'ciscoMgmt.172.16.204.1': {},
     'ciscoMgmt.172.16.204.2': {},
     'ciscoMgmt.310.169.1.1': {},
     'ciscoMgmt.310.169.1.2': {},
     'ciscoMgmt.310.169.1.3.1.10': {},
     'ciscoMgmt.310.169.1.3.1.11': {},
     'ciscoMgmt.310.169.1.3.1.12': {},
     'ciscoMgmt.310.169.1.3.1.13': {},
     'ciscoMgmt.310.169.1.3.1.14': {},
     'ciscoMgmt.310.169.1.3.1.15': {},
     'ciscoMgmt.310.169.1.3.1.2': {},
     'ciscoMgmt.310.169.1.3.1.3': {},
     'ciscoMgmt.310.169.1.3.1.4': {},
     'ciscoMgmt.310.169.1.3.1.5': {},
     'ciscoMgmt.310.169.1.3.1.6': {},
     'ciscoMgmt.310.169.1.3.1.7': {},
     'ciscoMgmt.310.169.1.3.1.8': {},
     'ciscoMgmt.310.169.1.3.1.9': {},
     'ciscoMgmt.310.169.1.4.1.2': {},
     'ciscoMgmt.310.169.1.4.1.3': {},
     'ciscoMgmt.310.169.1.4.1.4': {},
     'ciscoMgmt.310.169.1.4.1.5': {},
     'ciscoMgmt.310.169.1.4.1.6': {},
     'ciscoMgmt.310.169.1.4.1.7': {},
     'ciscoMgmt.310.169.1.4.1.8': {},
     'ciscoMgmt.310.169.2.1.1.10': {},
     'ciscoMgmt.310.169.2.1.1.11': {},
     'ciscoMgmt.310.169.2.1.1.2': {},
     'ciscoMgmt.310.169.2.1.1.3': {},
     'ciscoMgmt.310.169.2.1.1.4': {},
     'ciscoMgmt.310.169.2.1.1.5': {},
     'ciscoMgmt.310.169.2.1.1.6': {},
     'ciscoMgmt.310.169.2.1.1.7': {},
     'ciscoMgmt.310.169.2.1.1.8': {},
     'ciscoMgmt.310.169.2.1.1.9': {},
     'ciscoMgmt.310.169.2.2.1.3': {},
     'ciscoMgmt.310.169.2.2.1.4': {},
     'ciscoMgmt.310.169.2.2.1.5': {},
     'ciscoMgmt.310.169.2.3.1.3': {},
     'ciscoMgmt.310.169.2.3.1.4': {},
     'ciscoMgmt.310.169.2.3.1.5': {},
     'ciscoMgmt.310.169.2.3.1.6': {},
     'ciscoMgmt.310.169.2.3.1.7': {},
     'ciscoMgmt.310.169.2.3.1.8': {},
     'ciscoMgmt.310.169.3.1.1.1': {},
     'ciscoMgmt.310.169.3.1.1.2': {},
     'ciscoMgmt.310.169.3.1.1.3': {},
     'ciscoMgmt.310.169.3.1.1.4': {},
     'ciscoMgmt.310.169.3.1.1.5': {},
     'ciscoMgmt.310.169.3.1.1.6': {},
     'ciscoMgmt.410.169.1.1': {},
     'ciscoMgmt.410.169.1.2': {},
     'ciscoMgmt.410.169.2.1.1': {},
     'ciscoMgmt.10.76.1.1.1.1': {},
     'ciscoMgmt.10.76.1.1.1.2': {},
     'ciscoMgmt.10.76.1.1.1.3': {},
     'ciscoMgmt.10.76.1.1.1.4': {},
     'ciscoMgmt.610.21.1.1.10': {},
     'ciscoMgmt.610.21.1.1.11': {},
     'ciscoMgmt.610.21.1.1.12': {},
     'ciscoMgmt.610.21.1.1.13': {},
     'ciscoMgmt.610.21.1.1.14': {},
     'ciscoMgmt.610.21.1.1.15': {},
     'ciscoMgmt.610.21.1.1.16': {},
     'ciscoMgmt.610.21.1.1.17': {},
     'ciscoMgmt.610.21.1.1.18': {},
     'ciscoMgmt.610.21.1.1.19': {},
     'ciscoMgmt.610.21.1.1.2': {},
     'ciscoMgmt.610.21.1.1.20': {},
     'ciscoMgmt.610.21.1.1.21': {},
     'ciscoMgmt.610.21.1.1.22': {},
     'ciscoMgmt.610.21.1.1.23': {},
     'ciscoMgmt.610.21.1.1.24': {},
     'ciscoMgmt.610.21.1.1.25': {},
     'ciscoMgmt.610.21.1.1.26': {},
     'ciscoMgmt.610.21.1.1.27': {},
     'ciscoMgmt.610.21.1.1.28': {},
     'ciscoMgmt.610.21.1.1.3': {},
     'ciscoMgmt.610.21.1.1.30': {},
     'ciscoMgmt.610.21.1.1.4': {},
     'ciscoMgmt.610.21.1.1.5': {},
     'ciscoMgmt.610.21.1.1.6': {},
     'ciscoMgmt.610.21.1.1.7': {},
     'ciscoMgmt.610.21.1.1.8': {},
     'ciscoMgmt.610.21.1.1.9': {},
     'ciscoMgmt.610.21.2.1.10': {},
     'ciscoMgmt.610.21.2.1.11': {},
     'ciscoMgmt.610.21.2.1.12': {},
     'ciscoMgmt.610.21.2.1.13': {},
     'ciscoMgmt.610.21.2.1.14': {},
     'ciscoMgmt.610.21.2.1.15': {},
     'ciscoMgmt.610.21.2.1.16': {},
     'ciscoMgmt.610.21.2.1.2': {},
     'ciscoMgmt.610.21.2.1.3': {},
     'ciscoMgmt.610.21.2.1.4': {},
     'ciscoMgmt.610.21.2.1.5': {},
     'ciscoMgmt.610.21.2.1.6': {},
     'ciscoMgmt.610.21.2.1.7': {},
     'ciscoMgmt.610.21.2.1.8': {},
     'ciscoMgmt.610.21.2.1.9': {},
     'ciscoMgmt.610.94.1.1.10': {},
     'ciscoMgmt.610.94.1.1.11': {},
     'ciscoMgmt.610.94.1.1.12': {},
     'ciscoMgmt.610.94.1.1.13': {},
     'ciscoMgmt.610.94.1.1.14': {},
     'ciscoMgmt.610.94.1.1.15': {},
     'ciscoMgmt.610.94.1.1.16': {},
     'ciscoMgmt.610.94.1.1.17': {},
     'ciscoMgmt.610.94.1.1.18': {},
     'ciscoMgmt.610.94.1.1.2': {},
     'ciscoMgmt.610.94.1.1.3': {},
     'ciscoMgmt.610.94.1.1.4': {},
     'ciscoMgmt.610.94.1.1.5': {},
     'ciscoMgmt.610.94.1.1.6': {},
     'ciscoMgmt.610.94.1.1.7': {},
     'ciscoMgmt.610.94.1.1.8': {},
     'ciscoMgmt.610.94.1.1.9': {},
     'ciscoMgmt.610.94.2.1.10': {},
     'ciscoMgmt.610.94.2.1.11': {},
     'ciscoMgmt.610.94.2.1.12': {},
     'ciscoMgmt.610.94.2.1.13': {},
     'ciscoMgmt.610.94.2.1.14': {},
     'ciscoMgmt.610.94.2.1.15': {},
     'ciscoMgmt.610.94.2.1.16': {},
     'ciscoMgmt.610.94.2.1.17': {},
     'ciscoMgmt.610.94.2.1.18': {},
     'ciscoMgmt.610.94.2.1.19': {},
     'ciscoMgmt.610.94.2.1.2': {},
     'ciscoMgmt.610.94.2.1.20': {},
     'ciscoMgmt.610.94.2.1.3': {},
     'ciscoMgmt.610.94.2.1.4': {},
     'ciscoMgmt.610.94.2.1.5': {},
     'ciscoMgmt.610.94.2.1.6': {},
     'ciscoMgmt.610.94.2.1.7': {},
     'ciscoMgmt.610.94.2.1.8': {},
     'ciscoMgmt.610.94.2.1.9': {},
     'ciscoMgmt.610.94.3.1.10': {},
     'ciscoMgmt.610.94.3.1.11': {},
     'ciscoMgmt.610.94.3.1.12': {},
     'ciscoMgmt.610.94.3.1.13': {},
     'ciscoMgmt.610.94.3.1.14': {},
     'ciscoMgmt.610.94.3.1.15': {},
     'ciscoMgmt.610.94.3.1.16': {},
     'ciscoMgmt.610.94.3.1.17': {},
     'ciscoMgmt.610.94.3.1.18': {},
     'ciscoMgmt.610.94.3.1.19': {},
     'ciscoMgmt.610.94.3.1.2': {},
     'ciscoMgmt.610.94.3.1.3': {},
     'ciscoMgmt.610.94.3.1.4': {},
     'ciscoMgmt.610.94.3.1.5': {},
     'ciscoMgmt.610.94.3.1.6': {},
     'ciscoMgmt.610.94.3.1.7': {},
     'ciscoMgmt.610.94.3.1.8': {},
     'ciscoMgmt.610.94.3.1.9': {},
     'ciscoMgmt.10.84.1.1.1.5': {},
     'ciscoMgmt.10.84.1.1.1.6': {},
     'ciscoMgmt.10.84.1.1.1.7': {},
     'ciscoMgmt.10.84.1.2.1.4': {},
     'ciscoMgmt.10.84.1.2.1.5': {},
     'ciscoMgmt.10.84.1.3.1.2': {},
     'ciscoMgmt.10.84.2.1.1.10': {},
     'ciscoMgmt.10.84.2.1.1.11': {},
     'ciscoMgmt.10.84.2.1.1.12': {},
     'ciscoMgmt.10.84.2.1.1.13': {},
     'ciscoMgmt.10.84.2.1.1.14': {},
     'ciscoMgmt.10.84.2.1.1.15': {},
     'ciscoMgmt.10.84.2.1.1.16': {},
     'ciscoMgmt.10.84.2.1.1.17': {},
     'ciscoMgmt.10.84.2.1.1.7': {},
     'ciscoMgmt.10.84.2.1.1.8': {},
     'ciscoMgmt.10.84.2.1.1.9': {},
     'ciscoMgmt.10.64.1.1.1.2': {},
     'ciscoMgmt.10.64.1.1.1.3': {},
     'ciscoMgmt.10.64.1.1.1.4': {},
     'ciscoMgmt.10.64.1.1.1.5': {},
     'ciscoMgmt.10.64.1.1.1.6': {},
     'ciscoMgmt.10.64.2.1.1.4': {},
     'ciscoMgmt.10.64.2.1.1.5': {},
     'ciscoMgmt.10.64.2.1.1.6': {},
     'ciscoMgmt.10.64.2.1.1.7': {},
     'ciscoMgmt.10.64.2.1.1.8': {},
     'ciscoMgmt.10.64.2.1.1.9': {},
     'ciscoMgmt.10.64.3.1.1.1': {},
     'ciscoMgmt.10.64.3.1.1.2': {},
     'ciscoMgmt.10.64.3.1.1.3': {},
     'ciscoMgmt.10.64.3.1.1.4': {},
     'ciscoMgmt.10.64.3.1.1.5': {},
     'ciscoMgmt.10.64.3.1.1.6': {},
     'ciscoMgmt.10.64.3.1.1.7': {},
     'ciscoMgmt.10.64.3.1.1.8': {},
     'ciscoMgmt.10.64.3.1.1.9': {},
     'ciscoMgmt.10.64.4.1.1.1': {},
     'ciscoMgmt.10.64.4.1.1.10': {},
     'ciscoMgmt.10.64.4.1.1.2': {},
     'ciscoMgmt.10.64.4.1.1.3': {},
     'ciscoMgmt.10.64.4.1.1.4': {},
     'ciscoMgmt.10.64.4.1.1.5': {},
     'ciscoMgmt.10.64.4.1.1.6': {},
     'ciscoMgmt.10.64.4.1.1.7': {},
     'ciscoMgmt.10.64.4.1.1.8': {},
     'ciscoMgmt.10.64.4.1.1.9': {},
     'ciscoMgmt.710.196.1.1.1.1': {},
     'ciscoMgmt.710.196.1.1.1.10': {},
     'ciscoMgmt.710.196.1.1.1.11': {},
     'ciscoMgmt.710.196.1.1.1.12': {},
     'ciscoMgmt.710.196.1.1.1.2': {},
     'ciscoMgmt.710.196.1.1.1.3': {},
     'ciscoMgmt.710.196.1.1.1.4': {},
     'ciscoMgmt.710.196.1.1.1.5': {},
     'ciscoMgmt.710.196.1.1.1.6': {},
     'ciscoMgmt.710.196.1.1.1.7': {},
     'ciscoMgmt.710.196.1.1.1.8': {},
     'ciscoMgmt.710.196.1.1.1.9': {},
     'ciscoMgmt.710.196.1.2': {},
     'ciscoMgmt.710.196.1.3.1.1': {},
     'ciscoMgmt.710.196.1.3.1.10': {},
     'ciscoMgmt.710.196.1.3.1.11': {},
     'ciscoMgmt.710.196.1.3.1.12': {},
     'ciscoMgmt.710.196.1.3.1.2': {},
     'ciscoMgmt.710.196.1.3.1.3': {},
     'ciscoMgmt.710.196.1.3.1.4': {},
     'ciscoMgmt.710.196.1.3.1.5': {},
     'ciscoMgmt.710.196.1.3.1.6': {},
     'ciscoMgmt.710.196.1.3.1.7': {},
     'ciscoMgmt.710.196.1.3.1.8': {},
     'ciscoMgmt.710.196.1.3.1.9': {},
     'ciscoMgmt.710.84.1.1.1.1': {},
     'ciscoMgmt.710.84.1.1.1.10': {},
     'ciscoMgmt.710.84.1.1.1.11': {},
     'ciscoMgmt.710.84.1.1.1.12': {},
     'ciscoMgmt.710.84.1.1.1.2': {},
     'ciscoMgmt.710.84.1.1.1.3': {},
     'ciscoMgmt.710.84.1.1.1.4': {},
     'ciscoMgmt.710.84.1.1.1.5': {},
     'ciscoMgmt.710.84.1.1.1.6': {},
     'ciscoMgmt.710.84.1.1.1.7': {},
     'ciscoMgmt.710.84.1.1.1.8': {},
     'ciscoMgmt.710.84.1.1.1.9': {},
     'ciscoMgmt.710.84.1.2': {},
     'ciscoMgmt.710.84.1.3.1.1': {},
     'ciscoMgmt.710.84.1.3.1.10': {},
     'ciscoMgmt.710.84.1.3.1.11': {},
     'ciscoMgmt.710.84.1.3.1.12': {},
     'ciscoMgmt.710.84.1.3.1.2': {},
     'ciscoMgmt.710.84.1.3.1.3': {},
     'ciscoMgmt.710.84.1.3.1.4': {},
     'ciscoMgmt.710.84.1.3.1.5': {},
     'ciscoMgmt.710.84.1.3.1.6': {},
     'ciscoMgmt.710.84.1.3.1.7': {},
     'ciscoMgmt.710.84.1.3.1.8': {},
     'ciscoMgmt.710.84.1.3.1.9': {},
     'ciscoMgmt.10.16.1.1.1': {},
     'ciscoMgmt.10.16.1.1.2': {},
     'ciscoMgmt.10.16.1.1.3': {},
     'ciscoMgmt.10.16.1.1.4': {},
     'ciscoMgmt.10.195.1.1.1': {},
     'ciscoMgmt.10.195.1.1.10': {},
     'ciscoMgmt.10.195.1.1.11': {},
     'ciscoMgmt.10.195.1.1.12': {},
     'ciscoMgmt.10.195.1.1.13': {},
     'ciscoMgmt.10.195.1.1.14': {},
     'ciscoMgmt.10.195.1.1.15': {},
     'ciscoMgmt.10.195.1.1.16': {},
     'ciscoMgmt.10.195.1.1.17': {},
     'ciscoMgmt.10.195.1.1.18': {},
     'ciscoMgmt.10.195.1.1.19': {},
     'ciscoMgmt.10.195.1.1.2': {},
     'ciscoMgmt.10.195.1.1.20': {},
     'ciscoMgmt.10.195.1.1.21': {},
     'ciscoMgmt.10.195.1.1.22': {},
     'ciscoMgmt.10.195.1.1.23': {},
     'ciscoMgmt.10.195.1.1.24': {},
     'ciscoMgmt.10.195.1.1.3': {},
     'ciscoMgmt.10.195.1.1.4': {},
     'ciscoMgmt.10.195.1.1.5': {},
     'ciscoMgmt.10.195.1.1.6': {},
     'ciscoMgmt.10.195.1.1.7': {},
     'ciscoMgmt.10.195.1.1.8': {},
     'ciscoMgmt.10.195.1.1.9': {},
     'ciscoMvpnConfig.1.1.1': {},
     'ciscoMvpnConfig.1.1.2': {},
     'ciscoMvpnConfig.1.1.3': {},
     'ciscoMvpnConfig.1.1.4': {},
     'ciscoMvpnConfig.2.1.1': {},
     'ciscoMvpnConfig.2.1.2': {},
     'ciscoMvpnConfig.2.1.3': {},
     'ciscoMvpnConfig.2.1.4': {},
     'ciscoMvpnConfig.2.1.5': {},
     'ciscoMvpnConfig.2.1.6': {},
     'ciscoMvpnGeneric.1.1.1': {},
     'ciscoMvpnGeneric.1.1.2': {},
     'ciscoMvpnGeneric.1.1.3': {},
     'ciscoMvpnGeneric.1.1.4': {},
     'ciscoMvpnProtocol.1.1.6': {},
     'ciscoMvpnProtocol.1.1.7': {},
     'ciscoMvpnProtocol.1.1.8': {},
     'ciscoMvpnProtocol.2.1.3': {},
     'ciscoMvpnProtocol.2.1.6': {},
     'ciscoMvpnProtocol.2.1.7': {},
     'ciscoMvpnProtocol.2.1.8': {},
     'ciscoMvpnProtocol.2.1.9': {},
     'ciscoMvpnProtocol.3.1.5': {},
     'ciscoMvpnProtocol.3.1.6': {},
     'ciscoMvpnProtocol.4.1.5': {},
     'ciscoMvpnProtocol.4.1.6': {},
     'ciscoMvpnProtocol.4.1.7': {},
     'ciscoMvpnProtocol.5.1.1': {},
     'ciscoMvpnProtocol.5.1.2': {},
     'ciscoMvpnScalars': {'1': {}, '2': {}},
     'ciscoNetflowMIB.1.7.1': {},
     'ciscoNetflowMIB.1.7.10': {},
     'ciscoNetflowMIB.1.7.11': {},
     'ciscoNetflowMIB.1.7.12': {},
     'ciscoNetflowMIB.1.7.13': {},
     'ciscoNetflowMIB.1.7.14': {},
     'ciscoNetflowMIB.1.7.15': {},
     'ciscoNetflowMIB.1.7.16': {},
     'ciscoNetflowMIB.1.7.17': {},
     'ciscoNetflowMIB.1.7.18': {},
     'ciscoNetflowMIB.1.7.19': {},
     'ciscoNetflowMIB.1.7.2': {},
     'ciscoNetflowMIB.1.7.20': {},
     'ciscoNetflowMIB.1.7.21': {},
     'ciscoNetflowMIB.1.7.22': {},
     'ciscoNetflowMIB.1.7.23': {},
     'ciscoNetflowMIB.1.7.24': {},
     'ciscoNetflowMIB.1.7.25': {},
     'ciscoNetflowMIB.1.7.26': {},
     'ciscoNetflowMIB.1.7.27': {},
     'ciscoNetflowMIB.1.7.28': {},
     'ciscoNetflowMIB.1.7.29': {},
     'ciscoNetflowMIB.1.7.3': {},
     'ciscoNetflowMIB.1.7.30': {},
     'ciscoNetflowMIB.1.7.31': {},
     'ciscoNetflowMIB.1.7.32': {},
     'ciscoNetflowMIB.1.7.33': {},
     'ciscoNetflowMIB.1.7.34': {},
     'ciscoNetflowMIB.1.7.35': {},
     'ciscoNetflowMIB.1.7.36': {},
     'ciscoNetflowMIB.1.7.37': {},
     'ciscoNetflowMIB.1.7.38': {},
     'ciscoNetflowMIB.1.7.4': {},
     'ciscoNetflowMIB.1.7.5': {},
     'ciscoNetflowMIB.1.7.6': {},
     'ciscoNetflowMIB.1.7.7': {},
     'ciscoNetflowMIB.10.64.8.1.10': {},
     'ciscoNetflowMIB.10.64.8.1.11': {},
     'ciscoNetflowMIB.10.64.8.1.12': {},
     'ciscoNetflowMIB.10.64.8.1.13': {},
     'ciscoNetflowMIB.10.64.8.1.14': {},
     'ciscoNetflowMIB.10.64.8.1.15': {},
     'ciscoNetflowMIB.10.64.8.1.16': {},
     'ciscoNetflowMIB.10.64.8.1.17': {},
     'ciscoNetflowMIB.10.64.8.1.18': {},
     'ciscoNetflowMIB.10.64.8.1.19': {},
     'ciscoNetflowMIB.10.64.8.1.2': {},
     'ciscoNetflowMIB.10.64.8.1.20': {},
     'ciscoNetflowMIB.10.64.8.1.21': {},
     'ciscoNetflowMIB.10.64.8.1.22': {},
     'ciscoNetflowMIB.10.64.8.1.23': {},
     'ciscoNetflowMIB.10.64.8.1.24': {},
     'ciscoNetflowMIB.10.64.8.1.25': {},
     'ciscoNetflowMIB.10.64.8.1.26': {},
     'ciscoNetflowMIB.10.64.8.1.3': {},
     'ciscoNetflowMIB.10.64.8.1.4': {},
     'ciscoNetflowMIB.10.64.8.1.5': {},
     'ciscoNetflowMIB.10.64.8.1.6': {},
     'ciscoNetflowMIB.10.64.8.1.7': {},
     'ciscoNetflowMIB.10.64.8.1.8': {},
     'ciscoNetflowMIB.10.64.8.1.9': {},
     'ciscoNetflowMIB.1.7.9': {},
     'ciscoPimMIBNotificationObjects': {'1': {}},
     'ciscoPingEntry': {'10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '14': {},
                        '15': {},
                        '16': {},
                        '17': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'ciscoPppoeMIBObjects.10.9.1.1': {},
     'ciscoProcessMIB.10.9.3.1.1': {},
     'ciscoProcessMIB.10.9.3.1.10': {},
     'ciscoProcessMIB.10.9.3.1.11': {},
     'ciscoProcessMIB.10.9.3.1.12': {},
     'ciscoProcessMIB.10.9.3.1.13': {},
     'ciscoProcessMIB.10.9.3.1.14': {},
     'ciscoProcessMIB.10.9.3.1.15': {},
     'ciscoProcessMIB.10.9.3.1.16': {},
     'ciscoProcessMIB.10.9.3.1.17': {},
     'ciscoProcessMIB.10.9.3.1.18': {},
     'ciscoProcessMIB.10.9.3.1.19': {},
     'ciscoProcessMIB.10.9.3.1.2': {},
     'ciscoProcessMIB.10.9.3.1.20': {},
     'ciscoProcessMIB.10.9.3.1.21': {},
     'ciscoProcessMIB.10.9.3.1.22': {},
     'ciscoProcessMIB.10.9.3.1.23': {},
     'ciscoProcessMIB.10.9.3.1.24': {},
     'ciscoProcessMIB.10.9.3.1.25': {},
     'ciscoProcessMIB.10.9.3.1.26': {},
     'ciscoProcessMIB.10.9.3.1.27': {},
     'ciscoProcessMIB.10.9.3.1.28': {},
     'ciscoProcessMIB.10.9.3.1.29': {},
     'ciscoProcessMIB.10.9.3.1.3': {},
     'ciscoProcessMIB.10.9.3.1.30': {},
     'ciscoProcessMIB.10.9.3.1.4': {},
     'ciscoProcessMIB.10.9.3.1.5': {},
     'ciscoProcessMIB.10.9.3.1.6': {},
     'ciscoProcessMIB.10.9.3.1.7': {},
     'ciscoProcessMIB.10.9.3.1.8': {},
     'ciscoProcessMIB.10.9.3.1.9': {},
     'ciscoProcessMIB.10.9.5.1': {},
     'ciscoProcessMIB.10.9.5.2': {},
     'ciscoSessBorderCtrlrMIBObjects': {'73': {},
                                        '74': {},
                                        '75': {},
                                        '76': {},
                                        '77': {},
                                        '78': {},
                                        '79': {}},
     'ciscoSipUaMIB.10.4.7.1': {},
     'ciscoSipUaMIB.10.4.7.2': {},
     'ciscoSipUaMIB.10.4.7.3': {},
     'ciscoSipUaMIB.10.4.7.4': {},
     'ciscoSipUaMIB.10.9.10.1': {},
     'ciscoSipUaMIB.10.9.10.10': {},
     'ciscoSipUaMIB.10.9.10.11': {},
     'ciscoSipUaMIB.10.9.10.12': {},
     'ciscoSipUaMIB.10.9.10.13': {},
     'ciscoSipUaMIB.10.9.10.14': {},
     'ciscoSipUaMIB.10.9.10.2': {},
     'ciscoSipUaMIB.10.9.10.3': {},
     'ciscoSipUaMIB.10.9.10.4': {},
     'ciscoSipUaMIB.10.9.10.5': {},
     'ciscoSipUaMIB.10.9.10.6': {},
     'ciscoSipUaMIB.10.9.10.7': {},
     'ciscoSipUaMIB.10.9.10.8': {},
     'ciscoSipUaMIB.10.9.10.9': {},
     'ciscoSipUaMIB.10.9.9.1': {},
     'ciscoSnapshotActivityEntry': {'2': {},
                                    '3': {},
                                    '4': {},
                                    '5': {},
                                    '6': {},
                                    '7': {},
                                    '8': {}},
     'ciscoSnapshotInterfaceEntry': {'2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {}},
     'ciscoSnapshotMIB.1.1': {},
     'ciscoSyslogMIB.1.2.1': {},
     'ciscoSyslogMIB.1.2.2': {},
     'ciscoTcpConnEntry': {'1': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'ciscoVpdnMgmtMIB.0.1': {},
     'ciscoVpdnMgmtMIB.0.2': {},
     'ciscoVpdnMgmtMIBObjects.10.36.1.2': {},
     'ciscoVpdnMgmtMIBObjects.6.1': {},
     'ciscoVpdnMgmtMIBObjects.6.2': {},
     'ciscoVpdnMgmtMIBObjects.6.3': {},
     'ciscoVpdnMgmtMIBObjects.10.100.1.2': {},
     'ciscoVpdnMgmtMIBObjects.10.100.1.3': {},
     'ciscoVpdnMgmtMIBObjects.10.100.1.4': {},
     'ciscoVpdnMgmtMIBObjects.10.100.1.5': {},
     'ciscoVpdnMgmtMIBObjects.10.100.1.6': {},
     'ciscoVpdnMgmtMIBObjects.10.100.1.7': {},
     'ciscoVpdnMgmtMIBObjects.6.5': {},
     'ciscoVpdnMgmtMIBObjects.10.144.1.3': {},
     'ciscoVpdnMgmtMIBObjects.7.1': {},
     'ciscoVpdnMgmtMIBObjects.7.2': {},
     'clagAggDistributionAddressMode': {},
     'clagAggDistributionProtocol': {},
     'clagAggPortAdminStatus': {},
     'clagAggProtocolType': {},
     'clispExtEidRegMoreSpecificCount': {},
     'clispExtEidRegMoreSpecificLimit': {},
     'clispExtEidRegMoreSpecificWarningThreshold': {},
     'clispExtEidRegRlocMembershipConfigured': {},
     'clispExtEidRegRlocMembershipGleaned': {},
     'clispExtEidRegRlocMembershipMemberSince': {},
     'clispExtFeaturesEidRegMoreSpecificLimit': {},
     'clispExtFeaturesEidRegMoreSpecificWarningThreshold': {},
     'clispExtFeaturesMapCacheWarningThreshold': {},
     'clispExtGlobalStatsEidRegMoreSpecificEntryCount': {},
     'clispExtReliableTransportSessionBytesIn': {},
     'clispExtReliableTransportSessionBytesOut': {},
     'clispExtReliableTransportSessionEstablishmentRole': {},
     'clispExtReliableTransportSessionLastStateChangeTime': {},
     'clispExtReliableTransportSessionMessagesIn': {},
     'clispExtReliableTransportSessionMessagesOut': {},
     'clispExtReliableTransportSessionState': {},
     'clispExtRlocMembershipConfigured': {},
     'clispExtRlocMembershipDiscovered': {},
     'clispExtRlocMembershipMemberSince': {},
     'clogBasic': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'clogHistoryEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'cmiFaAdvertChallengeChapSPI': {},
     'cmiFaAdvertChallengeValue': {},
     'cmiFaAdvertChallengeWindow': {},
     'cmiFaAdvertIsBusy': {},
     'cmiFaAdvertRegRequired': {},
     'cmiFaChallengeEnable': {},
     'cmiFaChallengeSupported': {},
     'cmiFaCoaInterfaceOnly': {},
     'cmiFaCoaRegAsymLink': {},
     'cmiFaCoaTransmitOnly': {},
     'cmiFaCvsesFromHaRejected': {},
     'cmiFaCvsesFromMnRejected': {},
     'cmiFaDeRegRepliesValidFromHA': {},
     'cmiFaDeRegRepliesValidRelayToMN': {},
     'cmiFaDeRegRequestsDenied': {},
     'cmiFaDeRegRequestsDiscarded': {},
     'cmiFaDeRegRequestsReceived': {},
     'cmiFaDeRegRequestsRelayed': {},
     'cmiFaDeliveryStyleUnsupported': {},
     'cmiFaEncapDeliveryStyleSupported': {},
     'cmiFaInitRegRepliesValidFromHA': {},
     'cmiFaInitRegRepliesValidRelayMN': {},
     'cmiFaInitRegRequestsDenied': {},
     'cmiFaInitRegRequestsDiscarded': {},
     'cmiFaInitRegRequestsReceived': {},
     'cmiFaInitRegRequestsRelayed': {},
     'cmiFaMissingChallenge': {},
     'cmiFaMnAAAAuthFailures': {},
     'cmiFaMnFaAuthFailures': {},
     'cmiFaMnTooDistant': {},
     'cmiFaNvsesFromHaNeglected': {},
     'cmiFaNvsesFromMnNeglected': {},
     'cmiFaReRegRepliesValidFromHA': {},
     'cmiFaReRegRepliesValidRelayToMN': {},
     'cmiFaReRegRequestsDenied': {},
     'cmiFaReRegRequestsDiscarded': {},
     'cmiFaReRegRequestsReceived': {},
     'cmiFaReRegRequestsRelayed': {},
     'cmiFaRegTotalVisitors': {},
     'cmiFaRegVisitorChallengeValue': {},
     'cmiFaRegVisitorHomeAddress': {},
     'cmiFaRegVisitorHomeAgentAddress': {},
     'cmiFaRegVisitorRegFlags': {},
     'cmiFaRegVisitorRegFlagsRev1': {},
     'cmiFaRegVisitorRegIDHigh': {},
     'cmiFaRegVisitorRegIDLow': {},
     'cmiFaRegVisitorRegIsAccepted': {},
     'cmiFaRegVisitorTimeGranted': {},
     'cmiFaRegVisitorTimeRemaining': {},
     'cmiFaRevTunnelSupported': {},
     'cmiFaReverseTunnelBitNotSet': {},
     'cmiFaReverseTunnelEnable': {},
     'cmiFaReverseTunnelUnavailable': {},
     'cmiFaStaleChallenge': {},
     'cmiFaTotalRegReplies': {},
     'cmiFaTotalRegRequests': {},
     'cmiFaUnknownChallenge': {},
     'cmiHaCvsesFromFaRejected': {},
     'cmiHaCvsesFromMnRejected': {},
     'cmiHaDeRegRequestsAccepted': {},
     'cmiHaDeRegRequestsDenied': {},
     'cmiHaDeRegRequestsDiscarded': {},
     'cmiHaDeRegRequestsReceived': {},
     'cmiHaEncapUnavailable': {},
     'cmiHaEncapsulationUnavailable': {},
     'cmiHaInitRegRequestsAccepted': {},
     'cmiHaInitRegRequestsDenied': {},
     'cmiHaInitRegRequestsDiscarded': {},
     'cmiHaInitRegRequestsReceived': {},
     'cmiHaMnAAAAuthFailures': {},
     'cmiHaMnHaAuthFailures': {},
     'cmiHaMobNetDynamic': {},
     'cmiHaMobNetStatus': {},
     'cmiHaMrDynamic': {},
     'cmiHaMrMultiPath': {},
     'cmiHaMrMultiPathMetricType': {},
     'cmiHaMrStatus': {},
     'cmiHaNAICheckFailures': {},
     'cmiHaNvsesFromFaNeglected': {},
     'cmiHaNvsesFromMnNeglected': {},
     'cmiHaReRegRequestsAccepted': {},
     'cmiHaReRegRequestsDenied': {},
     'cmiHaReRegRequestsDiscarded': {},
     'cmiHaReRegRequestsReceived': {},
     'cmiHaRedunDroppedBIAcks': {},
     'cmiHaRedunDroppedBIReps': {},
     'cmiHaRedunFailedBIReps': {},
     'cmiHaRedunFailedBIReqs': {},
     'cmiHaRedunFailedBUs': {},
     'cmiHaRedunReceivedBIAcks': {},
     'cmiHaRedunReceivedBIReps': {},
     'cmiHaRedunReceivedBIReqs': {},
     'cmiHaRedunReceivedBUAcks': {},
     'cmiHaRedunReceivedBUs': {},
     'cmiHaRedunSecViolations': {},
     'cmiHaRedunSentBIAcks': {},
     'cmiHaRedunSentBIReps': {},
     'cmiHaRedunSentBIReqs': {},
     'cmiHaRedunSentBUAcks': {},
     'cmiHaRedunSentBUs': {},
     'cmiHaRedunTotalSentBIReps': {},
     'cmiHaRedunTotalSentBIReqs': {},
     'cmiHaRedunTotalSentBUs': {},
     'cmiHaRegAvgTimeRegsProcByAAA': {},
     'cmiHaRegDateMaxRegsProcByAAA': {},
     'cmiHaRegDateMaxRegsProcLoc': {},
     'cmiHaRegMaxProcByAAAInMinRegs': {},
     'cmiHaRegMaxProcLocInMinRegs': {},
     'cmiHaRegMaxTimeRegsProcByAAA': {},
     'cmiHaRegMnIdentifier': {},
     'cmiHaRegMnIdentifierType': {},
     'cmiHaRegMnIfBandwidth': {},
     'cmiHaRegMnIfDescription': {},
     'cmiHaRegMnIfID': {},
     'cmiHaRegMnIfPathMetricType': {},
     'cmiHaRegMobilityBindingRegFlags': {},
     'cmiHaRegOverallServTime': {},
     'cmiHaRegProcAAAInLastByMinRegs': {},
     'cmiHaRegProcLocInLastMinRegs': {},
     'cmiHaRegRecentServAcceptedTime': {},
     'cmiHaRegRecentServDeniedCode': {},
     'cmiHaRegRecentServDeniedTime': {},
     'cmiHaRegRequestsDenied': {},
     'cmiHaRegRequestsDiscarded': {},
     'cmiHaRegRequestsReceived': {},
     'cmiHaRegServAcceptedRequests': {},
     'cmiHaRegServDeniedRequests': {},
     'cmiHaRegTotalMobilityBindings': {},
     'cmiHaRegTotalProcByAAARegs': {},
     'cmiHaRegTotalProcLocRegs': {},
     'cmiHaReverseTunnelBitNotSet': {},
     'cmiHaReverseTunnelUnavailable': {},
     'cmiHaSystemVersion': {},
     'cmiMRIfDescription': {},
     'cmiMaAdvAddress': {},
     'cmiMaAdvAddressType': {},
     'cmiMaAdvMaxAdvLifetime': {},
     'cmiMaAdvMaxInterval': {},
     'cmiMaAdvMaxRegLifetime': {},
     'cmiMaAdvMinInterval': {},
     'cmiMaAdvPrefixLengthInclusion': {},
     'cmiMaAdvResponseSolicitationOnly': {},
     'cmiMaAdvStatus': {},
     'cmiMaInterfaceAddress': {},
     'cmiMaInterfaceAddressType': {},
     'cmiMaRegDateMaxRegsReceived': {},
     'cmiMaRegInLastMinuteRegs': {},
     'cmiMaRegMaxInMinuteRegs': {},
     'cmiMnAdvFlags': {},
     'cmiMnRegFlags': {},
     'cmiMrBetterIfDetected': {},
     'cmiMrCollocatedTunnel': {},
     'cmiMrHABest': {},
     'cmiMrHAPriority': {},
     'cmiMrHaTunnelIfIndex': {},
     'cmiMrIfCCoaAddress': {},
     'cmiMrIfCCoaAddressType': {},
     'cmiMrIfCCoaDefaultGw': {},
     'cmiMrIfCCoaDefaultGwType': {},
     'cmiMrIfCCoaEnable': {},
     'cmiMrIfCCoaOnly': {},
     'cmiMrIfCCoaRegRetry': {},
     'cmiMrIfCCoaRegRetryRemaining': {},
     'cmiMrIfCCoaRegistration': {},
     'cmiMrIfHaTunnelIfIndex': {},
     'cmiMrIfHoldDown': {},
     'cmiMrIfID': {},
     'cmiMrIfRegisteredCoA': {},
     'cmiMrIfRegisteredCoAType': {},
     'cmiMrIfRegisteredMaAddr': {},
     'cmiMrIfRegisteredMaAddrType': {},
     'cmiMrIfRoamPriority': {},
     'cmiMrIfRoamStatus': {},
     'cmiMrIfSolicitInterval': {},
     'cmiMrIfSolicitPeriodic': {},
     'cmiMrIfSolicitRetransCount': {},
     'cmiMrIfSolicitRetransCurrent': {},
     'cmiMrIfSolicitRetransInitial': {},
     'cmiMrIfSolicitRetransLimit': {},
     'cmiMrIfSolicitRetransMax': {},
     'cmiMrIfSolicitRetransRemaining': {},
     'cmiMrIfStatus': {},
     'cmiMrMaAdvFlags': {},
     'cmiMrMaAdvLifetimeRemaining': {},
     'cmiMrMaAdvMaxLifetime': {},
     'cmiMrMaAdvMaxRegLifetime': {},
     'cmiMrMaAdvRcvIf': {},
     'cmiMrMaAdvSequence': {},
     'cmiMrMaAdvTimeFirstHeard': {},
     'cmiMrMaAdvTimeReceived': {},
     'cmiMrMaHoldDownRemaining': {},
     'cmiMrMaIfMacAddress': {},
     'cmiMrMaIsHa': {},
     'cmiMrMobNetAddr': {},
     'cmiMrMobNetAddrType': {},
     'cmiMrMobNetPfxLen': {},
     'cmiMrMobNetStatus': {},
     'cmiMrMultiPath': {},
     'cmiMrMultiPathMetricType': {},
     'cmiMrRedStateActive': {},
     'cmiMrRedStatePassive': {},
     'cmiMrRedundancyGroup': {},
     'cmiMrRegExtendExpire': {},
     'cmiMrRegExtendInterval': {},
     'cmiMrRegExtendRetry': {},
     'cmiMrRegLifetime': {},
     'cmiMrRegNewHa': {},
     'cmiMrRegRetransInitial': {},
     'cmiMrRegRetransLimit': {},
     'cmiMrRegRetransMax': {},
     'cmiMrReverseTunnel': {},
     'cmiMrTunnelBytesRcvd': {},
     'cmiMrTunnelBytesSent': {},
     'cmiMrTunnelPktsRcvd': {},
     'cmiMrTunnelPktsSent': {},
     'cmiNtRegCOA': {},
     'cmiNtRegCOAType': {},
     'cmiNtRegDeniedCode': {},
     'cmiNtRegHAAddrType': {},
     'cmiNtRegHomeAddress': {},
     'cmiNtRegHomeAddressType': {},
     'cmiNtRegHomeAgent': {},
     'cmiNtRegNAI': {},
     'cmiSecAlgorithmMode': {},
     'cmiSecAlgorithmType': {},
     'cmiSecAssocsCount': {},
     'cmiSecKey': {},
     'cmiSecKey2': {},
     'cmiSecRecentViolationIDHigh': {},
     'cmiSecRecentViolationIDLow': {},
     'cmiSecRecentViolationReason': {},
     'cmiSecRecentViolationSPI': {},
     'cmiSecRecentViolationTime': {},
     'cmiSecReplayMethod': {},
     'cmiSecStatus': {},
     'cmiSecTotalViolations': {},
     'cmiTrapControl': {},
     'cmplsFrrConstEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'cmplsFrrFacRouteDBEntry': {'7': {}, '8': {}, '9': {}},
     'cmplsFrrMIB.1.1': {},
     'cmplsFrrMIB.1.10': {},
     'cmplsFrrMIB.1.11': {},
     'cmplsFrrMIB.1.12': {},
     'cmplsFrrMIB.1.13': {},
     'cmplsFrrMIB.1.14': {},
     'cmplsFrrMIB.1.2': {},
     'cmplsFrrMIB.1.3': {},
     'cmplsFrrMIB.1.4': {},
     'cmplsFrrMIB.1.5': {},
     'cmplsFrrMIB.1.6': {},
     'cmplsFrrMIB.1.7': {},
     'cmplsFrrMIB.1.8': {},
     'cmplsFrrMIB.1.9': {},
     'cmplsFrrMIB.10.9.2.1.2': {},
     'cmplsFrrMIB.10.9.2.1.3': {},
     'cmplsFrrMIB.10.9.2.1.4': {},
     'cmplsFrrMIB.10.9.2.1.5': {},
     'cmplsFrrMIB.10.9.2.1.6': {},
     'cmplsNodeConfigGlobalId': {},
     'cmplsNodeConfigIccId': {},
     'cmplsNodeConfigNodeId': {},
     'cmplsNodeConfigRowStatus': {},
     'cmplsNodeConfigStorageType': {},
     'cmplsNodeIccMapLocalId': {},
     'cmplsNodeIpMapLocalId': {},
     'cmplsTunnelExtDestTnlIndex': {},
     'cmplsTunnelExtDestTnlLspIndex': {},
     'cmplsTunnelExtDestTnlValid': {},
     'cmplsTunnelExtOppositeDirTnlValid': {},
     'cmplsTunnelOppositeDirPtr': {},
     'cmplsTunnelReversePerfBytes': {},
     'cmplsTunnelReversePerfErrors': {},
     'cmplsTunnelReversePerfHCBytes': {},
     'cmplsTunnelReversePerfHCPackets': {},
     'cmplsTunnelReversePerfPackets': {},
     'cmplsXCExtTunnelPointer': {},
     'cmplsXCOppositeDirXCPtr': {},
     'cmqCommonCallActiveASPCallReferenceId': {},
     'cmqCommonCallActiveASPCallType': {},
     'cmqCommonCallActiveASPConnectionId': {},
     'cmqCommonCallActiveASPDirEar': {},
     'cmqCommonCallActiveASPDirMic': {},
     'cmqCommonCallActiveASPEnabledEar': {},
     'cmqCommonCallActiveASPEnabledMic': {},
     'cmqCommonCallActiveASPMode': {},
     'cmqCommonCallActiveASPVer': {},
     'cmqCommonCallActiveDurSigASPTriggEar': {},
     'cmqCommonCallActiveDurSigASPTriggMic': {},
     'cmqCommonCallActiveLongestDurEpiEar': {},
     'cmqCommonCallActiveLongestDurEpiMic': {},
     'cmqCommonCallActiveLoudestFreqEstForLongEpiEar': {},
     'cmqCommonCallActiveLoudestFreqEstForLongEpiMic': {},
     'cmqCommonCallActiveNRCallReferenceId': {},
     'cmqCommonCallActiveNRCallType': {},
     'cmqCommonCallActiveNRConnectionId': {},
     'cmqCommonCallActiveNRDirEar': {},
     'cmqCommonCallActiveNRDirMic': {},
     'cmqCommonCallActiveNREnabledEar': {},
     'cmqCommonCallActiveNREnabledMic': {},
     'cmqCommonCallActiveNRIntensity': {},
     'cmqCommonCallActiveNRLibVer': {},
     'cmqCommonCallActiveNumSigASPTriggEar': {},
     'cmqCommonCallActiveNumSigASPTriggMic': {},
     'cmqCommonCallActivePostNRNoiseFloorEstEar': {},
     'cmqCommonCallActivePostNRNoiseFloorEstMic': {},
     'cmqCommonCallActivePreNRNoiseFloorEstEar': {},
     'cmqCommonCallActivePreNRNoiseFloorEstMic': {},
     'cmqCommonCallActiveTotASPDurEar': {},
     'cmqCommonCallActiveTotASPDurMic': {},
     'cmqCommonCallActiveTotNumASPTriggEar': {},
     'cmqCommonCallActiveTotNumASPTriggMic': {},
     'cmqCommonCallHistoryASPCallReferenceId': {},
     'cmqCommonCallHistoryASPCallType': {},
     'cmqCommonCallHistoryASPConnectionId': {},
     'cmqCommonCallHistoryASPDirEar': {},
     'cmqCommonCallHistoryASPDirMic': {},
     'cmqCommonCallHistoryASPEnabledEar': {},
     'cmqCommonCallHistoryASPEnabledMic': {},
     'cmqCommonCallHistoryASPMode': {},
     'cmqCommonCallHistoryASPVer': {},
     'cmqCommonCallHistoryDurSigASPTriggEar': {},
     'cmqCommonCallHistoryDurSigASPTriggMic': {},
     'cmqCommonCallHistoryLongestDurEpiEar': {},
     'cmqCommonCallHistoryLongestDurEpiMic': {},
     'cmqCommonCallHistoryLoudestFreqEstForLongEpiEar': {},
     'cmqCommonCallHistoryLoudestFreqEstForLongEpiMic': {},
     'cmqCommonCallHistoryNRCallReferenceId': {},
     'cmqCommonCallHistoryNRCallType': {},
     'cmqCommonCallHistoryNRConnectionId': {},
     'cmqCommonCallHistoryNRDirEar': {},
     'cmqCommonCallHistoryNRDirMic': {},
     'cmqCommonCallHistoryNREnabledEar': {},
     'cmqCommonCallHistoryNREnabledMic': {},
     'cmqCommonCallHistoryNRIntensity': {},
     'cmqCommonCallHistoryNRLibVer': {},
     'cmqCommonCallHistoryNumSigASPTriggEar': {},
     'cmqCommonCallHistoryNumSigASPTriggMic': {},
     'cmqCommonCallHistoryPostNRNoiseFloorEstEar': {},
     'cmqCommonCallHistoryPostNRNoiseFloorEstMic': {},
     'cmqCommonCallHistoryPreNRNoiseFloorEstEar': {},
     'cmqCommonCallHistoryPreNRNoiseFloorEstMic': {},
     'cmqCommonCallHistoryTotASPDurEar': {},
     'cmqCommonCallHistoryTotASPDurMic': {},
     'cmqCommonCallHistoryTotNumASPTriggEar': {},
     'cmqCommonCallHistoryTotNumASPTriggMic': {},
     'cmqVideoCallActiveCallReferenceId': {},
     'cmqVideoCallActiveConnectionId': {},
     'cmqVideoCallActiveRxCompressDegradeAverage': {},
     'cmqVideoCallActiveRxCompressDegradeInstant': {},
     'cmqVideoCallActiveRxMOSAverage': {},
     'cmqVideoCallActiveRxMOSInstant': {},
     'cmqVideoCallActiveRxNetworkDegradeAverage': {},
     'cmqVideoCallActiveRxNetworkDegradeInstant': {},
     'cmqVideoCallActiveRxTransscodeDegradeAverage': {},
     'cmqVideoCallActiveRxTransscodeDegradeInstant': {},
     'cmqVideoCallHistoryCallReferenceId': {},
     'cmqVideoCallHistoryConnectionId': {},
     'cmqVideoCallHistoryRxCompressDegradeAverage': {},
     'cmqVideoCallHistoryRxMOSAverage': {},
     'cmqVideoCallHistoryRxNetworkDegradeAverage': {},
     'cmqVideoCallHistoryRxTransscodeDegradeAverage': {},
     'cmqVoIPCallActive3550JCallAvg': {},
     'cmqVoIPCallActive3550JShortTermAvg': {},
     'cmqVoIPCallActiveCallReferenceId': {},
     'cmqVoIPCallActiveConnectionId': {},
     'cmqVoIPCallActiveRxCallConcealRatioPct': {},
     'cmqVoIPCallActiveRxCallDur': {},
     'cmqVoIPCallActiveRxCodecId': {},
     'cmqVoIPCallActiveRxConcealSec': {},
     'cmqVoIPCallActiveRxJBufDlyNow': {},
     'cmqVoIPCallActiveRxJBufLowWater': {},
     'cmqVoIPCallActiveRxJBufMode': {},
     'cmqVoIPCallActiveRxJBufNomDelay': {},
     'cmqVoIPCallActiveRxJBuffHiWater': {},
     'cmqVoIPCallActiveRxPktCntComfortNoise': {},
     'cmqVoIPCallActiveRxPktCntDiscarded': {},
     'cmqVoIPCallActiveRxPktCntEffLoss': {},
     'cmqVoIPCallActiveRxPktCntExpected': {},
     'cmqVoIPCallActiveRxPktCntNotArrived': {},
     'cmqVoIPCallActiveRxPktCntUnusableLate': {},
     'cmqVoIPCallActiveRxPktLossConcealDur': {},
     'cmqVoIPCallActiveRxPktLossRatioPct': {},
     'cmqVoIPCallActiveRxPred107CodecBPL': {},
     'cmqVoIPCallActiveRxPred107CodecIeBase': {},
     'cmqVoIPCallActiveRxPred107DefaultR0': {},
     'cmqVoIPCallActiveRxPred107Idd': {},
     'cmqVoIPCallActiveRxPred107IeEff': {},
     'cmqVoIPCallActiveRxPred107RMosConv': {},
     'cmqVoIPCallActiveRxPred107RMosListen': {},
     'cmqVoIPCallActiveRxPred107RScoreConv': {},
     'cmqVoIPCallActiveRxPred107Rscore': {},
     'cmqVoIPCallActiveRxPredMosLqoAvg': {},
     'cmqVoIPCallActiveRxPredMosLqoBaseline': {},
     'cmqVoIPCallActiveRxPredMosLqoBursts': {},
     'cmqVoIPCallActiveRxPredMosLqoFrLoss': {},
     'cmqVoIPCallActiveRxPredMosLqoMin': {},
     'cmqVoIPCallActiveRxPredMosLqoNumWin': {},
     'cmqVoIPCallActiveRxPredMosLqoRecent': {},
     'cmqVoIPCallActiveRxPredMosLqoVerID': {},
     'cmqVoIPCallActiveRxRoundTripTime': {},
     'cmqVoIPCallActiveRxSevConcealRatioPct': {},
     'cmqVoIPCallActiveRxSevConcealSec': {},
     'cmqVoIPCallActiveRxSignalLvl': {},
     'cmqVoIPCallActiveRxUnimpairedSecOK': {},
     'cmqVoIPCallActiveRxVoiceDur': {},
     'cmqVoIPCallActiveTxCodecId': {},
     'cmqVoIPCallActiveTxNoiseFloor': {},
     'cmqVoIPCallActiveTxSignalLvl': {},
     'cmqVoIPCallActiveTxTmrActSpeechDur': {},
     'cmqVoIPCallActiveTxTmrCallDur': {},
     'cmqVoIPCallActiveTxVadEnabled': {},
     'cmqVoIPCallHistory3550JCallAvg': {},
     'cmqVoIPCallHistory3550JShortTermAvg': {},
     'cmqVoIPCallHistoryCallReferenceId': {},
     'cmqVoIPCallHistoryConnectionId': {},
     'cmqVoIPCallHistoryRxCallConcealRatioPct': {},
     'cmqVoIPCallHistoryRxCallDur': {},
     'cmqVoIPCallHistoryRxCodecId': {},
     'cmqVoIPCallHistoryRxConcealSec': {},
     'cmqVoIPCallHistoryRxJBufDlyNow': {},
     'cmqVoIPCallHistoryRxJBufLowWater': {},
     'cmqVoIPCallHistoryRxJBufMode': {},
     'cmqVoIPCallHistoryRxJBufNomDelay': {},
     'cmqVoIPCallHistoryRxJBuffHiWater': {},
     'cmqVoIPCallHistoryRxPktCntComfortNoise': {},
     'cmqVoIPCallHistoryRxPktCntDiscarded': {},
     'cmqVoIPCallHistoryRxPktCntEffLoss': {},
     'cmqVoIPCallHistoryRxPktCntExpected': {},
     'cmqVoIPCallHistoryRxPktCntNotArrived': {},
     'cmqVoIPCallHistoryRxPktCntUnusableLate': {},
     'cmqVoIPCallHistoryRxPktLossConcealDur': {},
     'cmqVoIPCallHistoryRxPktLossRatioPct': {},
     'cmqVoIPCallHistoryRxPred107CodecBPL': {},
     'cmqVoIPCallHistoryRxPred107CodecIeBase': {},
     'cmqVoIPCallHistoryRxPred107DefaultR0': {},
     'cmqVoIPCallHistoryRxPred107Idd': {},
     'cmqVoIPCallHistoryRxPred107IeEff': {},
     'cmqVoIPCallHistoryRxPred107RMosConv': {},
     'cmqVoIPCallHistoryRxPred107RMosListen': {},
     'cmqVoIPCallHistoryRxPred107RScoreConv': {},
     'cmqVoIPCallHistoryRxPred107Rscore': {},
     'cmqVoIPCallHistoryRxPredMosLqoAvg': {},
     'cmqVoIPCallHistoryRxPredMosLqoBaseline': {},
     'cmqVoIPCallHistoryRxPredMosLqoBursts': {},
     'cmqVoIPCallHistoryRxPredMosLqoFrLoss': {},
     'cmqVoIPCallHistoryRxPredMosLqoMin': {},
     'cmqVoIPCallHistoryRxPredMosLqoNumWin': {},
     'cmqVoIPCallHistoryRxPredMosLqoRecent': {},
     'cmqVoIPCallHistoryRxPredMosLqoVerID': {},
     'cmqVoIPCallHistoryRxRoundTripTime': {},
     'cmqVoIPCallHistoryRxSevConcealRatioPct': {},
     'cmqVoIPCallHistoryRxSevConcealSec': {},
     'cmqVoIPCallHistoryRxSignalLvl': {},
     'cmqVoIPCallHistoryRxUnimpairedSecOK': {},
     'cmqVoIPCallHistoryRxVoiceDur': {},
     'cmqVoIPCallHistoryTxCodecId': {},
     'cmqVoIPCallHistoryTxNoiseFloor': {},
     'cmqVoIPCallHistoryTxSignalLvl': {},
     'cmqVoIPCallHistoryTxTmrActSpeechDur': {},
     'cmqVoIPCallHistoryTxTmrCallDur': {},
     'cmqVoIPCallHistoryTxVadEnabled': {},
     'cnatAddrBindCurrentIdleTime': {},
     'cnatAddrBindDirection': {},
     'cnatAddrBindGlobalAddr': {},
     'cnatAddrBindId': {},
     'cnatAddrBindInTranslate': {},
     'cnatAddrBindNumberOfEntries': {},
     'cnatAddrBindOutTranslate': {},
     'cnatAddrBindType': {},
     'cnatAddrPortBindCurrentIdleTime': {},
     'cnatAddrPortBindDirection': {},
     'cnatAddrPortBindGlobalAddr': {},
     'cnatAddrPortBindGlobalPort': {},
     'cnatAddrPortBindId': {},
     'cnatAddrPortBindInTranslate': {},
     'cnatAddrPortBindNumberOfEntries': {},
     'cnatAddrPortBindOutTranslate': {},
     'cnatAddrPortBindType': {},
     'cnatInterfaceRealm': {},
     'cnatInterfaceStatus': {},
     'cnatInterfaceStorageType': {},
     'cnatProtocolStatsInTranslate': {},
     'cnatProtocolStatsOutTranslate': {},
     'cnatProtocolStatsRejectCount': {},
     'cndeCollectorStatus': {},
     'cndeMaxCollectors': {},
     'cneClientStatRedirectRx': {},
     'cneNotifEnable': {},
     'cneServerStatRedirectTx': {},
     'cnfCIBridgedFlowStatsCtrlEntry': {'2': {}, '3': {}},
     'cnfCICacheEntry': {'2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'cnfCIInterfaceEntry': {'1': {}, '2': {}},
     'cnfCacheInfo': {'4': {}},
     'cnfEICollectorEntry': {'4': {}},
     'cnfEIExportInfoEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cnfExportInfo': {'2': {}},
     'cnfExportStatistics': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'cnfExportTemplate': {'1': {}},
     'cnfPSProtocolStatEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'cnfProtocolStatistics': {'1': {}, '2': {}},
     'cnfTemplateEntry': {'2': {}, '3': {}, '4': {}},
     'cnfTemplateExportInfoEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'cnpdAllStatsEntry': {'10': {},
                           '11': {},
                           '12': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cnpdNotificationsConfig': {'1': {}},
     'cnpdStatusEntry': {'1': {}, '2': {}},
     'cnpdSupportedProtocolsEntry': {'2': {}},
     'cnpdThresholdConfigEntry': {'10': {},
                                  '12': {},
                                  '2': {},
                                  '3': {},
                                  '4': {},
                                  '5': {},
                                  '6': {},
                                  '7': {},
                                  '8': {},
                                  '9': {}},
     'cnpdThresholdHistoryEntry': {'2': {},
                                   '3': {},
                                   '4': {},
                                   '5': {},
                                   '6': {},
                                   '7': {}},
     'cnpdTopNConfigEntry': {'2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {}},
     'cnpdTopNStatsEntry': {'2': {}, '3': {}, '4': {}},
     'cnsClkSelGlobClockMode': {},
     'cnsClkSelGlobCurrHoldoverSeconds': {},
     'cnsClkSelGlobEECOption': {},
     'cnsClkSelGlobESMCMode': {},
     'cnsClkSelGlobHoldoffTime': {},
     'cnsClkSelGlobLastHoldoverSeconds': {},
     'cnsClkSelGlobNetsyncEnable': {},
     'cnsClkSelGlobNetworkOption': {},
     'cnsClkSelGlobNofSources': {},
     'cnsClkSelGlobProcessMode': {},
     'cnsClkSelGlobRevertiveMode': {},
     'cnsClkSelGlobWtrTime': {},
     'cnsExtOutFSW': {},
     'cnsExtOutIntfType': {},
     'cnsExtOutMSW': {},
     'cnsExtOutName': {},
     'cnsExtOutPriority': {},
     'cnsExtOutQualityLevel': {},
     'cnsExtOutSelNetsyncIndex': {},
     'cnsExtOutSquelch': {},
     'cnsInpSrcAlarm': {},
     'cnsInpSrcAlarmInfo': {},
     'cnsInpSrcESMCCap': {},
     'cnsInpSrcFSW': {},
     'cnsInpSrcHoldoffTime': {},
     'cnsInpSrcIntfType': {},
     'cnsInpSrcLockout': {},
     'cnsInpSrcMSW': {},
     'cnsInpSrcName': {},
     'cnsInpSrcPriority': {},
     'cnsInpSrcQualityLevel': {},
     'cnsInpSrcQualityLevelRx': {},
     'cnsInpSrcQualityLevelRxCfg': {},
     'cnsInpSrcQualityLevelTx': {},
     'cnsInpSrcQualityLevelTxCfg': {},
     'cnsInpSrcSSMCap': {},
     'cnsInpSrcSignalFailure': {},
     'cnsInpSrcWtrTime': {},
     'cnsMIBEnableStatusNotification': {},
     'cnsSelInpSrcFSW': {},
     'cnsSelInpSrcIntfType': {},
     'cnsSelInpSrcMSW': {},
     'cnsSelInpSrcName': {},
     'cnsSelInpSrcPriority': {},
     'cnsSelInpSrcQualityLevel': {},
     'cnsSelInpSrcTimestamp': {},
     'cnsT4ClkSrcAlarm': {},
     'cnsT4ClkSrcAlarmInfo': {},
     'cnsT4ClkSrcESMCCap': {},
     'cnsT4ClkSrcFSW': {},
     'cnsT4ClkSrcHoldoffTime': {},
     'cnsT4ClkSrcIntfType': {},
     'cnsT4ClkSrcLockout': {},
     'cnsT4ClkSrcMSW': {},
     'cnsT4ClkSrcName': {},
     'cnsT4ClkSrcPriority': {},
     'cnsT4ClkSrcQualityLevel': {},
     'cnsT4ClkSrcQualityLevelRx': {},
     'cnsT4ClkSrcQualityLevelRxCfg': {},
     'cnsT4ClkSrcQualityLevelTx': {},
     'cnsT4ClkSrcQualityLevelTxCfg': {},
     'cnsT4ClkSrcSSMCap': {},
     'cnsT4ClkSrcSignalFailure': {},
     'cnsT4ClkSrcWtrTime': {},
     'cntpFilterRegisterEntry': {'2': {}, '3': {}, '4': {}},
     'cntpPeersVarEntry': {'10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '16': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '20': {},
                           '21': {},
                           '22': {},
                           '23': {},
                           '24': {},
                           '25': {},
                           '26': {},
                           '27': {},
                           '28': {},
                           '29': {},
                           '3': {},
                           '30': {},
                           '31': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cntpSystem': {'1': {},
                    '10': {},
                    '2': {},
                    '3': {},
                    '4': {},
                    '5': {},
                    '6': {},
                    '7': {},
                    '8': {},
                    '9': {}},
     'coiFECCurrentCorBitErrs': {},
     'coiFECCurrentCorByteErrs': {},
     'coiFECCurrentDetOneErrs': {},
     'coiFECCurrentDetZeroErrs': {},
     'coiFECCurrentUncorWords': {},
     'coiFECIntervalCorBitErrs': {},
     'coiFECIntervalCorByteErrs': {},
     'coiFECIntervalDetOneErrs': {},
     'coiFECIntervalDetZeroErrs': {},
     'coiFECIntervalUncorWords': {},
     'coiFECIntervalValidData': {},
     'coiFECThreshStatus': {},
     'coiFECThreshStorageType': {},
     'coiFECThreshValue': {},
     'coiIfControllerFECMode': {},
     'coiIfControllerFECValidIntervals': {},
     'coiIfControllerLaserAdminStatus': {},
     'coiIfControllerLaserOperStatus': {},
     'coiIfControllerLoopback': {},
     'coiIfControllerOTNValidIntervals': {},
     'coiIfControllerOtnStatus': {},
     'coiIfControllerPreFECBERExponent': {},
     'coiIfControllerPreFECBERMantissa': {},
     'coiIfControllerQFactor': {},
     'coiIfControllerQMargin': {},
     'coiIfControllerTDCOperMode': {},
     'coiIfControllerTDCOperSetting': {},
     'coiIfControllerTDCOperStatus': {},
     'coiIfControllerWavelength': {},
     'coiOtnFarEndCurrentBBERs': {},
     'coiOtnFarEndCurrentBBEs': {},
     'coiOtnFarEndCurrentESRs': {},
     'coiOtnFarEndCurrentESs': {},
     'coiOtnFarEndCurrentFCs': {},
     'coiOtnFarEndCurrentSESRs': {},
     'coiOtnFarEndCurrentSESs': {},
     'coiOtnFarEndCurrentUASs': {},
     'coiOtnFarEndIntervalBBERs': {},
     'coiOtnFarEndIntervalBBEs': {},
     'coiOtnFarEndIntervalESRs': {},
     'coiOtnFarEndIntervalESs': {},
     'coiOtnFarEndIntervalFCs': {},
     'coiOtnFarEndIntervalSESRs': {},
     'coiOtnFarEndIntervalSESs': {},
     'coiOtnFarEndIntervalUASs': {},
     'coiOtnFarEndIntervalValidData': {},
     'coiOtnFarEndThreshStatus': {},
     'coiOtnFarEndThreshStorageType': {},
     'coiOtnFarEndThreshValue': {},
     'coiOtnIfNotifEnabled': {},
     'coiOtnIfODUStatus': {},
     'coiOtnIfOTUStatus': {},
     'coiOtnNearEndCurrentBBERs': {},
     'coiOtnNearEndCurrentBBEs': {},
     'coiOtnNearEndCurrentESRs': {},
     'coiOtnNearEndCurrentESs': {},
     'coiOtnNearEndCurrentFCs': {},
     'coiOtnNearEndCurrentSESRs': {},
     'coiOtnNearEndCurrentSESs': {},
     'coiOtnNearEndCurrentUASs': {},
     'coiOtnNearEndIntervalBBERs': {},
     'coiOtnNearEndIntervalBBEs': {},
     'coiOtnNearEndIntervalESRs': {},
     'coiOtnNearEndIntervalESs': {},
     'coiOtnNearEndIntervalFCs': {},
     'coiOtnNearEndIntervalSESRs': {},
     'coiOtnNearEndIntervalSESs': {},
     'coiOtnNearEndIntervalUASs': {},
     'coiOtnNearEndIntervalValidData': {},
     'coiOtnNearEndThreshStatus': {},
     'coiOtnNearEndThreshStorageType': {},
     'coiOtnNearEndThreshValue': {},
     'convQllcAdminEntry': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'convQllcOperEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'convSdllcAddrEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'convSdllcPortEntry': {'1': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {}},
     'cospfAreaEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'cospfGeneralGroup': {'5': {}},
     'cospfIfEntry': {'1': {}, '2': {}},
     'cospfLocalLsdbEntry': {'6': {}, '7': {}, '8': {}, '9': {}},
     'cospfLsdbEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'cospfShamLinkEntry': {'4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}},
     'cospfShamLinkNbrEntry': {'4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cospfShamLinksEntry': {'10': {},
                             '11': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'cospfTrapControl': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cospfVirtIfEntry': {'1': {}, '2': {}},
     'cospfVirtLocalLsdbEntry': {'6': {}, '7': {}, '8': {}, '9': {}},
     'cpfrActiveProbeAdminStatus': {},
     'cpfrActiveProbeAssignedPfxAddress': {},
     'cpfrActiveProbeAssignedPfxAddressType': {},
     'cpfrActiveProbeAssignedPfxLen': {},
     'cpfrActiveProbeCodecName': {},
     'cpfrActiveProbeDscpValue': {},
     'cpfrActiveProbeMapIndex': {},
     'cpfrActiveProbeMapPolicyIndex': {},
     'cpfrActiveProbeMethod': {},
     'cpfrActiveProbeOperStatus': {},
     'cpfrActiveProbePfrMapIndex': {},
     'cpfrActiveProbeRowStatus': {},
     'cpfrActiveProbeStorageType': {},
     'cpfrActiveProbeTargetAddress': {},
     'cpfrActiveProbeTargetAddressType': {},
     'cpfrActiveProbeTargetPortNumber': {},
     'cpfrActiveProbeType': {},
     'cpfrBRAddress': {},
     'cpfrBRAddressType': {},
     'cpfrBRAuthFailCount': {},
     'cpfrBRConnFailureReason': {},
     'cpfrBRConnStatus': {},
     'cpfrBRKeyName': {},
     'cpfrBROperStatus': {},
     'cpfrBRRowStatus': {},
     'cpfrBRStorageType': {},
     'cpfrBRUpTime': {},
     'cpfrDowngradeBgpCommunity': {},
     'cpfrExitCapacity': {},
     'cpfrExitCost1': {},
     'cpfrExitCost2': {},
     'cpfrExitCost3': {},
     'cpfrExitCostCalcMethod': {},
     'cpfrExitCostDiscard': {},
     'cpfrExitCostDiscardAbsolute': {},
     'cpfrExitCostDiscardPercent': {},
     'cpfrExitCostDiscardType': {},
     'cpfrExitCostEndDayOfMonth': {},
     'cpfrExitCostEndOffset': {},
     'cpfrExitCostEndOffsetType': {},
     'cpfrExitCostFixedFeeCost': {},
     'cpfrExitCostNickName': {},
     'cpfrExitCostRollupPeriod': {},
     'cpfrExitCostSamplingPeriod': {},
     'cpfrExitCostSummerTimeEnd': {},
     'cpfrExitCostSummerTimeOffset': {},
     'cpfrExitCostSummerTimeStart': {},
     'cpfrExitCostTierFee': {},
     'cpfrExitCostTierRowStatus': {},
     'cpfrExitCostTierStorageType': {},
     'cpfrExitMaxUtilRxAbsolute': {},
     'cpfrExitMaxUtilRxPercentage': {},
     'cpfrExitMaxUtilRxType': {},
     'cpfrExitMaxUtilTxAbsolute': {},
     'cpfrExitMaxUtilTxPercentage': {},
     'cpfrExitMaxUtilTxType': {},
     'cpfrExitName': {},
     'cpfrExitNickName': {},
     'cpfrExitOperStatus': {},
     'cpfrExitRollupCollected': {},
     'cpfrExitRollupCumRxBytes': {},
     'cpfrExitRollupCumTxBytes': {},
     'cpfrExitRollupCurrentTgtUtil': {},
     'cpfrExitRollupDiscard': {},
     'cpfrExitRollupLeft': {},
     'cpfrExitRollupMomTgtUtil': {},
     'cpfrExitRollupStartingTgtUtil': {},
     'cpfrExitRollupTimeRemain': {},
     'cpfrExitRollupTotal': {},
     'cpfrExitRowStatus': {},
     'cpfrExitRsvpBandwidthPool': {},
     'cpfrExitRxBandwidth': {},
     'cpfrExitRxLoad': {},
     'cpfrExitStorageType': {},
     'cpfrExitSustainedUtil1': {},
     'cpfrExitSustainedUtil2': {},
     'cpfrExitSustainedUtil3': {},
     'cpfrExitTxBandwidth': {},
     'cpfrExitTxLoad': {},
     'cpfrExitType': {},
     'cpfrLearnAggAccesslistName': {},
     'cpfrLearnAggregationPrefixLen': {},
     'cpfrLearnAggregationType': {},
     'cpfrLearnExpireSessionNum': {},
     'cpfrLearnExpireTime': {},
     'cpfrLearnExpireType': {},
     'cpfrLearnFilterAccessListName': {},
     'cpfrLearnListAclFilterPfxName': {},
     'cpfrLearnListAclName': {},
     'cpfrLearnListMethod': {},
     'cpfrLearnListNbarAppl': {},
     'cpfrLearnListPfxInside': {},
     'cpfrLearnListPfxName': {},
     'cpfrLearnListReferenceName': {},
     'cpfrLearnListRowStatus': {},
     'cpfrLearnListSequenceNum': {},
     'cpfrLearnListStorageType': {},
     'cpfrLearnMethod': {},
     'cpfrLearnMonitorPeriod': {},
     'cpfrLearnPeriodInterval': {},
     'cpfrLearnPrefixesNumber': {},
     'cpfrLinkGroupBRIndex': {},
     'cpfrLinkGroupExitEntry': {'6': {}, '7': {}},
     'cpfrLinkGroupExitIndex': {},
     'cpfrLinkGroupRowStatus': {},
     'cpfrMCAdminStatus': {},
     'cpfrMCConnStatus': {},
     'cpfrMCEntranceLinksMaxUtil': {},
     'cpfrMCEntry': {'26': {}, '27': {}, '28': {}, '29': {}, '30': {}},
     'cpfrMCExitLinksMaxUtil': {},
     'cpfrMCKeepAliveTimer': {},
     'cpfrMCLearnState': {},
     'cpfrMCLearnStateTimeRemain': {},
     'cpfrMCMapIndex': {},
     'cpfrMCMaxPrefixLearn': {},
     'cpfrMCMaxPrefixTotal': {},
     'cpfrMCNetflowExporter': {},
     'cpfrMCNumofBorderRouters': {},
     'cpfrMCNumofExits': {},
     'cpfrMCOperStatus': {},
     'cpfrMCPbrMet': {},
     'cpfrMCPortNumber': {},
     'cpfrMCPrefixConfigured': {},
     'cpfrMCPrefixCount': {},
     'cpfrMCPrefixLearned': {},
     'cpfrMCResolveMapPolicyIndex': {},
     'cpfrMCResolvePolicyType': {},
     'cpfrMCResolvePriority': {},
     'cpfrMCResolveRowStatus': {},
     'cpfrMCResolveStorageType': {},
     'cpfrMCResolveVariance': {},
     'cpfrMCRowStatus': {},
     'cpfrMCRsvpPostDialDelay': {},
     'cpfrMCRsvpSignalingRetries': {},
     'cpfrMCStorageType': {},
     'cpfrMCTracerouteProbeDelay': {},
     'cpfrMapActiveProbeFrequency': {},
     'cpfrMapActiveProbePackets': {},
     'cpfrMapBackoffMaxTimer': {},
     'cpfrMapBackoffMinTimer': {},
     'cpfrMapBackoffStepTimer': {},
     'cpfrMapDelayRelativePercent': {},
     'cpfrMapDelayThresholdMax': {},
     'cpfrMapDelayType': {},
     'cpfrMapEntry': {'38': {}, '39': {}, '40': {}},
     'cpfrMapFallbackLinkGroupName': {},
     'cpfrMapHolddownTimer': {},
     'cpfrMapJitterThresholdMax': {},
     'cpfrMapLinkGroupName': {},
     'cpfrMapLossRelativeAvg': {},
     'cpfrMapLossThresholdMax': {},
     'cpfrMapLossType': {},
     'cpfrMapModeMonitor': {},
     'cpfrMapModeRouteOpts': {},
     'cpfrMapModeSelectExitType': {},
     'cpfrMapMossPercentage': {},
     'cpfrMapMossThresholdMin': {},
     'cpfrMapName': {},
     'cpfrMapNextHopAddress': {},
     'cpfrMapNextHopAddressType': {},
     'cpfrMapPeriodicTimer': {},
     'cpfrMapPrefixForwardInterface': {},
     'cpfrMapRoundRobinResolver': {},
     'cpfrMapRouteMetricBgpLocalPref': {},
     'cpfrMapRouteMetricEigrpTagCommunity': {},
     'cpfrMapRouteMetricStaticTag': {},
     'cpfrMapRowStatus': {},
     'cpfrMapStorageType': {},
     'cpfrMapTracerouteReporting': {},
     'cpfrMapUnreachableRelativeAvg': {},
     'cpfrMapUnreachableThresholdMax': {},
     'cpfrMapUnreachableType': {},
     'cpfrMatchAddrAccessList': {},
     'cpfrMatchAddrPrefixInside': {},
     'cpfrMatchAddrPrefixList': {},
     'cpfrMatchLearnListName': {},
     'cpfrMatchLearnMode': {},
     'cpfrMatchTCAccessListName': {},
     'cpfrMatchTCNbarApplPfxList': {},
     'cpfrMatchTCNbarListName': {},
     'cpfrMatchValid': {},
     'cpfrNbarApplListRowStatus': {},
     'cpfrNbarApplListStorageType': {},
     'cpfrNbarApplPdIndex': {},
     'cpfrResolveMapIndex': {},
     'cpfrTCBRExitIndex': {},
     'cpfrTCBRIndex': {},
     'cpfrTCDscpValue': {},
     'cpfrTCDstMaxPort': {},
     'cpfrTCDstMinPort': {},
     'cpfrTCDstPrefix': {},
     'cpfrTCDstPrefixLen': {},
     'cpfrTCDstPrefixType': {},
     'cpfrTCMActiveLTDelayAvg': {},
     'cpfrTCMActiveLTUnreachableAvg': {},
     'cpfrTCMActiveSTDelayAvg': {},
     'cpfrTCMActiveSTJitterAvg': {},
     'cpfrTCMActiveSTUnreachableAvg': {},
     'cpfrTCMAge': {},
     'cpfrTCMAttempts': {},
     'cpfrTCMLastUpdateTime': {},
     'cpfrTCMMOSPercentage': {},
     'cpfrTCMPackets': {},
     'cpfrTCMPassiveLTDelayAvg': {},
     'cpfrTCMPassiveLTLossAvg': {},
     'cpfrTCMPassiveLTUnreachableAvg': {},
     'cpfrTCMPassiveSTDelayAvg': {},
     'cpfrTCMPassiveSTLossAvg': {},
     'cpfrTCMPassiveSTUnreachableAvg': {},
     'cpfrTCMapIndex': {},
     'cpfrTCMapPolicyIndex': {},
     'cpfrTCMetricsValid': {},
     'cpfrTCNbarApplication': {},
     'cpfrTCProtocol': {},
     'cpfrTCSControlBy': {},
     'cpfrTCSControlState': {},
     'cpfrTCSLastOOPEventTime': {},
     'cpfrTCSLastOOPReason': {},
     'cpfrTCSLastRouteChangeEvent': {},
     'cpfrTCSLastRouteChangeReason': {},
     'cpfrTCSLearnListIndex': {},
     'cpfrTCSTimeOnCurrExit': {},
     'cpfrTCSTimeRemainCurrState': {},
     'cpfrTCSType': {},
     'cpfrTCSrcMaxPort': {},
     'cpfrTCSrcMinPort': {},
     'cpfrTCSrcPrefix': {},
     'cpfrTCSrcPrefixLen': {},
     'cpfrTCSrcPrefixType': {},
     'cpfrTCStatus': {},
     'cpfrTrafficClassValid': {},
     'cpim': {'1': {},
              '2': {},
              '3': {},
              '4': {},
              '5': {},
              '6': {},
              '7': {},
              '8': {},
              '9': {}},
     'cpmCPUHistoryTable.1.2': {},
     'cpmCPUHistoryTable.1.3': {},
     'cpmCPUHistoryTable.1.4': {},
     'cpmCPUHistoryTable.1.5': {},
     'cpmCPUProcessHistoryTable.1.2': {},
     'cpmCPUProcessHistoryTable.1.3': {},
     'cpmCPUProcessHistoryTable.1.4': {},
     'cpmCPUProcessHistoryTable.1.5': {},
     'cpmCPUThresholdTable.1.2': {},
     'cpmCPUThresholdTable.1.3': {},
     'cpmCPUThresholdTable.1.4': {},
     'cpmCPUThresholdTable.1.5': {},
     'cpmCPUThresholdTable.1.6': {},
     'cpmCPUTotalTable.1.10': {},
     'cpmCPUTotalTable.1.11': {},
     'cpmCPUTotalTable.1.12': {},
     'cpmCPUTotalTable.1.13': {},
     'cpmCPUTotalTable.1.14': {},
     'cpmCPUTotalTable.1.15': {},
     'cpmCPUTotalTable.1.16': {},
     'cpmCPUTotalTable.1.17': {},
     'cpmCPUTotalTable.1.18': {},
     'cpmCPUTotalTable.1.19': {},
     'cpmCPUTotalTable.1.2': {},
     'cpmCPUTotalTable.1.20': {},
     'cpmCPUTotalTable.1.21': {},
     'cpmCPUTotalTable.1.22': {},
     'cpmCPUTotalTable.1.23': {},
     'cpmCPUTotalTable.1.24': {},
     'cpmCPUTotalTable.1.25': {},
     'cpmCPUTotalTable.1.26': {},
     'cpmCPUTotalTable.1.27': {},
     'cpmCPUTotalTable.1.28': {},
     'cpmCPUTotalTable.1.29': {},
     'cpmCPUTotalTable.1.3': {},
     'cpmCPUTotalTable.1.4': {},
     'cpmCPUTotalTable.1.5': {},
     'cpmCPUTotalTable.1.6': {},
     'cpmCPUTotalTable.1.7': {},
     'cpmCPUTotalTable.1.8': {},
     'cpmCPUTotalTable.1.9': {},
     'cpmProcessExtTable.1.1': {},
     'cpmProcessExtTable.1.2': {},
     'cpmProcessExtTable.1.3': {},
     'cpmProcessExtTable.1.4': {},
     'cpmProcessExtTable.1.5': {},
     'cpmProcessExtTable.1.6': {},
     'cpmProcessExtTable.1.7': {},
     'cpmProcessExtTable.1.8': {},
     'cpmProcessTable.1.1': {},
     'cpmProcessTable.1.2': {},
     'cpmProcessTable.1.4': {},
     'cpmProcessTable.1.5': {},
     'cpmProcessTable.1.6': {},
     'cpmThreadTable.1.2': {},
     'cpmThreadTable.1.3': {},
     'cpmThreadTable.1.4': {},
     'cpmThreadTable.1.5': {},
     'cpmThreadTable.1.6': {},
     'cpmThreadTable.1.7': {},
     'cpmThreadTable.1.8': {},
     'cpmThreadTable.1.9': {},
     'cpmVirtualProcessTable.1.10': {},
     'cpmVirtualProcessTable.1.11': {},
     'cpmVirtualProcessTable.1.12': {},
     'cpmVirtualProcessTable.1.13': {},
     'cpmVirtualProcessTable.1.2': {},
     'cpmVirtualProcessTable.1.3': {},
     'cpmVirtualProcessTable.1.4': {},
     'cpmVirtualProcessTable.1.5': {},
     'cpmVirtualProcessTable.1.6': {},
     'cpmVirtualProcessTable.1.7': {},
     'cpmVirtualProcessTable.1.8': {},
     'cpmVirtualProcessTable.1.9': {},
     'cpwAtmAvgCellsPacked': {},
     'cpwAtmCellPacking': {},
     'cpwAtmCellsReceived': {},
     'cpwAtmCellsRejected': {},
     'cpwAtmCellsSent': {},
     'cpwAtmCellsTagged': {},
     'cpwAtmClpQosMapping': {},
     'cpwAtmEncap': {},
     'cpwAtmHCCellsReceived': {},
     'cpwAtmHCCellsRejected': {},
     'cpwAtmHCCellsTagged': {},
     'cpwAtmIf': {},
     'cpwAtmMcptTimeout': {},
     'cpwAtmMncp': {},
     'cpwAtmOamCellSupported': {},
     'cpwAtmPeerMncp': {},
     'cpwAtmPktsReceived': {},
     'cpwAtmPktsRejected': {},
     'cpwAtmPktsSent': {},
     'cpwAtmQosScalingFactor': {},
     'cpwAtmRowStatus': {},
     'cpwAtmVci': {},
     'cpwAtmVpi': {},
     'cpwVcAdminStatus': {},
     'cpwVcControlWord': {},
     'cpwVcCreateTime': {},
     'cpwVcDescr': {},
     'cpwVcHoldingPriority': {},
     'cpwVcID': {},
     'cpwVcIdMappingVcIndex': {},
     'cpwVcInboundMode': {},
     'cpwVcInboundOperStatus': {},
     'cpwVcInboundVcLabel': {},
     'cpwVcIndexNext': {},
     'cpwVcLocalGroupID': {},
     'cpwVcLocalIfMtu': {},
     'cpwVcLocalIfString': {},
     'cpwVcMplsEntry': {'1': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {}},
     'cpwVcMplsInboundEntry': {'2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'cpwVcMplsMIB.1.2': {},
     'cpwVcMplsMIB.1.4': {},
     'cpwVcMplsNonTeMappingEntry': {'4': {}},
     'cpwVcMplsOutboundEntry': {'2': {},
                                '3': {},
                                '4': {},
                                '5': {},
                                '6': {},
                                '7': {},
                                '8': {},
                                '9': {}},
     'cpwVcMplsTeMappingEntry': {'6': {}},
     'cpwVcName': {},
     'cpwVcNotifRate': {},
     'cpwVcOperStatus': {},
     'cpwVcOutboundOperStatus': {},
     'cpwVcOutboundVcLabel': {},
     'cpwVcOwner': {},
     'cpwVcPeerAddr': {},
     'cpwVcPeerAddrType': {},
     'cpwVcPeerMappingVcIndex': {},
     'cpwVcPerfCurrentInHCBytes': {},
     'cpwVcPerfCurrentInHCPackets': {},
     'cpwVcPerfCurrentOutHCBytes': {},
     'cpwVcPerfCurrentOutHCPackets': {},
     'cpwVcPerfIntervalInHCBytes': {},
     'cpwVcPerfIntervalInHCPackets': {},
     'cpwVcPerfIntervalOutHCBytes': {},
     'cpwVcPerfIntervalOutHCPackets': {},
     'cpwVcPerfIntervalTimeElapsed': {},
     'cpwVcPerfIntervalValidData': {},
     'cpwVcPerfTotalDiscontinuityTime': {},
     'cpwVcPerfTotalErrorPackets': {},
     'cpwVcPerfTotalInHCBytes': {},
     'cpwVcPerfTotalInHCPackets': {},
     'cpwVcPerfTotalOutHCBytes': {},
     'cpwVcPerfTotalOutHCPackets': {},
     'cpwVcPsnType': {},
     'cpwVcRemoteControlWord': {},
     'cpwVcRemoteGroupID': {},
     'cpwVcRemoteIfMtu': {},
     'cpwVcRemoteIfString': {},
     'cpwVcRowStatus': {},
     'cpwVcSetUpPriority': {},
     'cpwVcStorageType': {},
     'cpwVcTimeElapsed': {},
     'cpwVcType': {},
     'cpwVcUpDownNotifEnable': {},
     'cpwVcUpTime': {},
     'cpwVcValidIntervals': {},
     'cqvTerminationPeEncap': {},
     'cqvTerminationRowStatus': {},
     'cqvTranslationEntry': {'3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'creAcctClientAverageResponseDelay': {},
     'creAcctClientBadAuthenticators': {},
     'creAcctClientBufferAllocFailures': {},
     'creAcctClientDupIDs': {},
     'creAcctClientLastUsedSourceId': {},
     'creAcctClientMalformedResponses': {},
     'creAcctClientMaxBufferSize': {},
     'creAcctClientMaxResponseDelay': {},
     'creAcctClientTimeouts': {},
     'creAcctClientTotalPacketsWithResponses': {},
     'creAcctClientTotalPacketsWithoutResponses': {},
     'creAcctClientTotalResponses': {},
     'creAcctClientUnknownResponses': {},
     'creAuthClientAverageResponseDelay': {},
     'creAuthClientBadAuthenticators': {},
     'creAuthClientBufferAllocFailures': {},
     'creAuthClientDupIDs': {},
     'creAuthClientLastUsedSourceId': {},
     'creAuthClientMalformedResponses': {},
     'creAuthClientMaxBufferSize': {},
     'creAuthClientMaxResponseDelay': {},
     'creAuthClientTimeouts': {},
     'creAuthClientTotalPacketsWithResponses': {},
     'creAuthClientTotalPacketsWithoutResponses': {},
     'creAuthClientTotalResponses': {},
     'creAuthClientUnknownResponses': {},
     'creClientLastUsedSourceId': {},
     'creClientLastUsedSourcePort': {},
     'creClientSourcePortRangeEnd': {},
     'creClientSourcePortRangeStart': {},
     'creClientTotalAccessRejects': {},
     'creClientTotalAverageResponseDelay': {},
     'creClientTotalMaxDoneQLength': {},
     'creClientTotalMaxInQLength': {},
     'creClientTotalMaxWaitQLength': {},
     'crttMonIPEchoAdminDscp': {},
     'crttMonIPEchoAdminFlowLabel': {},
     'crttMonIPEchoAdminLSPSelAddrType': {},
     'crttMonIPEchoAdminLSPSelAddress': {},
     'crttMonIPEchoAdminNameServerAddrType': {},
     'crttMonIPEchoAdminNameServerAddress': {},
     'crttMonIPEchoAdminSourceAddrType': {},
     'crttMonIPEchoAdminSourceAddress': {},
     'crttMonIPEchoAdminTargetAddrType': {},
     'crttMonIPEchoAdminTargetAddress': {},
     'crttMonIPEchoPathAdminHopAddrType': {},
     'crttMonIPEchoPathAdminHopAddress': {},
     'crttMonIPHistoryCollectionAddrType': {},
     'crttMonIPHistoryCollectionAddress': {},
     'crttMonIPLatestRttOperAddress': {},
     'crttMonIPLatestRttOperAddressType': {},
     'crttMonIPLpdGrpStatsTargetPEAddr': {},
     'crttMonIPLpdGrpStatsTargetPEAddrType': {},
     'crttMonIPStatsCollectAddress': {},
     'crttMonIPStatsCollectAddressType': {},
     'csNotifications': {'1': {}},
     'csbAdjacencyStatusNotifEnabled': {},
     'csbBlackListNotifEnabled': {},
     'csbCallStatsActiveTranscodeFlows': {},
     'csbCallStatsAvailableFlows': {},
     'csbCallStatsAvailablePktRate': {},
     'csbCallStatsAvailableTranscodeFlows': {},
     'csbCallStatsCallsHigh': {},
     'csbCallStatsCallsLow': {},
     'csbCallStatsInstancePhysicalIndex': {},
     'csbCallStatsNoMediaCount': {},
     'csbCallStatsPeakFlows': {},
     'csbCallStatsPeakSigFlows': {},
     'csbCallStatsPeakTranscodeFlows': {},
     'csbCallStatsRTPOctetsDiscard': {},
     'csbCallStatsRTPOctetsRcvd': {},
     'csbCallStatsRTPOctetsSent': {},
     'csbCallStatsRTPPktsDiscard': {},
     'csbCallStatsRTPPktsRcvd': {},
     'csbCallStatsRTPPktsSent': {},
     'csbCallStatsRate1Sec': {},
     'csbCallStatsRouteErrors': {},
     'csbCallStatsSbcName': {},
     'csbCallStatsTotalFlows': {},
     'csbCallStatsTotalSigFlows': {},
     'csbCallStatsTotalTranscodeFlows': {},
     'csbCallStatsUnclassifiedPkts': {},
     'csbCallStatsUsedFlows': {},
     'csbCallStatsUsedSigFlows': {},
     'csbCongestionAlarmNotifEnabled': {},
     'csbCurrPeriodicIpsecCalls': {},
     'csbCurrPeriodicStatsActivatingCalls': {},
     'csbCurrPeriodicStatsActiveCallFailure': {},
     'csbCurrPeriodicStatsActiveCalls': {},
     'csbCurrPeriodicStatsActiveE2EmergencyCalls': {},
     'csbCurrPeriodicStatsActiveEmergencyCalls': {},
     'csbCurrPeriodicStatsActiveIpv6Calls': {},
     'csbCurrPeriodicStatsAudioTranscodedCalls': {},
     'csbCurrPeriodicStatsCallMediaFailure': {},
     'csbCurrPeriodicStatsCallResourceFailure': {},
     'csbCurrPeriodicStatsCallRoutingFailure': {},
     'csbCurrPeriodicStatsCallSetupCACBandwidthFailure': {},
     'csbCurrPeriodicStatsCallSetupCACCallLimitFailure': {},
     'csbCurrPeriodicStatsCallSetupCACMediaLimitFailure': {},
     'csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure': {},
     'csbCurrPeriodicStatsCallSetupCACPolicyFailure': {},
     'csbCurrPeriodicStatsCallSetupCACRateLimitFailure': {},
     'csbCurrPeriodicStatsCallSetupNAPolicyFailure': {},
     'csbCurrPeriodicStatsCallSetupPolicyFailure': {},
     'csbCurrPeriodicStatsCallSetupRoutingPolicyFailure': {},
     'csbCurrPeriodicStatsCallSigFailure': {},
     'csbCurrPeriodicStatsCongestionFailure': {},
     'csbCurrPeriodicStatsCurrentTaps': {},
     'csbCurrPeriodicStatsDeactivatingCalls': {},
     'csbCurrPeriodicStatsDtmfIw2833Calls': {},
     'csbCurrPeriodicStatsDtmfIw2833InbandCalls': {},
     'csbCurrPeriodicStatsDtmfIwInbandCalls': {},
     'csbCurrPeriodicStatsFailedCallAttempts': {},
     'csbCurrPeriodicStatsFaxTranscodedCalls': {},
     'csbCurrPeriodicStatsImsRxActiveCalls': {},
     'csbCurrPeriodicStatsImsRxCallRenegotiationAttempts': {},
     'csbCurrPeriodicStatsImsRxCallRenegotiationFailures': {},
     'csbCurrPeriodicStatsImsRxCallSetupFaiures': {},
     'csbCurrPeriodicStatsNonSrtpCalls': {},
     'csbCurrPeriodicStatsRtpDisallowedFailures': {},
     'csbCurrPeriodicStatsSrtpDisallowedFailures': {},
     'csbCurrPeriodicStatsSrtpIwCalls': {},
     'csbCurrPeriodicStatsSrtpNonIwCalls': {},
     'csbCurrPeriodicStatsTimestamp': {},
     'csbCurrPeriodicStatsTotalCallAttempts': {},
     'csbCurrPeriodicStatsTotalCallUpdateFailure': {},
     'csbCurrPeriodicStatsTotalTapsRequested': {},
     'csbCurrPeriodicStatsTotalTapsSucceeded': {},
     'csbCurrPeriodicStatsTranscodedCalls': {},
     'csbCurrPeriodicStatsTransratedCalls': {},
     'csbDiameterConnectionStatusNotifEnabled': {},
     'csbH248ControllerStatusNotifEnabled': {},
     'csbH248StatsEstablishedTime': {},
     'csbH248StatsEstablishedTimeRev1': {},
     'csbH248StatsLT': {},
     'csbH248StatsLTRev1': {},
     'csbH248StatsRTT': {},
     'csbH248StatsRTTRev1': {},
     'csbH248StatsRepliesRcvd': {},
     'csbH248StatsRepliesRcvdRev1': {},
     'csbH248StatsRepliesRetried': {},
     'csbH248StatsRepliesRetriedRev1': {},
     'csbH248StatsRepliesSent': {},
     'csbH248StatsRepliesSentRev1': {},
     'csbH248StatsRequestsFailed': {},
     'csbH248StatsRequestsFailedRev1': {},
     'csbH248StatsRequestsRcvd': {},
     'csbH248StatsRequestsRcvdRev1': {},
     'csbH248StatsRequestsRetried': {},
     'csbH248StatsRequestsRetriedRev1': {},
     'csbH248StatsRequestsSent': {},
     'csbH248StatsRequestsSentRev1': {},
     'csbH248StatsSegPktsRcvd': {},
     'csbH248StatsSegPktsRcvdRev1': {},
     'csbH248StatsSegPktsSent': {},
     'csbH248StatsSegPktsSentRev1': {},
     'csbH248StatsTMaxTimeoutVal': {},
     'csbH248StatsTMaxTimeoutValRev1': {},
     'csbHistoryStatsActiveCallFailure': {},
     'csbHistoryStatsActiveCalls': {},
     'csbHistoryStatsActiveE2EmergencyCalls': {},
     'csbHistoryStatsActiveEmergencyCalls': {},
     'csbHistoryStatsActiveIpv6Calls': {},
     'csbHistoryStatsAudioTranscodedCalls': {},
     'csbHistoryStatsCallMediaFailure': {},
     'csbHistoryStatsCallResourceFailure': {},
     'csbHistoryStatsCallRoutingFailure': {},
     'csbHistoryStatsCallSetupCACBandwidthFailure': {},
     'csbHistoryStatsCallSetupCACCallLimitFailure': {},
     'csbHistoryStatsCallSetupCACMediaLimitFailure': {},
     'csbHistoryStatsCallSetupCACMediaUpdateFailure': {},
     'csbHistoryStatsCallSetupCACPolicyFailure': {},
     'csbHistoryStatsCallSetupCACRateLimitFailure': {},
     'csbHistoryStatsCallSetupNAPolicyFailure': {},
     'csbHistoryStatsCallSetupPolicyFailure': {},
     'csbHistoryStatsCallSetupRoutingPolicyFailure': {},
     'csbHistoryStatsCongestionFailure': {},
     'csbHistoryStatsCurrentTaps': {},
     'csbHistoryStatsDtmfIw2833Calls': {},
     'csbHistoryStatsDtmfIw2833InbandCalls': {},
     'csbHistoryStatsDtmfIwInbandCalls': {},
     'csbHistoryStatsFailSigFailure': {},
     'csbHistoryStatsFailedCallAttempts': {},
     'csbHistoryStatsFaxTranscodedCalls': {},
     'csbHistoryStatsImsRxActiveCalls': {},
     'csbHistoryStatsImsRxCallRenegotiationAttempts': {},
     'csbHistoryStatsImsRxCallRenegotiationFailures': {},
     'csbHistoryStatsImsRxCallSetupFailures': {},
     'csbHistoryStatsIpsecCalls': {},
     'csbHistoryStatsNonSrtpCalls': {},
     'csbHistoryStatsRtpDisallowedFailures': {},
     'csbHistoryStatsSrtpDisallowedFailures': {},
     'csbHistoryStatsSrtpIwCalls': {},
     'csbHistoryStatsSrtpNonIwCalls': {},
     'csbHistoryStatsTimestamp': {},
     'csbHistoryStatsTotalCallAttempts': {},
     'csbHistoryStatsTotalCallUpdateFailure': {},
     'csbHistoryStatsTotalTapsRequested': {},
     'csbHistoryStatsTotalTapsSucceeded': {},
     'csbHistroyStatsTranscodedCalls': {},
     'csbHistroyStatsTransratedCalls': {},
     'csbPerFlowStatsAdrStatus': {},
     'csbPerFlowStatsDscpSettings': {},
     'csbPerFlowStatsEPJitter': {},
     'csbPerFlowStatsFlowType': {},
     'csbPerFlowStatsQASettings': {},
     'csbPerFlowStatsRTCPPktsLost': {},
     'csbPerFlowStatsRTCPPktsRcvd': {},
     'csbPerFlowStatsRTCPPktsSent': {},
     'csbPerFlowStatsRTPOctetsDiscard': {},
     'csbPerFlowStatsRTPOctetsRcvd': {},
     'csbPerFlowStatsRTPOctetsSent': {},
     'csbPerFlowStatsRTPPktsDiscard': {},
     'csbPerFlowStatsRTPPktsLost': {},
     'csbPerFlowStatsRTPPktsRcvd': {},
     'csbPerFlowStatsRTPPktsSent': {},
     'csbPerFlowStatsTmanPerMbs': {},
     'csbPerFlowStatsTmanPerSdr': {},
     'csbRadiusConnectionStatusNotifEnabled': {},
     'csbRadiusStatsAcsAccpts': {},
     'csbRadiusStatsAcsChalls': {},
     'csbRadiusStatsAcsRejects': {},
     'csbRadiusStatsAcsReqs': {},
     'csbRadiusStatsAcsRtrns': {},
     'csbRadiusStatsActReqs': {},
     'csbRadiusStatsActRetrans': {},
     'csbRadiusStatsActRsps': {},
     'csbRadiusStatsBadAuths': {},
     'csbRadiusStatsClientName': {},
     'csbRadiusStatsClientType': {},
     'csbRadiusStatsDropped': {},
     'csbRadiusStatsMalformedRsps': {},
     'csbRadiusStatsPending': {},
     'csbRadiusStatsSrvrName': {},
     'csbRadiusStatsTimeouts': {},
     'csbRadiusStatsUnknownType': {},
     'csbRfBillRealmStatsFailEventAcrs': {},
     'csbRfBillRealmStatsFailInterimAcrs': {},
     'csbRfBillRealmStatsFailStartAcrs': {},
     'csbRfBillRealmStatsFailStopAcrs': {},
     'csbRfBillRealmStatsRealmName': {},
     'csbRfBillRealmStatsSuccEventAcrs': {},
     'csbRfBillRealmStatsSuccInterimAcrs': {},
     'csbRfBillRealmStatsSuccStartAcrs': {},
     'csbRfBillRealmStatsSuccStopAcrs': {},
     'csbRfBillRealmStatsTotalEventAcrs': {},
     'csbRfBillRealmStatsTotalInterimAcrs': {},
     'csbRfBillRealmStatsTotalStartAcrs': {},
     'csbRfBillRealmStatsTotalStopAcrs': {},
     'csbSIPMthdCurrentStatsAdjName': {},
     'csbSIPMthdCurrentStatsMethodName': {},
     'csbSIPMthdCurrentStatsReqIn': {},
     'csbSIPMthdCurrentStatsReqOut': {},
     'csbSIPMthdCurrentStatsResp1xxIn': {},
     'csbSIPMthdCurrentStatsResp1xxOut': {},
     'csbSIPMthdCurrentStatsResp2xxIn': {},
     'csbSIPMthdCurrentStatsResp2xxOut': {},
     'csbSIPMthdCurrentStatsResp3xxIn': {},
     'csbSIPMthdCurrentStatsResp3xxOut': {},
     'csbSIPMthdCurrentStatsResp4xxIn': {},
     'csbSIPMthdCurrentStatsResp4xxOut': {},
     'csbSIPMthdCurrentStatsResp5xxIn': {},
     'csbSIPMthdCurrentStatsResp5xxOut': {},
     'csbSIPMthdCurrentStatsResp6xxIn': {},
     'csbSIPMthdCurrentStatsResp6xxOut': {},
     'csbSIPMthdHistoryStatsAdjName': {},
     'csbSIPMthdHistoryStatsMethodName': {},
     'csbSIPMthdHistoryStatsReqIn': {},
     'csbSIPMthdHistoryStatsReqOut': {},
     'csbSIPMthdHistoryStatsResp1xxIn': {},
     'csbSIPMthdHistoryStatsResp1xxOut': {},
     'csbSIPMthdHistoryStatsResp2xxIn': {},
     'csbSIPMthdHistoryStatsResp2xxOut': {},
     'csbSIPMthdHistoryStatsResp3xxIn': {},
     'csbSIPMthdHistoryStatsResp3xxOut': {},
     'csbSIPMthdHistoryStatsResp4xxIn': {},
     'csbSIPMthdHistoryStatsResp4xxOut': {},
     'csbSIPMthdHistoryStatsResp5xxIn': {},
     'csbSIPMthdHistoryStatsResp5xxOut': {},
     'csbSIPMthdHistoryStatsResp6xxIn': {},
     'csbSIPMthdHistoryStatsResp6xxOut': {},
     'csbSIPMthdRCCurrentStatsAdjName': {},
     'csbSIPMthdRCCurrentStatsMethodName': {},
     'csbSIPMthdRCCurrentStatsRespIn': {},
     'csbSIPMthdRCCurrentStatsRespOut': {},
     'csbSIPMthdRCHistoryStatsAdjName': {},
     'csbSIPMthdRCHistoryStatsMethodName': {},
     'csbSIPMthdRCHistoryStatsRespIn': {},
     'csbSIPMthdRCHistoryStatsRespOut': {},
     'csbSLAViolationNotifEnabled': {},
     'csbSLAViolationNotifEnabledRev1': {},
     'csbServiceStateNotifEnabled': {},
     'csbSourceAlertNotifEnabled': {},
     'cslFarEndTotalEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cslTotalEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cspFarEndTotalEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cspTotalEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'cssTotalEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'csubAggStatsAuthSessions': {},
     'csubAggStatsAvgSessionRPH': {},
     'csubAggStatsAvgSessionRPM': {},
     'csubAggStatsAvgSessionUptime': {},
     'csubAggStatsCurrAuthSessions': {},
     'csubAggStatsCurrCreatedSessions': {},
     'csubAggStatsCurrDiscSessions': {},
     'csubAggStatsCurrFailedSessions': {},
     'csubAggStatsCurrFlowsUp': {},
     'csubAggStatsCurrInvalidIntervals': {},
     'csubAggStatsCurrTimeElapsed': {},
     'csubAggStatsCurrUpSessions': {},
     'csubAggStatsCurrValidIntervals': {},
     'csubAggStatsDayAuthSessions': {},
     'csubAggStatsDayCreatedSessions': {},
     'csubAggStatsDayDiscSessions': {},
     'csubAggStatsDayFailedSessions': {},
     'csubAggStatsDayUpSessions': {},
     'csubAggStatsDiscontinuityTime': {},
     'csubAggStatsHighUpSessions': {},
     'csubAggStatsIntAuthSessions': {},
     'csubAggStatsIntCreatedSessions': {},
     'csubAggStatsIntDiscSessions': {},
     'csubAggStatsIntFailedSessions': {},
     'csubAggStatsIntUpSessions': {},
     'csubAggStatsIntValid': {},
     'csubAggStatsLightWeightSessions': {},
     'csubAggStatsPendingSessions': {},
     'csubAggStatsRedSessions': {},
     'csubAggStatsThrottleEngagements': {},
     'csubAggStatsTotalAuthSessions': {},
     'csubAggStatsTotalCreatedSessions': {},
     'csubAggStatsTotalDiscSessions': {},
     'csubAggStatsTotalFailedSessions': {},
     'csubAggStatsTotalFlowsUp': {},
     'csubAggStatsTotalLightWeightSessions': {},
     'csubAggStatsTotalUpSessions': {},
     'csubAggStatsUnAuthSessions': {},
     'csubAggStatsUpSessions': {},
     'csubJobControl': {},
     'csubJobCount': {},
     'csubJobFinishedNotifyEnable': {},
     'csubJobFinishedReason': {},
     'csubJobFinishedTime': {},
     'csubJobIdNext': {},
     'csubJobIndexedAttributes': {},
     'csubJobMatchAcctSessionId': {},
     'csubJobMatchAuthenticated': {},
     'csubJobMatchCircuitId': {},
     'csubJobMatchDanglingDuration': {},
     'csubJobMatchDhcpClass': {},
     'csubJobMatchDnis': {},
     'csubJobMatchDomain': {},
     'csubJobMatchDomainIpAddr': {},
     'csubJobMatchDomainIpAddrType': {},
     'csubJobMatchDomainIpMask': {},
     'csubJobMatchDomainVrf': {},
     'csubJobMatchIdentities': {},
     'csubJobMatchMacAddress': {},
     'csubJobMatchMedia': {},
     'csubJobMatchMlpNegotiated': {},
     'csubJobMatchNasPort': {},
     'csubJobMatchNativeIpAddr': {},
     'csubJobMatchNativeIpAddrType': {},
     'csubJobMatchNativeIpMask': {},
     'csubJobMatchNativeVrf': {},
     'csubJobMatchOtherParams': {},
     'csubJobMatchPbhk': {},
     'csubJobMatchProtocol': {},
     'csubJobMatchRedundancyMode': {},
     'csubJobMatchRemoteId': {},
     'csubJobMatchServiceName': {},
     'csubJobMatchState': {},
     'csubJobMatchSubscriberLabel': {},
     'csubJobMatchTunnelName': {},
     'csubJobMatchUsername': {},
     'csubJobMaxLife': {},
     'csubJobMaxNumber': {},
     'csubJobQueryResultingReportSize': {},
     'csubJobQuerySortKey1': {},
     'csubJobQuerySortKey2': {},
     'csubJobQuerySortKey3': {},
     'csubJobQueueJobId': {},
     'csubJobReportSession': {},
     'csubJobStartedTime': {},
     'csubJobState': {},
     'csubJobStatus': {},
     'csubJobStorage': {},
     'csubJobType': {},
     'csubSessionAcctSessionId': {},
     'csubSessionAuthenticated': {},
     'csubSessionAvailableIdentities': {},
     'csubSessionByType': {},
     'csubSessionCircuitId': {},
     'csubSessionCreationTime': {},
     'csubSessionDerivedCfg': {},
     'csubSessionDhcpClass': {},
     'csubSessionDnis': {},
     'csubSessionDomain': {},
     'csubSessionDomainIpAddr': {},
     'csubSessionDomainIpAddrType': {},
     'csubSessionDomainIpMask': {},
     'csubSessionDomainVrf': {},
     'csubSessionIfIndex': {},
     'csubSessionIpAddrAssignment': {},
     'csubSessionLastChanged': {},
     'csubSessionLocationIdentifier': {},
     'csubSessionMacAddress': {},
     'csubSessionMedia': {},
     'csubSessionMlpNegotiated': {},
     'csubSessionNasPort': {},
     'csubSessionNativeIpAddr': {},
     'csubSessionNativeIpAddr2': {},
     'csubSessionNativeIpAddrType': {},
     'csubSessionNativeIpAddrType2': {},
     'csubSessionNativeIpMask': {},
     'csubSessionNativeIpMask2': {},
     'csubSessionNativeVrf': {},
     'csubSessionPbhk': {},
     'csubSessionProtocol': {},
     'csubSessionRedundancyMode': {},
     'csubSessionRemoteId': {},
     'csubSessionServiceIdentifier': {},
     'csubSessionState': {},
     'csubSessionSubscriberLabel': {},
     'csubSessionTunnelName': {},
     'csubSessionType': {},
     'csubSessionUsername': {},
     'cubeEnabled': {},
     'cubeTotalSessionAllowed': {},
     'cubeVersion': {},
     'cufwAIAlertEnabled': {},
     'cufwAIAuditTrailEnabled': {},
     'cufwAaicGlobalNumBadPDUSize': {},
     'cufwAaicGlobalNumBadPortRange': {},
     'cufwAaicGlobalNumBadProtocolOps': {},
     'cufwAaicHttpNumBadContent': {},
     'cufwAaicHttpNumBadPDUSize': {},
     'cufwAaicHttpNumBadProtocolOps': {},
     'cufwAaicHttpNumDoubleEncodedPkts': {},
     'cufwAaicHttpNumLargeURIs': {},
     'cufwAaicHttpNumMismatchContent': {},
     'cufwAaicHttpNumTunneledConns': {},
     'cufwAppConnNumAborted': {},
     'cufwAppConnNumActive': {},
     'cufwAppConnNumAttempted': {},
     'cufwAppConnNumHalfOpen': {},
     'cufwAppConnNumPolicyDeclined': {},
     'cufwAppConnNumResDeclined': {},
     'cufwAppConnNumSetupsAborted': {},
     'cufwAppConnSetupRate1': {},
     'cufwAppConnSetupRate5': {},
     'cufwCntlL2StaticMacAddressMoved': {},
     'cufwCntlUrlfServerStatusChange': {},
     'cufwConnGlobalConnSetupRate1': {},
     'cufwConnGlobalConnSetupRate5': {},
     'cufwConnGlobalNumAborted': {},
     'cufwConnGlobalNumActive': {},
     'cufwConnGlobalNumAttempted': {},
     'cufwConnGlobalNumEmbryonic': {},
     'cufwConnGlobalNumExpired': {},
     'cufwConnGlobalNumHalfOpen': {},
     'cufwConnGlobalNumPolicyDeclined': {},
     'cufwConnGlobalNumRemoteAccess': {},
     'cufwConnGlobalNumResDeclined': {},
     'cufwConnGlobalNumSetupsAborted': {},
     'cufwConnNumAborted': {},
     'cufwConnNumActive': {},
     'cufwConnNumAttempted': {},
     'cufwConnNumHalfOpen': {},
     'cufwConnNumPolicyDeclined': {},
     'cufwConnNumResDeclined': {},
     'cufwConnNumSetupsAborted': {},
     'cufwConnReptAppStats': {},
     'cufwConnReptAppStatsLastChanged': {},
     'cufwConnResActiveConnMemoryUsage': {},
     'cufwConnResEmbrConnMemoryUsage': {},
     'cufwConnResHOConnMemoryUsage': {},
     'cufwConnResMemoryUsage': {},
     'cufwConnSetupRate1': {},
     'cufwConnSetupRate5': {},
     'cufwInspectionStatus': {},
     'cufwL2GlobalArpCacheSize': {},
     'cufwL2GlobalArpOverflowRate5': {},
     'cufwL2GlobalEnableArpInspection': {},
     'cufwL2GlobalEnableStealthMode': {},
     'cufwL2GlobalNumArpRequests': {},
     'cufwL2GlobalNumBadArpResponses': {},
     'cufwL2GlobalNumDrops': {},
     'cufwL2GlobalNumFloods': {},
     'cufwL2GlobalNumIcmpRequests': {},
     'cufwL2GlobalNumSpoofedArpResps': {},
     'cufwPolAppConnNumAborted': {},
     'cufwPolAppConnNumActive': {},
     'cufwPolAppConnNumAttempted': {},
     'cufwPolAppConnNumHalfOpen': {},
     'cufwPolAppConnNumPolicyDeclined': {},
     'cufwPolAppConnNumResDeclined': {},
     'cufwPolAppConnNumSetupsAborted': {},
     'cufwPolConnNumAborted': {},
     'cufwPolConnNumActive': {},
     'cufwPolConnNumAttempted': {},
     'cufwPolConnNumHalfOpen': {},
     'cufwPolConnNumPolicyDeclined': {},
     'cufwPolConnNumResDeclined': {},
     'cufwPolConnNumSetupsAborted': {},
     'cufwUrlfAllowModeReqNumAllowed': {},
     'cufwUrlfAllowModeReqNumDenied': {},
     'cufwUrlfFunctionEnabled': {},
     'cufwUrlfNumServerRetries': {},
     'cufwUrlfNumServerTimeouts': {},
     'cufwUrlfRequestsDeniedRate1': {},
     'cufwUrlfRequestsDeniedRate5': {},
     'cufwUrlfRequestsNumAllowed': {},
     'cufwUrlfRequestsNumCacheAllowed': {},
     'cufwUrlfRequestsNumCacheDenied': {},
     'cufwUrlfRequestsNumDenied': {},
     'cufwUrlfRequestsNumProcessed': {},
     'cufwUrlfRequestsNumResDropped': {},
     'cufwUrlfRequestsProcRate1': {},
     'cufwUrlfRequestsProcRate5': {},
     'cufwUrlfRequestsResDropRate1': {},
     'cufwUrlfRequestsResDropRate5': {},
     'cufwUrlfResTotalRequestCacheSize': {},
     'cufwUrlfResTotalRespCacheSize': {},
     'cufwUrlfResponsesNumLate': {},
     'cufwUrlfServerAvgRespTime1': {},
     'cufwUrlfServerAvgRespTime5': {},
     'cufwUrlfServerNumRetries': {},
     'cufwUrlfServerNumTimeouts': {},
     'cufwUrlfServerReqsNumAllowed': {},
     'cufwUrlfServerReqsNumDenied': {},
     'cufwUrlfServerReqsNumProcessed': {},
     'cufwUrlfServerRespsNumLate': {},
     'cufwUrlfServerRespsNumReceived': {},
     'cufwUrlfServerStatus': {},
     'cufwUrlfServerVendor': {},
     'cufwUrlfUrlAccRespsNumResDropped': {},
     'cvActiveCallStatsAvgVal': {},
     'cvActiveCallStatsMaxVal': {},
     'cvActiveCallWMValue': {},
     'cvActiveCallWMts': {},
     'cvBasic': {'1': {}, '2': {}, '3': {}},
     'cvCallActiveACOMLevel': {},
     'cvCallActiveAccountCode': {},
     'cvCallActiveCallId': {},
     'cvCallActiveCallerIDBlock': {},
     'cvCallActiveCallingName': {},
     'cvCallActiveCoderTypeRate': {},
     'cvCallActiveConnectionId': {},
     'cvCallActiveDS0s': {},
     'cvCallActiveDS0sHighNotifyEnable': {},
     'cvCallActiveDS0sHighThreshold': {},
     'cvCallActiveDS0sLowNotifyEnable': {},
     'cvCallActiveDS0sLowThreshold': {},
     'cvCallActiveERLLevel': {},
     'cvCallActiveERLLevelRev1': {},
     'cvCallActiveEcanReflectorLocation': {},
     'cvCallActiveFaxTxDuration': {},
     'cvCallActiveImgPageCount': {},
     'cvCallActiveInSignalLevel': {},
     'cvCallActiveNoiseLevel': {},
     'cvCallActiveOutSignalLevel': {},
     'cvCallActiveSessionTarget': {},
     'cvCallActiveTxDuration': {},
     'cvCallActiveVoiceTxDuration': {},
     'cvCallDurationStatsAvgVal': {},
     'cvCallDurationStatsMaxVal': {},
     'cvCallDurationStatsThreshold': {},
     'cvCallHistoryACOMLevel': {},
     'cvCallHistoryAccountCode': {},
     'cvCallHistoryCallId': {},
     'cvCallHistoryCallerIDBlock': {},
     'cvCallHistoryCallingName': {},
     'cvCallHistoryCoderTypeRate': {},
     'cvCallHistoryConnectionId': {},
     'cvCallHistoryFaxTxDuration': {},
     'cvCallHistoryImgPageCount': {},
     'cvCallHistoryNoiseLevel': {},
     'cvCallHistorySessionTarget': {},
     'cvCallHistoryTxDuration': {},
     'cvCallHistoryVoiceTxDuration': {},
     'cvCallLegRateStatsAvgVal': {},
     'cvCallLegRateStatsMaxVal': {},
     'cvCallLegRateWMValue': {},
     'cvCallLegRateWMts': {},
     'cvCallRate': {},
     'cvCallRateHiWaterMark': {},
     'cvCallRateMonitorEnable': {},
     'cvCallRateMonitorTime': {},
     'cvCallRateStatsAvgVal': {},
     'cvCallRateStatsMaxVal': {},
     'cvCallRateWMValue': {},
     'cvCallRateWMts': {},
     'cvCallVolConnActiveConnection': {},
     'cvCallVolConnMaxCallConnectionLicenese': {},
     'cvCallVolConnTotalActiveConnections': {},
     'cvCallVolMediaIncomingCalls': {},
     'cvCallVolMediaOutgoingCalls': {},
     'cvCallVolPeerIncomingCalls': {},
     'cvCallVolPeerOutgoingCalls': {},
     'cvCallVolumeWMTableSize': {},
     'cvCommonDcCallActiveCallerIDBlock': {},
     'cvCommonDcCallActiveCallingName': {},
     'cvCommonDcCallActiveCodecBytes': {},
     'cvCommonDcCallActiveCoderTypeRate': {},
     'cvCommonDcCallActiveConnectionId': {},
     'cvCommonDcCallActiveInBandSignaling': {},
     'cvCommonDcCallActiveVADEnable': {},
     'cvCommonDcCallHistoryCallerIDBlock': {},
     'cvCommonDcCallHistoryCallingName': {},
     'cvCommonDcCallHistoryCodecBytes': {},
     'cvCommonDcCallHistoryCoderTypeRate': {},
     'cvCommonDcCallHistoryConnectionId': {},
     'cvCommonDcCallHistoryInBandSignaling': {},
     'cvCommonDcCallHistoryVADEnable': {},
     'cvForwNeighborEntry': {'4': {}, '5': {}, '6': {}, '7': {}, '8': {}, '9': {}},
     'cvForwRouteEntry': {'10': {},
                          '11': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'cvForwarding': {'1': {},
                      '2': {},
                      '3': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {}},
     'cvGeneralDSCPPolicyNotificationEnable': {},
     'cvGeneralFallbackNotificationEnable': {},
     'cvGeneralMediaPolicyNotificationEnable': {},
     'cvGeneralPoorQoVNotificationEnable': {},
     'cvIfCfgEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'cvIfConfigEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'cvIfCountInEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '25': {},
                          '26': {},
                          '27': {},
                          '28': {},
                          '29': {},
                          '3': {},
                          '30': {},
                          '31': {},
                          '32': {},
                          '33': {},
                          '34': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'cvIfCountOutEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '16': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '20': {},
                           '21': {},
                           '22': {},
                           '23': {},
                           '24': {},
                           '25': {},
                           '26': {},
                           '27': {},
                           '28': {},
                           '29': {},
                           '3': {},
                           '30': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'cvInterfaceVnetTrunkEnabled': {},
     'cvInterfaceVnetVrfList': {},
     'cvPeerCfgIfIndex': {},
     'cvPeerCfgPeerType': {},
     'cvPeerCfgRowStatus': {},
     'cvPeerCfgType': {},
     'cvPeerCommonCfgApplicationName': {},
     'cvPeerCommonCfgDnisMappingName': {},
     'cvPeerCommonCfgHuntStop': {},
     'cvPeerCommonCfgIncomingDnisDigits': {},
     'cvPeerCommonCfgMaxConnections': {},
     'cvPeerCommonCfgPreference': {},
     'cvPeerCommonCfgSourceCarrierId': {},
     'cvPeerCommonCfgSourceTrunkGrpLabel': {},
     'cvPeerCommonCfgTargetCarrierId': {},
     'cvPeerCommonCfgTargetTrunkGrpLabel': {},
     'cvSipMsgRateStatsAvgVal': {},
     'cvSipMsgRateStatsMaxVal': {},
     'cvSipMsgRateWMValue': {},
     'cvSipMsgRateWMts': {},
     'cvTotal': {'1': {},
                 '10': {},
                 '11': {},
                 '12': {},
                 '13': {},
                 '14': {},
                 '15': {},
                 '16': {},
                 '17': {},
                 '18': {},
                 '19': {},
                 '2': {},
                 '20': {},
                 '21': {},
                 '22': {},
                 '23': {},
                 '24': {},
                 '25': {},
                 '3': {},
                 '4': {},
                 '5': {},
                 '6': {},
                 '7': {},
                 '8': {},
                 '9': {}},
     'cvVnetTrunkNotifEnable': {},
     'cvVoIPCallActiveBitRates': {},
     'cvVoIPCallActiveCRC': {},
     'cvVoIPCallActiveCallId': {},
     'cvVoIPCallActiveCallReferenceId': {},
     'cvVoIPCallActiveChannels': {},
     'cvVoIPCallActiveCoderMode': {},
     'cvVoIPCallActiveCoderTypeRate': {},
     'cvVoIPCallActiveConnectionId': {},
     'cvVoIPCallActiveEarlyPackets': {},
     'cvVoIPCallActiveEncap': {},
     'cvVoIPCallActiveEntry': {'46': {}},
     'cvVoIPCallActiveGapFillWithInterpolation': {},
     'cvVoIPCallActiveGapFillWithPrediction': {},
     'cvVoIPCallActiveGapFillWithRedundancy': {},
     'cvVoIPCallActiveGapFillWithSilence': {},
     'cvVoIPCallActiveHiWaterPlayoutDelay': {},
     'cvVoIPCallActiveInterleaving': {},
     'cvVoIPCallActiveJBufferNominalDelay': {},
     'cvVoIPCallActiveLatePackets': {},
     'cvVoIPCallActiveLoWaterPlayoutDelay': {},
     'cvVoIPCallActiveLostPackets': {},
     'cvVoIPCallActiveMaxPtime': {},
     'cvVoIPCallActiveModeChgNeighbor': {},
     'cvVoIPCallActiveModeChgPeriod': {},
     'cvVoIPCallActiveMosQe': {},
     'cvVoIPCallActiveOctetAligned': {},
     'cvVoIPCallActiveOnTimeRvPlayout': {},
     'cvVoIPCallActiveOutOfOrder': {},
     'cvVoIPCallActiveProtocolCallId': {},
     'cvVoIPCallActivePtime': {},
     'cvVoIPCallActiveReceiveDelay': {},
     'cvVoIPCallActiveRemMediaIPAddr': {},
     'cvVoIPCallActiveRemMediaIPAddrT': {},
     'cvVoIPCallActiveRemMediaPort': {},
     'cvVoIPCallActiveRemSigIPAddr': {},
     'cvVoIPCallActiveRemSigIPAddrT': {},
     'cvVoIPCallActiveRemSigPort': {},
     'cvVoIPCallActiveRemoteIPAddress': {},
     'cvVoIPCallActiveRemoteUDPPort': {},
     'cvVoIPCallActiveReversedDirectionPeerAddress': {},
     'cvVoIPCallActiveRobustSorting': {},
     'cvVoIPCallActiveRoundTripDelay': {},
     'cvVoIPCallActiveSRTPEnable': {},
     'cvVoIPCallActiveSelectedQoS': {},
     'cvVoIPCallActiveSessionProtocol': {},
     'cvVoIPCallActiveSessionTarget': {},
     'cvVoIPCallActiveTotalPacketLoss': {},
     'cvVoIPCallActiveUsername': {},
     'cvVoIPCallActiveVADEnable': {},
     'cvVoIPCallHistoryBitRates': {},
     'cvVoIPCallHistoryCRC': {},
     'cvVoIPCallHistoryCallId': {},
     'cvVoIPCallHistoryCallReferenceId': {},
     'cvVoIPCallHistoryChannels': {},
     'cvVoIPCallHistoryCoderMode': {},
     'cvVoIPCallHistoryCoderTypeRate': {},
     'cvVoIPCallHistoryConnectionId': {},
     'cvVoIPCallHistoryEarlyPackets': {},
     'cvVoIPCallHistoryEncap': {},
     'cvVoIPCallHistoryEntry': {'48': {}},
     'cvVoIPCallHistoryFallbackDelay': {},
     'cvVoIPCallHistoryFallbackIcpif': {},
     'cvVoIPCallHistoryFallbackLoss': {},
     'cvVoIPCallHistoryGapFillWithInterpolation': {},
     'cvVoIPCallHistoryGapFillWithPrediction': {},
     'cvVoIPCallHistoryGapFillWithRedundancy': {},
     'cvVoIPCallHistoryGapFillWithSilence': {},
     'cvVoIPCallHistoryHiWaterPlayoutDelay': {},
     'cvVoIPCallHistoryIcpif': {},
     'cvVoIPCallHistoryInterleaving': {},
     'cvVoIPCallHistoryJBufferNominalDelay': {},
     'cvVoIPCallHistoryLatePackets': {},
     'cvVoIPCallHistoryLoWaterPlayoutDelay': {},
     'cvVoIPCallHistoryLostPackets': {},
     'cvVoIPCallHistoryMaxPtime': {},
     'cvVoIPCallHistoryModeChgNeighbor': {},
     'cvVoIPCallHistoryModeChgPeriod': {},
     'cvVoIPCallHistoryMosQe': {},
     'cvVoIPCallHistoryOctetAligned': {},
     'cvVoIPCallHistoryOnTimeRvPlayout': {},
     'cvVoIPCallHistoryOutOfOrder': {},
     'cvVoIPCallHistoryProtocolCallId': {},
     'cvVoIPCallHistoryPtime': {},
     'cvVoIPCallHistoryReceiveDelay': {},
     'cvVoIPCallHistoryRemMediaIPAddr': {},
     'cvVoIPCallHistoryRemMediaIPAddrT': {},
     'cvVoIPCallHistoryRemMediaPort': {},
     'cvVoIPCallHistoryRemSigIPAddr': {},
     'cvVoIPCallHistoryRemSigIPAddrT': {},
     'cvVoIPCallHistoryRemSigPort': {},
     'cvVoIPCallHistoryRemoteIPAddress': {},
     'cvVoIPCallHistoryRemoteUDPPort': {},
     'cvVoIPCallHistoryRobustSorting': {},
     'cvVoIPCallHistoryRoundTripDelay': {},
     'cvVoIPCallHistorySRTPEnable': {},
     'cvVoIPCallHistorySelectedQoS': {},
     'cvVoIPCallHistorySessionProtocol': {},
     'cvVoIPCallHistorySessionTarget': {},
     'cvVoIPCallHistoryTotalPacketLoss': {},
     'cvVoIPCallHistoryUsername': {},
     'cvVoIPCallHistoryVADEnable': {},
     'cvVoIPPeerCfgBitRate': {},
     'cvVoIPPeerCfgBitRates': {},
     'cvVoIPPeerCfgCRC': {},
     'cvVoIPPeerCfgCoderBytes': {},
     'cvVoIPPeerCfgCoderMode': {},
     'cvVoIPPeerCfgCoderRate': {},
     'cvVoIPPeerCfgCodingMode': {},
     'cvVoIPPeerCfgDSCPPolicyNotificationEnable': {},
     'cvVoIPPeerCfgDesiredQoS': {},
     'cvVoIPPeerCfgDesiredQoSVideo': {},
     'cvVoIPPeerCfgDigitRelay': {},
     'cvVoIPPeerCfgExpectFactor': {},
     'cvVoIPPeerCfgFaxBytes': {},
     'cvVoIPPeerCfgFaxRate': {},
     'cvVoIPPeerCfgFrameSize': {},
     'cvVoIPPeerCfgIPPrecedence': {},
     'cvVoIPPeerCfgIcpif': {},
     'cvVoIPPeerCfgInBandSignaling': {},
     'cvVoIPPeerCfgMediaPolicyNotificationEnable': {},
     'cvVoIPPeerCfgMediaSetting': {},
     'cvVoIPPeerCfgMinAcceptableQoS': {},
     'cvVoIPPeerCfgMinAcceptableQoSVideo': {},
     'cvVoIPPeerCfgOctetAligned': {},
     'cvVoIPPeerCfgPoorQoVNotificationEnable': {},
     'cvVoIPPeerCfgRedirectip2ip': {},
     'cvVoIPPeerCfgSessionProtocol': {},
     'cvVoIPPeerCfgSessionTarget': {},
     'cvVoIPPeerCfgTechPrefix': {},
     'cvVoIPPeerCfgUDPChecksumEnable': {},
     'cvVoIPPeerCfgVADEnable': {},
     'cvVoicePeerCfgCasGroup': {},
     'cvVoicePeerCfgDIDCallEnable': {},
     'cvVoicePeerCfgDialDigitsPrefix': {},
     'cvVoicePeerCfgEchoCancellerTest': {},
     'cvVoicePeerCfgForwardDigits': {},
     'cvVoicePeerCfgRegisterE164': {},
     'cvVoicePeerCfgSessionTarget': {},
     'cvVrfIfNotifEnable': {},
     'cvVrfInterfaceRowStatus': {},
     'cvVrfInterfaceStorageType': {},
     'cvVrfInterfaceType': {},
     'cvVrfInterfaceVnetTagOverride': {},
     'cvVrfListRowStatus': {},
     'cvVrfListStorageType': {},
     'cvVrfListVrfIndex': {},
     'cvVrfName': {},
     'cvVrfOperStatus': {},
     'cvVrfRouteDistProt': {},
     'cvVrfRowStatus': {},
     'cvVrfStorageType': {},
     'cvVrfVnetTag': {},
     'cvaIfCfgImpedance': {},
     'cvaIfCfgIntegratedDSP': {},
     'cvaIfEMCfgDialType': {},
     'cvaIfEMCfgEntry': {'7': {}},
     'cvaIfEMCfgLmrECap': {},
     'cvaIfEMCfgLmrMCap': {},
     'cvaIfEMCfgOperation': {},
     'cvaIfEMCfgSignalType': {},
     'cvaIfEMCfgType': {},
     'cvaIfEMInSeizureActive': {},
     'cvaIfEMOutSeizureActive': {},
     'cvaIfEMTimeoutLmrTeardown': {},
     'cvaIfEMTimingClearWaitDuration': {},
     'cvaIfEMTimingDelayStart': {},
     'cvaIfEMTimingDigitDuration': {},
     'cvaIfEMTimingEntry': {'13': {}, '14': {}, '15': {}},
     'cvaIfEMTimingInterDigitDuration': {},
     'cvaIfEMTimingMaxDelayDuration': {},
     'cvaIfEMTimingMaxWinkDuration': {},
     'cvaIfEMTimingMaxWinkWaitDuration': {},
     'cvaIfEMTimingMinDelayPulseWidth': {},
     'cvaIfEMTimingPulseInterDigitDuration': {},
     'cvaIfEMTimingPulseRate': {},
     'cvaIfEMTimingVoiceHangover': {},
     'cvaIfFXOCfgDialType': {},
     'cvaIfFXOCfgNumberRings': {},
     'cvaIfFXOCfgSignalType': {},
     'cvaIfFXOCfgSupDisconnect': {},
     'cvaIfFXOCfgSupDisconnect2': {},
     'cvaIfFXOHookStatus': {},
     'cvaIfFXORingDetect': {},
     'cvaIfFXORingGround': {},
     'cvaIfFXOTimingDigitDuration': {},
     'cvaIfFXOTimingInterDigitDuration': {},
     'cvaIfFXOTimingPulseInterDigitDuration': {},
     'cvaIfFXOTimingPulseRate': {},
     'cvaIfFXOTipGround': {},
     'cvaIfFXSCfgSignalType': {},
     'cvaIfFXSHookStatus': {},
     'cvaIfFXSRingActive': {},
     'cvaIfFXSRingFrequency': {},
     'cvaIfFXSRingGround': {},
     'cvaIfFXSTimingDigitDuration': {},
     'cvaIfFXSTimingInterDigitDuration': {},
     'cvaIfFXSTipGround': {},
     'cvaIfMaintenanceMode': {},
     'cvaIfStatusInfoType': {},
     'cvaIfStatusSignalErrors': {},
     'cviRoutedVlanIfIndex': {},
     'cvpdnDeniedUsersTotal': {},
     'cvpdnSessionATOTimeouts': {},
     'cvpdnSessionAdaptiveTimeOut': {},
     'cvpdnSessionAttrBytesIn': {},
     'cvpdnSessionAttrBytesOut': {},
     'cvpdnSessionAttrCallDuration': {},
     'cvpdnSessionAttrDS1ChannelIndex': {},
     'cvpdnSessionAttrDS1PortIndex': {},
     'cvpdnSessionAttrDS1SlotIndex': {},
     'cvpdnSessionAttrDeviceCallerId': {},
     'cvpdnSessionAttrDevicePhyId': {},
     'cvpdnSessionAttrDeviceType': {},
     'cvpdnSessionAttrEntry': {'20': {}, '21': {}, '22': {}, '23': {}, '24': {}},
     'cvpdnSessionAttrModemCallStartIndex': {},
     'cvpdnSessionAttrModemCallStartTime': {},
     'cvpdnSessionAttrModemPortIndex': {},
     'cvpdnSessionAttrModemSlotIndex': {},
     'cvpdnSessionAttrMultilink': {},
     'cvpdnSessionAttrPacketsIn': {},
     'cvpdnSessionAttrPacketsOut': {},
     'cvpdnSessionAttrState': {},
     'cvpdnSessionAttrUserName': {},
     'cvpdnSessionCalculationType': {},
     'cvpdnSessionCurrentWindowSize': {},
     'cvpdnSessionInterfaceName': {},
     'cvpdnSessionLastChange': {},
     'cvpdnSessionLocalWindowSize': {},
     'cvpdnSessionMinimumWindowSize': {},
     'cvpdnSessionOutGoingQueueSize': {},
     'cvpdnSessionOutOfOrderPackets': {},
     'cvpdnSessionPktProcessingDelay': {},
     'cvpdnSessionRecvRBits': {},
     'cvpdnSessionRecvSequence': {},
     'cvpdnSessionRecvZLB': {},
     'cvpdnSessionRemoteId': {},
     'cvpdnSessionRemoteRecvSequence': {},
     'cvpdnSessionRemoteSendSequence': {},
     'cvpdnSessionRemoteWindowSize': {},
     'cvpdnSessionRoundTripTime': {},
     'cvpdnSessionSendSequence': {},
     'cvpdnSessionSentRBits': {},
     'cvpdnSessionSentZLB': {},
     'cvpdnSessionSequencing': {},
     'cvpdnSessionTotal': {},
     'cvpdnSessionZLBTime': {},
     'cvpdnSystemDeniedUsersTotal': {},
     'cvpdnSystemInfo': {'5': {}, '6': {}},
     'cvpdnSystemSessionTotal': {},
     'cvpdnSystemTunnelTotal': {},
     'cvpdnTunnelActiveSessions': {},
     'cvpdnTunnelAttrActiveSessions': {},
     'cvpdnTunnelAttrDeniedUsers': {},
     'cvpdnTunnelAttrEntry': {'16': {},
                              '17': {},
                              '18': {},
                              '19': {},
                              '20': {},
                              '21': {}},
     'cvpdnTunnelAttrLocalInitConnection': {},
     'cvpdnTunnelAttrLocalIpAddress': {},
     'cvpdnTunnelAttrLocalName': {},
     'cvpdnTunnelAttrNetworkServiceType': {},
     'cvpdnTunnelAttrOrigCause': {},
     'cvpdnTunnelAttrRemoteEndpointName': {},
     'cvpdnTunnelAttrRemoteIpAddress': {},
     'cvpdnTunnelAttrRemoteName': {},
     'cvpdnTunnelAttrRemoteTunnelId': {},
     'cvpdnTunnelAttrSoftshut': {},
     'cvpdnTunnelAttrSourceIpAddress': {},
     'cvpdnTunnelAttrState': {},
     'cvpdnTunnelBytesIn': {},
     'cvpdnTunnelBytesOut': {},
     'cvpdnTunnelDeniedUsers': {},
     'cvpdnTunnelExtEntry': {'8': {}, '9': {}},
     'cvpdnTunnelLastChange': {},
     'cvpdnTunnelLocalInitConnection': {},
     'cvpdnTunnelLocalIpAddress': {},
     'cvpdnTunnelLocalName': {},
     'cvpdnTunnelLocalPort': {},
     'cvpdnTunnelNetworkServiceType': {},
     'cvpdnTunnelOrigCause': {},
     'cvpdnTunnelPacketsIn': {},
     'cvpdnTunnelPacketsOut': {},
     'cvpdnTunnelRemoteEndpointName': {},
     'cvpdnTunnelRemoteIpAddress': {},
     'cvpdnTunnelRemoteName': {},
     'cvpdnTunnelRemotePort': {},
     'cvpdnTunnelRemoteTunnelId': {},
     'cvpdnTunnelSessionBytesIn': {},
     'cvpdnTunnelSessionBytesOut': {},
     'cvpdnTunnelSessionCallDuration': {},
     'cvpdnTunnelSessionDS1ChannelIndex': {},
     'cvpdnTunnelSessionDS1PortIndex': {},
     'cvpdnTunnelSessionDS1SlotIndex': {},
     'cvpdnTunnelSessionDeviceCallerId': {},
     'cvpdnTunnelSessionDevicePhyId': {},
     'cvpdnTunnelSessionDeviceType': {},
     'cvpdnTunnelSessionModemCallStartIndex': {},
     'cvpdnTunnelSessionModemCallStartTime': {},
     'cvpdnTunnelSessionModemPortIndex': {},
     'cvpdnTunnelSessionModemSlotIndex': {},
     'cvpdnTunnelSessionMultilink': {},
     'cvpdnTunnelSessionPacketsIn': {},
     'cvpdnTunnelSessionPacketsOut': {},
     'cvpdnTunnelSessionState': {},
     'cvpdnTunnelSessionUserName': {},
     'cvpdnTunnelSoftshut': {},
     'cvpdnTunnelSourceIpAddress': {},
     'cvpdnTunnelState': {},
     'cvpdnTunnelTotal': {},
     'cvpdnUnameToFailHistCount': {},
     'cvpdnUnameToFailHistDestIp': {},
     'cvpdnUnameToFailHistFailReason': {},
     'cvpdnUnameToFailHistFailTime': {},
     'cvpdnUnameToFailHistFailType': {},
     'cvpdnUnameToFailHistLocalInitConn': {},
     'cvpdnUnameToFailHistLocalName': {},
     'cvpdnUnameToFailHistRemoteName': {},
     'cvpdnUnameToFailHistSourceIp': {},
     'cvpdnUnameToFailHistUserId': {},
     'cvpdnUserToFailHistInfoEntry': {'13': {}, '14': {}, '15': {}, '16': {}},
     'ddp': {'1': {},
             '10': {},
             '11': {},
             '12': {},
             '13': {},
             '14': {},
             '2': {},
             '3': {},
             '4': {},
             '5': {},
             '6': {},
             '7': {},
             '8': {},
             '9': {}},
     'demandNbrAcceptCalls': {},
     'demandNbrAddress': {},
     'demandNbrCallOrigin': {},
     'demandNbrClearCode': {},
     'demandNbrClearReason': {},
     'demandNbrFailCalls': {},
     'demandNbrLastAttemptTime': {},
     'demandNbrLastDuration': {},
     'demandNbrLogIf': {},
     'demandNbrMaxDuration': {},
     'demandNbrName': {},
     'demandNbrPermission': {},
     'demandNbrRefuseCalls': {},
     'demandNbrStatus': {},
     'demandNbrSuccessCalls': {},
     'dialCtlAcceptMode': {},
     'dialCtlPeerCfgAnswerAddress': {},
     'dialCtlPeerCfgCallRetries': {},
     'dialCtlPeerCfgCarrierDelay': {},
     'dialCtlPeerCfgFailureDelay': {},
     'dialCtlPeerCfgIfType': {},
     'dialCtlPeerCfgInactivityTimer': {},
     'dialCtlPeerCfgInfoType': {},
     'dialCtlPeerCfgLowerIf': {},
     'dialCtlPeerCfgMaxDuration': {},
     'dialCtlPeerCfgMinDuration': {},
     'dialCtlPeerCfgOriginateAddress': {},
     'dialCtlPeerCfgPermission': {},
     'dialCtlPeerCfgRetryDelay': {},
     'dialCtlPeerCfgSpeed': {},
     'dialCtlPeerCfgStatus': {},
     'dialCtlPeerCfgSubAddress': {},
     'dialCtlPeerCfgTrapEnable': {},
     'dialCtlPeerStatsAcceptCalls': {},
     'dialCtlPeerStatsChargedUnits': {},
     'dialCtlPeerStatsConnectTime': {},
     'dialCtlPeerStatsFailCalls': {},
     'dialCtlPeerStatsLastDisconnectCause': {},
     'dialCtlPeerStatsLastDisconnectText': {},
     'dialCtlPeerStatsLastSetupTime': {},
     'dialCtlPeerStatsRefuseCalls': {},
     'dialCtlPeerStatsSuccessCalls': {},
     'dialCtlTrapEnable': {},
     'diffServAction': {'1': {}, '4': {}},
     'diffServActionEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'diffServAlgDrop': {'1': {}, '3': {}},
     'diffServAlgDropEntry': {'10': {},
                              '11': {},
                              '12': {},
                              '2': {},
                              '3': {},
                              '4': {},
                              '5': {},
                              '6': {},
                              '7': {},
                              '8': {},
                              '9': {}},
     'diffServClassifier': {'1': {}, '3': {}, '5': {}},
     'diffServClfrElementEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'diffServClfrEntry': {'2': {}, '3': {}},
     'diffServCountActEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'diffServDataPathEntry': {'2': {}, '3': {}, '4': {}},
     'diffServDscpMarkActEntry': {'1': {}},
     'diffServMaxRateEntry': {'3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'diffServMeter': {'1': {}},
     'diffServMeterEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'diffServMinRateEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'diffServMultiFieldClfrEntry': {'10': {},
                                     '11': {},
                                     '12': {},
                                     '13': {},
                                     '14': {},
                                     '15': {},
                                     '2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {},
                                     '9': {}},
     'diffServQEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'diffServQueue': {'1': {}},
     'diffServRandomDropEntry': {'10': {},
                                 '2': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {},
                                 '9': {}},
     'diffServScheduler': {'1': {}, '3': {}, '5': {}},
     'diffServSchedulerEntry': {'2': {},
                                '3': {},
                                '4': {},
                                '5': {},
                                '6': {},
                                '7': {}},
     'diffServTBParam': {'1': {}},
     'diffServTBParamEntry': {'2': {},
                              '3': {},
                              '4': {},
                              '5': {},
                              '6': {},
                              '7': {}},
     'dlswCircuitEntry': {'10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '25': {},
                          '26': {},
                          '27': {},
                          '28': {},
                          '29': {},
                          '3': {},
                          '30': {},
                          '31': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {}},
     'dlswCircuitStat': {'1': {}, '2': {}},
     'dlswDirLocateMacEntry': {'3': {}},
     'dlswDirLocateNBEntry': {'3': {}},
     'dlswDirMacEntry': {'2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'dlswDirNBEntry': {'2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'dlswDirStat': {'1': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {}},
     'dlswIfEntry': {'1': {}, '2': {}, '3': {}},
     'dlswNode': {'1': {},
                  '2': {},
                  '3': {},
                  '4': {},
                  '5': {},
                  '6': {},
                  '7': {},
                  '8': {},
                  '9': {}},
     'dlswSdlc': {'1': {}},
     'dlswSdlcLsEntry': {'1': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {}},
     'dlswTConnConfigEntry': {'10': {},
                              '11': {},
                              '12': {},
                              '13': {},
                              '2': {},
                              '3': {},
                              '4': {},
                              '5': {},
                              '6': {},
                              '7': {},
                              '8': {},
                              '9': {}},
     'dlswTConnOperEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '2': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '26': {},
                            '27': {},
                            '28': {},
                            '29': {},
                            '30': {},
                            '31': {},
                            '32': {},
                            '33': {},
                            '34': {},
                            '35': {},
                            '36': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'dlswTConnStat': {'1': {}, '2': {}, '3': {}},
     'dlswTConnTcpConfigEntry': {'1': {}, '2': {}, '3': {}},
     'dlswTConnTcpOperEntry': {'1': {}, '2': {}, '3': {}},
     'dlswTrapControl': {'1': {}, '2': {}, '3': {}, '4': {}},
     'dnAreaTableEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {}},
     'dnHostTableEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {}},
     'dnIfTableEntry': {'1': {}},
     'dot1agCfmConfigErrorListErrorType': {},
     'dot1agCfmDefaultMdDefIdPermission': {},
     'dot1agCfmDefaultMdDefLevel': {},
     'dot1agCfmDefaultMdDefMhfCreation': {},
     'dot1agCfmDefaultMdIdPermission': {},
     'dot1agCfmDefaultMdLevel': {},
     'dot1agCfmDefaultMdMhfCreation': {},
     'dot1agCfmDefaultMdStatus': {},
     'dot1agCfmLtrChassisId': {},
     'dot1agCfmLtrChassisIdSubtype': {},
     'dot1agCfmLtrEgress': {},
     'dot1agCfmLtrEgressMac': {},
     'dot1agCfmLtrEgressPortId': {},
     'dot1agCfmLtrEgressPortIdSubtype': {},
     'dot1agCfmLtrForwarded': {},
     'dot1agCfmLtrIngress': {},
     'dot1agCfmLtrIngressMac': {},
     'dot1agCfmLtrIngressPortId': {},
     'dot1agCfmLtrIngressPortIdSubtype': {},
     'dot1agCfmLtrLastEgressIdentifier': {},
     'dot1agCfmLtrManAddress': {},
     'dot1agCfmLtrManAddressDomain': {},
     'dot1agCfmLtrNextEgressIdentifier': {},
     'dot1agCfmLtrOrganizationSpecificTlv': {},
     'dot1agCfmLtrRelay': {},
     'dot1agCfmLtrTerminalMep': {},
     'dot1agCfmLtrTtl': {},
     'dot1agCfmMaCompIdPermission': {},
     'dot1agCfmMaCompMhfCreation': {},
     'dot1agCfmMaCompNumberOfVids': {},
     'dot1agCfmMaCompPrimaryVlanId': {},
     'dot1agCfmMaCompRowStatus': {},
     'dot1agCfmMaMepListRowStatus': {},
     'dot1agCfmMaNetCcmInterval': {},
     'dot1agCfmMaNetFormat': {},
     'dot1agCfmMaNetName': {},
     'dot1agCfmMaNetRowStatus': {},
     'dot1agCfmMdFormat': {},
     'dot1agCfmMdMaNextIndex': {},
     'dot1agCfmMdMdLevel': {},
     'dot1agCfmMdMhfCreation': {},
     'dot1agCfmMdMhfIdPermission': {},
     'dot1agCfmMdName': {},
     'dot1agCfmMdRowStatus': {},
     'dot1agCfmMdTableNextIndex': {},
     'dot1agCfmMepActive': {},
     'dot1agCfmMepCciEnabled': {},
     'dot1agCfmMepCciSentCcms': {},
     'dot1agCfmMepCcmLtmPriority': {},
     'dot1agCfmMepCcmSequenceErrors': {},
     'dot1agCfmMepDbChassisId': {},
     'dot1agCfmMepDbChassisIdSubtype': {},
     'dot1agCfmMepDbInterfaceStatusTlv': {},
     'dot1agCfmMepDbMacAddress': {},
     'dot1agCfmMepDbManAddress': {},
     'dot1agCfmMepDbManAddressDomain': {},
     'dot1agCfmMepDbPortStatusTlv': {},
     'dot1agCfmMepDbRMepFailedOkTime': {},
     'dot1agCfmMepDbRMepState': {},
     'dot1agCfmMepDbRdi': {},
     'dot1agCfmMepDefects': {},
     'dot1agCfmMepDirection': {},
     'dot1agCfmMepErrorCcmLastFailure': {},
     'dot1agCfmMepFngAlarmTime': {},
     'dot1agCfmMepFngResetTime': {},
     'dot1agCfmMepFngState': {},
     'dot1agCfmMepHighestPrDefect': {},
     'dot1agCfmMepIfIndex': {},
     'dot1agCfmMepLbrBadMsdu': {},
     'dot1agCfmMepLbrIn': {},
     'dot1agCfmMepLbrInOutOfOrder': {},
     'dot1agCfmMepLbrOut': {},
     'dot1agCfmMepLowPrDef': {},
     'dot1agCfmMepLtmNextSeqNumber': {},
     'dot1agCfmMepMacAddress': {},
     'dot1agCfmMepNextLbmTransId': {},
     'dot1agCfmMepPrimaryVid': {},
     'dot1agCfmMepRowStatus': {},
     'dot1agCfmMepTransmitLbmDataTlv': {},
     'dot1agCfmMepTransmitLbmDestIsMepId': {},
     'dot1agCfmMepTransmitLbmDestMacAddress': {},
     'dot1agCfmMepTransmitLbmDestMepId': {},
     'dot1agCfmMepTransmitLbmMessages': {},
     'dot1agCfmMepTransmitLbmResultOK': {},
     'dot1agCfmMepTransmitLbmSeqNumber': {},
     'dot1agCfmMepTransmitLbmStatus': {},
     'dot1agCfmMepTransmitLbmVlanDropEnable': {},
     'dot1agCfmMepTransmitLbmVlanPriority': {},
     'dot1agCfmMepTransmitLtmEgressIdentifier': {},
     'dot1agCfmMepTransmitLtmFlags': {},
     'dot1agCfmMepTransmitLtmResult': {},
     'dot1agCfmMepTransmitLtmSeqNumber': {},
     'dot1agCfmMepTransmitLtmStatus': {},
     'dot1agCfmMepTransmitLtmTargetIsMepId': {},
     'dot1agCfmMepTransmitLtmTargetMacAddress': {},
     'dot1agCfmMepTransmitLtmTargetMepId': {},
     'dot1agCfmMepTransmitLtmTtl': {},
     'dot1agCfmMepUnexpLtrIn': {},
     'dot1agCfmMepXconCcmLastFailure': {},
     'dot1agCfmStackMaIndex': {},
     'dot1agCfmStackMacAddress': {},
     'dot1agCfmStackMdIndex': {},
     'dot1agCfmStackMepId': {},
     'dot1agCfmVlanPrimaryVid': {},
     'dot1agCfmVlanRowStatus': {},
     'dot1dBase': {'1': {}, '2': {}, '3': {}},
     'dot1dBasePortEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'dot1dSrPortEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'dot1dStaticEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'dot1dStp': {'1': {},
                  '10': {},
                  '11': {},
                  '12': {},
                  '13': {},
                  '14': {},
                  '2': {},
                  '3': {},
                  '4': {},
                  '5': {},
                  '6': {},
                  '7': {},
                  '8': {},
                  '9': {}},
     'dot1dStpPortEntry': {'1': {},
                           '10': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'dot1dTp': {'1': {}, '2': {}},
     'dot1dTpFdbEntry': {'1': {}, '2': {}, '3': {}},
     'dot1dTpPortEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'dot10.196.1.1': {},
     'dot10.196.1.2': {},
     'dot10.196.1.3': {},
     'dot10.196.1.4': {},
     'dot10.196.1.5': {},
     'dot10.196.1.6': {},
     'dot3CollEntry': {'3': {}},
     'dot3ControlEntry': {'1': {}, '2': {}, '3': {}},
     'dot3PauseEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'dot3StatsEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '13': {},
                        '16': {},
                        '17': {},
                        '18': {},
                        '19': {},
                        '2': {},
                        '20': {},
                        '21': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'dot3adAggActorAdminKey': {},
     'dot3adAggActorOperKey': {},
     'dot3adAggActorSystemID': {},
     'dot3adAggActorSystemPriority': {},
     'dot3adAggAggregateOrIndividual': {},
     'dot3adAggCollectorMaxDelay': {},
     'dot3adAggMACAddress': {},
     'dot3adAggPartnerOperKey': {},
     'dot3adAggPartnerSystemID': {},
     'dot3adAggPartnerSystemPriority': {},
     'dot3adAggPortActorAdminKey': {},
     'dot3adAggPortActorAdminState': {},
     'dot3adAggPortActorOperKey': {},
     'dot3adAggPortActorOperState': {},
     'dot3adAggPortActorPort': {},
     'dot3adAggPortActorPortPriority': {},
     'dot3adAggPortActorSystemID': {},
     'dot3adAggPortActorSystemPriority': {},
     'dot3adAggPortAggregateOrIndividual': {},
     'dot3adAggPortAttachedAggID': {},
     'dot3adAggPortDebugActorChangeCount': {},
     'dot3adAggPortDebugActorChurnCount': {},
     'dot3adAggPortDebugActorChurnState': {},
     'dot3adAggPortDebugActorSyncTransitionCount': {},
     'dot3adAggPortDebugLastRxTime': {},
     'dot3adAggPortDebugMuxReason': {},
     'dot3adAggPortDebugMuxState': {},
     'dot3adAggPortDebugPartnerChangeCount': {},
     'dot3adAggPortDebugPartnerChurnCount': {},
     'dot3adAggPortDebugPartnerChurnState': {},
     'dot3adAggPortDebugPartnerSyncTransitionCount': {},
     'dot3adAggPortDebugRxState': {},
     'dot3adAggPortListPorts': {},
     'dot3adAggPortPartnerAdminKey': {},
     'dot3adAggPortPartnerAdminPort': {},
     'dot3adAggPortPartnerAdminPortPriority': {},
     'dot3adAggPortPartnerAdminState': {},
     'dot3adAggPortPartnerAdminSystemID': {},
     'dot3adAggPortPartnerAdminSystemPriority': {},
     'dot3adAggPortPartnerOperKey': {},
     'dot3adAggPortPartnerOperPort': {},
     'dot3adAggPortPartnerOperPortPriority': {},
     'dot3adAggPortPartnerOperState': {},
     'dot3adAggPortPartnerOperSystemID': {},
     'dot3adAggPortPartnerOperSystemPriority': {},
     'dot3adAggPortSelectedAggID': {},
     'dot3adAggPortStatsIllegalRx': {},
     'dot3adAggPortStatsLACPDUsRx': {},
     'dot3adAggPortStatsLACPDUsTx': {},
     'dot3adAggPortStatsMarkerPDUsRx': {},
     'dot3adAggPortStatsMarkerPDUsTx': {},
     'dot3adAggPortStatsMarkerResponsePDUsRx': {},
     'dot3adAggPortStatsMarkerResponsePDUsTx': {},
     'dot3adAggPortStatsUnknownRx': {},
     'dot3adTablesLastChanged': {},
     'dot5Entry': {'1': {},
                   '2': {},
                   '3': {},
                   '4': {},
                   '5': {},
                   '6': {},
                   '7': {},
                   '8': {},
                   '9': {}},
     'dot5StatsEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '14': {},
                        '15': {},
                        '16': {},
                        '17': {},
                        '18': {},
                        '19': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'ds10.121.1.1': {},
     'ds10.121.1.10': {},
     'ds10.121.1.11': {},
     'ds10.121.1.12': {},
     'ds10.121.1.13': {},
     'ds10.121.1.2': {},
     'ds10.121.1.3': {},
     'ds10.121.1.4': {},
     'ds10.121.1.5': {},
     'ds10.121.1.6': {},
     'ds10.121.1.7': {},
     'ds10.121.1.8': {},
     'ds10.121.1.9': {},
     'ds10.144.1.1': {},
     'ds10.144.1.10': {},
     'ds10.144.1.11': {},
     'ds10.144.1.12': {},
     'ds10.144.1.2': {},
     'ds10.144.1.3': {},
     'ds10.144.1.4': {},
     'ds10.144.1.5': {},
     'ds10.144.1.6': {},
     'ds10.144.1.7': {},
     'ds10.144.1.8': {},
     'ds10.144.1.9': {},
     'ds10.169.1.1': {},
     'ds10.169.1.10': {},
     'ds10.169.1.2': {},
     'ds10.169.1.3': {},
     'ds10.169.1.4': {},
     'ds10.169.1.5': {},
     'ds10.169.1.6': {},
     'ds10.169.1.7': {},
     'ds10.169.1.8': {},
     'ds10.169.1.9': {},
     'ds10.34.1.1': {},
     'ds10.169.1.8': {},
     'ds10.196.1.7': {},
     'dspuLuAdminEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'dspuLuOperEntry': {'2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'dspuNode': {'1': {},
                  '10': {},
                  '2': {},
                  '3': {},
                  '4': {},
                  '5': {},
                  '6': {},
                  '7': {},
                  '8': {},
                  '9': {}},
     'dspuPoolClassEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'dspuPooledLuEntry': {'1': {}, '2': {}},
     'dspuPuAdminEntry': {'10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'dspuPuOperEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '2': {},
                         '20': {},
                         '21': {},
                         '22': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'dspuPuStatsEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'dspuSapEntry': {'2': {}, '6': {}, '7': {}},
     'dsx1ConfigEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '2': {},
                         '20': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'dsx1CurrentEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'dsx1FracEntry': {'1': {}, '2': {}, '3': {}},
     'dsx1IntervalEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'dsx1TotalEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'dsx3ConfigEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'dsx3CurrentEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'dsx3FracEntry': {'1': {}, '2': {}, '3': {}},
     'dsx3IntervalEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'dsx3TotalEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'entAliasMappingEntry': {'2': {}},
     'entLPMappingEntry': {'1': {}},
     'entLastInconsistencyDetectTime': {},
     'entLogicalEntry': {'2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {}},
     'entPhySensorOperStatus': {},
     'entPhySensorPrecision': {},
     'entPhySensorScale': {},
     'entPhySensorType': {},
     'entPhySensorUnitsDisplay': {},
     'entPhySensorValue': {},
     'entPhySensorValueTimeStamp': {},
     'entPhySensorValueUpdateRate': {},
     'entPhysicalContainsEntry': {'1': {}},
     'entPhysicalEntry': {'10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'entSensorMeasuredEntity': {},
     'entSensorPrecision': {},
     'entSensorScale': {},
     'entSensorStatus': {},
     'entSensorThresholdEvaluation': {},
     'entSensorThresholdNotificationEnable': {},
     'entSensorThresholdRelation': {},
     'entSensorThresholdSeverity': {},
     'entSensorThresholdValue': {},
     'entSensorType': {},
     'entSensorValue': {},
     'entSensorValueTimeStamp': {},
     'entSensorValueUpdateRate': {},
     'entStateTable.1.1': {},
     'entStateTable.1.2': {},
     'entStateTable.1.3': {},
     'entStateTable.1.4': {},
     'entStateTable.1.5': {},
     'entStateTable.1.6': {},
     'enterprises.310.49.6.10.10.25.1.1': {},
     'enterprises.310.49.6.1.10.4.1.2': {},
     'enterprises.310.49.6.1.10.4.1.3': {},
     'enterprises.310.49.6.1.10.4.1.4': {},
     'enterprises.310.49.6.1.10.4.1.5': {},
     'enterprises.310.49.6.1.10.4.1.6': {},
     'enterprises.310.49.6.1.10.4.1.7': {},
     'enterprises.310.49.6.1.10.4.1.8': {},
     'enterprises.310.49.6.1.10.4.1.9': {},
     'enterprises.310.49.6.1.10.9.1.1': {},
     'enterprises.310.49.6.1.10.9.1.10': {},
     'enterprises.310.49.6.1.10.9.1.11': {},
     'enterprises.310.49.6.1.10.9.1.12': {},
     'enterprises.310.49.6.1.10.9.1.13': {},
     'enterprises.310.49.6.1.10.9.1.14': {},
     'enterprises.310.49.6.1.10.9.1.2': {},
     'enterprises.310.49.6.1.10.9.1.3': {},
     'enterprises.310.49.6.1.10.9.1.4': {},
     'enterprises.310.49.6.1.10.9.1.5': {},
     'enterprises.310.49.6.1.10.9.1.6': {},
     'enterprises.310.49.6.1.10.9.1.7': {},
     'enterprises.310.49.6.1.10.9.1.8': {},
     'enterprises.310.49.6.1.10.9.1.9': {},
     'enterprises.310.49.6.1.10.16.1.10': {},
     'enterprises.310.49.6.1.10.16.1.11': {},
     'enterprises.310.49.6.1.10.16.1.12': {},
     'enterprises.310.49.6.1.10.16.1.13': {},
     'enterprises.310.49.6.1.10.16.1.14': {},
     'enterprises.310.49.6.1.10.16.1.3': {},
     'enterprises.310.49.6.1.10.16.1.4': {},
     'enterprises.310.49.6.1.10.16.1.5': {},
     'enterprises.310.49.6.1.10.16.1.6': {},
     'enterprises.310.49.6.1.10.16.1.7': {},
     'enterprises.310.49.6.1.10.16.1.8': {},
     'enterprises.310.49.6.1.10.16.1.9': {},
     'entityGeneral': {'1': {}},
     'etherWisDeviceRxTestPatternErrors': {},
     'etherWisDeviceRxTestPatternMode': {},
     'etherWisDeviceTxTestPatternMode': {},
     'etherWisFarEndPathCurrentStatus': {},
     'etherWisPathCurrentJ1Received': {},
     'etherWisPathCurrentJ1Transmitted': {},
     'etherWisPathCurrentStatus': {},
     'etherWisSectionCurrentJ0Received': {},
     'etherWisSectionCurrentJ0Transmitted': {},
     'eventEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'faAdmProhibited': {},
     'faCOAStatus': {},
     'faEncapsulationUnavailable': {},
     'faHAAuthenticationFailure': {},
     'faHAUnreachable': {},
     'faInsufficientResource': {},
     'faMNAuthenticationFailure': {},
     'faPoorlyFormedReplies': {},
     'faPoorlyFormedRequests': {},
     'faReasonUnspecified': {},
     'faRegLifetimeTooLong': {},
     'faRegRepliesRecieved': {},
     'faRegRepliesRelayed': {},
     'faRegRequestsReceived': {},
     'faRegRequestsRelayed': {},
     'faVisitorHomeAddress': {},
     'faVisitorHomeAgentAddress': {},
     'faVisitorIPAddress': {},
     'faVisitorRegFlags': {},
     'faVisitorRegIDHigh': {},
     'faVisitorRegIDLow': {},
     'faVisitorRegIsAccepted': {},
     'faVisitorTimeGranted': {},
     'faVisitorTimeRemaining': {},
     'frCircuitEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '14': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'frDlcmiEntry': {'1': {},
                      '10': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'frTrapState': {},
     'frasBanLlc': {},
     'frasBanSdlc': {},
     'frasBnnLlc': {},
     'frasBnnSdlc': {},
     'haAdmProhibited': {},
     'haDeRegRepliesSent': {},
     'haDeRegRequestsReceived': {},
     'haFAAuthenticationFailure': {},
     'haGratuitiousARPsSent': {},
     'haIDMismatch': {},
     'haInsufficientResource': {},
     'haMNAuthenticationFailure': {},
     'haMobilityBindingCOA': {},
     'haMobilityBindingMN': {},
     'haMobilityBindingRegFlags': {},
     'haMobilityBindingRegIDHigh': {},
     'haMobilityBindingRegIDLow': {},
     'haMobilityBindingSourceAddress': {},
     'haMobilityBindingTimeGranted': {},
     'haMobilityBindingTimeRemaining': {},
     'haMultiBindingUnsupported': {},
     'haOverallServiceTime': {},
     'haPoorlyFormedRequest': {},
     'haProxyARPsSent': {},
     'haReasonUnspecified': {},
     'haRecentServiceAcceptedTime': {},
     'haRecentServiceDeniedCode': {},
     'haRecentServiceDeniedTime': {},
     'haRegRepliesSent': {},
     'haRegRequestsReceived': {},
     'haRegistrationAccepted': {},
     'haServiceRequestsAccepted': {},
     'haServiceRequestsDenied': {},
     'haTooManyBindings': {},
     'haUnknownHA': {},
     'hcAlarmAbsValue': {},
     'hcAlarmCapabilities': {},
     'hcAlarmFallingEventIndex': {},
     'hcAlarmFallingThreshAbsValueHi': {},
     'hcAlarmFallingThreshAbsValueLo': {},
     'hcAlarmFallingThresholdValStatus': {},
     'hcAlarmInterval': {},
     'hcAlarmOwner': {},
     'hcAlarmRisingEventIndex': {},
     'hcAlarmRisingThreshAbsValueHi': {},
     'hcAlarmRisingThreshAbsValueLo': {},
     'hcAlarmRisingThresholdValStatus': {},
     'hcAlarmSampleType': {},
     'hcAlarmStartupAlarm': {},
     'hcAlarmStatus': {},
     'hcAlarmStorageType': {},
     'hcAlarmValueFailedAttempts': {},
     'hcAlarmValueStatus': {},
     'hcAlarmVariable': {},
     'icmp': {'1': {},
              '10': {},
              '11': {},
              '12': {},
              '13': {},
              '14': {},
              '15': {},
              '16': {},
              '17': {},
              '18': {},
              '19': {},
              '2': {},
              '20': {},
              '21': {},
              '22': {},
              '23': {},
              '24': {},
              '25': {},
              '26': {},
              '3': {},
              '4': {},
              '5': {},
              '6': {},
              '7': {},
              '8': {},
              '9': {}},
     'icmpMsgStatsEntry': {'3': {}, '4': {}},
     'icmpStatsEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'ieee8021CfmConfigErrorListErrorType': {},
     'ieee8021CfmDefaultMdIdPermission': {},
     'ieee8021CfmDefaultMdLevel': {},
     'ieee8021CfmDefaultMdMhfCreation': {},
     'ieee8021CfmDefaultMdStatus': {},
     'ieee8021CfmMaCompIdPermission': {},
     'ieee8021CfmMaCompMhfCreation': {},
     'ieee8021CfmMaCompNumberOfVids': {},
     'ieee8021CfmMaCompPrimarySelectorOrNone': {},
     'ieee8021CfmMaCompPrimarySelectorType': {},
     'ieee8021CfmMaCompRowStatus': {},
     'ieee8021CfmStackMaIndex': {},
     'ieee8021CfmStackMacAddress': {},
     'ieee8021CfmStackMdIndex': {},
     'ieee8021CfmStackMepId': {},
     'ieee8021CfmVlanPrimarySelector': {},
     'ieee8021CfmVlanRowStatus': {},
     'ifAdminStatus': {},
     'ifAlias': {},
     'ifConnectorPresent': {},
     'ifCounterDiscontinuityTime': {},
     'ifDescr': {},
     'ifHCInBroadcastPkts': {},
     'ifHCInMulticastPkts': {},
     'ifHCInOctets': {},
     'ifHCInUcastPkts': {},
     'ifHCOutBroadcastPkts': {},
     'ifHCOutMulticastPkts': {},
     'ifHCOutOctets': {},
     'ifHCOutUcastPkts': {},
     'ifHighSpeed': {},
     'ifInBroadcastPkts': {},
     'ifInDiscards': {},
     'ifInErrors': {},
     'ifInMulticastPkts': {},
     'ifInNUcastPkts': {},
     'ifInOctets': {},
     'ifInUcastPkts': {},
     'ifInUnknownProtos': {},
     'ifIndex': {},
     'ifLastChange': {},
     'ifLinkUpDownTrapEnable': {},
     'ifMtu': {},
     'ifName': {},
     'ifNumber': {},
     'ifOperStatus': {},
     'ifOutBroadcastPkts': {},
     'ifOutDiscards': {},
     'ifOutErrors': {},
     'ifOutMulticastPkts': {},
     'ifOutNUcastPkts': {},
     'ifOutOctets': {},
     'ifOutQLen': {},
     'ifOutUcastPkts': {},
     'ifPhysAddress': {},
     'ifPromiscuousMode': {},
     'ifRcvAddressStatus': {},
     'ifRcvAddressType': {},
     'ifSpecific': {},
     'ifSpeed': {},
     'ifStackLastChange': {},
     'ifStackStatus': {},
     'ifTableLastChange': {},
     'ifTestCode': {},
     'ifTestId': {},
     'ifTestOwner': {},
     'ifTestResult': {},
     'ifTestStatus': {},
     'ifTestType': {},
     'ifType': {},
     'igmpCacheEntry': {'3': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'igmpInterfaceEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'inetCidrRouteEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'intSrvFlowEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '2': {},
                         '20': {},
                         '21': {},
                         '22': {},
                         '23': {},
                         '24': {},
                         '25': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'intSrvGenObjects': {'1': {}},
     'intSrvGuaranteedIfEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'intSrvIfAttribEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'ip': {'1': {},
            '10': {},
            '11': {},
            '12': {},
            '13': {},
            '14': {},
            '15': {},
            '16': {},
            '17': {},
            '18': {},
            '19': {},
            '2': {},
            '23': {},
            '25': {},
            '26': {},
            '27': {},
            '29': {},
            '3': {},
            '33': {},
            '38': {},
            '4': {},
            '5': {},
            '6': {},
            '7': {},
            '8': {},
            '9': {}},
     'ipAddrEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ipAddressEntry': {'10': {},
                        '11': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'ipAddressPrefixEntry': {'5': {}, '6': {}, '7': {}, '8': {}, '9': {}},
     'ipCidrRouteEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'ipDefaultRouterEntry': {'4': {}, '5': {}},
     'ipForward': {'3': {}, '6': {}},
     'ipIfStatsEntry': {'10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '14': {},
                        '15': {},
                        '16': {},
                        '17': {},
                        '18': {},
                        '19': {},
                        '20': {},
                        '21': {},
                        '23': {},
                        '24': {},
                        '25': {},
                        '26': {},
                        '27': {},
                        '28': {},
                        '29': {},
                        '3': {},
                        '30': {},
                        '31': {},
                        '32': {},
                        '33': {},
                        '34': {},
                        '35': {},
                        '36': {},
                        '37': {},
                        '38': {},
                        '39': {},
                        '4': {},
                        '40': {},
                        '41': {},
                        '42': {},
                        '43': {},
                        '44': {},
                        '45': {},
                        '46': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'ipMRoute': {'1': {}, '7': {}},
     'ipMRouteBoundaryEntry': {'4': {}},
     'ipMRouteEntry': {'10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '15': {},
                       '16': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'ipMRouteInterfaceEntry': {'2': {},
                                '3': {},
                                '4': {},
                                '5': {},
                                '6': {},
                                '7': {},
                                '8': {}},
     'ipMRouteNextHopEntry': {'10': {},
                              '11': {},
                              '6': {},
                              '7': {},
                              '8': {},
                              '9': {}},
     'ipMRouteScopeNameEntry': {'4': {}, '5': {}, '6': {}},
     'ipNetToMediaEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'ipNetToPhysicalEntry': {'4': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'ipSystemStatsEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '26': {},
                            '27': {},
                            '28': {},
                            '29': {},
                            '3': {},
                            '30': {},
                            '31': {},
                            '32': {},
                            '33': {},
                            '34': {},
                            '35': {},
                            '36': {},
                            '37': {},
                            '38': {},
                            '39': {},
                            '4': {},
                            '40': {},
                            '41': {},
                            '42': {},
                            '43': {},
                            '44': {},
                            '45': {},
                            '46': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'ipTrafficStats': {'2': {}},
     'ipslaEtherJAggMaxSucFrmLoss': {},
     'ipslaEtherJAggMeasuredAvgJ': {},
     'ipslaEtherJAggMeasuredAvgJDS': {},
     'ipslaEtherJAggMeasuredAvgJSD': {},
     'ipslaEtherJAggMeasuredAvgLossDenominatorDS': {},
     'ipslaEtherJAggMeasuredAvgLossDenominatorSD': {},
     'ipslaEtherJAggMeasuredAvgLossNumeratorDS': {},
     'ipslaEtherJAggMeasuredAvgLossNumeratorSD': {},
     'ipslaEtherJAggMeasuredBusies': {},
     'ipslaEtherJAggMeasuredCmpletions': {},
     'ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS': {},
     'ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD': {},
     'ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS': {},
     'ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD': {},
     'ipslaEtherJAggMeasuredCumulativeLossDenominatorDS': {},
     'ipslaEtherJAggMeasuredCumulativeLossDenominatorSD': {},
     'ipslaEtherJAggMeasuredCumulativeLossNumeratorDS': {},
     'ipslaEtherJAggMeasuredCumulativeLossNumeratorSD': {},
     'ipslaEtherJAggMeasuredErrors': {},
     'ipslaEtherJAggMeasuredFrmLateAs': {},
     'ipslaEtherJAggMeasuredFrmLossSDs': {},
     'ipslaEtherJAggMeasuredFrmLssDSes': {},
     'ipslaEtherJAggMeasuredFrmMIAes': {},
     'ipslaEtherJAggMeasuredFrmOutSeqs': {},
     'ipslaEtherJAggMeasuredFrmSkippds': {},
     'ipslaEtherJAggMeasuredFrmUnPrcds': {},
     'ipslaEtherJAggMeasuredIAJIn': {},
     'ipslaEtherJAggMeasuredIAJOut': {},
     'ipslaEtherJAggMeasuredMaxLossDenominatorDS': {},
     'ipslaEtherJAggMeasuredMaxLossDenominatorSD': {},
     'ipslaEtherJAggMeasuredMaxLossNumeratorDS': {},
     'ipslaEtherJAggMeasuredMaxLossNumeratorSD': {},
     'ipslaEtherJAggMeasuredMaxNegDS': {},
     'ipslaEtherJAggMeasuredMaxNegSD': {},
     'ipslaEtherJAggMeasuredMaxNegTW': {},
     'ipslaEtherJAggMeasuredMaxPosDS': {},
     'ipslaEtherJAggMeasuredMaxPosSD': {},
     'ipslaEtherJAggMeasuredMaxPosTW': {},
     'ipslaEtherJAggMeasuredMinLossDenominatorDS': {},
     'ipslaEtherJAggMeasuredMinLossDenominatorSD': {},
     'ipslaEtherJAggMeasuredMinLossNumeratorDS': {},
     'ipslaEtherJAggMeasuredMinLossNumeratorSD': {},
     'ipslaEtherJAggMeasuredMinNegDS': {},
     'ipslaEtherJAggMeasuredMinNegSD': {},
     'ipslaEtherJAggMeasuredMinNegTW': {},
     'ipslaEtherJAggMeasuredMinPosDS': {},
     'ipslaEtherJAggMeasuredMinPosSD': {},
     'ipslaEtherJAggMeasuredMinPosTW': {},
     'ipslaEtherJAggMeasuredNumNegDSes': {},
     'ipslaEtherJAggMeasuredNumNegSDs': {},
     'ipslaEtherJAggMeasuredNumOWs': {},
     'ipslaEtherJAggMeasuredNumOverThresh': {},
     'ipslaEtherJAggMeasuredNumPosDSes': {},
     'ipslaEtherJAggMeasuredNumPosSDs': {},
     'ipslaEtherJAggMeasuredNumRTTs': {},
     'ipslaEtherJAggMeasuredOWMaxDS': {},
     'ipslaEtherJAggMeasuredOWMaxSD': {},
     'ipslaEtherJAggMeasuredOWMinDS': {},
     'ipslaEtherJAggMeasuredOWMinSD': {},
     'ipslaEtherJAggMeasuredOWSum2DSHs': {},
     'ipslaEtherJAggMeasuredOWSum2DSLs': {},
     'ipslaEtherJAggMeasuredOWSum2SDHs': {},
     'ipslaEtherJAggMeasuredOWSum2SDLs': {},
     'ipslaEtherJAggMeasuredOWSumDSes': {},
     'ipslaEtherJAggMeasuredOWSumSDs': {},
     'ipslaEtherJAggMeasuredOvThrshlds': {},
     'ipslaEtherJAggMeasuredRTTMax': {},
     'ipslaEtherJAggMeasuredRTTMin': {},
     'ipslaEtherJAggMeasuredRTTSum2Hs': {},
     'ipslaEtherJAggMeasuredRTTSum2Ls': {},
     'ipslaEtherJAggMeasuredRTTSums': {},
     'ipslaEtherJAggMeasuredRxFrmsDS': {},
     'ipslaEtherJAggMeasuredRxFrmsSD': {},
     'ipslaEtherJAggMeasuredSum2NDSHs': {},
     'ipslaEtherJAggMeasuredSum2NDSLs': {},
     'ipslaEtherJAggMeasuredSum2NSDHs': {},
     'ipslaEtherJAggMeasuredSum2NSDLs': {},
     'ipslaEtherJAggMeasuredSum2PDSHs': {},
     'ipslaEtherJAggMeasuredSum2PDSLs': {},
     'ipslaEtherJAggMeasuredSum2PSDHs': {},
     'ipslaEtherJAggMeasuredSum2PSDLs': {},
     'ipslaEtherJAggMeasuredSumNegDSes': {},
     'ipslaEtherJAggMeasuredSumNegSDs': {},
     'ipslaEtherJAggMeasuredSumPosDSes': {},
     'ipslaEtherJAggMeasuredSumPosSDs': {},
     'ipslaEtherJAggMeasuredTxFrmsDS': {},
     'ipslaEtherJAggMeasuredTxFrmsSD': {},
     'ipslaEtherJAggMinSucFrmLoss': {},
     'ipslaEtherJLatestFrmUnProcessed': {},
     'ipslaEtherJitterLatestAvgDSJ': {},
     'ipslaEtherJitterLatestAvgJitter': {},
     'ipslaEtherJitterLatestAvgSDJ': {},
     'ipslaEtherJitterLatestFrmLateA': {},
     'ipslaEtherJitterLatestFrmLossDS': {},
     'ipslaEtherJitterLatestFrmLossSD': {},
     'ipslaEtherJitterLatestFrmMIA': {},
     'ipslaEtherJitterLatestFrmOutSeq': {},
     'ipslaEtherJitterLatestFrmSkipped': {},
     'ipslaEtherJitterLatestIAJIn': {},
     'ipslaEtherJitterLatestIAJOut': {},
     'ipslaEtherJitterLatestMaxNegDS': {},
     'ipslaEtherJitterLatestMaxNegSD': {},
     'ipslaEtherJitterLatestMaxPosDS': {},
     'ipslaEtherJitterLatestMaxPosSD': {},
     'ipslaEtherJitterLatestMaxSucFrmL': {},
     'ipslaEtherJitterLatestMinNegDS': {},
     'ipslaEtherJitterLatestMinNegSD': {},
     'ipslaEtherJitterLatestMinPosDS': {},
     'ipslaEtherJitterLatestMinPosSD': {},
     'ipslaEtherJitterLatestMinSucFrmL': {},
     'ipslaEtherJitterLatestNumNegDS': {},
     'ipslaEtherJitterLatestNumNegSD': {},
     'ipslaEtherJitterLatestNumOW': {},
     'ipslaEtherJitterLatestNumOverThresh': {},
     'ipslaEtherJitterLatestNumPosDS': {},
     'ipslaEtherJitterLatestNumPosSD': {},
     'ipslaEtherJitterLatestNumRTT': {},
     'ipslaEtherJitterLatestOWAvgDS': {},
     'ipslaEtherJitterLatestOWAvgSD': {},
     'ipslaEtherJitterLatestOWMaxDS': {},
     'ipslaEtherJitterLatestOWMaxSD': {},
     'ipslaEtherJitterLatestOWMinDS': {},
     'ipslaEtherJitterLatestOWMinSD': {},
     'ipslaEtherJitterLatestOWSum2DS': {},
     'ipslaEtherJitterLatestOWSum2SD': {},
     'ipslaEtherJitterLatestOWSumDS': {},
     'ipslaEtherJitterLatestOWSumSD': {},
     'ipslaEtherJitterLatestRTTMax': {},
     'ipslaEtherJitterLatestRTTMin': {},
     'ipslaEtherJitterLatestRTTSum': {},
     'ipslaEtherJitterLatestRTTSum2': {},
     'ipslaEtherJitterLatestSense': {},
     'ipslaEtherJitterLatestSum2NegDS': {},
     'ipslaEtherJitterLatestSum2NegSD': {},
     'ipslaEtherJitterLatestSum2PosDS': {},
     'ipslaEtherJitterLatestSum2PosSD': {},
     'ipslaEtherJitterLatestSumNegDS': {},
     'ipslaEtherJitterLatestSumNegSD': {},
     'ipslaEtherJitterLatestSumPosDS': {},
     'ipslaEtherJitterLatestSumPosSD': {},
     'ipslaEthernetGrpCtrlCOS': {},
     'ipslaEthernetGrpCtrlDomainName': {},
     'ipslaEthernetGrpCtrlDomainNameType': {},
     'ipslaEthernetGrpCtrlEntry': {'21': {}, '22': {}},
     'ipslaEthernetGrpCtrlInterval': {},
     'ipslaEthernetGrpCtrlMPIDExLst': {},
     'ipslaEthernetGrpCtrlNumFrames': {},
     'ipslaEthernetGrpCtrlOwner': {},
     'ipslaEthernetGrpCtrlProbeList': {},
     'ipslaEthernetGrpCtrlReqDataSize': {},
     'ipslaEthernetGrpCtrlRttType': {},
     'ipslaEthernetGrpCtrlStatus': {},
     'ipslaEthernetGrpCtrlStorageType': {},
     'ipslaEthernetGrpCtrlTag': {},
     'ipslaEthernetGrpCtrlThreshold': {},
     'ipslaEthernetGrpCtrlTimeout': {},
     'ipslaEthernetGrpCtrlVLAN': {},
     'ipslaEthernetGrpReactActionType': {},
     'ipslaEthernetGrpReactStatus': {},
     'ipslaEthernetGrpReactStorageType': {},
     'ipslaEthernetGrpReactThresholdCountX': {},
     'ipslaEthernetGrpReactThresholdCountY': {},
     'ipslaEthernetGrpReactThresholdFalling': {},
     'ipslaEthernetGrpReactThresholdRising': {},
     'ipslaEthernetGrpReactThresholdType': {},
     'ipslaEthernetGrpReactVar': {},
     'ipslaEthernetGrpScheduleFrequency': {},
     'ipslaEthernetGrpSchedulePeriod': {},
     'ipslaEthernetGrpScheduleRttStartTime': {},
     'ipv4InterfaceEntry': {'2': {}, '3': {}, '4': {}},
     'ipv6InterfaceEntry': {'2': {}, '3': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'ipv6RouterAdvertEntry': {'10': {},
                               '11': {},
                               '12': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {},
                               '7': {},
                               '8': {},
                               '9': {}},
     'ipv6ScopeZoneIndexEntry': {'10': {},
                                 '11': {},
                                 '12': {},
                                 '13': {},
                                 '2': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {},
                                 '9': {}},
     'ipxAdvSysEntry': {'1': {},
                        '10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'ipxBasicSysEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'ipxCircEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '22': {},
                      '23': {},
                      '24': {},
                      '25': {},
                      '26': {},
                      '27': {},
                      '28': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'ipxDestEntry': {'1': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {}},
     'ipxDestServEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {}},
     'ipxServEntry': {'1': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {}},
     'ipxStaticRouteEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'ipxStaticServEntry': {'1': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'isdnBasicRateEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'isdnBearerEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'isdnDirectoryEntry': {'2': {}, '3': {}, '4': {}},
     'isdnEndpointEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'isdnEndpointGetIndex': {},
     'isdnMib.10.16.4.1.1': {},
     'isdnMib.10.16.4.1.2': {},
     'isdnMib.10.16.4.1.3': {},
     'isdnMib.10.16.4.1.4': {},
     'isdnSignalingEntry': {'2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {}},
     'isdnSignalingGetIndex': {},
     'isdnSignalingStatsEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'lapbAdmnEntry': {'1': {},
                       '10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'lapbFlowEntry': {'1': {},
                       '10': {},
                       '11': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'lapbOperEntry': {'1': {},
                       '10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'lapbXidEntry': {'1': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {}},
     'lifEntry': {'1': {},
                  '10': {},
                  '100': {},
                  '101': {},
                  '102': {},
                  '103': {},
                  '104': {},
                  '105': {},
                  '106': {},
                  '107': {},
                  '108': {},
                  '109': {},
                  '11': {},
                  '110': {},
                  '111': {},
                  '112': {},
                  '113': {},
                  '114': {},
                  '12': {},
                  '13': {},
                  '14': {},
                  '15': {},
                  '16': {},
                  '17': {},
                  '18': {},
                  '19': {},
                  '2': {},
                  '20': {},
                  '21': {},
                  '22': {},
                  '23': {},
                  '24': {},
                  '25': {},
                  '26': {},
                  '27': {},
                  '28': {},
                  '3': {},
                  '30': {},
                  '31': {},
                  '32': {},
                  '33': {},
                  '34': {},
                  '35': {},
                  '36': {},
                  '37': {},
                  '38': {},
                  '39': {},
                  '4': {},
                  '40': {},
                  '41': {},
                  '42': {},
                  '43': {},
                  '44': {},
                  '45': {},
                  '46': {},
                  '47': {},
                  '48': {},
                  '49': {},
                  '5': {},
                  '50': {},
                  '51': {},
                  '52': {},
                  '53': {},
                  '54': {},
                  '55': {},
                  '56': {},
                  '57': {},
                  '58': {},
                  '59': {},
                  '6': {},
                  '60': {},
                  '61': {},
                  '62': {},
                  '63': {},
                  '64': {},
                  '65': {},
                  '66': {},
                  '67': {},
                  '68': {},
                  '69': {},
                  '7': {},
                  '70': {},
                  '71': {},
                  '72': {},
                  '73': {},
                  '74': {},
                  '75': {},
                  '76': {},
                  '77': {},
                  '78': {},
                  '79': {},
                  '8': {},
                  '80': {},
                  '81': {},
                  '82': {},
                  '83': {},
                  '84': {},
                  '85': {},
                  '86': {},
                  '87': {},
                  '88': {},
                  '89': {},
                  '9': {},
                  '90': {},
                  '91': {},
                  '92': {},
                  '93': {},
                  '94': {},
                  '95': {},
                  '96': {},
                  '97': {},
                  '98': {},
                  '99': {}},
     'lip': {'10': {}, '11': {}, '12': {}, '4': {}, '5': {}, '6': {}, '8': {}},
     'lipAccountEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'lipAddrEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'lipCkAccountEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'lipRouteEntry': {'1': {}, '2': {}, '3': {}},
     'lipxAccountingEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'lipxCkAccountingEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'lispConfiguredLocatorRlocLocal': {},
     'lispConfiguredLocatorRlocState': {},
     'lispConfiguredLocatorRlocTimeStamp': {},
     'lispEidRegistrationAuthenticationErrors': {},
     'lispEidRegistrationEtrLastTimeStamp': {},
     'lispEidRegistrationEtrProxyReply': {},
     'lispEidRegistrationEtrTtl': {},
     'lispEidRegistrationEtrWantsMapNotify': {},
     'lispEidRegistrationFirstTimeStamp': {},
     'lispEidRegistrationIsRegistered': {},
     'lispEidRegistrationLastRegisterSender': {},
     'lispEidRegistrationLastRegisterSenderLength': {},
     'lispEidRegistrationLastTimeStamp': {},
     'lispEidRegistrationLocatorIsLocal': {},
     'lispEidRegistrationLocatorMPriority': {},
     'lispEidRegistrationLocatorMWeight': {},
     'lispEidRegistrationLocatorPriority': {},
     'lispEidRegistrationLocatorRlocState': {},
     'lispEidRegistrationLocatorWeight': {},
     'lispEidRegistrationRlocsMismatch': {},
     'lispEidRegistrationSiteDescription': {},
     'lispEidRegistrationSiteName': {},
     'lispFeaturesEtrAcceptMapDataEnabled': {},
     'lispFeaturesEtrAcceptMapDataVerifyEnabled': {},
     'lispFeaturesEtrEnabled': {},
     'lispFeaturesEtrMapCacheTtl': {},
     'lispFeaturesItrEnabled': {},
     'lispFeaturesMapCacheLimit': {},
     'lispFeaturesMapCacheSize': {},
     'lispFeaturesMapResolverEnabled': {},
     'lispFeaturesMapServerEnabled': {},
     'lispFeaturesProxyEtrEnabled': {},
     'lispFeaturesProxyItrEnabled': {},
     'lispFeaturesRlocProbeEnabled': {},
     'lispFeaturesRouterTimeStamp': {},
     'lispGlobalStatsMapRegistersIn': {},
     'lispGlobalStatsMapRegistersOut': {},
     'lispGlobalStatsMapRepliesIn': {},
     'lispGlobalStatsMapRepliesOut': {},
     'lispGlobalStatsMapRequestsIn': {},
     'lispGlobalStatsMapRequestsOut': {},
     'lispIidToVrfName': {},
     'lispMapCacheEidAuthoritative': {},
     'lispMapCacheEidEncapOctets': {},
     'lispMapCacheEidEncapPackets': {},
     'lispMapCacheEidExpiryTime': {},
     'lispMapCacheEidState': {},
     'lispMapCacheEidTimeStamp': {},
     'lispMapCacheLocatorRlocLastMPriorityChange': {},
     'lispMapCacheLocatorRlocLastMWeightChange': {},
     'lispMapCacheLocatorRlocLastPriorityChange': {},
     'lispMapCacheLocatorRlocLastStateChange': {},
     'lispMapCacheLocatorRlocLastWeightChange': {},
     'lispMapCacheLocatorRlocMPriority': {},
     'lispMapCacheLocatorRlocMWeight': {},
     'lispMapCacheLocatorRlocPriority': {},
     'lispMapCacheLocatorRlocRtt': {},
     'lispMapCacheLocatorRlocState': {},
     'lispMapCacheLocatorRlocTimeStamp': {},
     'lispMapCacheLocatorRlocWeight': {},
     'lispMappingDatabaseEidPartitioned': {},
     'lispMappingDatabaseLocatorRlocLocal': {},
     'lispMappingDatabaseLocatorRlocMPriority': {},
     'lispMappingDatabaseLocatorRlocMWeight': {},
     'lispMappingDatabaseLocatorRlocPriority': {},
     'lispMappingDatabaseLocatorRlocState': {},
     'lispMappingDatabaseLocatorRlocTimeStamp': {},
     'lispMappingDatabaseLocatorRlocWeight': {},
     'lispMappingDatabaseLsb': {},
     'lispMappingDatabaseTimeStamp': {},
     'lispUseMapResolverState': {},
     'lispUseMapServerState': {},
     'lispUseProxyEtrMPriority': {},
     'lispUseProxyEtrMWeight': {},
     'lispUseProxyEtrPriority': {},
     'lispUseProxyEtrState': {},
     'lispUseProxyEtrWeight': {},
     'lldpLocManAddrEntry': {'3': {}, '4': {}, '5': {}, '6': {}},
     'lldpLocPortEntry': {'2': {}, '3': {}, '4': {}},
     'lldpLocalSystemData': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'lldpRemEntry': {'10': {},
                      '11': {},
                      '12': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'lldpRemManAddrEntry': {'3': {}, '4': {}, '5': {}},
     'lldpRemOrgDefInfoEntry': {'4': {}},
     'lldpRemUnknownTLVEntry': {'2': {}},
     'logEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'lsystem': {'1': {},
                 '10': {},
                 '11': {},
                 '12': {},
                 '13': {},
                 '14': {},
                 '15': {},
                 '16': {},
                 '17': {},
                 '18': {},
                 '19': {},
                 '2': {},
                 '20': {},
                 '21': {},
                 '22': {},
                 '23': {},
                 '24': {},
                 '25': {},
                 '26': {},
                 '27': {},
                 '28': {},
                 '29': {},
                 '3': {},
                 '30': {},
                 '31': {},
                 '32': {},
                 '33': {},
                 '34': {},
                 '35': {},
                 '36': {},
                 '37': {},
                 '38': {},
                 '39': {},
                 '4': {},
                 '40': {},
                 '41': {},
                 '42': {},
                 '43': {},
                 '44': {},
                 '45': {},
                 '46': {},
                 '47': {},
                 '48': {},
                 '49': {},
                 '5': {},
                 '50': {},
                 '51': {},
                 '52': {},
                 '53': {},
                 '54': {},
                 '55': {},
                 '56': {},
                 '57': {},
                 '58': {},
                 '59': {},
                 '6': {},
                 '60': {},
                 '61': {},
                 '62': {},
                 '63': {},
                 '64': {},
                 '65': {},
                 '66': {},
                 '67': {},
                 '68': {},
                 '69': {},
                 '70': {},
                 '71': {},
                 '72': {},
                 '73': {},
                 '74': {},
                 '75': {},
                 '76': {},
                 '8': {},
                 '9': {}},
     'ltcpConnEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'lts': {'1': {},
             '10': {},
             '4': {},
             '5': {},
             '6': {},
             '7': {},
             '8': {},
             '9': {}},
     'ltsLineEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'ltsLineSessionEntry': {'1': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {}},
     'maAdvAddress': {},
     'maAdvMaxAdvLifetime': {},
     'maAdvMaxInterval': {},
     'maAdvMaxRegLifetime': {},
     'maAdvMinInterval': {},
     'maAdvPrefixLengthInclusion': {},
     'maAdvResponseSolicitationOnly': {},
     'maAdvStatus': {},
     'maAdvertisementsSent': {},
     'maAdvsSentForSolicitation': {},
     'maSolicitationsReceived': {},
     'mfrBundleActivationClass': {},
     'mfrBundleBandwidth': {},
     'mfrBundleCountMaxRetry': {},
     'mfrBundleFarEndName': {},
     'mfrBundleFragmentation': {},
     'mfrBundleIfIndex': {},
     'mfrBundleIfIndexMappingIndex': {},
     'mfrBundleLinkConfigBundleIndex': {},
     'mfrBundleLinkDelay': {},
     'mfrBundleLinkFarEndBundleName': {},
     'mfrBundleLinkFarEndName': {},
     'mfrBundleLinkFramesControlInvalid': {},
     'mfrBundleLinkFramesControlRx': {},
     'mfrBundleLinkFramesControlTx': {},
     'mfrBundleLinkLoopbackSuspected': {},
     'mfrBundleLinkMismatch': {},
     'mfrBundleLinkNearEndName': {},
     'mfrBundleLinkRowStatus': {},
     'mfrBundleLinkState': {},
     'mfrBundleLinkTimerExpiredCount': {},
     'mfrBundleLinkUnexpectedSequence': {},
     'mfrBundleLinksActive': {},
     'mfrBundleLinksConfigured': {},
     'mfrBundleMaxBundleLinks': {},
     'mfrBundleMaxDiffDelay': {},
     'mfrBundleMaxFragSize': {},
     'mfrBundleMaxNumBundles': {},
     'mfrBundleNearEndName': {},
     'mfrBundleNextIndex': {},
     'mfrBundleResequencingErrors': {},
     'mfrBundleRowStatus': {},
     'mfrBundleSeqNumSize': {},
     'mfrBundleThreshold': {},
     'mfrBundleTimerAck': {},
     'mfrBundleTimerHello': {},
     'mgmdHostCacheLastReporter': {},
     'mgmdHostCacheSourceFilterMode': {},
     'mgmdHostCacheUpTime': {},
     'mgmdHostInterfaceQuerier': {},
     'mgmdHostInterfaceStatus': {},
     'mgmdHostInterfaceVersion': {},
     'mgmdHostInterfaceVersion1QuerierTimer': {},
     'mgmdHostInterfaceVersion2QuerierTimer': {},
     'mgmdHostInterfaceVersion3Robustness': {},
     'mgmdHostSrcListExpire': {},
     'mgmdInverseHostCacheAddress': {},
     'mgmdInverseRouterCacheAddress': {},
     'mgmdRouterCacheExcludeModeExpiryTimer': {},
     'mgmdRouterCacheExpiryTime': {},
     'mgmdRouterCacheLastReporter': {},
     'mgmdRouterCacheSourceFilterMode': {},
     'mgmdRouterCacheUpTime': {},
     'mgmdRouterCacheVersion1HostTimer': {},
     'mgmdRouterCacheVersion2HostTimer': {},
     'mgmdRouterInterfaceGroups': {},
     'mgmdRouterInterfaceJoins': {},
     'mgmdRouterInterfaceLastMemberQueryCount': {},
     'mgmdRouterInterfaceLastMemberQueryInterval': {},
     'mgmdRouterInterfaceProxyIfIndex': {},
     'mgmdRouterInterfaceQuerier': {},
     'mgmdRouterInterfaceQuerierExpiryTime': {},
     'mgmdRouterInterfaceQuerierUpTime': {},
     'mgmdRouterInterfaceQueryInterval': {},
     'mgmdRouterInterfaceQueryMaxResponseTime': {},
     'mgmdRouterInterfaceRobustness': {},
     'mgmdRouterInterfaceStartupQueryCount': {},
     'mgmdRouterInterfaceStartupQueryInterval': {},
     'mgmdRouterInterfaceStatus': {},
     'mgmdRouterInterfaceVersion': {},
     'mgmdRouterInterfaceWrongVersionQueries': {},
     'mgmdRouterSrcListExpire': {},
     'mib-10.49.1.1.1': {},
     'mib-10.49.1.1.2': {},
     'mib-10.49.1.1.3': {},
     'mib-10.49.1.1.4': {},
     'mib-10.49.1.1.5': {},
     'mib-10.49.1.2.1.1.3': {},
     'mib-10.49.1.2.1.1.4': {},
     'mib-10.49.1.2.1.1.5': {},
     'mib-10.49.1.2.1.1.6': {},
     'mib-10.49.1.2.1.1.7': {},
     'mib-10.49.1.2.1.1.8': {},
     'mib-10.49.1.2.1.1.9': {},
     'mib-10.49.1.2.2.1.1': {},
     'mib-10.49.1.2.2.1.2': {},
     'mib-10.49.1.2.2.1.3': {},
     'mib-10.49.1.2.2.1.4': {},
     'mib-10.49.1.2.3.1.10': {},
     'mib-10.49.1.2.3.1.2': {},
     'mib-10.49.1.2.3.1.3': {},
     'mib-10.49.1.2.3.1.4': {},
     'mib-10.49.1.2.3.1.5': {},
     'mib-10.49.1.2.3.1.6': {},
     'mib-10.49.1.2.3.1.7': {},
     'mib-10.49.1.2.3.1.8': {},
     'mib-10.49.1.2.3.1.9': {},
     'mib-10.49.1.3.1.1.2': {},
     'mib-10.49.1.3.1.1.3': {},
     'mib-10.49.1.3.1.1.4': {},
     'mib-10.49.1.3.1.1.5': {},
     'mib-10.49.1.3.1.1.6': {},
     'mib-10.49.1.3.1.1.7': {},
     'mib-10.49.1.3.1.1.8': {},
     'mib-10.49.1.3.1.1.9': {},
     'mipEnable': {},
     'mipEncapsulationSupported': {},
     'mipEntities': {},
     'mipSecAlgorithmMode': {},
     'mipSecAlgorithmType': {},
     'mipSecKey': {},
     'mipSecRecentViolationIDHigh': {},
     'mipSecRecentViolationIDLow': {},
     'mipSecRecentViolationReason': {},
     'mipSecRecentViolationSPI': {},
     'mipSecRecentViolationTime': {},
     'mipSecReplayMethod': {},
     'mipSecTotalViolations': {},
     'mipSecViolationCounter': {},
     'mipSecViolatorAddress': {},
     'mnAdvFlags': {},
     'mnAdvMaxAdvLifetime': {},
     'mnAdvMaxRegLifetime': {},
     'mnAdvSequence': {},
     'mnAdvSourceAddress': {},
     'mnAdvTimeReceived': {},
     'mnAdvertisementsReceived': {},
     'mnAdvsDroppedInvalidExtension': {},
     'mnAdvsIgnoredUnknownExtension': {},
     'mnAgentRebootsDectected': {},
     'mnCOA': {},
     'mnCOAIsLocal': {},
     'mnCurrentHA': {},
     'mnDeRegRepliesRecieved': {},
     'mnDeRegRequestsSent': {},
     'mnFAAddress': {},
     'mnGratuitousARPsSend': {},
     'mnHAStatus': {},
     'mnHomeAddress': {},
     'mnMoveFromFAToFA': {},
     'mnMoveFromFAToHA': {},
     'mnMoveFromHAToFA': {},
     'mnRegAgentAddress': {},
     'mnRegCOA': {},
     'mnRegFlags': {},
     'mnRegIDHigh': {},
     'mnRegIDLow': {},
     'mnRegIsAccepted': {},
     'mnRegRepliesRecieved': {},
     'mnRegRequestsAccepted': {},
     'mnRegRequestsDeniedByFA': {},
     'mnRegRequestsDeniedByHA': {},
     'mnRegRequestsDeniedByHADueToID': {},
     'mnRegRequestsSent': {},
     'mnRegTimeRemaining': {},
     'mnRegTimeRequested': {},
     'mnRegTimeSent': {},
     'mnRepliesDroppedInvalidExtension': {},
     'mnRepliesFAAuthenticationFailure': {},
     'mnRepliesHAAuthenticationFailure': {},
     'mnRepliesIgnoredUnknownExtension': {},
     'mnRepliesInvalidHomeAddress': {},
     'mnRepliesInvalidID': {},
     'mnRepliesUnknownFA': {},
     'mnRepliesUnknownHA': {},
     'mnSolicitationsSent': {},
     'mnState': {},
     'mplsFecAddr': {},
     'mplsFecAddrPrefixLength': {},
     'mplsFecAddrType': {},
     'mplsFecIndexNext': {},
     'mplsFecLastChange': {},
     'mplsFecRowStatus': {},
     'mplsFecStorageType': {},
     'mplsFecType': {},
     'mplsInSegmentAddrFamily': {},
     'mplsInSegmentIndexNext': {},
     'mplsInSegmentInterface': {},
     'mplsInSegmentLabel': {},
     'mplsInSegmentLabelPtr': {},
     'mplsInSegmentLdpLspLabelType': {},
     'mplsInSegmentLdpLspType': {},
     'mplsInSegmentMapIndex': {},
     'mplsInSegmentNPop': {},
     'mplsInSegmentOwner': {},
     'mplsInSegmentPerfDiscards': {},
     'mplsInSegmentPerfDiscontinuityTime': {},
     'mplsInSegmentPerfErrors': {},
     'mplsInSegmentPerfHCOctets': {},
     'mplsInSegmentPerfOctets': {},
     'mplsInSegmentPerfPackets': {},
     'mplsInSegmentRowStatus': {},
     'mplsInSegmentStorageType': {},
     'mplsInSegmentTrafficParamPtr': {},
     'mplsInSegmentXCIndex': {},
     'mplsInterfaceAvailableBandwidth': {},
     'mplsInterfaceLabelMaxIn': {},
     'mplsInterfaceLabelMaxOut': {},
     'mplsInterfaceLabelMinIn': {},
     'mplsInterfaceLabelMinOut': {},
     'mplsInterfaceLabelParticipationType': {},
     'mplsInterfacePerfInLabelLookupFailures': {},
     'mplsInterfacePerfInLabelsInUse': {},
     'mplsInterfacePerfOutFragmentedPkts': {},
     'mplsInterfacePerfOutLabelsInUse': {},
     'mplsInterfaceTotalBandwidth': {},
     'mplsL3VpnIfConfEntry': {'2': {}, '3': {}, '4': {}},
     'mplsL3VpnIfConfRowStatus': {},
     'mplsL3VpnMIB.1.1.1': {},
     'mplsL3VpnMIB.1.1.2': {},
     'mplsL3VpnMIB.1.1.3': {},
     'mplsL3VpnMIB.1.1.4': {},
     'mplsL3VpnMIB.1.1.5': {},
     'mplsL3VpnMIB.1.1.6': {},
     'mplsL3VpnMIB.1.1.7': {},
     'mplsL3VpnVrfConfHighRteThresh': {},
     'mplsL3VpnVrfConfMidRteThresh': {},
     'mplsL3VpnVrfEntry': {'11': {},
                           '12': {},
                           '13': {},
                           '14': {},
                           '15': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '7': {},
                           '8': {}},
     'mplsL3VpnVrfOperStatus': {},
     'mplsL3VpnVrfPerfCurrNumRoutes': {},
     'mplsL3VpnVrfPerfEntry': {'1': {}, '2': {}, '4': {}, '5': {}},
     'mplsL3VpnVrfRTEntry': {'4': {}, '5': {}, '6': {}, '7': {}},
     'mplsL3VpnVrfRteEntry': {'10': {},
                              '11': {},
                              '12': {},
                              '13': {},
                              '14': {},
                              '15': {},
                              '16': {},
                              '17': {},
                              '18': {},
                              '7': {},
                              '8': {},
                              '9': {}},
     'mplsL3VpnVrfSecEntry': {'2': {}},
     'mplsL3VpnVrfSecIllegalLblVltns': {},
     'mplsLabelStackIndexNext': {},
     'mplsLabelStackLabel': {},
     'mplsLabelStackLabelPtr': {},
     'mplsLabelStackRowStatus': {},
     'mplsLabelStackStorageType': {},
     'mplsLdpEntityAdminStatus': {},
     'mplsLdpEntityAtmDefaultControlVci': {},
     'mplsLdpEntityAtmDefaultControlVpi': {},
     'mplsLdpEntityAtmIfIndexOrZero': {},
     'mplsLdpEntityAtmLRComponents': {},
     'mplsLdpEntityAtmLRMaxVci': {},
     'mplsLdpEntityAtmLRMaxVpi': {},
     'mplsLdpEntityAtmLRRowStatus': {},
     'mplsLdpEntityAtmLRStorageType': {},
     'mplsLdpEntityAtmLsrConnectivity': {},
     'mplsLdpEntityAtmMergeCap': {},
     'mplsLdpEntityAtmRowStatus': {},
     'mplsLdpEntityAtmStorageType': {},
     'mplsLdpEntityAtmUnlabTrafVci': {},
     'mplsLdpEntityAtmUnlabTrafVpi': {},
     'mplsLdpEntityAtmVcDirectionality': {},
     'mplsLdpEntityDiscontinuityTime': {},
     'mplsLdpEntityGenericIfIndexOrZero': {},
     'mplsLdpEntityGenericLRRowStatus': {},
     'mplsLdpEntityGenericLRStorageType': {},
     'mplsLdpEntityGenericLabelSpace': {},
     'mplsLdpEntityHelloHoldTimer': {},
     'mplsLdpEntityHopCountLimit': {},
     'mplsLdpEntityIndexNext': {},
     'mplsLdpEntityInitSessionThreshold': {},
     'mplsLdpEntityKeepAliveHoldTimer': {},
     'mplsLdpEntityLabelDistMethod': {},
     'mplsLdpEntityLabelRetentionMode': {},
     'mplsLdpEntityLabelType': {},
     'mplsLdpEntityLastChange': {},
     'mplsLdpEntityMaxPduLength': {},
     'mplsLdpEntityOperStatus': {},
     'mplsLdpEntityPathVectorLimit': {},
     'mplsLdpEntityProtocolVersion': {},
     'mplsLdpEntityRowStatus': {},
     'mplsLdpEntityStatsBadLdpIdentifierErrors': {},
     'mplsLdpEntityStatsBadMessageLengthErrors': {},
     'mplsLdpEntityStatsBadPduLengthErrors': {},
     'mplsLdpEntityStatsBadTlvLengthErrors': {},
     'mplsLdpEntityStatsKeepAliveTimerExpErrors': {},
     'mplsLdpEntityStatsMalformedTlvValueErrors': {},
     'mplsLdpEntityStatsSessionAttempts': {},
     'mplsLdpEntityStatsSessionRejectedAdErrors': {},
     'mplsLdpEntityStatsSessionRejectedLRErrors': {},
     'mplsLdpEntityStatsSessionRejectedMaxPduErrors': {},
     'mplsLdpEntityStatsSessionRejectedNoHelloErrors': {},
     'mplsLdpEntityStatsShutdownReceivedNotifications': {},
     'mplsLdpEntityStatsShutdownSentNotifications': {},
     'mplsLdpEntityStorageType': {},
     'mplsLdpEntityTargetPeer': {},
     'mplsLdpEntityTargetPeerAddr': {},
     'mplsLdpEntityTargetPeerAddrType': {},
     'mplsLdpEntityTcpPort': {},
     'mplsLdpEntityTransportAddrKind': {},
     'mplsLdpEntityUdpDscPort': {},
     'mplsLdpHelloAdjacencyHoldTime': {},
     'mplsLdpHelloAdjacencyHoldTimeRem': {},
     'mplsLdpHelloAdjacencyType': {},
     'mplsLdpLspFecLastChange': {},
     'mplsLdpLspFecRowStatus': {},
     'mplsLdpLspFecStorageType': {},
     'mplsLdpLsrId': {},
     'mplsLdpLsrLoopDetectionCapable': {},
     'mplsLdpPeerLabelDistMethod': {},
     'mplsLdpPeerLastChange': {},
     'mplsLdpPeerPathVectorLimit': {},
     'mplsLdpPeerTransportAddr': {},
     'mplsLdpPeerTransportAddrType': {},
     'mplsLdpSessionAtmLRUpperBoundVci': {},
     'mplsLdpSessionAtmLRUpperBoundVpi': {},
     'mplsLdpSessionDiscontinuityTime': {},
     'mplsLdpSessionKeepAliveHoldTimeRem': {},
     'mplsLdpSessionKeepAliveTime': {},
     'mplsLdpSessionMaxPduLength': {},
     'mplsLdpSessionPeerNextHopAddr': {},
     'mplsLdpSessionPeerNextHopAddrType': {},
     'mplsLdpSessionProtocolVersion': {},
     'mplsLdpSessionRole': {},
     'mplsLdpSessionState': {},
     'mplsLdpSessionStateLastChange': {},
     'mplsLdpSessionStatsUnknownMesTypeErrors': {},
     'mplsLdpSessionStatsUnknownTlvErrors': {},
     'mplsLsrMIB.1.10': {},
     'mplsLsrMIB.1.11': {},
     'mplsLsrMIB.1.13': {},
     'mplsLsrMIB.1.15': {},
     'mplsLsrMIB.1.16': {},
     'mplsLsrMIB.1.17': {},
     'mplsLsrMIB.1.5': {},
     'mplsLsrMIB.1.8': {},
     'mplsMaxLabelStackDepth': {},
     'mplsOutSegmentIndexNext': {},
     'mplsOutSegmentInterface': {},
     'mplsOutSegmentLdpLspLabelType': {},
     'mplsOutSegmentLdpLspType': {},
     'mplsOutSegmentNextHopAddr': {},
     'mplsOutSegmentNextHopAddrType': {},
     'mplsOutSegmentOwner': {},
     'mplsOutSegmentPerfDiscards': {},
     'mplsOutSegmentPerfDiscontinuityTime': {},
     'mplsOutSegmentPerfErrors': {},
     'mplsOutSegmentPerfHCOctets': {},
     'mplsOutSegmentPerfOctets': {},
     'mplsOutSegmentPerfPackets': {},
     'mplsOutSegmentPushTopLabel': {},
     'mplsOutSegmentRowStatus': {},
     'mplsOutSegmentStorageType': {},
     'mplsOutSegmentTopLabel': {},
     'mplsOutSegmentTopLabelPtr': {},
     'mplsOutSegmentTrafficParamPtr': {},
     'mplsOutSegmentXCIndex': {},
     'mplsTeMIB.1.1': {},
     'mplsTeMIB.1.2': {},
     'mplsTeMIB.1.3': {},
     'mplsTeMIB.1.4': {},
     'mplsTeMIB.2.1': {},
     'mplsTeMIB.2.10': {},
     'mplsTeMIB.2.3': {},
     'mplsTeMIB.10.36.1.10': {},
     'mplsTeMIB.10.36.1.11': {},
     'mplsTeMIB.10.36.1.12': {},
     'mplsTeMIB.10.36.1.13': {},
     'mplsTeMIB.10.36.1.4': {},
     'mplsTeMIB.10.36.1.5': {},
     'mplsTeMIB.10.36.1.6': {},
     'mplsTeMIB.10.36.1.7': {},
     'mplsTeMIB.10.36.1.8': {},
     'mplsTeMIB.10.36.1.9': {},
     'mplsTeMIB.2.5': {},
     'mplsTeObjects.10.1.1': {},
     'mplsTeObjects.10.1.2': {},
     'mplsTeObjects.10.1.3': {},
     'mplsTeObjects.10.1.4': {},
     'mplsTeObjects.10.1.5': {},
     'mplsTeObjects.10.1.6': {},
     'mplsTeObjects.10.1.7': {},
     'mplsTunnelARHopEntry': {'3': {}, '4': {}, '5': {}, '6': {}},
     'mplsTunnelActive': {},
     'mplsTunnelAdminStatus': {},
     'mplsTunnelCHopEntry': {'3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'mplsTunnelConfigured': {},
     'mplsTunnelEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '20': {},
                         '21': {},
                         '22': {},
                         '23': {},
                         '24': {},
                         '25': {},
                         '26': {},
                         '27': {},
                         '28': {},
                         '29': {},
                         '30': {},
                         '31': {},
                         '32': {},
                         '33': {},
                         '36': {},
                         '37': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'mplsTunnelHopEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'mplsTunnelHopListIndexNext': {},
     'mplsTunnelIndexNext': {},
     'mplsTunnelMaxHops': {},
     'mplsTunnelNotificationEnable': {},
     'mplsTunnelNotificationMaxRate': {},
     'mplsTunnelOperStatus': {},
     'mplsTunnelPerfEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'mplsTunnelResourceEntry': {'10': {},
                                 '3': {},
                                 '4': {},
                                 '5': {},
                                 '6': {},
                                 '7': {},
                                 '8': {},
                                 '9': {}},
     'mplsTunnelResourceIndexNext': {},
     'mplsTunnelResourceMaxRate': {},
     'mplsTunnelTEDistProto': {},
     'mplsVpnInterfaceConfEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'mplsVpnMIB.1.1.1': {},
     'mplsVpnMIB.1.1.2': {},
     'mplsVpnMIB.1.1.3': {},
     'mplsVpnMIB.1.1.4': {},
     'mplsVpnMIB.1.1.5': {},
     'mplsVpnVrfBgpNbrAddrEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'mplsVpnVrfBgpNbrPrefixEntry': {'10': {},
                                     '11': {},
                                     '12': {},
                                     '13': {},
                                     '14': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {},
                                     '9': {}},
     'mplsVpnVrfConfHighRouteThreshold': {},
     'mplsVpnVrfEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {}},
     'mplsVpnVrfPerfCurrNumRoutes': {},
     'mplsVpnVrfPerfEntry': {'1': {}, '2': {}},
     'mplsVpnVrfRouteEntry': {'10': {},
                              '11': {},
                              '12': {},
                              '13': {},
                              '14': {},
                              '15': {},
                              '16': {},
                              '17': {},
                              '18': {},
                              '19': {},
                              '2': {},
                              '20': {},
                              '4': {},
                              '5': {},
                              '6': {},
                              '7': {},
                              '8': {},
                              '9': {}},
     'mplsVpnVrfRouteTargetEntry': {'4': {}, '5': {}, '6': {}},
     'mplsVpnVrfSecEntry': {'2': {}},
     'mplsVpnVrfSecIllegalLabelViolations': {},
     'mplsXCAdminStatus': {},
     'mplsXCIndexNext': {},
     'mplsXCLabelStackIndex': {},
     'mplsXCLspId': {},
     'mplsXCNotificationsEnable': {},
     'mplsXCOperStatus': {},
     'mplsXCOwner': {},
     'mplsXCRowStatus': {},
     'mplsXCStorageType': {},
     'msdp': {'1': {}, '2': {}, '3': {}, '9': {}},
     'msdpPeerEntry': {'10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '15': {},
                       '16': {},
                       '17': {},
                       '18': {},
                       '19': {},
                       '20': {},
                       '21': {},
                       '22': {},
                       '23': {},
                       '24': {},
                       '25': {},
                       '26': {},
                       '27': {},
                       '3': {},
                       '30': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'msdpSACacheEntry': {'10': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'mteEventActions': {},
     'mteEventComment': {},
     'mteEventEnabled': {},
     'mteEventEntryStatus': {},
     'mteEventFailures': {},
     'mteEventNotification': {},
     'mteEventNotificationObjects': {},
     'mteEventNotificationObjectsOwner': {},
     'mteEventSetContextName': {},
     'mteEventSetContextNameWildcard': {},
     'mteEventSetObject': {},
     'mteEventSetObjectWildcard': {},
     'mteEventSetTargetTag': {},
     'mteEventSetValue': {},
     'mteFailedReason': {},
     'mteHotContextName': {},
     'mteHotOID': {},
     'mteHotTargetName': {},
     'mteHotTrigger': {},
     'mteHotValue': {},
     'mteObjectsEntryStatus': {},
     'mteObjectsID': {},
     'mteObjectsIDWildcard': {},
     'mteResourceSampleInstanceLacks': {},
     'mteResourceSampleInstanceMaximum': {},
     'mteResourceSampleInstances': {},
     'mteResourceSampleInstancesHigh': {},
     'mteResourceSampleMinimum': {},
     'mteTriggerBooleanComparison': {},
     'mteTriggerBooleanEvent': {},
     'mteTriggerBooleanEventOwner': {},
     'mteTriggerBooleanObjects': {},
     'mteTriggerBooleanObjectsOwner': {},
     'mteTriggerBooleanStartup': {},
     'mteTriggerBooleanValue': {},
     'mteTriggerComment': {},
     'mteTriggerContextName': {},
     'mteTriggerContextNameWildcard': {},
     'mteTriggerDeltaDiscontinuityID': {},
     'mteTriggerDeltaDiscontinuityIDType': {},
     'mteTriggerDeltaDiscontinuityIDWildcard': {},
     'mteTriggerEnabled': {},
     'mteTriggerEntryStatus': {},
     'mteTriggerExistenceEvent': {},
     'mteTriggerExistenceEventOwner': {},
     'mteTriggerExistenceObjects': {},
     'mteTriggerExistenceObjectsOwner': {},
     'mteTriggerExistenceStartup': {},
     'mteTriggerExistenceTest': {},
     'mteTriggerFailures': {},
     'mteTriggerFrequency': {},
     'mteTriggerObjects': {},
     'mteTriggerObjectsOwner': {},
     'mteTriggerSampleType': {},
     'mteTriggerTargetTag': {},
     'mteTriggerTest': {},
     'mteTriggerThresholdDeltaFalling': {},
     'mteTriggerThresholdDeltaFallingEvent': {},
     'mteTriggerThresholdDeltaFallingEventOwner': {},
     'mteTriggerThresholdDeltaRising': {},
     'mteTriggerThresholdDeltaRisingEvent': {},
     'mteTriggerThresholdDeltaRisingEventOwner': {},
     'mteTriggerThresholdFalling': {},
     'mteTriggerThresholdFallingEvent': {},
     'mteTriggerThresholdFallingEventOwner': {},
     'mteTriggerThresholdObjects': {},
     'mteTriggerThresholdObjectsOwner': {},
     'mteTriggerThresholdRising': {},
     'mteTriggerThresholdRisingEvent': {},
     'mteTriggerThresholdRisingEventOwner': {},
     'mteTriggerThresholdStartup': {},
     'mteTriggerValueID': {},
     'mteTriggerValueIDWildcard': {},
     'natAddrBindCurrentIdleTime': {},
     'natAddrBindGlobalAddr': {},
     'natAddrBindGlobalAddrType': {},
     'natAddrBindId': {},
     'natAddrBindInTranslates': {},
     'natAddrBindMapIndex': {},
     'natAddrBindMaxIdleTime': {},
     'natAddrBindNumberOfEntries': {},
     'natAddrBindOutTranslates': {},
     'natAddrBindSessions': {},
     'natAddrBindTranslationEntity': {},
     'natAddrBindType': {},
     'natAddrPortBindNumberOfEntries': {},
     'natBindDefIdleTimeout': {},
     'natIcmpDefIdleTimeout': {},
     'natInterfaceDiscards': {},
     'natInterfaceInTranslates': {},
     'natInterfaceOutTranslates': {},
     'natInterfaceRealm': {},
     'natInterfaceRowStatus': {},
     'natInterfaceServiceType': {},
     'natInterfaceStorageType': {},
     'natMIBObjects.10.169.1.1': {},
     'natMIBObjects.10.169.1.2': {},
     'natMIBObjects.10.169.1.3': {},
     'natMIBObjects.10.169.1.4': {},
     'natMIBObjects.10.169.1.5': {},
     'natMIBObjects.10.169.1.6': {},
     'natMIBObjects.10.169.1.7': {},
     'natMIBObjects.10.169.1.8': {},
     'natMIBObjects.10.196.1.2': {},
     'natMIBObjects.10.196.1.3': {},
     'natMIBObjects.10.196.1.4': {},
     'natMIBObjects.10.196.1.5': {},
     'natMIBObjects.10.196.1.6': {},
     'natMIBObjects.10.196.1.7': {},
     'natOtherDefIdleTimeout': {},
     'natPoolPortMax': {},
     'natPoolPortMin': {},
     'natPoolRangeAllocations': {},
     'natPoolRangeBegin': {},
     'natPoolRangeDeallocations': {},
     'natPoolRangeEnd': {},
     'natPoolRangeType': {},
     'natPoolRealm': {},
     'natPoolWatermarkHigh': {},
     'natPoolWatermarkLow': {},
     'natTcpDefIdleTimeout': {},
     'natTcpDefNegTimeout': {},
     'natUdpDefIdleTimeout': {},
     'nbpEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'nhrpCacheHoldingTime': {},
     'nhrpCacheHoldingTimeValid': {},
     'nhrpCacheNbmaAddr': {},
     'nhrpCacheNbmaAddrType': {},
     'nhrpCacheNbmaSubaddr': {},
     'nhrpCacheNegotiatedMtu': {},
     'nhrpCacheNextHopInternetworkAddr': {},
     'nhrpCachePreference': {},
     'nhrpCachePrefixLength': {},
     'nhrpCacheRowStatus': {},
     'nhrpCacheState': {},
     'nhrpCacheStorageType': {},
     'nhrpCacheType': {},
     'nhrpClientDefaultMtu': {},
     'nhrpClientHoldTime': {},
     'nhrpClientInitialRequestTimeout': {},
     'nhrpClientInternetworkAddr': {},
     'nhrpClientInternetworkAddrType': {},
     'nhrpClientNbmaAddr': {},
     'nhrpClientNbmaAddrType': {},
     'nhrpClientNbmaSubaddr': {},
     'nhrpClientNhsInUse': {},
     'nhrpClientNhsInternetworkAddr': {},
     'nhrpClientNhsInternetworkAddrType': {},
     'nhrpClientNhsNbmaAddr': {},
     'nhrpClientNhsNbmaAddrType': {},
     'nhrpClientNhsNbmaSubaddr': {},
     'nhrpClientNhsRowStatus': {},
     'nhrpClientPurgeRequestRetries': {},
     'nhrpClientRegRowStatus': {},
     'nhrpClientRegState': {},
     'nhrpClientRegUniqueness': {},
     'nhrpClientRegistrationRequestRetries': {},
     'nhrpClientRequestID': {},
     'nhrpClientResolutionRequestRetries': {},
     'nhrpClientRowStatus': {},
     'nhrpClientStatDiscontinuityTime': {},
     'nhrpClientStatRxErrAuthenticationFailure': {},
     'nhrpClientStatRxErrHopCountExceeded': {},
     'nhrpClientStatRxErrInvalidExtension': {},
     'nhrpClientStatRxErrLoopDetected': {},
     'nhrpClientStatRxErrProtoAddrUnreachable': {},
     'nhrpClientStatRxErrProtoError': {},
     'nhrpClientStatRxErrSduSizeExceeded': {},
     'nhrpClientStatRxErrUnrecognizedExtension': {},
     'nhrpClientStatRxPurgeReply': {},
     'nhrpClientStatRxPurgeReq': {},
     'nhrpClientStatRxRegisterAck': {},
     'nhrpClientStatRxRegisterNakAlreadyReg': {},
     'nhrpClientStatRxRegisterNakInsufResources': {},
     'nhrpClientStatRxRegisterNakProhibited': {},
     'nhrpClientStatRxResolveReplyAck': {},
     'nhrpClientStatRxResolveReplyNakInsufResources': {},
     'nhrpClientStatRxResolveReplyNakNoBinding': {},
     'nhrpClientStatRxResolveReplyNakNotUnique': {},
     'nhrpClientStatRxResolveReplyNakProhibited': {},
     'nhrpClientStatTxErrorIndication': {},
     'nhrpClientStatTxPurgeReply': {},
     'nhrpClientStatTxPurgeReq': {},
     'nhrpClientStatTxRegisterReq': {},
     'nhrpClientStatTxResolveReq': {},
     'nhrpClientStorageType': {},
     'nhrpNextIndex': {},
     'nhrpPurgeCacheIdentifier': {},
     'nhrpPurgePrefixLength': {},
     'nhrpPurgeReplyExpected': {},
     'nhrpPurgeRequestID': {},
     'nhrpPurgeRowStatus': {},
     'nhrpServerCacheAuthoritative': {},
     'nhrpServerCacheUniqueness': {},
     'nhrpServerInternetworkAddr': {},
     'nhrpServerInternetworkAddrType': {},
     'nhrpServerNbmaAddr': {},
     'nhrpServerNbmaAddrType': {},
     'nhrpServerNbmaSubaddr': {},
     'nhrpServerNhcInUse': {},
     'nhrpServerNhcInternetworkAddr': {},
     'nhrpServerNhcInternetworkAddrType': {},
     'nhrpServerNhcNbmaAddr': {},
     'nhrpServerNhcNbmaAddrType': {},
     'nhrpServerNhcNbmaSubaddr': {},
     'nhrpServerNhcPrefixLength': {},
     'nhrpServerNhcRowStatus': {},
     'nhrpServerRowStatus': {},
     'nhrpServerStatDiscontinuityTime': {},
     'nhrpServerStatFwErrorIndication': {},
     'nhrpServerStatFwPurgeReply': {},
     'nhrpServerStatFwPurgeReq': {},
     'nhrpServerStatFwRegisterReply': {},
     'nhrpServerStatFwRegisterReq': {},
     'nhrpServerStatFwResolveReply': {},
     'nhrpServerStatFwResolveReq': {},
     'nhrpServerStatRxErrAuthenticationFailure': {},
     'nhrpServerStatRxErrHopCountExceeded': {},
     'nhrpServerStatRxErrInvalidExtension': {},
     'nhrpServerStatRxErrInvalidResReplyReceived': {},
     'nhrpServerStatRxErrLoopDetected': {},
     'nhrpServerStatRxErrProtoAddrUnreachable': {},
     'nhrpServerStatRxErrProtoError': {},
     'nhrpServerStatRxErrSduSizeExceeded': {},
     'nhrpServerStatRxErrUnrecognizedExtension': {},
     'nhrpServerStatRxPurgeReply': {},
     'nhrpServerStatRxPurgeReq': {},
     'nhrpServerStatRxRegisterReq': {},
     'nhrpServerStatRxResolveReq': {},
     'nhrpServerStatTxErrAuthenticationFailure': {},
     'nhrpServerStatTxErrHopCountExceeded': {},
     'nhrpServerStatTxErrInvalidExtension': {},
     'nhrpServerStatTxErrLoopDetected': {},
     'nhrpServerStatTxErrProtoAddrUnreachable': {},
     'nhrpServerStatTxErrProtoError': {},
     'nhrpServerStatTxErrSduSizeExceeded': {},
     'nhrpServerStatTxErrUnrecognizedExtension': {},
     'nhrpServerStatTxPurgeReply': {},
     'nhrpServerStatTxPurgeReq': {},
     'nhrpServerStatTxRegisterAck': {},
     'nhrpServerStatTxRegisterNakAlreadyReg': {},
     'nhrpServerStatTxRegisterNakInsufResources': {},
     'nhrpServerStatTxRegisterNakProhibited': {},
     'nhrpServerStatTxResolveReplyAck': {},
     'nhrpServerStatTxResolveReplyNakInsufResources': {},
     'nhrpServerStatTxResolveReplyNakNoBinding': {},
     'nhrpServerStatTxResolveReplyNakNotUnique': {},
     'nhrpServerStatTxResolveReplyNakProhibited': {},
     'nhrpServerStorageType': {},
     'nlmConfig': {'1': {}, '2': {}},
     'nlmConfigLogEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'nlmLogEntry': {'2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'nlmLogVariableEntry': {'10': {},
                             '11': {},
                             '12': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'nlmStats': {'1': {}, '2': {}},
     'nlmStatsLogEntry': {'1': {}, '2': {}},
     'ntpAssocAddress': {},
     'ntpAssocAddressType': {},
     'ntpAssocName': {},
     'ntpAssocOffset': {},
     'ntpAssocRefId': {},
     'ntpAssocStatInPkts': {},
     'ntpAssocStatOutPkts': {},
     'ntpAssocStatProtocolError': {},
     'ntpAssocStatusDelay': {},
     'ntpAssocStatusDispersion': {},
     'ntpAssocStatusJitter': {},
     'ntpAssocStratum': {},
     'ntpEntInfo': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'ntpEntStatus': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'ntpEntStatus.17.1.2': {},
     'ntpEntStatus.17.1.3': {},
     'ntpSnmpMIBObjects.4.1': {},
     'ntpSnmpMIBObjects.4.2': {},
     'optIfOChCurrentStatus': {},
     'optIfOChDirectionality': {},
     'optIfOChSinkCurDayHighInputPower': {},
     'optIfOChSinkCurDayLowInputPower': {},
     'optIfOChSinkCurDaySuspectedFlag': {},
     'optIfOChSinkCurrentHighInputPower': {},
     'optIfOChSinkCurrentInputPower': {},
     'optIfOChSinkCurrentLowInputPower': {},
     'optIfOChSinkCurrentLowerInputPowerThreshold': {},
     'optIfOChSinkCurrentSuspectedFlag': {},
     'optIfOChSinkCurrentUpperInputPowerThreshold': {},
     'optIfOChSinkIntervalHighInputPower': {},
     'optIfOChSinkIntervalLastInputPower': {},
     'optIfOChSinkIntervalLowInputPower': {},
     'optIfOChSinkIntervalSuspectedFlag': {},
     'optIfOChSinkPrevDayHighInputPower': {},
     'optIfOChSinkPrevDayLastInputPower': {},
     'optIfOChSinkPrevDayLowInputPower': {},
     'optIfOChSinkPrevDaySuspectedFlag': {},
     'optIfOChSrcCurDayHighOutputPower': {},
     'optIfOChSrcCurDayLowOutputPower': {},
     'optIfOChSrcCurDaySuspectedFlag': {},
     'optIfOChSrcCurrentHighOutputPower': {},
     'optIfOChSrcCurrentLowOutputPower': {},
     'optIfOChSrcCurrentLowerOutputPowerThreshold': {},
     'optIfOChSrcCurrentOutputPower': {},
     'optIfOChSrcCurrentSuspectedFlag': {},
     'optIfOChSrcCurrentUpperOutputPowerThreshold': {},
     'optIfOChSrcIntervalHighOutputPower': {},
     'optIfOChSrcIntervalLastOutputPower': {},
     'optIfOChSrcIntervalLowOutputPower': {},
     'optIfOChSrcIntervalSuspectedFlag': {},
     'optIfOChSrcPrevDayHighOutputPower': {},
     'optIfOChSrcPrevDayLastOutputPower': {},
     'optIfOChSrcPrevDayLowOutputPower': {},
     'optIfOChSrcPrevDaySuspectedFlag': {},
     'optIfODUkTtpCurrentStatus': {},
     'optIfODUkTtpDAPIExpected': {},
     'optIfODUkTtpDEGM': {},
     'optIfODUkTtpDEGThr': {},
     'optIfODUkTtpSAPIExpected': {},
     'optIfODUkTtpTIMActEnabled': {},
     'optIfODUkTtpTIMDetMode': {},
     'optIfODUkTtpTraceIdentifierAccepted': {},
     'optIfODUkTtpTraceIdentifierTransmitted': {},
     'optIfOTUk.2.1.2': {},
     'optIfOTUk.2.1.3': {},
     'optIfOTUkBitRateK': {},
     'optIfOTUkCurrentStatus': {},
     'optIfOTUkDAPIExpected': {},
     'optIfOTUkDEGM': {},
     'optIfOTUkDEGThr': {},
     'optIfOTUkDirectionality': {},
     'optIfOTUkSAPIExpected': {},
     'optIfOTUkSinkAdaptActive': {},
     'optIfOTUkSinkFECEnabled': {},
     'optIfOTUkSourceAdaptActive': {},
     'optIfOTUkTIMActEnabled': {},
     'optIfOTUkTIMDetMode': {},
     'optIfOTUkTraceIdentifierAccepted': {},
     'optIfOTUkTraceIdentifierTransmitted': {},
     'optIfObjects.10.4.1.1': {},
     'optIfObjects.10.4.1.2': {},
     'optIfObjects.10.4.1.3': {},
     'optIfObjects.10.4.1.4': {},
     'optIfObjects.10.4.1.5': {},
     'optIfObjects.10.4.1.6': {},
     'optIfObjects.10.9.1.1': {},
     'optIfObjects.10.9.1.2': {},
     'optIfObjects.10.9.1.3': {},
     'optIfObjects.10.9.1.4': {},
     'optIfObjects.10.16.1.1': {},
     'optIfObjects.10.16.1.10': {},
     'optIfObjects.10.16.1.2': {},
     'optIfObjects.10.16.1.3': {},
     'optIfObjects.10.16.1.4': {},
     'optIfObjects.10.16.1.5': {},
     'optIfObjects.10.16.1.6': {},
     'optIfObjects.10.16.1.7': {},
     'optIfObjects.10.16.1.8': {},
     'optIfObjects.10.16.1.9': {},
     'optIfObjects.10.25.1.1': {},
     'optIfObjects.10.25.1.10': {},
     'optIfObjects.10.25.1.11': {},
     'optIfObjects.10.25.1.2': {},
     'optIfObjects.10.25.1.3': {},
     'optIfObjects.10.25.1.4': {},
     'optIfObjects.10.25.1.5': {},
     'optIfObjects.10.25.1.6': {},
     'optIfObjects.10.25.1.7': {},
     'optIfObjects.10.25.1.8': {},
     'optIfObjects.10.25.1.9': {},
     'optIfObjects.10.36.1.2': {},
     'optIfObjects.10.36.1.3': {},
     'optIfObjects.10.36.1.4': {},
     'optIfObjects.10.36.1.5': {},
     'optIfObjects.10.36.1.6': {},
     'optIfObjects.10.36.1.7': {},
     'optIfObjects.10.36.1.8': {},
     'optIfObjects.10.49.1.1': {},
     'optIfObjects.10.49.1.2': {},
     'optIfObjects.10.49.1.3': {},
     'optIfObjects.10.49.1.4': {},
     'optIfObjects.10.49.1.5': {},
     'optIfObjects.10.64.1.1': {},
     'optIfObjects.10.64.1.2': {},
     'optIfObjects.10.64.1.3': {},
     'optIfObjects.10.64.1.4': {},
     'optIfObjects.10.64.1.5': {},
     'optIfObjects.10.64.1.6': {},
     'optIfObjects.10.64.1.7': {},
     'optIfObjects.10.81.1.1': {},
     'optIfObjects.10.81.1.10': {},
     'optIfObjects.10.81.1.11': {},
     'optIfObjects.10.81.1.2': {},
     'optIfObjects.10.81.1.3': {},
     'optIfObjects.10.81.1.4': {},
     'optIfObjects.10.81.1.5': {},
     'optIfObjects.10.81.1.6': {},
     'optIfObjects.10.81.1.7': {},
     'optIfObjects.10.81.1.8': {},
     'optIfObjects.10.81.1.9': {},
     'optIfObjects.10.100.1.2': {},
     'optIfObjects.10.100.1.3': {},
     'optIfObjects.10.100.1.4': {},
     'optIfObjects.10.100.1.5': {},
     'optIfObjects.10.100.1.6': {},
     'optIfObjects.10.100.1.7': {},
     'optIfObjects.10.100.1.8': {},
     'optIfObjects.10.121.1.1': {},
     'optIfObjects.10.121.1.2': {},
     'optIfObjects.10.121.1.3': {},
     'optIfObjects.10.121.1.4': {},
     'optIfObjects.10.121.1.5': {},
     'optIfObjects.10.144.1.1': {},
     'optIfObjects.10.144.1.2': {},
     'optIfObjects.10.144.1.3': {},
     'optIfObjects.10.144.1.4': {},
     'optIfObjects.10.144.1.5': {},
     'optIfObjects.10.144.1.6': {},
     'optIfObjects.10.144.1.7': {},
     'optIfObjects.10.25.1.1': {},
     'optIfObjects.10.25.1.2': {},
     'optIfObjects.10.36.1.1': {},
     'optIfObjects.10.36.1.10': {},
     'optIfObjects.10.36.1.11': {},
     'optIfObjects.10.36.1.2': {},
     'optIfObjects.10.36.1.3': {},
     'optIfObjects.10.36.1.4': {},
     'optIfObjects.10.36.1.5': {},
     'optIfObjects.10.36.1.6': {},
     'optIfObjects.10.36.1.7': {},
     'optIfObjects.10.36.1.8': {},
     'optIfObjects.10.36.1.9': {},
     'optIfObjects.10.49.1.2': {},
     'optIfObjects.10.49.1.3': {},
     'optIfObjects.10.49.1.4': {},
     'optIfObjects.10.49.1.5': {},
     'optIfObjects.10.49.1.6': {},
     'optIfObjects.10.49.1.7': {},
     'optIfObjects.10.49.1.8': {},
     'optIfObjects.10.64.1.1': {},
     'optIfObjects.10.64.1.2': {},
     'optIfObjects.10.64.1.3': {},
     'optIfObjects.10.64.1.4': {},
     'optIfObjects.10.64.1.5': {},
     'optIfObjects.10.81.1.1': {},
     'optIfObjects.10.81.1.2': {},
     'optIfObjects.10.81.1.3': {},
     'optIfObjects.10.81.1.4': {},
     'optIfObjects.10.81.1.5': {},
     'optIfObjects.10.81.1.6': {},
     'optIfObjects.10.81.1.7': {},
     'optIfObjects.10.100.1.1': {},
     'optIfObjects.10.100.1.10': {},
     'optIfObjects.10.100.1.11': {},
     'optIfObjects.10.100.1.2': {},
     'optIfObjects.10.100.1.3': {},
     'optIfObjects.10.100.1.4': {},
     'optIfObjects.10.100.1.5': {},
     'optIfObjects.10.100.1.6': {},
     'optIfObjects.10.100.1.7': {},
     'optIfObjects.10.100.1.8': {},
     'optIfObjects.10.100.1.9': {},
     'optIfObjects.10.121.1.2': {},
     'optIfObjects.10.121.1.3': {},
     'optIfObjects.10.121.1.4': {},
     'optIfObjects.10.121.1.5': {},
     'optIfObjects.10.121.1.6': {},
     'optIfObjects.10.121.1.7': {},
     'optIfObjects.10.121.1.8': {},
     'optIfObjects.10.144.1.1': {},
     'optIfObjects.10.144.1.2': {},
     'optIfObjects.10.144.1.3': {},
     'optIfObjects.10.144.1.4': {},
     'optIfObjects.10.144.1.5': {},
     'optIfObjects.10.169.1.1': {},
     'optIfObjects.10.169.1.2': {},
     'optIfObjects.10.169.1.3': {},
     'optIfObjects.10.169.1.4': {},
     'optIfObjects.10.169.1.5': {},
     'optIfObjects.10.169.1.6': {},
     'optIfObjects.10.169.1.7': {},
     'optIfObjects.10.36.1.1': {},
     'optIfObjects.10.49.1.1': {},
     'optIfObjects.10.49.1.10': {},
     'optIfObjects.10.49.1.11': {},
     'optIfObjects.10.49.1.2': {},
     'optIfObjects.10.49.1.3': {},
     'optIfObjects.10.49.1.4': {},
     'optIfObjects.10.49.1.5': {},
     'optIfObjects.10.49.1.6': {},
     'optIfObjects.10.49.1.7': {},
     'optIfObjects.10.49.1.8': {},
     'optIfObjects.10.49.1.9': {},
     'optIfObjects.10.64.1.2': {},
     'optIfObjects.10.64.1.3': {},
     'optIfObjects.10.64.1.4': {},
     'optIfObjects.10.64.1.5': {},
     'optIfObjects.10.64.1.6': {},
     'optIfObjects.10.64.1.7': {},
     'optIfObjects.10.64.1.8': {},
     'optIfObjects.10.81.1.1': {},
     'optIfObjects.10.81.1.2': {},
     'optIfObjects.10.81.1.3': {},
     'optIfObjects.10.81.1.4': {},
     'optIfObjects.10.81.1.5': {},
     'optIfObjects.10.100.1.1': {},
     'optIfObjects.10.100.1.2': {},
     'optIfObjects.10.100.1.3': {},
     'optIfObjects.10.100.1.4': {},
     'optIfObjects.10.100.1.5': {},
     'optIfObjects.10.100.1.6': {},
     'optIfObjects.10.100.1.7': {},
     'optIfObjects.10.121.1.1': {},
     'optIfObjects.10.121.1.10': {},
     'optIfObjects.10.121.1.11': {},
     'optIfObjects.10.121.1.2': {},
     'optIfObjects.10.121.1.3': {},
     'optIfObjects.10.121.1.4': {},
     'optIfObjects.10.121.1.5': {},
     'optIfObjects.10.121.1.6': {},
     'optIfObjects.10.121.1.7': {},
     'optIfObjects.10.121.1.8': {},
     'optIfObjects.10.121.1.9': {},
     'optIfObjects.10.144.1.2': {},
     'optIfObjects.10.144.1.3': {},
     'optIfObjects.10.144.1.4': {},
     'optIfObjects.10.144.1.5': {},
     'optIfObjects.10.144.1.6': {},
     'optIfObjects.10.144.1.7': {},
     'optIfObjects.10.144.1.8': {},
     'optIfObjects.10.169.1.1': {},
     'optIfObjects.10.169.1.2': {},
     'optIfObjects.10.169.1.3': {},
     'optIfObjects.10.169.1.4': {},
     'optIfObjects.10.169.1.5': {},
     'optIfObjects.10.196.1.1': {},
     'optIfObjects.10.196.1.2': {},
     'optIfObjects.10.196.1.3': {},
     'optIfObjects.10.196.1.4': {},
     'optIfObjects.10.196.1.5': {},
     'optIfObjects.10.196.1.6': {},
     'optIfObjects.10.196.1.7': {},
     'optIfObjects.10.81.1.1': {},
     'optIfObjects.10.81.1.2': {},
     'optIfObjects.10.81.1.3': {},
     'optIfObjects.10.81.1.4': {},
     'optIfObjects.10.81.1.5': {},
     'optIfObjects.10.121.1.2': {},
     'optIfObjects.10.121.1.3': {},
     'optIfObjects.10.144.1.10': {},
     'optIfObjects.10.144.1.2': {},
     'optIfObjects.10.144.1.3': {},
     'optIfObjects.10.144.1.4': {},
     'optIfObjects.10.144.1.5': {},
     'optIfObjects.10.144.1.6': {},
     'optIfObjects.10.144.1.7': {},
     'optIfObjects.10.144.1.8': {},
     'optIfObjects.10.144.1.9': {},
     'optIfObjects.10.169.1.3': {},
     'optIfObjects.10.169.1.4': {},
     'optIfObjects.10.169.1.5': {},
     'optIfObjects.10.100.1.10': {},
     'optIfObjects.10.100.1.11': {},
     'optIfObjects.10.100.1.12': {},
     'optIfObjects.10.100.1.13': {},
     'optIfObjects.10.100.1.14': {},
     'optIfObjects.10.100.1.15': {},
     'optIfObjects.10.100.1.3': {},
     'optIfObjects.10.100.1.4': {},
     'optIfObjects.10.100.1.5': {},
     'optIfObjects.10.100.1.6': {},
     'optIfObjects.10.100.1.7': {},
     'optIfObjects.10.100.1.8': {},
     'optIfObjects.10.100.1.9': {},
     'optIfObjects.10.121.1.10': {},
     'optIfObjects.10.121.1.11': {},
     'optIfObjects.10.121.1.3': {},
     'optIfObjects.10.121.1.4': {},
     'optIfObjects.10.121.1.5': {},
     'optIfObjects.10.121.1.6': {},
     'optIfObjects.10.121.1.7': {},
     'optIfObjects.10.121.1.8': {},
     'optIfObjects.10.121.1.9': {},
     'ospfAreaAggregateEntry': {'1': {},
                                '2': {},
                                '3': {},
                                '4': {},
                                '5': {},
                                '6': {}},
     'ospfAreaEntry': {'1': {},
                       '10': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'ospfAreaRangeEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ospfExtLsdbEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {}},
     'ospfGeneralGroup': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'ospfHostEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ospfIfEntry': {'1': {},
                     '10': {},
                     '11': {},
                     '12': {},
                     '13': {},
                     '14': {},
                     '15': {},
                     '16': {},
                     '17': {},
                     '18': {},
                     '19': {},
                     '2': {},
                     '20': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'ospfIfMetricEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ospfLsdbEntry': {'1': {},
                       '2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {}},
     'ospfNbrEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'ospfStubAreaEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'ospfTrap.1.1': {},
     'ospfTrap.1.2': {},
     'ospfTrap.1.3': {},
     'ospfTrap.1.4': {},
     'ospfVirtIfEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'ospfVirtNbrEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {}},
     'ospfv3AreaAggregateEntry': {'6': {}, '7': {}, '8': {}},
     'ospfv3AreaEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'ospfv3AreaLsdbEntry': {'5': {}, '6': {}, '7': {}, '8': {}, '9': {}},
     'ospfv3AsLsdbEntry': {'4': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'ospfv3CfgNbrEntry': {'5': {}, '6': {}},
     'ospfv3GeneralGroup': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '2': {},
                            '20': {},
                            '21': {},
                            '22': {},
                            '23': {},
                            '24': {},
                            '25': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'ospfv3HostEntry': {'3': {}, '4': {}, '5': {}},
     'ospfv3IfEntry': {'10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '15': {},
                       '16': {},
                       '17': {},
                       '18': {},
                       '19': {},
                       '20': {},
                       '21': {},
                       '22': {},
                       '23': {},
                       '24': {},
                       '25': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'ospfv3LinkLsdbEntry': {'10': {}, '6': {}, '7': {}, '8': {}, '9': {}},
     'ospfv3NbrEntry': {'10': {},
                        '11': {},
                        '12': {},
                        '13': {},
                        '14': {},
                        '15': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'ospfv3VirtIfEntry': {'10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'ospfv3VirtLinkLsdbEntry': {'10': {}, '6': {}, '7': {}, '8': {}, '9': {}},
     'ospfv3VirtNbrEntry': {'10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'pim': {'1': {}},
     'pimAnycastRPSetLocalRouter': {},
     'pimAnycastRPSetRowStatus': {},
     'pimBidirDFElectionState': {},
     'pimBidirDFElectionStateTimer': {},
     'pimBidirDFElectionWinnerAddress': {},
     'pimBidirDFElectionWinnerAddressType': {},
     'pimBidirDFElectionWinnerMetric': {},
     'pimBidirDFElectionWinnerMetricPref': {},
     'pimBidirDFElectionWinnerUpTime': {},
     'pimCandidateRPEntry': {'3': {}, '4': {}},
     'pimComponentEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'pimGroupMappingPimMode': {},
     'pimGroupMappingPrecedence': {},
     'pimInAsserts': {},
     'pimInterfaceAddress': {},
     'pimInterfaceAddressType': {},
     'pimInterfaceBidirCapable': {},
     'pimInterfaceDFElectionRobustness': {},
     'pimInterfaceDR': {},
     'pimInterfaceDRPriority': {},
     'pimInterfaceDRPriorityEnabled': {},
     'pimInterfaceDomainBorder': {},
     'pimInterfaceEffectOverrideIvl': {},
     'pimInterfaceEffectPropagDelay': {},
     'pimInterfaceElectionNotificationPeriod': {},
     'pimInterfaceElectionWinCount': {},
     'pimInterfaceEntry': {'2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'pimInterfaceGenerationIDValue': {},
     'pimInterfaceGraftRetryInterval': {},
     'pimInterfaceHelloHoldtime': {},
     'pimInterfaceHelloInterval': {},
     'pimInterfaceJoinPruneHoldtime': {},
     'pimInterfaceJoinPruneInterval': {},
     'pimInterfaceLanDelayEnabled': {},
     'pimInterfaceOverrideInterval': {},
     'pimInterfacePropagationDelay': {},
     'pimInterfacePruneLimitInterval': {},
     'pimInterfaceSRPriorityEnabled': {},
     'pimInterfaceStatus': {},
     'pimInterfaceStubInterface': {},
     'pimInterfaceSuppressionEnabled': {},
     'pimInterfaceTrigHelloInterval': {},
     'pimInvalidJoinPruneAddressType': {},
     'pimInvalidJoinPruneGroup': {},
     'pimInvalidJoinPruneMsgsRcvd': {},
     'pimInvalidJoinPruneNotificationPeriod': {},
     'pimInvalidJoinPruneOrigin': {},
     'pimInvalidJoinPruneRp': {},
     'pimInvalidRegisterAddressType': {},
     'pimInvalidRegisterGroup': {},
     'pimInvalidRegisterMsgsRcvd': {},
     'pimInvalidRegisterNotificationPeriod': {},
     'pimInvalidRegisterOrigin': {},
     'pimInvalidRegisterRp': {},
     'pimIpMRouteEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'pimIpMRouteNextHopEntry': {'2': {}},
     'pimKeepalivePeriod': {},
     'pimLastAssertGroupAddress': {},
     'pimLastAssertGroupAddressType': {},
     'pimLastAssertInterface': {},
     'pimLastAssertSourceAddress': {},
     'pimLastAssertSourceAddressType': {},
     'pimNbrSecAddress': {},
     'pimNeighborBidirCapable': {},
     'pimNeighborDRPriority': {},
     'pimNeighborDRPriorityPresent': {},
     'pimNeighborEntry': {'2': {}, '3': {}, '4': {}, '5': {}},
     'pimNeighborExpiryTime': {},
     'pimNeighborGenerationIDPresent': {},
     'pimNeighborGenerationIDValue': {},
     'pimNeighborLanPruneDelayPresent': {},
     'pimNeighborLossCount': {},
     'pimNeighborLossNotificationPeriod': {},
     'pimNeighborOverrideInterval': {},
     'pimNeighborPropagationDelay': {},
     'pimNeighborSRCapable': {},
     'pimNeighborTBit': {},
     'pimNeighborUpTime': {},
     'pimOutAsserts': {},
     'pimRPEntry': {'3': {}, '4': {}, '5': {}, '6': {}},
     'pimRPMappingChangeCount': {},
     'pimRPMappingNotificationPeriod': {},
     'pimRPSetEntry': {'4': {}, '5': {}},
     'pimRegisterSuppressionTime': {},
     'pimSGDRRegisterState': {},
     'pimSGDRRegisterStopTimer': {},
     'pimSGEntries': {},
     'pimSGIAssertState': {},
     'pimSGIAssertTimer': {},
     'pimSGIAssertWinnerAddress': {},
     'pimSGIAssertWinnerAddressType': {},
     'pimSGIAssertWinnerMetric': {},
     'pimSGIAssertWinnerMetricPref': {},
     'pimSGIEntries': {},
     'pimSGIJoinExpiryTimer': {},
     'pimSGIJoinPruneState': {},
     'pimSGILocalMembership': {},
     'pimSGIPrunePendingTimer': {},
     'pimSGIUpTime': {},
     'pimSGKeepaliveTimer': {},
     'pimSGOriginatorState': {},
     'pimSGPimMode': {},
     'pimSGRPFIfIndex': {},
     'pimSGRPFNextHop': {},
     'pimSGRPFNextHopType': {},
     'pimSGRPFRouteAddress': {},
     'pimSGRPFRouteMetric': {},
     'pimSGRPFRouteMetricPref': {},
     'pimSGRPFRoutePrefixLength': {},
     'pimSGRPFRouteProtocol': {},
     'pimSGRPRegisterPMBRAddress': {},
     'pimSGRPRegisterPMBRAddressType': {},
     'pimSGRptEntries': {},
     'pimSGRptIEntries': {},
     'pimSGRptIJoinPruneState': {},
     'pimSGRptILocalMembership': {},
     'pimSGRptIPruneExpiryTimer': {},
     'pimSGRptIPrunePendingTimer': {},
     'pimSGRptIUpTime': {},
     'pimSGRptUpTime': {},
     'pimSGRptUpstreamOverrideTimer': {},
     'pimSGRptUpstreamPruneState': {},
     'pimSGSPTBit': {},
     'pimSGSourceActiveTimer': {},
     'pimSGStateRefreshTimer': {},
     'pimSGUpTime': {},
     'pimSGUpstreamJoinState': {},
     'pimSGUpstreamJoinTimer': {},
     'pimSGUpstreamNeighbor': {},
     'pimSGUpstreamPruneLimitTimer': {},
     'pimSGUpstreamPruneState': {},
     'pimStarGEntries': {},
     'pimStarGIAssertState': {},
     'pimStarGIAssertTimer': {},
     'pimStarGIAssertWinnerAddress': {},
     'pimStarGIAssertWinnerAddressType': {},
     'pimStarGIAssertWinnerMetric': {},
     'pimStarGIAssertWinnerMetricPref': {},
     'pimStarGIEntries': {},
     'pimStarGIJoinExpiryTimer': {},
     'pimStarGIJoinPruneState': {},
     'pimStarGILocalMembership': {},
     'pimStarGIPrunePendingTimer': {},
     'pimStarGIUpTime': {},
     'pimStarGPimMode': {},
     'pimStarGPimModeOrigin': {},
     'pimStarGRPAddress': {},
     'pimStarGRPAddressType': {},
     'pimStarGRPFIfIndex': {},
     'pimStarGRPFNextHop': {},
     'pimStarGRPFNextHopType': {},
     'pimStarGRPFRouteAddress': {},
     'pimStarGRPFRouteMetric': {},
     'pimStarGRPFRouteMetricPref': {},
     'pimStarGRPFRoutePrefixLength': {},
     'pimStarGRPFRouteProtocol': {},
     'pimStarGRPIsLocal': {},
     'pimStarGUpTime': {},
     'pimStarGUpstreamJoinState': {},
     'pimStarGUpstreamJoinTimer': {},
     'pimStarGUpstreamNeighbor': {},
     'pimStarGUpstreamNeighborType': {},
     'pimStaticRPOverrideDynamic': {},
     'pimStaticRPPimMode': {},
     'pimStaticRPPrecedence': {},
     'pimStaticRPRPAddress': {},
     'pimStaticRPRowStatus': {},
     'qllcLSAdminEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {}},
     'qllcLSOperEntry': {'1': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {}},
     'qllcLSStatsEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'ripCircEntry': {'1': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'ripSysEntry': {'1': {}, '2': {}, '3': {}},
     'rmon.10.106.1.2': {},
     'rmon.10.106.1.3': {},
     'rmon.10.106.1.4': {},
     'rmon.10.106.1.5': {},
     'rmon.10.106.1.6': {},
     'rmon.10.106.1.7': {},
     'rmon.10.145.1.2': {},
     'rmon.10.145.1.3': {},
     'rmon.10.186.1.2': {},
     'rmon.10.186.1.3': {},
     'rmon.10.186.1.4': {},
     'rmon.10.186.1.5': {},
     'rmon.10.229.1.1': {},
     'rmon.10.229.1.2': {},
     'rmon.19.1': {},
     'rmon.10.76.1.1': {},
     'rmon.10.76.1.2': {},
     'rmon.10.76.1.3': {},
     'rmon.10.76.1.4': {},
     'rmon.10.76.1.5': {},
     'rmon.10.76.1.6': {},
     'rmon.10.76.1.7': {},
     'rmon.10.76.1.8': {},
     'rmon.10.76.1.9': {},
     'rmon.10.135.1.1': {},
     'rmon.10.135.1.2': {},
     'rmon.10.135.1.3': {},
     'rmon.19.12': {},
     'rmon.10.4.1.2': {},
     'rmon.10.4.1.3': {},
     'rmon.10.4.1.4': {},
     'rmon.10.4.1.5': {},
     'rmon.10.4.1.6': {},
     'rmon.10.69.1.2': {},
     'rmon.10.69.1.3': {},
     'rmon.10.69.1.4': {},
     'rmon.10.69.1.5': {},
     'rmon.10.69.1.6': {},
     'rmon.10.69.1.7': {},
     'rmon.10.69.1.8': {},
     'rmon.10.69.1.9': {},
     'rmon.19.15': {},
     'rmon.19.16': {},
     'rmon.19.2': {},
     'rmon.19.3': {},
     'rmon.19.4': {},
     'rmon.19.5': {},
     'rmon.19.6': {},
     'rmon.19.7': {},
     'rmon.19.8': {},
     'rmon.19.9': {},
     'rs232': {'1': {}},
     'rs232AsyncPortEntry': {'1': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {}},
     'rs232InSigEntry': {'1': {}, '2': {}, '3': {}},
     'rs232OutSigEntry': {'1': {}, '2': {}, '3': {}},
     'rs232PortEntry': {'1': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {}},
     'rs232SyncPortEntry': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'rsrbRemotePeerEntry': {'10': {},
                             '11': {},
                             '12': {},
                             '13': {},
                             '14': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'rsrbRingEntry': {'2': {},
                       '3': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {}},
     'rsrbVirtRingEntry': {'2': {}, '3': {}},
     'rsvp.2.1': {},
     'rsvp.2.2': {},
     'rsvp.2.3': {},
     'rsvp.2.4': {},
     'rsvp.2.5': {},
     'rsvpIfEntry': {'1': {},
                     '10': {},
                     '11': {},
                     '2': {},
                     '3': {},
                     '4': {},
                     '5': {},
                     '6': {},
                     '7': {},
                     '8': {},
                     '9': {}},
     'rsvpNbrEntry': {'2': {}, '3': {}},
     'rsvpResvEntry': {'10': {},
                       '11': {},
                       '12': {},
                       '13': {},
                       '14': {},
                       '15': {},
                       '16': {},
                       '17': {},
                       '18': {},
                       '19': {},
                       '2': {},
                       '20': {},
                       '21': {},
                       '22': {},
                       '23': {},
                       '24': {},
                       '25': {},
                       '26': {},
                       '27': {},
                       '28': {},
                       '29': {},
                       '3': {},
                       '30': {},
                       '4': {},
                       '5': {},
                       '6': {},
                       '7': {},
                       '8': {},
                       '9': {}},
     'rsvpResvFwdEntry': {'10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '25': {},
                          '26': {},
                          '27': {},
                          '28': {},
                          '29': {},
                          '3': {},
                          '30': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'rsvpSenderEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '2': {},
                         '20': {},
                         '21': {},
                         '22': {},
                         '23': {},
                         '24': {},
                         '25': {},
                         '26': {},
                         '27': {},
                         '28': {},
                         '29': {},
                         '3': {},
                         '30': {},
                         '31': {},
                         '32': {},
                         '33': {},
                         '34': {},
                         '35': {},
                         '36': {},
                         '37': {},
                         '38': {},
                         '39': {},
                         '4': {},
                         '40': {},
                         '41': {},
                         '42': {},
                         '43': {},
                         '44': {},
                         '45': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'rsvpSenderOutInterfaceStatus': {},
     'rsvpSessionEntry': {'2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'rtmpEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}},
     'rttMonApplAuthKeyChain': {},
     'rttMonApplAuthKeyString1': {},
     'rttMonApplAuthKeyString2': {},
     'rttMonApplAuthKeyString3': {},
     'rttMonApplAuthKeyString4': {},
     'rttMonApplAuthKeyString5': {},
     'rttMonApplAuthStatus': {},
     'rttMonApplFreeMemLowWaterMark': {},
     'rttMonApplLatestSetError': {},
     'rttMonApplLpdGrpStatsReset': {},
     'rttMonApplMaxPacketDataSize': {},
     'rttMonApplNumCtrlAdminEntry': {},
     'rttMonApplPreConfigedReset': {},
     'rttMonApplPreConfigedValid': {},
     'rttMonApplProbeCapacity': {},
     'rttMonApplReset': {},
     'rttMonApplResponder': {},
     'rttMonApplSupportedProtocolsValid': {},
     'rttMonApplSupportedRttTypesValid': {},
     'rttMonApplTimeOfLastSet': {},
     'rttMonApplVersion': {},
     'rttMonControlEnableErrors': {},
     'rttMonCtrlAdminFrequency': {},
     'rttMonCtrlAdminGroupName': {},
     'rttMonCtrlAdminLongTag': {},
     'rttMonCtrlAdminNvgen': {},
     'rttMonCtrlAdminOwner': {},
     'rttMonCtrlAdminRttType': {},
     'rttMonCtrlAdminStatus': {},
     'rttMonCtrlAdminTag': {},
     'rttMonCtrlAdminThreshold': {},
     'rttMonCtrlAdminTimeout': {},
     'rttMonCtrlAdminVerifyData': {},
     'rttMonCtrlOperConnectionLostOccurred': {},
     'rttMonCtrlOperDiagText': {},
     'rttMonCtrlOperModificationTime': {},
     'rttMonCtrlOperNumRtts': {},
     'rttMonCtrlOperOctetsInUse': {},
     'rttMonCtrlOperOverThresholdOccurred': {},
     'rttMonCtrlOperResetTime': {},
     'rttMonCtrlOperRttLife': {},
     'rttMonCtrlOperState': {},
     'rttMonCtrlOperTimeoutOccurred': {},
     'rttMonCtrlOperVerifyErrorOccurred': {},
     'rttMonEchoAdminAggBurstCycles': {},
     'rttMonEchoAdminAvailNumFrames': {},
     'rttMonEchoAdminCache': {},
     'rttMonEchoAdminCallDuration': {},
     'rttMonEchoAdminCalledNumber': {},
     'rttMonEchoAdminCodecInterval': {},
     'rttMonEchoAdminCodecNumPackets': {},
     'rttMonEchoAdminCodecPayload': {},
     'rttMonEchoAdminCodecType': {},
     'rttMonEchoAdminControlEnable': {},
     'rttMonEchoAdminControlRetry': {},
     'rttMonEchoAdminControlTimeout': {},
     'rttMonEchoAdminDetectPoint': {},
     'rttMonEchoAdminDscp': {},
     'rttMonEchoAdminEmulateSourceAddress': {},
     'rttMonEchoAdminEmulateSourcePort': {},
     'rttMonEchoAdminEmulateTargetAddress': {},
     'rttMonEchoAdminEmulateTargetPort': {},
     'rttMonEchoAdminEnableBurst': {},
     'rttMonEchoAdminEndPointListName': {},
     'rttMonEchoAdminEntry': {'77': {}, '78': {}, '79': {}},
     'rttMonEchoAdminEthernetCOS': {},
     'rttMonEchoAdminGKRegistration': {},
     'rttMonEchoAdminHTTPVersion': {},
     'rttMonEchoAdminICPIFAdvFactor': {},
     'rttMonEchoAdminIgmpTreeInit': {},
     'rttMonEchoAdminInputInterface': {},
     'rttMonEchoAdminInterval': {},
     'rttMonEchoAdminLSPExp': {},
     'rttMonEchoAdminLSPFECType': {},
     'rttMonEchoAdminLSPNullShim': {},
     'rttMonEchoAdminLSPReplyDscp': {},
     'rttMonEchoAdminLSPReplyMode': {},
     'rttMonEchoAdminLSPSelector': {},
     'rttMonEchoAdminLSPTTL': {},
     'rttMonEchoAdminLSPVccvID': {},
     'rttMonEchoAdminLSREnable': {},
     'rttMonEchoAdminLossRatioNumFrames': {},
     'rttMonEchoAdminMode': {},
     'rttMonEchoAdminNameServer': {},
     'rttMonEchoAdminNumPackets': {},
     'rttMonEchoAdminOWNTPSyncTolAbs': {},
     'rttMonEchoAdminOWNTPSyncTolPct': {},
     'rttMonEchoAdminOWNTPSyncTolType': {},
     'rttMonEchoAdminOperation': {},
     'rttMonEchoAdminPktDataRequestSize': {},
     'rttMonEchoAdminPktDataResponseSize': {},
     'rttMonEchoAdminPrecision': {},
     'rttMonEchoAdminProbePakPriority': {},
     'rttMonEchoAdminProtocol': {},
     'rttMonEchoAdminProxy': {},
     'rttMonEchoAdminReserveDsp': {},
     'rttMonEchoAdminSSM': {},
     'rttMonEchoAdminSourceAddress': {},
     'rttMonEchoAdminSourceMPID': {},
     'rttMonEchoAdminSourceMacAddress': {},
     'rttMonEchoAdminSourcePort': {},
     'rttMonEchoAdminSourceVoicePort': {},
     'rttMonEchoAdminString1': {},
     'rttMonEchoAdminString2': {},
     'rttMonEchoAdminString3': {},
     'rttMonEchoAdminString4': {},
     'rttMonEchoAdminString5': {},
     'rttMonEchoAdminTOS': {},
     'rttMonEchoAdminTargetAddress': {},
     'rttMonEchoAdminTargetAddressString': {},
     'rttMonEchoAdminTargetDomainName': {},
     'rttMonEchoAdminTargetEVC': {},
     'rttMonEchoAdminTargetMEPPort': {},
     'rttMonEchoAdminTargetMPID': {},
     'rttMonEchoAdminTargetMacAddress': {},
     'rttMonEchoAdminTargetPort': {},
     'rttMonEchoAdminTargetVLAN': {},
     'rttMonEchoAdminTstampOptimization': {},
     'rttMonEchoAdminURL': {},
     'rttMonEchoAdminVideoTrafficProfile': {},
     'rttMonEchoAdminVrfName': {},
     'rttMonEchoPathAdminHopAddress': {},
     'rttMonFileIOAdminAction': {},
     'rttMonFileIOAdminFilePath': {},
     'rttMonFileIOAdminSize': {},
     'rttMonGeneratedOperCtrlAdminIndex': {},
     'rttMonGrpScheduleAdminAdd': {},
     'rttMonGrpScheduleAdminAgeout': {},
     'rttMonGrpScheduleAdminDelete': {},
     'rttMonGrpScheduleAdminFreqMax': {},
     'rttMonGrpScheduleAdminFreqMin': {},
     'rttMonGrpScheduleAdminFrequency': {},
     'rttMonGrpScheduleAdminLife': {},
     'rttMonGrpScheduleAdminPeriod': {},
     'rttMonGrpScheduleAdminProbes': {},
     'rttMonGrpScheduleAdminReset': {},
     'rttMonGrpScheduleAdminStartDelay': {},
     'rttMonGrpScheduleAdminStartTime': {},
     'rttMonGrpScheduleAdminStartType': {},
     'rttMonGrpScheduleAdminStatus': {},
     'rttMonHTTPStatsBusies': {},
     'rttMonHTTPStatsCompletions': {},
     'rttMonHTTPStatsDNSQueryError': {},
     'rttMonHTTPStatsDNSRTTSum': {},
     'rttMonHTTPStatsDNSServerTimeout': {},
     'rttMonHTTPStatsError': {},
     'rttMonHTTPStatsHTTPError': {},
     'rttMonHTTPStatsMessageBodyOctetsSum': {},
     'rttMonHTTPStatsOverThresholds': {},
     'rttMonHTTPStatsRTTMax': {},
     'rttMonHTTPStatsRTTMin': {},
     'rttMonHTTPStatsRTTSum': {},
     'rttMonHTTPStatsRTTSum2High': {},
     'rttMonHTTPStatsRTTSum2Low': {},
     'rttMonHTTPStatsTCPConnectRTTSum': {},
     'rttMonHTTPStatsTCPConnectTimeout': {},
     'rttMonHTTPStatsTransactionRTTSum': {},
     'rttMonHTTPStatsTransactionTimeout': {},
     'rttMonHistoryAdminFilter': {},
     'rttMonHistoryAdminNumBuckets': {},
     'rttMonHistoryAdminNumLives': {},
     'rttMonHistoryAdminNumSamples': {},
     'rttMonHistoryCollectionAddress': {},
     'rttMonHistoryCollectionApplSpecificSense': {},
     'rttMonHistoryCollectionCompletionTime': {},
     'rttMonHistoryCollectionSampleTime': {},
     'rttMonHistoryCollectionSense': {},
     'rttMonHistoryCollectionSenseDescription': {},
     'rttMonIcmpJStatsOWSum2DSHighs': {},
     'rttMonIcmpJStatsOWSum2DSLows': {},
     'rttMonIcmpJStatsOWSum2SDHighs': {},
     'rttMonIcmpJStatsOWSum2SDLows': {},
     'rttMonIcmpJStatsOverThresholds': {},
     'rttMonIcmpJStatsPktOutSeqBoth': {},
     'rttMonIcmpJStatsPktOutSeqDSes': {},
     'rttMonIcmpJStatsPktOutSeqSDs': {},
     'rttMonIcmpJStatsRTTSum2Highs': {},
     'rttMonIcmpJStatsRTTSum2Lows': {},
     'rttMonIcmpJStatsSum2NegDSHighs': {},
     'rttMonIcmpJStatsSum2NegDSLows': {},
     'rttMonIcmpJStatsSum2NegSDHighs': {},
     'rttMonIcmpJStatsSum2NegSDLows': {},
     'rttMonIcmpJStatsSum2PosDSHighs': {},
     'rttMonIcmpJStatsSum2PosDSLows': {},
     'rttMonIcmpJStatsSum2PosSDHighs': {},
     'rttMonIcmpJStatsSum2PosSDLows': {},
     'rttMonIcmpJitterMaxSucPktLoss': {},
     'rttMonIcmpJitterMinSucPktLoss': {},
     'rttMonIcmpJitterStatsAvgJ': {},
     'rttMonIcmpJitterStatsAvgJDS': {},
     'rttMonIcmpJitterStatsAvgJSD': {},
     'rttMonIcmpJitterStatsBusies': {},
     'rttMonIcmpJitterStatsCompletions': {},
     'rttMonIcmpJitterStatsErrors': {},
     'rttMonIcmpJitterStatsIAJIn': {},
     'rttMonIcmpJitterStatsIAJOut': {},
     'rttMonIcmpJitterStatsMaxNegDS': {},
     'rttMonIcmpJitterStatsMaxNegSD': {},
     'rttMonIcmpJitterStatsMaxPosDS': {},
     'rttMonIcmpJitterStatsMaxPosSD': {},
     'rttMonIcmpJitterStatsMinNegDS': {},
     'rttMonIcmpJitterStatsMinNegSD': {},
     'rttMonIcmpJitterStatsMinPosDS': {},
     'rttMonIcmpJitterStatsMinPosSD': {},
     'rttMonIcmpJitterStatsNumNegDSes': {},
     'rttMonIcmpJitterStatsNumNegSDs': {},
     'rttMonIcmpJitterStatsNumOWs': {},
     'rttMonIcmpJitterStatsNumOverThresh': {},
     'rttMonIcmpJitterStatsNumPosDSes': {},
     'rttMonIcmpJitterStatsNumPosSDs': {},
     'rttMonIcmpJitterStatsNumRTTs': {},
     'rttMonIcmpJitterStatsOWMaxDS': {},
     'rttMonIcmpJitterStatsOWMaxSD': {},
     'rttMonIcmpJitterStatsOWMinDS': {},
     'rttMonIcmpJitterStatsOWMinSD': {},
     'rttMonIcmpJitterStatsOWSumDSes': {},
     'rttMonIcmpJitterStatsOWSumSDs': {},
     'rttMonIcmpJitterStatsPktLateAs': {},
     'rttMonIcmpJitterStatsPktLosses': {},
     'rttMonIcmpJitterStatsPktSkippeds': {},
     'rttMonIcmpJitterStatsRTTMax': {},
     'rttMonIcmpJitterStatsRTTMin': {},
     'rttMonIcmpJitterStatsRTTSums': {},
     'rttMonIcmpJitterStatsSumNegDSes': {},
     'rttMonIcmpJitterStatsSumNegSDs': {},
     'rttMonIcmpJitterStatsSumPosDSes': {},
     'rttMonIcmpJitterStatsSumPosSDs': {},
     'rttMonJitterStatsAvgJitter': {},
     'rttMonJitterStatsAvgJitterDS': {},
     'rttMonJitterStatsAvgJitterSD': {},
     'rttMonJitterStatsBusies': {},
     'rttMonJitterStatsCompletions': {},
     'rttMonJitterStatsError': {},
     'rttMonJitterStatsIAJIn': {},
     'rttMonJitterStatsIAJOut': {},
     'rttMonJitterStatsMaxOfICPIF': {},
     'rttMonJitterStatsMaxOfMOS': {},
     'rttMonJitterStatsMaxOfNegativesDS': {},
     'rttMonJitterStatsMaxOfNegativesSD': {},
     'rttMonJitterStatsMaxOfPositivesDS': {},
     'rttMonJitterStatsMaxOfPositivesSD': {},
     'rttMonJitterStatsMinOfICPIF': {},
     'rttMonJitterStatsMinOfMOS': {},
     'rttMonJitterStatsMinOfNegativesDS': {},
     'rttMonJitterStatsMinOfNegativesSD': {},
     'rttMonJitterStatsMinOfPositivesDS': {},
     'rttMonJitterStatsMinOfPositivesSD': {},
     'rttMonJitterStatsNumOfNegativesDS': {},
     'rttMonJitterStatsNumOfNegativesSD': {},
     'rttMonJitterStatsNumOfOW': {},
     'rttMonJitterStatsNumOfPositivesDS': {},
     'rttMonJitterStatsNumOfPositivesSD': {},
     'rttMonJitterStatsNumOfRTT': {},
     'rttMonJitterStatsNumOverThresh': {},
     'rttMonJitterStatsOWMaxDS': {},
     'rttMonJitterStatsOWMaxDSNew': {},
     'rttMonJitterStatsOWMaxSD': {},
     'rttMonJitterStatsOWMaxSDNew': {},
     'rttMonJitterStatsOWMinDS': {},
     'rttMonJitterStatsOWMinDSNew': {},
     'rttMonJitterStatsOWMinSD': {},
     'rttMonJitterStatsOWMinSDNew': {},
     'rttMonJitterStatsOWSum2DSHigh': {},
     'rttMonJitterStatsOWSum2DSLow': {},
     'rttMonJitterStatsOWSum2SDHigh': {},
     'rttMonJitterStatsOWSum2SDLow': {},
     'rttMonJitterStatsOWSumDS': {},
     'rttMonJitterStatsOWSumDSHigh': {},
     'rttMonJitterStatsOWSumSD': {},
     'rttMonJitterStatsOWSumSDHigh': {},
     'rttMonJitterStatsOverThresholds': {},
     'rttMonJitterStatsPacketLateArrival': {},
     'rttMonJitterStatsPacketLossDS': {},
     'rttMonJitterStatsPacketLossSD': {},
     'rttMonJitterStatsPacketMIA': {},
     'rttMonJitterStatsPacketOutOfSequence': {},
     'rttMonJitterStatsRTTMax': {},
     'rttMonJitterStatsRTTMin': {},
     'rttMonJitterStatsRTTSum': {},
     'rttMonJitterStatsRTTSum2High': {},
     'rttMonJitterStatsRTTSum2Low': {},
     'rttMonJitterStatsRTTSumHigh': {},
     'rttMonJitterStatsSum2NegativesDSHigh': {},
     'rttMonJitterStatsSum2NegativesDSLow': {},
     'rttMonJitterStatsSum2NegativesSDHigh': {},
     'rttMonJitterStatsSum2NegativesSDLow': {},
     'rttMonJitterStatsSum2PositivesDSHigh': {},
     'rttMonJitterStatsSum2PositivesDSLow': {},
     'rttMonJitterStatsSum2PositivesSDHigh': {},
     'rttMonJitterStatsSum2PositivesSDLow': {},
     'rttMonJitterStatsSumOfNegativesDS': {},
     'rttMonJitterStatsSumOfNegativesSD': {},
     'rttMonJitterStatsSumOfPositivesDS': {},
     'rttMonJitterStatsSumOfPositivesSD': {},
     'rttMonJitterStatsUnSyncRTs': {},
     'rttMonLatestHTTPErrorSenseDescription': {},
     'rttMonLatestHTTPOperDNSRTT': {},
     'rttMonLatestHTTPOperMessageBodyOctets': {},
     'rttMonLatestHTTPOperRTT': {},
     'rttMonLatestHTTPOperSense': {},
     'rttMonLatestHTTPOperTCPConnectRTT': {},
     'rttMonLatestHTTPOperTransactionRTT': {},
     'rttMonLatestIcmpJPktOutSeqBoth': {},
     'rttMonLatestIcmpJPktOutSeqDS': {},
     'rttMonLatestIcmpJPktOutSeqSD': {},
     'rttMonLatestIcmpJitterAvgDSJ': {},
     'rttMonLatestIcmpJitterAvgJitter': {},
     'rttMonLatestIcmpJitterAvgSDJ': {},
     'rttMonLatestIcmpJitterIAJIn': {},
     'rttMonLatestIcmpJitterIAJOut': {},
     'rttMonLatestIcmpJitterMaxNegDS': {},
     'rttMonLatestIcmpJitterMaxNegSD': {},
     'rttMonLatestIcmpJitterMaxPosDS': {},
     'rttMonLatestIcmpJitterMaxPosSD': {},
     'rttMonLatestIcmpJitterMaxSucPktL': {},
     'rttMonLatestIcmpJitterMinNegDS': {},
     'rttMonLatestIcmpJitterMinNegSD': {},
     'rttMonLatestIcmpJitterMinPosDS': {},
     'rttMonLatestIcmpJitterMinPosSD': {},
     'rttMonLatestIcmpJitterMinSucPktL': {},
     'rttMonLatestIcmpJitterNumNegDS': {},
     'rttMonLatestIcmpJitterNumNegSD': {},
     'rttMonLatestIcmpJitterNumOW': {},
     'rttMonLatestIcmpJitterNumOverThresh': {},
     'rttMonLatestIcmpJitterNumPosDS': {},
     'rttMonLatestIcmpJitterNumPosSD': {},
     'rttMonLatestIcmpJitterNumRTT': {},
     'rttMonLatestIcmpJitterOWAvgDS': {},
     'rttMonLatestIcmpJitterOWAvgSD': {},
     'rttMonLatestIcmpJitterOWMaxDS': {},
     'rttMonLatestIcmpJitterOWMaxSD': {},
     'rttMonLatestIcmpJitterOWMinDS': {},
     'rttMonLatestIcmpJitterOWMinSD': {},
     'rttMonLatestIcmpJitterOWSum2DS': {},
     'rttMonLatestIcmpJitterOWSum2SD': {},
     'rttMonLatestIcmpJitterOWSumDS': {},
     'rttMonLatestIcmpJitterOWSumSD': {},
     'rttMonLatestIcmpJitterPktLateA': {},
     'rttMonLatestIcmpJitterPktLoss': {},
     'rttMonLatestIcmpJitterPktSkipped': {},
     'rttMonLatestIcmpJitterRTTMax': {},
     'rttMonLatestIcmpJitterRTTMin': {},
     'rttMonLatestIcmpJitterRTTSum': {},
     'rttMonLatestIcmpJitterRTTSum2': {},
     'rttMonLatestIcmpJitterSense': {},
     'rttMonLatestIcmpJitterSum2NegDS': {},
     'rttMonLatestIcmpJitterSum2NegSD': {},
     'rttMonLatestIcmpJitterSum2PosDS': {},
     'rttMonLatestIcmpJitterSum2PosSD': {},
     'rttMonLatestIcmpJitterSumNegDS': {},
     'rttMonLatestIcmpJitterSumNegSD': {},
     'rttMonLatestIcmpJitterSumPosDS': {},
     'rttMonLatestIcmpJitterSumPosSD': {},
     'rttMonLatestJitterErrorSenseDescription': {},
     'rttMonLatestJitterOperAvgDSJ': {},
     'rttMonLatestJitterOperAvgJitter': {},
     'rttMonLatestJitterOperAvgSDJ': {},
     'rttMonLatestJitterOperIAJIn': {},
     'rttMonLatestJitterOperIAJOut': {},
     'rttMonLatestJitterOperICPIF': {},
     'rttMonLatestJitterOperMOS': {},
     'rttMonLatestJitterOperMaxOfNegativesDS': {},
     'rttMonLatestJitterOperMaxOfNegativesSD': {},
     'rttMonLatestJitterOperMaxOfPositivesDS': {},
     'rttMonLatestJitterOperMaxOfPositivesSD': {},
     'rttMonLatestJitterOperMinOfNegativesDS': {},
     'rttMonLatestJitterOperMinOfNegativesSD': {},
     'rttMonLatestJitterOperMinOfPositivesDS': {},
     'rttMonLatestJitterOperMinOfPositivesSD': {},
     'rttMonLatestJitterOperNTPState': {},
     'rttMonLatestJitterOperNumOfNegativesDS': {},
     'rttMonLatestJitterOperNumOfNegativesSD': {},
     'rttMonLatestJitterOperNumOfOW': {},
     'rttMonLatestJitterOperNumOfPositivesDS': {},
     'rttMonLatestJitterOperNumOfPositivesSD': {},
     'rttMonLatestJitterOperNumOfRTT': {},
     'rttMonLatestJitterOperNumOverThresh': {},
     'rttMonLatestJitterOperOWAvgDS': {},
     'rttMonLatestJitterOperOWAvgSD': {},
     'rttMonLatestJitterOperOWMaxDS': {},
     'rttMonLatestJitterOperOWMaxSD': {},
     'rttMonLatestJitterOperOWMinDS': {},
     'rttMonLatestJitterOperOWMinSD': {},
     'rttMonLatestJitterOperOWSum2DS': {},
     'rttMonLatestJitterOperOWSum2DSHigh': {},
     'rttMonLatestJitterOperOWSum2SD': {},
     'rttMonLatestJitterOperOWSum2SDHigh': {},
     'rttMonLatestJitterOperOWSumDS': {},
     'rttMonLatestJitterOperOWSumDSHigh': {},
     'rttMonLatestJitterOperOWSumSD': {},
     'rttMonLatestJitterOperOWSumSDHigh': {},
     'rttMonLatestJitterOperPacketLateArrival': {},
     'rttMonLatestJitterOperPacketLossDS': {},
     'rttMonLatestJitterOperPacketLossSD': {},
     'rttMonLatestJitterOperPacketMIA': {},
     'rttMonLatestJitterOperPacketOutOfSequence': {},
     'rttMonLatestJitterOperRTTMax': {},
     'rttMonLatestJitterOperRTTMin': {},
     'rttMonLatestJitterOperRTTSum': {},
     'rttMonLatestJitterOperRTTSum2': {},
     'rttMonLatestJitterOperRTTSum2High': {},
     'rttMonLatestJitterOperRTTSumHigh': {},
     'rttMonLatestJitterOperSense': {},
     'rttMonLatestJitterOperSum2NegativesDS': {},
     'rttMonLatestJitterOperSum2NegativesSD': {},
     'rttMonLatestJitterOperSum2PositivesDS': {},
     'rttMonLatestJitterOperSum2PositivesSD': {},
     'rttMonLatestJitterOperSumOfNegativesDS': {},
     'rttMonLatestJitterOperSumOfNegativesSD': {},
     'rttMonLatestJitterOperSumOfPositivesDS': {},
     'rttMonLatestJitterOperSumOfPositivesSD': {},
     'rttMonLatestJitterOperUnSyncRTs': {},
     'rttMonLatestRtpErrorSenseDescription': {},
     'rttMonLatestRtpOperAvgOWDS': {},
     'rttMonLatestRtpOperAvgOWSD': {},
     'rttMonLatestRtpOperFrameLossDS': {},
     'rttMonLatestRtpOperIAJitterDS': {},
     'rttMonLatestRtpOperIAJitterSD': {},
     'rttMonLatestRtpOperMOSCQDS': {},
     'rttMonLatestRtpOperMOSCQSD': {},
     'rttMonLatestRtpOperMOSLQDS': {},
     'rttMonLatestRtpOperMaxOWDS': {},
     'rttMonLatestRtpOperMaxOWSD': {},
     'rttMonLatestRtpOperMinOWDS': {},
     'rttMonLatestRtpOperMinOWSD': {},
     'rttMonLatestRtpOperPacketEarlyDS': {},
     'rttMonLatestRtpOperPacketLateDS': {},
     'rttMonLatestRtpOperPacketLossDS': {},
     'rttMonLatestRtpOperPacketLossSD': {},
     'rttMonLatestRtpOperPacketOOSDS': {},
     'rttMonLatestRtpOperPacketsMIA': {},
     'rttMonLatestRtpOperRFactorDS': {},
     'rttMonLatestRtpOperRFactorSD': {},
     'rttMonLatestRtpOperRTT': {},
     'rttMonLatestRtpOperSense': {},
     'rttMonLatestRtpOperTotalPaksDS': {},
     'rttMonLatestRtpOperTotalPaksSD': {},
     'rttMonLatestRttOperAddress': {},
     'rttMonLatestRttOperApplSpecificSense': {},
     'rttMonLatestRttOperCompletionTime': {},
     'rttMonLatestRttOperSense': {},
     'rttMonLatestRttOperSenseDescription': {},
     'rttMonLatestRttOperTime': {},
     'rttMonLpdGrpStatsAvgRTT': {},
     'rttMonLpdGrpStatsGroupProbeIndex': {},
     'rttMonLpdGrpStatsGroupStatus': {},
     'rttMonLpdGrpStatsLPDCompTime': {},
     'rttMonLpdGrpStatsLPDFailCause': {},
     'rttMonLpdGrpStatsLPDFailOccurred': {},
     'rttMonLpdGrpStatsLPDStartTime': {},
     'rttMonLpdGrpStatsMaxNumPaths': {},
     'rttMonLpdGrpStatsMaxRTT': {},
     'rttMonLpdGrpStatsMinNumPaths': {},
     'rttMonLpdGrpStatsMinRTT': {},
     'rttMonLpdGrpStatsNumOfFail': {},
     'rttMonLpdGrpStatsNumOfPass': {},
     'rttMonLpdGrpStatsNumOfTimeout': {},
     'rttMonLpdGrpStatsPathIds': {},
     'rttMonLpdGrpStatsProbeStatus': {},
     'rttMonLpdGrpStatsResetTime': {},
     'rttMonLpdGrpStatsTargetPE': {},
     'rttMonReactActionType': {},
     'rttMonReactAdminActionType': {},
     'rttMonReactAdminConnectionEnable': {},
     'rttMonReactAdminThresholdCount': {},
     'rttMonReactAdminThresholdCount2': {},
     'rttMonReactAdminThresholdFalling': {},
     'rttMonReactAdminThresholdType': {},
     'rttMonReactAdminTimeoutEnable': {},
     'rttMonReactAdminVerifyErrorEnable': {},
     'rttMonReactOccurred': {},
     'rttMonReactStatus': {},
     'rttMonReactThresholdCountX': {},
     'rttMonReactThresholdCountY': {},
     'rttMonReactThresholdFalling': {},
     'rttMonReactThresholdRising': {},
     'rttMonReactThresholdType': {},
     'rttMonReactTriggerAdminStatus': {},
     'rttMonReactTriggerOperState': {},
     'rttMonReactValue': {},
     'rttMonReactVar': {},
     'rttMonRtpStatsFrameLossDSAvg': {},
     'rttMonRtpStatsFrameLossDSMax': {},
     'rttMonRtpStatsFrameLossDSMin': {},
     'rttMonRtpStatsIAJitterDSAvg': {},
     'rttMonRtpStatsIAJitterDSMax': {},
     'rttMonRtpStatsIAJitterDSMin': {},
     'rttMonRtpStatsIAJitterSDAvg': {},
     'rttMonRtpStatsIAJitterSDMax': {},
     'rttMonRtpStatsIAJitterSDMin': {},
     'rttMonRtpStatsMOSCQDSAvg': {},
     'rttMonRtpStatsMOSCQDSMax': {},
     'rttMonRtpStatsMOSCQDSMin': {},
     'rttMonRtpStatsMOSCQSDAvg': {},
     'rttMonRtpStatsMOSCQSDMax': {},
     'rttMonRtpStatsMOSCQSDMin': {},
     'rttMonRtpStatsMOSLQDSAvg': {},
     'rttMonRtpStatsMOSLQDSMax': {},
     'rttMonRtpStatsMOSLQDSMin': {},
     'rttMonRtpStatsOperAvgOWDS': {},
     'rttMonRtpStatsOperAvgOWSD': {},
     'rttMonRtpStatsOperMaxOWDS': {},
     'rttMonRtpStatsOperMaxOWSD': {},
     'rttMonRtpStatsOperMinOWDS': {},
     'rttMonRtpStatsOperMinOWSD': {},
     'rttMonRtpStatsPacketEarlyDSAvg': {},
     'rttMonRtpStatsPacketLateDSAvg': {},
     'rttMonRtpStatsPacketLossDSAvg': {},
     'rttMonRtpStatsPacketLossDSMax': {},
     'rttMonRtpStatsPacketLossDSMin': {},
     'rttMonRtpStatsPacketLossSDAvg': {},
     'rttMonRtpStatsPacketLossSDMax': {},
     'rttMonRtpStatsPacketLossSDMin': {},
     'rttMonRtpStatsPacketOOSDSAvg': {},
     'rttMonRtpStatsPacketsMIAAvg': {},
     'rttMonRtpStatsRFactorDSAvg': {},
     'rttMonRtpStatsRFactorDSMax': {},
     'rttMonRtpStatsRFactorDSMin': {},
     'rttMonRtpStatsRFactorSDAvg': {},
     'rttMonRtpStatsRFactorSDMax': {},
     'rttMonRtpStatsRFactorSDMin': {},
     'rttMonRtpStatsRTTAvg': {},
     'rttMonRtpStatsRTTMax': {},
     'rttMonRtpStatsRTTMin': {},
     'rttMonRtpStatsTotalPacketsDSAvg': {},
     'rttMonRtpStatsTotalPacketsDSMax': {},
     'rttMonRtpStatsTotalPacketsDSMin': {},
     'rttMonRtpStatsTotalPacketsSDAvg': {},
     'rttMonRtpStatsTotalPacketsSDMax': {},
     'rttMonRtpStatsTotalPacketsSDMin': {},
     'rttMonScheduleAdminConceptRowAgeout': {},
     'rttMonScheduleAdminConceptRowAgeoutV2': {},
     'rttMonScheduleAdminRttLife': {},
     'rttMonScheduleAdminRttRecurring': {},
     'rttMonScheduleAdminRttStartTime': {},
     'rttMonScheduleAdminStartDelay': {},
     'rttMonScheduleAdminStartType': {},
     'rttMonScriptAdminCmdLineParams': {},
     'rttMonScriptAdminName': {},
     'rttMonStatisticsAdminDistInterval': {},
     'rttMonStatisticsAdminNumDistBuckets': {},
     'rttMonStatisticsAdminNumHops': {},
     'rttMonStatisticsAdminNumHourGroups': {},
     'rttMonStatisticsAdminNumPaths': {},
     'rttMonStatsCaptureCompletionTimeMax': {},
     'rttMonStatsCaptureCompletionTimeMin': {},
     'rttMonStatsCaptureCompletions': {},
     'rttMonStatsCaptureOverThresholds': {},
     'rttMonStatsCaptureSumCompletionTime': {},
     'rttMonStatsCaptureSumCompletionTime2High': {},
     'rttMonStatsCaptureSumCompletionTime2Low': {},
     'rttMonStatsCollectAddress': {},
     'rttMonStatsCollectBusies': {},
     'rttMonStatsCollectCtrlEnErrors': {},
     'rttMonStatsCollectDrops': {},
     'rttMonStatsCollectNoConnections': {},
     'rttMonStatsCollectNumDisconnects': {},
     'rttMonStatsCollectRetrieveErrors': {},
     'rttMonStatsCollectSequenceErrors': {},
     'rttMonStatsCollectTimeouts': {},
     'rttMonStatsCollectVerifyErrors': {},
     'rttMonStatsRetrieveErrors': {},
     'rttMonStatsTotalsElapsedTime': {},
     'rttMonStatsTotalsInitiations': {},
     'rttMplsVpnMonCtrlDelScanFactor': {},
     'rttMplsVpnMonCtrlEXP': {},
     'rttMplsVpnMonCtrlLpd': {},
     'rttMplsVpnMonCtrlLpdCompTime': {},
     'rttMplsVpnMonCtrlLpdGrpList': {},
     'rttMplsVpnMonCtrlProbeList': {},
     'rttMplsVpnMonCtrlRequestSize': {},
     'rttMplsVpnMonCtrlRttType': {},
     'rttMplsVpnMonCtrlScanInterval': {},
     'rttMplsVpnMonCtrlStatus': {},
     'rttMplsVpnMonCtrlStorageType': {},
     'rttMplsVpnMonCtrlTag': {},
     'rttMplsVpnMonCtrlThreshold': {},
     'rttMplsVpnMonCtrlTimeout': {},
     'rttMplsVpnMonCtrlVerifyData': {},
     'rttMplsVpnMonCtrlVrfName': {},
     'rttMplsVpnMonReactActionType': {},
     'rttMplsVpnMonReactConnectionEnable': {},
     'rttMplsVpnMonReactLpdNotifyType': {},
     'rttMplsVpnMonReactLpdRetryCount': {},
     'rttMplsVpnMonReactThresholdCount': {},
     'rttMplsVpnMonReactThresholdType': {},
     'rttMplsVpnMonReactTimeoutEnable': {},
     'rttMplsVpnMonScheduleFrequency': {},
     'rttMplsVpnMonSchedulePeriod': {},
     'rttMplsVpnMonScheduleRttStartTime': {},
     'rttMplsVpnMonTypeDestPort': {},
     'rttMplsVpnMonTypeInterval': {},
     'rttMplsVpnMonTypeLSPReplyDscp': {},
     'rttMplsVpnMonTypeLSPReplyMode': {},
     'rttMplsVpnMonTypeLSPTTL': {},
     'rttMplsVpnMonTypeLpdEchoInterval': {},
     'rttMplsVpnMonTypeLpdEchoNullShim': {},
     'rttMplsVpnMonTypeLpdEchoTimeout': {},
     'rttMplsVpnMonTypeLpdMaxSessions': {},
     'rttMplsVpnMonTypeLpdScanPeriod': {},
     'rttMplsVpnMonTypeLpdSessTimeout': {},
     'rttMplsVpnMonTypeLpdStatHours': {},
     'rttMplsVpnMonTypeLspSelector': {},
     'rttMplsVpnMonTypeNumPackets': {},
     'rttMplsVpnMonTypeSecFreqType': {},
     'rttMplsVpnMonTypeSecFreqValue': {},
     'sapCircEntry': {'1': {},
                      '10': {},
                      '2': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'sapSysEntry': {'1': {}, '2': {}, '3': {}},
     'sdlcLSAdminEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'sdlcLSOperEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '2': {},
                         '20': {},
                         '21': {},
                         '22': {},
                         '23': {},
                         '24': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'sdlcLSStatsEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '25': {},
                          '26': {},
                          '27': {},
                          '28': {},
                          '29': {},
                          '3': {},
                          '30': {},
                          '31': {},
                          '32': {},
                          '33': {},
                          '34': {},
                          '35': {},
                          '36': {},
                          '37': {},
                          '38': {},
                          '39': {},
                          '4': {},
                          '40': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'sdlcPortAdminEntry': {'1': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'sdlcPortOperEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '13': {},
                           '2': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'sdlcPortStatsEntry': {'1': {},
                            '10': {},
                            '11': {},
                            '12': {},
                            '13': {},
                            '14': {},
                            '15': {},
                            '16': {},
                            '17': {},
                            '18': {},
                            '19': {},
                            '2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'snmp': {'1': {},
              '10': {},
              '11': {},
              '12': {},
              '13': {},
              '14': {},
              '15': {},
              '16': {},
              '17': {},
              '18': {},
              '19': {},
              '2': {},
              '20': {},
              '21': {},
              '22': {},
              '24': {},
              '25': {},
              '26': {},
              '27': {},
              '28': {},
              '29': {},
              '3': {},
              '30': {},
              '31': {},
              '32': {},
              '4': {},
              '5': {},
              '6': {},
              '8': {},
              '9': {}},
     'snmpCommunityMIB.10.4.1.2': {},
     'snmpCommunityMIB.10.4.1.3': {},
     'snmpCommunityMIB.10.4.1.4': {},
     'snmpCommunityMIB.10.4.1.5': {},
     'snmpCommunityMIB.10.4.1.6': {},
     'snmpCommunityMIB.10.4.1.7': {},
     'snmpCommunityMIB.10.4.1.8': {},
     'snmpCommunityMIB.10.9.1.1': {},
     'snmpCommunityMIB.10.9.1.2': {},
     'snmpFrameworkMIB.2.1.1': {},
     'snmpFrameworkMIB.2.1.2': {},
     'snmpFrameworkMIB.2.1.3': {},
     'snmpFrameworkMIB.2.1.4': {},
     'snmpMIB.1.6.1': {},
     'snmpMPDMIB.2.1.1': {},
     'snmpMPDMIB.2.1.2': {},
     'snmpMPDMIB.2.1.3': {},
     'snmpNotificationMIB.10.4.1.2': {},
     'snmpNotificationMIB.10.4.1.3': {},
     'snmpNotificationMIB.10.4.1.4': {},
     'snmpNotificationMIB.10.4.1.5': {},
     'snmpNotificationMIB.10.9.1.1': {},
     'snmpNotificationMIB.10.9.1.2': {},
     'snmpNotificationMIB.10.9.1.3': {},
     'snmpNotificationMIB.10.16.1.2': {},
     'snmpNotificationMIB.10.16.1.3': {},
     'snmpNotificationMIB.10.16.1.4': {},
     'snmpNotificationMIB.10.16.1.5': {},
     'snmpProxyMIB.10.9.1.2': {},
     'snmpProxyMIB.10.9.1.3': {},
     'snmpProxyMIB.10.9.1.4': {},
     'snmpProxyMIB.10.9.1.5': {},
     'snmpProxyMIB.10.9.1.6': {},
     'snmpProxyMIB.10.9.1.7': {},
     'snmpProxyMIB.10.9.1.8': {},
     'snmpProxyMIB.10.9.1.9': {},
     'snmpTargetMIB.1.1': {},
     'snmpTargetMIB.10.9.1.2': {},
     'snmpTargetMIB.10.9.1.3': {},
     'snmpTargetMIB.10.9.1.4': {},
     'snmpTargetMIB.10.9.1.5': {},
     'snmpTargetMIB.10.9.1.6': {},
     'snmpTargetMIB.10.9.1.7': {},
     'snmpTargetMIB.10.9.1.8': {},
     'snmpTargetMIB.10.9.1.9': {},
     'snmpTargetMIB.10.16.1.2': {},
     'snmpTargetMIB.10.16.1.3': {},
     'snmpTargetMIB.10.16.1.4': {},
     'snmpTargetMIB.10.16.1.5': {},
     'snmpTargetMIB.10.16.1.6': {},
     'snmpTargetMIB.10.16.1.7': {},
     'snmpTargetMIB.1.4': {},
     'snmpTargetMIB.1.5': {},
     'snmpUsmMIB.1.1.1': {},
     'snmpUsmMIB.1.1.2': {},
     'snmpUsmMIB.1.1.3': {},
     'snmpUsmMIB.1.1.4': {},
     'snmpUsmMIB.1.1.5': {},
     'snmpUsmMIB.1.1.6': {},
     'snmpUsmMIB.1.2.1': {},
     'snmpUsmMIB.10.9.2.1.10': {},
     'snmpUsmMIB.10.9.2.1.11': {},
     'snmpUsmMIB.10.9.2.1.12': {},
     'snmpUsmMIB.10.9.2.1.13': {},
     'snmpUsmMIB.10.9.2.1.3': {},
     'snmpUsmMIB.10.9.2.1.4': {},
     'snmpUsmMIB.10.9.2.1.5': {},
     'snmpUsmMIB.10.9.2.1.6': {},
     'snmpUsmMIB.10.9.2.1.7': {},
     'snmpUsmMIB.10.9.2.1.8': {},
     'snmpUsmMIB.10.9.2.1.9': {},
     'snmpVacmMIB.10.4.1.1': {},
     'snmpVacmMIB.10.9.1.3': {},
     'snmpVacmMIB.10.9.1.4': {},
     'snmpVacmMIB.10.9.1.5': {},
     'snmpVacmMIB.10.25.1.4': {},
     'snmpVacmMIB.10.25.1.5': {},
     'snmpVacmMIB.10.25.1.6': {},
     'snmpVacmMIB.10.25.1.7': {},
     'snmpVacmMIB.10.25.1.8': {},
     'snmpVacmMIB.10.25.1.9': {},
     'snmpVacmMIB.1.5.1': {},
     'snmpVacmMIB.10.36.2.1.3': {},
     'snmpVacmMIB.10.36.2.1.4': {},
     'snmpVacmMIB.10.36.2.1.5': {},
     'snmpVacmMIB.10.36.2.1.6': {},
     'sonetFarEndLineCurrentEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'sonetFarEndLineIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetFarEndPathCurrentEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'sonetFarEndPathIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetFarEndVTCurrentEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'sonetFarEndVTIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetLineCurrentEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'sonetLineIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetMedium': {'2': {}},
     'sonetMediumEntry': {'1': {},
                          '2': {},
                          '3': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {}},
     'sonetPathCurrentEntry': {'1': {},
                               '2': {},
                               '3': {},
                               '4': {},
                               '5': {},
                               '6': {}},
     'sonetPathIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetSectionCurrentEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'sonetSectionIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetVTCurrentEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'sonetVTIntervalEntry': {'2': {}, '3': {}, '4': {}, '5': {}, '6': {}},
     'srpErrCntCurrEntry': {'2': {},
                            '3': {},
                            '4': {},
                            '5': {},
                            '6': {},
                            '7': {},
                            '8': {},
                            '9': {}},
     'srpErrCntIntEntry': {'10': {},
                           '3': {},
                           '4': {},
                           '5': {},
                           '6': {},
                           '7': {},
                           '8': {},
                           '9': {}},
     'srpErrorsCountersCurrentEntry': {'10': {},
                                       '2': {},
                                       '3': {},
                                       '4': {},
                                       '5': {},
                                       '6': {},
                                       '7': {},
                                       '8': {},
                                       '9': {}},
     'srpErrorsCountersIntervalEntry': {'10': {},
                                        '11': {},
                                        '3': {},
                                        '4': {},
                                        '5': {},
                                        '6': {},
                                        '7': {},
                                        '8': {},
                                        '9': {}},
     'srpHostCountersCurrentEntry': {'10': {},
                                     '11': {},
                                     '12': {},
                                     '13': {},
                                     '14': {},
                                     '15': {},
                                     '16': {},
                                     '17': {},
                                     '2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {},
                                     '9': {}},
     'srpHostCountersIntervalEntry': {'10': {},
                                      '11': {},
                                      '12': {},
                                      '13': {},
                                      '14': {},
                                      '15': {},
                                      '16': {},
                                      '17': {},
                                      '18': {},
                                      '3': {},
                                      '4': {},
                                      '5': {},
                                      '6': {},
                                      '7': {},
                                      '8': {},
                                      '9': {}},
     'srpIfEntry': {'1': {},
                    '2': {},
                    '3': {},
                    '4': {},
                    '5': {},
                    '6': {},
                    '7': {},
                    '8': {}},
     'srpMACCountersEntry': {'1': {},
                             '10': {},
                             '11': {},
                             '12': {},
                             '2': {},
                             '3': {},
                             '4': {},
                             '5': {},
                             '6': {},
                             '7': {},
                             '8': {},
                             '9': {}},
     'srpMACSideEntry': {'10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'srpRingCountersCurrentEntry': {'10': {},
                                     '11': {},
                                     '12': {},
                                     '13': {},
                                     '14': {},
                                     '15': {},
                                     '16': {},
                                     '17': {},
                                     '2': {},
                                     '3': {},
                                     '4': {},
                                     '5': {},
                                     '6': {},
                                     '7': {},
                                     '8': {},
                                     '9': {}},
     'srpRingCountersIntervalEntry': {'10': {},
                                      '11': {},
                                      '12': {},
                                      '13': {},
                                      '14': {},
                                      '15': {},
                                      '16': {},
                                      '17': {},
                                      '18': {},
                                      '19': {},
                                      '3': {},
                                      '4': {},
                                      '5': {},
                                      '6': {},
                                      '7': {},
                                      '8': {},
                                      '9': {}},
     'srpRingTopologyMapEntry': {'2': {}, '3': {}, '4': {}},
     'stunGlobal': {'1': {}},
     'stunGroupEntry': {'2': {}},
     'stunPortEntry': {'1': {}, '2': {}, '3': {}, '4': {}},
     'stunRouteEntry': {'10': {},
                        '11': {},
                        '2': {},
                        '3': {},
                        '4': {},
                        '5': {},
                        '6': {},
                        '7': {},
                        '8': {},
                        '9': {}},
     'sysOREntry': {'2': {}, '3': {}, '4': {}},
     'sysUpTime': {},
     'system': {'1': {}, '2': {}, '4': {}, '5': {}, '6': {}, '7': {}, '8': {}},
     'tcp': {'1': {},
             '10': {},
             '11': {},
             '12': {},
             '14': {},
             '15': {},
             '17': {},
             '18': {},
             '2': {},
             '3': {},
             '4': {},
             '5': {},
             '6': {},
             '7': {},
             '8': {},
             '9': {}},
     'tcp.19.1.7': {},
     'tcp.19.1.8': {},
     'tcp.20.1.4': {},
     'tcpConnEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}},
     'tmpappletalk': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '22': {},
                      '23': {},
                      '24': {},
                      '25': {},
                      '26': {},
                      '27': {},
                      '28': {},
                      '29': {},
                      '3': {},
                      '30': {},
                      '31': {},
                      '4': {},
                      '5': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'tmpdecnet': {'1': {},
                   '10': {},
                   '11': {},
                   '12': {},
                   '13': {},
                   '14': {},
                   '15': {},
                   '16': {},
                   '17': {},
                   '18': {},
                   '19': {},
                   '2': {},
                   '20': {},
                   '21': {},
                   '22': {},
                   '23': {},
                   '24': {},
                   '25': {},
                   '3': {},
                   '4': {},
                   '5': {},
                   '6': {},
                   '7': {},
                   '8': {},
                   '9': {}},
     'tmpnovell': {'1': {},
                   '10': {},
                   '11': {},
                   '12': {},
                   '13': {},
                   '14': {},
                   '15': {},
                   '16': {},
                   '17': {},
                   '18': {},
                   '19': {},
                   '2': {},
                   '20': {},
                   '22': {},
                   '24': {},
                   '25': {},
                   '3': {},
                   '4': {},
                   '5': {},
                   '6': {},
                   '7': {},
                   '8': {},
                   '9': {}},
     'tmpvines': {'1': {},
                  '10': {},
                  '11': {},
                  '12': {},
                  '13': {},
                  '14': {},
                  '15': {},
                  '16': {},
                  '17': {},
                  '18': {},
                  '19': {},
                  '2': {},
                  '20': {},
                  '21': {},
                  '22': {},
                  '23': {},
                  '24': {},
                  '25': {},
                  '26': {},
                  '27': {},
                  '28': {},
                  '3': {},
                  '4': {},
                  '5': {},
                  '6': {},
                  '7': {},
                  '8': {},
                  '9': {}},
     'tmpxns': {'1': {},
                '10': {},
                '11': {},
                '12': {},
                '13': {},
                '14': {},
                '15': {},
                '16': {},
                '17': {},
                '18': {},
                '19': {},
                '2': {},
                '20': {},
                '21': {},
                '3': {},
                '4': {},
                '5': {},
                '6': {},
                '7': {},
                '8': {},
                '9': {}},
     'tunnelConfigIfIndex': {},
     'tunnelConfigStatus': {},
     'tunnelIfAddressType': {},
     'tunnelIfEncapsLimit': {},
     'tunnelIfEncapsMethod': {},
     'tunnelIfFlowLabel': {},
     'tunnelIfHopLimit': {},
     'tunnelIfLocalAddress': {},
     'tunnelIfLocalInetAddress': {},
     'tunnelIfRemoteAddress': {},
     'tunnelIfRemoteInetAddress': {},
     'tunnelIfSecurity': {},
     'tunnelIfTOS': {},
     'tunnelInetConfigIfIndex': {},
     'tunnelInetConfigStatus': {},
     'tunnelInetConfigStorageType': {},
     'udp': {'1': {}, '2': {}, '3': {}, '4': {}, '8': {}, '9': {}},
     'udp.7.1.8': {},
     'udpEntry': {'1': {}, '2': {}},
     'vinesIfTableEntry': {'1': {},
                           '10': {},
                           '11': {},
                           '12': {},
                           '17': {},
                           '18': {},
                           '19': {},
                           '2': {},
                           '20': {},
                           '21': {},
                           '22': {},
                           '23': {},
                           '24': {},
                           '25': {},
                           '26': {},
                           '27': {},
                           '28': {},
                           '29': {},
                           '3': {},
                           '30': {},
                           '31': {},
                           '32': {},
                           '33': {},
                           '34': {},
                           '35': {},
                           '36': {},
                           '37': {},
                           '38': {},
                           '39': {},
                           '4': {},
                           '40': {},
                           '41': {},
                           '42': {},
                           '43': {},
                           '44': {},
                           '45': {},
                           '46': {},
                           '47': {},
                           '48': {},
                           '49': {},
                           '5': {},
                           '50': {},
                           '51': {},
                           '52': {},
                           '53': {},
                           '54': {},
                           '55': {},
                           '56': {},
                           '57': {},
                           '58': {},
                           '59': {},
                           '6': {},
                           '60': {},
                           '61': {},
                           '62': {},
                           '63': {},
                           '64': {},
                           '65': {},
                           '66': {},
                           '67': {},
                           '68': {},
                           '69': {},
                           '70': {},
                           '71': {},
                           '72': {},
                           '73': {},
                           '74': {},
                           '75': {},
                           '76': {},
                           '77': {},
                           '78': {},
                           '79': {},
                           '8': {},
                           '80': {},
                           '81': {},
                           '82': {},
                           '83': {},
                           '9': {}},
     'vrrpAssoIpAddrRowStatus': {},
     'vrrpNodeVersion': {},
     'vrrpNotificationCntl': {},
     'vrrpOperAdminState': {},
     'vrrpOperAdvertisementInterval': {},
     'vrrpOperAuthKey': {},
     'vrrpOperAuthType': {},
     'vrrpOperIpAddrCount': {},
     'vrrpOperMasterIpAddr': {},
     'vrrpOperPreemptMode': {},
     'vrrpOperPrimaryIpAddr': {},
     'vrrpOperPriority': {},
     'vrrpOperProtocol': {},
     'vrrpOperRowStatus': {},
     'vrrpOperState': {},
     'vrrpOperVirtualMacAddr': {},
     'vrrpOperVirtualRouterUpTime': {},
     'vrrpRouterChecksumErrors': {},
     'vrrpRouterVersionErrors': {},
     'vrrpRouterVrIdErrors': {},
     'vrrpStatsAddressListErrors': {},
     'vrrpStatsAdvertiseIntervalErrors': {},
     'vrrpStatsAdvertiseRcvd': {},
     'vrrpStatsAuthFailures': {},
     'vrrpStatsAuthTypeMismatch': {},
     'vrrpStatsBecomeMaster': {},
     'vrrpStatsInvalidAuthType': {},
     'vrrpStatsInvalidTypePktsRcvd': {},
     'vrrpStatsIpTtlErrors': {},
     'vrrpStatsPacketLengthErrors': {},
     'vrrpStatsPriorityZeroPktsRcvd': {},
     'vrrpStatsPriorityZeroPktsSent': {},
     'vrrpTrapAuthErrorType': {},
     'vrrpTrapPacketSrc': {},
     'x25': {'6': {}, '7': {}},
     'x25AdmnEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '22': {},
                      '23': {},
                      '24': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'x25CallParmEntry': {'1': {},
                          '10': {},
                          '11': {},
                          '12': {},
                          '13': {},
                          '14': {},
                          '15': {},
                          '16': {},
                          '17': {},
                          '18': {},
                          '19': {},
                          '2': {},
                          '20': {},
                          '21': {},
                          '22': {},
                          '23': {},
                          '24': {},
                          '25': {},
                          '26': {},
                          '27': {},
                          '28': {},
                          '29': {},
                          '3': {},
                          '30': {},
                          '4': {},
                          '5': {},
                          '6': {},
                          '7': {},
                          '8': {},
                          '9': {}},
     'x25ChannelEntry': {'1': {},
                         '2': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {}},
     'x25CircuitEntry': {'1': {},
                         '10': {},
                         '11': {},
                         '12': {},
                         '13': {},
                         '14': {},
                         '15': {},
                         '16': {},
                         '17': {},
                         '18': {},
                         '19': {},
                         '2': {},
                         '20': {},
                         '21': {},
                         '3': {},
                         '4': {},
                         '5': {},
                         '6': {},
                         '7': {},
                         '8': {},
                         '9': {}},
     'x25ClearedCircuitEntry': {'1': {},
                                '10': {},
                                '11': {},
                                '12': {},
                                '2': {},
                                '3': {},
                                '4': {},
                                '5': {},
                                '6': {},
                                '7': {},
                                '8': {},
                                '9': {}},
     'x25OperEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '22': {},
                      '23': {},
                      '24': {},
                      '25': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'x25StatEntry': {'1': {},
                      '10': {},
                      '11': {},
                      '12': {},
                      '13': {},
                      '14': {},
                      '15': {},
                      '16': {},
                      '17': {},
                      '18': {},
                      '19': {},
                      '2': {},
                      '20': {},
                      '21': {},
                      '22': {},
                      '23': {},
                      '24': {},
                      '25': {},
                      '3': {},
                      '4': {},
                      '5': {},
                      '6': {},
                      '7': {},
                      '8': {},
                      '9': {}},
     'xdsl2ChAlarmConfProfileRowStatus': {},
     'xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations': {},
     'xdsl2ChAlarmConfProfileXtucThresh15MinCorrected': {},
     'xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations': {},
     'xdsl2ChAlarmConfProfileXturThresh15MinCorrected': {},
     'xdsl2ChConfProfDsDataRateDs': {},
     'xdsl2ChConfProfDsDataRateUs': {},
     'xdsl2ChConfProfImaEnabled': {},
     'xdsl2ChConfProfInitPolicy': {},
     'xdsl2ChConfProfMaxBerDs': {},
     'xdsl2ChConfProfMaxBerUs': {},
     'xdsl2ChConfProfMaxDataRateDs': {},
     'xdsl2ChConfProfMaxDataRateUs': {},
     'xdsl2ChConfProfMaxDelayDs': {},
     'xdsl2ChConfProfMaxDelayUs': {},
     'xdsl2ChConfProfMaxDelayVar': {},
     'xdsl2ChConfProfMinDataRateDs': {},
     'xdsl2ChConfProfMinDataRateLowPwrDs': {},
     'xdsl2ChConfProfMinDataRateLowPwrUs': {},
     'xdsl2ChConfProfMinDataRateUs': {},
     'xdsl2ChConfProfMinProtection8Ds': {},
     'xdsl2ChConfProfMinProtection8Us': {},
     'xdsl2ChConfProfMinProtectionDs': {},
     'xdsl2ChConfProfMinProtectionUs': {},
     'xdsl2ChConfProfMinResDataRateDs': {},
     'xdsl2ChConfProfMinResDataRateUs': {},
     'xdsl2ChConfProfRowStatus': {},
     'xdsl2ChConfProfUsDataRateDs': {},
     'xdsl2ChConfProfUsDataRateUs': {},
     'xdsl2ChStatusActDataRate': {},
     'xdsl2ChStatusActDelay': {},
     'xdsl2ChStatusActInp': {},
     'xdsl2ChStatusAtmStatus': {},
     'xdsl2ChStatusInpReport': {},
     'xdsl2ChStatusIntlvBlock': {},
     'xdsl2ChStatusIntlvDepth': {},
     'xdsl2ChStatusLPath': {},
     'xdsl2ChStatusLSymb': {},
     'xdsl2ChStatusNFec': {},
     'xdsl2ChStatusPrevDataRate': {},
     'xdsl2ChStatusPtmStatus': {},
     'xdsl2ChStatusRFec': {},
     'xdsl2LAlarmConfTempChan1ConfProfile': {},
     'xdsl2LAlarmConfTempChan2ConfProfile': {},
     'xdsl2LAlarmConfTempChan3ConfProfile': {},
     'xdsl2LAlarmConfTempChan4ConfProfile': {},
     'xdsl2LAlarmConfTempLineProfile': {},
     'xdsl2LAlarmConfTempRowStatus': {},
     'xdsl2LConfProfCeFlag': {},
     'xdsl2LConfProfClassMask': {},
     'xdsl2LConfProfDpboEPsd': {},
     'xdsl2LConfProfDpboEsCableModelA': {},
     'xdsl2LConfProfDpboEsCableModelB': {},
     'xdsl2LConfProfDpboEsCableModelC': {},
     'xdsl2LConfProfDpboEsEL': {},
     'xdsl2LConfProfDpboFMax': {},
     'xdsl2LConfProfDpboFMin': {},
     'xdsl2LConfProfDpboMus': {},
     'xdsl2LConfProfForceInp': {},
     'xdsl2LConfProfL0Time': {},
     'xdsl2LConfProfL2Atpr': {},
     'xdsl2LConfProfL2Atprt': {},
     'xdsl2LConfProfL2Time': {},
     'xdsl2LConfProfLimitMask': {},
     'xdsl2LConfProfMaxAggRxPwrUs': {},
     'xdsl2LConfProfMaxNomAtpDs': {},
     'xdsl2LConfProfMaxNomAtpUs': {},
     'xdsl2LConfProfMaxNomPsdDs': {},
     'xdsl2LConfProfMaxNomPsdUs': {},
     'xdsl2LConfProfMaxSnrmDs': {},
     'xdsl2LConfProfMaxSnrmUs': {},
     'xdsl2LConfProfMinSnrmDs': {},
     'xdsl2LConfProfMinSnrmUs': {},
     'xdsl2LConfProfModeSpecBandUsRowStatus': {},
     'xdsl2LConfProfModeSpecRowStatus': {},
     'xdsl2LConfProfMsgMinDs': {},
     'xdsl2LConfProfMsgMinUs': {},
     'xdsl2LConfProfPmMode': {},
     'xdsl2LConfProfProfiles': {},
     'xdsl2LConfProfPsdMaskDs': {},
     'xdsl2LConfProfPsdMaskSelectUs': {},
     'xdsl2LConfProfPsdMaskUs': {},
     'xdsl2LConfProfRaDsNrmDs': {},
     'xdsl2LConfProfRaDsNrmUs': {},
     'xdsl2LConfProfRaDsTimeDs': {},
     'xdsl2LConfProfRaDsTimeUs': {},
     'xdsl2LConfProfRaModeDs': {},
     'xdsl2LConfProfRaModeUs': {},
     'xdsl2LConfProfRaUsNrmDs': {},
     'xdsl2LConfProfRaUsNrmUs': {},
     'xdsl2LConfProfRaUsTimeDs': {},
     'xdsl2LConfProfRaUsTimeUs': {},
     'xdsl2LConfProfRfiBands': {},
     'xdsl2LConfProfRowStatus': {},
     'xdsl2LConfProfScMaskDs': {},
     'xdsl2LConfProfScMaskUs': {},
     'xdsl2LConfProfSnrModeDs': {},
     'xdsl2LConfProfSnrModeUs': {},
     'xdsl2LConfProfTargetSnrmDs': {},
     'xdsl2LConfProfTargetSnrmUs': {},
     'xdsl2LConfProfTxRefVnDs': {},
     'xdsl2LConfProfTxRefVnUs': {},
     'xdsl2LConfProfUpboKL': {},
     'xdsl2LConfProfUpboKLF': {},
     'xdsl2LConfProfUpboPsdA': {},
     'xdsl2LConfProfUpboPsdB': {},
     'xdsl2LConfProfUs0Disable': {},
     'xdsl2LConfProfUs0Mask': {},
     'xdsl2LConfProfVdsl2CarMask': {},
     'xdsl2LConfProfXtuTransSysEna': {},
     'xdsl2LConfTempChan1ConfProfile': {},
     'xdsl2LConfTempChan1RaRatioDs': {},
     'xdsl2LConfTempChan1RaRatioUs': {},
     'xdsl2LConfTempChan2ConfProfile': {},
     'xdsl2LConfTempChan2RaRatioDs': {},
     'xdsl2LConfTempChan2RaRatioUs': {},
     'xdsl2LConfTempChan3ConfProfile': {},
     'xdsl2LConfTempChan3RaRatioDs': {},
     'xdsl2LConfTempChan3RaRatioUs': {},
     'xdsl2LConfTempChan4ConfProfile': {},
     'xdsl2LConfTempChan4RaRatioDs': {},
     'xdsl2LConfTempChan4RaRatioUs': {},
     'xdsl2LConfTempLineProfile': {},
     'xdsl2LConfTempRowStatus': {},
     'xdsl2LInvG994VendorId': {},
     'xdsl2LInvSelfTestResult': {},
     'xdsl2LInvSerialNumber': {},
     'xdsl2LInvSystemVendorId': {},
     'xdsl2LInvTransmissionCapabilities': {},
     'xdsl2LInvVersionNumber': {},
     'xdsl2LineAlarmConfProfileRowStatus': {},
     'xdsl2LineAlarmConfProfileThresh15MinFailedFullInt': {},
     'xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt': {},
     'xdsl2LineAlarmConfProfileXtucThresh15MinEs': {},
     'xdsl2LineAlarmConfProfileXtucThresh15MinFecs': {},
     'xdsl2LineAlarmConfProfileXtucThresh15MinLoss': {},
     'xdsl2LineAlarmConfProfileXtucThresh15MinSes': {},
     'xdsl2LineAlarmConfProfileXtucThresh15MinUas': {},
     'xdsl2LineAlarmConfProfileXturThresh15MinEs': {},
     'xdsl2LineAlarmConfProfileXturThresh15MinFecs': {},
     'xdsl2LineAlarmConfProfileXturThresh15MinLoss': {},
     'xdsl2LineAlarmConfProfileXturThresh15MinSes': {},
     'xdsl2LineAlarmConfProfileXturThresh15MinUas': {},
     'xdsl2LineAlarmConfTemplate': {},
     'xdsl2LineBandStatusLnAtten': {},
     'xdsl2LineBandStatusSigAtten': {},
     'xdsl2LineBandStatusSnrMargin': {},
     'xdsl2LineCmndAutomodeColdStart': {},
     'xdsl2LineCmndConfBpsc': {},
     'xdsl2LineCmndConfBpscFailReason': {},
     'xdsl2LineCmndConfBpscRequests': {},
     'xdsl2LineCmndConfLdsf': {},
     'xdsl2LineCmndConfLdsfFailReason': {},
     'xdsl2LineCmndConfPmsf': {},
     'xdsl2LineCmndConfReset': {},
     'xdsl2LineConfFallbackTemplate': {},
     'xdsl2LineConfTemplate': {},
     'xdsl2LineSegmentBitsAlloc': {},
     'xdsl2LineSegmentRowStatus': {},
     'xdsl2LineStatusActAtpDs': {},
     'xdsl2LineStatusActAtpUs': {},
     'xdsl2LineStatusActLimitMask': {},
     'xdsl2LineStatusActProfile': {},
     'xdsl2LineStatusActPsdDs': {},
     'xdsl2LineStatusActPsdUs': {},
     'xdsl2LineStatusActSnrModeDs': {},
     'xdsl2LineStatusActSnrModeUs': {},
     'xdsl2LineStatusActTemplate': {},
     'xdsl2LineStatusActUs0Mask': {},
     'xdsl2LineStatusActualCe': {},
     'xdsl2LineStatusAttainableRateDs': {},
     'xdsl2LineStatusAttainableRateUs': {},
     'xdsl2LineStatusElectricalLength': {},
     'xdsl2LineStatusInitResult': {},
     'xdsl2LineStatusLastStateDs': {},
     'xdsl2LineStatusLastStateUs': {},
     'xdsl2LineStatusMrefPsdDs': {},
     'xdsl2LineStatusMrefPsdUs': {},
     'xdsl2LineStatusPwrMngState': {},
     'xdsl2LineStatusTrellisDs': {},
     'xdsl2LineStatusTrellisUs': {},
     'xdsl2LineStatusTssiDs': {},
     'xdsl2LineStatusTssiUs': {},
     'xdsl2LineStatusXtuTransSys': {},
     'xdsl2LineStatusXtuc': {},
     'xdsl2LineStatusXtur': {},
     'xdsl2PMChCurr15MCodingViolations': {},
     'xdsl2PMChCurr15MCorrectedBlocks': {},
     'xdsl2PMChCurr15MInvalidIntervals': {},
     'xdsl2PMChCurr15MTimeElapsed': {},
     'xdsl2PMChCurr15MValidIntervals': {},
     'xdsl2PMChCurr1DayCodingViolations': {},
     'xdsl2PMChCurr1DayCorrectedBlocks': {},
     'xdsl2PMChCurr1DayInvalidIntervals': {},
     'xdsl2PMChCurr1DayTimeElapsed': {},
     'xdsl2PMChCurr1DayValidIntervals': {},
     'xdsl2PMChHist15MCodingViolations': {},
     'xdsl2PMChHist15MCorrectedBlocks': {},
     'xdsl2PMChHist15MMonitoredTime': {},
     'xdsl2PMChHist15MValidInterval': {},
     'xdsl2PMChHist1DCodingViolations': {},
     'xdsl2PMChHist1DCorrectedBlocks': {},
     'xdsl2PMChHist1DMonitoredTime': {},
     'xdsl2PMChHist1DValidInterval': {},
     'xdsl2PMLCurr15MEs': {},
     'xdsl2PMLCurr15MFecs': {},
     'xdsl2PMLCurr15MInvalidIntervals': {},
     'xdsl2PMLCurr15MLoss': {},
     'xdsl2PMLCurr15MSes': {},
     'xdsl2PMLCurr15MTimeElapsed': {},
     'xdsl2PMLCurr15MUas': {},
     'xdsl2PMLCurr15MValidIntervals': {},
     'xdsl2PMLCurr1DayEs': {},
     'xdsl2PMLCurr1DayFecs': {},
     'xdsl2PMLCurr1DayInvalidIntervals': {},
     'xdsl2PMLCurr1DayLoss': {},
     'xdsl2PMLCurr1DaySes': {},
     'xdsl2PMLCurr1DayTimeElapsed': {},
     'xdsl2PMLCurr1DayUas': {},
     'xdsl2PMLCurr1DayValidIntervals': {},
     'xdsl2PMLHist15MEs': {},
     'xdsl2PMLHist15MFecs': {},
     'xdsl2PMLHist15MLoss': {},
     'xdsl2PMLHist15MMonitoredTime': {},
     'xdsl2PMLHist15MSes': {},
     'xdsl2PMLHist15MUas': {},
     'xdsl2PMLHist15MValidInterval': {},
     'xdsl2PMLHist1DEs': {},
     'xdsl2PMLHist1DFecs': {},
     'xdsl2PMLHist1DLoss': {},
     'xdsl2PMLHist1DMonitoredTime': {},
     'xdsl2PMLHist1DSes': {},
     'xdsl2PMLHist1DUas': {},
     'xdsl2PMLHist1DValidInterval': {},
     'xdsl2PMLInitCurr15MFailedFullInits': {},
     'xdsl2PMLInitCurr15MFailedShortInits': {},
     'xdsl2PMLInitCurr15MFullInits': {},
     'xdsl2PMLInitCurr15MInvalidIntervals': {},
     'xdsl2PMLInitCurr15MShortInits': {},
     'xdsl2PMLInitCurr15MTimeElapsed': {},
     'xdsl2PMLInitCurr15MValidIntervals': {},
     'xdsl2PMLInitCurr1DayFailedFullInits': {},
     'xdsl2PMLInitCurr1DayFailedShortInits': {},
     'xdsl2PMLInitCurr1DayFullInits': {},
     'xdsl2PMLInitCurr1DayInvalidIntervals': {},
     'xdsl2PMLInitCurr1DayShortInits': {},
     'xdsl2PMLInitCurr1DayTimeElapsed': {},
     'xdsl2PMLInitCurr1DayValidIntervals': {},
     'xdsl2PMLInitHist15MFailedFullInits': {},
     'xdsl2PMLInitHist15MFailedShortInits': {},
     'xdsl2PMLInitHist15MFullInits': {},
     'xdsl2PMLInitHist15MMonitoredTime': {},
     'xdsl2PMLInitHist15MShortInits': {},
     'xdsl2PMLInitHist15MValidInterval': {},
     'xdsl2PMLInitHist1DFailedFullInits': {},
     'xdsl2PMLInitHist1DFailedShortInits': {},
     'xdsl2PMLInitHist1DFullInits': {},
     'xdsl2PMLInitHist1DMonitoredTime': {},
     'xdsl2PMLInitHist1DShortInits': {},
     'xdsl2PMLInitHist1DValidInterval': {},
     'xdsl2SCStatusAttainableRate': {},
     'xdsl2SCStatusBandLnAtten': {},
     'xdsl2SCStatusBandSigAtten': {},
     'xdsl2SCStatusLinScGroupSize': {},
     'xdsl2SCStatusLinScale': {},
     'xdsl2SCStatusLogMt': {},
     'xdsl2SCStatusLogScGroupSize': {},
     'xdsl2SCStatusQlnMt': {},
     'xdsl2SCStatusQlnScGroupSize': {},
     'xdsl2SCStatusRowStatus': {},
     'xdsl2SCStatusSegmentBitsAlloc': {},
     'xdsl2SCStatusSegmentGainAlloc': {},
     'xdsl2SCStatusSegmentLinImg': {},
     'xdsl2SCStatusSegmentLinReal': {},
     'xdsl2SCStatusSegmentLog': {},
     'xdsl2SCStatusSegmentQln': {},
     'xdsl2SCStatusSegmentSnr': {},
     'xdsl2SCStatusSnrMtime': {},
     'xdsl2SCStatusSnrScGroupSize': {},
     'xdsl2ScalarSCAvailInterfaces': {},
     'xdsl2ScalarSCMaxInterfaces': {},
     'zipEntry': {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}}}

    golden_output1 = {'execute.return_value': '''
            Router#show snmp mib
            Load for five secs: 24%/0%; one minute: 24%; five minutes: 25%
            Time source is NTP, 17:04:50.878 EST Tue Sep 13 2016

            lldpLocalSystemData.1
            lldpLocalSystemData.2
            lldpLocalSystemData.3
            lldpLocalSystemData.4
            lldpLocalSystemData.5
            lldpLocalSystemData.6
            lldpLocPortEntry.2
            lldpLocPortEntry.3
            lldpLocPortEntry.4
            lldpLocManAddrEntry.3
            lldpLocManAddrEntry.4
            lldpLocManAddrEntry.5
            lldpLocManAddrEntry.6
            lldpRemEntry.4
            lldpRemEntry.5
            lldpRemEntry.6
            lldpRemEntry.7
            lldpRemEntry.8
            lldpRemEntry.9
            lldpRemEntry.10
            lldpRemEntry.11
            lldpRemEntry.12
            lldpRemManAddrEntry.3
            lldpRemManAddrEntry.4
            lldpRemManAddrEntry.5
            lldpRemUnknownTLVEntry.2
            lldpRemOrgDefInfoEntry.4
            dot3adAggMACAddress
            dot3adAggActorSystemPriority
            dot3adAggActorSystemID
            dot3adAggAggregateOrIndividual
            dot3adAggActorAdminKey
            dot3adAggActorOperKey
            dot3adAggPartnerSystemID
            dot3adAggPartnerSystemPriority
            dot3adAggPartnerOperKey
            dot3adAggCollectorMaxDelay
            dot3adAggPortListPorts
            dot3adAggPortActorSystemPriority
            dot3adAggPortActorSystemID
            dot3adAggPortActorAdminKey
            dot3adAggPortActorOperKey
            dot3adAggPortPartnerAdminSystemPriority
            dot3adAggPortPartnerOperSystemPriority
            dot3adAggPortPartnerAdminSystemID
            dot3adAggPortPartnerOperSystemID
            dot3adAggPortPartnerAdminKey
            dot3adAggPortPartnerOperKey
            dot3adAggPortSelectedAggID
            dot3adAggPortAttachedAggID
            dot3adAggPortActorPort
            dot3adAggPortActorPortPriority
            dot3adAggPortPartnerAdminPort
            dot3adAggPortPartnerOperPort
            dot3adAggPortPartnerAdminPortPriority
            dot3adAggPortPartnerOperPortPriority
            dot3adAggPortActorAdminState
            dot3adAggPortActorOperState
            dot3adAggPortPartnerAdminState
            dot3adAggPortPartnerOperState
            dot3adAggPortAggregateOrIndividual
            dot3adAggPortStatsLACPDUsRx
            dot3adAggPortStatsMarkerPDUsRx
            dot3adAggPortStatsMarkerResponsePDUsRx
            dot3adAggPortStatsUnknownRx
            dot3adAggPortStatsIllegalRx
            dot3adAggPortStatsLACPDUsTx
            dot3adAggPortStatsMarkerPDUsTx
            dot3adAggPortStatsMarkerResponsePDUsTx
            dot3adAggPortDebugRxState
            dot3adAggPortDebugLastRxTime
            dot3adAggPortDebugMuxState
            dot3adAggPortDebugMuxReason
            dot3adAggPortDebugActorChurnState
            dot3adAggPortDebugPartnerChurnState
            dot3adAggPortDebugActorChurnCount
            dot3adAggPortDebugPartnerChurnCount
            dot3adAggPortDebugActorSyncTransitionCount
            dot3adAggPortDebugPartnerSyncTransitionCount
            dot3adAggPortDebugActorChangeCount
            dot3adAggPortDebugPartnerChangeCount
            dot3adTablesLastChanged
            system.1
            system.2
            sysUpTime
            system.4
            system.5
            system.6
            system.7
            system.8
            sysOREntry.2
            sysOREntry.3
            sysOREntry.4
            ifNumber
            ifIndex
            ifDescr
            ifType
            ifMtu
            ifSpeed
            ifPhysAddress
            ifAdminStatus
            ifOperStatus
            ifLastChange
            ifInOctets
            ifInUcastPkts
            ifInNUcastPkts
            ifInDiscards
            ifInErrors
            ifInUnknownProtos
            ifOutOctets
            ifOutUcastPkts
            ifOutNUcastPkts
            ifOutDiscards
            ifOutErrors
            ifOutQLen
            ifSpecific
            atEntry.1
            atEntry.2
            atEntry.3
            ip.1
            ip.2
            ip.3
            ip.4
            ip.5
            ip.6
            ip.7
            ip.8
            ip.9
            ip.10
            ip.11
            ip.12
            ip.13
            ip.14
            ip.15
            ip.16
            ip.17
            ip.18
            ip.19
            ipAddrEntry.1
            ipAddrEntry.2
            ipAddrEntry.3
            ipAddrEntry.4
            ipAddrEntry.5
            ipNetToMediaEntry.1
            ipNetToMediaEntry.2
            ipNetToMediaEntry.3
            ipNetToMediaEntry.4
            ip.23
            ipForward.3
            ipCidrRouteEntry.1
            ipCidrRouteEntry.2
            ipCidrRouteEntry.3
            ipCidrRouteEntry.4
            ipCidrRouteEntry.5
            ipCidrRouteEntry.6
            ipCidrRouteEntry.7
            ipCidrRouteEntry.8
            ipCidrRouteEntry.9
            ipCidrRouteEntry.10
            ipCidrRouteEntry.11
            ipCidrRouteEntry.12
            ipCidrRouteEntry.13
            ipCidrRouteEntry.14
            ipCidrRouteEntry.15
            ipCidrRouteEntry.16
            ipForward.6
            inetCidrRouteEntry.7
            inetCidrRouteEntry.8
            inetCidrRouteEntry.9
            inetCidrRouteEntry.10
            inetCidrRouteEntry.11
            inetCidrRouteEntry.12
            inetCidrRouteEntry.13
            inetCidrRouteEntry.14
            inetCidrRouteEntry.15
            inetCidrRouteEntry.16
            inetCidrRouteEntry.17
            ip.25
            ip.26
            ip.27
            ipv4InterfaceEntry.2
            ipv4InterfaceEntry.3
            ipv4InterfaceEntry.4
            ip.29
            ipv6InterfaceEntry.2
            ipv6InterfaceEntry.3
            ipv6InterfaceEntry.5
            ipv6InterfaceEntry.6
            ipv6InterfaceEntry.7
            ipv6InterfaceEntry.8
            ipSystemStatsEntry.3
            ipSystemStatsEntry.4
            ipSystemStatsEntry.5
            ipSystemStatsEntry.6
            ipSystemStatsEntry.7
            ipSystemStatsEntry.8
            ipSystemStatsEntry.9
            ipSystemStatsEntry.10
            ipSystemStatsEntry.11
            ipSystemStatsEntry.12
            ipSystemStatsEntry.13
            ipSystemStatsEntry.14
            ipSystemStatsEntry.15
            ipSystemStatsEntry.16
            ipSystemStatsEntry.17
            ipSystemStatsEntry.18
            ipSystemStatsEntry.19
            ipSystemStatsEntry.20
            ipSystemStatsEntry.21
            ipSystemStatsEntry.22
            ipSystemStatsEntry.23
            ipSystemStatsEntry.24
            ipSystemStatsEntry.25
            ipSystemStatsEntry.26
            ipSystemStatsEntry.27
            ipSystemStatsEntry.28
            ipSystemStatsEntry.29
            ipSystemStatsEntry.30
            ipSystemStatsEntry.31
            ipSystemStatsEntry.32
            ipSystemStatsEntry.33
            ipSystemStatsEntry.34
            ipSystemStatsEntry.35
            ipSystemStatsEntry.36
            ipSystemStatsEntry.37
            ipSystemStatsEntry.38
            ipSystemStatsEntry.39
            ipSystemStatsEntry.40
            ipSystemStatsEntry.41
            ipSystemStatsEntry.42
            ipSystemStatsEntry.43
            ipSystemStatsEntry.44
            ipSystemStatsEntry.45
            ipSystemStatsEntry.46
            ipTrafficStats.2
            ipIfStatsEntry.3
            ipIfStatsEntry.4
            ipIfStatsEntry.5
            ipIfStatsEntry.6
            ipIfStatsEntry.7
            ipIfStatsEntry.8
            ipIfStatsEntry.9
            ipIfStatsEntry.10
            ipIfStatsEntry.11
            ipIfStatsEntry.12
            ipIfStatsEntry.13
            ipIfStatsEntry.14
            ipIfStatsEntry.15
            ipIfStatsEntry.16
            ipIfStatsEntry.17
            ipIfStatsEntry.18
            ipIfStatsEntry.19
            ipIfStatsEntry.20
            ipIfStatsEntry.21
            ipIfStatsEntry.23
            ipIfStatsEntry.24
            ipIfStatsEntry.25
            ipIfStatsEntry.26
            ipIfStatsEntry.27
            ipIfStatsEntry.28
            ipIfStatsEntry.29
            ipIfStatsEntry.30
            ipIfStatsEntry.31
            ipIfStatsEntry.32
            ipIfStatsEntry.33
            ipIfStatsEntry.34
            ipIfStatsEntry.35
            ipIfStatsEntry.36
            ipIfStatsEntry.37
            ipIfStatsEntry.38
            ipIfStatsEntry.39
            ipIfStatsEntry.40
            ipIfStatsEntry.41
            ipIfStatsEntry.42
            ipIfStatsEntry.43
            ipIfStatsEntry.44
            ipIfStatsEntry.45
            ipIfStatsEntry.46
            ipAddressPrefixEntry.5
            ipAddressPrefixEntry.6
            ipAddressPrefixEntry.7
            ipAddressPrefixEntry.8
            ipAddressPrefixEntry.9
            ip.33
            ipAddressEntry.3
            ipAddressEntry.4
            ipAddressEntry.5
            ipAddressEntry.6
            ipAddressEntry.7
            ipAddressEntry.8
            ipAddressEntry.9
            ipAddressEntry.10
            ipAddressEntry.11
            ipNetToPhysicalEntry.4
            ipNetToPhysicalEntry.5
            ipNetToPhysicalEntry.6
            ipNetToPhysicalEntry.7
            ipNetToPhysicalEntry.8
            ipv6ScopeZoneIndexEntry.2
            ipv6ScopeZoneIndexEntry.3
            ipv6ScopeZoneIndexEntry.4
            ipv6ScopeZoneIndexEntry.5
            ipv6ScopeZoneIndexEntry.6
            ipv6ScopeZoneIndexEntry.7
            ipv6ScopeZoneIndexEntry.8
            ipv6ScopeZoneIndexEntry.9
            ipv6ScopeZoneIndexEntry.10
            ipv6ScopeZoneIndexEntry.11
            ipv6ScopeZoneIndexEntry.12
            ipv6ScopeZoneIndexEntry.13
            ipDefaultRouterEntry.4
            ipDefaultRouterEntry.5
            ip.38
            ipv6RouterAdvertEntry.2
            ipv6RouterAdvertEntry.3
            ipv6RouterAdvertEntry.4
            ipv6RouterAdvertEntry.5
            ipv6RouterAdvertEntry.6
            ipv6RouterAdvertEntry.7
            ipv6RouterAdvertEntry.8
            ipv6RouterAdvertEntry.9
            ipv6RouterAdvertEntry.10
            ipv6RouterAdvertEntry.11
            ipv6RouterAdvertEntry.12
            icmp.1
            icmp.2
            icmp.3
            icmp.4
            icmp.5
            icmp.6
            icmp.7
            icmp.8
            icmp.9
            icmp.10
            icmp.11
            icmp.12
            icmp.13
            icmp.14
            icmp.15
            icmp.16
            icmp.17
            icmp.18
            icmp.19
            icmp.20
            icmp.21
            icmp.22
            icmp.23
            icmp.24
            icmp.25
            icmp.26
            icmpStatsEntry.2
            icmpStatsEntry.3
            icmpStatsEntry.4
            icmpStatsEntry.5
            icmpMsgStatsEntry.3
            icmpMsgStatsEntry.4
            tcp.1
            tcp.2
            tcp.3
            tcp.4
            tcp.5
            tcp.6
            tcp.7
            tcp.8
            tcp.9
            tcp.10
            tcp.11
            tcp.12
            tcpConnEntry.1
            tcpConnEntry.2
            tcpConnEntry.3
            tcpConnEntry.4
            tcpConnEntry.5
            tcp.14
            tcp.15
            tcp.17
            tcp.18
            tcp.19.1.7
            tcp.19.1.8
            tcp.20.1.4
            udp.1
            udp.2
            udp.3
            udp.4
            udpEntry.1
            udpEntry.2
            udp.7.1.8
            udp.8
            udp.9
            x25AdmnEntry.1
            x25AdmnEntry.2
            x25AdmnEntry.3
            x25AdmnEntry.4
            x25AdmnEntry.5
            x25AdmnEntry.6
            x25AdmnEntry.7
            x25AdmnEntry.8
            x25AdmnEntry.9
            x25AdmnEntry.10
            x25AdmnEntry.11
            x25AdmnEntry.12
            x25AdmnEntry.13
            x25AdmnEntry.14
            x25AdmnEntry.15
            x25AdmnEntry.16
            x25AdmnEntry.17
            x25AdmnEntry.18
            x25AdmnEntry.19
            x25AdmnEntry.20
            x25AdmnEntry.21
            x25AdmnEntry.22
            x25AdmnEntry.23
            x25AdmnEntry.24
            x25OperEntry.1
            x25OperEntry.2
            x25OperEntry.3
            x25OperEntry.4
            x25OperEntry.5
            x25OperEntry.6
            x25OperEntry.7
            x25OperEntry.8
            x25OperEntry.9
            x25OperEntry.10
            x25OperEntry.11
            x25OperEntry.12
            x25OperEntry.13
            x25OperEntry.14
            x25OperEntry.15
            x25OperEntry.16
            x25OperEntry.17
            x25OperEntry.18
            x25OperEntry.19
            x25OperEntry.20
            x25OperEntry.21
            x25OperEntry.22
            x25OperEntry.23
            x25OperEntry.24
            x25OperEntry.25
            x25StatEntry.1
            x25StatEntry.2
            x25StatEntry.3
            x25StatEntry.4
            x25StatEntry.5
            x25StatEntry.6
            x25StatEntry.7
            x25StatEntry.8
            x25StatEntry.9
            x25StatEntry.10
            x25StatEntry.11
            x25StatEntry.12
            x25StatEntry.13
            x25StatEntry.14
            x25StatEntry.15
            x25StatEntry.16
            x25StatEntry.17
            x25StatEntry.18
            x25StatEntry.19
            x25StatEntry.20
            x25StatEntry.21
            x25StatEntry.22
            x25StatEntry.23
            x25StatEntry.24
            x25StatEntry.25
            x25ChannelEntry.1
            x25ChannelEntry.2
            x25ChannelEntry.3
            x25ChannelEntry.4
            x25ChannelEntry.5
            x25ChannelEntry.6
            x25ChannelEntry.7
            x25CircuitEntry.1
            x25CircuitEntry.2
            x25CircuitEntry.3
            x25CircuitEntry.4
            x25CircuitEntry.5
            x25CircuitEntry.6
            x25CircuitEntry.7
            x25CircuitEntry.8
            x25CircuitEntry.9
            x25CircuitEntry.10
            x25CircuitEntry.11
            x25CircuitEntry.12
            x25CircuitEntry.13
            x25CircuitEntry.14
            x25CircuitEntry.15
            x25CircuitEntry.16
            x25CircuitEntry.17
            x25CircuitEntry.18
            x25CircuitEntry.19
            x25CircuitEntry.20
            x25CircuitEntry.21
            x25.6
            x25.7
            x25ClearedCircuitEntry.1
            x25ClearedCircuitEntry.2
            x25ClearedCircuitEntry.3
            x25ClearedCircuitEntry.4
            x25ClearedCircuitEntry.5
            x25ClearedCircuitEntry.6
            x25ClearedCircuitEntry.7
            x25ClearedCircuitEntry.8
            x25ClearedCircuitEntry.9
            x25ClearedCircuitEntry.10
            x25ClearedCircuitEntry.11
            x25ClearedCircuitEntry.12
            x25CallParmEntry.1
            x25CallParmEntry.2
            x25CallParmEntry.3
            x25CallParmEntry.4
            x25CallParmEntry.5
            x25CallParmEntry.6
            x25CallParmEntry.7
            x25CallParmEntry.8
            x25CallParmEntry.9
            x25CallParmEntry.10
            x25CallParmEntry.11
            x25CallParmEntry.12
            x25CallParmEntry.13
            x25CallParmEntry.14
            x25CallParmEntry.15
            x25CallParmEntry.16
            x25CallParmEntry.17
            x25CallParmEntry.18
            x25CallParmEntry.19
            x25CallParmEntry.20
            x25CallParmEntry.21
            x25CallParmEntry.22
            x25CallParmEntry.23
            x25CallParmEntry.24
            x25CallParmEntry.25
            x25CallParmEntry.26
            x25CallParmEntry.27
            x25CallParmEntry.28
            x25CallParmEntry.29
            x25CallParmEntry.30
            dot3StatsEntry.1
            dot3StatsEntry.2
            dot3StatsEntry.3
            dot3StatsEntry.4
            dot3StatsEntry.5
            dot3StatsEntry.6
            dot3StatsEntry.7
            dot3StatsEntry.8
            dot3StatsEntry.9
            dot3StatsEntry.10
            dot3StatsEntry.11
            dot3StatsEntry.13
            dot3StatsEntry.16
            dot3StatsEntry.17
            dot3StatsEntry.18
            dot3StatsEntry.19
            dot3StatsEntry.20
            dot3StatsEntry.21
            dot3CollEntry.3
            dot3ControlEntry.1
            dot3ControlEntry.2
            dot3ControlEntry.3
            dot3PauseEntry.1
            dot3PauseEntry.2
            dot3PauseEntry.3
            dot3PauseEntry.4
            dot3PauseEntry.5
            dot3PauseEntry.6
            dot10.196.1.1
            dot10.196.1.2
            dot10.196.1.3
            dot10.196.1.4
            dot10.196.1.5
            dot10.196.1.6
            dot5Entry.1
            dot5Entry.2
            dot5Entry.3
            dot5Entry.4
            dot5Entry.5
            dot5Entry.6
            dot5Entry.7
            dot5Entry.8
            dot5Entry.9
            dot5StatsEntry.1
            dot5StatsEntry.2
            dot5StatsEntry.3
            dot5StatsEntry.4
            dot5StatsEntry.5
            dot5StatsEntry.6
            dot5StatsEntry.7
            dot5StatsEntry.8
            dot5StatsEntry.9
            dot5StatsEntry.10
            dot5StatsEntry.11
            dot5StatsEntry.12
            dot5StatsEntry.13
            dot5StatsEntry.14
            dot5StatsEntry.15
            dot5StatsEntry.16
            dot5StatsEntry.17
            dot5StatsEntry.18
            dot5StatsEntry.19
            lapbAdmnEntry.1
            lapbAdmnEntry.2
            lapbAdmnEntry.3
            lapbAdmnEntry.4
            lapbAdmnEntry.5
            lapbAdmnEntry.6
            lapbAdmnEntry.7
            lapbAdmnEntry.8
            lapbAdmnEntry.9
            lapbAdmnEntry.10
            lapbAdmnEntry.11
            lapbAdmnEntry.12
            lapbAdmnEntry.13
            lapbAdmnEntry.14
            lapbOperEntry.1
            lapbOperEntry.2
            lapbOperEntry.3
            lapbOperEntry.4
            lapbOperEntry.5
            lapbOperEntry.6
            lapbOperEntry.7
            lapbOperEntry.8
            lapbOperEntry.9
            lapbOperEntry.10
            lapbOperEntry.11
            lapbOperEntry.12
            lapbOperEntry.13
            lapbOperEntry.14
            lapbFlowEntry.1
            lapbFlowEntry.2
            lapbFlowEntry.3
            lapbFlowEntry.4
            lapbFlowEntry.5
            lapbFlowEntry.6
            lapbFlowEntry.7
            lapbFlowEntry.8
            lapbFlowEntry.9
            lapbFlowEntry.10
            lapbFlowEntry.11
            lapbXidEntry.1
            lapbXidEntry.2
            lapbXidEntry.3
            lapbXidEntry.4
            lapbXidEntry.5
            lapbXidEntry.6
            lapbXidEntry.7
            dsx1ConfigEntry.1
            dsx1ConfigEntry.2
            dsx1ConfigEntry.3
            dsx1ConfigEntry.4
            dsx1ConfigEntry.5
            dsx1ConfigEntry.6
            dsx1ConfigEntry.7
            dsx1ConfigEntry.8
            dsx1ConfigEntry.9
            dsx1ConfigEntry.10
            dsx1ConfigEntry.11
            dsx1ConfigEntry.12
            dsx1ConfigEntry.13
            dsx1ConfigEntry.14
            dsx1ConfigEntry.15
            dsx1ConfigEntry.16
            dsx1ConfigEntry.17
            dsx1ConfigEntry.18
            dsx1ConfigEntry.19
            dsx1ConfigEntry.20
            dsx1CurrentEntry.1
            dsx1CurrentEntry.2
            dsx1CurrentEntry.3
            dsx1CurrentEntry.4
            dsx1CurrentEntry.5
            dsx1CurrentEntry.6
            dsx1CurrentEntry.7
            dsx1CurrentEntry.8
            dsx1CurrentEntry.9
            dsx1CurrentEntry.10
            dsx1CurrentEntry.11
            dsx1IntervalEntry.1
            dsx1IntervalEntry.2
            dsx1IntervalEntry.3
            dsx1IntervalEntry.4
            dsx1IntervalEntry.5
            dsx1IntervalEntry.6
            dsx1IntervalEntry.7
            dsx1IntervalEntry.8
            dsx1IntervalEntry.9
            dsx1IntervalEntry.10
            dsx1IntervalEntry.11
            dsx1IntervalEntry.12
            dsx1IntervalEntry.13
            dsx1TotalEntry.1
            dsx1TotalEntry.2
            dsx1TotalEntry.3
            dsx1TotalEntry.4
            dsx1TotalEntry.5
            dsx1TotalEntry.6
            dsx1TotalEntry.7
            dsx1TotalEntry.8
            dsx1TotalEntry.9
            dsx1TotalEntry.10
            dsx1TotalEntry.11
            ds10.121.1.1
            ds10.121.1.2
            ds10.121.1.3
            ds10.121.1.4
            ds10.121.1.5
            ds10.121.1.6
            ds10.121.1.7
            ds10.121.1.8
            ds10.121.1.9
            ds10.121.1.10
            ds10.121.1.11
            ds10.121.1.12
            ds10.121.1.13
            ds10.144.1.1
            ds10.144.1.2
            ds10.144.1.3
            ds10.144.1.4
            ds10.144.1.5
            ds10.144.1.6
            ds10.144.1.7
            ds10.144.1.8
            ds10.144.1.9
            ds10.144.1.10
            ds10.144.1.11
            ds10.144.1.12
            ds10.169.1.1
            ds10.169.1.2
            ds10.169.1.3
            ds10.169.1.4
            ds10.169.1.5
            ds10.169.1.6
            ds10.169.1.7
            ds10.169.1.8
            ds10.169.1.9
            ds10.169.1.10
            dsx1FracEntry.1
            dsx1FracEntry.2
            dsx1FracEntry.3
            ds10.34.1.1
            isdnBasicRateEntry.1
            isdnBasicRateEntry.2
            isdnBasicRateEntry.3
            isdnBasicRateEntry.4
            isdnBearerEntry.1
            isdnBearerEntry.2
            isdnBearerEntry.3
            isdnBearerEntry.4
            isdnBearerEntry.5
            isdnBearerEntry.6
            isdnBearerEntry.7
            isdnBearerEntry.8
            isdnBearerEntry.9
            isdnBearerEntry.10
            isdnBearerEntry.11
            isdnSignalingGetIndex
            isdnSignalingEntry.2
            isdnSignalingEntry.3
            isdnSignalingEntry.4
            isdnSignalingEntry.5
            isdnSignalingEntry.6
            isdnSignalingEntry.7
            isdnSignalingEntry.8
            isdnSignalingStatsEntry.1
            isdnSignalingStatsEntry.2
            isdnSignalingStatsEntry.3
            isdnSignalingStatsEntry.4
            isdnSignalingStatsEntry.5
            isdnMib.10.16.4.1.1
            isdnMib.10.16.4.1.2
            isdnMib.10.16.4.1.3
            isdnMib.10.16.4.1.4
            isdnEndpointGetIndex
            isdnEndpointEntry.2
            isdnEndpointEntry.3
            isdnEndpointEntry.4
            isdnEndpointEntry.5
            isdnEndpointEntry.6
            isdnEndpointEntry.7
            isdnDirectoryEntry.2
            isdnDirectoryEntry.3
            isdnDirectoryEntry.4
            dialCtlAcceptMode
            dialCtlTrapEnable
            dialCtlPeerCfgIfType
            dialCtlPeerCfgLowerIf
            dialCtlPeerCfgOriginateAddress
            dialCtlPeerCfgAnswerAddress
            dialCtlPeerCfgSubAddress
            dialCtlPeerCfgSpeed
            dialCtlPeerCfgInfoType
            dialCtlPeerCfgPermission
            dialCtlPeerCfgInactivityTimer
            dialCtlPeerCfgMinDuration
            dialCtlPeerCfgMaxDuration
            dialCtlPeerCfgCarrierDelay
            dialCtlPeerCfgCallRetries
            dialCtlPeerCfgRetryDelay
            dialCtlPeerCfgFailureDelay
            dialCtlPeerCfgTrapEnable
            dialCtlPeerCfgStatus
            dialCtlPeerStatsConnectTime
            dialCtlPeerStatsChargedUnits
            dialCtlPeerStatsSuccessCalls
            dialCtlPeerStatsFailCalls
            dialCtlPeerStatsAcceptCalls
            dialCtlPeerStatsRefuseCalls
            dialCtlPeerStatsLastDisconnectCause
            dialCtlPeerStatsLastDisconnectText
            dialCtlPeerStatsLastSetupTime
            callActivePeerAddress
            callActivePeerSubAddress
            callActivePeerId
            callActivePeerIfIndex
            callActiveLogicalIfIndex
            callActiveConnectTime
            callActiveCallState
            callActiveCallOrigin
            callActiveChargedUnits
            callActiveInfoType
            callActiveTransmitPackets
            callActiveTransmitBytes
            callActiveReceivePackets
            callActiveReceiveBytes
            callHistoryTableMaxLength
            callHistoryRetainTimer
            callHistoryPeerAddress
            callHistoryPeerSubAddress
            callHistoryPeerId
            callHistoryPeerIfIndex
            callHistoryLogicalIfIndex
            callHistoryDisconnectCause
            callHistoryDisconnectText
            callHistoryConnectTime
            callHistoryDisconnectTime
            callHistoryCallOrigin
            callHistoryChargedUnits
            callHistoryInfoType
            callHistoryTransmitPackets
            callHistoryTransmitBytes
            callHistoryReceivePackets
            callHistoryReceiveBytes
            dsx3ConfigEntry.1
            dsx3ConfigEntry.2
            dsx3ConfigEntry.3
            dsx3ConfigEntry.4
            dsx3ConfigEntry.5
            dsx3ConfigEntry.6
            dsx3ConfigEntry.7
            dsx3ConfigEntry.8
            dsx3ConfigEntry.9
            dsx3ConfigEntry.10
            dsx3ConfigEntry.11
            dsx3ConfigEntry.12
            dsx3ConfigEntry.13
            dsx3ConfigEntry.14
            dsx3ConfigEntry.15
            dsx3ConfigEntry.16
            dsx3ConfigEntry.17
            dsx3ConfigEntry.18
            dsx3CurrentEntry.1
            dsx3CurrentEntry.2
            dsx3CurrentEntry.3
            dsx3CurrentEntry.4
            dsx3CurrentEntry.5
            dsx3CurrentEntry.6
            dsx3CurrentEntry.7
            dsx3CurrentEntry.8
            dsx3CurrentEntry.9
            dsx3CurrentEntry.10
            dsx3CurrentEntry.11
            dsx3IntervalEntry.1
            dsx3IntervalEntry.2
            dsx3IntervalEntry.3
            dsx3IntervalEntry.4
            dsx3IntervalEntry.5
            dsx3IntervalEntry.6
            dsx3IntervalEntry.7
            dsx3IntervalEntry.8
            dsx3IntervalEntry.9
            dsx3IntervalEntry.10
            dsx3IntervalEntry.11
            dsx3IntervalEntry.12
            dsx3IntervalEntry.13
            dsx3TotalEntry.1
            dsx3TotalEntry.2
            dsx3TotalEntry.3
            dsx3TotalEntry.4
            dsx3TotalEntry.5
            dsx3TotalEntry.6
            dsx3TotalEntry.7
            dsx3TotalEntry.8
            dsx3TotalEntry.9
            dsx3TotalEntry.10
            dsx3TotalEntry.11
            ds10.169.1.8
            ds10.196.1.7
            dsx3FracEntry.1
            dsx3FracEntry.2
            dsx3FracEntry.3
            frDlcmiEntry.1
            frDlcmiEntry.2
            frDlcmiEntry.3
            frDlcmiEntry.4
            frDlcmiEntry.5
            frDlcmiEntry.6
            frDlcmiEntry.7
            frDlcmiEntry.8
            frDlcmiEntry.9
            frDlcmiEntry.10
            frCircuitEntry.1
            frCircuitEntry.2
            frCircuitEntry.3
            frCircuitEntry.4
            frCircuitEntry.5
            frCircuitEntry.6
            frCircuitEntry.7
            frCircuitEntry.8
            frCircuitEntry.9
            frCircuitEntry.10
            frCircuitEntry.11
            frCircuitEntry.12
            frCircuitEntry.13
            frCircuitEntry.14
            frTrapState
            rs232.1
            rs232PortEntry.1
            rs232PortEntry.2
            rs232PortEntry.3
            rs232PortEntry.4
            rs232PortEntry.5
            rs232PortEntry.6
            rs232PortEntry.7
            rs232PortEntry.8
            rs232AsyncPortEntry.1
            rs232AsyncPortEntry.2
            rs232AsyncPortEntry.3
            rs232AsyncPortEntry.4
            rs232AsyncPortEntry.5
            rs232AsyncPortEntry.6
            rs232AsyncPortEntry.7
            rs232AsyncPortEntry.8
            rs232SyncPortEntry.1
            rs232SyncPortEntry.2
            rs232SyncPortEntry.3
            rs232SyncPortEntry.4
            rs232SyncPortEntry.5
            rs232SyncPortEntry.6
            rs232SyncPortEntry.7
            rs232SyncPortEntry.8
            rs232SyncPortEntry.9
            rs232SyncPortEntry.10
            rs232SyncPortEntry.11
            rs232SyncPortEntry.12
            rs232SyncPortEntry.13
            rs232SyncPortEntry.14
            rs232InSigEntry.1
            rs232InSigEntry.2
            rs232InSigEntry.3
            rs232OutSigEntry.1
            rs232OutSigEntry.2
            rs232OutSigEntry.3
            sonetMediumEntry.1
            sonetMediumEntry.2
            sonetMediumEntry.3
            sonetMediumEntry.4
            sonetMediumEntry.5
            sonetMediumEntry.6
            sonetMediumEntry.7
            sonetMediumEntry.8
            sonetMedium.2
            sonetSectionCurrentEntry.1
            sonetSectionCurrentEntry.2
            sonetSectionCurrentEntry.3
            sonetSectionCurrentEntry.4
            sonetSectionCurrentEntry.5
            sonetSectionIntervalEntry.2
            sonetSectionIntervalEntry.3
            sonetSectionIntervalEntry.4
            sonetSectionIntervalEntry.5
            sonetSectionIntervalEntry.6
            sonetLineCurrentEntry.1
            sonetLineCurrentEntry.2
            sonetLineCurrentEntry.3
            sonetLineCurrentEntry.4
            sonetLineCurrentEntry.5
            sonetLineIntervalEntry.2
            sonetLineIntervalEntry.3
            sonetLineIntervalEntry.4
            sonetLineIntervalEntry.5
            sonetLineIntervalEntry.6
            sonetFarEndLineCurrentEntry.1
            sonetFarEndLineCurrentEntry.2
            sonetFarEndLineCurrentEntry.3
            sonetFarEndLineCurrentEntry.4
            sonetFarEndLineIntervalEntry.2
            sonetFarEndLineIntervalEntry.3
            sonetFarEndLineIntervalEntry.4
            sonetFarEndLineIntervalEntry.5
            sonetFarEndLineIntervalEntry.6
            sonetPathCurrentEntry.1
            sonetPathCurrentEntry.2
            sonetPathCurrentEntry.3
            sonetPathCurrentEntry.4
            sonetPathCurrentEntry.5
            sonetPathCurrentEntry.6
            sonetPathIntervalEntry.2
            sonetPathIntervalEntry.3
            sonetPathIntervalEntry.4
            sonetPathIntervalEntry.5
            sonetPathIntervalEntry.6
            sonetFarEndPathCurrentEntry.1
            sonetFarEndPathCurrentEntry.2
            sonetFarEndPathCurrentEntry.3
            sonetFarEndPathCurrentEntry.4
            sonetFarEndPathIntervalEntry.2
            sonetFarEndPathIntervalEntry.3
            sonetFarEndPathIntervalEntry.4
            sonetFarEndPathIntervalEntry.5
            sonetFarEndPathIntervalEntry.6
            sonetVTCurrentEntry.1
            sonetVTCurrentEntry.2
            sonetVTCurrentEntry.3
            sonetVTCurrentEntry.4
            sonetVTCurrentEntry.5
            sonetVTCurrentEntry.6
            sonetVTIntervalEntry.2
            sonetVTIntervalEntry.3
            sonetVTIntervalEntry.4
            sonetVTIntervalEntry.5
            sonetVTIntervalEntry.6
            sonetFarEndVTCurrentEntry.1
            sonetFarEndVTCurrentEntry.2
            sonetFarEndVTCurrentEntry.3
            sonetFarEndVTCurrentEntry.4
            sonetFarEndVTIntervalEntry.2
            sonetFarEndVTIntervalEntry.3
            sonetFarEndVTIntervalEntry.4
            sonetFarEndVTIntervalEntry.5
            sonetFarEndVTIntervalEntry.6
            mfrBundleMaxNumBundles
            mfrBundleNextIndex
            mfrBundleIfIndex
            mfrBundleRowStatus
            mfrBundleNearEndName
            mfrBundleFragmentation
            mfrBundleMaxFragSize
            mfrBundleTimerHello
            mfrBundleTimerAck
            mfrBundleCountMaxRetry
            mfrBundleActivationClass
            mfrBundleThreshold
            mfrBundleMaxDiffDelay
            mfrBundleSeqNumSize
            mfrBundleMaxBundleLinks
            mfrBundleLinksConfigured
            mfrBundleLinksActive
            mfrBundleBandwidth
            mfrBundleFarEndName
            mfrBundleResequencingErrors
            mfrBundleIfIndexMappingIndex
            mfrBundleLinkRowStatus
            mfrBundleLinkConfigBundleIndex
            mfrBundleLinkNearEndName
            mfrBundleLinkState
            mfrBundleLinkFarEndName
            mfrBundleLinkFarEndBundleName
            mfrBundleLinkDelay
            mfrBundleLinkFramesControlTx
            mfrBundleLinkFramesControlRx
            mfrBundleLinkFramesControlInvalid
            mfrBundleLinkTimerExpiredCount
            mfrBundleLinkLoopbackSuspected
            mfrBundleLinkUnexpectedSequence
            mfrBundleLinkMismatch
            adslLineCoding
            adslLineType
            adslLineSpecific
            adslLineConfProfile
            adslLineAlarmConfProfile
            adslAtucInvSerialNumber
            adslAtucInvVendorID
            adslAtucInvVersionNumber
            adslAtucCurrSnrMgn
            adslAtucCurrAtn
            adslAtucCurrStatus
            adslAtucCurrOutputPwr
            adslAtucCurrAttainableRate
            adslAturInvSerialNumber
            adslAturInvVendorID
            adslAturInvVersionNumber
            adslAturCurrSnrMgn
            adslAturCurrAtn
            adslAturCurrStatus
            adslAturCurrOutputPwr
            adslAturCurrAttainableRate
            adslAtucChanInterleaveDelay
            adslAtucChanCurrTxRate
            adslAtucChanPrevTxRate
            adslAtucChanCrcBlockLength
            adslAturChanInterleaveDelay
            adslAturChanCurrTxRate
            adslAturChanPrevTxRate
            adslAturChanCrcBlockLength
            adslAtucPerfLofs
            adslAtucPerfLoss
            adslAtucPerfLols
            adslAtucPerfLprs
            adslAtucPerfESs
            adslAtucPerfInits
            adslAtucPerfValidIntervals
            adslAtucPerfInvalidIntervals
            adslAtucPerfCurr15MinTimeElapsed
            adslAtucPerfCurr15MinLofs
            adslAtucPerfCurr15MinLoss
            adslAtucPerfCurr15MinLols
            adslAtucPerfCurr15MinLprs
            adslAtucPerfCurr15MinESs
            adslAtucPerfCurr15MinInits
            adslAtucPerfCurr1DayTimeElapsed
            adslAtucPerfCurr1DayLofs
            adslAtucPerfCurr1DayLoss
            adslAtucPerfCurr1DayLols
            adslAtucPerfCurr1DayLprs
            adslAtucPerfCurr1DayESs
            adslAtucPerfCurr1DayInits
            adslAtucPerfPrev1DayMoniSecs
            adslAtucPerfPrev1DayLofs
            adslAtucPerfPrev1DayLoss
            adslAtucPerfPrev1DayLols
            adslAtucPerfPrev1DayLprs
            adslAtucPerfPrev1DayESs
            adslAtucPerfPrev1DayInits
            adslAturPerfLofs
            adslAturPerfLoss
            adslAturPerfLprs
            adslAturPerfESs
            adslAturPerfValidIntervals
            adslAturPerfInvalidIntervals
            adslAturPerfCurr15MinTimeElapsed
            adslAturPerfCurr15MinLofs
            adslAturPerfCurr15MinLoss
            adslAturPerfCurr15MinLprs
            adslAturPerfCurr15MinESs
            adslAturPerfCurr1DayTimeElapsed
            adslAturPerfCurr1DayLofs
            adslAturPerfCurr1DayLoss
            adslAturPerfCurr1DayLprs
            adslAturPerfCurr1DayESs
            adslAturPerfPrev1DayMoniSecs
            adslAturPerfPrev1DayLofs
            adslAturPerfPrev1DayLoss
            adslAturPerfPrev1DayLprs
            adslAturPerfPrev1DayESs
            adslAtucIntervalLofs
            adslAtucIntervalLoss
            adslAtucIntervalLols
            adslAtucIntervalLprs
            adslAtucIntervalESs
            adslAtucIntervalInits
            adslAtucIntervalValidData
            adslAturIntervalLofs
            adslAturIntervalLoss
            adslAturIntervalLprs
            adslAturIntervalESs
            adslAturIntervalValidData
            adslAtucChanReceivedBlks
            adslAtucChanTransmittedBlks
            adslAtucChanCorrectedBlks
            adslAtucChanUncorrectBlks
            adslAtucChanPerfValidIntervals
            adslAtucChanPerfInvalidIntervals
            adslAtucChanPerfCurr15MinTimeElapsed
            adslAtucChanPerfCurr15MinReceivedBlks
            adslAtucChanPerfCurr15MinTransmittedBlks
            adslAtucChanPerfCurr15MinCorrectedBlks
            adslAtucChanPerfCurr15MinUncorrectBlks
            adslAtucChanPerfCurr1DayTimeElapsed
            adslAtucChanPerfCurr1DayReceivedBlks
            adslAtucChanPerfCurr1DayTransmittedBlks
            adslAtucChanPerfCurr1DayCorrectedBlks
            adslAtucChanPerfCurr1DayUncorrectBlks
            adslAtucChanPerfPrev1DayMoniSecs
            adslAtucChanPerfPrev1DayReceivedBlks
            adslAtucChanPerfPrev1DayTransmittedBlks
            adslAtucChanPerfPrev1DayCorrectedBlks
            adslAtucChanPerfPrev1DayUncorrectBlks
            adslAturChanReceivedBlks
            adslAturChanTransmittedBlks
            adslAturChanCorrectedBlks
            adslAturChanUncorrectBlks
            adslAturChanPerfValidIntervals
            adslAturChanPerfInvalidIntervals
            adslAturChanPerfCurr15MinTimeElapsed
            adslAturChanPerfCurr15MinReceivedBlks
            adslAturChanPerfCurr15MinTransmittedBlks
            adslAturChanPerfCurr15MinCorrectedBlks
            adslAturChanPerfCurr15MinUncorrectBlks
            adslAturChanPerfCurr1DayTimeElapsed
            adslAturChanPerfCurr1DayReceivedBlks
            adslAturChanPerfCurr1DayTransmittedBlks
            adslAturChanPerfCurr1DayCorrectedBlks
            adslAturChanPerfCurr1DayUncorrectBlks
            adslAturChanPerfPrev1DayMoniSecs
            adslAturChanPerfPrev1DayReceivedBlks
            adslAturChanPerfPrev1DayTransmittedBlks
            adslAturChanPerfPrev1DayCorrectedBlks
            adslAturChanPerfPrev1DayUncorrectBlks
            adslAtucChanIntervalReceivedBlks
            adslAtucChanIntervalTransmittedBlks
            adslAtucChanIntervalCorrectedBlks
            adslAtucChanIntervalUncorrectBlks
            adslAtucChanIntervalValidData
            adslAturChanIntervalReceivedBlks
            adslAturChanIntervalTransmittedBlks
            adslAturChanIntervalCorrectedBlks
            adslAturChanIntervalUncorrectBlks
            adslAturChanIntervalValidData
            adslAtucConfRateMode
            adslAtucConfRateChanRatio
            adslAtucConfTargetSnrMgn
            adslAtucConfMaxSnrMgn
            adslAtucConfMinSnrMgn
            adslAtucConfDownshiftSnrMgn
            adslAtucConfUpshiftSnrMgn
            adslAtucConfMinUpshiftTime
            adslAtucConfMinDownshiftTime
            adslAtucChanConfFastMinTxRate
            adslAtucChanConfInterleaveMinTxRate
            adslAtucChanConfFastMaxTxRate
            adslAtucChanConfInterleaveMaxTxRate
            adslAtucChanConfMaxInterleaveDelay
            adslAturConfRateMode
            adslAturConfRateChanRatio
            adslAturConfTargetSnrMgn
            adslAturConfMaxSnrMgn
            adslAturConfMinSnrMgn
            adslAturConfDownshiftSnrMgn
            adslAturConfUpshiftSnrMgn
            adslAturConfMinUpshiftTime
            adslAturConfMinDownshiftTime
            adslAturChanConfFastMinTxRate
            adslAturChanConfInterleaveMinTxRate
            adslAturChanConfFastMaxTxRate
            adslAturChanConfInterleaveMaxTxRate
            adslAturChanConfMaxInterleaveDelay
            adslLineConfProfileRowStatus
            adslAtucThresh15MinLofs
            adslAtucThresh15MinLoss
            adslAtucThresh15MinLols
            adslAtucThresh15MinLprs
            adslAtucThresh15MinESs
            adslAtucThreshFastRateUp
            adslAtucThreshInterleaveRateUp
            adslAtucThreshFastRateDown
            adslAtucThreshInterleaveRateDown
            adslAtucInitFailureTrapEnable
            adslAturThresh15MinLofs
            adslAturThresh15MinLoss
            adslAturThresh15MinLprs
            adslAturThresh15MinESs
            adslAturThreshFastRateUp
            adslAturThreshInterleaveRateUp
            adslAturThreshFastRateDown
            adslAturThreshInterleaveRateDown
            adslLineAlarmConfProfileRowStatus
            adslLineDmtTrellis
            adslLineDmtEOC
            adslAtucDmtIssue
            adslAtucDmtState
            adslAtucDmtInterleavePath
            adslAtucDmtFastPath
            adslAturDmtIssue
            adslAturDmtState
            adslAturDmtInterleavePath
            adslAturDmtFastPath
            adslAtucDmtConfFreqBins
            adslAturDmtConfFreqBins
            adslLineDmtConfMode
            adslLineDmtConfTrellis
            adslLineDmtConfEOC
            adslAtucDmtConfInterleavePath
            adslAtucDmtConfFastPath
            adslAturDmtConfInterleavePath
            adslAturDmtConfFastPath
            tunnelIfLocalAddress
            tunnelIfRemoteAddress
            tunnelIfEncapsMethod
            tunnelIfHopLimit
            tunnelIfSecurity
            tunnelIfTOS
            tunnelIfFlowLabel
            tunnelIfAddressType
            tunnelIfLocalInetAddress
            tunnelIfRemoteInetAddress
            tunnelIfEncapsLimit
            tunnelConfigIfIndex
            tunnelConfigStatus
            tunnelInetConfigIfIndex
            tunnelInetConfigStatus
            tunnelInetConfigStorageType
            optIfObjects.10.4.1.1
            optIfObjects.10.4.1.2
            optIfObjects.10.4.1.3
            optIfObjects.10.4.1.4
            optIfObjects.10.4.1.5
            optIfObjects.10.4.1.6
            optIfObjects.10.9.1.1
            optIfObjects.10.9.1.2
            optIfObjects.10.9.1.3
            optIfObjects.10.9.1.4
            optIfObjects.10.16.1.1
            optIfObjects.10.16.1.2
            optIfObjects.10.16.1.3
            optIfObjects.10.16.1.4
            optIfObjects.10.16.1.5
            optIfObjects.10.16.1.6
            optIfObjects.10.16.1.7
            optIfObjects.10.16.1.8
            optIfObjects.10.16.1.9
            optIfObjects.10.16.1.10
            optIfObjects.10.25.1.1
            optIfObjects.10.25.1.2
            optIfObjects.10.25.1.3
            optIfObjects.10.25.1.4
            optIfObjects.10.25.1.5
            optIfObjects.10.25.1.6
            optIfObjects.10.25.1.7
            optIfObjects.10.25.1.8
            optIfObjects.10.25.1.9
            optIfObjects.10.25.1.10
            optIfObjects.10.25.1.11
            optIfObjects.10.36.1.2
            optIfObjects.10.36.1.3
            optIfObjects.10.36.1.4
            optIfObjects.10.36.1.5
            optIfObjects.10.36.1.6
            optIfObjects.10.36.1.7
            optIfObjects.10.36.1.8
            optIfObjects.10.49.1.1
            optIfObjects.10.49.1.2
            optIfObjects.10.49.1.3
            optIfObjects.10.49.1.4
            optIfObjects.10.49.1.5
            optIfObjects.10.64.1.1
            optIfObjects.10.64.1.2
            optIfObjects.10.64.1.3
            optIfObjects.10.64.1.4
            optIfObjects.10.64.1.5
            optIfObjects.10.64.1.6
            optIfObjects.10.64.1.7
            optIfObjects.10.81.1.1
            optIfObjects.10.81.1.2
            optIfObjects.10.81.1.3
            optIfObjects.10.81.1.4
            optIfObjects.10.81.1.5
            optIfObjects.10.81.1.6
            optIfObjects.10.81.1.7
            optIfObjects.10.81.1.8
            optIfObjects.10.81.1.9
            optIfObjects.10.81.1.10
            optIfObjects.10.81.1.11
            optIfObjects.10.100.1.2
            optIfObjects.10.100.1.3
            optIfObjects.10.100.1.4
            optIfObjects.10.100.1.5
            optIfObjects.10.100.1.6
            optIfObjects.10.100.1.7
            optIfObjects.10.100.1.8
            optIfObjects.10.121.1.1
            optIfObjects.10.121.1.2
            optIfObjects.10.121.1.3
            optIfObjects.10.121.1.4
            optIfObjects.10.121.1.5
            optIfObjects.10.144.1.1
            optIfObjects.10.144.1.2
            optIfObjects.10.144.1.3
            optIfObjects.10.144.1.4
            optIfObjects.10.144.1.5
            optIfObjects.10.144.1.6
            optIfObjects.10.144.1.7
            optIfObjects.10.25.1.1
            optIfObjects.10.25.1.2
            optIfObjects.10.36.1.1
            optIfObjects.10.36.1.2
            optIfObjects.10.36.1.3
            optIfObjects.10.36.1.4
            optIfObjects.10.36.1.5
            optIfObjects.10.36.1.6
            optIfObjects.10.36.1.7
            optIfObjects.10.36.1.8
            optIfObjects.10.36.1.9
            optIfObjects.10.36.1.10
            optIfObjects.10.36.1.11
            optIfObjects.10.49.1.2
            optIfObjects.10.49.1.3
            optIfObjects.10.49.1.4
            optIfObjects.10.49.1.5
            optIfObjects.10.49.1.6
            optIfObjects.10.49.1.7
            optIfObjects.10.49.1.8
            optIfObjects.10.64.1.1
            optIfObjects.10.64.1.2
            optIfObjects.10.64.1.3
            optIfObjects.10.64.1.4
            optIfObjects.10.64.1.5
            optIfObjects.10.81.1.1
            optIfObjects.10.81.1.2
            optIfObjects.10.81.1.3
            optIfObjects.10.81.1.4
            optIfObjects.10.81.1.5
            optIfObjects.10.81.1.6
            optIfObjects.10.81.1.7
            optIfObjects.10.100.1.1
            optIfObjects.10.100.1.2
            optIfObjects.10.100.1.3
            optIfObjects.10.100.1.4
            optIfObjects.10.100.1.5
            optIfObjects.10.100.1.6
            optIfObjects.10.100.1.7
            optIfObjects.10.100.1.8
            optIfObjects.10.100.1.9
            optIfObjects.10.100.1.10
            optIfObjects.10.100.1.11
            optIfObjects.10.121.1.2
            optIfObjects.10.121.1.3
            optIfObjects.10.121.1.4
            optIfObjects.10.121.1.5
            optIfObjects.10.121.1.6
            optIfObjects.10.121.1.7
            optIfObjects.10.121.1.8
            optIfObjects.10.144.1.1
            optIfObjects.10.144.1.2
            optIfObjects.10.144.1.3
            optIfObjects.10.144.1.4
            optIfObjects.10.144.1.5
            optIfObjects.10.169.1.1
            optIfObjects.10.169.1.2
            optIfObjects.10.169.1.3
            optIfObjects.10.169.1.4
            optIfObjects.10.169.1.5
            optIfObjects.10.169.1.6
            optIfObjects.10.169.1.7
            optIfObjects.10.36.1.1
            optIfObjects.10.49.1.1
            optIfObjects.10.49.1.2
            optIfObjects.10.49.1.3
            optIfObjects.10.49.1.4
            optIfObjects.10.49.1.5
            optIfObjects.10.49.1.6
            optIfObjects.10.49.1.7
            optIfObjects.10.49.1.8
            optIfObjects.10.49.1.9
            optIfObjects.10.49.1.10
            optIfObjects.10.49.1.11
            optIfObjects.10.64.1.2
            optIfObjects.10.64.1.3
            optIfObjects.10.64.1.4
            optIfObjects.10.64.1.5
            optIfObjects.10.64.1.6
            optIfObjects.10.64.1.7
            optIfObjects.10.64.1.8
            optIfObjects.10.81.1.1
            optIfObjects.10.81.1.2
            optIfObjects.10.81.1.3
            optIfObjects.10.81.1.4
            optIfObjects.10.81.1.5
            optIfObjects.10.100.1.1
            optIfObjects.10.100.1.2
            optIfObjects.10.100.1.3
            optIfObjects.10.100.1.4
            optIfObjects.10.100.1.5
            optIfObjects.10.100.1.6
            optIfObjects.10.100.1.7
            optIfObjects.10.121.1.1
            optIfObjects.10.121.1.2
            optIfObjects.10.121.1.3
            optIfObjects.10.121.1.4
            optIfObjects.10.121.1.5
            optIfObjects.10.121.1.6
            optIfObjects.10.121.1.7
            optIfObjects.10.121.1.8
            optIfObjects.10.121.1.9
            optIfObjects.10.121.1.10
            optIfObjects.10.121.1.11
            optIfObjects.10.144.1.2
            optIfObjects.10.144.1.3
            optIfObjects.10.144.1.4
            optIfObjects.10.144.1.5
            optIfObjects.10.144.1.6
            optIfObjects.10.144.1.7
            optIfObjects.10.144.1.8
            optIfObjects.10.169.1.1
            optIfObjects.10.169.1.2
            optIfObjects.10.169.1.3
            optIfObjects.10.169.1.4
            optIfObjects.10.169.1.5
            optIfObjects.10.196.1.1
            optIfObjects.10.196.1.2
            optIfObjects.10.196.1.3
            optIfObjects.10.196.1.4
            optIfObjects.10.196.1.5
            optIfObjects.10.196.1.6
            optIfObjects.10.196.1.7
            optIfOChDirectionality
            optIfOChCurrentStatus
            optIfOChSinkCurrentSuspectedFlag
            optIfOChSinkCurrentInputPower
            optIfOChSinkCurrentLowInputPower
            optIfOChSinkCurrentHighInputPower
            optIfOChSinkCurrentLowerInputPowerThreshold
            optIfOChSinkCurrentUpperInputPowerThreshold
            optIfOChSinkIntervalSuspectedFlag
            optIfOChSinkIntervalLastInputPower
            optIfOChSinkIntervalLowInputPower
            optIfOChSinkIntervalHighInputPower
            optIfOChSinkCurDaySuspectedFlag
            optIfOChSinkCurDayLowInputPower
            optIfOChSinkCurDayHighInputPower
            optIfOChSinkPrevDaySuspectedFlag
            optIfOChSinkPrevDayLastInputPower
            optIfOChSinkPrevDayLowInputPower
            optIfOChSinkPrevDayHighInputPower
            optIfOChSrcCurrentSuspectedFlag
            optIfOChSrcCurrentOutputPower
            optIfOChSrcCurrentLowOutputPower
            optIfOChSrcCurrentHighOutputPower
            optIfOChSrcCurrentLowerOutputPowerThreshold
            optIfOChSrcCurrentUpperOutputPowerThreshold
            optIfOChSrcIntervalSuspectedFlag
            optIfOChSrcIntervalLastOutputPower
            optIfOChSrcIntervalLowOutputPower
            optIfOChSrcIntervalHighOutputPower
            optIfOChSrcCurDaySuspectedFlag
            optIfOChSrcCurDayLowOutputPower
            optIfOChSrcCurDayHighOutputPower
            optIfOChSrcPrevDaySuspectedFlag
            optIfOChSrcPrevDayLastOutputPower
            optIfOChSrcPrevDayLowOutputPower
            optIfOChSrcPrevDayHighOutputPower
            optIfOTUkDirectionality
            optIfOTUkBitRateK
            optIfOTUkTraceIdentifierTransmitted
            optIfOTUkDAPIExpected
            optIfOTUkSAPIExpected
            optIfOTUkTraceIdentifierAccepted
            optIfOTUkTIMDetMode
            optIfOTUkTIMActEnabled
            optIfOTUkDEGThr
            optIfOTUkDEGM
            optIfOTUkSinkAdaptActive
            optIfOTUkSourceAdaptActive
            optIfOTUkSinkFECEnabled
            optIfOTUkCurrentStatus
            optIfOTUk.2.1.2
            optIfOTUk.2.1.3
            optIfObjects.10.81.1.1
            optIfObjects.10.81.1.2
            optIfObjects.10.81.1.3
            optIfObjects.10.81.1.4
            optIfObjects.10.81.1.5
            optIfODUkTtpTraceIdentifierTransmitted
            optIfODUkTtpDAPIExpected
            optIfODUkTtpSAPIExpected
            optIfODUkTtpTraceIdentifierAccepted
            optIfODUkTtpTIMDetMode
            optIfODUkTtpTIMActEnabled
            optIfODUkTtpDEGThr
            optIfODUkTtpDEGM
            optIfODUkTtpCurrentStatus
            optIfObjects.10.121.1.2
            optIfObjects.10.121.1.3
            optIfObjects.10.144.1.2
            optIfObjects.10.144.1.3
            optIfObjects.10.144.1.4
            optIfObjects.10.144.1.5
            optIfObjects.10.144.1.6
            optIfObjects.10.144.1.7
            optIfObjects.10.144.1.8
            optIfObjects.10.144.1.9
            optIfObjects.10.144.1.10
            optIfObjects.10.169.1.3
            optIfObjects.10.169.1.4
            optIfObjects.10.169.1.5
            optIfObjects.10.100.1.3
            optIfObjects.10.100.1.4
            optIfObjects.10.100.1.5
            optIfObjects.10.100.1.6
            optIfObjects.10.100.1.7
            optIfObjects.10.100.1.8
            optIfObjects.10.100.1.9
            optIfObjects.10.100.1.10
            optIfObjects.10.100.1.11
            optIfObjects.10.100.1.12
            optIfObjects.10.100.1.13
            optIfObjects.10.100.1.14
            optIfObjects.10.100.1.15
            optIfObjects.10.121.1.3
            optIfObjects.10.121.1.4
            optIfObjects.10.121.1.5
            optIfObjects.10.121.1.6
            optIfObjects.10.121.1.7
            optIfObjects.10.121.1.8
            optIfObjects.10.121.1.9
            optIfObjects.10.121.1.10
            optIfObjects.10.121.1.11
            etherWisDeviceTxTestPatternMode
            etherWisDeviceRxTestPatternMode
            etherWisDeviceRxTestPatternErrors
            etherWisSectionCurrentJ0Transmitted
            etherWisSectionCurrentJ0Received
            etherWisPathCurrentStatus
            etherWisPathCurrentJ1Transmitted
            etherWisPathCurrentJ1Received
            etherWisFarEndPathCurrentStatus
            mplsInterfaceLabelMinIn
            mplsInterfaceLabelMaxIn
            mplsInterfaceLabelMinOut
            mplsInterfaceLabelMaxOut
            mplsInterfaceTotalBandwidth
            mplsInterfaceAvailableBandwidth
            mplsInterfaceLabelParticipationType
            mplsInterfacePerfInLabelsInUse
            mplsInterfacePerfInLabelLookupFailures
            mplsInterfacePerfOutLabelsInUse
            mplsInterfacePerfOutFragmentedPkts
            mplsInSegmentIndexNext
            mplsInSegmentInterface
            mplsInSegmentLabel
            mplsInSegmentLabelPtr
            mplsInSegmentNPop
            mplsInSegmentAddrFamily
            mplsInSegmentXCIndex
            mplsInSegmentOwner
            mplsInSegmentTrafficParamPtr
            mplsInSegmentRowStatus
            mplsInSegmentStorageType
            mplsInSegmentPerfOctets
            mplsInSegmentPerfPackets
            mplsInSegmentPerfErrors
            mplsInSegmentPerfDiscards
            mplsInSegmentPerfHCOctets
            mplsInSegmentPerfDiscontinuityTime
            mplsOutSegmentIndexNext
            mplsOutSegmentInterface
            mplsOutSegmentPushTopLabel
            mplsOutSegmentTopLabel
            mplsOutSegmentTopLabelPtr
            mplsOutSegmentNextHopAddrType
            mplsOutSegmentNextHopAddr
            mplsOutSegmentXCIndex
            mplsOutSegmentOwner
            mplsOutSegmentTrafficParamPtr
            mplsOutSegmentRowStatus
            mplsOutSegmentStorageType
            mplsOutSegmentPerfOctets
            mplsOutSegmentPerfPackets
            mplsOutSegmentPerfErrors
            mplsOutSegmentPerfDiscards
            mplsOutSegmentPerfHCOctets
            mplsOutSegmentPerfDiscontinuityTime
            mplsXCIndexNext
            mplsXCLspId
            mplsXCLabelStackIndex
            mplsXCOwner
            mplsXCRowStatus
            mplsXCStorageType
            mplsXCAdminStatus
            mplsXCOperStatus
            mplsMaxLabelStackDepth
            mplsLabelStackIndexNext
            mplsLabelStackLabel
            mplsLabelStackLabelPtr
            mplsLabelStackRowStatus
            mplsLabelStackStorageType
            mplsInSegmentMapIndex
            mplsXCNotificationsEnable
            mplsTunnelConfigured
            mplsTunnelActive
            mplsTunnelTEDistProto
            mplsTunnelMaxHops
            mplsTunnelNotificationMaxRate
            mplsTunnelIndexNext
            mplsTunnelEntry.5
            mplsTunnelEntry.6
            mplsTunnelEntry.7
            mplsTunnelEntry.8
            mplsTunnelEntry.9
            mplsTunnelEntry.10
            mplsTunnelEntry.11
            mplsTunnelEntry.12
            mplsTunnelEntry.13
            mplsTunnelEntry.14
            mplsTunnelEntry.15
            mplsTunnelEntry.16
            mplsTunnelEntry.17
            mplsTunnelEntry.18
            mplsTunnelEntry.19
            mplsTunnelEntry.20
            mplsTunnelEntry.21
            mplsTunnelEntry.22
            mplsTunnelEntry.23
            mplsTunnelEntry.24
            mplsTunnelEntry.25
            mplsTunnelEntry.26
            mplsTunnelEntry.27
            mplsTunnelEntry.28
            mplsTunnelEntry.29
            mplsTunnelEntry.30
            mplsTunnelEntry.31
            mplsTunnelEntry.32
            mplsTunnelEntry.33
            mplsTunnelAdminStatus
            mplsTunnelOperStatus
            mplsTunnelEntry.36
            mplsTunnelEntry.37
            mplsTunnelHopListIndexNext
            mplsTunnelHopEntry.4
            mplsTunnelHopEntry.5
            mplsTunnelHopEntry.6
            mplsTunnelHopEntry.7
            mplsTunnelHopEntry.8
            mplsTunnelHopEntry.9
            mplsTunnelHopEntry.10
            mplsTunnelHopEntry.11
            mplsTunnelHopEntry.12
            mplsTunnelHopEntry.13
            mplsTunnelHopEntry.14
            mplsTunnelHopEntry.15
            mplsTunnelResourceIndexNext
            mplsTunnelResourceMaxRate
            mplsTunnelResourceEntry.3
            mplsTunnelResourceEntry.4
            mplsTunnelResourceEntry.5
            mplsTunnelResourceEntry.6
            mplsTunnelResourceEntry.7
            mplsTunnelResourceEntry.8
            mplsTunnelResourceEntry.9
            mplsTunnelResourceEntry.10
            mplsTunnelARHopEntry.3
            mplsTunnelARHopEntry.4
            mplsTunnelARHopEntry.5
            mplsTunnelARHopEntry.6
            mplsTunnelCHopEntry.3
            mplsTunnelCHopEntry.4
            mplsTunnelCHopEntry.5
            mplsTunnelCHopEntry.6
            mplsTunnelCHopEntry.7
            mplsTunnelCHopEntry.8
            mplsTunnelCHopEntry.9
            mplsTunnelPerfEntry.1
            mplsTunnelPerfEntry.2
            mplsTunnelPerfEntry.3
            mplsTunnelPerfEntry.4
            mplsTunnelPerfEntry.5
            mplsTeObjects.10.1.1
            mplsTeObjects.10.1.2
            mplsTeObjects.10.1.3
            mplsTeObjects.10.1.4
            mplsTeObjects.10.1.5
            mplsTeObjects.10.1.6
            mplsTeObjects.10.1.7
            mplsTunnelNotificationEnable
            mplsLdpLsrId
            mplsLdpLsrLoopDetectionCapable
            mplsLdpEntityLastChange
            mplsLdpEntityIndexNext
            mplsLdpEntityProtocolVersion
            mplsLdpEntityAdminStatus
            mplsLdpEntityOperStatus
            mplsLdpEntityTcpPort
            mplsLdpEntityUdpDscPort
            mplsLdpEntityMaxPduLength
            mplsLdpEntityKeepAliveHoldTimer
            mplsLdpEntityHelloHoldTimer
            mplsLdpEntityInitSessionThreshold
            mplsLdpEntityLabelDistMethod
            mplsLdpEntityLabelRetentionMode
            mplsLdpEntityPathVectorLimit
            mplsLdpEntityHopCountLimit
            mplsLdpEntityTransportAddrKind
            mplsLdpEntityTargetPeer
            mplsLdpEntityTargetPeerAddrType
            mplsLdpEntityTargetPeerAddr
            mplsLdpEntityLabelType
            mplsLdpEntityDiscontinuityTime
            mplsLdpEntityStorageType
            mplsLdpEntityRowStatus
            mplsLdpEntityStatsSessionAttempts
            mplsLdpEntityStatsSessionRejectedNoHelloErrors
            mplsLdpEntityStatsSessionRejectedAdErrors
            mplsLdpEntityStatsSessionRejectedMaxPduErrors
            mplsLdpEntityStatsSessionRejectedLRErrors
            mplsLdpEntityStatsBadLdpIdentifierErrors
            mplsLdpEntityStatsBadPduLengthErrors
            mplsLdpEntityStatsBadMessageLengthErrors
            mplsLdpEntityStatsBadTlvLengthErrors
            mplsLdpEntityStatsMalformedTlvValueErrors
            mplsLdpEntityStatsKeepAliveTimerExpErrors
            mplsLdpEntityStatsShutdownReceivedNotifications
            mplsLdpEntityStatsShutdownSentNotifications
            mplsLdpPeerLastChange
            mplsLdpPeerLabelDistMethod
            mplsLdpPeerPathVectorLimit
            mplsLdpPeerTransportAddrType
            mplsLdpPeerTransportAddr
            mplsLdpSessionStateLastChange
            mplsLdpSessionState
            mplsLdpSessionRole
            mplsLdpSessionProtocolVersion
            mplsLdpSessionKeepAliveHoldTimeRem
            mplsLdpSessionKeepAliveTime
            mplsLdpSessionMaxPduLength
            mplsLdpSessionDiscontinuityTime
            mplsLdpSessionStatsUnknownMesTypeErrors
            mplsLdpSessionStatsUnknownTlvErrors
            mplsLdpHelloAdjacencyHoldTimeRem
            mplsLdpHelloAdjacencyHoldTime
            mplsLdpHelloAdjacencyType
            mplsInSegmentLdpLspLabelType
            mplsInSegmentLdpLspType
            mplsOutSegmentLdpLspLabelType
            mplsOutSegmentLdpLspType
            mplsFecLastChange
            mplsFecIndexNext
            mplsFecType
            mplsFecAddrPrefixLength
            mplsFecAddrType
            mplsFecAddr
            mplsFecStorageType
            mplsFecRowStatus
            mplsLdpLspFecLastChange
            mplsLdpLspFecStorageType
            mplsLdpLspFecRowStatus
            mplsLdpSessionPeerNextHopAddrType
            mplsLdpSessionPeerNextHopAddr
            mplsLdpEntityAtmIfIndexOrZero
            mplsLdpEntityAtmMergeCap
            mplsLdpEntityAtmLRComponents
            mplsLdpEntityAtmVcDirectionality
            mplsLdpEntityAtmLsrConnectivity
            mplsLdpEntityAtmDefaultControlVpi
            mplsLdpEntityAtmDefaultControlVci
            mplsLdpEntityAtmUnlabTrafVpi
            mplsLdpEntityAtmUnlabTrafVci
            mplsLdpEntityAtmStorageType
            mplsLdpEntityAtmRowStatus
            mplsLdpEntityAtmLRMaxVpi
            mplsLdpEntityAtmLRMaxVci
            mplsLdpEntityAtmLRStorageType
            mplsLdpEntityAtmLRRowStatus
            mplsLdpSessionAtmLRUpperBoundVpi
            mplsLdpSessionAtmLRUpperBoundVci
            mplsLdpEntityGenericLabelSpace
            mplsLdpEntityGenericIfIndexOrZero
            mplsLdpEntityGenericLRStorageType
            mplsLdpEntityGenericLRRowStatus
            mplsL3VpnMIB.1.1.1
            mplsL3VpnMIB.1.1.2
            mplsL3VpnMIB.1.1.3
            mplsL3VpnMIB.1.1.4
            mplsL3VpnMIB.1.1.5
            mplsL3VpnMIB.1.1.6
            mplsL3VpnMIB.1.1.7
            mplsL3VpnIfConfEntry.2
            mplsL3VpnIfConfEntry.3
            mplsL3VpnIfConfEntry.4
            mplsL3VpnIfConfRowStatus
            mplsL3VpnVrfEntry.2
            mplsL3VpnVrfEntry.3
            mplsL3VpnVrfEntry.4
            mplsL3VpnVrfEntry.5
            mplsL3VpnVrfOperStatus
            mplsL3VpnVrfEntry.7
            mplsL3VpnVrfEntry.8
            mplsL3VpnVrfConfMidRteThresh
            mplsL3VpnVrfConfHighRteThresh
            mplsL3VpnVrfEntry.11
            mplsL3VpnVrfEntry.12
            mplsL3VpnVrfEntry.13
            mplsL3VpnVrfEntry.14
            mplsL3VpnVrfEntry.15
            mplsL3VpnVrfRTEntry.4
            mplsL3VpnVrfRTEntry.5
            mplsL3VpnVrfRTEntry.6
            mplsL3VpnVrfRTEntry.7
            mplsL3VpnVrfSecIllegalLblVltns
            mplsL3VpnVrfSecEntry.2
            mplsL3VpnVrfPerfEntry.1
            mplsL3VpnVrfPerfEntry.2
            mplsL3VpnVrfPerfCurrNumRoutes
            mplsL3VpnVrfPerfEntry.4
            mplsL3VpnVrfPerfEntry.5
            mplsL3VpnVrfRteEntry.7
            mplsL3VpnVrfRteEntry.8
            mplsL3VpnVrfRteEntry.9
            mplsL3VpnVrfRteEntry.10
            mplsL3VpnVrfRteEntry.11
            mplsL3VpnVrfRteEntry.12
            mplsL3VpnVrfRteEntry.13
            mplsL3VpnVrfRteEntry.14
            mplsL3VpnVrfRteEntry.15
            mplsL3VpnVrfRteEntry.16
            mplsL3VpnVrfRteEntry.17
            mplsL3VpnVrfRteEntry.18
            xdsl2LineConfTemplate
            xdsl2LineConfFallbackTemplate
            xdsl2LineAlarmConfTemplate
            xdsl2LineCmndConfPmsf
            xdsl2LineCmndConfLdsf
            xdsl2LineCmndConfLdsfFailReason
            xdsl2LineCmndConfBpsc
            xdsl2LineCmndConfBpscFailReason
            xdsl2LineCmndConfBpscRequests
            xdsl2LineCmndAutomodeColdStart
            xdsl2LineCmndConfReset
            xdsl2LineStatusActTemplate
            xdsl2LineStatusXtuTransSys
            xdsl2LineStatusPwrMngState
            xdsl2LineStatusInitResult
            xdsl2LineStatusLastStateDs
            xdsl2LineStatusLastStateUs
            xdsl2LineStatusXtur
            xdsl2LineStatusXtuc
            xdsl2LineStatusAttainableRateDs
            xdsl2LineStatusAttainableRateUs
            xdsl2LineStatusActPsdDs
            xdsl2LineStatusActPsdUs
            xdsl2LineStatusActAtpDs
            xdsl2LineStatusActAtpUs
            xdsl2LineStatusActProfile
            xdsl2LineStatusActLimitMask
            xdsl2LineStatusActUs0Mask
            xdsl2LineStatusActSnrModeDs
            xdsl2LineStatusActSnrModeUs
            xdsl2LineStatusElectricalLength
            xdsl2LineStatusTssiDs
            xdsl2LineStatusTssiUs
            xdsl2LineStatusMrefPsdDs
            xdsl2LineStatusMrefPsdUs
            xdsl2LineStatusTrellisDs
            xdsl2LineStatusTrellisUs
            xdsl2LineStatusActualCe
            xdsl2LineBandStatusLnAtten
            xdsl2LineBandStatusSigAtten
            xdsl2LineBandStatusSnrMargin
            xdsl2LineSegmentBitsAlloc
            xdsl2LineSegmentRowStatus
            xdsl2ChStatusActDataRate
            xdsl2ChStatusPrevDataRate
            xdsl2ChStatusActDelay
            xdsl2ChStatusActInp
            xdsl2ChStatusInpReport
            xdsl2ChStatusNFec
            xdsl2ChStatusRFec
            xdsl2ChStatusLSymb
            xdsl2ChStatusIntlvDepth
            xdsl2ChStatusIntlvBlock
            xdsl2ChStatusLPath
            xdsl2ChStatusAtmStatus
            xdsl2ChStatusPtmStatus
            xdsl2SCStatusLinScale
            xdsl2SCStatusLinScGroupSize
            xdsl2SCStatusLogMt
            xdsl2SCStatusLogScGroupSize
            xdsl2SCStatusQlnMt
            xdsl2SCStatusQlnScGroupSize
            xdsl2SCStatusSnrMtime
            xdsl2SCStatusSnrScGroupSize
            xdsl2SCStatusAttainableRate
            xdsl2SCStatusRowStatus
            xdsl2SCStatusBandLnAtten
            xdsl2SCStatusBandSigAtten
            xdsl2SCStatusSegmentLinReal
            xdsl2SCStatusSegmentLinImg
            xdsl2SCStatusSegmentLog
            xdsl2SCStatusSegmentQln
            xdsl2SCStatusSegmentSnr
            xdsl2SCStatusSegmentBitsAlloc
            xdsl2SCStatusSegmentGainAlloc
            xdsl2LInvG994VendorId
            xdsl2LInvSystemVendorId
            xdsl2LInvVersionNumber
            xdsl2LInvSerialNumber
            xdsl2LInvSelfTestResult
            xdsl2LInvTransmissionCapabilities
            xdsl2PMLCurr15MValidIntervals
            xdsl2PMLCurr15MInvalidIntervals
            xdsl2PMLCurr15MTimeElapsed
            xdsl2PMLCurr15MFecs
            xdsl2PMLCurr15MEs
            xdsl2PMLCurr15MSes
            xdsl2PMLCurr15MLoss
            xdsl2PMLCurr15MUas
            xdsl2PMLCurr1DayValidIntervals
            xdsl2PMLCurr1DayInvalidIntervals
            xdsl2PMLCurr1DayTimeElapsed
            xdsl2PMLCurr1DayFecs
            xdsl2PMLCurr1DayEs
            xdsl2PMLCurr1DaySes
            xdsl2PMLCurr1DayLoss
            xdsl2PMLCurr1DayUas
            xdsl2PMLInitCurr15MValidIntervals
            xdsl2PMLInitCurr15MInvalidIntervals
            xdsl2PMLInitCurr15MTimeElapsed
            xdsl2PMLInitCurr15MFullInits
            xdsl2PMLInitCurr15MFailedFullInits
            xdsl2PMLInitCurr15MShortInits
            xdsl2PMLInitCurr15MFailedShortInits
            xdsl2PMLInitCurr1DayValidIntervals
            xdsl2PMLInitCurr1DayInvalidIntervals
            xdsl2PMLInitCurr1DayTimeElapsed
            xdsl2PMLInitCurr1DayFullInits
            xdsl2PMLInitCurr1DayFailedFullInits
            xdsl2PMLInitCurr1DayShortInits
            xdsl2PMLInitCurr1DayFailedShortInits
            xdsl2PMLHist15MMonitoredTime
            xdsl2PMLHist15MFecs
            xdsl2PMLHist15MEs
            xdsl2PMLHist15MSes
            xdsl2PMLHist15MLoss
            xdsl2PMLHist15MUas
            xdsl2PMLHist15MValidInterval
            xdsl2PMLHist1DMonitoredTime
            xdsl2PMLHist1DFecs
            xdsl2PMLHist1DEs
            xdsl2PMLHist1DSes
            xdsl2PMLHist1DLoss
            xdsl2PMLHist1DUas
            xdsl2PMLHist1DValidInterval
            xdsl2PMLInitHist15MMonitoredTime
            xdsl2PMLInitHist15MFullInits
            xdsl2PMLInitHist15MFailedFullInits
            xdsl2PMLInitHist15MShortInits
            xdsl2PMLInitHist15MFailedShortInits
            xdsl2PMLInitHist15MValidInterval
            xdsl2PMLInitHist1DMonitoredTime
            xdsl2PMLInitHist1DFullInits
            xdsl2PMLInitHist1DFailedFullInits
            xdsl2PMLInitHist1DShortInits
            xdsl2PMLInitHist1DFailedShortInits
            xdsl2PMLInitHist1DValidInterval
            xdsl2PMChCurr15MValidIntervals
            xdsl2PMChCurr15MInvalidIntervals
            xdsl2PMChCurr15MTimeElapsed
            xdsl2PMChCurr15MCodingViolations
            xdsl2PMChCurr15MCorrectedBlocks
            xdsl2PMChCurr1DayValidIntervals
            xdsl2PMChCurr1DayInvalidIntervals
            xdsl2PMChCurr1DayTimeElapsed
            xdsl2PMChCurr1DayCodingViolations
            xdsl2PMChCurr1DayCorrectedBlocks
            xdsl2PMChHist15MMonitoredTime
            xdsl2PMChHist15MCodingViolations
            xdsl2PMChHist15MCorrectedBlocks
            xdsl2PMChHist15MValidInterval
            xdsl2PMChHist1DMonitoredTime
            xdsl2PMChHist1DCodingViolations
            xdsl2PMChHist1DCorrectedBlocks
            xdsl2PMChHist1DValidInterval
            xdsl2LConfTempLineProfile
            xdsl2LConfTempChan1ConfProfile
            xdsl2LConfTempChan1RaRatioDs
            xdsl2LConfTempChan1RaRatioUs
            xdsl2LConfTempChan2ConfProfile
            xdsl2LConfTempChan2RaRatioDs
            xdsl2LConfTempChan2RaRatioUs
            xdsl2LConfTempChan3ConfProfile
            xdsl2LConfTempChan3RaRatioDs
            xdsl2LConfTempChan3RaRatioUs
            xdsl2LConfTempChan4ConfProfile
            xdsl2LConfTempChan4RaRatioDs
            xdsl2LConfTempChan4RaRatioUs
            xdsl2LConfTempRowStatus
            xdsl2LConfProfScMaskDs
            xdsl2LConfProfScMaskUs
            xdsl2LConfProfVdsl2CarMask
            xdsl2LConfProfRfiBands
            xdsl2LConfProfRaModeDs
            xdsl2LConfProfRaModeUs
            xdsl2LConfProfRaUsNrmDs
            xdsl2LConfProfRaUsNrmUs
            xdsl2LConfProfRaUsTimeDs
            xdsl2LConfProfRaUsTimeUs
            xdsl2LConfProfRaDsNrmDs
            xdsl2LConfProfRaDsNrmUs
            xdsl2LConfProfRaDsTimeDs
            xdsl2LConfProfRaDsTimeUs
            xdsl2LConfProfTargetSnrmDs
            xdsl2LConfProfTargetSnrmUs
            xdsl2LConfProfMaxSnrmDs
            xdsl2LConfProfMaxSnrmUs
            xdsl2LConfProfMinSnrmDs
            xdsl2LConfProfMinSnrmUs
            xdsl2LConfProfMsgMinUs
            xdsl2LConfProfMsgMinDs
            xdsl2LConfProfCeFlag
            xdsl2LConfProfSnrModeDs
            xdsl2LConfProfSnrModeUs
            xdsl2LConfProfTxRefVnDs
            xdsl2LConfProfTxRefVnUs
            xdsl2LConfProfXtuTransSysEna
            xdsl2LConfProfPmMode
            xdsl2LConfProfL0Time
            xdsl2LConfProfL2Time
            xdsl2LConfProfL2Atpr
            xdsl2LConfProfL2Atprt
            xdsl2LConfProfProfiles
            xdsl2LConfProfDpboEPsd
            xdsl2LConfProfDpboEsEL
            xdsl2LConfProfDpboEsCableModelA
            xdsl2LConfProfDpboEsCableModelB
            xdsl2LConfProfDpboEsCableModelC
            xdsl2LConfProfDpboMus
            xdsl2LConfProfDpboFMin
            xdsl2LConfProfDpboFMax
            xdsl2LConfProfUpboKL
            xdsl2LConfProfUpboKLF
            xdsl2LConfProfUs0Mask
            xdsl2LConfProfForceInp
            xdsl2LConfProfRowStatus
            xdsl2LConfProfMaxNomPsdDs
            xdsl2LConfProfMaxNomPsdUs
            xdsl2LConfProfMaxNomAtpDs
            xdsl2LConfProfMaxNomAtpUs
            xdsl2LConfProfMaxAggRxPwrUs
            xdsl2LConfProfPsdMaskDs
            xdsl2LConfProfPsdMaskUs
            xdsl2LConfProfPsdMaskSelectUs
            xdsl2LConfProfClassMask
            xdsl2LConfProfLimitMask
            xdsl2LConfProfUs0Disable
            xdsl2LConfProfModeSpecRowStatus
            xdsl2LConfProfUpboPsdA
            xdsl2LConfProfUpboPsdB
            xdsl2LConfProfModeSpecBandUsRowStatus
            xdsl2ChConfProfMinDataRateDs
            xdsl2ChConfProfMinDataRateUs
            xdsl2ChConfProfMinResDataRateDs
            xdsl2ChConfProfMinResDataRateUs
            xdsl2ChConfProfMaxDataRateDs
            xdsl2ChConfProfMaxDataRateUs
            xdsl2ChConfProfMinDataRateLowPwrDs
            xdsl2ChConfProfMinDataRateLowPwrUs
            xdsl2ChConfProfMaxDelayDs
            xdsl2ChConfProfMaxDelayUs
            xdsl2ChConfProfMinProtectionDs
            xdsl2ChConfProfMinProtectionUs
            xdsl2ChConfProfMinProtection8Ds
            xdsl2ChConfProfMinProtection8Us
            xdsl2ChConfProfMaxBerDs
            xdsl2ChConfProfMaxBerUs
            xdsl2ChConfProfUsDataRateDs
            xdsl2ChConfProfDsDataRateDs
            xdsl2ChConfProfUsDataRateUs
            xdsl2ChConfProfDsDataRateUs
            xdsl2ChConfProfImaEnabled
            xdsl2ChConfProfMaxDelayVar
            xdsl2ChConfProfInitPolicy
            xdsl2ChConfProfRowStatus
            xdsl2LAlarmConfTempLineProfile
            xdsl2LAlarmConfTempChan1ConfProfile
            xdsl2LAlarmConfTempChan2ConfProfile
            xdsl2LAlarmConfTempChan3ConfProfile
            xdsl2LAlarmConfTempChan4ConfProfile
            xdsl2LAlarmConfTempRowStatus
            xdsl2LineAlarmConfProfileXtucThresh15MinFecs
            xdsl2LineAlarmConfProfileXtucThresh15MinEs
            xdsl2LineAlarmConfProfileXtucThresh15MinSes
            xdsl2LineAlarmConfProfileXtucThresh15MinLoss
            xdsl2LineAlarmConfProfileXtucThresh15MinUas
            xdsl2LineAlarmConfProfileXturThresh15MinFecs
            xdsl2LineAlarmConfProfileXturThresh15MinEs
            xdsl2LineAlarmConfProfileXturThresh15MinSes
            xdsl2LineAlarmConfProfileXturThresh15MinLoss
            xdsl2LineAlarmConfProfileXturThresh15MinUas
            xdsl2LineAlarmConfProfileThresh15MinFailedFullInt
            xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt
            xdsl2LineAlarmConfProfileRowStatus
            xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations
            xdsl2ChAlarmConfProfileXtucThresh15MinCorrected
            xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations
            xdsl2ChAlarmConfProfileXturThresh15MinCorrected
            xdsl2ChAlarmConfProfileRowStatus
            xdsl2ScalarSCMaxInterfaces
            xdsl2ScalarSCAvailInterfaces
            snmp.1
            snmp.2
            snmp.3
            snmp.4
            snmp.5
            snmp.6
            snmp.8
            snmp.9
            snmp.10
            snmp.11
            snmp.12
            snmp.13
            snmp.14
            snmp.15
            snmp.16
            snmp.17
            snmp.18
            snmp.19
            snmp.20
            snmp.21
            snmp.22
            snmp.24
            snmp.25
            snmp.26
            snmp.27
            snmp.28
            snmp.29
            snmp.30
            snmp.31
            snmp.32
            aarpEntry.1
            aarpEntry.2
            aarpEntry.3
            atportEntry.1
            atportEntry.2
            atportEntry.3
            atportEntry.4
            atportEntry.5
            atportEntry.6
            atportEntry.7
            atportEntry.8
            atportEntry.9
            atportEntry.10
            atportEntry.11
            ddp.1
            ddp.2
            ddp.3
            ddp.4
            ddp.5
            ddp.6
            ddp.7
            ddp.8
            ddp.9
            ddp.10
            ddp.11
            ddp.12
            ddp.13
            ddp.14
            rtmpEntry.1
            rtmpEntry.2
            rtmpEntry.3
            rtmpEntry.4
            rtmpEntry.5
            rtmpEntry.6
            rtmpEntry.7
            zipEntry.1
            zipEntry.2
            zipEntry.3
            zipEntry.4
            zipEntry.5
            nbpEntry.1
            nbpEntry.2
            nbpEntry.3
            nbpEntry.4
            nbpEntry.5
            atecho.1
            atecho.2
            ospfGeneralGroup.1
            ospfGeneralGroup.2
            ospfGeneralGroup.3
            ospfGeneralGroup.4
            ospfGeneralGroup.5
            ospfGeneralGroup.6
            ospfGeneralGroup.7
            ospfGeneralGroup.8
            ospfGeneralGroup.9
            ospfGeneralGroup.10
            ospfGeneralGroup.11
            ospfGeneralGroup.12
            ospfGeneralGroup.13
            ospfGeneralGroup.14
            ospfAreaEntry.1
            ospfAreaEntry.2
            ospfAreaEntry.3
            ospfAreaEntry.4
            ospfAreaEntry.5
            ospfAreaEntry.6
            ospfAreaEntry.7
            ospfAreaEntry.8
            ospfAreaEntry.9
            ospfAreaEntry.10
            ospfStubAreaEntry.1
            ospfStubAreaEntry.2
            ospfStubAreaEntry.3
            ospfStubAreaEntry.4
            ospfStubAreaEntry.5
            ospfLsdbEntry.1
            ospfLsdbEntry.2
            ospfLsdbEntry.3
            ospfLsdbEntry.4
            ospfLsdbEntry.5
            ospfLsdbEntry.6
            ospfLsdbEntry.7
            ospfLsdbEntry.8
            ospfAreaRangeEntry.1
            ospfAreaRangeEntry.2
            ospfAreaRangeEntry.3
            ospfAreaRangeEntry.4
            ospfAreaRangeEntry.5
            ospfHostEntry.1
            ospfHostEntry.2
            ospfHostEntry.3
            ospfHostEntry.4
            ospfHostEntry.5
            ospfIfEntry.1
            ospfIfEntry.2
            ospfIfEntry.3
            ospfIfEntry.4
            ospfIfEntry.5
            ospfIfEntry.6
            ospfIfEntry.7
            ospfIfEntry.8
            ospfIfEntry.9
            ospfIfEntry.10
            ospfIfEntry.11
            ospfIfEntry.12
            ospfIfEntry.13
            ospfIfEntry.14
            ospfIfEntry.15
            ospfIfEntry.16
            ospfIfEntry.17
            ospfIfEntry.18
            ospfIfEntry.19
            ospfIfEntry.20
            ospfIfMetricEntry.1
            ospfIfMetricEntry.2
            ospfIfMetricEntry.3
            ospfIfMetricEntry.4
            ospfIfMetricEntry.5
            ospfVirtIfEntry.1
            ospfVirtIfEntry.2
            ospfVirtIfEntry.3
            ospfVirtIfEntry.4
            ospfVirtIfEntry.5
            ospfVirtIfEntry.6
            ospfVirtIfEntry.7
            ospfVirtIfEntry.8
            ospfVirtIfEntry.9
            ospfVirtIfEntry.10
            ospfVirtIfEntry.11
            ospfNbrEntry.1
            ospfNbrEntry.2
            ospfNbrEntry.3
            ospfNbrEntry.4
            ospfNbrEntry.5
            ospfNbrEntry.6
            ospfNbrEntry.7
            ospfNbrEntry.8
            ospfNbrEntry.9
            ospfNbrEntry.10
            ospfNbrEntry.11
            ospfVirtNbrEntry.1
            ospfVirtNbrEntry.2
            ospfVirtNbrEntry.3
            ospfVirtNbrEntry.4
            ospfVirtNbrEntry.5
            ospfVirtNbrEntry.6
            ospfVirtNbrEntry.7
            ospfVirtNbrEntry.8
            ospfExtLsdbEntry.1
            ospfExtLsdbEntry.2
            ospfExtLsdbEntry.3
            ospfExtLsdbEntry.4
            ospfExtLsdbEntry.5
            ospfExtLsdbEntry.6
            ospfExtLsdbEntry.7
            ospfAreaAggregateEntry.1
            ospfAreaAggregateEntry.2
            ospfAreaAggregateEntry.3
            ospfAreaAggregateEntry.4
            ospfAreaAggregateEntry.5
            ospfAreaAggregateEntry.6
            ospfTrap.1.1
            ospfTrap.1.2
            ospfTrap.1.3
            ospfTrap.1.4
            bgpVersion
            bgpLocalAs
            bgpPeerIdentifier
            bgpPeerEntry.2
            bgpPeerAdminStatus
            bgpPeerNegotiatedVersion
            bgpPeerLocalAddr
            bgpPeerLocalPort
            bgpPeerRemoteAddr
            bgpPeerRemotePort
            bgpPeerRemoteAs
            bgpPeerInUpdates
            bgpPeerOutUpdates
            bgpPeerInTotalMessages
            bgpPeerOutTotalMessages
            bgpPeerEntry.14
            bgpPeerFsmEstablishedTransitions
            bgpPeerFsmEstablishedTime
            bgpPeerConnectRetryInterval
            bgpPeerHoldTime
            bgpPeerKeepAlive
            bgpPeerHoldTimeConfigured
            bgpPeerKeepAliveConfigured
            bgpPeerMinASOriginationInterval
            bgpPeerMinRouteAdvertisementInterval
            bgpPeerInUpdateElapsedTime
            bgpIdentifier
            bgp4PathAttrPeer
            bgp4PathAttrIpAddrPrefixLen
            bgp4PathAttrIpAddrPrefix
            bgp4PathAttrOrigin
            bgp4PathAttrASPathSegment
            bgp4PathAttrNextHop
            bgp4PathAttrMultiExitDisc
            bgp4PathAttrLocalPref
            bgp4PathAttrAtomicAggregate
            bgp4PathAttrAggregatorAS
            bgp4PathAttrAggregatorAddr
            bgp4PathAttrCalcLocalPref
            bgp4PathAttrBest
            bgp4PathAttrUnknown
            alarmEntry.1
            alarmEntry.2
            alarmEntry.3
            alarmEntry.4
            alarmEntry.5
            alarmEntry.6
            alarmEntry.7
            alarmEntry.8
            alarmEntry.9
            alarmEntry.10
            alarmEntry.11
            alarmEntry.12
            eventEntry.1
            eventEntry.2
            eventEntry.3
            eventEntry.4
            eventEntry.5
            eventEntry.6
            eventEntry.7
            logEntry.1
            logEntry.2
            logEntry.3
            logEntry.4
            rmon.10.106.1.2
            rmon.10.106.1.3
            rmon.10.106.1.4
            rmon.10.106.1.5
            rmon.10.106.1.6
            rmon.10.106.1.7
            rmon.10.145.1.2
            rmon.10.145.1.3
            rmon.10.186.1.2
            rmon.10.186.1.3
            rmon.10.186.1.4
            rmon.10.186.1.5
            rmon.10.229.1.1
            rmon.10.229.1.2
            rmon.19.1
            rmon.19.2
            rmon.19.3
            rmon.19.4
            rmon.19.5
            rmon.19.6
            rmon.19.7
            rmon.19.8
            rmon.19.9
            rmon.10.76.1.1
            rmon.10.76.1.2
            rmon.10.76.1.3
            rmon.10.76.1.4
            rmon.10.76.1.5
            rmon.10.76.1.6
            rmon.10.76.1.7
            rmon.10.76.1.8
            rmon.10.76.1.9
            rmon.10.135.1.1
            rmon.10.135.1.2
            rmon.10.135.1.3
            rmon.19.12
            rmon.10.4.1.2
            rmon.10.4.1.3
            rmon.10.4.1.4
            rmon.10.4.1.5
            rmon.10.4.1.6
            rmon.10.69.1.2
            rmon.10.69.1.3
            rmon.10.69.1.4
            rmon.10.69.1.5
            rmon.10.69.1.6
            rmon.10.69.1.7
            rmon.10.69.1.8
            rmon.10.69.1.9
            rmon.19.15
            rmon.19.16
            hcAlarmInterval
            hcAlarmVariable
            hcAlarmSampleType
            hcAlarmAbsValue
            hcAlarmValueStatus
            hcAlarmStartupAlarm
            hcAlarmRisingThreshAbsValueLo
            hcAlarmRisingThreshAbsValueHi
            hcAlarmRisingThresholdValStatus
            hcAlarmFallingThreshAbsValueLo
            hcAlarmFallingThreshAbsValueHi
            hcAlarmFallingThresholdValStatus
            hcAlarmRisingEventIndex
            hcAlarmFallingEventIndex
            hcAlarmValueFailedAttempts
            hcAlarmOwner
            hcAlarmStorageType
            hcAlarmStatus
            hcAlarmCapabilities
            dot1dBase.1
            dot1dBase.2
            dot1dBase.3
            dot1dBasePortEntry.1
            dot1dBasePortEntry.2
            dot1dBasePortEntry.3
            dot1dBasePortEntry.4
            dot1dBasePortEntry.5
            dot1dStp.1
            dot1dStp.2
            dot1dStp.3
            dot1dStp.4
            dot1dStp.5
            dot1dStp.6
            dot1dStp.7
            dot1dStp.8
            dot1dStp.9
            dot1dStp.10
            dot1dStp.11
            dot1dStp.12
            dot1dStp.13
            dot1dStp.14
            dot1dStpPortEntry.1
            dot1dStpPortEntry.2
            dot1dStpPortEntry.3
            dot1dStpPortEntry.4
            dot1dStpPortEntry.5
            dot1dStpPortEntry.6
            dot1dStpPortEntry.7
            dot1dStpPortEntry.8
            dot1dStpPortEntry.9
            dot1dStpPortEntry.10
            dot1dSrPortEntry.1
            dot1dSrPortEntry.2
            dot1dSrPortEntry.3
            dot1dSrPortEntry.4
            dot1dSrPortEntry.5
            dot1dSrPortEntry.6
            dot1dSrPortEntry.7
            dot1dSrPortEntry.8
            dot1dSrPortEntry.9
            dot1dSrPortEntry.10
            dot1dSrPortEntry.11
            dot1dSrPortEntry.12
            dot1dSrPortEntry.13
            dot1dSrPortEntry.14
            dot1dSrPortEntry.15
            dot1dSrPortEntry.16
            dot1dSrPortEntry.17
            dot1dSrPortEntry.18
            dot1dTp.1
            dot1dTp.2
            dot1dTpFdbEntry.1
            dot1dTpFdbEntry.2
            dot1dTpFdbEntry.3
            dot1dTpPortEntry.1
            dot1dTpPortEntry.2
            dot1dTpPortEntry.3
            dot1dTpPortEntry.4
            dot1dTpPortEntry.5
            dot1dStaticEntry.1
            dot1dStaticEntry.2
            dot1dStaticEntry.3
            dot1dStaticEntry.4
            ifName
            ifInMulticastPkts
            ifInBroadcastPkts
            ifOutMulticastPkts
            ifOutBroadcastPkts
            ifHCInOctets
            ifHCInUcastPkts
            ifHCInMulticastPkts
            ifHCInBroadcastPkts
            ifHCOutOctets
            ifHCOutUcastPkts
            ifHCOutMulticastPkts
            ifHCOutBroadcastPkts
            ifLinkUpDownTrapEnable
            ifHighSpeed
            ifPromiscuousMode
            ifConnectorPresent
            ifAlias
            ifCounterDiscontinuityTime
            ifStackStatus
            ifTestId
            ifTestStatus
            ifTestType
            ifTestResult
            ifTestCode
            ifTestOwner
            ifRcvAddressStatus
            ifRcvAddressType
            ifTableLastChange
            ifStackLastChange
            atmInterfaceConfEntry.1
            atmInterfaceConfEntry.2
            atmInterfaceConfEntry.3
            atmInterfaceConfEntry.4
            atmInterfaceConfEntry.5
            atmInterfaceConfEntry.6
            atmInterfaceConfEntry.7
            atmInterfaceConfEntry.8
            atmInterfaceConfEntry.9
            atmInterfaceConfEntry.10
            atmInterfaceConfEntry.11
            atmInterfaceConfEntry.12
            atmTrafficDescrParamEntry.2
            atmTrafficDescrParamEntry.3
            atmTrafficDescrParamEntry.4
            atmTrafficDescrParamEntry.5
            atmTrafficDescrParamEntry.6
            atmTrafficDescrParamEntry.7
            atmTrafficDescrParamEntry.8
            atmTrafficDescrParamEntry.9
            atmVplEntry.2
            atmVplEntry.3
            atmVplEntry.4
            atmVplEntry.5
            atmVplEntry.6
            atmVplEntry.7
            atmVplEntry.8
            atmVclEntry.3
            atmVclEntry.4
            atmVclEntry.5
            atmVclEntry.6
            atmVclEntry.7
            atmVclEntry.8
            atmVclEntry.9
            atmVclEntry.10
            atmVclEntry.11
            atmVclEntry.12
            atmVclEntry.13
            aal5VccEntry.3
            aal5VccEntry.4
            aal5VccEntry.5
            sdlcPortAdminEntry.1
            sdlcPortAdminEntry.2
            sdlcPortAdminEntry.3
            sdlcPortAdminEntry.4
            sdlcPortAdminEntry.5
            sdlcPortAdminEntry.6
            sdlcPortAdminEntry.7
            sdlcPortAdminEntry.8
            sdlcPortAdminEntry.9
            sdlcPortOperEntry.1
            sdlcPortOperEntry.2
            sdlcPortOperEntry.3
            sdlcPortOperEntry.4
            sdlcPortOperEntry.5
            sdlcPortOperEntry.6
            sdlcPortOperEntry.7
            sdlcPortOperEntry.8
            sdlcPortOperEntry.9
            sdlcPortOperEntry.10
            sdlcPortOperEntry.11
            sdlcPortOperEntry.12
            sdlcPortOperEntry.13
            sdlcPortStatsEntry.1
            sdlcPortStatsEntry.2
            sdlcPortStatsEntry.3
            sdlcPortStatsEntry.4
            sdlcPortStatsEntry.5
            sdlcPortStatsEntry.6
            sdlcPortStatsEntry.7
            sdlcPortStatsEntry.8
            sdlcPortStatsEntry.9
            sdlcPortStatsEntry.10
            sdlcPortStatsEntry.11
            sdlcPortStatsEntry.12
            sdlcPortStatsEntry.13
            sdlcPortStatsEntry.14
            sdlcPortStatsEntry.15
            sdlcPortStatsEntry.16
            sdlcPortStatsEntry.17
            sdlcPortStatsEntry.18
            sdlcPortStatsEntry.19
            sdlcLSAdminEntry.1
            sdlcLSAdminEntry.2
            sdlcLSAdminEntry.3
            sdlcLSAdminEntry.4
            sdlcLSAdminEntry.5
            sdlcLSAdminEntry.6
            sdlcLSAdminEntry.7
            sdlcLSAdminEntry.8
            sdlcLSAdminEntry.9
            sdlcLSAdminEntry.10
            sdlcLSAdminEntry.11
            sdlcLSAdminEntry.12
            sdlcLSAdminEntry.13
            sdlcLSAdminEntry.14
            sdlcLSAdminEntry.15
            sdlcLSAdminEntry.16
            sdlcLSAdminEntry.17
            sdlcLSAdminEntry.18
            sdlcLSAdminEntry.19
            sdlcLSOperEntry.1
            sdlcLSOperEntry.2
            sdlcLSOperEntry.3
            sdlcLSOperEntry.4
            sdlcLSOperEntry.5
            sdlcLSOperEntry.6
            sdlcLSOperEntry.7
            sdlcLSOperEntry.8
            sdlcLSOperEntry.9
            sdlcLSOperEntry.10
            sdlcLSOperEntry.11
            sdlcLSOperEntry.12
            sdlcLSOperEntry.13
            sdlcLSOperEntry.14
            sdlcLSOperEntry.15
            sdlcLSOperEntry.16
            sdlcLSOperEntry.17
            sdlcLSOperEntry.18
            sdlcLSOperEntry.19
            sdlcLSOperEntry.20
            sdlcLSOperEntry.21
            sdlcLSOperEntry.22
            sdlcLSOperEntry.23
            sdlcLSOperEntry.24
            sdlcLSStatsEntry.1
            sdlcLSStatsEntry.2
            sdlcLSStatsEntry.3
            sdlcLSStatsEntry.4
            sdlcLSStatsEntry.5
            sdlcLSStatsEntry.6
            sdlcLSStatsEntry.7
            sdlcLSStatsEntry.8
            sdlcLSStatsEntry.9
            sdlcLSStatsEntry.10
            sdlcLSStatsEntry.11
            sdlcLSStatsEntry.12
            sdlcLSStatsEntry.13
            sdlcLSStatsEntry.14
            sdlcLSStatsEntry.15
            sdlcLSStatsEntry.16
            sdlcLSStatsEntry.17
            sdlcLSStatsEntry.18
            sdlcLSStatsEntry.19
            sdlcLSStatsEntry.20
            sdlcLSStatsEntry.21
            sdlcLSStatsEntry.22
            sdlcLSStatsEntry.23
            sdlcLSStatsEntry.24
            sdlcLSStatsEntry.25
            sdlcLSStatsEntry.26
            sdlcLSStatsEntry.27
            sdlcLSStatsEntry.28
            sdlcLSStatsEntry.29
            sdlcLSStatsEntry.30
            sdlcLSStatsEntry.31
            sdlcLSStatsEntry.32
            sdlcLSStatsEntry.33
            sdlcLSStatsEntry.34
            sdlcLSStatsEntry.35
            sdlcLSStatsEntry.36
            sdlcLSStatsEntry.37
            sdlcLSStatsEntry.38
            sdlcLSStatsEntry.39
            sdlcLSStatsEntry.40
            mipEntities
            mipEnable
            mipEncapsulationSupported
            mipSecAlgorithmType
            mipSecAlgorithmMode
            mipSecKey
            mipSecReplayMethod
            mipSecTotalViolations
            mipSecViolatorAddress
            mipSecViolationCounter
            mipSecRecentViolationSPI
            mipSecRecentViolationTime
            mipSecRecentViolationIDLow
            mipSecRecentViolationIDHigh
            mipSecRecentViolationReason
            mnState
            mnHomeAddress
            mnCurrentHA
            mnHAStatus
            mnFAAddress
            mnCOA
            mnAdvSourceAddress
            mnAdvSequence
            mnAdvFlags
            mnAdvMaxRegLifetime
            mnAdvMaxAdvLifetime
            mnAdvTimeReceived
            mnSolicitationsSent
            mnAdvertisementsReceived
            mnAdvsDroppedInvalidExtension
            mnAdvsIgnoredUnknownExtension
            mnMoveFromHAToFA
            mnMoveFromFAToFA
            mnMoveFromFAToHA
            mnGratuitousARPsSend
            mnAgentRebootsDectected
            mnRegAgentAddress
            mnRegCOA
            mnRegFlags
            mnRegIDLow
            mnRegIDHigh
            mnRegTimeRequested
            mnRegTimeRemaining
            mnRegTimeSent
            mnRegIsAccepted
            mnCOAIsLocal
            mnRegRequestsSent
            mnDeRegRequestsSent
            mnRegRepliesRecieved
            mnDeRegRepliesRecieved
            mnRepliesInvalidHomeAddress
            mnRepliesUnknownHA
            mnRepliesUnknownFA
            mnRepliesInvalidID
            mnRepliesDroppedInvalidExtension
            mnRepliesIgnoredUnknownExtension
            mnRepliesHAAuthenticationFailure
            mnRepliesFAAuthenticationFailure
            mnRegRequestsAccepted
            mnRegRequestsDeniedByHA
            mnRegRequestsDeniedByFA
            mnRegRequestsDeniedByHADueToID
            maAdvMaxRegLifetime
            maAdvPrefixLengthInclusion
            maAdvAddress
            maAdvMaxInterval
            maAdvMinInterval
            maAdvMaxAdvLifetime
            maAdvResponseSolicitationOnly
            maAdvStatus
            maAdvertisementsSent
            maAdvsSentForSolicitation
            maSolicitationsReceived
            faCOAStatus
            faVisitorIPAddress
            faVisitorHomeAddress
            faVisitorHomeAgentAddress
            faVisitorTimeGranted
            faVisitorTimeRemaining
            faVisitorRegFlags
            faVisitorRegIDLow
            faVisitorRegIDHigh
            faVisitorRegIsAccepted
            faRegRequestsReceived
            faRegRequestsRelayed
            faReasonUnspecified
            faAdmProhibited
            faInsufficientResource
            faMNAuthenticationFailure
            faRegLifetimeTooLong
            faPoorlyFormedRequests
            faEncapsulationUnavailable
            faHAUnreachable
            faRegRepliesRecieved
            faRegRepliesRelayed
            faHAAuthenticationFailure
            faPoorlyFormedReplies
            haMobilityBindingMN
            haMobilityBindingCOA
            haMobilityBindingSourceAddress
            haMobilityBindingRegFlags
            haMobilityBindingRegIDLow
            haMobilityBindingRegIDHigh
            haMobilityBindingTimeGranted
            haMobilityBindingTimeRemaining
            haServiceRequestsAccepted
            haServiceRequestsDenied
            haOverallServiceTime
            haRecentServiceAcceptedTime
            haRecentServiceDeniedTime
            haRecentServiceDeniedCode
            haRegistrationAccepted
            haMultiBindingUnsupported
            haReasonUnspecified
            haAdmProhibited
            haInsufficientResource
            haMNAuthenticationFailure
            haFAAuthenticationFailure
            haIDMismatch
            haPoorlyFormedRequest
            haTooManyBindings
            haUnknownHA
            haGratuitiousARPsSent
            haProxyARPsSent
            haRegRequestsReceived
            haDeRegRequestsReceived
            haRegRepliesSent
            haDeRegRepliesSent
            dlswNode.1
            dlswNode.2
            dlswNode.3
            dlswNode.4
            dlswNode.5
            dlswNode.6
            dlswNode.7
            dlswNode.8
            dlswNode.9
            dlswTrapControl.1
            dlswTrapControl.2
            dlswTrapControl.3
            dlswTrapControl.4
            dlswTConnStat.1
            dlswTConnStat.2
            dlswTConnStat.3
            dlswTConnConfigEntry.2
            dlswTConnConfigEntry.3
            dlswTConnConfigEntry.4
            dlswTConnConfigEntry.5
            dlswTConnConfigEntry.6
            dlswTConnConfigEntry.7
            dlswTConnConfigEntry.8
            dlswTConnConfigEntry.9
            dlswTConnConfigEntry.10
            dlswTConnConfigEntry.11
            dlswTConnConfigEntry.12
            dlswTConnConfigEntry.13
            dlswTConnOperEntry.2
            dlswTConnOperEntry.4
            dlswTConnOperEntry.5
            dlswTConnOperEntry.6
            dlswTConnOperEntry.7
            dlswTConnOperEntry.8
            dlswTConnOperEntry.9
            dlswTConnOperEntry.10
            dlswTConnOperEntry.11
            dlswTConnOperEntry.12
            dlswTConnOperEntry.13
            dlswTConnOperEntry.14
            dlswTConnOperEntry.15
            dlswTConnOperEntry.16
            dlswTConnOperEntry.17
            dlswTConnOperEntry.18
            dlswTConnOperEntry.19
            dlswTConnOperEntry.20
            dlswTConnOperEntry.21
            dlswTConnOperEntry.22
            dlswTConnOperEntry.23
            dlswTConnOperEntry.24
            dlswTConnOperEntry.25
            dlswTConnOperEntry.26
            dlswTConnOperEntry.27
            dlswTConnOperEntry.28
            dlswTConnOperEntry.29
            dlswTConnOperEntry.30
            dlswTConnOperEntry.31
            dlswTConnOperEntry.32
            dlswTConnOperEntry.33
            dlswTConnOperEntry.34
            dlswTConnOperEntry.35
            dlswTConnOperEntry.36
            dlswTConnTcpConfigEntry.1
            dlswTConnTcpConfigEntry.2
            dlswTConnTcpConfigEntry.3
            dlswTConnTcpOperEntry.1
            dlswTConnTcpOperEntry.2
            dlswTConnTcpOperEntry.3
            dlswIfEntry.1
            dlswIfEntry.2
            dlswIfEntry.3
            dlswDirStat.1
            dlswDirStat.2
            dlswDirStat.3
            dlswDirStat.4
            dlswDirStat.5
            dlswDirStat.6
            dlswDirStat.7
            dlswDirStat.8
            dlswDirMacEntry.2
            dlswDirMacEntry.3
            dlswDirMacEntry.4
            dlswDirMacEntry.5
            dlswDirMacEntry.6
            dlswDirMacEntry.7
            dlswDirMacEntry.8
            dlswDirMacEntry.9
            dlswDirNBEntry.2
            dlswDirNBEntry.3
            dlswDirNBEntry.4
            dlswDirNBEntry.5
            dlswDirNBEntry.6
            dlswDirNBEntry.7
            dlswDirNBEntry.8
            dlswDirNBEntry.9
            dlswDirLocateMacEntry.3
            dlswDirLocateNBEntry.3
            dlswCircuitStat.1
            dlswCircuitStat.2
            dlswCircuitEntry.3
            dlswCircuitEntry.4
            dlswCircuitEntry.5
            dlswCircuitEntry.6
            dlswCircuitEntry.7
            dlswCircuitEntry.10
            dlswCircuitEntry.11
            dlswCircuitEntry.12
            dlswCircuitEntry.13
            dlswCircuitEntry.14
            dlswCircuitEntry.15
            dlswCircuitEntry.16
            dlswCircuitEntry.17
            dlswCircuitEntry.18
            dlswCircuitEntry.19
            dlswCircuitEntry.20
            dlswCircuitEntry.21
            dlswCircuitEntry.22
            dlswCircuitEntry.23
            dlswCircuitEntry.24
            dlswCircuitEntry.25
            dlswCircuitEntry.26
            dlswCircuitEntry.27
            dlswCircuitEntry.28
            dlswCircuitEntry.29
            dlswCircuitEntry.30
            dlswCircuitEntry.31
            dlswSdlc.1
            dlswSdlcLsEntry.1
            dlswSdlcLsEntry.2
            dlswSdlcLsEntry.3
            dlswSdlcLsEntry.4
            dlswSdlcLsEntry.5
            dlswSdlcLsEntry.6
            dlswSdlcLsEntry.7
            entPhysicalEntry.2
            entPhysicalEntry.3
            entPhysicalEntry.4
            entPhysicalEntry.5
            entPhysicalEntry.6
            entPhysicalEntry.7
            entPhysicalEntry.8
            entPhysicalEntry.9
            entPhysicalEntry.10
            entPhysicalEntry.11
            entPhysicalEntry.12
            entPhysicalEntry.13
            entPhysicalEntry.14
            entPhysicalEntry.15
            entPhysicalEntry.16
            entPhysicalEntry.17
            entPhysicalEntry.18
            entLogicalEntry.2
            entLogicalEntry.3
            entLogicalEntry.4
            entLogicalEntry.5
            entLogicalEntry.6
            entLogicalEntry.7
            entLogicalEntry.8
            entLPMappingEntry.1
            entAliasMappingEntry.2
            entPhysicalContainsEntry.1
            entityGeneral.1
            rsvpSessionEntry.2
            rsvpSessionEntry.3
            rsvpSessionEntry.4
            rsvpSessionEntry.5
            rsvpSessionEntry.6
            rsvpSessionEntry.7
            rsvpSessionEntry.8
            rsvpSessionEntry.9
            rsvpSenderEntry.2
            rsvpSenderEntry.3
            rsvpSenderEntry.4
            rsvpSenderEntry.5
            rsvpSenderEntry.6
            rsvpSenderEntry.7
            rsvpSenderEntry.8
            rsvpSenderEntry.9
            rsvpSenderEntry.10
            rsvpSenderEntry.11
            rsvpSenderEntry.12
            rsvpSenderEntry.13
            rsvpSenderEntry.14
            rsvpSenderEntry.15
            rsvpSenderEntry.16
            rsvpSenderEntry.17
            rsvpSenderEntry.18
            rsvpSenderEntry.19
            rsvpSenderEntry.20
            rsvpSenderEntry.21
            rsvpSenderEntry.22
            rsvpSenderEntry.23
            rsvpSenderEntry.24
            rsvpSenderEntry.25
            rsvpSenderEntry.26
            rsvpSenderEntry.27
            rsvpSenderEntry.28
            rsvpSenderEntry.29
            rsvpSenderEntry.30
            rsvpSenderEntry.31
            rsvpSenderEntry.32
            rsvpSenderEntry.33
            rsvpSenderEntry.34
            rsvpSenderEntry.35
            rsvpSenderEntry.36
            rsvpSenderEntry.37
            rsvpSenderEntry.38
            rsvpSenderEntry.39
            rsvpSenderEntry.40
            rsvpSenderEntry.41
            rsvpSenderEntry.42
            rsvpSenderEntry.43
            rsvpSenderEntry.44
            rsvpSenderEntry.45
            rsvpSenderOutInterfaceStatus
            rsvpResvEntry.2
            rsvpResvEntry.3
            rsvpResvEntry.4
            rsvpResvEntry.5
            rsvpResvEntry.6
            rsvpResvEntry.7
            rsvpResvEntry.8
            rsvpResvEntry.9
            rsvpResvEntry.10
            rsvpResvEntry.11
            rsvpResvEntry.12
            rsvpResvEntry.13
            rsvpResvEntry.14
            rsvpResvEntry.15
            rsvpResvEntry.16
            rsvpResvEntry.17
            rsvpResvEntry.18
            rsvpResvEntry.19
            rsvpResvEntry.20
            rsvpResvEntry.21
            rsvpResvEntry.22
            rsvpResvEntry.23
            rsvpResvEntry.24
            rsvpResvEntry.25
            rsvpResvEntry.26
            rsvpResvEntry.27
            rsvpResvEntry.28
            rsvpResvEntry.29
            rsvpResvEntry.30
            rsvpResvFwdEntry.2
            rsvpResvFwdEntry.3
            rsvpResvFwdEntry.4
            rsvpResvFwdEntry.5
            rsvpResvFwdEntry.6
            rsvpResvFwdEntry.7
            rsvpResvFwdEntry.8
            rsvpResvFwdEntry.9
            rsvpResvFwdEntry.10
            rsvpResvFwdEntry.11
            rsvpResvFwdEntry.12
            rsvpResvFwdEntry.13
            rsvpResvFwdEntry.14
            rsvpResvFwdEntry.15
            rsvpResvFwdEntry.16
            rsvpResvFwdEntry.17
            rsvpResvFwdEntry.18
            rsvpResvFwdEntry.19
            rsvpResvFwdEntry.20
            rsvpResvFwdEntry.21
            rsvpResvFwdEntry.22
            rsvpResvFwdEntry.23
            rsvpResvFwdEntry.24
            rsvpResvFwdEntry.25
            rsvpResvFwdEntry.26
            rsvpResvFwdEntry.27
            rsvpResvFwdEntry.28
            rsvpResvFwdEntry.29
            rsvpResvFwdEntry.30
            rsvpIfEntry.1
            rsvpIfEntry.2
            rsvpIfEntry.3
            rsvpIfEntry.4
            rsvpIfEntry.5
            rsvpIfEntry.6
            rsvpIfEntry.7
            rsvpIfEntry.8
            rsvpIfEntry.9
            rsvpIfEntry.10
            rsvpIfEntry.11
            rsvpNbrEntry.2
            rsvpNbrEntry.3
            rsvp.2.1
            rsvp.2.2
            rsvp.2.3
            rsvp.2.4
            rsvp.2.5
            intSrvIfAttribEntry.1
            intSrvIfAttribEntry.2
            intSrvIfAttribEntry.3
            intSrvIfAttribEntry.4
            intSrvIfAttribEntry.5
            intSrvIfAttribEntry.6
            intSrvFlowEntry.2
            intSrvFlowEntry.3
            intSrvFlowEntry.4
            intSrvFlowEntry.5
            intSrvFlowEntry.6
            intSrvFlowEntry.7
            intSrvFlowEntry.8
            intSrvFlowEntry.9
            intSrvFlowEntry.10
            intSrvFlowEntry.11
            intSrvFlowEntry.12
            intSrvFlowEntry.13
            intSrvFlowEntry.14
            intSrvFlowEntry.15
            intSrvFlowEntry.16
            intSrvFlowEntry.17
            intSrvFlowEntry.18
            intSrvFlowEntry.19
            intSrvFlowEntry.20
            intSrvFlowEntry.21
            intSrvFlowEntry.22
            intSrvFlowEntry.23
            intSrvFlowEntry.24
            intSrvFlowEntry.25
            intSrvGenObjects.1
            intSrvGuaranteedIfEntry.1
            intSrvGuaranteedIfEntry.2
            intSrvGuaranteedIfEntry.3
            intSrvGuaranteedIfEntry.4
            vrrpNodeVersion
            vrrpNotificationCntl
            vrrpOperVirtualMacAddr
            vrrpOperState
            vrrpOperAdminState
            vrrpOperPriority
            vrrpOperIpAddrCount
            vrrpOperMasterIpAddr
            vrrpOperPrimaryIpAddr
            vrrpOperAuthType
            vrrpOperAuthKey
            vrrpOperAdvertisementInterval
            vrrpOperPreemptMode
            vrrpOperVirtualRouterUpTime
            vrrpOperProtocol
            vrrpOperRowStatus
            vrrpAssoIpAddrRowStatus
            vrrpTrapPacketSrc
            vrrpTrapAuthErrorType
            vrrpRouterChecksumErrors
            vrrpRouterVersionErrors
            vrrpRouterVrIdErrors
            vrrpStatsBecomeMaster
            vrrpStatsAdvertiseRcvd
            vrrpStatsAdvertiseIntervalErrors
            vrrpStatsAuthFailures
            vrrpStatsIpTtlErrors
            vrrpStatsPriorityZeroPktsRcvd
            vrrpStatsPriorityZeroPktsSent
            vrrpStatsInvalidTypePktsRcvd
            vrrpStatsAddressListErrors
            vrrpStatsInvalidAuthType
            vrrpStatsAuthTypeMismatch
            vrrpStatsPacketLengthErrors
            nhrpNextIndex
            nhrpCachePrefixLength
            nhrpCacheNextHopInternetworkAddr
            nhrpCacheNbmaAddrType
            nhrpCacheNbmaAddr
            nhrpCacheNbmaSubaddr
            nhrpCacheType
            nhrpCacheState
            nhrpCacheHoldingTimeValid
            nhrpCacheHoldingTime
            nhrpCacheNegotiatedMtu
            nhrpCachePreference
            nhrpCacheStorageType
            nhrpCacheRowStatus
            nhrpPurgeCacheIdentifier
            nhrpPurgePrefixLength
            nhrpPurgeRequestID
            nhrpPurgeReplyExpected
            nhrpPurgeRowStatus
            nhrpClientInternetworkAddrType
            nhrpClientInternetworkAddr
            nhrpClientNbmaAddrType
            nhrpClientNbmaAddr
            nhrpClientNbmaSubaddr
            nhrpClientInitialRequestTimeout
            nhrpClientRegistrationRequestRetries
            nhrpClientResolutionRequestRetries
            nhrpClientPurgeRequestRetries
            nhrpClientDefaultMtu
            nhrpClientHoldTime
            nhrpClientRequestID
            nhrpClientStorageType
            nhrpClientRowStatus
            nhrpClientRegUniqueness
            nhrpClientRegState
            nhrpClientRegRowStatus
            nhrpClientNhsInternetworkAddrType
            nhrpClientNhsInternetworkAddr
            nhrpClientNhsNbmaAddrType
            nhrpClientNhsNbmaAddr
            nhrpClientNhsNbmaSubaddr
            nhrpClientNhsInUse
            nhrpClientNhsRowStatus
            nhrpClientStatTxResolveReq
            nhrpClientStatRxResolveReplyAck
            nhrpClientStatRxResolveReplyNakProhibited
            nhrpClientStatRxResolveReplyNakInsufResources
            nhrpClientStatRxResolveReplyNakNoBinding
            nhrpClientStatRxResolveReplyNakNotUnique
            nhrpClientStatTxRegisterReq
            nhrpClientStatRxRegisterAck
            nhrpClientStatRxRegisterNakProhibited
            nhrpClientStatRxRegisterNakInsufResources
            nhrpClientStatRxRegisterNakAlreadyReg
            nhrpClientStatRxPurgeReq
            nhrpClientStatTxPurgeReq
            nhrpClientStatRxPurgeReply
            nhrpClientStatTxPurgeReply
            nhrpClientStatTxErrorIndication
            nhrpClientStatRxErrUnrecognizedExtension
            nhrpClientStatRxErrLoopDetected
            nhrpClientStatRxErrProtoAddrUnreachable
            nhrpClientStatRxErrProtoError
            nhrpClientStatRxErrSduSizeExceeded
            nhrpClientStatRxErrInvalidExtension
            nhrpClientStatRxErrAuthenticationFailure
            nhrpClientStatRxErrHopCountExceeded
            nhrpClientStatDiscontinuityTime
            nhrpServerInternetworkAddrType
            nhrpServerInternetworkAddr
            nhrpServerNbmaAddrType
            nhrpServerNbmaAddr
            nhrpServerNbmaSubaddr
            nhrpServerStorageType
            nhrpServerRowStatus
            nhrpServerCacheAuthoritative
            nhrpServerCacheUniqueness
            nhrpServerNhcPrefixLength
            nhrpServerNhcInternetworkAddrType
            nhrpServerNhcInternetworkAddr
            nhrpServerNhcNbmaAddrType
            nhrpServerNhcNbmaAddr
            nhrpServerNhcNbmaSubaddr
            nhrpServerNhcInUse
            nhrpServerNhcRowStatus
            nhrpServerStatRxResolveReq
            nhrpServerStatTxResolveReplyAck
            nhrpServerStatTxResolveReplyNakProhibited
            nhrpServerStatTxResolveReplyNakInsufResources
            nhrpServerStatTxResolveReplyNakNoBinding
            nhrpServerStatTxResolveReplyNakNotUnique
            nhrpServerStatRxRegisterReq
            nhrpServerStatTxRegisterAck
            nhrpServerStatTxRegisterNakProhibited
            nhrpServerStatTxRegisterNakInsufResources
            nhrpServerStatTxRegisterNakAlreadyReg
            nhrpServerStatRxPurgeReq
            nhrpServerStatTxPurgeReq
            nhrpServerStatRxPurgeReply
            nhrpServerStatTxPurgeReply
            nhrpServerStatRxErrUnrecognizedExtension
            nhrpServerStatRxErrLoopDetected
            nhrpServerStatRxErrProtoAddrUnreachable
            nhrpServerStatRxErrProtoError
            nhrpServerStatRxErrSduSizeExceeded
            nhrpServerStatRxErrInvalidExtension
            nhrpServerStatRxErrInvalidResReplyReceived
            nhrpServerStatRxErrAuthenticationFailure
            nhrpServerStatRxErrHopCountExceeded
            nhrpServerStatTxErrUnrecognizedExtension
            nhrpServerStatTxErrLoopDetected
            nhrpServerStatTxErrProtoAddrUnreachable
            nhrpServerStatTxErrProtoError
            nhrpServerStatTxErrSduSizeExceeded
            nhrpServerStatTxErrInvalidExtension
            nhrpServerStatTxErrAuthenticationFailure
            nhrpServerStatTxErrHopCountExceeded
            nhrpServerStatFwResolveReq
            nhrpServerStatFwResolveReply
            nhrpServerStatFwRegisterReq
            nhrpServerStatFwRegisterReply
            nhrpServerStatFwPurgeReq
            nhrpServerStatFwPurgeReply
            nhrpServerStatFwErrorIndication
            nhrpServerStatDiscontinuityTime
            ipMRoute.1
            ipMRouteEntry.4
            ipMRouteEntry.5
            ipMRouteEntry.6
            ipMRouteEntry.7
            ipMRouteEntry.8
            ipMRouteEntry.9
            ipMRouteEntry.10
            ipMRouteEntry.11
            ipMRouteEntry.12
            ipMRouteEntry.13
            ipMRouteEntry.14
            ipMRouteEntry.15
            ipMRouteEntry.16
            ipMRouteNextHopEntry.6
            ipMRouteNextHopEntry.7
            ipMRouteNextHopEntry.8
            ipMRouteNextHopEntry.9
            ipMRouteNextHopEntry.10
            ipMRouteNextHopEntry.11
            ipMRouteInterfaceEntry.2
            ipMRouteInterfaceEntry.3
            ipMRouteInterfaceEntry.4
            ipMRouteInterfaceEntry.5
            ipMRouteInterfaceEntry.6
            ipMRouteInterfaceEntry.7
            ipMRouteInterfaceEntry.8
            ipMRouteBoundaryEntry.4
            ipMRouteScopeNameEntry.4
            ipMRouteScopeNameEntry.5
            ipMRouteScopeNameEntry.6
            ipMRoute.7
            igmpInterfaceEntry.2
            igmpInterfaceEntry.3
            igmpInterfaceEntry.4
            igmpInterfaceEntry.5
            igmpInterfaceEntry.6
            igmpInterfaceEntry.7
            igmpInterfaceEntry.8
            igmpInterfaceEntry.9
            igmpInterfaceEntry.10
            igmpInterfaceEntry.11
            igmpInterfaceEntry.12
            igmpInterfaceEntry.13
            igmpInterfaceEntry.14
            igmpInterfaceEntry.15
            igmpCacheEntry.3
            igmpCacheEntry.4
            igmpCacheEntry.5
            igmpCacheEntry.6
            igmpCacheEntry.7
            igmpCacheEntry.8
            mteResourceSampleMinimum
            mteResourceSampleInstanceMaximum
            mteResourceSampleInstances
            mteResourceSampleInstancesHigh
            mteResourceSampleInstanceLacks
            mteTriggerFailures
            mteTriggerComment
            mteTriggerTest
            mteTriggerSampleType
            mteTriggerValueID
            mteTriggerValueIDWildcard
            mteTriggerTargetTag
            mteTriggerContextName
            mteTriggerContextNameWildcard
            mteTriggerFrequency
            mteTriggerObjectsOwner
            mteTriggerObjects
            mteTriggerEnabled
            mteTriggerEntryStatus
            mteTriggerDeltaDiscontinuityID
            mteTriggerDeltaDiscontinuityIDWildcard
            mteTriggerDeltaDiscontinuityIDType
            mteTriggerExistenceTest
            mteTriggerExistenceStartup
            mteTriggerExistenceObjectsOwner
            mteTriggerExistenceObjects
            mteTriggerExistenceEventOwner
            mteTriggerExistenceEvent
            mteTriggerBooleanComparison
            mteTriggerBooleanValue
            mteTriggerBooleanStartup
            mteTriggerBooleanObjectsOwner
            mteTriggerBooleanObjects
            mteTriggerBooleanEventOwner
            mteTriggerBooleanEvent
            mteTriggerThresholdStartup
            mteTriggerThresholdRising
            mteTriggerThresholdFalling
            mteTriggerThresholdDeltaRising
            mteTriggerThresholdDeltaFalling
            mteTriggerThresholdObjectsOwner
            mteTriggerThresholdObjects
            mteTriggerThresholdRisingEventOwner
            mteTriggerThresholdRisingEvent
            mteTriggerThresholdFallingEventOwner
            mteTriggerThresholdFallingEvent
            mteTriggerThresholdDeltaRisingEventOwner
            mteTriggerThresholdDeltaRisingEvent
            mteTriggerThresholdDeltaFallingEventOwner
            mteTriggerThresholdDeltaFallingEvent
            mteObjectsID
            mteObjectsIDWildcard
            mteObjectsEntryStatus
            mteEventFailures
            mteEventComment
            mteEventActions
            mteEventEnabled
            mteEventEntryStatus
            mteEventNotification
            mteEventNotificationObjectsOwner
            mteEventNotificationObjects
            mteEventSetObject
            mteEventSetObjectWildcard
            mteEventSetValue
            mteEventSetTargetTag
            mteEventSetContextName
            mteEventSetContextNameWildcard
            mteHotTrigger
            mteHotTargetName
            mteHotContextName
            mteHotOID
            mteHotValue
            mteFailedReason
            mib-10.49.1.1.1
            mib-10.49.1.1.2
            mib-10.49.1.1.3
            mib-10.49.1.1.4
            mib-10.49.1.1.5
            mib-10.49.1.2.1.1.3
            mib-10.49.1.2.1.1.4
            mib-10.49.1.2.1.1.5
            mib-10.49.1.2.1.1.6
            mib-10.49.1.2.1.1.7
            mib-10.49.1.2.1.1.8
            mib-10.49.1.2.1.1.9
            mib-10.49.1.2.2.1.1
            mib-10.49.1.2.2.1.2
            mib-10.49.1.2.2.1.3
            mib-10.49.1.2.2.1.4
            mib-10.49.1.2.3.1.2
            mib-10.49.1.2.3.1.3
            mib-10.49.1.2.3.1.4
            mib-10.49.1.2.3.1.5
            mib-10.49.1.2.3.1.6
            mib-10.49.1.2.3.1.7
            mib-10.49.1.2.3.1.8
            mib-10.49.1.2.3.1.9
            mib-10.49.1.2.3.1.10
            mib-10.49.1.3.1.1.2
            mib-10.49.1.3.1.1.3
            mib-10.49.1.3.1.1.4
            mib-10.49.1.3.1.1.5
            mib-10.49.1.3.1.1.6
            mib-10.49.1.3.1.1.7
            mib-10.49.1.3.1.1.8
            mib-10.49.1.3.1.1.9
            nlmConfig.1
            nlmConfig.2
            nlmConfigLogEntry.2
            nlmConfigLogEntry.3
            nlmConfigLogEntry.4
            nlmConfigLogEntry.5
            nlmConfigLogEntry.6
            nlmConfigLogEntry.7
            nlmStats.1
            nlmStats.2
            nlmStatsLogEntry.1
            nlmStatsLogEntry.2
            nlmLogEntry.2
            nlmLogEntry.3
            nlmLogEntry.4
            nlmLogEntry.5
            nlmLogEntry.6
            nlmLogEntry.7
            nlmLogEntry.8
            nlmLogEntry.9
            nlmLogVariableEntry.2
            nlmLogVariableEntry.3
            nlmLogVariableEntry.4
            nlmLogVariableEntry.5
            nlmLogVariableEntry.6
            nlmLogVariableEntry.7
            nlmLogVariableEntry.8
            nlmLogVariableEntry.9
            nlmLogVariableEntry.10
            nlmLogVariableEntry.11
            nlmLogVariableEntry.12
            diffServDataPathEntry.2
            diffServDataPathEntry.3
            diffServDataPathEntry.4
            diffServClassifier.1
            diffServClfrEntry.2
            diffServClfrEntry.3
            diffServClassifier.3
            diffServClfrElementEntry.2
            diffServClfrElementEntry.3
            diffServClfrElementEntry.4
            diffServClfrElementEntry.5
            diffServClfrElementEntry.6
            diffServClassifier.5
            diffServMultiFieldClfrEntry.2
            diffServMultiFieldClfrEntry.3
            diffServMultiFieldClfrEntry.4
            diffServMultiFieldClfrEntry.5
            diffServMultiFieldClfrEntry.6
            diffServMultiFieldClfrEntry.7
            diffServMultiFieldClfrEntry.8
            diffServMultiFieldClfrEntry.9
            diffServMultiFieldClfrEntry.10
            diffServMultiFieldClfrEntry.11
            diffServMultiFieldClfrEntry.12
            diffServMultiFieldClfrEntry.13
            diffServMultiFieldClfrEntry.14
            diffServMultiFieldClfrEntry.15
            diffServMeter.1
            diffServMeterEntry.2
            diffServMeterEntry.3
            diffServMeterEntry.4
            diffServMeterEntry.5
            diffServMeterEntry.6
            diffServTBParam.1
            diffServTBParamEntry.2
            diffServTBParamEntry.3
            diffServTBParamEntry.4
            diffServTBParamEntry.5
            diffServTBParamEntry.6
            diffServTBParamEntry.7
            diffServAction.1
            diffServActionEntry.2
            diffServActionEntry.3
            diffServActionEntry.4
            diffServActionEntry.5
            diffServActionEntry.6
            diffServDscpMarkActEntry.1
            diffServAction.4
            diffServCountActEntry.2
            diffServCountActEntry.3
            diffServCountActEntry.4
            diffServCountActEntry.5
            diffServAlgDrop.1
            diffServAlgDropEntry.2
            diffServAlgDropEntry.3
            diffServAlgDropEntry.4
            diffServAlgDropEntry.5
            diffServAlgDropEntry.6
            diffServAlgDropEntry.7
            diffServAlgDropEntry.8
            diffServAlgDropEntry.9
            diffServAlgDropEntry.10
            diffServAlgDropEntry.11
            diffServAlgDropEntry.12
            diffServAlgDrop.3
            diffServRandomDropEntry.2
            diffServRandomDropEntry.3
            diffServRandomDropEntry.4
            diffServRandomDropEntry.5
            diffServRandomDropEntry.6
            diffServRandomDropEntry.7
            diffServRandomDropEntry.8
            diffServRandomDropEntry.9
            diffServRandomDropEntry.10
            diffServQueue.1
            diffServQEntry.2
            diffServQEntry.3
            diffServQEntry.4
            diffServQEntry.5
            diffServQEntry.6
            diffServScheduler.1
            diffServSchedulerEntry.2
            diffServSchedulerEntry.3
            diffServSchedulerEntry.4
            diffServSchedulerEntry.5
            diffServSchedulerEntry.6
            diffServSchedulerEntry.7
            diffServScheduler.3
            diffServMinRateEntry.2
            diffServMinRateEntry.3
            diffServMinRateEntry.4
            diffServMinRateEntry.5
            diffServMinRateEntry.6
            diffServScheduler.5
            diffServMaxRateEntry.3
            diffServMaxRateEntry.4
            diffServMaxRateEntry.5
            diffServMaxRateEntry.6
            diffServMaxRateEntry.7
            entPhySensorType
            entPhySensorScale
            entPhySensorPrecision
            entPhySensorValue
            entPhySensorOperStatus
            entPhySensorUnitsDisplay
            entPhySensorValueTimeStamp
            entPhySensorValueUpdateRate
            natBindDefIdleTimeout
            natUdpDefIdleTimeout
            natIcmpDefIdleTimeout
            natOtherDefIdleTimeout
            natTcpDefIdleTimeout
            natTcpDefNegTimeout
            natInterfaceRealm
            natInterfaceServiceType
            natInterfaceInTranslates
            natInterfaceOutTranslates
            natInterfaceDiscards
            natInterfaceStorageType
            natInterfaceRowStatus
            natAddrBindNumberOfEntries
            natAddrBindGlobalAddrType
            natAddrBindGlobalAddr
            natAddrBindId
            natAddrBindTranslationEntity
            natAddrBindType
            natAddrBindMapIndex
            natAddrBindSessions
            natAddrBindMaxIdleTime
            natAddrBindCurrentIdleTime
            natAddrBindInTranslates
            natAddrBindOutTranslates
            natAddrPortBindNumberOfEntries
            natMIBObjects.10.169.1.1
            natMIBObjects.10.169.1.2
            natMIBObjects.10.169.1.3
            natMIBObjects.10.169.1.4
            natMIBObjects.10.169.1.5
            natMIBObjects.10.169.1.6
            natMIBObjects.10.169.1.7
            natMIBObjects.10.169.1.8
            natMIBObjects.10.196.1.2
            natMIBObjects.10.196.1.3
            natMIBObjects.10.196.1.4
            natMIBObjects.10.196.1.5
            natMIBObjects.10.196.1.6
            natMIBObjects.10.196.1.7
            natPoolRealm
            natPoolWatermarkLow
            natPoolWatermarkHigh
            natPoolPortMin
            natPoolPortMax
            natPoolRangeType
            natPoolRangeBegin
            natPoolRangeEnd
            natPoolRangeAllocations
            natPoolRangeDeallocations
            entStateTable.1.1
            entStateTable.1.2
            entStateTable.1.3
            entStateTable.1.4
            entStateTable.1.5
            entStateTable.1.6
            pimInterfaceAddressType
            pimInterfaceAddress
            pimInterfaceGenerationIDValue
            pimInterfaceDR
            pimInterfaceDRPriority
            pimInterfaceDRPriorityEnabled
            pimInterfaceHelloInterval
            pimInterfaceTrigHelloInterval
            pimInterfaceHelloHoldtime
            pimInterfaceJoinPruneInterval
            pimInterfaceJoinPruneHoldtime
            pimInterfaceDFElectionRobustness
            pimInterfaceLanDelayEnabled
            pimInterfacePropagationDelay
            pimInterfaceOverrideInterval
            pimInterfaceEffectPropagDelay
            pimInterfaceEffectOverrideIvl
            pimInterfaceSuppressionEnabled
            pimInterfaceBidirCapable
            pimInterfaceDomainBorder
            pimInterfaceStubInterface
            pimInterfacePruneLimitInterval
            pimInterfaceGraftRetryInterval
            pimInterfaceSRPriorityEnabled
            pimInterfaceStatus
            pimNeighborGenerationIDPresent
            pimNeighborGenerationIDValue
            pimNeighborUpTime
            pimNeighborExpiryTime
            pimNeighborDRPriorityPresent
            pimNeighborDRPriority
            pimNeighborLanPruneDelayPresent
            pimNeighborTBit
            pimNeighborPropagationDelay
            pimNeighborOverrideInterval
            pimNeighborBidirCapable
            pimNeighborSRCapable
            pimNbrSecAddress
            pimStarGUpTime
            pimStarGPimMode
            pimStarGRPAddressType
            pimStarGRPAddress
            pimStarGPimModeOrigin
            pimStarGRPIsLocal
            pimStarGUpstreamJoinState
            pimStarGUpstreamJoinTimer
            pimStarGUpstreamNeighborType
            pimStarGUpstreamNeighbor
            pimStarGRPFIfIndex
            pimStarGRPFNextHopType
            pimStarGRPFNextHop
            pimStarGRPFRouteProtocol
            pimStarGRPFRouteAddress
            pimStarGRPFRoutePrefixLength
            pimStarGRPFRouteMetricPref
            pimStarGRPFRouteMetric
            pimStarGIUpTime
            pimStarGILocalMembership
            pimStarGIJoinPruneState
            pimStarGIPrunePendingTimer
            pimStarGIJoinExpiryTimer
            pimStarGIAssertState
            pimStarGIAssertTimer
            pimStarGIAssertWinnerAddressType
            pimStarGIAssertWinnerAddress
            pimStarGIAssertWinnerMetricPref
            pimStarGIAssertWinnerMetric
            pimSGUpTime
            pimSGPimMode
            pimSGUpstreamJoinState
            pimSGUpstreamJoinTimer
            pimSGUpstreamNeighbor
            pimSGRPFIfIndex
            pimSGRPFNextHopType
            pimSGRPFNextHop
            pimSGRPFRouteProtocol
            pimSGRPFRouteAddress
            pimSGRPFRoutePrefixLength
            pimSGRPFRouteMetricPref
            pimSGRPFRouteMetric
            pimSGSPTBit
            pimSGKeepaliveTimer
            pimSGDRRegisterState
            pimSGDRRegisterStopTimer
            pimSGRPRegisterPMBRAddressType
            pimSGRPRegisterPMBRAddress
            pimSGUpstreamPruneState
            pimSGUpstreamPruneLimitTimer
            pimSGOriginatorState
            pimSGSourceActiveTimer
            pimSGStateRefreshTimer
            pimSGIUpTime
            pimSGILocalMembership
            pimSGIJoinPruneState
            pimSGIPrunePendingTimer
            pimSGIJoinExpiryTimer
            pimSGIAssertState
            pimSGIAssertTimer
            pimSGIAssertWinnerAddressType
            pimSGIAssertWinnerAddress
            pimSGIAssertWinnerMetricPref
            pimSGIAssertWinnerMetric
            pimSGRptUpTime
            pimSGRptUpstreamPruneState
            pimSGRptUpstreamOverrideTimer
            pimSGRptIUpTime
            pimSGRptILocalMembership
            pimSGRptIJoinPruneState
            pimSGRptIPrunePendingTimer
            pimSGRptIPruneExpiryTimer
            pimBidirDFElectionWinnerAddressType
            pimBidirDFElectionWinnerAddress
            pimBidirDFElectionWinnerUpTime
            pimBidirDFElectionWinnerMetricPref
            pimBidirDFElectionWinnerMetric
            pimBidirDFElectionState
            pimBidirDFElectionStateTimer
            pimStaticRPRPAddress
            pimStaticRPPimMode
            pimStaticRPOverrideDynamic
            pimStaticRPPrecedence
            pimStaticRPRowStatus
            pimAnycastRPSetLocalRouter
            pimAnycastRPSetRowStatus
            pimGroupMappingPimMode
            pimGroupMappingPrecedence
            pimKeepalivePeriod
            pimRegisterSuppressionTime
            pimStarGEntries
            pimStarGIEntries
            pimSGEntries
            pimSGIEntries
            pimSGRptEntries
            pimSGRptIEntries
            pimOutAsserts
            pimInAsserts
            pimLastAssertInterface
            pimLastAssertGroupAddressType
            pimLastAssertGroupAddress
            pimLastAssertSourceAddressType
            pimLastAssertSourceAddress
            pimNeighborLossNotificationPeriod
            pimNeighborLossCount
            pimInvalidRegisterNotificationPeriod
            pimInvalidRegisterMsgsRcvd
            pimInvalidRegisterAddressType
            pimInvalidRegisterOrigin
            pimInvalidRegisterGroup
            pimInvalidRegisterRp
            pimInvalidJoinPruneNotificationPeriod
            pimInvalidJoinPruneMsgsRcvd
            pimInvalidJoinPruneAddressType
            pimInvalidJoinPruneOrigin
            pimInvalidJoinPruneGroup
            pimInvalidJoinPruneRp
            pimRPMappingNotificationPeriod
            pimRPMappingChangeCount
            pimInterfaceElectionNotificationPeriod
            pimInterfaceElectionWinCount
            mgmdHostInterfaceQuerier
            mgmdHostInterfaceStatus
            mgmdHostInterfaceVersion
            mgmdHostInterfaceVersion1QuerierTimer
            mgmdHostInterfaceVersion2QuerierTimer
            mgmdHostInterfaceVersion3Robustness
            mgmdRouterInterfaceQuerier
            mgmdRouterInterfaceQueryInterval
            mgmdRouterInterfaceStatus
            mgmdRouterInterfaceVersion
            mgmdRouterInterfaceQueryMaxResponseTime
            mgmdRouterInterfaceQuerierUpTime
            mgmdRouterInterfaceQuerierExpiryTime
            mgmdRouterInterfaceWrongVersionQueries
            mgmdRouterInterfaceJoins
            mgmdRouterInterfaceProxyIfIndex
            mgmdRouterInterfaceGroups
            mgmdRouterInterfaceRobustness
            mgmdRouterInterfaceLastMemberQueryInterval
            mgmdRouterInterfaceLastMemberQueryCount
            mgmdRouterInterfaceStartupQueryCount
            mgmdRouterInterfaceStartupQueryInterval
            mgmdHostCacheUpTime
            mgmdHostCacheLastReporter
            mgmdHostCacheSourceFilterMode
            mgmdRouterCacheLastReporter
            mgmdRouterCacheUpTime
            mgmdRouterCacheExpiryTime
            mgmdRouterCacheExcludeModeExpiryTimer
            mgmdRouterCacheVersion1HostTimer
            mgmdRouterCacheVersion2HostTimer
            mgmdRouterCacheSourceFilterMode
            mgmdInverseHostCacheAddress
            mgmdInverseRouterCacheAddress
            mgmdHostSrcListExpire
            mgmdRouterSrcListExpire
            ospfv3GeneralGroup.1
            ospfv3GeneralGroup.2
            ospfv3GeneralGroup.3
            ospfv3GeneralGroup.4
            ospfv3GeneralGroup.5
            ospfv3GeneralGroup.6
            ospfv3GeneralGroup.7
            ospfv3GeneralGroup.8
            ospfv3GeneralGroup.9
            ospfv3GeneralGroup.10
            ospfv3GeneralGroup.11
            ospfv3GeneralGroup.12
            ospfv3GeneralGroup.13
            ospfv3GeneralGroup.14
            ospfv3GeneralGroup.15
            ospfv3GeneralGroup.16
            ospfv3GeneralGroup.17
            ospfv3GeneralGroup.18
            ospfv3GeneralGroup.19
            ospfv3GeneralGroup.20
            ospfv3GeneralGroup.21
            ospfv3GeneralGroup.22
            ospfv3GeneralGroup.23
            ospfv3GeneralGroup.24
            ospfv3GeneralGroup.25
            ospfv3AreaEntry.2
            ospfv3AreaEntry.3
            ospfv3AreaEntry.4
            ospfv3AreaEntry.5
            ospfv3AreaEntry.6
            ospfv3AreaEntry.7
            ospfv3AreaEntry.8
            ospfv3AreaEntry.9
            ospfv3AreaEntry.10
            ospfv3AreaEntry.11
            ospfv3AreaEntry.12
            ospfv3AreaEntry.13
            ospfv3AreaEntry.14
            ospfv3AreaEntry.15
            ospfv3AreaEntry.16
            ospfv3AsLsdbEntry.4
            ospfv3AsLsdbEntry.5
            ospfv3AsLsdbEntry.6
            ospfv3AsLsdbEntry.7
            ospfv3AsLsdbEntry.8
            ospfv3AreaLsdbEntry.5
            ospfv3AreaLsdbEntry.6
            ospfv3AreaLsdbEntry.7
            ospfv3AreaLsdbEntry.8
            ospfv3AreaLsdbEntry.9
            ospfv3LinkLsdbEntry.6
            ospfv3LinkLsdbEntry.7
            ospfv3LinkLsdbEntry.8
            ospfv3LinkLsdbEntry.9
            ospfv3LinkLsdbEntry.10
            ospfv3HostEntry.3
            ospfv3HostEntry.4
            ospfv3HostEntry.5
            ospfv3IfEntry.3
            ospfv3IfEntry.4
            ospfv3IfEntry.5
            ospfv3IfEntry.6
            ospfv3IfEntry.7
            ospfv3IfEntry.8
            ospfv3IfEntry.9
            ospfv3IfEntry.10
            ospfv3IfEntry.11
            ospfv3IfEntry.12
            ospfv3IfEntry.13
            ospfv3IfEntry.14
            ospfv3IfEntry.15
            ospfv3IfEntry.16
            ospfv3IfEntry.17
            ospfv3IfEntry.18
            ospfv3IfEntry.19
            ospfv3IfEntry.20
            ospfv3IfEntry.21
            ospfv3IfEntry.22
            ospfv3IfEntry.23
            ospfv3IfEntry.24
            ospfv3IfEntry.25
            ospfv3VirtIfEntry.3
            ospfv3VirtIfEntry.4
            ospfv3VirtIfEntry.5
            ospfv3VirtIfEntry.6
            ospfv3VirtIfEntry.7
            ospfv3VirtIfEntry.8
            ospfv3VirtIfEntry.9
            ospfv3VirtIfEntry.10
            ospfv3VirtIfEntry.11
            ospfv3VirtIfEntry.12
            ospfv3VirtIfEntry.13
            ospfv3NbrEntry.4
            ospfv3NbrEntry.5
            ospfv3NbrEntry.6
            ospfv3NbrEntry.7
            ospfv3NbrEntry.8
            ospfv3NbrEntry.9
            ospfv3NbrEntry.10
            ospfv3NbrEntry.11
            ospfv3NbrEntry.12
            ospfv3NbrEntry.13
            ospfv3NbrEntry.14
            ospfv3NbrEntry.15
            ospfv3CfgNbrEntry.5
            ospfv3CfgNbrEntry.6
            ospfv3VirtNbrEntry.3
            ospfv3VirtNbrEntry.4
            ospfv3VirtNbrEntry.5
            ospfv3VirtNbrEntry.6
            ospfv3VirtNbrEntry.7
            ospfv3VirtNbrEntry.8
            ospfv3VirtNbrEntry.9
            ospfv3VirtNbrEntry.10
            ospfv3VirtNbrEntry.11
            ospfv3VirtNbrEntry.12
            ospfv3VirtNbrEntry.13
            ospfv3VirtNbrEntry.14
            ospfv3VirtNbrEntry.15
            ospfv3AreaAggregateEntry.6
            ospfv3AreaAggregateEntry.7
            ospfv3AreaAggregateEntry.8
            ospfv3VirtLinkLsdbEntry.6
            ospfv3VirtLinkLsdbEntry.7
            ospfv3VirtLinkLsdbEntry.8
            ospfv3VirtLinkLsdbEntry.9
            ospfv3VirtLinkLsdbEntry.10
            ntpEntInfo.1
            ntpEntInfo.2
            ntpEntInfo.3
            ntpEntInfo.4
            ntpEntInfo.5
            ntpEntInfo.6
            ntpEntInfo.7
            ntpEntStatus.1
            ntpEntStatus.2
            ntpEntStatus.3
            ntpEntStatus.4
            ntpEntStatus.5
            ntpEntStatus.6
            ntpEntStatus.7
            ntpEntStatus.8
            ntpEntStatus.9
            ntpEntStatus.10
            ntpEntStatus.11
            ntpEntStatus.12
            ntpEntStatus.13
            ntpEntStatus.14
            ntpEntStatus.15
            ntpEntStatus.16
            ntpEntStatus.17.1.2
            ntpEntStatus.17.1.3
            ntpAssocName
            ntpAssocRefId
            ntpAssocAddressType
            ntpAssocAddress
            ntpAssocOffset
            ntpAssocStratum
            ntpAssocStatusJitter
            ntpAssocStatusDelay
            ntpAssocStatusDispersion
            ntpAssocStatInPkts
            ntpAssocStatOutPkts
            ntpAssocStatProtocolError
            ntpSnmpMIBObjects.4.1
            ntpSnmpMIBObjects.4.2
            lispFeaturesItrEnabled
            lispFeaturesEtrEnabled
            lispFeaturesProxyItrEnabled
            lispFeaturesProxyEtrEnabled
            lispFeaturesMapServerEnabled
            lispFeaturesMapResolverEnabled
            lispFeaturesMapCacheSize
            lispFeaturesMapCacheLimit
            lispFeaturesEtrMapCacheTtl
            lispFeaturesRlocProbeEnabled
            lispFeaturesEtrAcceptMapDataEnabled
            lispFeaturesEtrAcceptMapDataVerifyEnabled
            lispFeaturesRouterTimeStamp
            lispIidToVrfName
            lispGlobalStatsMapRequestsIn
            lispGlobalStatsMapRequestsOut
            lispGlobalStatsMapRepliesIn
            lispGlobalStatsMapRepliesOut
            lispGlobalStatsMapRegistersIn
            lispGlobalStatsMapRegistersOut
            lispMappingDatabaseLsb
            lispMappingDatabaseEidPartitioned
            lispMappingDatabaseTimeStamp
            lispMappingDatabaseLocatorRlocPriority
            lispMappingDatabaseLocatorRlocWeight
            lispMappingDatabaseLocatorRlocMPriority
            lispMappingDatabaseLocatorRlocMWeight
            lispMappingDatabaseLocatorRlocState
            lispMappingDatabaseLocatorRlocLocal
            lispMappingDatabaseLocatorRlocTimeStamp
            lispMapCacheEidTimeStamp
            lispMapCacheEidExpiryTime
            lispMapCacheEidState
            lispMapCacheEidAuthoritative
            lispMapCacheEidEncapOctets
            lispMapCacheEidEncapPackets
            lispMapCacheLocatorRlocPriority
            lispMapCacheLocatorRlocWeight
            lispMapCacheLocatorRlocMPriority
            lispMapCacheLocatorRlocMWeight
            lispMapCacheLocatorRlocState
            lispMapCacheLocatorRlocTimeStamp
            lispMapCacheLocatorRlocLastPriorityChange
            lispMapCacheLocatorRlocLastWeightChange
            lispMapCacheLocatorRlocLastMPriorityChange
            lispMapCacheLocatorRlocLastMWeightChange
            lispMapCacheLocatorRlocLastStateChange
            lispMapCacheLocatorRlocRtt
            lispConfiguredLocatorRlocState
            lispConfiguredLocatorRlocLocal
            lispConfiguredLocatorRlocTimeStamp
            lispEidRegistrationSiteName
            lispEidRegistrationSiteDescription
            lispEidRegistrationIsRegistered
            lispEidRegistrationFirstTimeStamp
            lispEidRegistrationLastTimeStamp
            lispEidRegistrationLastRegisterSenderLength
            lispEidRegistrationLastRegisterSender
            lispEidRegistrationAuthenticationErrors
            lispEidRegistrationRlocsMismatch
            lispEidRegistrationEtrLastTimeStamp
            lispEidRegistrationEtrTtl
            lispEidRegistrationEtrProxyReply
            lispEidRegistrationEtrWantsMapNotify
            lispEidRegistrationLocatorRlocState
            lispEidRegistrationLocatorIsLocal
            lispEidRegistrationLocatorPriority
            lispEidRegistrationLocatorWeight
            lispEidRegistrationLocatorMPriority
            lispEidRegistrationLocatorMWeight
            lispUseMapServerState
            lispUseMapResolverState
            lispUseProxyEtrPriority
            lispUseProxyEtrWeight
            lispUseProxyEtrMPriority
            lispUseProxyEtrMWeight
            lispUseProxyEtrState
            pim.1
            pimInterfaceEntry.2
            pimInterfaceEntry.3
            pimInterfaceEntry.4
            pimInterfaceEntry.5
            pimInterfaceEntry.6
            pimInterfaceEntry.7
            pimInterfaceEntry.8
            pimInterfaceEntry.9
            pimNeighborEntry.2
            pimNeighborEntry.3
            pimNeighborEntry.4
            pimNeighborEntry.5
            pimIpMRouteEntry.1
            pimIpMRouteEntry.2
            pimIpMRouteEntry.3
            pimIpMRouteEntry.4
            pimIpMRouteEntry.5
            pimRPEntry.3
            pimRPEntry.4
            pimRPEntry.5
            pimRPEntry.6
            pimRPSetEntry.4
            pimRPSetEntry.5
            pimIpMRouteNextHopEntry.2
            pimCandidateRPEntry.3
            pimCandidateRPEntry.4
            pimComponentEntry.2
            pimComponentEntry.3
            pimComponentEntry.4
            pimComponentEntry.5
            msdp.1
            msdp.2
            msdp.3
            msdpPeerEntry.3
            msdpPeerEntry.4
            msdpPeerEntry.5
            msdpPeerEntry.6
            msdpPeerEntry.7
            msdpPeerEntry.8
            msdpPeerEntry.9
            msdpPeerEntry.10
            msdpPeerEntry.11
            msdpPeerEntry.12
            msdpPeerEntry.13
            msdpPeerEntry.14
            msdpPeerEntry.15
            msdpPeerEntry.16
            msdpPeerEntry.17
            msdpPeerEntry.18
            msdpPeerEntry.19
            msdpPeerEntry.20
            msdpPeerEntry.21
            msdpPeerEntry.22
            msdpPeerEntry.23
            msdpPeerEntry.24
            msdpPeerEntry.25
            msdpPeerEntry.26
            msdpPeerEntry.27
            msdpPeerEntry.30
            msdpSACacheEntry.4
            msdpSACacheEntry.5
            msdpSACacheEntry.6
            msdpSACacheEntry.7
            msdpSACacheEntry.8
            msdpSACacheEntry.9
            msdpSACacheEntry.10
            msdp.9
            mplsTeMIB.1.1
            mplsTeMIB.1.2
            mplsTeMIB.1.3
            mplsTeMIB.1.4
            mplsTeMIB.2.1
            MPLS-TE-MIB::mplsTunnelEntry.5
            MPLS-TE-MIB::mplsTunnelEntry.6
            MPLS-TE-MIB::mplsTunnelEntry.7
            MPLS-TE-MIB::mplsTunnelEntry.8
            MPLS-TE-MIB::mplsTunnelEntry.9
            MPLS-TE-MIB::mplsTunnelEntry.10
            MPLS-TE-MIB::mplsTunnelEntry.11
            MPLS-TE-MIB::mplsTunnelEntry.12
            MPLS-TE-MIB::mplsTunnelEntry.13
            MPLS-TE-MIB::mplsTunnelEntry.14
            MPLS-TE-MIB::mplsTunnelEntry.15
            MPLS-TE-MIB::mplsTunnelEntry.16
            MPLS-TE-MIB::mplsTunnelEntry.17
            MPLS-TE-MIB::mplsTunnelEntry.18
            MPLS-TE-MIB::mplsTunnelEntry.19
            MPLS-TE-MIB::mplsTunnelEntry.20
            MPLS-TE-MIB::mplsTunnelEntry.21
            MPLS-TE-MIB::mplsTunnelEntry.22
            MPLS-TE-MIB::mplsTunnelEntry.23
            MPLS-TE-MIB::mplsTunnelEntry.24
            MPLS-TE-MIB::mplsTunnelEntry.25
            MPLS-TE-MIB::mplsTunnelEntry.26
            MPLS-TE-MIB::mplsTunnelEntry.27
            MPLS-TE-MIB::mplsTunnelEntry.28
            MPLS-TE-MIB::mplsTunnelEntry.29
            MPLS-TE-MIB::mplsTunnelEntry.30
            MPLS-TE-MIB::mplsTunnelEntry.31
            MPLS-TE-MIB::mplsTunnelEntry.32
            MPLS-TE-MIB::mplsTunnelEntry.33
            MPLS-TE-MIB::mplsTunnelAdminStatus
            MPLS-TE-MIB::mplsTunnelOperStatus
            MPLS-TE-MIB::mplsTunnelEntry.36
            MPLS-TE-MIB::mplsTunnelEntry.37
            mplsTeMIB.2.3
            mplsTeMIB.10.36.1.4
            mplsTeMIB.10.36.1.5
            mplsTeMIB.10.36.1.6
            mplsTeMIB.10.36.1.7
            mplsTeMIB.10.36.1.8
            mplsTeMIB.10.36.1.9
            mplsTeMIB.10.36.1.10
            mplsTeMIB.10.36.1.11
            mplsTeMIB.10.36.1.12
            mplsTeMIB.10.36.1.13
            mplsTeMIB.2.5
            MPLS-TE-MIB::mplsTunnelResourceMaxRate
            MPLS-TE-MIB::mplsTunnelResourceEntry.3
            MPLS-TE-MIB::mplsTunnelResourceEntry.4
            MPLS-TE-MIB::mplsTunnelResourceEntry.5
            MPLS-TE-MIB::mplsTunnelResourceEntry.6
            MPLS-TE-MIB::mplsTunnelARHopEntry.3
            MPLS-TE-MIB::mplsTunnelARHopEntry.4
            MPLS-TE-MIB::mplsTunnelARHopEntry.5
            MPLS-TE-MIB::mplsTunnelARHopEntry.6
            MPLS-TE-MIB::mplsTunnelARHopEntry.7
            MPLS-TE-MIB::mplsTunnelARHopEntry.8
            MPLS-TE-MIB::mplsTunnelARHopEntry.9
            MPLS-TE-MIB::mplsTunnelCHopEntry.3
            MPLS-TE-MIB::mplsTunnelCHopEntry.4
            MPLS-TE-MIB::mplsTunnelCHopEntry.5
            MPLS-TE-MIB::mplsTunnelCHopEntry.6
            MPLS-TE-MIB::mplsTunnelCHopEntry.7
            MPLS-TE-MIB::mplsTunnelCHopEntry.8
            MPLS-TE-MIB::mplsTunnelCHopEntry.9
            MPLS-TE-MIB::mplsTunnelPerfEntry.1
            MPLS-TE-MIB::mplsTunnelPerfEntry.2
            MPLS-TE-MIB::mplsTunnelPerfEntry.3
            MPLS-TE-MIB::mplsTunnelPerfEntry.4
            MPLS-TE-MIB::mplsTunnelPerfEntry.5
            mplsTeMIB.2.10
            MPLS-LSR-MIB::mplsInterfaceConfEntry.2
            MPLS-LSR-MIB::mplsInterfaceConfEntry.3
            MPLS-LSR-MIB::mplsInterfaceConfEntry.4
            MPLS-LSR-MIB::mplsInterfaceConfEntry.5
            MPLS-LSR-MIB::mplsInterfaceConfEntry.6
            MPLS-LSR-MIB::mplsInterfaceConfEntry.7
            MPLS-LSR-MIB::mplsInterfaceConfEntry.8
            MPLS-LSR-MIB::mplsInterfaceConfEntry.9
            MPLS-LSR-MIB::mplsInterfaceConfEntry.10
            MPLS-LSR-MIB::mplsInterfaceConfEntry.11
            MPLS-LSR-MIB::mplsInterfacePerfEntry.1
            MPLS-LSR-MIB::mplsInterfacePerfEntry.2
            MPLS-LSR-MIB::mplsInterfacePerfEntry.3
            MPLS-LSR-MIB::mplsInterfacePerfEntry.4
            MPLS-LSR-MIB::mplsInterfacePerfEntry.5
            MPLS-LSR-MIB::mplsInterfacePerfEntry.6
            MPLS-LSR-MIB::mplsInterfacePerfEntry.7
            MPLS-LSR-MIB::mplsInterfacePerfEntry.8
            MPLS-LSR-MIB::mplsInSegmentEntry.3
            MPLS-LSR-MIB::mplsInSegmentEntry.4
            MPLS-LSR-MIB::mplsInSegmentEntry.5
            MPLS-LSR-MIB::mplsInSegmentEntry.6
            MPLS-LSR-MIB::mplsInSegmentEntry.7
            MPLS-LSR-MIB::mplsInSegmentEntry.8
            MPLS-LSR-MIB::mplsInSegmentEntry.9
            MPLS-LSR-MIB::mplsInSegmentEntry.10
            MPLS-LSR-MIB::mplsInSegmentEntry.11
            MPLS-LSR-MIB::mplsInSegmentPerfEntry.1
            MPLS-LSR-MIB::mplsInSegmentPerfEntry.2
            MPLS-LSR-MIB::mplsInSegmentPerfEntry.3
            MPLS-LSR-MIB::mplsInSegmentPerfEntry.4
            MPLS-LSR-MIB::mplsInSegmentPerfEntry.5
            MPLS-LSR-MIB::mplsInSegmentPerfEntry.6
            mplsLsrMIB.1.5
            MPLS-LSR-MIB::mplsOutSegmentEntry.2
            MPLS-LSR-MIB::mplsOutSegmentEntry.3
            MPLS-LSR-MIB::mplsOutSegmentEntry.4
            MPLS-LSR-MIB::mplsOutSegmentEntry.5
            MPLS-LSR-MIB::mplsOutSegmentEntry.6
            MPLS-LSR-MIB::mplsOutSegmentEntry.7
            MPLS-LSR-MIB::mplsOutSegmentEntry.8
            MPLS-LSR-MIB::mplsOutSegmentEntry.9
            MPLS-LSR-MIB::mplsOutSegmentEntry.10
            MPLS-LSR-MIB::mplsOutSegmentEntry.11
            MPLS-LSR-MIB::mplsOutSegmentEntry.12
            MPLS-LSR-MIB::mplsOutSegmentEntry.13
            MPLS-LSR-MIB::mplsOutSegmentEntry.14
            MPLS-LSR-MIB::mplsOutSegmentPerfEntry.1
            MPLS-LSR-MIB::mplsOutSegmentPerfEntry.2
            MPLS-LSR-MIB::mplsOutSegmentPerfEntry.3
            MPLS-LSR-MIB::mplsOutSegmentPerfEntry.4
            MPLS-LSR-MIB::mplsOutSegmentPerfEntry.5
            MPLS-LSR-MIB::mplsOutSegmentPerfEntry.6
            mplsLsrMIB.1.8
            MPLS-LSR-MIB::mplsXCLspId
            MPLS-LSR-MIB::mplsXCEntry.3
            MPLS-LSR-MIB::mplsXCEntry.4
            MPLS-LSR-MIB::mplsXCEntry.5
            MPLS-LSR-MIB::mplsXCEntry.6
            MPLS-LSR-MIB::mplsXCEntry.7
            MPLS-LSR-MIB::mplsXCEntry.8
            MPLS-LSR-MIB::mplsXCEntry.9
            mplsLsrMIB.1.10
            mplsLsrMIB.1.11
            MPLS-LSR-MIB::mplsLabelStackEntry.3
            MPLS-LSR-MIB::mplsLabelStackEntry.4
            MPLS-LSR-MIB::mplsLabelStackEntry.5
            mplsLsrMIB.1.13
            MPLS-LSR-MIB::mplsTrafficParamEntry.2
            MPLS-LSR-MIB::mplsTrafficParamEntry.3
            MPLS-LSR-MIB::mplsTrafficParamEntry.4
            MPLS-LSR-MIB::mplsTrafficParamEntry.5
            MPLS-LSR-MIB::mplsTrafficParamEntry.6
            mplsLsrMIB.1.15
            mplsLsrMIB.1.16
            mplsLsrMIB.1.17
            mplsVpnMIB.1.1.1
            mplsVpnMIB.1.1.2
            mplsVpnMIB.1.1.3
            mplsVpnMIB.1.1.4
            mplsVpnMIB.1.1.5
            mplsVpnInterfaceConfEntry.2
            mplsVpnInterfaceConfEntry.3
            mplsVpnInterfaceConfEntry.4
            mplsVpnInterfaceConfEntry.5
            mplsVpnInterfaceConfEntry.6
            mplsVpnVrfEntry.2
            mplsVpnVrfEntry.3
            mplsVpnVrfEntry.4
            mplsVpnVrfEntry.5
            mplsVpnVrfEntry.6
            mplsVpnVrfEntry.7
            mplsVpnVrfEntry.8
            mplsVpnVrfConfHighRouteThreshold
            mplsVpnVrfEntry.10
            mplsVpnVrfEntry.11
            mplsVpnVrfEntry.12
            mplsVpnVrfEntry.13
            mplsVpnVrfRouteTargetEntry.4
            mplsVpnVrfRouteTargetEntry.5
            mplsVpnVrfRouteTargetEntry.6
            mplsVpnVrfBgpNbrAddrEntry.2
            mplsVpnVrfBgpNbrAddrEntry.3
            mplsVpnVrfBgpNbrAddrEntry.4
            mplsVpnVrfBgpNbrAddrEntry.5
            mplsVpnVrfBgpNbrAddrEntry.6
            mplsVpnVrfBgpNbrPrefixEntry.4
            mplsVpnVrfBgpNbrPrefixEntry.5
            mplsVpnVrfBgpNbrPrefixEntry.6
            mplsVpnVrfBgpNbrPrefixEntry.7
            mplsVpnVrfBgpNbrPrefixEntry.8
            mplsVpnVrfBgpNbrPrefixEntry.9
            mplsVpnVrfBgpNbrPrefixEntry.10
            mplsVpnVrfBgpNbrPrefixEntry.11
            mplsVpnVrfBgpNbrPrefixEntry.12
            mplsVpnVrfBgpNbrPrefixEntry.13
            mplsVpnVrfBgpNbrPrefixEntry.14
            mplsVpnVrfSecIllegalLabelViolations
            mplsVpnVrfSecEntry.2
            mplsVpnVrfPerfEntry.1
            mplsVpnVrfPerfEntry.2
            mplsVpnVrfPerfCurrNumRoutes
            mplsVpnVrfRouteEntry.2
            mplsVpnVrfRouteEntry.4
            mplsVpnVrfRouteEntry.5
            mplsVpnVrfRouteEntry.6
            mplsVpnVrfRouteEntry.7
            mplsVpnVrfRouteEntry.8
            mplsVpnVrfRouteEntry.9
            mplsVpnVrfRouteEntry.10
            mplsVpnVrfRouteEntry.11
            mplsVpnVrfRouteEntry.12
            mplsVpnVrfRouteEntry.13
            mplsVpnVrfRouteEntry.14
            mplsVpnVrfRouteEntry.15
            mplsVpnVrfRouteEntry.16
            mplsVpnVrfRouteEntry.17
            mplsVpnVrfRouteEntry.18
            mplsVpnVrfRouteEntry.19
            mplsVpnVrfRouteEntry.20
            lsystem.1
            lsystem.2
            lsystem.3
            lsystem.4
            lsystem.5
            lsystem.6
            lsystem.8
            lsystem.9
            lsystem.10
            lsystem.11
            lsystem.12
            lsystem.13
            lsystem.14
            lsystem.15
            lsystem.16
            lsystem.17
            lsystem.18
            lsystem.19
            lsystem.20
            lsystem.21
            lsystem.22
            lsystem.23
            lsystem.24
            lsystem.25
            lsystem.26
            lsystem.27
            lsystem.28
            lsystem.29
            lsystem.30
            lsystem.31
            lsystem.32
            lsystem.33
            lsystem.34
            lsystem.35
            lsystem.36
            lsystem.37
            lsystem.38
            lsystem.39
            lsystem.40
            lsystem.41
            lsystem.42
            lsystem.43
            lsystem.44
            lsystem.45
            lsystem.46
            lsystem.47
            lsystem.48
            lsystem.49
            lsystem.50
            lsystem.51
            lsystem.52
            lsystem.53
            lsystem.54
            lsystem.55
            lsystem.56
            lsystem.57
            lsystem.58
            lsystem.59
            lsystem.60
            lsystem.61
            lsystem.62
            lsystem.63
            lsystem.64
            lsystem.65
            lsystem.66
            lsystem.67
            lsystem.68
            lsystem.69
            lsystem.70
            lsystem.71
            lsystem.72
            lsystem.73
            lsystem.74
            lsystem.75
            lsystem.76
            lifEntry.1
            lifEntry.2
            lifEntry.3
            lifEntry.4
            lifEntry.5
            lifEntry.6
            lifEntry.7
            lifEntry.8
            lifEntry.9
            lifEntry.10
            lifEntry.11
            lifEntry.12
            lifEntry.13
            lifEntry.14
            lifEntry.15
            lifEntry.16
            lifEntry.17
            lifEntry.18
            lifEntry.19
            lifEntry.20
            lifEntry.21
            lifEntry.22
            lifEntry.23
            lifEntry.24
            lifEntry.25
            lifEntry.26
            lifEntry.27
            lifEntry.28
            lifEntry.30
            lifEntry.31
            lifEntry.32
            lifEntry.33
            lifEntry.34
            lifEntry.35
            lifEntry.36
            lifEntry.37
            lifEntry.38
            lifEntry.39
            lifEntry.40
            lifEntry.41
            lifEntry.42
            lifEntry.43
            lifEntry.44
            lifEntry.45
            lifEntry.46
            lifEntry.47
            lifEntry.48
            lifEntry.49
            lifEntry.50
            lifEntry.51
            lifEntry.52
            lifEntry.53
            lifEntry.54
            lifEntry.55
            lifEntry.56
            lifEntry.57
            lifEntry.58
            lifEntry.59
            lifEntry.60
            lifEntry.61
            lifEntry.62
            lifEntry.63
            lifEntry.64
            lifEntry.65
            lifEntry.66
            lifEntry.67
            lifEntry.68
            lifEntry.69
            lifEntry.70
            lifEntry.71
            lifEntry.72
            lifEntry.73
            lifEntry.74
            lifEntry.75
            lifEntry.76
            lifEntry.77
            lifEntry.78
            lifEntry.79
            lifEntry.80
            lifEntry.81
            lifEntry.82
            lifEntry.83
            lifEntry.84
            lifEntry.85
            lifEntry.86
            lifEntry.87
            lifEntry.88
            lifEntry.89
            lifEntry.90
            lifEntry.91
            lifEntry.92
            lifEntry.93
            lifEntry.94
            lifEntry.95
            lifEntry.96
            lifEntry.97
            lifEntry.98
            lifEntry.99
            lifEntry.100
            lifEntry.101
            lifEntry.102
            lifEntry.103
            lifEntry.104
            lifEntry.105
            lifEntry.106
            lifEntry.107
            lifEntry.108
            lifEntry.109
            lifEntry.110
            lifEntry.111
            lifEntry.112
            lifEntry.113
            lifEntry.114
            lipAddrEntry.1
            lipAddrEntry.2
            lipAddrEntry.3
            lipAddrEntry.4
            lipAddrEntry.5
            lipAddrEntry.6
            lipRouteEntry.1
            lipRouteEntry.2
            lipRouteEntry.3
            lip.4
            lip.5
            lip.6
            lipAccountEntry.1
            lipAccountEntry.2
            lipAccountEntry.3
            lipAccountEntry.4
            lipAccountEntry.5
            lip.8
            lipCkAccountEntry.1
            lipCkAccountEntry.2
            lipCkAccountEntry.3
            lipCkAccountEntry.4
            lipCkAccountEntry.5
            lip.10
            lip.11
            lip.12
            ltcpConnEntry.1
            ltcpConnEntry.2
            ltcpConnEntry.3
            ltcpConnEntry.4
            ltcpConnEntry.5
            lts.1
            ltsLineEntry.1
            ltsLineEntry.2
            ltsLineEntry.3
            ltsLineEntry.4
            ltsLineEntry.5
            ltsLineEntry.6
            ltsLineEntry.7
            ltsLineEntry.8
            ltsLineEntry.9
            ltsLineEntry.10
            ltsLineEntry.11
            ltsLineEntry.12
            ltsLineEntry.13
            ltsLineEntry.14
            ltsLineEntry.15
            ltsLineEntry.16
            ltsLineEntry.17
            ltsLineEntry.18
            ltsLineEntry.19
            ltsLineEntry.20
            ltsLineEntry.21
            ltsLineSessionEntry.1
            ltsLineSessionEntry.2
            ltsLineSessionEntry.3
            ltsLineSessionEntry.4
            ltsLineSessionEntry.5
            ltsLineSessionEntry.6
            ltsLineSessionEntry.7
            ltsLineSessionEntry.8
            lts.4
            lts.5
            lts.6
            lts.7
            lts.8
            lts.9
            lts.10
            tmpdecnet.1
            tmpdecnet.2
            tmpdecnet.3
            tmpdecnet.4
            tmpdecnet.5
            tmpdecnet.6
            tmpdecnet.7
            tmpdecnet.8
            tmpdecnet.9
            tmpdecnet.10
            tmpdecnet.11
            tmpdecnet.12
            tmpdecnet.13
            tmpdecnet.14
            tmpdecnet.15
            tmpdecnet.16
            tmpdecnet.17
            tmpdecnet.18
            tmpdecnet.19
            tmpdecnet.20
            tmpdecnet.21
            tmpdecnet.22
            tmpdecnet.23
            tmpdecnet.24
            tmpdecnet.25
            dnAreaTableEntry.1
            dnAreaTableEntry.2
            dnAreaTableEntry.3
            dnAreaTableEntry.4
            dnAreaTableEntry.5
            dnAreaTableEntry.6
            dnAreaTableEntry.7
            dnHostTableEntry.1
            dnHostTableEntry.2
            dnHostTableEntry.3
            dnHostTableEntry.4
            dnHostTableEntry.5
            dnHostTableEntry.6
            dnHostTableEntry.7
            dnIfTableEntry.1
            tmpxns.1
            tmpxns.2
            tmpxns.3
            tmpxns.4
            tmpxns.5
            tmpxns.6
            tmpxns.7
            tmpxns.8
            tmpxns.9
            tmpxns.10
            tmpxns.11
            tmpxns.12
            tmpxns.13
            tmpxns.14
            tmpxns.15
            tmpxns.16
            tmpxns.17
            tmpxns.18
            tmpxns.19
            tmpxns.20
            tmpxns.21
            tmpappletalk.1
            tmpappletalk.2
            tmpappletalk.3
            tmpappletalk.4
            tmpappletalk.5
            tmpappletalk.7
            tmpappletalk.8
            tmpappletalk.9
            tmpappletalk.10
            tmpappletalk.11
            tmpappletalk.12
            tmpappletalk.13
            tmpappletalk.14
            tmpappletalk.15
            tmpappletalk.16
            tmpappletalk.17
            tmpappletalk.18
            tmpappletalk.19
            tmpappletalk.20
            tmpappletalk.21
            tmpappletalk.22
            tmpappletalk.23
            tmpappletalk.24
            tmpappletalk.25
            tmpappletalk.26
            tmpappletalk.27
            tmpappletalk.28
            tmpappletalk.29
            tmpappletalk.30
            tmpappletalk.31
            tmpnovell.1
            tmpnovell.2
            tmpnovell.3
            tmpnovell.4
            tmpnovell.5
            tmpnovell.6
            tmpnovell.7
            tmpnovell.8
            tmpnovell.9
            tmpnovell.10
            tmpnovell.11
            tmpnovell.12
            tmpnovell.13
            tmpnovell.14
            tmpnovell.15
            tmpnovell.16
            tmpnovell.17
            tmpnovell.18
            tmpnovell.19
            tmpnovell.20
            lipxAccountingEntry.1
            lipxAccountingEntry.2
            lipxAccountingEntry.3
            lipxAccountingEntry.4
            tmpnovell.22
            lipxCkAccountingEntry.1
            lipxCkAccountingEntry.2
            lipxCkAccountingEntry.3
            lipxCkAccountingEntry.4
            tmpnovell.24
            tmpnovell.25
            tmpvines.1
            tmpvines.2
            tmpvines.3
            tmpvines.4
            tmpvines.5
            tmpvines.6
            tmpvines.7
            tmpvines.8
            tmpvines.9
            tmpvines.10
            tmpvines.11
            tmpvines.12
            tmpvines.13
            tmpvines.14
            tmpvines.15
            tmpvines.16
            tmpvines.17
            tmpvines.18
            tmpvines.19
            tmpvines.20
            tmpvines.21
            tmpvines.22
            tmpvines.23
            tmpvines.24
            tmpvines.25
            tmpvines.26
            tmpvines.27
            tmpvines.28
            vinesIfTableEntry.1
            vinesIfTableEntry.2
            vinesIfTableEntry.3
            vinesIfTableEntry.4
            vinesIfTableEntry.5
            vinesIfTableEntry.6
            vinesIfTableEntry.8
            vinesIfTableEntry.9
            vinesIfTableEntry.10
            vinesIfTableEntry.11
            vinesIfTableEntry.12
            vinesIfTableEntry.17
            vinesIfTableEntry.18
            vinesIfTableEntry.19
            vinesIfTableEntry.20
            vinesIfTableEntry.21
            vinesIfTableEntry.22
            vinesIfTableEntry.23
            vinesIfTableEntry.24
            vinesIfTableEntry.25
            vinesIfTableEntry.26
            vinesIfTableEntry.27
            vinesIfTableEntry.28
            vinesIfTableEntry.29
            vinesIfTableEntry.30
            vinesIfTableEntry.31
            vinesIfTableEntry.32
            vinesIfTableEntry.33
            vinesIfTableEntry.34
            vinesIfTableEntry.35
            vinesIfTableEntry.36
            vinesIfTableEntry.37
            vinesIfTableEntry.38
            vinesIfTableEntry.39
            vinesIfTableEntry.40
            vinesIfTableEntry.41
            vinesIfTableEntry.42
            vinesIfTableEntry.43
            vinesIfTableEntry.44
            vinesIfTableEntry.45
            vinesIfTableEntry.46
            vinesIfTableEntry.47
            vinesIfTableEntry.48
            vinesIfTableEntry.49
            vinesIfTableEntry.50
            vinesIfTableEntry.51
            vinesIfTableEntry.52
            vinesIfTableEntry.53
            vinesIfTableEntry.54
            vinesIfTableEntry.55
            vinesIfTableEntry.56
            vinesIfTableEntry.57
            vinesIfTableEntry.58
            vinesIfTableEntry.59
            vinesIfTableEntry.60
            vinesIfTableEntry.61
            vinesIfTableEntry.62
            vinesIfTableEntry.63
            vinesIfTableEntry.64
            vinesIfTableEntry.65
            vinesIfTableEntry.66
            vinesIfTableEntry.67
            vinesIfTableEntry.68
            vinesIfTableEntry.69
            vinesIfTableEntry.70
            vinesIfTableEntry.71
            vinesIfTableEntry.72
            vinesIfTableEntry.73
            vinesIfTableEntry.74
            vinesIfTableEntry.75
            vinesIfTableEntry.76
            vinesIfTableEntry.77
            vinesIfTableEntry.78
            vinesIfTableEntry.79
            vinesIfTableEntry.80
            vinesIfTableEntry.81
            vinesIfTableEntry.82
            vinesIfTableEntry.83
            chassis.1
            chassis.2
            chassis.3
            chassis.4
            chassis.5
            chassis.6
            chassis.7
            chassis.8
            chassis.9
            chassis.10
            cardTableEntry.1
            cardTableEntry.2
            cardTableEntry.3
            cardTableEntry.4
            cardTableEntry.5
            cardTableEntry.6
            cardTableEntry.7
            cardTableEntry.8
            cardTableEntry.9
            cardTableEntry.10
            chassis.12
            cardIfIndexEntry.1
            cardIfIndexEntry.2
            cardIfIndexEntry.3
            cardIfIndexEntry.4
            cardIfIndexEntry.5
            chassis.14
            chassis.15
            ciscoTcpConnEntry.1
            ciscoTcpConnEntry.2
            ciscoTcpConnEntry.3
            ciscoTcpConnEntry.4
            ciscoTcpConnEntry.5
            ciscoTcpConnEntry.6
            ciscoTcpConnEntry.7
            ciscoTcpConnEntry.8
            ciscoTcpConnEntry.9
            ciscoFlashDevice.1
            ciscoFlashDeviceEntry.2
            ciscoFlashDeviceEntry.3
            ciscoFlashDeviceEntry.4
            ciscoFlashDeviceEntry.5
            ciscoFlashDeviceEntry.6
            ciscoFlashDeviceEntry.7
            ciscoFlashDeviceEntry.8
            ciscoFlashDeviceEntry.9
            ciscoFlashDeviceEntry.10
            ciscoFlashDeviceEntry.11
            ciscoFlashDeviceEntry.12
            ciscoFlashDeviceEntry.13
            ciscoFlashDeviceEntry.14
            ciscoFlashDeviceEntry.15
            ciscoFlashDeviceEntry.16
            ciscoFlashDeviceEntry.17
            ciscoFlashChipEntry.2
            ciscoFlashChipEntry.3
            ciscoFlashChipEntry.4
            ciscoFlashChipEntry.5
            ciscoFlashChipEntry.6
            ciscoFlashChipEntry.7
            ciscoFlashPartitionEntry.2
            ciscoFlashPartitionEntry.3
            ciscoFlashPartitionEntry.4
            ciscoFlashPartitionEntry.5
            ciscoFlashPartitionEntry.6
            ciscoFlashPartitionEntry.7
            ciscoFlashPartitionEntry.8
            ciscoFlashPartitionEntry.9
            ciscoFlashPartitionEntry.10
            ciscoFlashPartitionEntry.11
            ciscoFlashPartitionEntry.12
            ciscoFlashPartitionEntry.13
            ciscoFlashPartitionEntry.14
            ciscoFlashFileEntry.2
            ciscoFlashFileEntry.3
            ciscoFlashFileEntry.4
            ciscoFlashFileEntry.5
            ciscoFlashFileEntry.6
            ciscoFlashFileEntry.7
            ciscoFlashFileByTypeEntry.1
            ciscoFlashFileByTypeEntry.2
            ciscoFlashFileByTypeEntry.3
            ciscoFlashFileByTypeEntry.4
            ciscoFlashFileByTypeEntry.5
            ciscoFlashCopyEntry.2
            ciscoFlashCopyEntry.3
            ciscoFlashCopyEntry.4
            ciscoFlashCopyEntry.5
            ciscoFlashCopyEntry.6
            ciscoFlashCopyEntry.7
            ciscoFlashCopyEntry.8
            ciscoFlashCopyEntry.9
            ciscoFlashCopyEntry.10
            ciscoFlashCopyEntry.11
            ciscoFlashCopyEntry.12
            ciscoFlashCopyEntry.13
            ciscoFlashCopyEntry.14
            ciscoFlashCopyEntry.15
            ciscoFlashPartitioningEntry.2
            ciscoFlashPartitioningEntry.3
            ciscoFlashPartitioningEntry.4
            ciscoFlashPartitioningEntry.5
            ciscoFlashPartitioningEntry.6
            ciscoFlashPartitioningEntry.7
            ciscoFlashPartitioningEntry.8
            ciscoFlashPartitioningEntry.9
            ciscoFlashMiscOpEntry.2
            ciscoFlashMiscOpEntry.3
            ciscoFlashMiscOpEntry.4
            ciscoFlashMiscOpEntry.5
            ciscoFlashMiscOpEntry.6
            ciscoFlashMiscOpEntry.7
            ciscoFlashMIB.1.4.1
            ciscoFlashMIB.1.4.2
            ciscoPingEntry.2
            ciscoPingEntry.3
            ciscoPingEntry.4
            ciscoPingEntry.5
            ciscoPingEntry.6
            ciscoPingEntry.7
            ciscoPingEntry.8
            ciscoPingEntry.9
            ciscoPingEntry.10
            ciscoPingEntry.11
            ciscoPingEntry.12
            ciscoPingEntry.13
            ciscoPingEntry.14
            ciscoPingEntry.15
            ciscoPingEntry.16
            ciscoPingEntry.17
            cvBasic.1
            cvBasic.2
            cvBasic.3
            cvForwarding.1
            cvForwarding.2
            cvForwarding.3
            cvForwNeighborEntry.4
            cvForwNeighborEntry.5
            cvForwNeighborEntry.6
            cvForwNeighborEntry.7
            cvForwNeighborEntry.8
            cvForwNeighborEntry.9
            cvForwarding.5
            cvForwarding.6
            cvForwarding.7
            cvForwarding.8
            cvForwRouteEntry.3
            cvForwRouteEntry.4
            cvForwRouteEntry.5
            cvForwRouteEntry.6
            cvForwRouteEntry.7
            cvForwRouteEntry.8
            cvForwRouteEntry.9
            cvForwRouteEntry.10
            cvForwRouteEntry.11
            cvTotal.1
            cvTotal.2
            cvTotal.3
            cvTotal.4
            cvTotal.5
            cvTotal.6
            cvTotal.7
            cvTotal.8
            cvTotal.9
            cvTotal.10
            cvTotal.11
            cvTotal.12
            cvTotal.13
            cvTotal.14
            cvTotal.15
            cvTotal.16
            cvTotal.17
            cvTotal.18
            cvTotal.19
            cvTotal.20
            cvTotal.21
            cvTotal.22
            cvTotal.23
            cvTotal.24
            cvTotal.25
            cvIfConfigEntry.1
            cvIfConfigEntry.2
            cvIfConfigEntry.3
            cvIfConfigEntry.4
            cvIfConfigEntry.5
            cvIfConfigEntry.6
            cvIfConfigEntry.7
            cvIfConfigEntry.8
            cvIfConfigEntry.9
            cvIfConfigEntry.10
            cvIfConfigEntry.11
            cvIfConfigEntry.12
            cvIfConfigEntry.13
            cvIfConfigEntry.14
            cvIfCountInEntry.1
            cvIfCountInEntry.2
            cvIfCountInEntry.3
            cvIfCountInEntry.4
            cvIfCountInEntry.5
            cvIfCountInEntry.6
            cvIfCountInEntry.7
            cvIfCountInEntry.8
            cvIfCountInEntry.9
            cvIfCountInEntry.10
            cvIfCountInEntry.11
            cvIfCountInEntry.12
            cvIfCountInEntry.13
            cvIfCountInEntry.14
            cvIfCountInEntry.15
            cvIfCountInEntry.16
            cvIfCountInEntry.17
            cvIfCountInEntry.18
            cvIfCountInEntry.19
            cvIfCountInEntry.20
            cvIfCountInEntry.21
            cvIfCountInEntry.22
            cvIfCountInEntry.23
            cvIfCountInEntry.24
            cvIfCountInEntry.25
            cvIfCountInEntry.26
            cvIfCountInEntry.27
            cvIfCountInEntry.28
            cvIfCountInEntry.29
            cvIfCountInEntry.30
            cvIfCountInEntry.31
            cvIfCountInEntry.32
            cvIfCountInEntry.33
            cvIfCountInEntry.34
            cvIfCountOutEntry.1
            cvIfCountOutEntry.2
            cvIfCountOutEntry.3
            cvIfCountOutEntry.4
            cvIfCountOutEntry.5
            cvIfCountOutEntry.6
            cvIfCountOutEntry.7
            cvIfCountOutEntry.8
            cvIfCountOutEntry.9
            cvIfCountOutEntry.10
            cvIfCountOutEntry.11
            cvIfCountOutEntry.12
            cvIfCountOutEntry.13
            cvIfCountOutEntry.14
            cvIfCountOutEntry.15
            cvIfCountOutEntry.16
            cvIfCountOutEntry.17
            cvIfCountOutEntry.18
            cvIfCountOutEntry.19
            cvIfCountOutEntry.20
            cvIfCountOutEntry.21
            cvIfCountOutEntry.22
            cvIfCountOutEntry.23
            cvIfCountOutEntry.24
            cvIfCountOutEntry.25
            cvIfCountOutEntry.26
            cvIfCountOutEntry.27
            cvIfCountOutEntry.28
            cvIfCountOutEntry.29
            cvIfCountOutEntry.30
            ciscoSnapshotMIB.1.1
            ciscoSnapshotInterfaceEntry.2
            ciscoSnapshotInterfaceEntry.3
            ciscoSnapshotInterfaceEntry.4
            ciscoSnapshotInterfaceEntry.5
            ciscoSnapshotInterfaceEntry.6
            ciscoSnapshotInterfaceEntry.7
            ciscoSnapshotInterfaceEntry.8
            ciscoSnapshotActivityEntry.2
            ciscoSnapshotActivityEntry.3
            ciscoSnapshotActivityEntry.4
            ciscoSnapshotActivityEntry.5
            ciscoSnapshotActivityEntry.6
            ciscoSnapshotActivityEntry.7
            ciscoSnapshotActivityEntry.8
            cdpInterfaceEntry.2
            cdpInterfaceEntry.3
            cdpInterfaceEntry.4
            cdpInterfaceEntry.5
            cdpInterfaceEntry.6
            cdpInterface.2.1.1
            cdpInterface.2.1.2
            cdpCacheEntry.3
            cdpCacheEntry.4
            cdpCacheEntry.5
            cdpCacheEntry.6
            cdpCacheEntry.7
            cdpCacheEntry.8
            cdpCacheEntry.9
            cdpCacheEntry.10
            cdpCacheEntry.11
            cdpCacheEntry.12
            cdpCacheEntry.13
            cdpCacheEntry.14
            cdpCacheEntry.15
            cdpCacheEntry.16
            cdpCacheEntry.17
            cdpCacheEntry.18
            cdpCacheEntry.19
            cdpCacheEntry.20
            cdpCacheEntry.21
            cdpCacheEntry.22
            cdpCacheEntry.23
            cdpCacheEntry.24
            cdpCache.2.1.4
            cdpCache.2.1.5
            cdpGlobal.1
            cdpGlobal.2
            cdpGlobal.3
            cdpGlobal.4
            cdpGlobal.5
            cdpGlobal.6
            cdpGlobal.7
            dspuNode.1
            dspuNode.2
            dspuNode.3
            dspuNode.4
            dspuNode.5
            dspuNode.6
            dspuNode.7
            dspuNode.8
            dspuNode.9
            dspuNode.10
            dspuPoolClassEntry.2
            dspuPoolClassEntry.3
            dspuPoolClassEntry.4
            dspuPoolClassEntry.5
            dspuPooledLuEntry.1
            dspuPooledLuEntry.2
            dspuPuAdminEntry.2
            dspuPuAdminEntry.3
            dspuPuAdminEntry.4
            dspuPuAdminEntry.5
            dspuPuAdminEntry.6
            dspuPuAdminEntry.7
            dspuPuAdminEntry.8
            dspuPuAdminEntry.9
            dspuPuAdminEntry.10
            dspuPuAdminEntry.11
            dspuPuAdminEntry.12
            dspuPuAdminEntry.13
            dspuPuAdminEntry.14
            dspuPuAdminEntry.15
            dspuPuAdminEntry.16
            dspuPuAdminEntry.17
            dspuPuAdminEntry.18
            dspuPuAdminEntry.19
            dspuPuOperEntry.2
            dspuPuOperEntry.3
            dspuPuOperEntry.4
            dspuPuOperEntry.5
            dspuPuOperEntry.6
            dspuPuOperEntry.7
            dspuPuOperEntry.8
            dspuPuOperEntry.9
            dspuPuOperEntry.10
            dspuPuOperEntry.11
            dspuPuOperEntry.12
            dspuPuOperEntry.13
            dspuPuOperEntry.14
            dspuPuOperEntry.15
            dspuPuOperEntry.16
            dspuPuOperEntry.17
            dspuPuOperEntry.18
            dspuPuOperEntry.19
            dspuPuOperEntry.20
            dspuPuOperEntry.21
            dspuPuOperEntry.22
            dspuPuStatsEntry.1
            dspuPuStatsEntry.2
            dspuPuStatsEntry.3
            dspuPuStatsEntry.4
            dspuPuStatsEntry.5
            dspuPuStatsEntry.6
            dspuPuStatsEntry.7
            dspuPuStatsEntry.8
            dspuPuStatsEntry.9
            dspuPuStatsEntry.10
            dspuPuStatsEntry.11
            dspuLuAdminEntry.2
            dspuLuAdminEntry.3
            dspuLuAdminEntry.4
            dspuLuAdminEntry.5
            dspuLuAdminEntry.6
            dspuLuOperEntry.2
            dspuLuOperEntry.3
            dspuLuOperEntry.4
            dspuLuOperEntry.5
            dspuLuOperEntry.6
            dspuLuOperEntry.7
            dspuLuOperEntry.8
            dspuLuOperEntry.9
            dspuSapEntry.2
            dspuSapEntry.6
            dspuSapEntry.7
            ciscoImageEntry.2
            demandNbrLogIf
            demandNbrName
            demandNbrAddress
            demandNbrPermission
            demandNbrMaxDuration
            demandNbrLastDuration
            demandNbrClearReason
            demandNbrClearCode
            demandNbrSuccessCalls
            demandNbrFailCalls
            demandNbrAcceptCalls
            demandNbrRefuseCalls
            demandNbrLastAttemptTime
            demandNbrStatus
            demandNbrCallOrigin
            ciscoCallHistory.1
            ciscoCallHistory.2
            ciscoCallHistoryEntry.3
            ciscoCallHistoryEntry.4
            ciscoCallHistoryEntry.5
            ciscoCallHistoryEntry.6
            ciscoCallHistoryEntry.7
            ciscoCallHistoryEntry.8
            ciscoCallHistoryEntry.9
            ciscoCallHistoryEntry.10
            ciscoCallHistoryEntry.11
            ciscoCallHistoryEntry.12
            ciscoCallHistoryEntry.13
            ciscoCallHistoryEntry.14
            ciscoCallHistoryEntry.15
            ciscoCallHistoryEntry.16
            ciscoCallHistoryEntry.17
            ciscoCallHistoryEntry.18
            ciscoCallHistoryEntry.19
            ciscoCallHistoryEntry.20
            ciscoCallHistoryEntry.21
            convSdllcPortEntry.1
            convSdllcPortEntry.2
            convSdllcPortEntry.3
            convSdllcPortEntry.4
            convSdllcPortEntry.5
            convSdllcPortEntry.6
            convSdllcPortEntry.7
            convSdllcAddrEntry.2
            convSdllcAddrEntry.3
            convSdllcAddrEntry.4
            convSdllcAddrEntry.5
            rsrbVirtRingEntry.2
            rsrbVirtRingEntry.3
            rsrbRemotePeerEntry.2
            rsrbRemotePeerEntry.3
            rsrbRemotePeerEntry.4
            rsrbRemotePeerEntry.5
            rsrbRemotePeerEntry.6
            rsrbRemotePeerEntry.7
            rsrbRemotePeerEntry.8
            rsrbRemotePeerEntry.9
            rsrbRemotePeerEntry.10
            rsrbRemotePeerEntry.11
            rsrbRemotePeerEntry.12
            rsrbRemotePeerEntry.13
            rsrbRemotePeerEntry.14
            rsrbRingEntry.2
            rsrbRingEntry.3
            rsrbRingEntry.4
            rsrbRingEntry.5
            rsrbRingEntry.6
            rsrbRingEntry.7
            rsrbRingEntry.8
            stunGlobal.1
            stunGroupEntry.2
            stunPortEntry.1
            stunPortEntry.2
            stunPortEntry.3
            stunPortEntry.4
            stunRouteEntry.2
            stunRouteEntry.3
            stunRouteEntry.4
            stunRouteEntry.5
            stunRouteEntry.6
            stunRouteEntry.7
            stunRouteEntry.8
            stunRouteEntry.9
            stunRouteEntry.10
            stunRouteEntry.11
            bstunGlobal.1
            bstunGlobal.2
            bstunGlobal.3
            bstunGlobal.4
            bstunGroupEntry.2
            bstunGroupEntry.3
            bstunGroupEntry.4
            bstunGroupEntry.5
            bstunPortEntry.1
            bstunPortEntry.2
            bstunPortEntry.3
            bstunPortEntry.4
            bstunRouteEntry.3
            bstunRouteEntry.4
            bstunRouteEntry.5
            bstunRouteEntry.6
            bstunRouteEntry.7
            bstunRouteEntry.8
            bstunRouteEntry.9
            bstunRouteEntry.10
            bstunRouteEntry.11
            bstunRouteEntry.12
            bstunRouteEntry.13
            bstunRouteEntry.14
            bscPortEntry.1
            bscPortEntry.2
            bscPortEntry.3
            bscPortEntry.4
            bscPortEntry.5
            bscPortEntry.6
            bscPortEntry.7
            bscPortEntry.8
            bscPortEntry.9
            bscPortEntry.10
            bscPortEntry.11
            bscPortEntry.12
            bscPortEntry.13
            bscPortEntry.14
            bscCUEntry.2
            bscCUEntry.3
            bscCUEntry.4
            bscCUEntry.5
            bscCUEntry.6
            bscCUEntry.7
            bscCUEntry.8
            bscCUEntry.9
            bscCUEntry.10
            bscCUEntry.11
            bscExtAddressEntry.2
            cQIfEntry.1
            cQIfEntry.2
            cQIfEntry.3
            cQStatsEntry.2
            cQStatsEntry.3
            cQStatsEntry.4
            cQRotationEntry.1
            clogBasic.1
            clogBasic.2
            clogBasic.3
            clogBasic.4
            clogBasic.5
            ciscoSyslogMIB.1.2.1
            ciscoSyslogMIB.1.2.2
            clogHistoryEntry.2
            clogHistoryEntry.3
            clogHistoryEntry.4
            clogHistoryEntry.5
            clogHistoryEntry.6
            rttMonApplVersion
            rttMonApplMaxPacketDataSize
            rttMonApplTimeOfLastSet
            rttMonApplNumCtrlAdminEntry
            rttMonApplReset
            rttMonApplPreConfigedReset
            rttMonApplSupportedRttTypesValid
            rttMonApplSupportedProtocolsValid
            rttMonApplPreConfigedValid
            rttMonApplProbeCapacity
            rttMonApplFreeMemLowWaterMark
            rttMonApplLatestSetError
            rttMonApplResponder
            rttMonApplAuthKeyChain
            rttMonApplAuthKeyString1
            rttMonApplAuthKeyString2
            rttMonApplAuthKeyString3
            rttMonApplAuthKeyString4
            rttMonApplAuthKeyString5
            rttMonApplAuthStatus
            rttMonApplLpdGrpStatsReset
            rttMonCtrlAdminOwner
            rttMonCtrlAdminTag
            rttMonCtrlAdminRttType
            rttMonCtrlAdminThreshold
            rttMonCtrlAdminFrequency
            rttMonCtrlAdminTimeout
            rttMonCtrlAdminVerifyData
            rttMonCtrlAdminStatus
            rttMonCtrlAdminNvgen
            rttMonCtrlAdminGroupName
            rttMonCtrlAdminLongTag
            rttMonEchoAdminProtocol
            rttMonEchoAdminTargetAddress
            rttMonEchoAdminPktDataRequestSize
            rttMonEchoAdminPktDataResponseSize
            rttMonEchoAdminTargetPort
            rttMonEchoAdminSourceAddress
            rttMonEchoAdminSourcePort
            rttMonEchoAdminControlEnable
            rttMonEchoAdminTOS
            rttMonEchoAdminLSREnable
            rttMonEchoAdminTargetAddressString
            rttMonEchoAdminNameServer
            rttMonEchoAdminOperation
            rttMonEchoAdminHTTPVersion
            rttMonEchoAdminURL
            rttMonEchoAdminCache
            rttMonEchoAdminInterval
            rttMonEchoAdminNumPackets
            rttMonEchoAdminProxy
            rttMonEchoAdminString1
            rttMonEchoAdminString2
            rttMonEchoAdminString3
            rttMonEchoAdminString4
            rttMonEchoAdminString5
            rttMonEchoAdminMode
            rttMonEchoAdminVrfName
            rttMonEchoAdminCodecType
            rttMonEchoAdminCodecInterval
            rttMonEchoAdminCodecPayload
            rttMonEchoAdminCodecNumPackets
            rttMonEchoAdminICPIFAdvFactor
            rttMonEchoAdminLSPFECType
            rttMonEchoAdminLSPSelector
            rttMonEchoAdminLSPReplyMode
            rttMonEchoAdminLSPTTL
            rttMonEchoAdminLSPExp
            rttMonEchoAdminPrecision
            rttMonEchoAdminProbePakPriority
            rttMonEchoAdminOWNTPSyncTolAbs
            rttMonEchoAdminOWNTPSyncTolPct
            rttMonEchoAdminOWNTPSyncTolType
            rttMonEchoAdminCalledNumber
            rttMonEchoAdminDetectPoint
            rttMonEchoAdminGKRegistration
            rttMonEchoAdminSourceVoicePort
            rttMonEchoAdminCallDuration
            rttMonEchoAdminLSPReplyDscp
            rttMonEchoAdminLSPNullShim
            rttMonEchoAdminTargetMPID
            rttMonEchoAdminTargetDomainName
            rttMonEchoAdminTargetVLAN
            rttMonEchoAdminEthernetCOS
            rttMonEchoAdminLSPVccvID
            rttMonEchoAdminTargetEVC
            rttMonEchoAdminTargetMEPPort
            rttMonEchoAdminVideoTrafficProfile
            rttMonEchoAdminDscp
            rttMonEchoAdminReserveDsp
            rttMonEchoAdminInputInterface
            rttMonEchoAdminEmulateSourceAddress
            rttMonEchoAdminEmulateSourcePort
            rttMonEchoAdminEmulateTargetAddress
            rttMonEchoAdminEmulateTargetPort
            rttMonEchoAdminTargetMacAddress
            rttMonEchoAdminSourceMacAddress
            rttMonEchoAdminSourceMPID
            rttMonEchoAdminEndPointListName
            rttMonEchoAdminSSM
            rttMonEchoAdminControlRetry
            rttMonEchoAdminControlTimeout
            rttMonEchoAdminIgmpTreeInit
            rttMonEchoAdminEnableBurst
            rttMonEchoAdminAggBurstCycles
            rttMonEchoAdminLossRatioNumFrames
            rttMonEchoAdminAvailNumFrames
            rttMonEchoAdminTstampOptimization
            rttMonEchoAdminEntry.77
            rttMonEchoAdminEntry.78
            rttMonEchoAdminEntry.79
            rttMonFileIOAdminFilePath
            rttMonFileIOAdminSize
            rttMonFileIOAdminAction
            rttMonScriptAdminName
            rttMonScriptAdminCmdLineParams
            rttMonScheduleAdminRttLife
            rttMonScheduleAdminRttStartTime
            rttMonScheduleAdminConceptRowAgeout
            rttMonScheduleAdminRttRecurring
            rttMonScheduleAdminConceptRowAgeoutV2
            rttMonScheduleAdminStartType
            rttMonScheduleAdminStartDelay
            rttMonReactAdminConnectionEnable
            rttMonReactAdminTimeoutEnable
            rttMonReactAdminThresholdType
            rttMonReactAdminThresholdFalling
            rttMonReactAdminThresholdCount
            rttMonReactAdminThresholdCount2
            rttMonReactAdminActionType
            rttMonReactAdminVerifyErrorEnable
            rttMonStatisticsAdminNumHourGroups
            rttMonStatisticsAdminNumPaths
            rttMonStatisticsAdminNumHops
            rttMonStatisticsAdminNumDistBuckets
            rttMonStatisticsAdminDistInterval
            rttMonHistoryAdminNumLives
            rttMonHistoryAdminNumBuckets
            rttMonHistoryAdminNumSamples
            rttMonHistoryAdminFilter
            rttMonCtrlOperModificationTime
            rttMonCtrlOperDiagText
            rttMonCtrlOperResetTime
            rttMonCtrlOperOctetsInUse
            rttMonCtrlOperConnectionLostOccurred
            rttMonCtrlOperTimeoutOccurred
            rttMonCtrlOperOverThresholdOccurred
            rttMonCtrlOperNumRtts
            rttMonCtrlOperRttLife
            rttMonCtrlOperState
            rttMonCtrlOperVerifyErrorOccurred
            rttMonLatestRttOperCompletionTime
            rttMonLatestRttOperSense
            rttMonLatestRttOperApplSpecificSense
            rttMonLatestRttOperSenseDescription
            rttMonLatestRttOperTime
            rttMonLatestRttOperAddress
            rttMonReactTriggerAdminStatus
            rttMonReactTriggerOperState
            rttMonEchoPathAdminHopAddress
            rttMonGrpScheduleAdminProbes
            rttMonGrpScheduleAdminPeriod
            rttMonGrpScheduleAdminFrequency
            rttMonGrpScheduleAdminLife
            rttMonGrpScheduleAdminAgeout
            rttMonGrpScheduleAdminStatus
            rttMonGrpScheduleAdminFreqMax
            rttMonGrpScheduleAdminFreqMin
            rttMonGrpScheduleAdminStartTime
            rttMonGrpScheduleAdminAdd
            rttMonGrpScheduleAdminDelete
            rttMonGrpScheduleAdminReset
            rttMonGrpScheduleAdminStartType
            rttMonGrpScheduleAdminStartDelay
            rttMplsVpnMonCtrlRttType
            rttMplsVpnMonCtrlVrfName
            rttMplsVpnMonCtrlTag
            rttMplsVpnMonCtrlThreshold
            rttMplsVpnMonCtrlTimeout
            rttMplsVpnMonCtrlScanInterval
            rttMplsVpnMonCtrlDelScanFactor
            rttMplsVpnMonCtrlEXP
            rttMplsVpnMonCtrlRequestSize
            rttMplsVpnMonCtrlVerifyData
            rttMplsVpnMonCtrlStorageType
            rttMplsVpnMonCtrlProbeList
            rttMplsVpnMonCtrlStatus
            rttMplsVpnMonCtrlLpd
            rttMplsVpnMonCtrlLpdGrpList
            rttMplsVpnMonCtrlLpdCompTime
            rttMplsVpnMonTypeInterval
            rttMplsVpnMonTypeNumPackets
            rttMplsVpnMonTypeDestPort
            rttMplsVpnMonTypeSecFreqType
            rttMplsVpnMonTypeSecFreqValue
            rttMplsVpnMonTypeLspSelector
            rttMplsVpnMonTypeLSPReplyMode
            rttMplsVpnMonTypeLSPTTL
            rttMplsVpnMonTypeLSPReplyDscp
            rttMplsVpnMonTypeLpdMaxSessions
            rttMplsVpnMonTypeLpdSessTimeout
            rttMplsVpnMonTypeLpdEchoTimeout
            rttMplsVpnMonTypeLpdEchoInterval
            rttMplsVpnMonTypeLpdEchoNullShim
            rttMplsVpnMonTypeLpdScanPeriod
            rttMplsVpnMonTypeLpdStatHours
            rttMplsVpnMonScheduleRttStartTime
            rttMplsVpnMonSchedulePeriod
            rttMplsVpnMonScheduleFrequency
            rttMplsVpnMonReactConnectionEnable
            rttMplsVpnMonReactTimeoutEnable
            rttMplsVpnMonReactThresholdType
            rttMplsVpnMonReactThresholdCount
            rttMplsVpnMonReactActionType
            rttMplsVpnMonReactLpdNotifyType
            rttMplsVpnMonReactLpdRetryCount
            rttMonReactVar
            rttMonReactThresholdType
            rttMonReactActionType
            rttMonReactThresholdRising
            rttMonReactThresholdFalling
            rttMonReactThresholdCountX
            rttMonReactThresholdCountY
            rttMonReactValue
            rttMonReactOccurred
            rttMonReactStatus
            rttMonGeneratedOperCtrlAdminIndex
            rttMonStatsCaptureCompletions
            rttMonStatsCaptureOverThresholds
            rttMonStatsCaptureSumCompletionTime
            rttMonStatsCaptureSumCompletionTime2Low
            rttMonStatsCaptureSumCompletionTime2High
            rttMonStatsCaptureCompletionTimeMax
            rttMonStatsCaptureCompletionTimeMin
            rttMonStatsCollectNumDisconnects
            rttMonStatsCollectTimeouts
            rttMonStatsCollectBusies
            rttMonStatsCollectNoConnections
            rttMonStatsCollectDrops
            rttMonStatsCollectSequenceErrors
            rttMonStatsCollectVerifyErrors
            rttMonStatsCollectAddress
            rttMonControlEnableErrors
            rttMonStatsRetrieveErrors
            rttMonStatsCollectCtrlEnErrors
            rttMonStatsCollectRetrieveErrors
            rttMonStatsTotalsElapsedTime
            rttMonStatsTotalsInitiations
            rttMonHTTPStatsCompletions
            rttMonHTTPStatsOverThresholds
            rttMonHTTPStatsRTTSum
            rttMonHTTPStatsRTTSum2Low
            rttMonHTTPStatsRTTSum2High
            rttMonHTTPStatsRTTMin
            rttMonHTTPStatsRTTMax
            rttMonHTTPStatsDNSRTTSum
            rttMonHTTPStatsTCPConnectRTTSum
            rttMonHTTPStatsTransactionRTTSum
            rttMonHTTPStatsMessageBodyOctetsSum
            rttMonHTTPStatsDNSServerTimeout
            rttMonHTTPStatsTCPConnectTimeout
            rttMonHTTPStatsTransactionTimeout
            rttMonHTTPStatsDNSQueryError
            rttMonHTTPStatsHTTPError
            rttMonHTTPStatsError
            rttMonHTTPStatsBusies
            rttMonJitterStatsCompletions
            rttMonJitterStatsOverThresholds
            rttMonJitterStatsNumOfRTT
            rttMonJitterStatsRTTSum
            rttMonJitterStatsRTTSum2Low
            rttMonJitterStatsRTTSum2High
            rttMonJitterStatsRTTMin
            rttMonJitterStatsRTTMax
            rttMonJitterStatsMinOfPositivesSD
            rttMonJitterStatsMaxOfPositivesSD
            rttMonJitterStatsNumOfPositivesSD
            rttMonJitterStatsSumOfPositivesSD
            rttMonJitterStatsSum2PositivesSDLow
            rttMonJitterStatsSum2PositivesSDHigh
            rttMonJitterStatsMinOfNegativesSD
            rttMonJitterStatsMaxOfNegativesSD
            rttMonJitterStatsNumOfNegativesSD
            rttMonJitterStatsSumOfNegativesSD
            rttMonJitterStatsSum2NegativesSDLow
            rttMonJitterStatsSum2NegativesSDHigh
            rttMonJitterStatsMinOfPositivesDS
            rttMonJitterStatsMaxOfPositivesDS
            rttMonJitterStatsNumOfPositivesDS
            rttMonJitterStatsSumOfPositivesDS
            rttMonJitterStatsSum2PositivesDSLow
            rttMonJitterStatsSum2PositivesDSHigh
            rttMonJitterStatsMinOfNegativesDS
            rttMonJitterStatsMaxOfNegativesDS
            rttMonJitterStatsNumOfNegativesDS
            rttMonJitterStatsSumOfNegativesDS
            rttMonJitterStatsSum2NegativesDSLow
            rttMonJitterStatsSum2NegativesDSHigh
            rttMonJitterStatsPacketLossSD
            rttMonJitterStatsPacketLossDS
            rttMonJitterStatsPacketOutOfSequence
            rttMonJitterStatsPacketMIA
            rttMonJitterStatsPacketLateArrival
            rttMonJitterStatsError
            rttMonJitterStatsBusies
            rttMonJitterStatsOWSumSD
            rttMonJitterStatsOWSum2SDLow
            rttMonJitterStatsOWSum2SDHigh
            rttMonJitterStatsOWMinSD
            rttMonJitterStatsOWMaxSD
            rttMonJitterStatsOWSumDS
            rttMonJitterStatsOWSum2DSLow
            rttMonJitterStatsOWSum2DSHigh
            rttMonJitterStatsOWMinDS
            rttMonJitterStatsOWMaxDS
            rttMonJitterStatsNumOfOW
            rttMonJitterStatsOWMinSDNew
            rttMonJitterStatsOWMaxSDNew
            rttMonJitterStatsOWMinDSNew
            rttMonJitterStatsOWMaxDSNew
            rttMonJitterStatsMinOfMOS
            rttMonJitterStatsMaxOfMOS
            rttMonJitterStatsMinOfICPIF
            rttMonJitterStatsMaxOfICPIF
            rttMonJitterStatsIAJOut
            rttMonJitterStatsIAJIn
            rttMonJitterStatsAvgJitter
            rttMonJitterStatsAvgJitterSD
            rttMonJitterStatsAvgJitterDS
            rttMonJitterStatsUnSyncRTs
            rttMonJitterStatsRTTSumHigh
            rttMonJitterStatsOWSumSDHigh
            rttMonJitterStatsOWSumDSHigh
            rttMonJitterStatsNumOverThresh
            rttMonRtpStatsRTTAvg
            rttMonRtpStatsRTTMin
            rttMonRtpStatsRTTMax
            rttMonRtpStatsIAJitterDSAvg
            rttMonRtpStatsIAJitterDSMin
            rttMonRtpStatsIAJitterDSMax
            rttMonRtpStatsPacketLossDSAvg
            rttMonRtpStatsPacketLossDSMin
            rttMonRtpStatsPacketLossDSMax
            rttMonRtpStatsPacketLateDSAvg
            rttMonRtpStatsPacketEarlyDSAvg
            rttMonRtpStatsPacketOOSDSAvg
            rttMonRtpStatsFrameLossDSAvg
            rttMonRtpStatsFrameLossDSMin
            rttMonRtpStatsFrameLossDSMax
            rttMonRtpStatsRFactorDSAvg
            rttMonRtpStatsRFactorDSMin
            rttMonRtpStatsRFactorDSMax
            rttMonRtpStatsMOSCQDSAvg
            rttMonRtpStatsMOSCQDSMin
            rttMonRtpStatsMOSCQDSMax
            rttMonRtpStatsMOSLQDSAvg
            rttMonRtpStatsMOSLQDSMin
            rttMonRtpStatsMOSLQDSMax
            rttMonRtpStatsIAJitterSDAvg
            rttMonRtpStatsIAJitterSDMin
            rttMonRtpStatsIAJitterSDMax
            rttMonRtpStatsPacketLossSDAvg
            rttMonRtpStatsPacketLossSDMin
            rttMonRtpStatsPacketLossSDMax
            rttMonRtpStatsPacketsMIAAvg
            rttMonRtpStatsRFactorSDAvg
            rttMonRtpStatsRFactorSDMin
            rttMonRtpStatsRFactorSDMax
            rttMonRtpStatsMOSCQSDAvg
            rttMonRtpStatsMOSCQSDMin
            rttMonRtpStatsMOSCQSDMax
            rttMonRtpStatsOperAvgOWSD
            rttMonRtpStatsOperMinOWSD
            rttMonRtpStatsOperMaxOWSD
            rttMonRtpStatsOperAvgOWDS
            rttMonRtpStatsOperMinOWDS
            rttMonRtpStatsOperMaxOWDS
            rttMonRtpStatsTotalPacketsSDAvg
            rttMonRtpStatsTotalPacketsSDMin
            rttMonRtpStatsTotalPacketsSDMax
            rttMonRtpStatsTotalPacketsDSAvg
            rttMonRtpStatsTotalPacketsDSMax
            rttMonRtpStatsTotalPacketsDSMin
            rttMonLpdGrpStatsTargetPE
            rttMonLpdGrpStatsNumOfPass
            rttMonLpdGrpStatsNumOfFail
            rttMonLpdGrpStatsNumOfTimeout
            rttMonLpdGrpStatsAvgRTT
            rttMonLpdGrpStatsMinRTT
            rttMonLpdGrpStatsMaxRTT
            rttMonLpdGrpStatsMinNumPaths
            rttMonLpdGrpStatsMaxNumPaths
            rttMonLpdGrpStatsLPDStartTime
            rttMonLpdGrpStatsLPDFailOccurred
            rttMonLpdGrpStatsLPDFailCause
            rttMonLpdGrpStatsLPDCompTime
            rttMonLpdGrpStatsGroupStatus
            rttMonLpdGrpStatsGroupProbeIndex
            rttMonLpdGrpStatsPathIds
            rttMonLpdGrpStatsProbeStatus
            rttMonLpdGrpStatsResetTime
            rttMonIcmpJitterStatsCompletions
            rttMonIcmpJStatsOverThresholds
            rttMonIcmpJitterStatsNumRTTs
            rttMonIcmpJitterStatsRTTSums
            rttMonIcmpJStatsRTTSum2Lows
            rttMonIcmpJStatsRTTSum2Highs
            rttMonIcmpJitterStatsRTTMin
            rttMonIcmpJitterStatsRTTMax
            rttMonIcmpJitterStatsMinPosSD
            rttMonIcmpJitterStatsMaxPosSD
            rttMonIcmpJitterStatsNumPosSDs
            rttMonIcmpJitterStatsSumPosSDs
            rttMonIcmpJStatsSum2PosSDLows
            rttMonIcmpJStatsSum2PosSDHighs
            rttMonIcmpJitterStatsMinNegSD
            rttMonIcmpJitterStatsMaxNegSD
            rttMonIcmpJitterStatsNumNegSDs
            rttMonIcmpJitterStatsSumNegSDs
            rttMonIcmpJStatsSum2NegSDLows
            rttMonIcmpJStatsSum2NegSDHighs
            rttMonIcmpJitterStatsMinPosDS
            rttMonIcmpJitterStatsMaxPosDS
            rttMonIcmpJitterStatsNumPosDSes
            rttMonIcmpJitterStatsSumPosDSes
            rttMonIcmpJStatsSum2PosDSLows
            rttMonIcmpJStatsSum2PosDSHighs
            rttMonIcmpJitterStatsMinNegDS
            rttMonIcmpJitterStatsMaxNegDS
            rttMonIcmpJitterStatsNumNegDSes
            rttMonIcmpJitterStatsSumNegDSes
            rttMonIcmpJStatsSum2NegDSLows
            rttMonIcmpJStatsSum2NegDSHighs
            rttMonIcmpJitterStatsPktLosses
            rttMonIcmpJStatsPktOutSeqBoth
            rttMonIcmpJStatsPktOutSeqSDs
            rttMonIcmpJStatsPktOutSeqDSes
            rttMonIcmpJitterStatsPktSkippeds
            rttMonIcmpJitterStatsErrors
            rttMonIcmpJitterStatsBusies
            rttMonIcmpJitterStatsOWSumSDs
            rttMonIcmpJStatsOWSum2SDLows
            rttMonIcmpJStatsOWSum2SDHighs
            rttMonIcmpJitterStatsOWMinSD
            rttMonIcmpJitterStatsOWMaxSD
            rttMonIcmpJitterStatsOWSumDSes
            rttMonIcmpJStatsOWSum2DSLows
            rttMonIcmpJStatsOWSum2DSHighs
            rttMonIcmpJitterStatsOWMinDS
            rttMonIcmpJitterStatsOWMaxDS
            rttMonIcmpJitterStatsNumOWs
            rttMonIcmpJitterStatsAvgJ
            rttMonIcmpJitterStatsAvgJSD
            rttMonIcmpJitterStatsAvgJDS
            rttMonIcmpJitterMinSucPktLoss
            rttMonIcmpJitterMaxSucPktLoss
            rttMonIcmpJitterStatsIAJOut
            rttMonIcmpJitterStatsIAJIn
            rttMonIcmpJitterStatsPktLateAs
            rttMonIcmpJitterStatsNumOverThresh
            rttMonHistoryCollectionSampleTime
            rttMonHistoryCollectionAddress
            rttMonHistoryCollectionCompletionTime
            rttMonHistoryCollectionSense
            rttMonHistoryCollectionApplSpecificSense
            rttMonHistoryCollectionSenseDescription
            rttMonLatestHTTPOperRTT
            rttMonLatestHTTPOperDNSRTT
            rttMonLatestHTTPOperTCPConnectRTT
            rttMonLatestHTTPOperTransactionRTT
            rttMonLatestHTTPOperMessageBodyOctets
            rttMonLatestHTTPOperSense
            rttMonLatestHTTPErrorSenseDescription
            rttMonLatestJitterOperNumOfRTT
            rttMonLatestJitterOperRTTSum
            rttMonLatestJitterOperRTTSum2
            rttMonLatestJitterOperRTTMin
            rttMonLatestJitterOperRTTMax
            rttMonLatestJitterOperMinOfPositivesSD
            rttMonLatestJitterOperMaxOfPositivesSD
            rttMonLatestJitterOperNumOfPositivesSD
            rttMonLatestJitterOperSumOfPositivesSD
            rttMonLatestJitterOperSum2PositivesSD
            rttMonLatestJitterOperMinOfNegativesSD
            rttMonLatestJitterOperMaxOfNegativesSD
            rttMonLatestJitterOperNumOfNegativesSD
            rttMonLatestJitterOperSumOfNegativesSD
            rttMonLatestJitterOperSum2NegativesSD
            rttMonLatestJitterOperMinOfPositivesDS
            rttMonLatestJitterOperMaxOfPositivesDS
            rttMonLatestJitterOperNumOfPositivesDS
            rttMonLatestJitterOperSumOfPositivesDS
            rttMonLatestJitterOperSum2PositivesDS
            rttMonLatestJitterOperMinOfNegativesDS
            rttMonLatestJitterOperMaxOfNegativesDS
            rttMonLatestJitterOperNumOfNegativesDS
            rttMonLatestJitterOperSumOfNegativesDS
            rttMonLatestJitterOperSum2NegativesDS
            rttMonLatestJitterOperPacketLossSD
            rttMonLatestJitterOperPacketLossDS
            rttMonLatestJitterOperPacketOutOfSequence
            rttMonLatestJitterOperPacketMIA
            rttMonLatestJitterOperPacketLateArrival
            rttMonLatestJitterOperSense
            rttMonLatestJitterErrorSenseDescription
            rttMonLatestJitterOperOWSumSD
            rttMonLatestJitterOperOWSum2SD
            rttMonLatestJitterOperOWMinSD
            rttMonLatestJitterOperOWMaxSD
            rttMonLatestJitterOperOWSumDS
            rttMonLatestJitterOperOWSum2DS
            rttMonLatestJitterOperOWMinDS
            rttMonLatestJitterOperOWMaxDS
            rttMonLatestJitterOperNumOfOW
            rttMonLatestJitterOperMOS
            rttMonLatestJitterOperICPIF
            rttMonLatestJitterOperIAJOut
            rttMonLatestJitterOperIAJIn
            rttMonLatestJitterOperAvgJitter
            rttMonLatestJitterOperAvgSDJ
            rttMonLatestJitterOperAvgDSJ
            rttMonLatestJitterOperOWAvgSD
            rttMonLatestJitterOperOWAvgDS
            rttMonLatestJitterOperNTPState
            rttMonLatestJitterOperUnSyncRTs
            rttMonLatestJitterOperRTTSumHigh
            rttMonLatestJitterOperRTTSum2High
            rttMonLatestJitterOperOWSumSDHigh
            rttMonLatestJitterOperOWSum2SDHigh
            rttMonLatestJitterOperOWSumDSHigh
            rttMonLatestJitterOperOWSum2DSHigh
            rttMonLatestJitterOperNumOverThresh
            rttMonLatestRtpOperRTT
            rttMonLatestRtpOperIAJitterDS
            rttMonLatestRtpOperPacketLossDS
            rttMonLatestRtpOperPacketLateDS
            rttMonLatestRtpOperPacketEarlyDS
            rttMonLatestRtpOperPacketOOSDS
            rttMonLatestRtpOperFrameLossDS
            rttMonLatestRtpOperRFactorDS
            rttMonLatestRtpOperMOSCQDS
            rttMonLatestRtpOperMOSLQDS
            rttMonLatestRtpOperSense
            rttMonLatestRtpErrorSenseDescription
            rttMonLatestRtpOperIAJitterSD
            rttMonLatestRtpOperPacketLossSD
            rttMonLatestRtpOperPacketsMIA
            rttMonLatestRtpOperRFactorSD
            rttMonLatestRtpOperMOSCQSD
            rttMonLatestRtpOperMinOWSD
            rttMonLatestRtpOperMaxOWSD
            rttMonLatestRtpOperAvgOWSD
            rttMonLatestRtpOperMinOWDS
            rttMonLatestRtpOperMaxOWDS
            rttMonLatestRtpOperAvgOWDS
            rttMonLatestRtpOperTotalPaksSD
            rttMonLatestRtpOperTotalPaksDS
            rttMonLatestIcmpJitterNumRTT
            rttMonLatestIcmpJitterRTTSum
            rttMonLatestIcmpJitterRTTSum2
            rttMonLatestIcmpJitterRTTMin
            rttMonLatestIcmpJitterRTTMax
            rttMonLatestIcmpJitterMinPosSD
            rttMonLatestIcmpJitterMaxPosSD
            rttMonLatestIcmpJitterNumPosSD
            rttMonLatestIcmpJitterSumPosSD
            rttMonLatestIcmpJitterSum2PosSD
            rttMonLatestIcmpJitterMinNegSD
            rttMonLatestIcmpJitterMaxNegSD
            rttMonLatestIcmpJitterNumNegSD
            rttMonLatestIcmpJitterSumNegSD
            rttMonLatestIcmpJitterSum2NegSD
            rttMonLatestIcmpJitterMinPosDS
            rttMonLatestIcmpJitterMaxPosDS
            rttMonLatestIcmpJitterNumPosDS
            rttMonLatestIcmpJitterSumPosDS
            rttMonLatestIcmpJitterSum2PosDS
            rttMonLatestIcmpJitterMinNegDS
            rttMonLatestIcmpJitterMaxNegDS
            rttMonLatestIcmpJitterNumNegDS
            rttMonLatestIcmpJitterSumNegDS
            rttMonLatestIcmpJitterSum2NegDS
            rttMonLatestIcmpJitterPktLoss
            rttMonLatestIcmpJPktOutSeqBoth
            rttMonLatestIcmpJPktOutSeqSD
            rttMonLatestIcmpJPktOutSeqDS
            rttMonLatestIcmpJitterPktSkipped
            rttMonLatestIcmpJitterSense
            rttMonLatestIcmpJitterPktLateA
            rttMonLatestIcmpJitterMinSucPktL
            rttMonLatestIcmpJitterMaxSucPktL
            rttMonLatestIcmpJitterOWSumSD
            rttMonLatestIcmpJitterOWSum2SD
            rttMonLatestIcmpJitterOWMinSD
            rttMonLatestIcmpJitterOWMaxSD
            rttMonLatestIcmpJitterOWSumDS
            rttMonLatestIcmpJitterOWSum2DS
            rttMonLatestIcmpJitterOWMinDS
            rttMonLatestIcmpJitterOWMaxDS
            rttMonLatestIcmpJitterNumOW
            rttMonLatestIcmpJitterAvgJitter
            rttMonLatestIcmpJitterAvgSDJ
            rttMonLatestIcmpJitterAvgDSJ
            rttMonLatestIcmpJitterOWAvgSD
            rttMonLatestIcmpJitterOWAvgDS
            rttMonLatestIcmpJitterIAJOut
            rttMonLatestIcmpJitterIAJIn
            rttMonLatestIcmpJitterNumOverThresh
            ccmHistoryRunningLastChanged
            ccmHistoryRunningLastSaved
            ccmHistoryStartupLastChanged
            ccmHistoryMaxEventEntries
            ccmHistoryEventEntriesBumped
            ccmHistoryEventTime
            ccmHistoryEventCommandSource
            ccmHistoryEventConfigSource
            ccmHistoryEventConfigDestination
            ccmHistoryEventTerminalType
            ccmHistoryEventTerminalNumber
            ccmHistoryEventTerminalUser
            ccmHistoryEventTerminalLocation
            ccmHistoryEventCommandSourceAddress
            ccmHistoryEventVirtualHostName
            ccmHistoryEventServerAddress
            ccmHistoryEventFile
            ccmHistoryEventRcpUser
            ccmHistoryCLICmdEntriesBumped
            ccmHistoryEventCommandSourceAddrType
            ccmHistoryEventCommandSourceAddrRev1
            ccmHistoryEventServerAddrType
            ccmHistoryEventServerAddrRev1
            ccmCLIHistoryMaxCmdEntries
            ccmCLIHistoryCmdEntries
            ccmCLIHistoryCmdEntriesAllowed
            ccmCLIHistoryCommand
            ccmCLICfgRunConfNotifEnable
            ccmCTID
            ccmCTIDLastChangeTime
            ccmCTIDWhoChanged
            ccmCTIDRolledOverNotifEnable
            ciscoMemoryPoolEntry.2
            ciscoMemoryPoolEntry.3
            ciscoMemoryPoolEntry.4
            ciscoMemoryPoolEntry.5
            ciscoMemoryPoolEntry.6
            ciscoMemoryPoolEntry.7
            cfrLmiEntry.1
            cfrLmiEntry.2
            cfrLmiEntry.3
            cfrLmiEntry.4
            cfrLmiEntry.5
            cfrLmiEntry.6
            cfrLmiEntry.7
            cfrLmiEntry.8
            cfrLmiEntry.9
            cfrLmiEntry.10
            cfrLmiEntry.11
            cfrLmiEntry.12
            cfrLmiEntry.13
            cfrCircuitEntry.1
            cfrCircuitEntry.2
            cfrCircuitEntry.3
            cfrCircuitEntry.4
            cfrExtCircuitEntry.1
            cfrExtCircuitEntry.2
            cfrExtCircuitEntry.3
            cfrExtCircuitEntry.4
            cfrExtCircuitEntry.5
            cfrExtCircuitEntry.6
            cfrExtCircuitEntry.7
            cfrExtCircuitEntry.8
            cfrExtCircuitEntry.9
            cfrExtCircuitEntry.10
            cfrExtCircuitEntry.11
            cfrExtCircuitEntry.12
            cfrExtCircuitEntry.13
            cfrExtCircuitEntry.14
            cfrExtCircuitEntry.15
            cfrExtCircuitEntry.16
            cfrExtCircuitEntry.17
            cfrExtCircuitEntry.18
            cfrExtCircuitEntry.19
            cfrExtCircuitEntry.20
            cfrExtCircuitEntry.21
            cfrExtCircuitEntry.22
            cfrExtCircuitEntry.23
            cfrExtCircuitEntry.24
            cfrExtCircuitEntry.25
            cfrExtCircuitEntry.26
            cfrExtCircuitEntry.27
            cfrExtCircuitEntry.28
            cfrExtCircuitEntry.29
            cfrExtCircuitEntry.30
            cfrMapEntry.1
            cfrMapEntry.2
            cfrMapEntry.3
            cfrMapEntry.4
            cfrMapEntry.5
            cfrMapEntry.6
            cfrMapEntry.7
            cfrMapEntry.8
            cfrMapEntry.9
            cfrMapEntry.10
            cfrSvcEntry.1
            cfrSvcEntry.2
            cfrSvcEntry.3
            cfrSvcEntry.4
            cfrSvcEntry.5
            cfrSvcEntry.6
            cfrSvcEntry.7
            cfrSvcEntry.8
            cfrElmiObjs.1
            cfrElmiEntry.1
            cfrElmiEntry.2
            cfrElmiEntry.3
            cfrElmiNeighborEntry.1
            cfrElmiNeighborEntry.2
            cfrElmiNeighborEntry.3
            cfrElmiNeighborEntry.4
            cfrElmiNeighborEntry.5
            cfrElmiNeighborEntry.6
            cfrFragEntry.1
            cfrFragEntry.2
            cfrFragEntry.3
            cfrFragEntry.4
            cfrFragEntry.5
            cfrFragEntry.6
            cfrFragEntry.7
            cfrFragEntry.8
            cfrFragEntry.9
            cfrFragEntry.10
            cfrFragEntry.11
            cfrFragEntry.12
            cfrFragEntry.13
            cfrFragEntry.14
            cfrFragEntry.15
            cfrFragEntry.16
            cfrFragEntry.17
            cfrFragEntry.18
            cfrFragEntry.19
            cfrFragEntry.20
            cfrFragEntry.21
            cfrConnectionEntry.1
            cfrConnectionEntry.2
            cfrConnectionEntry.3
            cfrConnectionEntry.4
            cfrConnectionEntry.5
            cfrConnectionEntry.6
            cfrConnectionEntry.7
            cfrConnectionEntry.8
            cfrConnectionEntry.9
            cfrConnectionEntry.10
            cfrConnectionEntry.11
            cfrConnectionEntry.12
            cfrConnectionEntry.13
            cfrConnectionEntry.14
            ciscoMgmt.10.76.1.1.1.1
            ciscoMgmt.10.76.1.1.1.2
            ciscoMgmt.10.76.1.1.1.3
            ciscoMgmt.10.76.1.1.1.4
            cvaIfCfgImpedance
            cvaIfCfgIntegratedDSP
            cvaIfStatusInfoType
            cvaIfMaintenanceMode
            cvaIfStatusSignalErrors
            cvaIfEMCfgSignalType
            cvaIfEMCfgOperation
            cvaIfEMCfgType
            cvaIfEMCfgDialType
            cvaIfEMCfgLmrMCap
            cvaIfEMCfgLmrECap
            cvaIfEMCfgEntry.7
            cvaIfEMInSeizureActive
            cvaIfEMOutSeizureActive
            cvaIfEMTimingDigitDuration
            cvaIfEMTimingInterDigitDuration
            cvaIfEMTimingPulseRate
            cvaIfEMTimingPulseInterDigitDuration
            cvaIfEMTimingClearWaitDuration
            cvaIfEMTimingMaxWinkWaitDuration
            cvaIfEMTimingMaxWinkDuration
            cvaIfEMTimingDelayStart
            cvaIfEMTimingMaxDelayDuration
            cvaIfEMTimingMinDelayPulseWidth
            cvaIfEMTimingVoiceHangover
            cvaIfEMTimeoutLmrTeardown
            cvaIfEMTimingEntry.13
            cvaIfEMTimingEntry.14
            cvaIfEMTimingEntry.15
            cvaIfFXOCfgSignalType
            cvaIfFXOCfgNumberRings
            cvaIfFXOCfgSupDisconnect
            cvaIfFXOCfgDialType
            cvaIfFXOCfgSupDisconnect2
            cvaIfFXOHookStatus
            cvaIfFXORingDetect
            cvaIfFXORingGround
            cvaIfFXOTipGround
            cvaIfFXOTimingDigitDuration
            cvaIfFXOTimingInterDigitDuration
            cvaIfFXOTimingPulseRate
            cvaIfFXOTimingPulseInterDigitDuration
            cvaIfFXSCfgSignalType
            cvaIfFXSRingFrequency
            cvaIfFXSHookStatus
            cvaIfFXSRingActive
            cvaIfFXSRingGround
            cvaIfFXSTipGround
            cvaIfFXSTimingDigitDuration
            cvaIfFXSTimingInterDigitDuration
            cvGeneralPoorQoVNotificationEnable
            cvGeneralFallbackNotificationEnable
            cvGeneralDSCPPolicyNotificationEnable
            cvGeneralMediaPolicyNotificationEnable
            cvPeerCfgIfIndex
            cvPeerCfgType
            cvPeerCfgRowStatus
            cvPeerCfgPeerType
            cvVoicePeerCfgSessionTarget
            cvVoicePeerCfgDialDigitsPrefix
            cvVoicePeerCfgDIDCallEnable
            cvVoicePeerCfgCasGroup
            cvVoicePeerCfgRegisterE164
            cvVoicePeerCfgForwardDigits
            cvVoicePeerCfgEchoCancellerTest
            cvVoIPPeerCfgSessionProtocol
            cvVoIPPeerCfgDesiredQoS
            cvVoIPPeerCfgMinAcceptableQoS
            cvVoIPPeerCfgSessionTarget
            cvVoIPPeerCfgCoderRate
            cvVoIPPeerCfgFaxRate
            cvVoIPPeerCfgVADEnable
            cvVoIPPeerCfgExpectFactor
            cvVoIPPeerCfgIcpif
            cvVoIPPeerCfgPoorQoVNotificationEnable
            cvVoIPPeerCfgUDPChecksumEnable
            cvVoIPPeerCfgIPPrecedence
            cvVoIPPeerCfgTechPrefix
            cvVoIPPeerCfgDigitRelay
            cvVoIPPeerCfgCoderBytes
            cvVoIPPeerCfgFaxBytes
            cvVoIPPeerCfgInBandSignaling
            cvVoIPPeerCfgMediaSetting
            cvVoIPPeerCfgDesiredQoSVideo
            cvVoIPPeerCfgMinAcceptableQoSVideo
            cvVoIPPeerCfgRedirectip2ip
            cvVoIPPeerCfgOctetAligned
            cvVoIPPeerCfgBitRates
            cvVoIPPeerCfgCRC
            cvVoIPPeerCfgCoderMode
            cvVoIPPeerCfgCodingMode
            cvVoIPPeerCfgBitRate
            cvVoIPPeerCfgFrameSize
            cvVoIPPeerCfgDSCPPolicyNotificationEnable
            cvVoIPPeerCfgMediaPolicyNotificationEnable
            cvPeerCommonCfgIncomingDnisDigits
            cvPeerCommonCfgMaxConnections
            cvPeerCommonCfgApplicationName
            cvPeerCommonCfgPreference
            cvPeerCommonCfgHuntStop
            cvPeerCommonCfgDnisMappingName
            cvPeerCommonCfgSourceCarrierId
            cvPeerCommonCfgTargetCarrierId
            cvPeerCommonCfgSourceTrunkGrpLabel
            cvPeerCommonCfgTargetTrunkGrpLabel
            cvCallActiveConnectionId
            cvCallActiveTxDuration
            cvCallActiveVoiceTxDuration
            cvCallActiveFaxTxDuration
            cvCallActiveCoderTypeRate
            cvCallActiveNoiseLevel
            cvCallActiveACOMLevel
            cvCallActiveOutSignalLevel
            cvCallActiveInSignalLevel
            cvCallActiveERLLevel
            cvCallActiveSessionTarget
            cvCallActiveImgPageCount
            cvCallActiveCallingName
            cvCallActiveCallerIDBlock
            cvCallActiveEcanReflectorLocation
            cvCallActiveAccountCode
            cvCallActiveERLLevelRev1
            cvCallActiveCallId
            cvVoIPCallActiveConnectionId
            cvVoIPCallActiveRemoteIPAddress
            cvVoIPCallActiveRemoteUDPPort
            cvVoIPCallActiveRoundTripDelay
            cvVoIPCallActiveSelectedQoS
            cvVoIPCallActiveSessionProtocol
            cvVoIPCallActiveSessionTarget
            cvVoIPCallActiveOnTimeRvPlayout
            cvVoIPCallActiveGapFillWithSilence
            cvVoIPCallActiveGapFillWithPrediction
            cvVoIPCallActiveGapFillWithInterpolation
            cvVoIPCallActiveGapFillWithRedundancy
            cvVoIPCallActiveHiWaterPlayoutDelay
            cvVoIPCallActiveLoWaterPlayoutDelay
            cvVoIPCallActiveReceiveDelay
            cvVoIPCallActiveVADEnable
            cvVoIPCallActiveCoderTypeRate
            cvVoIPCallActiveLostPackets
            cvVoIPCallActiveEarlyPackets
            cvVoIPCallActiveLatePackets
            cvVoIPCallActiveUsername
            cvVoIPCallActiveProtocolCallId
            cvVoIPCallActiveRemSigIPAddrT
            cvVoIPCallActiveRemSigIPAddr
            cvVoIPCallActiveRemSigPort
            cvVoIPCallActiveRemMediaIPAddrT
            cvVoIPCallActiveRemMediaIPAddr
            cvVoIPCallActiveRemMediaPort
            cvVoIPCallActiveSRTPEnable
            cvVoIPCallActiveOctetAligned
            cvVoIPCallActiveBitRates
            cvVoIPCallActiveModeChgPeriod
            cvVoIPCallActiveModeChgNeighbor
            cvVoIPCallActiveMaxPtime
            cvVoIPCallActiveCRC
            cvVoIPCallActiveRobustSorting
            cvVoIPCallActiveEncap
            cvVoIPCallActiveInterleaving
            cvVoIPCallActivePtime
            cvVoIPCallActiveChannels
            cvVoIPCallActiveCoderMode
            cvVoIPCallActiveCallId
            cvVoIPCallActiveCallReferenceId
            ccVoIPCallActivePolicyName
            cvVoIPCallActiveReversedDirectionPeerAddress
            cvVoIPCallActiveEntry.46
            cvVoIPCallActiveMosQe
            cvVoIPCallActiveJBufferNominalDelay
            cvVoIPCallActiveTotalPacketLoss
            cvVoIPCallActiveOutOfOrder
            cvCallActiveDS0s
            cvCallActiveDS0sHighThreshold
            cvCallActiveDS0sLowThreshold
            cvCallActiveDS0sHighNotifyEnable
            cvCallActiveDS0sLowNotifyEnable
            cvCallVolConnActiveConnection
            cvCallVolConnTotalActiveConnections
            cvCallVolConnMaxCallConnectionLicenese
            cvCallVolPeerIncomingCalls
            cvCallVolPeerOutgoingCalls
            cvCallVolMediaIncomingCalls
            cvCallVolMediaOutgoingCalls
            cvCallRateMonitorEnable
            cvCallRateMonitorTime
            cvCallRate
            cvCallRateHiWaterMark
            cvCallHistoryConnectionId
            cvCallHistoryTxDuration
            cvCallHistoryVoiceTxDuration
            cvCallHistoryFaxTxDuration
            cvCallHistoryCoderTypeRate
            cvCallHistoryNoiseLevel
            cvCallHistoryACOMLevel
            cvCallHistorySessionTarget
            cvCallHistoryImgPageCount
            cvCallHistoryCallingName
            cvCallHistoryCallerIDBlock
            cvCallHistoryAccountCode
            cvCallHistoryCallId
            cvVoIPCallHistoryConnectionId
            cvVoIPCallHistoryRemoteIPAddress
            cvVoIPCallHistoryRemoteUDPPort
            cvVoIPCallHistoryRoundTripDelay
            cvVoIPCallHistorySelectedQoS
            cvVoIPCallHistorySessionProtocol
            cvVoIPCallHistorySessionTarget
            cvVoIPCallHistoryOnTimeRvPlayout
            cvVoIPCallHistoryGapFillWithSilence
            cvVoIPCallHistoryGapFillWithPrediction
            cvVoIPCallHistoryGapFillWithInterpolation
            cvVoIPCallHistoryGapFillWithRedundancy
            cvVoIPCallHistoryHiWaterPlayoutDelay
            cvVoIPCallHistoryLoWaterPlayoutDelay
            cvVoIPCallHistoryReceiveDelay
            cvVoIPCallHistoryVADEnable
            cvVoIPCallHistoryCoderTypeRate
            cvVoIPCallHistoryIcpif
            cvVoIPCallHistoryLostPackets
            cvVoIPCallHistoryEarlyPackets
            cvVoIPCallHistoryLatePackets
            cvVoIPCallHistoryUsername
            cvVoIPCallHistoryProtocolCallId
            cvVoIPCallHistoryRemSigIPAddrT
            cvVoIPCallHistoryRemSigIPAddr
            cvVoIPCallHistoryRemSigPort
            cvVoIPCallHistoryRemMediaIPAddrT
            cvVoIPCallHistoryRemMediaIPAddr
            cvVoIPCallHistoryRemMediaPort
            cvVoIPCallHistorySRTPEnable
            cvVoIPCallHistoryFallbackIcpif
            cvVoIPCallHistoryFallbackLoss
            cvVoIPCallHistoryFallbackDelay
            cvVoIPCallHistoryOctetAligned
            cvVoIPCallHistoryBitRates
            cvVoIPCallHistoryModeChgPeriod
            cvVoIPCallHistoryModeChgNeighbor
            cvVoIPCallHistoryMaxPtime
            cvVoIPCallHistoryCRC
            cvVoIPCallHistoryRobustSorting
            cvVoIPCallHistoryEncap
            cvVoIPCallHistoryInterleaving
            cvVoIPCallHistoryPtime
            cvVoIPCallHistoryChannels
            cvVoIPCallHistoryCoderMode
            cvVoIPCallHistoryCallId
            cvVoIPCallHistoryCallReferenceId
            cvVoIPCallHistoryEntry.48
            cvVoIPCallHistoryMosQe
            cvVoIPCallHistoryJBufferNominalDelay
            cvVoIPCallHistoryTotalPacketLoss
            cvVoIPCallHistoryOutOfOrder
            cvCallRateStatsMaxVal
            cvCallRateStatsAvgVal
            cvCallLegRateStatsMaxVal
            cvCallLegRateStatsAvgVal
            cvActiveCallStatsMaxVal
            cvActiveCallStatsAvgVal
            cvCallDurationStatsMaxVal
            cvCallDurationStatsAvgVal
            cvSipMsgRateStatsMaxVal
            cvSipMsgRateStatsAvgVal
            cvCallRateWMValue
            cvCallRateWMts
            cvCallLegRateWMValue
            cvCallLegRateWMts
            cvActiveCallWMValue
            cvActiveCallWMts
            cvSipMsgRateWMValue
            cvSipMsgRateWMts
            cvCallDurationStatsThreshold
            cvCallVolumeWMTableSize
            cvIfCfgEntry.1
            cvIfCfgEntry.2
            cvIfCfgEntry.3
            cvIfCfgEntry.4
            cvIfCfgEntry.5
            cvIfCfgEntry.6
            cvIfCfgEntry.7
            cvIfCfgEntry.8
            cvIfCfgEntry.9
            cvIfCfgEntry.10
            cvIfCfgEntry.11
            cvIfCfgEntry.12
            cvIfCfgEntry.13
            cvIfCfgEntry.14
            cvIfCfgEntry.15
            cAal5VccEntry.1
            cAal5VccEntry.2
            cAal5VccEntry.3
            cAal5VccEntry.4
            cAal5VccEntry.5
            cAal5VccEntry.6
            cAal5VccEntry.7
            cAal5VccEntry.8
            cAal5VccEntry.9
            cAal5VccEntry.10
            cAal5VccEntry.11
            cAal5VccEntry.12
            ciscoMgmt.10.84.1.1.1.5
            ciscoMgmt.10.84.1.1.1.6
            ciscoMgmt.10.84.1.1.1.7
            ciscoMgmt.10.84.1.2.1.4
            ciscoMgmt.10.84.1.2.1.5
            ciscoMgmt.10.84.1.3.1.2
            ciscoMgmt.10.84.2.1.1.7
            ciscoMgmt.10.84.2.1.1.8
            ciscoMgmt.10.84.2.1.1.9
            ciscoMgmt.10.84.2.1.1.10
            ciscoMgmt.10.84.2.1.1.11
            ciscoMgmt.10.84.2.1.1.12
            ciscoMgmt.10.84.2.1.1.13
            ciscoMgmt.10.84.2.1.1.14
            ciscoMgmt.10.84.2.1.1.15
            ciscoMgmt.10.84.2.1.1.16
            ciscoMgmt.10.84.2.1.1.17
            cdeNode.1
            cdeNode.2
            cdeNode.3
            cdeNode.4
            cdeNode.5
            cdeNode.6
            cdeNode.7
            cdeNode.8
            cdeNode.9
            cdeNode.10
            cdeNode.11
            cdeNode.12
            cdeNode.13
            cdeNode.14
            cdeNode.15
            cdeNode.16
            cdeNode.17
            cdeNode.18
            cdeNode.19
            cdeNode.20
            cdeNode.21
            cdeNode.22
            cdeTConnConfigEntry.1
            cdeTConnConfigEntry.2
            cdeTConnConfigEntry.3
            cdeTConnConfigEntry.4
            cdeTConnConfigEntry.5
            cdeTConnConfigEntry.6
            cdeTConnConfigEntry.7
            cdeTConnConfigEntry.8
            cdeTConnConfigEntry.9
            cdeTConnConfigEntry.10
            cdeTConnConfigEntry.11
            cdeTConnConfigEntry.12
            cdeTConnConfigEntry.13
            cdeTConnConfigEntry.14
            cdeTConnOperEntry.1
            cdeTConnOperEntry.2
            cdeTConnOperEntry.3
            cdeTConnOperEntry.4
            cdeTConnOperEntry.5
            cdeTConnTcpConfigEntry.1
            cdeTConnDirectConfigEntry.1
            cdeTConnDirectConfigEntry.2
            cdeTConnDirectConfigEntry.3
            cdeIfEntry.1
            cdeCircuitEntry.1
            cdeCircuitEntry.2
            cdeCircuitEntry.3
            cdeCircuitEntry.4
            cdeFastEntry.5
            cdeFastEntry.6
            cdeFastEntry.7
            cdeFastEntry.8
            cdeFastEntry.9
            cdeFastEntry.10
            cdeFastEntry.11
            cdeFastEntry.12
            cdeTrapControl.1
            cdeTrapControl.2
            ciscoMgmt.10.64.1.1.1.2
            ciscoMgmt.10.64.1.1.1.3
            ciscoMgmt.10.64.1.1.1.4
            ciscoMgmt.10.64.1.1.1.5
            ciscoMgmt.10.64.1.1.1.6
            ciscoMgmt.10.64.2.1.1.4
            ciscoMgmt.10.64.2.1.1.5
            ciscoMgmt.10.64.2.1.1.6
            ciscoMgmt.10.64.2.1.1.7
            ciscoMgmt.10.64.2.1.1.8
            ciscoMgmt.10.64.2.1.1.9
            ciscoMgmt.10.64.3.1.1.1
            ciscoMgmt.10.64.3.1.1.2
            ciscoMgmt.10.64.3.1.1.3
            ciscoMgmt.10.64.3.1.1.4
            ciscoMgmt.10.64.3.1.1.5
            ciscoMgmt.10.64.3.1.1.6
            ciscoMgmt.10.64.3.1.1.7
            ciscoMgmt.10.64.3.1.1.8
            ciscoMgmt.10.64.3.1.1.9
            ciscoMgmt.10.64.4.1.1.1
            ciscoMgmt.10.64.4.1.1.2
            ciscoMgmt.10.64.4.1.1.3
            ciscoMgmt.10.64.4.1.1.4
            ciscoMgmt.10.64.4.1.1.5
            ciscoMgmt.10.64.4.1.1.6
            ciscoMgmt.10.64.4.1.1.7
            ciscoMgmt.10.64.4.1.1.8
            ciscoMgmt.10.64.4.1.1.9
            ciscoMgmt.10.64.4.1.1.10
            ciscoFtpClientMIB.1.1.1
            ciscoFtpClientMIB.1.1.2
            ciscoFtpClientMIB.1.1.3
            ciscoFtpClientMIB.1.1.4
            cfcRequestTable.1.2
            cfcRequestTable.1.3
            cfcRequestTable.1.4
            cfcRequestTable.1.5
            cfcRequestTable.1.6
            cfcRequestTable.1.7
            cfcRequestTable.1.8
            cfcRequestTable.1.9
            cfcRequestTable.1.10
            cfcRequestTable.1.11
            cfcRequestTable.1.12
            ciscoBulkFileMIB.1.1.1
            ciscoBulkFileMIB.1.1.2
            ciscoBulkFileMIB.1.1.3
            ciscoBulkFileMIB.1.1.4
            ciscoBulkFileMIB.1.1.5
            ciscoBulkFileMIB.1.1.6
            ciscoBulkFileMIB.1.1.7
            ciscoBulkFileMIB.1.1.8
            cbfDefineFileTable.1.2
            cbfDefineFileTable.1.3
            cbfDefineFileTable.1.4
            cbfDefineFileTable.1.5
            cbfDefineFileTable.1.6
            cbfDefineFileTable.1.7
            cbfDefineObjectTable.1.2
            cbfDefineObjectTable.1.3
            cbfDefineObjectTable.1.4
            cbfDefineObjectTable.1.5
            cbfDefineObjectTable.1.6
            cbfDefineObjectTable.1.7
            ciscoBulkFileMIB.1.2.1
            ciscoBulkFileMIB.1.2.2
            ciscoBulkFileMIB.1.2.3
            ciscoBulkFileMIB.1.2.4
            cbfStatusFileTable.1.2
            cbfStatusFileTable.1.3
            cbfStatusFileTable.1.4
            cipPrecedenceEntry.3
            cipPrecedenceEntry.4
            cipPrecedenceXEntry.1
            cipPrecedenceXEntry.2
            cipMacEntry.3
            cipMacEntry.4
            cipMacFreeEntry.2
            cipMacXEntry.1
            cipMacXEntry.2
            cdspCardIndex
            cdspCardState
            cdspCardResourceUtilization
            cdspCardLastHiWaterUtilization
            cdspCardLastResetTime
            cdspCardMaxChanPerDSP
            cdspTotalDsp
            cdspFailedDsp
            cdspDspSwitchOverThreshold
            cdspCongestedDsp
            cdspNormalDsp
            cdspNx64Dsp
            cdspCodecTemplateSupported
            cdspCardVideoPoolUtilization
            cdspCardVideoPoolUtilizationThreshold
            cdspOperState
            cdspAlarms
            cdspLastAlarmCause
            cdspLastAlarmCauseText
            cdspLastAlarmTime
            cdspTotalChannels
            cdspInUseChannels
            cdspActiveChannels
            cdspSigBearerChannelSplit
            cdspNumCongestionOccurrence
            cdspDspNum
            cdspXNumberOfBearerCalls
            cdspXNumberOfSigCalls
            cdspXAvailableBearerBandwidth
            cdspXAvailableSigBandwidth
            cdspMIBEnableCardStatusNotification
            cdspEnableOperStateNotification
            cdspVideoUsageNotificationEnable
            cdspVideoOutOfResourceNotificationEnable
            cdspRtpSidPayloadType
            cdspRtcpControl
            cdspRtcpTransInterval
            cdspRtcpRecvMultiplier
            cdspVadAdaptive
            cdspDtmfPowerLevel
            cdspDtmfPowerTwist
            cdspRtcpTimerControl
            cdspVqmControl
            cdspRtcpXrControl
            cdspRtcpXrTransMultiplier
            cdspRtcpXrGminDefault
            cdspRtcpXrExtRfactor
            cdspPktLossConcealment
            cdspVqmThreshSES
            cdspTransparentIpIp
            cdspVoiceModeIpIp
            cdspCurrentUtilCap
            cdspCurrentAvlbCap
            cdspGlobMaxConfTranscodeSess
            cdspGlobMaxAvailTranscodeSess
            cdspTranscodeProfileMaxConfSess
            cdspTranscodeProfileMaxAvailSess
            cdspTranscodeProfileRowStatus
            cdspTranscodeProfileEntry.5
            cdspTranscodeProfileEntry.6
            cdspTranscodeProfileEntry.7
            cdspTranscodeProfileEntry.8
            cdspTranscodeProfileEntry.9
            cdspTranscodeProfileEntry.10
            cdspTranscodeProfileEntry.11
            cdspMtpProfileMaxConfSoftSess
            cdspMtpProfileMaxConfHardSess
            cdspMtpProfileMaxAvailHardSess
            cdspMtpProfileRowStatus
            cdspMtpProfileEntry.6
            cdspMtpProfileEntry.7
            cdspMtpProfileEntry.8
            cdspMtpProfileEntry.9
            cdspMtpProfileEntry.10
            cdspMtpProfileEntry.11
            cdspMtpProfileEntry.12
            cdspMtpProfileEntry.13
            cdspDspfarmObjects.5.1.2
            cdspDspfarmObjects.5.1.3
            cdspDspfarmObjects.5.1.4
            cdspDspfarmObjects.5.1.5
            cdspDspfarmObjects.5.1.6
            cdspDspfarmObjects.5.1.7
            cdspDspfarmObjects.5.1.8
            cdspDspfarmObjects.5.1.9
            cdspDspfarmObjects.5.1.10
            cdspDspfarmObjects.5.1.11
            cdspTotAvailTranscodeSess
            cdspTotUnusedTranscodeSess
            cdspTotAvailMtpSess
            cdspTotUnusedMtpSess
            ciscoMgmt.10.16.1.1.1
            ciscoMgmt.10.16.1.1.2
            ciscoMgmt.10.16.1.1.3
            ciscoMgmt.10.16.1.1.4
            ciscoMgmt.10.195.1.1.1
            ciscoMgmt.10.195.1.1.2
            ciscoMgmt.10.195.1.1.3
            ciscoMgmt.10.195.1.1.4
            ciscoMgmt.10.195.1.1.5
            ciscoMgmt.10.195.1.1.6
            ciscoMgmt.10.195.1.1.7
            ciscoMgmt.10.195.1.1.8
            ciscoMgmt.10.195.1.1.9
            ciscoMgmt.10.195.1.1.10
            ciscoMgmt.10.195.1.1.11
            ciscoMgmt.10.195.1.1.12
            ciscoMgmt.10.195.1.1.13
            ciscoMgmt.10.195.1.1.14
            ciscoMgmt.10.195.1.1.15
            ciscoMgmt.10.195.1.1.16
            ciscoMgmt.10.195.1.1.17
            ciscoMgmt.10.195.1.1.18
            ciscoMgmt.10.195.1.1.19
            ciscoMgmt.10.195.1.1.20
            ciscoMgmt.10.195.1.1.21
            ciscoMgmt.10.195.1.1.22
            ciscoMgmt.10.195.1.1.23
            ciscoMgmt.10.195.1.1.24
            entSensorType
            entSensorScale
            entSensorPrecision
            entSensorValue
            entSensorStatus
            entSensorValueTimeStamp
            entSensorValueUpdateRate
            entSensorMeasuredEntity
            entSensorThresholdSeverity
            entSensorThresholdRelation
            entSensorThresholdValue
            entSensorThresholdEvaluation
            entSensorThresholdNotificationEnable
            ceAssetOEMString
            ceAssetSerialNumber
            ceAssetOrderablePartNumber
            ceAssetHardwareRevision
            ceAssetMfgAssyNumber
            ceAssetMfgAssyRevision
            ceAssetFirmwareID
            ceAssetFirmwareRevision
            ceAssetSoftwareID
            ceAssetSoftwareRevision
            ceAssetCLEI
            ceAssetAlias
            ceAssetTag
            ceAssetIsFRU
            alpsPeerLocalIpAddr
            alpsPeerLocalAtpPort
            alpsPeerKeepaliveTimeout
            alpsPeerKeepaliveMaxRetries
            alpsPeerInCallsAcceptFlag
            alpsRemPeerConnType
            alpsRemPeerLocalPort
            alpsRemPeerRemotePort
            alpsRemPeerState
            alpsRemPeerUptime
            alpsRemPeerNumActiveCkts
            alpsRemPeerIdleTimer
            alpsRemPeerAlarmsEnabled
            alpsRemPeerTCPQlen
            alpsRemPeerOutPackets
            alpsRemPeerOutOctets
            alpsRemPeerInPackets
            alpsRemPeerInOctets
            alpsRemPeerDropsGiant
            alpsRemPeerDropsQFull
            alpsRemPeerDropsPeerUnreach
            alpsRemPeerRowStatus
            alpsRemPeerCfgActivation
            alpsRemPeerCfgTCPQLen
            alpsRemPeerCfgIdleTimer
            alpsRemPeerCfgNoCircTimer
            alpsRemPeerCfgAlarmsOn
            alpsRemPeerCfgStatIntvl
            alpsRemPeerCfgStatRetry
            alpsRemPeerCfgRowStatus
            alpsRemPeerConnLocalPort
            alpsRemPeerConnForeignPort
            alpsRemPeerConnState
            alpsRemPeerConnProtocol
            alpsRemPeerConnCreation
            alpsRemPeerConnActivation
            alpsRemPeerConnUptime
            alpsRemPeerConnNumActCirc
            alpsRemPeerConnLastTxRx
            alpsRemPeerConnLastRxAny
            alpsRemPeerConnIdleTimer
            alpsRemPeerConnNoCircTimer
            alpsRemPeerConnTCPQLen
            alpsRemPeerConnAlarmsOn
            alpsRemPeerConnStatIntvl
            alpsRemPeerConnStatRetry
            alpsRemPeerConnDownReason
            alpsRemPeerConnOutPackets
            alpsRemPeerConnOutOctets
            alpsRemPeerConnInPackets
            alpsRemPeerConnInOctets
            alpsRemPeerConnDropsGiant
            alpsRemPeerConnDropsQFull
            alpsRemPeerConnDropsUnreach
            alpsRemPeerConnDropsVersion
            alpsCktBasePriPeerAddr
            alpsCktBaseAlarmsEnabled
            alpsCktBaseConnType
            alpsCktBaseState
            alpsCktBaseNumActiveAscus
            alpsCktBaseCurrentPeer
            alpsCktBaseLifeTimeTimer
            alpsCktBaseHostLinkNumber
            alpsCktBaseHostLinkType
            alpsCktBaseRemHld
            alpsCktBaseLocalHld
            alpsCktBaseDownReason
            alpsCktBaseOutPackets
            alpsCktBaseOutOctets
            alpsCktBaseInPackets
            alpsCktBaseInOctets
            alpsCktBaseDropsCktDisabled
            alpsCktBaseDropsQOverflow
            alpsCktBaseDropsLifeTimeExpd
            alpsCktBaseEnabled
            alpsCktBaseRowStatus
            alpsCktBaseCurrPeerConnId
            alpsCktX25IfIndex
            alpsCktX25LCN
            alpsCktX25HostX121
            alpsCktX25RemoteX121
            alpsCktX25DropsVcReset
            alpsCktP1024BackupPeerAddr
            alpsCktP1024RetryTimer
            alpsCktP1024IdleTimer
            alpsCktP1024EmtoxX121
            alpsCktP1024Ax25LCN
            alpsCktP1024WinOut
            alpsCktP1024WinIn
            alpsCktP1024OutPktSize
            alpsCktP1024InPktSize
            alpsCktP1024SvcMsgList
            alpsCktP1024SvcMsgIntvl
            alpsCktP1024DropsUnkAscu
            alpsCktP1024RowStatus
            alpsCktP1024MatipCloseDelay
            alpsCktAscuIfIndex
            alpsCktAscuId
            alpsCktAscuStatus
            alpsIfP1024EncapType
            alpsIfP1024PollRespTimeout
            alpsIfP1024GATimeout
            alpsIfP1024PollPauseTimeout
            alpsIfP1024MaxErrCnt
            alpsIfP1024MaxRetrans
            alpsIfP1024CurrErrCnt
            alpsIfP1024MinGoodPollResp
            alpsIfP1024PollingRatio
            alpsIfP1024NumAscus
            alpsIfP1024Entry.11
            alpsIfP1024Entry.12
            alpsIfP1024Entry.13
            alpsIfHLinkX25ProtocolType
            alpsIfHLinkAx25PvcDamp
            alpsIfHLinkEmtoxHostX121
            alpsIfHLinkActiveCkts
            alpsAscuA1
            alpsAscuA2
            alpsAscuCktName
            alpsAscuAlarmsEnabled
            alpsAscuRetryOption
            alpsAscuMaxMsgLength
            alpsAscuFwdStatusOption
            alpsAscuState
            alpsAscuDownReason
            alpsAscuOutPackets
            alpsAscuOutOctets
            alpsAscuInPackets
            alpsAscuInOctets
            alpsAscuDropsGarbledPkts
            alpsAscuDropsAscuDown
            alpsAscuDropsAscuDisabled
            alpsAscuEnabled
            alpsAscuRowStatus
            alpsAscuEntry.20
            alpsSvcMsg
            alpsSvcMsgRowStatus
            alpsIpAddress
            alpsX121ToIpTransRowStatus
            ccCopyTable.1.2
            ccCopyTable.1.3
            ccCopyTable.1.4
            ccCopyTable.1.5
            ccCopyTable.1.6
            ccCopyTable.1.7
            ccCopyTable.1.8
            ccCopyTable.1.9
            ccCopyTable.1.10
            ccCopyTable.1.11
            ccCopyTable.1.12
            ccCopyTable.1.13
            ccCopyTable.1.14
            ccCopyTable.1.15
            ccCopyTable.1.16
            cHsrpGlobalConfig.1
            cHsrpGrpEntry.2
            cHsrpGrpEntry.3
            cHsrpGrpEntry.4
            cHsrpGrpEntry.5
            cHsrpGrpEntry.6
            cHsrpGrpEntry.7
            cHsrpGrpEntry.8
            cHsrpGrpEntry.9
            cHsrpGrpEntry.10
            cHsrpGrpEntry.11
            cHsrpGrpEntry.12
            cHsrpGrpEntry.13
            cHsrpGrpEntry.14
            cHsrpGrpEntry.15
            cHsrpGrpEntry.16
            cHsrpGrpEntry.17
            cHsrpExtIfTrackedEntry.2
            cHsrpExtIfTrackedEntry.3
            cHsrpExtSecAddrEntry.2
            cHsrpExtIfEntry.1
            cHsrpExtIfEntry.2
            cpmCPUTotalTable.1.2
            cpmCPUTotalTable.1.3
            cpmCPUTotalTable.1.4
            cpmCPUTotalTable.1.5
            cpmCPUTotalTable.1.6
            cpmCPUTotalTable.1.7
            cpmCPUTotalTable.1.8
            cpmCPUTotalTable.1.9
            cpmCPUTotalTable.1.10
            cpmCPUTotalTable.1.11
            cpmCPUTotalTable.1.12
            cpmCPUTotalTable.1.13
            cpmCPUTotalTable.1.14
            cpmCPUTotalTable.1.15
            cpmCPUTotalTable.1.16
            cpmCPUTotalTable.1.17
            cpmCPUTotalTable.1.18
            cpmCPUTotalTable.1.19
            cpmCPUTotalTable.1.20
            cpmCPUTotalTable.1.21
            cpmCPUTotalTable.1.22
            cpmCPUTotalTable.1.23
            cpmCPUTotalTable.1.24
            cpmCPUTotalTable.1.25
            cpmCPUTotalTable.1.26
            cpmCPUTotalTable.1.27
            cpmCPUTotalTable.1.28
            cpmCPUTotalTable.1.29
            cpmProcessTable.1.1
            cpmProcessTable.1.2
            cpmProcessTable.1.4
            cpmProcessTable.1.5
            cpmProcessTable.1.6
            cpmProcessExtTable.1.1
            cpmProcessExtTable.1.2
            cpmProcessExtTable.1.3
            cpmProcessExtTable.1.4
            cpmProcessExtTable.1.5
            cpmProcessExtTable.1.6
            cpmProcessExtTable.1.7
            cpmProcessExtTable.1.8
            ciscoProcessMIB.10.9.3.1.1
            ciscoProcessMIB.10.9.3.1.2
            ciscoProcessMIB.10.9.3.1.3
            ciscoProcessMIB.10.9.3.1.4
            ciscoProcessMIB.10.9.3.1.5
            ciscoProcessMIB.10.9.3.1.6
            ciscoProcessMIB.10.9.3.1.7
            ciscoProcessMIB.10.9.3.1.8
            ciscoProcessMIB.10.9.3.1.9
            ciscoProcessMIB.10.9.3.1.10
            ciscoProcessMIB.10.9.3.1.11
            ciscoProcessMIB.10.9.3.1.12
            ciscoProcessMIB.10.9.3.1.13
            ciscoProcessMIB.10.9.3.1.14
            ciscoProcessMIB.10.9.3.1.15
            ciscoProcessMIB.10.9.3.1.16
            ciscoProcessMIB.10.9.3.1.17
            ciscoProcessMIB.10.9.3.1.18
            ciscoProcessMIB.10.9.3.1.19
            ciscoProcessMIB.10.9.3.1.20
            ciscoProcessMIB.10.9.3.1.21
            ciscoProcessMIB.10.9.3.1.22
            ciscoProcessMIB.10.9.3.1.23
            ciscoProcessMIB.10.9.3.1.24
            ciscoProcessMIB.10.9.3.1.25
            ciscoProcessMIB.10.9.3.1.26
            ciscoProcessMIB.10.9.3.1.27
            ciscoProcessMIB.10.9.3.1.28
            ciscoProcessMIB.10.9.3.1.29
            ciscoProcessMIB.10.9.3.1.30
            cpmCPUThresholdTable.1.2
            cpmCPUThresholdTable.1.3
            cpmCPUThresholdTable.1.4
            cpmCPUThresholdTable.1.5
            cpmCPUThresholdTable.1.6
            ciscoProcessMIB.10.9.5.1
            ciscoProcessMIB.10.9.5.2
            cpmCPUHistoryTable.1.2
            cpmCPUHistoryTable.1.3
            cpmCPUHistoryTable.1.4
            cpmCPUHistoryTable.1.5
            cpmCPUProcessHistoryTable.1.2
            cpmCPUProcessHistoryTable.1.3
            cpmCPUProcessHistoryTable.1.4
            cpmCPUProcessHistoryTable.1.5
            cpmThreadTable.1.2
            cpmThreadTable.1.3
            cpmThreadTable.1.4
            cpmThreadTable.1.5
            cpmThreadTable.1.6
            cpmThreadTable.1.7
            cpmThreadTable.1.8
            cpmThreadTable.1.9
            cpmVirtualProcessTable.1.2
            cpmVirtualProcessTable.1.3
            cpmVirtualProcessTable.1.4
            cpmVirtualProcessTable.1.5
            cpmVirtualProcessTable.1.6
            cpmVirtualProcessTable.1.7
            cpmVirtualProcessTable.1.8
            cpmVirtualProcessTable.1.9
            cpmVirtualProcessTable.1.10
            cpmVirtualProcessTable.1.11
            cpmVirtualProcessTable.1.12
            cpmVirtualProcessTable.1.13
            ccarConfigType
            ccarConfigAccIdx
            ccarConfigRate
            ccarConfigLimit
            ccarConfigExtLimit
            ccarConfigConformAction
            ccarConfigExceedAction
            ccarStatSwitchedPkts
            ccarStatSwitchedBytes
            ccarStatFilteredPkts
            ccarStatFilteredBytes
            ccarStatCurBurst
            ccarStatSwitchedPktsOverflow
            ccarStatSwitchedBytesOverflow
            ccarStatFilteredPktsOverflow
            ccarStatFilteredBytesOverflow
            ccarStatHCSwitchedPkts
            ccarStatHCSwitchedBytes
            ccarStatHCFilteredPkts
            ccarStatHCFilteredBytes
            ciscoMgmt.10.196.3.1
            ciscoMgmt.10.196.3.2
            ciscoMgmt.10.196.3.3
            ciscoMgmt.10.196.3.4
            ciscoMgmt.10.196.3.5
            ciscoMgmt.10.196.3.6.1.2
            ciscoMgmt.10.196.3.6.1.3
            ciscoMgmt.10.196.3.6.1.4
            ciscoMgmt.10.196.3.6.1.5
            ciscoMgmt.10.196.3.6.1.6
            ciscoMgmt.10.196.3.6.1.7
            ciscoMgmt.10.196.3.6.1.8
            ciscoMgmt.10.196.3.6.1.9
            ciscoMgmt.10.196.3.6.1.10
            ciscoMgmt.10.196.3.6.1.11
            ciscoMgmt.10.196.3.6.1.12
            ciscoMgmt.10.196.3.6.1.13
            ciscoMgmt.10.196.3.6.1.14
            ciscoMgmt.10.196.3.6.1.15
            ciscoMgmt.10.196.3.6.1.16
            ciscoMgmt.10.196.3.6.1.17
            ciscoMgmt.10.196.3.6.1.18
            ciscoMgmt.10.196.3.6.1.19
            ciscoMgmt.10.196.3.6.1.20
            ciscoMgmt.10.196.3.6.1.21
            ciscoMgmt.10.196.3.6.1.22
            ciscoMgmt.10.196.3.6.1.23
            ciscoMgmt.10.196.3.6.1.24
            ciscoMgmt.10.196.3.6.1.25
            ciscoMgmt.10.196.3.7
            ciscoMgmt.10.196.3.8
            ciscoMgmt.10.196.3.9
            ciscoMgmt.10.196.3.10
            ciscoMgmt.10.196.4.1.1.2
            ciscoMgmt.10.196.4.1.1.3
            ciscoMgmt.10.196.4.1.1.4
            ciscoMgmt.10.196.4.1.1.5
            ciscoMgmt.10.196.4.1.1.6
            ciscoMgmt.10.196.4.1.1.7
            ciscoMgmt.10.196.4.1.1.8
            ciscoMgmt.10.196.4.1.1.9
            ciscoMgmt.10.196.4.1.1.10
            ciscoMgmt.10.196.4.2.1.2
            cefcFRUPowerSupplyGroupTable.1.1
            cefcFRUPowerSupplyGroupTable.1.2
            cefcFRUPowerSupplyGroupTable.1.3
            cefcFRUPowerSupplyGroupTable.1.4
            cefcFRUPowerSupplyGroupTable.1.5
            cefcFRUPowerSupplyGroupTable.1.6
            cefcFRUPowerSupplyGroupTable.1.7
            cefcFRUPowerStatusTable.1.1
            cefcFRUPowerStatusTable.1.2
            cefcFRUPowerStatusTable.1.3
            cefcFRUPowerStatusTable.1.4
            cefcFRUPowerStatusTable.1.5
            cefcMaxDefaultInLinePower
            cefcFRUPowerSupplyValueTable.1.1
            cefcFRUPowerSupplyValueTable.1.2
            cefcFRUPowerSupplyValueTable.1.3
            cefcFRUPowerSupplyValueTable.1.4
            ciscoEntityFRUControlMIB.1.1.5
            cefcModuleTable.1.1
            cefcModuleTable.1.2
            cefcModuleTable.1.3
            cefcModuleTable.1.4
            cefcModuleTable.1.5
            cefcModuleTable.1.6
            cefcModuleTable.1.7
            cefcModuleTable.1.8
            ciscoEntityFRUControlMIB.10.9.2.1.1
            ciscoEntityFRUControlMIB.10.9.2.1.2
            ciscoEntityFRUControlMIB.10.9.3.1.1
            cefcMIBEnableStatusNotification
            ciscoEntityFRUControlMIB.1.3.2
            ciscoEntityFRUControlMIB.10.25.1.1.1
            ciscoEntityFRUControlMIB.10.36.1.1.1
            ciscoEntityFRUControlMIB.10.49.1.1.2
            ciscoEntityFRUControlMIB.10.49.2.1.2
            ciscoEntityFRUControlMIB.10.49.2.1.3
            ciscoEntityFRUControlMIB.10.64.1.1.1
            ciscoEntityFRUControlMIB.10.64.1.1.2
            ciscoEntityFRUControlMIB.10.64.2.1.1
            ciscoEntityFRUControlMIB.10.64.2.1.2
            ciscoEntityFRUControlMIB.10.64.3.1.1
            ciscoEntityFRUControlMIB.10.64.3.1.2
            ciscoEntityFRUControlMIB.10.64.4.1.2
            ciscoEntityFRUControlMIB.10.64.4.1.3
            ciscoEntityFRUControlMIB.10.64.4.1.4
            ciscoEntityFRUControlMIB.10.64.4.1.5
            ciscoEntityFRUControlMIB.10.81.1.1.1
            ciscoEntityFRUControlMIB.10.81.2.1.1
            ciscoMgmt.10.84.1.1.1.2
            ciscoMgmt.10.84.1.1.1.3
            ciscoMgmt.10.84.1.1.1.4
            ciscoMgmt.10.84.1.1.1.5
            ciscoMgmt.10.84.1.1.1.6
            ciscoMgmt.10.84.1.1.1.7
            ciscoMgmt.10.84.1.1.1.8
            ciscoMgmt.10.84.1.1.1.9
            ciscoMgmt.10.84.2.1.1.1
            ciscoMgmt.10.84.2.1.1.2
            ciscoMgmt.10.84.2.1.1.3
            ciscoMgmt.10.84.2.1.1.4
            ciscoMgmt.10.84.2.1.1.5
            ciscoMgmt.10.84.2.1.1.6
            ciscoMgmt.10.84.2.1.1.7
            ciscoMgmt.10.84.2.1.1.8
            ciscoMgmt.10.84.2.1.1.9
            ciscoMgmt.10.84.2.2.1.1
            ciscoMgmt.10.84.2.2.1.2
            ciscoMgmt.10.84.3.1.1.2
            ciscoMgmt.10.84.3.1.1.3
            ciscoMgmt.10.84.3.1.1.4
            ciscoMgmt.10.84.3.1.1.5
            ciscoMgmt.10.84.4.1.1.3
            ciscoMgmt.10.84.4.1.1.4
            ciscoMgmt.10.84.4.1.1.5
            ciscoMgmt.10.84.4.1.1.6
            ciscoMgmt.10.84.4.1.1.7
            ciscoMgmt.10.84.4.2.1.3
            ciscoMgmt.10.84.4.2.1.4
            ciscoMgmt.10.84.4.2.1.5
            ciscoMgmt.10.84.4.2.1.6
            ciscoMgmt.10.84.4.2.1.7
            ciscoMgmt.10.84.4.3.1.3
            ciscoMgmt.10.84.4.3.1.4
            ciscoMgmt.10.84.4.3.1.5
            ciscoMgmt.10.84.4.3.1.6
            ciscoMgmt.10.84.4.3.1.7
            cssTotalEntry.1
            cssTotalEntry.2
            cssTotalEntry.3
            cssTotalEntry.4
            cslTotalEntry.1
            cslTotalEntry.2
            cslTotalEntry.3
            cslTotalEntry.4
            cslFarEndTotalEntry.1
            cslFarEndTotalEntry.2
            cslFarEndTotalEntry.3
            cslFarEndTotalEntry.4
            cspTotalEntry.1
            cspTotalEntry.2
            cspTotalEntry.3
            cspTotalEntry.4
            cspFarEndTotalEntry.1
            cspFarEndTotalEntry.2
            cspFarEndTotalEntry.3
            cspFarEndTotalEntry.4
            csNotifications.1
            cviRoutedVlanIfIndex
            ciscoMgmt.172.16.84.1.1
            ciscoMgmt.172.16.94.1.1
            ciscoMgmt.172.16.120.1.1
            ciscoMgmt.172.16.120.1.2
            ciscoMgmt.172.16.136.1.1
            ciscoMgmt.172.16.136.1.2
            ciscoMgmt.172.16.115.1.1
            ciscoMgmt.172.16.115.1.2
            ciscoMgmt.172.16.115.1.3
            ciscoMgmt.172.16.115.1.4
            ciscoMgmt.172.16.115.1.5
            ciscoMgmt.172.16.115.1.6
            ciscoMgmt.172.16.115.1.7
            ciscoMgmt.172.16.115.1.8
            ciscoMgmt.172.16.115.1.9
            ciscoMgmt.172.16.115.1.10
            ciscoMgmt.172.16.115.1.11
            ciscoMgmt.172.16.115.1.12
            ciscoMgmt.172.16.151.1.1
            ciscoMgmt.172.16.151.1.2
            ceAlarmDescrVendorType
            ceAlarmDescrSeverity
            ceAlarmDescrText
            ceAlarmCriticalCount
            ceAlarmMajorCount
            ceAlarmMinorCount
            ceAlarmCutOff
            ceAlarmFilterProfile
            ceAlarmSeverity
            ceAlarmList
            ceAlarmHistTableSize
            ceAlarmHistLastIndex
            ceAlarmHistType
            ceAlarmHistEntPhysicalIndex
            ceAlarmHistAlarmType
            ceAlarmHistSeverity
            ceAlarmHistTimeStamp
            ceAlarmNotifiesEnable
            ceAlarmSyslogEnable
            ceAlarmFilterProfileIndexNext
            ceAlarmFilterStatus
            ceAlarmFilterAlias
            ceAlarmFilterAlarmsEnabled
            ceAlarmFilterNotifiesEnabled
            ceAlarmFilterSyslogEnabled
            ccapAppLocation
            ccapAppLoadState
            ccapAppLoadFailReason
            ccapAppDescr
            ccapAppCallType
            ccapAppRowStatus
            ccapAppActiveInstances
            ccapAppEventLogging
            ccapAppPSTNInCallNowConn
            ccapAppPSTNOutCallNowConn
            ccapAppIPInCallNowConn
            ccapAppIPOutCallNowConn
            ccapAppPlaceCallInProgress
            ccapAppHandoffInProgress
            ccapAppPromptPlayActive
            ccapAppRecordingActive
            ccapAppTTSActive
            ccapAppTypeHisEvtLogging
            ccapAppTypeHisLastResetTime
            ccapAppTypeHisPSTNInCallSetupInd
            ccapAppTypeHisPSTNInCallTotConn
            ccapAppTypeHisPSTNInCallHandedOut
            ccapAppTypeHisPSTNInCallHandOutRet
            ccapAppTypeHisPSTNInCallInHandoff
            ccapAppTypeHisPSTNInCallInHandoffRet
            ccapAppTypeHisPSTNInCallDiscNormal
            ccapAppTypeHisPSTNInCallDiscUsrErr
            ccapAppTypeHisPSTNInCallDiscSysErr
            ccapAppTypeHisPSTNOutCallSetupReq
            ccapAppTypeHisPSTNOutCallTotConn
            ccapAppTypeHisPSTNOutCallHandedOut
            ccapAppTypeHisPSTNOutCallHandOutRet
            ccapAppTypeHisPSTNOutCallInHandoff
            ccapAppTypeHisPSTNOutCallInHandoffRet
            ccapAppTypeHisPSTNOutCallDiscNormal
            ccapAppTypeHisPSTNOutCallDiscUsrErr
            ccapAppTypeHisPSTNOutCallDiscSysErr
            ccapAppTypeHisIPInCallSetupInd
            ccapAppTypeHisIPInCallTotConn
            ccapAppTypeHisIPInCallHandedOut
            ccapAppTypeHisIPInCallHandOutRet
            ccapAppTypeHisIPInCallInHandoff
            ccapAppTypeHisIPInCallInHandoffRet
            ccapAppTypeHisIPInCallDiscNormal
            ccapAppTypeHisIPInCallDiscUsrErr
            ccapAppTypeHisIPInCallDiscSysErr
            ccapAppTypeHisIPOutCallSetupReq
            ccapAppTypeHisIPOutCallTotConn
            ccapAppTypeHisIPOutCallHandedOut
            ccapAppTypeHisIPOutCallHandOutRet
            ccapAppTypeHisIPOutCallInHandoff
            ccapAppTypeHisIPOutCallInHandoffRet
            ccapAppTypeHisIPOutCallDiscNormal
            ccapAppTypeHisIPOutCallDiscUsrErr
            ccapAppTypeHisIPOutCallDiscSysErr
            ccapAppTypeHisPlaceCallAttempts
            ccapAppTypeHisPlaceCallSuccess
            ccapAppTypeHisPlaceCallFailure
            ccapAppTypeHisInHandoffCallback
            ccapAppTypeHisInHandoffCallbackRet
            ccapAppTypeHisInHandoffNoCallback
            ccapAppTypeHisOutHandoffCallback
            ccapAppTypeHisOutHandoffCallbackRet
            ccapAppTypeHisOutHandoffNoCallback
            ccapAppTypeHisOutHandofffailures
            ccapAppTypeHisDocumentReadAttempts
            ccapAppTypeHisDocumentReadSuccess
            ccapAppTypeHisDocumentReadFailures
            ccapAppTypeHisDocumentParseErrors
            ccapAppTypeHisDocumentWriteAttempts
            ccapAppTypeHisDocumentWriteSuccess
            ccapAppTypeHisDocumentWriteFailures
            ccapAppTypeHisDTMFAttempts
            ccapAppTypeHisDTMFAborted
            ccapAppTypeHisDTMFNoMatch
            ccapAppTypeHisDTMFNoInput
            ccapAppTypeHisDTMFMatch
            ccapAppTypeHisDTMFLongPound
            ccapAppTypeHisASRAttempts
            ccapAppTypeHisASRAborted
            ccapAppTypeHisASRNoMatch
            ccapAppTypeHisASRNoInput
            ccapAppTypeHisASRMatch
            ccapAppTypeHisAAAAuthenticateFailure
            ccapAppTypeHisAAAAuthenticateSuccess
            ccapAppTypeHisAAAAuthorizeFailure
            ccapAppTypeHisAAAAuthorizeSuccess
            ccapAppTypeHisASNLSubscriptionsSent
            ccapAppTypeHisASNLSubscriptionsSuccess
            ccapAppTypeHisASNLSubscriptionsFailed
            ccapAppTypeHisASNLNotifReceived
            ccapAppTypeHisPromptPlayAttempts
            ccapAppTypeHisPromptPlaySuccess
            ccapAppTypeHisPromptPlayFailed
            ccapAppTypeHisPromptPlayDuration
            ccapAppTypeHisRecordingAttempts
            ccapAppTypeHisRecordingSuccess
            ccapAppTypeHisRecordingFailed
            ccapAppTypeHisRecordingDuration
            ccapAppTypeHisTTSAttempts
            ccapAppTypeHisTTSSuccess
            ccapAppTypeHisTTSFailed
            ccapAppInstHisSessionID
            ccapAppInstHisAppName
            ccapAppInstHisPSTNInCallSetupInd
            ccapAppInstHisPSTNInCallTotConn
            ccapAppInstHisPSTNInCallHandedOut
            ccapAppInstHisPSTNInCallHandOutRet
            ccapAppInstHisPSTNInCallInHandoff
            ccapAppInstHisPSTNInCallInHandoffRet
            ccapAppInstHisPSTNInCallDiscNormal
            ccapAppInstHisPSTNInCallDiscUsrErr
            ccapAppInstHisPSTNInCallDiscSysErr
            ccapAppInstHisPSTNOutCallSetupReq
            ccapAppInstHisPSTNOutCallTotConn
            ccapAppInstHisPSTNOutCallHandedOut
            ccapAppInstHisPSTNOutCallHandOutRet
            ccapAppInstHisPSTNOutCallInHandoff
            ccapAppInstHisPSTNOutCallInHandoffRet
            ccapAppInstHisPSTNOutCallDiscNormal
            ccapAppInstHisPSTNOutCallDiscUsrErr
            ccapAppInstHisPSTNOutCallDiscSysErr
            ccapAppInstHisIPInCallSetupInd
            ccapAppInstHisIPInCallTotConn
            ccapAppInstHisIPInCallHandedOut
            ccapAppInstHisIPInCallHandOutRet
            ccapAppInstHisIPInCallInHandoff
            ccapAppInstHisIPInCallInHandoffRet
            ccapAppInstHisIPInCallDiscNormal
            ccapAppInstHisIPInCallDiscUsrErr
            ccapAppInstHisIPInCallDiscSysErr
            ccapAppInstHisIPOutCallSetupReq
            ccapAppInstHisIPOutCallTotConn
            ccapAppInstHisIPOutCallHandedOut
            ccapAppInstHisIPOutCallHandOutRet
            ccapAppInstHisIPOutCallInHandoff
            ccapAppInstHisIPOutCallInHandoffRet
            ccapAppInstHisIPOutCallDiscNormal
            ccapAppInstHisIPOutCallDiscUsrErr
            ccapAppInstHisIPOutCallDiscSysErr
            ccapAppInstHisPlaceCallAttempts
            ccapAppInstHisPlaceCallSuccess
            ccapAppInstHisPlaceCallFailure
            ccapAppInstHisInHandoffCallback
            ccapAppInstHisInHandoffCallbackRet
            ccapAppInstHisInHandoffNoCallback
            ccapAppInstHisOutHandoffCallback
            ccapAppInstHisOutHandoffCallbackRet
            ccapAppInstHisOutHandoffNoCallback
            ccapAppInstHisOutHandofffailures
            ccapAppInstHisDocumentReadAttempts
            ccapAppInstHisDocumentReadSuccess
            ccapAppInstHisDocumentReadFailures
            ccapAppInstHisDocumentParseErrors
            ccapAppInstHisDocumentWriteAttempts
            ccapAppInstHisDocumentWriteSuccess
            ccapAppInstHisDocumentWriteFailures
            ccapAppInstHisDTMFAttempts
            ccapAppInstHisDTMFAborted
            ccapAppInstHisDTMFNoMatch
            ccapAppInstHisDTMFNoInput
            ccapAppInstHisDTMFMatch
            ccapAppInstHisDTMFLongPound
            ccapAppInstHisASRAttempts
            ccapAppInstHisASRAborted
            ccapAppInstHisASRNoMatch
            ccapAppInstHisASRNoInput
            ccapAppInstHisASRMatch
            ccapAppInstHisAAAAuthenticateFailure
            ccapAppInstHisAAAAuthenticateSuccess
            ccapAppInstHisAAAAuthorizeFailure
            ccapAppInstHisAAAAuthorizeSuccess
            ccapAppInstHisASNLSubscriptionsSent
            ccapAppInstHisASNLSubscriptionsSuccess
            ccapAppInstHisASNLSubscriptionsFailed
            ccapAppInstHisASNLNotifReceived
            ccapAppInstHisPromptPlayAttempts
            ccapAppInstHisPromptPlaySuccess
            ccapAppInstHisPromptPlayFailed
            ccapAppInstHisPromptPlayDuration
            ccapAppInstHisRecordingAttempts
            ccapAppInstHisRecordingSuccess
            ccapAppInstHisRecordingFailed
            ccapAppInstHisRecordingDuration
            ccapAppInstHisTTSAttempts
            ccapAppInstHisTTSSuccess
            ccapAppInstHisTTSFailed
            ccapAppInstHistEvtLogging
            ccapAppGblActCurrentInstances
            ccapAppGblActPSTNInCallNowConn
            ccapAppGblActPSTNOutCallNowConn
            ccapAppGblActIPInCallNowConn
            ccapAppGblActIPOutCallNowConn
            ccapAppGblActPlaceCallInProgress
            ccapAppGblActHandoffInProgress
            ccapAppGblActPromptPlayActive
            ccapAppGblActRecordingActive
            ccapAppGblActTTSActive
            ccapAppGblStatsLogging
            ccapAppGblEventLogging
            ccapAppGblEvtLogflush
            ccapAppGblStatsClear
            ccapAppGblLastResetTime
            ccapAppGblHisTotalInstances
            ccapAppGblHisLastReset
            ccapAppGblHisPSTNInCallSetupInd
            ccapAppGblHisPSTNInCallTotConn
            ccapAppGblHisPSTNInCallHandedOut
            ccapAppGblHisPSTNInCallHandOutRet
            ccapAppGblHisPSTNInCallInHandoff
            ccapAppGblHisPSTNInCallInHandoffRet
            ccapAppGblHisPSTNInCallDiscNormal
            ccapAppGblHisPSTNInCallDiscUsrErr
            ccapAppGblHisPSTNInCallDiscSysErr
            ccapAppGblHisPSTNOutCallSetupReq
            ccapAppGblHisPSTNOutCallTotConn
            ccapAppGblHisPSTNOutCallHandedOut
            ccapAppGblHisPSTNOutCallHandOutRet
            ccapAppGblHisPSTNOutCallInHandoff
            ccapAppGblHisPSTNOutCallInHandoffRet
            ccapAppGblHisPSTNOutCallDiscNormal
            ccapAppGblHisPSTNOutCallDiscUsrErr
            ccapAppGblHisPSTNOutCallDiscSysErr
            ccapAppGblHisIPInCallSetupInd
            ccapAppGblHisIPInCallTotConn
            ccapAppGblHisIPInCallHandedOut
            ccapAppGblHisIPInCallHandOutRet
            ccapAppGblHisIPInCallInHandoff
            ccapAppGblHisIPInCallInHandoffRet
            ccapAppGblHisIPInCallDiscNormal
            ccapAppGblHisIPInCallDiscUsrErr
            ccapAppGblHisIPInCallDiscSysErr
            ccapAppGblHisIPOutCallSetupReq
            ccapAppGblHisIPOutCallTotConn
            ccapAppGblHisIPOutCallHandedOut
            ccapAppGblHisIPOutCallHandOutRet
            ccapAppGblHisIPOutCallInHandoff
            ccapAppGblHisIPOutCallInHandoffRet
            ccapAppGblHisIPOutCallDiscNormal
            ccapAppGblHisIPOutCallDiscUsrErr
            ccapAppGblHisIPOutCallDiscSysErr
            ccapAppGblHisPlaceCallAttempts
            ccapAppGblHisPlaceCallSuccess
            ccapAppGblHisPlaceCallFailure
            ccapAppGblHisInHandoffCallback
            ccapAppGblHisInHandoffCallbackRet
            ccapAppGblHisInHandoffNoCallback
            ccapAppGblHisOutHandoffCallback
            ccapAppGblHisOutHandoffCallbackRet
            ccapAppGblHisOutHandoffNoCallback
            ccapAppGblHisOutHandofffailures
            ccapAppGblHisDocumentReadAttempts
            ccapAppGblHisDocumentReadSuccess
            ccapAppGblHisDocumentReadFailures
            ccapAppGblHisDocumentParseErrors
            ccapAppGblHisDocumentWriteAttempts
            ccapAppGblHisDocumentWriteSuccess
            ccapAppGblHisDocumentWriteFailures
            ccapAppGblHisDTMFAttempts
            ccapAppGblHisDTMFAborted
            ccapAppGblHisDTMFNoMatch
            ccapAppGblHisDTMFNoInput
            ccapAppGblHisDTMFMatch
            ccapAppGblHisDTMFLongPound
            ccapAppGblHisASRAttempts
            ccapAppGblHisASRAborted
            ccapAppGblHisASRNoMatch
            ccapAppGblHisASRNoInput
            ccapAppGblHisASRMatch
            ccapAppGblHisAAAAuthenticateFailure
            ccapAppGblHisAAAAuthenticateSuccess
            ccapAppGblHisAAAAuthorizeFailure
            ccapAppGblHisAAAAuthorizeSuccess
            ccapAppGblHisASNLSubscriptionsSent
            ccapAppGblHisASNLSubscriptionsSuccess
            ccapAppGblHisASNLSubscriptionsFailed
            ccapAppGblHisASNLNotifReceived
            ccapAppGblHisPromptPlayAttempts
            ccapAppGblHisPromptPlaySuccess
            ccapAppGblHisPromptPlayFailed
            ccapAppGblHisPromptPlayDuration
            ccapAppGblHisRecordingAttempts
            ccapAppGblHisRecordingSuccess
            ccapAppGblHisRecordingFailed
            ccapAppGblHisRecordingDuration
            ccapAppGblHisTTSAttempts
            ccapAppGblHisTTSSuccess
            ccapAppGblHisTTSFailed
            ccapAppIntfGblStatsLogging
            ccapAppIntfGblEventLogging
            ccapAppIntfGblEvtLogFlush
            ccapAppIntfGblStatsClear
            ccapAppIntfGblLastResetTime
            ccapAppIntfHTTPStats
            ccapAppIntfHTTPEvtLog
            ccapAppIntfHTTPGetRequest
            ccapAppIntfHTTPGetSuccess
            ccapAppIntfHTTPGetFailure
            ccapAppIntfHTTPPostRequest
            ccapAppIntfHTTPPostSuccess
            ccapAppIntfHTTPPostFailure
            ccapAppIntfHTTPTxBytes
            ccapAppIntfHTTPRxBytes
            ccapAppIntfHTTPMinXferRate
            ccapAppIntfHTTPMaxXferRate
            ccapAppIntfHTTPAvgXferRate
            ccapAppIntfHTTPLastResetTime
            ccapAppIntfRTSPStats
            ccapAppIntfRTSPEvtLog
            ccapAppIntfRTSPReadRequest
            ccapAppIntfRTSPReadSuccess
            ccapAppIntfRTSPReadFailure
            ccapAppIntfRTSPWriteRequest
            ccapAppIntfRTSPWriteSuccess
            ccapAppIntfRTSPWriteFailure
            ccapAppIntfRTSPTxBytes
            ccapAppIntfRTSPRxBytes
            ccapAppIntfRTSPMinXferRate
            ccapAppIntfRTSPMaxXferRate
            ccapAppIntfRTSPAvgXferRate
            ccapAppIntfRTSPLastResetTime
            ccapAppIntfTFTPStats
            ccapAppIntfTFTPEvtLog
            ccapAppIntfTFTPReadRequest
            ccapAppIntfTFTPReadSuccess
            ccapAppIntfTFTPReadFailure
            ccapAppIntfTFTPWriteRequest
            ccapAppIntfTFTPWriteSuccess
            ccapAppIntfTFTPWriteFailure
            ccapAppIntfTFTPTxBytes
            ccapAppIntfTFTPRxBytes
            ccapAppIntfTFTPMinXferRate
            ccapAppIntfTFTPMaxXferRate
            ccapAppIntfTFTPAvgXferRate
            ccapAppIntfTFTPLastResetTime
            ccapAppIntfFlashReadRequest
            ccapAppIntfFlashReadSuccess
            ccapAppIntfFlashReadFailure
            ccapAppIntfRAMRecordReadRequest
            ccapAppIntfRAMRecordReadSuccess
            ccapAppIntfRAMRecordiongReadFailure
            ccapAppIntfRAMRecordRequest
            ccapAppIntfRAMRecordSuccess
            ccapAppIntfRAMRecordiongFailure
            ccapAppIntfSMTPStats
            ccapAppIntfSMTPEvtLog
            ccapAppIntfSMTPReadRequest
            ccapAppIntfSMTPReadSuccess
            ccapAppIntfSMTPReadFailure
            ccapAppIntfSMTPWriteRequest
            ccapAppIntfSMTPWriteSuccess
            ccapAppIntfSMTPWriteFailure
            ccapAppIntfSMTPTxBytes
            ccapAppIntfSMTPRxBytes
            ccapAppIntfSMTPMinXferRate
            ccapAppIntfSMTPMaxXferRate
            ccapAppIntfSMTPAvgXferRate
            ccapAppIntfSMTPLastResetTime
            ccapAppIntfAAAMethodListStats
            ccapAppIntfAAAMethodListEvtLog
            ccapAppIntfAAAMethodListReadRequest
            ccapAppIntfAAAMethodListReadSuccess
            ccapAppIntfAAAMethodListReadFailure
            ccapAppIntfAAAMethodListLastResetTime
            ccapAppIntfASRStats
            ccapAppIntfASREvtLog
            ccapAppIntfASRReadRequest
            ccapAppIntfASRReadSuccess
            ccapAppIntfASRReadFailure
            ccapAppIntfASRLastResetTime
            ccapAppIntfTTSStats
            ccapAppIntfTTSEvtLog
            ccapAppIntfTTSReadRequest
            ccapAppIntfTTSReadSuccess
            ccapAppIntfTTSReadFailure
            ccapAppIntfTTSLastResetTime
            cbpAcctEntry.1
            cbpAcctEntry.2
            cbpAcctEntry.3
            cbpAcctEntry.4
            cbpAcctEntry.5
            ciscoMgmt.172.16.154.1
            ciscoMgmt.172.16.154.2
            ciscoMgmt.172.16.154.3.1.2
            ciscoMgmt.172.16.154.3.1.3
            ciscoMgmt.172.16.154.3.1.4
            ciscoMgmt.172.16.154.3.1.5
            ciscoMgmt.172.16.154.3.1.6
            ciscoMgmt.172.16.154.3.1.7
            ciscoMgmt.172.16.154.3.1.8
            ciscoMgmt.172.16.204.1
            ciscoMgmt.172.16.204.2
            cSipCfgBase.1
            cSipCfgBase.2
            cSipCfgBase.3
            cSipCfgBase.4
            cSipCfgBase.5
            cSipCfgBase.6
            cSipCfgBase.7
            cSipCfgBase.8
            cSipCfgBase.9.1.2
            cSipCfgBase.10
            cSipCfgBase.11
            cSipCfgBase.12.1.2
            cSipCfgBase.13
            cSipCfgBase.14
            cSipCfgBase.15
            cSipCfgBase.16
            cSipCfgBase.17
            cSipCfgBase.18
            cSipCfgBase.19
            cSipCfgBase.20
            cSipCfgBase.21
            cSipCfgBase.22
            cSipCfgBase.23
            cSipCfgBase.24
            cSipCfgBase.25
            cSipCfgBase.26
            cSipCfgBase.27
            cSipCfgBase.28
            cSipCfgBase.29
            cSipCfgBase.30
            cSipCfgTimer.1
            cSipCfgTimer.2
            cSipCfgTimer.3
            cSipCfgTimer.4
            cSipCfgTimer.5
            cSipCfgTimer.6
            cSipCfgTimer.7
            cSipCfgTimer.8
            cSipCfgTimer.9
            cSipCfgTimer.10
            cSipCfgTimer.11
            cSipCfgTimer.12
            cSipCfgTimer.13
            cSipCfgTimer.14
            cSipCfgTimer.15
            cSipCfgTimer.16
            cSipCfgTimer.17
            cSipCfgRetry.1
            cSipCfgRetry.2
            cSipCfgRetry.3
            cSipCfgRetry.4
            cSipCfgRetry.5
            cSipCfgRetry.6
            cSipCfgRetry.7
            cSipCfgRetry.8
            cSipCfgRetry.9
            cSipCfgRetry.10
            cSipCfgRetry.11
            cSipCfgRetry.12
            cSipCfgRetry.13
            cSipCfgRetry.14
            cSipCfgRetry.15
            cSipCfgPeer.1.1.2
            cSipCfgPeer.1.1.3
            cSipCfgPeer.1.1.4
            cSipCfgPeer.1.1.5
            cSipCfgPeer.1.1.6
            cSipCfgPeer.1.1.7
            cSipCfgPeer.1.1.8
            cSipCfgPeer.1.1.9
            cSipCfgPeer.1.1.10
            cSipCfgPeer.1.1.11
            cSipCfgPeer.1.1.12
            cSipCfgPeer.1.1.13
            cSipCfgPeer.1.1.14
            cSipCfgPeer.1.1.15
            cSipCfgPeer.1.1.16
            cSipCfgPeer.1.1.17
            cSipCfgPeer.1.1.18
            cSipCfgPeer.2
            cSipCfgPeer.3
            cSipCfgPeer.4
            cSipCfgPeer.5
            cSipCfgPeer.6
            cSipCfgPeer.7
            cSipCfgPeer.8
            cSipCfgPeer.9
            cSipCfgPeer.10
            cSipCfgPeer.11
            cSipCfgPeer.12
            cSipCfgPeer.13
            cSipCfgPeer.14
            cSipCfgStatusCauseMap.1.1.2
            cSipCfgStatusCauseMap.1.1.3
            cSipCfgStatusCauseMap.2.1.2
            cSipCfgStatusCauseMap.2.1.3
            cSipCfgAaa.1
            ciscoSipUaMIB.10.4.7.1
            ciscoSipUaMIB.10.4.7.2
            ciscoSipUaMIB.10.4.7.3
            ciscoSipUaMIB.10.4.7.4
            cSipStatsInfo.1
            cSipStatsInfo.2
            cSipStatsInfo.3
            cSipStatsInfo.4
            cSipStatsInfo.5
            cSipStatsInfo.6
            cSipStatsInfo.7
            cSipStatsInfo.8
            cSipStatsInfo.9
            cSipStatsInfo.10
            cSipStatsSuccess.1
            cSipStatsSuccess.2
            cSipStatsSuccess.3
            cSipStatsSuccess.4
            cSipStatsSuccess.5.1.2
            cSipStatsSuccess.5.1.3
            cSipStatsRedirect.1
            cSipStatsRedirect.2
            cSipStatsRedirect.3
            cSipStatsRedirect.4
            cSipStatsRedirect.5
            cSipStatsRedirect.6
            cSipStatsRedirect.7
            cSipStatsRedirect.8
            cSipStatsErrClient.1
            cSipStatsErrClient.2
            cSipStatsErrClient.3
            cSipStatsErrClient.4
            cSipStatsErrClient.5
            cSipStatsErrClient.6
            cSipStatsErrClient.7
            cSipStatsErrClient.8
            cSipStatsErrClient.9
            cSipStatsErrClient.10
            cSipStatsErrClient.11
            cSipStatsErrClient.12
            cSipStatsErrClient.13
            cSipStatsErrClient.14
            cSipStatsErrClient.15
            cSipStatsErrClient.16
            cSipStatsErrClient.17
            cSipStatsErrClient.18
            cSipStatsErrClient.19
            cSipStatsErrClient.20
            cSipStatsErrClient.21
            cSipStatsErrClient.22
            cSipStatsErrClient.23
            cSipStatsErrClient.24
            cSipStatsErrClient.25
            cSipStatsErrClient.26
            cSipStatsErrClient.27
            cSipStatsErrClient.28
            cSipStatsErrClient.29
            cSipStatsErrClient.30
            cSipStatsErrClient.31
            cSipStatsErrClient.32
            cSipStatsErrClient.33
            cSipStatsErrClient.34
            cSipStatsErrClient.35
            cSipStatsErrClient.36
            cSipStatsErrClient.37
            cSipStatsErrClient.38
            cSipStatsErrClient.39
            cSipStatsErrClient.40
            cSipStatsErrClient.41
            cSipStatsErrClient.42
            cSipStatsErrClient.43
            cSipStatsErrClient.44
            cSipStatsErrClient.45
            cSipStatsErrClient.46
            cSipStatsErrClient.47
            cSipStatsErrClient.48
            cSipStatsErrClient.49
            cSipStatsErrClient.50
            cSipStatsErrClient.51
            cSipStatsErrClient.52
            cSipStatsErrClient.53
            cSipStatsErrClient.54
            cSipStatsErrClient.55
            cSipStatsErrClient.56
            cSipStatsErrServer.1
            cSipStatsErrServer.2
            cSipStatsErrServer.3
            cSipStatsErrServer.4
            cSipStatsErrServer.5
            cSipStatsErrServer.6
            cSipStatsErrServer.7
            cSipStatsErrServer.8
            cSipStatsErrServer.9
            cSipStatsErrServer.10
            cSipStatsErrServer.11
            cSipStatsErrServer.12
            cSipStatsErrServer.13
            cSipStatsErrServer.14
            cSipStatsGlobalFail.1
            cSipStatsGlobalFail.2
            cSipStatsGlobalFail.3
            cSipStatsGlobalFail.4
            cSipStatsGlobalFail.5
            cSipStatsGlobalFail.6
            cSipStatsGlobalFail.7
            cSipStatsGlobalFail.8
            cSipStatsTraffic.1
            cSipStatsTraffic.2
            cSipStatsTraffic.3
            cSipStatsTraffic.4
            cSipStatsTraffic.5
            cSipStatsTraffic.6
            cSipStatsTraffic.7
            cSipStatsTraffic.8
            cSipStatsTraffic.9
            cSipStatsTraffic.10
            cSipStatsTraffic.11
            cSipStatsTraffic.12
            cSipStatsTraffic.13
            cSipStatsTraffic.14
            cSipStatsTraffic.15
            cSipStatsTraffic.16
            cSipStatsTraffic.17
            cSipStatsTraffic.18
            cSipStatsTraffic.19
            cSipStatsTraffic.20
            cSipStatsTraffic.21
            cSipStatsTraffic.22
            cSipStatsTraffic.23
            cSipStatsTraffic.24
            cSipStatsTraffic.25
            cSipStatsTraffic.26
            cSipStatsRetry.1
            cSipStatsRetry.2
            cSipStatsRetry.3
            cSipStatsRetry.4
            cSipStatsRetry.5
            cSipStatsRetry.6
            cSipStatsRetry.7
            cSipStatsRetry.8
            cSipStatsRetry.9
            cSipStatsRetry.10
            cSipStatsRetry.11
            cSipStatsRetry.12
            cSipStatsRetry.13
            ciscoSipUaMIB.10.9.9.1
            ciscoSipUaMIB.10.9.10.1
            ciscoSipUaMIB.10.9.10.2
            ciscoSipUaMIB.10.9.10.3
            ciscoSipUaMIB.10.9.10.4
            ciscoSipUaMIB.10.9.10.5
            ciscoSipUaMIB.10.9.10.6
            ciscoSipUaMIB.10.9.10.7
            ciscoSipUaMIB.10.9.10.8
            ciscoSipUaMIB.10.9.10.9
            ciscoSipUaMIB.10.9.10.10
            ciscoSipUaMIB.10.9.10.11
            ciscoSipUaMIB.10.9.10.12
            ciscoSipUaMIB.10.9.10.13
            ciscoSipUaMIB.10.9.10.14
            cciDescriptionEntry.1
            cciDescriptionEntry.2
            cbQosServicePolicyEntry.2
            cbQosServicePolicyEntry.3
            cbQosServicePolicyEntry.4
            cbQosServicePolicyEntry.5
            cbQosServicePolicyEntry.6
            cbQosServicePolicyEntry.7
            cbQosServicePolicyEntry.8
            cbQosVlanIndex
            cbQosServicePolicyEntry.10
            cbQosServicePolicyEntry.11
            cbQosServicePolicyEntry.12
            cbQosServicePolicyEntry.13
            cbQosServicePolicyEntry.14
            cbQosServicePolicyEntry.15
            cbQosInterfacePolicyEntry.1
            cbQosFrameRelayPolicyEntry.1
            cbQosATMPVCPolicyEntry.1
            cbQosObjectsEntry.2
            cbQosObjectsEntry.3
            cbQosObjectsEntry.4
            cbQosPolicyMapCfgEntry.1
            cbQosPolicyMapCfgEntry.2
            cbQosCMCfgEntry.1
            cbQosCMCfgEntry.2
            cbQosCMCfgEntry.3
            cbQosMatchStmtCfgEntry.1
            cbQosMatchStmtCfgEntry.2
            cbQosQueueingCfgEntry.1
            cbQosQueueingCfgEntry.2
            cbQosQueueingCfgEntry.3
            cbQosQueueingCfgEntry.4
            cbQosQueueingCfgEntry.5
            cbQosQueueingCfgEntry.6
            cbQosQueueingCfgEntry.7
            cbQosQueueingCfgEntry.8
            cbQosQueueingCfgEntry.9
            cbQosQueueingCfgEntry.10
            cbQosQueueingCfgEntry.11
            cbQosQueueingCfgEntry.12
            cbQosQueueingCfgEntry.13
            cbQosQueueingCfgEntry.14
            cbQosREDCfgEntry.1
            cbQosREDCfgEntry.2
            cbQosREDCfgEntry.3
            cbQosREDCfgEntry.4
            cbQosREDClassCfgEntry.2
            cbQosREDClassCfgEntry.3
            cbQosREDClassCfgEntry.4
            cbQosREDClassCfgEntry.5
            cbQosREDClassCfgEntry.6
            cbQosREDClassCfgEntry.7
            cbQosREDClassCfgEntry.8
            cbQosREDClassCfgEntry.9
            cbQosREDClassCfgEntry.10
            cbQosREDClassCfgEntry.11
            cbQosPoliceCfgEntry.1
            cbQosPoliceCfgEntry.2
            cbQosPoliceCfgEntry.3
            cbQosPoliceCfgEntry.4
            cbQosPoliceCfgEntry.5
            cbQosPoliceCfgEntry.6
            cbQosPoliceCfgEntry.7
            cbQosPoliceCfgEntry.8
            cbQosPoliceCfgEntry.9
            cbQosPoliceCfgEntry.10
            cbQosPoliceCfgEntry.11
            cbQosPoliceCfgEntry.12
            cbQosPoliceCfgEntry.13
            cbQosPoliceCfgEntry.14
            cbQosPoliceCfgEntry.15
            cbQosPoliceCfgEntry.16
            cbQosPoliceCfgEntry.17
            cbQosPoliceCfgEntry.18
            cbQosPoliceCfgEntry.19
            cbQosPoliceCfgEntry.20
            cbQosPoliceCfgEntry.21
            cbQosPoliceCfgEntry.22
            cbQosPoliceCfgEntry.23
            cbQosPoliceCfgEntry.24
            cbQosPoliceCfgEntry.25
            cbQosPoliceCfgEntry.26
            cbQosPoliceCfgEntry.27
            cbQosTSCfgEntry.1
            cbQosTSCfgEntry.2
            cbQosTSCfgEntry.3
            cbQosTSCfgEntry.4
            cbQosTSCfgEntry.5
            cbQosTSCfgEntry.6
            cbQosTSCfgEntry.7
            cbQosTSCfgEntry.8
            cbQosTSCfgEntry.9
            cbQosTSCfgEntry.10
            cbQosTSCfgEntry.11
            cbQosTSCfgEntry.12
            cbQosTSCfgEntry.13
            cbQosTSCfgEntry.14
            cbQosSetCfgEntry.1
            cbQosSetCfgEntry.2
            cbQosSetCfgEntry.3
            cbQosSetCfgEntry.4
            cbQosSetCfgEntry.5
            cbQosSetCfgEntry.6
            cbQosSetCfgEntry.7
            cbQosSetCfgEntry.8
            cbQosSetCfgEntry.9
            cbQosSetCfgEntry.10
            cbQosSetCfgEntry.11
            cbQosSetCfgEntry.12
            cbQosSetCfgEntry.13
            cbQosSetCfgEntry.14
            cbQosSetCfgEntry.15
            cbQosSetCfgEntry.16
            cbQosCMStatsEntry.1
            cbQosCMStatsEntry.2
            cbQosCMStatsEntry.3
            cbQosCMStatsEntry.4
            cbQosCMStatsEntry.5
            cbQosCMStatsEntry.6
            cbQosCMStatsEntry.7
            cbQosCMStatsEntry.8
            cbQosCMStatsEntry.9
            cbQosCMStatsEntry.10
            cbQosCMStatsEntry.11
            cbQosCMStatsEntry.12
            cbQosCMStatsEntry.13
            cbQosCMStatsEntry.14
            cbQosCMStatsEntry.15
            cbQosCMStatsEntry.16
            cbQosCMStatsEntry.17
            cbQosCMStatsEntry.18
            cbQosCMStatsEntry.19
            cbQosCMStatsEntry.20
            cbQosCMStatsEntry.21
            cbQosCMStatsEntry.22
            cbQosCMStatsEntry.23
            cbQosCMStatsEntry.24
            cbQosCMStatsEntry.25
            cbQosCMStatsEntry.26
            cbQosCMStatsEntry.27
            cbQosCMStatsEntry.28
            cbQosCMStatsEntry.29
            cbQosCMStatsEntry.30
            cbQosMatchStmtStatsEntry.1
            cbQosMatchStmtStatsEntry.2
            cbQosMatchStmtStatsEntry.3
            cbQosMatchStmtStatsEntry.4
            cbQosMatchStmtStatsEntry.5
            cbQosMatchStmtStatsEntry.6
            cbQosMatchStmtStatsEntry.7
            cbQosPoliceStatsEntry.1
            cbQosPoliceStatsEntry.2
            cbQosPoliceStatsEntry.3
            cbQosPoliceStatsEntry.4
            cbQosPoliceStatsEntry.5
            cbQosPoliceStatsEntry.6
            cbQosPoliceStatsEntry.7
            cbQosPoliceStatsEntry.8
            cbQosPoliceStatsEntry.9
            cbQosPoliceStatsEntry.10
            cbQosPoliceStatsEntry.11
            cbQosPoliceStatsEntry.12
            cbQosPoliceStatsEntry.13
            cbQosPoliceStatsEntry.14
            cbQosPoliceStatsEntry.15
            cbQosPoliceStatsEntry.16
            cbQosPoliceStatsEntry.17
            cbQosPoliceStatsEntry.18
            cbQosPoliceStatsEntry.19
            cbQosPoliceStatsEntry.20
            cbQosPoliceStatsEntry.21
            cbQosPoliceStatsEntry.22
            cbQosPoliceStatsEntry.23
            cbQosPoliceStatsEntry.24
            cbQosQueueingStatsEntry.1
            cbQosQueueingStatsEntry.2
            cbQosQueueingStatsEntry.3
            cbQosQueueingStatsEntry.4
            cbQosQueueingStatsEntry.5
            cbQosQueueingStatsEntry.6
            cbQosQueueingStatsEntry.7
            cbQosQueueingStatsEntry.8
            cbQosQueueingStatsEntry.9
            cbQosQueueingStatsEntry.10
            cbQosQueueingStatsEntry.11
            cbQosQueueingStatsEntry.12
            cbQosTSStatsEntry.1
            cbQosTSStatsEntry.2
            cbQosTSStatsEntry.3
            cbQosTSStatsEntry.4
            cbQosTSStatsEntry.5
            cbQosTSStatsEntry.6
            cbQosTSStatsEntry.7
            cbQosTSStatsEntry.8
            cbQosTSStatsEntry.9
            cbQosTSStatsEntry.10
            cbQosTSStatsEntry.11
            cbQosTSStatsEntry.12
            cbQosTSStatsEntry.13
            cbQosTSStatsEntry.14
            cbQosTSStatsEntry.15
            cbQosREDClassStatsEntry.1
            cbQosREDClassStatsEntry.2
            cbQosREDClassStatsEntry.3
            cbQosREDClassStatsEntry.4
            cbQosREDClassStatsEntry.5
            cbQosREDClassStatsEntry.6
            cbQosREDClassStatsEntry.7
            cbQosREDClassStatsEntry.8
            cbQosREDClassStatsEntry.9
            cbQosREDClassStatsEntry.10
            cbQosREDClassStatsEntry.11
            cbQosREDClassStatsEntry.12
            cbQosREDClassStatsEntry.13
            cbQosREDClassStatsEntry.14
            cbQosREDClassStatsEntry.15
            cbQosREDClassStatsEntry.16
            cbQosREDClassStatsEntry.17
            cbQosREDClassStatsEntry.18
            cbQosREDClassStatsEntry.19
            cbQosREDClassStatsEntry.20
            cbQosREDClassStatsEntry.21
            cbQosREDClassStatsEntry.22
            cbQosREDClassStatsEntry.23
            cbQosREDClassStatsEntry.24
            cbQosREDClassStatsEntry.25
            cbQosREDClassStatsEntry.26
            cbQosPoliceActionCfgEntry.2
            cbQosPoliceActionCfgEntry.3
            cbQosPoliceActionCfgEntry.4
            cbQosPoliceActionCfgEntry.5
            cbQosPoliceActionCfgEntry.6
            cbQosPoliceActionCfgEntry.7
            cbQosIPHCCfgEntry.1
            cbQosIPHCCfgEntry.2
            cbQosIPHCStatsEntry.1
            cbQosIPHCStatsEntry.2
            cbQosIPHCStatsEntry.3
            cbQosIPHCStatsEntry.4
            cbQosIPHCStatsEntry.5
            cbQosIPHCStatsEntry.6
            cbQosIPHCStatsEntry.7
            cbQosIPHCStatsEntry.8
            cbQosIPHCStatsEntry.9
            cbQosIPHCStatsEntry.10
            cbQosIPHCStatsEntry.11
            cbQosIPHCStatsEntry.12
            cbQosIPHCStatsEntry.13
            cbQosIPHCStatsEntry.14
            cbQosIPHCStatsEntry.15
            cbQosIPHCStatsEntry.16
            cbQosIPHCStatsEntry.17
            cbQosIPHCStatsEntry.18
            cbQosIPHCStatsEntry.19
            cbQosIPHCStatsEntry.20
            cbQosIPHCStatsEntry.21
            cbQosIPHCStatsEntry.22
            cbQosIPHCStatsEntry.23
            cbQosIPHCStatsEntry.24
            cbQosIPHCStatsEntry.25
            cbQosIPHCStatsEntry.26
            cbQosIPHCStatsEntry.27
            cbQosIPHCStatsEntry.28
            cbQosIPHCStatsEntry.29
            cbQosIPHCStatsEntry.30
            cbQosIPHCStatsEntry.31
            cbQosIPHCStatsEntry.32
            cbQosSetStatsEntry.1
            cbQosSetStatsEntry.2
            cbQosSetStatsEntry.3
            cbQosSetStatsEntry.4
            cbQosSetStatsEntry.5
            cbQosSetStatsEntry.6
            cbQosSetStatsEntry.7
            cbQosSetStatsEntry.8
            cbQosSetStatsEntry.9
            cbQosSetStatsEntry.10
            cbQosSetStatsEntry.11
            cbQosSetStatsEntry.12
            cbQosSetStatsEntry.13
            cbQosPoliceColorStatsEntry.1
            cbQosPoliceColorStatsEntry.2
            cbQosPoliceColorStatsEntry.3
            cbQosPoliceColorStatsEntry.4
            cbQosPoliceColorStatsEntry.5
            cbQosPoliceColorStatsEntry.6
            cbQosPoliceColorStatsEntry.7
            cbQosPoliceColorStatsEntry.8
            cbQosPoliceColorStatsEntry.9
            cbQosPoliceColorStatsEntry.10
            cbQosPoliceColorStatsEntry.11
            cbQosPoliceColorStatsEntry.12
            cbQosPoliceColorStatsEntry.13
            cbQosPoliceColorStatsEntry.14
            cbQosPoliceColorStatsEntry.15
            cbQosPoliceColorStatsEntry.16
            cbQosPoliceColorStatsEntry.17
            cbQosPoliceColorStatsEntry.18
            cbQosTableMapCfgEntry.2
            cbQosTableMapCfgEntry.3
            cbQosTableMapCfgEntry.4
            cbQosTableMapValueCfgEntry.2
            cbQosTableMapSetCfgEntry.1
            cbQosTableMapSetCfgEntry.2
            cbQosTableMapSetCfgEntry.3
            cbQosTableMapSetCfgEntry.4
            cbQosTableMapSetCfgEntry.5
            cbQosTableMapSetCfgEntry.6
            cbQosTableMapSetCfgEntry.7
            cbQosTableMapSetCfgEntry.8
            cbQosTableMapSetCfgEntry.9
            cbQosTableMapSetCfgEntry.10
            cbQosTableMapSetCfgEntry.11
            cbQosTableMapSetCfgEntry.12
            cbQosEBCfgEntry.1
            cbQosEBCfgEntry.2
            cbQosEBCfgEntry.3
            cbQosEBCfgEntry.4
            cbQosEBStatsEntry.1
            cbQosEBStatsEntry.2
            cbQosEBStatsEntry.3
            ciscoCBQosMIBObjects.10.4.1.1
            ciscoCBQosMIBObjects.10.4.1.2
            ciscoCBQosMIBObjects.10.69.1.3
            ciscoCBQosMIBObjects.10.69.1.4
            ciscoCBQosMIBObjects.10.69.1.5
            ciscoCBQosMIBObjects.10.136.1.1
            ciscoCBQosMIBObjects.10.205.1.1
            ciscoCBQosMIBObjects.10.205.1.2
            ciscoCBQosMIBObjects.10.205.1.3
            ciscoCBQosMIBObjects.10.205.1.4
            ciscoCBQosMIBObjects.10.205.1.5
            ciscoCBQosMIBObjects.10.205.1.6
            ciscoCBQosMIBObjects.10.205.1.7
            ciscoCBQosMIBObjects.10.205.1.8
            ciscoCBQosMIBObjects.10.205.1.9
            ciscoCBQosMIBObjects.10.205.1.10
            ciscoCBQosMIBObjects.10.205.1.11
            ciscoCBQosMIBObjects.10.205.1.12
            cntpSystem.1
            cntpSystem.2
            cntpSystem.3
            cntpSystem.4
            cntpSystem.5
            cntpSystem.6
            cntpSystem.7
            cntpSystem.8
            cntpSystem.9
            cntpSystem.10
            cntpPeersVarEntry.2
            cntpPeersVarEntry.3
            cntpPeersVarEntry.4
            cntpPeersVarEntry.5
            cntpPeersVarEntry.6
            cntpPeersVarEntry.7
            cntpPeersVarEntry.8
            cntpPeersVarEntry.9
            cntpPeersVarEntry.10
            cntpPeersVarEntry.11
            cntpPeersVarEntry.12
            cntpPeersVarEntry.13
            cntpPeersVarEntry.14
            cntpPeersVarEntry.15
            cntpPeersVarEntry.16
            cntpPeersVarEntry.17
            cntpPeersVarEntry.18
            cntpPeersVarEntry.19
            cntpPeersVarEntry.20
            cntpPeersVarEntry.21
            cntpPeersVarEntry.22
            cntpPeersVarEntry.23
            cntpPeersVarEntry.24
            cntpPeersVarEntry.25
            cntpPeersVarEntry.26
            cntpPeersVarEntry.27
            cntpPeersVarEntry.28
            cntpPeersVarEntry.29
            cntpPeersVarEntry.30
            cntpPeersVarEntry.31
            cntpFilterRegisterEntry.2
            cntpFilterRegisterEntry.3
            cntpFilterRegisterEntry.4
            cmiFaRegTotalVisitors
            cmiFaRegVisitorHomeAddress
            cmiFaRegVisitorHomeAgentAddress
            cmiFaRegVisitorTimeGranted
            cmiFaRegVisitorTimeRemaining
            cmiFaRegVisitorRegFlags
            cmiFaRegVisitorRegIDLow
            cmiFaRegVisitorRegIDHigh
            cmiFaRegVisitorRegIsAccepted
            cmiFaRegVisitorRegFlagsRev1
            cmiFaRegVisitorChallengeValue
            cmiFaInitRegRequestsReceived
            cmiFaInitRegRequestsRelayed
            cmiFaInitRegRequestsDenied
            cmiFaInitRegRequestsDiscarded
            cmiFaInitRegRepliesValidFromHA
            cmiFaInitRegRepliesValidRelayMN
            cmiFaReRegRequestsReceived
            cmiFaReRegRequestsRelayed
            cmiFaReRegRequestsDenied
            cmiFaReRegRequestsDiscarded
            cmiFaReRegRepliesValidFromHA
            cmiFaReRegRepliesValidRelayToMN
            cmiFaDeRegRequestsReceived
            cmiFaDeRegRequestsRelayed
            cmiFaDeRegRequestsDenied
            cmiFaDeRegRequestsDiscarded
            cmiFaDeRegRepliesValidFromHA
            cmiFaDeRegRepliesValidRelayToMN
            cmiFaReverseTunnelUnavailable
            cmiFaReverseTunnelBitNotSet
            cmiFaMnTooDistant
            cmiFaDeliveryStyleUnsupported
            cmiFaUnknownChallenge
            cmiFaMissingChallenge
            cmiFaStaleChallenge
            cmiFaCvsesFromMnRejected
            cmiFaCvsesFromHaRejected
            cmiFaNvsesFromMnNeglected
            cmiFaNvsesFromHaNeglected
            cmiFaTotalRegRequests
            cmiFaTotalRegReplies
            cmiFaMnFaAuthFailures
            cmiFaMnAAAAuthFailures
            cmiFaAdvertIsBusy
            cmiFaAdvertRegRequired
            cmiFaAdvertChallengeWindow
            cmiFaAdvertChallengeValue
            cmiFaRevTunnelSupported
            cmiFaChallengeSupported
            cmiFaEncapDeliveryStyleSupported
            cmiFaReverseTunnelEnable
            cmiFaChallengeEnable
            cmiFaAdvertChallengeChapSPI
            cmiFaCoaInterfaceOnly
            cmiFaCoaTransmitOnly
            cmiFaCoaRegAsymLink
            cmiHaRegTotalMobilityBindings
            cmiHaRegMnIdentifierType
            cmiHaRegMnIdentifier
            cmiHaRegMobilityBindingRegFlags
            cmiHaRegMnIfDescription
            cmiHaRegMnIfBandwidth
            cmiHaRegMnIfID
            cmiHaRegMnIfPathMetricType
            cmiHaRegServAcceptedRequests
            cmiHaRegServDeniedRequests
            cmiHaRegOverallServTime
            cmiHaRegRecentServAcceptedTime
            cmiHaRegRecentServDeniedTime
            cmiHaRegRecentServDeniedCode
            cmiHaRegTotalProcLocRegs
            cmiHaRegMaxProcLocInMinRegs
            cmiHaRegDateMaxRegsProcLoc
            cmiHaRegProcLocInLastMinRegs
            cmiHaRegTotalProcByAAARegs
            cmiHaRegMaxProcByAAAInMinRegs
            cmiHaRegDateMaxRegsProcByAAA
            cmiHaRegProcAAAInLastByMinRegs
            cmiHaRegAvgTimeRegsProcByAAA
            cmiHaRegMaxTimeRegsProcByAAA
            cmiHaRegRequestsReceived
            cmiHaRegRequestsDenied
            cmiHaRegRequestsDiscarded
            cmiHaEncapUnavailable
            cmiHaNAICheckFailures
            cmiHaInitRegRequestsReceived
            cmiHaInitRegRequestsAccepted
            cmiHaInitRegRequestsDenied
            cmiHaInitRegRequestsDiscarded
            cmiHaReRegRequestsReceived
            cmiHaReRegRequestsAccepted
            cmiHaReRegRequestsDenied
            cmiHaReRegRequestsDiscarded
            cmiHaDeRegRequestsReceived
            cmiHaDeRegRequestsAccepted
            cmiHaDeRegRequestsDenied
            cmiHaDeRegRequestsDiscarded
            cmiHaReverseTunnelUnavailable
            cmiHaReverseTunnelBitNotSet
            cmiHaEncapsulationUnavailable
            cmiHaCvsesFromMnRejected
            cmiHaCvsesFromFaRejected
            cmiHaNvsesFromMnNeglected
            cmiHaNvsesFromFaNeglected
            cmiHaMnHaAuthFailures
            cmiHaMnAAAAuthFailures
            cmiHaRedunSentBUs
            cmiHaRedunFailedBUs
            cmiHaRedunReceivedBUAcks
            cmiHaRedunTotalSentBUs
            cmiHaRedunReceivedBUs
            cmiHaRedunSentBUAcks
            cmiHaRedunSentBIReqs
            cmiHaRedunFailedBIReqs
            cmiHaRedunTotalSentBIReqs
            cmiHaRedunReceivedBIReps
            cmiHaRedunDroppedBIReps
            cmiHaRedunSentBIAcks
            cmiHaRedunReceivedBIReqs
            cmiHaRedunSentBIReps
            cmiHaRedunFailedBIReps
            cmiHaRedunTotalSentBIReps
            cmiHaRedunReceivedBIAcks
            cmiHaRedunDroppedBIAcks
            cmiHaRedunSecViolations
            cmiHaMrDynamic
            cmiHaMrStatus
            cmiHaMrMultiPath
            cmiHaMrMultiPathMetricType
            cmiHaMobNetDynamic
            cmiHaMobNetStatus
            cmiHaSystemVersion
            cmiSecAssocsCount
            cmiSecAlgorithmType
            cmiSecAlgorithmMode
            cmiSecKey
            cmiSecReplayMethod
            cmiSecStatus
            cmiSecKey2
            cmiSecTotalViolations
            cmiSecRecentViolationSPI
            cmiSecRecentViolationTime
            cmiSecRecentViolationIDLow
            cmiSecRecentViolationIDHigh
            cmiSecRecentViolationReason
            cmiMaRegMaxInMinuteRegs
            cmiMaRegDateMaxRegsReceived
            cmiMaRegInLastMinuteRegs
            cmiMaInterfaceAddressType
            cmiMaInterfaceAddress
            cmiMaAdvMaxRegLifetime
            cmiMaAdvPrefixLengthInclusion
            cmiMaAdvAddressType
            cmiMaAdvAddress
            cmiMaAdvMaxInterval
            cmiMaAdvMinInterval
            cmiMaAdvMaxAdvLifetime
            cmiMaAdvResponseSolicitationOnly
            cmiMaAdvStatus
            cmiMnAdvFlags
            cmiMnRegFlags
            cmiMrReverseTunnel
            cmiMrRedundancyGroup
            cmiMrMobNetAddrType
            cmiMrMobNetAddr
            cmiMrMobNetPfxLen
            cmiMrMobNetStatus
            cmiMrHaTunnelIfIndex
            cmiMrHAPriority
            cmiMrHABest
            cmiMRIfDescription
            cmiMrIfHoldDown
            cmiMrIfRoamPriority
            cmiMrIfSolicitPeriodic
            cmiMrIfSolicitInterval
            cmiMrIfSolicitRetransInitial
            cmiMrIfSolicitRetransMax
            cmiMrIfSolicitRetransLimit
            cmiMrIfSolicitRetransCurrent
            cmiMrIfSolicitRetransRemaining
            cmiMrIfSolicitRetransCount
            cmiMrIfCCoaAddressType
            cmiMrIfCCoaAddress
            cmiMrIfCCoaDefaultGwType
            cmiMrIfCCoaDefaultGw
            cmiMrIfCCoaRegRetry
            cmiMrIfCCoaRegRetryRemaining
            cmiMrIfStatus
            cmiMrIfCCoaRegistration
            cmiMrIfCCoaOnly
            cmiMrIfCCoaEnable
            cmiMrIfRoamStatus
            cmiMrIfRegisteredCoAType
            cmiMrIfRegisteredCoA
            cmiMrIfRegisteredMaAddrType
            cmiMrIfRegisteredMaAddr
            cmiMrIfHaTunnelIfIndex
            cmiMrIfID
            cmiMrBetterIfDetected
            cmiMrTunnelPktsRcvd
            cmiMrTunnelPktsSent
            cmiMrTunnelBytesRcvd
            cmiMrTunnelBytesSent
            cmiMrRedStateActive
            cmiMrRedStatePassive
            cmiMrCollocatedTunnel
            cmiMrMultiPath
            cmiMrMultiPathMetricType
            cmiMrMaIsHa
            cmiMrMaAdvRcvIf
            cmiMrMaIfMacAddress
            cmiMrMaAdvSequence
            cmiMrMaAdvFlags
            cmiMrMaAdvMaxRegLifetime
            cmiMrMaAdvMaxLifetime
            cmiMrMaAdvLifetimeRemaining
            cmiMrMaAdvTimeReceived
            cmiMrMaAdvTimeFirstHeard
            cmiMrMaHoldDownRemaining
            cmiMrRegExtendExpire
            cmiMrRegExtendRetry
            cmiMrRegExtendInterval
            cmiMrRegLifetime
            cmiMrRegRetransInitial
            cmiMrRegRetransMax
            cmiMrRegRetransLimit
            cmiMrRegNewHa
            cmiTrapControl
            cmiNtRegCOAType
            cmiNtRegCOA
            cmiNtRegHAAddrType
            cmiNtRegHomeAgent
            cmiNtRegHomeAddressType
            cmiNtRegHomeAddress
            cmiNtRegNAI
            cmiNtRegDeniedCode
            cRFStatusUnitId
            cRFStatusUnitState
            cRFStatusPeerUnitId
            cRFStatusPeerUnitState
            cRFStatusPrimaryMode
            cRFStatusDuplexMode
            cRFStatusManualSwactInhibit
            cRFStatusLastSwactReasonCode
            cRFStatusFailoverTime
            cRFStatusPeerStandByEntryTime
            cRFStatusRFModeCapsModeDescr
            cRFStatusIssuState
            cRFStatusIssuStateRev1
            cRFStatusIssuFromVersion
            cRFStatusIssuToVersion
            cRFStatusDomainInstanceEntry.1
            cRFStatusDomainInstanceEntry.2
            cRFStatusDomainInstanceEntry.3
            cRFStatusDomainInstanceEntry.4
            cRFCfgSplitMode
            cRFCfgKeepaliveThresh
            cRFCfgKeepaliveThreshMin
            cRFCfgKeepaliveThreshMax
            cRFCfgKeepaliveTimer
            cRFCfgKeepaliveTimerMin
            cRFCfgKeepaliveTimerMax
            cRFCfgNotifTimer
            cRFCfgNotifTimerMin
            cRFCfgNotifTimerMax
            cRFCfgAdminAction
            cRFCfgNotifsEnabled
            cRFCfgMaintenanceMode
            cRFCfgRedundancyMode
            cRFCfgRedundancyModeDescr
            cRFCfgRedundancyOperMode
            cRFHistoryTableMaxLength
            cRFHistoryPrevActiveUnitId
            cRFHistoryCurrActiveUnitId
            cRFHistorySwitchOverReason
            cRFHistorySwactTime
            cRFHistoryColdStarts
            cRFHistoryStandByAvailTime
            cpim.1
            cpim.2
            cpim.3
            cpim.4
            cpim.5
            cpim.6
            cpim.7
            cpim.8
            cpim.9
            ciscoPimMIBNotificationObjects.1
            cbgpRouteOrigin
            cbgpRouteASPathSegment
            cbgpRouteNextHop
            cbgpRouteMedPresent
            cbgpRouteMultiExitDisc
            cbgpRouteLocalPrefPresent
            cbgpRouteLocalPref
            cbgpRouteAtomicAggregate
            cbgpRouteAggregatorAS
            cbgpRouteAggregatorAddrType
            cbgpRouteAggregatorAddr
            cbgpRouteBest
            cbgpRouteUnknownAttr
            cbgpPeerPrefixAccepted
            cbgpPeerPrefixDenied
            cbgpPeerPrefixLimit
            cbgpPeerPrefixAdvertised
            cbgpPeerPrefixSuppressed
            cbgpPeerPrefixWithdrawn
            cbgpPeerEntry.7
            cbgpPeerEntry.8
            cbgpPeerCapValue
            cbgpPeerAddrFamilyName
            cbgpPeerAcceptedPrefixes
            cbgpPeerDeniedPrefixes
            cbgpPeerAddrFamilyPrefixEntry.3
            cbgpPeerAddrFamilyPrefixEntry.4
            cbgpPeerAddrFamilyPrefixEntry.5
            cbgpPeerAdvertisedPrefixes
            cbgpPeerSuppressedPrefixes
            cbgpPeerWithdrawnPrefixes
            cbgpPeer2State
            cbgpPeer2AdminStatus
            cbgpPeer2NegotiatedVersion
            cbgpPeer2LocalAddr
            cbgpPeer2LocalPort
            cbgpPeer2LocalAs
            cbgpPeer2LocalIdentifier
            cbgpPeer2RemotePort
            cbgpPeer2RemoteAs
            cbgpPeer2RemoteIdentifier
            cbgpPeer2InUpdates
            cbgpPeer2OutUpdates
            cbgpPeer2InTotalMessages
            cbgpPeer2OutTotalMessages
            cbgpPeer2LastError
            cbgpPeer2FsmEstablishedTransitions
            cbgpPeer2FsmEstablishedTime
            cbgpPeer2ConnectRetryInterval
            cbgpPeer2HoldTime
            cbgpPeer2KeepAlive
            cbgpPeer2HoldTimeConfigured
            cbgpPeer2KeepAliveConfigured
            cbgpPeer2MinASOriginationInterval
            cbgpPeer2MinRouteAdvertisementInterval
            cbgpPeer2InUpdateElapsedTime
            cbgpPeer2LastErrorTxt
            cbgpPeer2PrevState
            cbgpPeer2CapValue
            cbgpPeer2AddrFamilyName
            cbgpPeer2AcceptedPrefixes
            cbgpPeer2DeniedPrefixes
            cbgpPeer2PrefixAdminLimit
            cbgpPeer2PrefixThreshold
            cbgpPeer2PrefixClearThreshold
            cbgpPeer2AdvertisedPrefixes
            cbgpPeer2SuppressedPrefixes
            cbgpPeer2WithdrawnPrefixes
            cbgpNotifsEnable
            cbgpGlobal.2
            cPppoeSystemCurrSessions
            cPppoeSystemHighWaterSessions
            cPppoeSystemMaxAllowedSessions
            cPppoeSystemThresholdSessions
            cPppoeSystemExceededSessionErrors
            cPppoeSystemPerMACSessionlimit
            cPppoeSystemPerMACSessionIWFlimit
            cPppoeSystemPerMacThrottleRatelimit
            cPppoeSystemPerVLANlimit
            cPppoeSystemPerVLANthrottleRatelimit
            cPppoeSystemPerVClimit
            cPppoeSystemPerVCThrottleRatelimit
            cPppoeSystemSessionLossThreshold
            cPppoeSystemSessionLossPercent
            ciscoPppoeMIBObjects.10.9.1.1
            cPppoeVcCurrSessions
            cPppoeVcHighWaterSessions
            cPppoeVcMaxAllowedSessions
            cPppoeVcThresholdSessions
            cPppoeVcExceededSessionErrors
            cPppoeTotalSessions
            cPppoePtaSessions
            cPppoeFwdedSessions
            cPppoeTransSessions
            cPppoePerInterfaceSessionLossThreshold
            cPppoePerInterfaceSessionLossPercent
            cPppoeSystemSessionNotifyObjects.1
            cPppoeSystemSessionNotifyObjects.2
            cPppoeSystemSessionNotifyObjects.3
            cPppoeSystemSessionNotifyObjects.4
            cPppoeSystemSessionNotifyObjects.5
            ceExtProcessorRam
            ceExtNVRAMSize
            ceExtNVRAMUsed
            ceExtProcessorRamOverflow
            ceExtHCProcessorRam
            ceExtConfigRegister
            ceExtConfigRegNext
            ceExtSysBootImageList
            ceExtKickstartImageList
            ceExtEntityLEDColor
            ceExtEntDoorNotifEnable
            ceExtEntBreakOutPortNotifEnable
            ceExtNotificationControlObjects.3
            ceExtUSBModemIMEI
            ceExtUSBModemIMSI
            ceExtUSBModemServiceProvider
            ceExtUSBModemSignalStrength
            cempMemPoolEntry.2
            cempMemPoolEntry.3
            cempMemPoolEntry.4
            cempMemPoolEntry.5
            cempMemPoolEntry.6
            cempMemPoolEntry.7
            cempMemPoolEntry.8
            cempMemPoolEntry.9
            cempMemPoolEntry.10
            cempMemPoolEntry.17
            cempMemPoolEntry.18
            cempMemPoolEntry.19
            cempMemPoolEntry.20
            cempMemPoolEntry.21
            cempMemPoolEntry.22
            cempMemPoolEntry.23
            cempMemPoolEntry.24
            cempMemBufferPoolEntry.2
            cempMemBufferPoolEntry.3
            cempMemBufferPoolEntry.4
            cempMemBufferPoolEntry.5
            cempMemBufferPoolEntry.6
            cempMemBufferPoolEntry.7
            cempMemBufferPoolEntry.8
            cempMemBufferPoolEntry.9
            cempMemBufferPoolEntry.10
            cempMemBufferPoolEntry.11
            cempMemBufferPoolEntry.12
            cempMemBufferPoolEntry.13
            cempMemBufferPoolEntry.16
            cempMemBufferPoolEntry.17
            cempMemBufferPoolEntry.18
            cempMemBufferPoolEntry.19
            cempMemBufferPoolEntry.20
            cempMemBufferPoolEntry.21
            cempMemBufferPoolEntry.22
            cempMemBufferCachePoolEntry.1
            cempMemBufferCachePoolEntry.2
            cempMemBufferCachePoolEntry.3
            cempMemBufferCachePoolEntry.4
            cempMemBufferCachePoolEntry.5
            cempMemBufferCachePoolEntry.6
            cempMemBufferCachePoolEntry.7
            cempMIBObjects.2.1
            clagAggDistributionProtocol
            clagAggDistributionAddressMode
            clagAggProtocolType
            clagAggPortAdminStatus
            cndeMaxCollectors
            cndeCollectorStatus
            cIgmpFilterEnable
            cIgmpFilterMaxProfiles
            cIgmpFilterEndAddressType
            cIgmpFilterEndAddress
            cIgmpFilterProfileAction
            cIgmpFilterInterfaceProfileIndex
            cIgmpFilterEditSpinLock
            cIgmpFilterEditProfileIndex
            cIgmpFilterEditStartAddressType
            cIgmpFilterEditStartAddress
            cIgmpFilterEditEndAddressType
            cIgmpFilterEditEndAddress
            cIgmpFilterEditProfileAction
            cIgmpFilterEditOperation
            cIgmpFilterApplyStatus
            cnpdStatusEntry.1
            cnpdStatusEntry.2
            cnpdAllStatsEntry.2
            cnpdAllStatsEntry.3
            cnpdAllStatsEntry.4
            cnpdAllStatsEntry.5
            cnpdAllStatsEntry.6
            cnpdAllStatsEntry.7
            cnpdAllStatsEntry.8
            cnpdAllStatsEntry.9
            cnpdAllStatsEntry.10
            cnpdAllStatsEntry.11
            cnpdAllStatsEntry.12
            cnpdTopNConfigEntry.2
            cnpdTopNConfigEntry.3
            cnpdTopNConfigEntry.4
            cnpdTopNConfigEntry.5
            cnpdTopNConfigEntry.6
            cnpdTopNConfigEntry.7
            cnpdTopNConfigEntry.8
            cnpdTopNStatsEntry.2
            cnpdTopNStatsEntry.3
            cnpdTopNStatsEntry.4
            cnpdThresholdConfigEntry.2
            cnpdThresholdConfigEntry.3
            cnpdThresholdConfigEntry.4
            cnpdThresholdConfigEntry.5
            cnpdThresholdConfigEntry.6
            cnpdThresholdConfigEntry.7
            cnpdThresholdConfigEntry.8
            cnpdThresholdConfigEntry.9
            cnpdThresholdConfigEntry.10
            cnpdThresholdConfigEntry.12
            cnpdThresholdHistoryEntry.2
            cnpdThresholdHistoryEntry.3
            cnpdThresholdHistoryEntry.4
            cnpdThresholdHistoryEntry.5
            cnpdThresholdHistoryEntry.6
            cnpdThresholdHistoryEntry.7
            cnpdNotificationsConfig.1
            cnpdSupportedProtocolsEntry.2
            ceImage.1.1.2
            ceImage.1.1.3
            ceImage.1.1.4
            ceImage.1.1.5
            ceImage.1.1.6
            ceImage.1.1.7
            ceImageLocationTable.1.2
            ceImageLocationTable.1.3
            ceImageInstallableTable.1.2
            ceImageInstallableTable.1.3
            ceImageInstallableTable.1.4
            ceImageInstallableTable.1.5
            ceImageInstallableTable.1.6
            ceImageInstallableTable.1.7
            ceImageInstallableTable.1.8
            ceImageInstallableTable.1.9
            ceImageTags.1.1.2
            ceImageTags.1.1.3
            ceImageTags.1.1.4
            bcpOperEntry.1
            bcpConfigEntry.1
            bcpConfigEntry.2
            bcpConfigEntry.3
            bcpConfigEntry.4
            bcpConfigEntry.5
            bcpConfigEntry.6
            bcpConfigEntry.7
            bcpConfigEntry.8
            bcpConfigEntry.9
            bcpConfigEntry.10
            bcpConfigEntry.11
            bcpConfigEntry.12
            bcpConfigEntry.13
            bcpConfigEntry.14
            cieIfPacketStatsEntry.1
            cieIfPacketStatsEntry.2
            cieIfPacketStatsEntry.3
            cieIfPacketStatsEntry.4
            cieIfPacketStatsEntry.5
            cieIfPacketStatsEntry.6
            cieIfPacketStatsEntry.7
            cieIfPacketStatsEntry.8
            cieIfPacketStatsEntry.9
            cieIfPacketStatsEntry.10
            cieIfPacketStatsEntry.11
            cieIfPacketStatsEntry.12
            cieIfInterfaceEntry.1
            cieIfInterfaceEntry.2
            cieIfInterfaceEntry.3
            cieIfInterfaceEntry.4
            cieIfInterfaceEntry.5
            cieIfInterfaceEntry.6
            cieIfInterfaceEntry.7
            cieIfInterfaceEntry.8
            cieIfInterfaceEntry.9
            cieIfInterfaceEntry.10
            cieIfInterfaceEntry.11
            cieIfInterfaceEntry.12
            ciscoIfExtSystemConfig.1
            cieIfDot1qCustomEtherTypeEntry.1
            cieIfDot1qCustomEtherTypeEntry.2
            cieIfUtilEntry.1
            cieIfUtilEntry.2
            cieIfUtilEntry.3
            cieIfUtilEntry.4
            cieIfDot1dBaseMappingEntry.1
            cieIfNameMappingEntry.2
            caqVccParamsEntry.1
            caqVccParamsEntry.2
            caqVccParamsEntry.3
            caqVccParamsEntry.4
            caqVccParamsEntry.5
            caqVccParamsEntry.6
            caqVccParamsEntry.7
            caqVccParamsEntry.8
            caqVccParamsEntry.9
            caqVccParamsEntry.10
            caqVccParamsEntry.11
            caqVccParamsEntry.12
            caqVccParamsEntry.13
            caqVccParamsEntry.14
            caqVccParamsEntry.15
            caqVccParamsEntry.16
            caqVccParamsEntry.17
            caqVccParamsEntry.18
            caqVccParamsEntry.19
            caqVpcParamsEntry.1
            caqVpcParamsEntry.2
            caqVpcParamsEntry.3
            caqVpcParamsEntry.4
            caqVpcParamsEntry.5
            caqVpcParamsEntry.6
            caqVpcParamsEntry.7
            caqVpcParamsEntry.8
            caqVpcParamsEntry.9
            caqQueuingParamsEntry.1
            caqQueuingParamsClassEntry.2
            caqQueuingParamsClassEntry.3
            caqQueuingParamsClassEntry.4
            caqQueuingParamsClassEntry.5
            caqQueuingParamsClassEntry.6
            ccmCallHomeConfiguration.1
            ccmCallHomeConfiguration.2
            ccmCallHomeConfiguration.3
            ccmCallHomeConfiguration.4
            ccmCallHomeConfiguration.5
            ccmCallHomeConfiguration.6
            ccmCallHomeConfiguration.7
            ccmCallHomeConfiguration.8
            ccmCallHomeConfiguration.9
            ccmCallHomeConfiguration.10
            ccmCallHomeConfiguration.11
            callHomeDestProfileEntry.2
            callHomeDestProfileEntry.3
            callHomeDestProfileEntry.4
            callHomeDestProfileEntry.5
            callHomeDestProfileEntry.6
            callHomeDestProfileEntry.7
            callHomeDestProfileEntry.8
            callHomeDestProfileEntry.9
            ccmCallHomeConfiguration.13
            callHomeDestEmailAddressEntry.2
            callHomeDestEmailAddressEntry.3
            callHomeDestEmailAddressEntry.4
            callHomeDestEmailAddressEntry.5
            ccmCallHomeConfiguration.15
            ccmCallHomeConfiguration.16
            ccmCallHomeConfiguration.17
            ccmCallHomeConfiguration.18
            ccmCallHomeConfiguration.19
            ccmCallHomeConfiguration.20
            ccmCallHomeConfiguration.21
            ccmSmtpServersEntry.3
            ccmSmtpServersEntry.4
            ccmSmtpServersEntry.5
            ccmSmtpServersEntry.6
            ccmCallHomeConfiguration.23
            ccmCallHomeConfiguration.24
            callHomeAlertGroupTypeEntry.2
            callHomeAlertGroupTypeEntry.3
            callHomeAlertGroupTypeEntry.4
            callHomeSwInventoryEntry.3
            callHomeSwInventoryEntry.4
            ccmCallHomeConfiguration.27
            ccmCallHomeConfiguration.28
            ccmCallHomeConfiguration.29
            ccmSeverityAlertGroupEntry.1
            ccmPeriodicAlertGroupEntry.1
            ccmPeriodicAlertGroupEntry.2
            ccmPeriodicAlertGroupEntry.3
            ccmPeriodicAlertGroupEntry.4
            ccmPeriodicAlertGroupEntry.5
            ccmPeriodicAlertGroupEntry.6
            ccmPeriodicAlertGroupEntry.7
            ccmCallHomeAlertGroupCfg.3
            ccmPatternAlertGroupEntry.2
            ccmPatternAlertGroupEntry.3
            ccmPatternAlertGroupEntry.4
            ccmCallHomeAlertGroupCfg.5
            callHomeUserDefCmdEntry.2
            callHomeUserDefCmdEntry.3
            ccmEventAlertGroupEntry.1
            ccmEventAlertGroupEntry.2
            ccmDestProfileTestEntry.1
            ccmDestProfileTestEntry.2
            ccmDestProfileTestEntry.3
            ccmDestProfileTestEntry.4
            ccmCallHomeNotifConfig.1
            ccmPeriodicSwInventoryCfg.1
            ccmCallHomeConfiguration.34
            ccmCallHomeConfiguration.35
            ccmCallHomeConfiguration.36
            ccmCallHomeConfiguration.37
            ccmCallHomeConfiguration.38
            ccmCallHomeConfiguration.39
            ccmCallHomeConfiguration.40
            ccmCallHomeStats.1
            ccmCallHomeStats.2
            ccmCallHomeStats.3
            ccmCallHomeStats.4
            ccmEventStatsEntry.3
            ccmEventStatsEntry.4
            ccmEventStatsEntry.5
            ccmEventStatsEntry.6
            ccmEventStatsEntry.7
            ccmEventStatsEntry.8
            ccmEventStatsEntry.9
            ccmEventStatsEntry.10
            ccmEventStatsEntry.11
            ccmCallHomeStatus.1
            ccmCallHomeStatus.2
            ccmCallHomeStatus.3
            ccmSmtpServerStatusEntry.1
            ccmCallHomeStatus.5
            ccmOnDemandMsgSendControl.1
            ccmOnDemandMsgSendControl.2
            ccmOnDemandMsgSendControl.3
            ccmOnDemandMsgSendControl.4
            ccmOnDemandCliMsgControl.1
            ccmOnDemandCliMsgControl.2
            ccmOnDemandCliMsgControl.3
            ccmOnDemandCliMsgControl.4
            ccmOnDemandCliMsgControl.5
            ccmOnDemandCliMsgControl.6
            ccmSmartCallHomeActions.1
            ccmSmartCallHomeActions.2
            ccmSmartCallHomeActions.3
            ccmSmartCallHomeActions.4
            ccmSmartCallHomeActions.5
            ccmCallHomeVrf.1
            ccmCallHomeMessageSource.1
            ccmCallHomeMessageSource.2
            ccmCallHomeMessageSource.3
            ccmCallHomeDiagSignature.2
            ccmCallHomeDiagSignature.3
            ccmCallHomeDiagSignatureInfoEntry.2
            ccmCallHomeDiagSignatureInfoEntry.3
            ccmCallHomeDiagSignatureInfoEntry.4
            ccmCallHomeDiagSignatureInfoEntry.5
            ccmCallHomeDiagSignatureInfoEntry.6
            ccmCallHomeDiagSignatureInfoEntry.7
            ccmCallHomeDiagSignatureInfoEntry.8
            ccmCallHomeSecurity.1
            ccmCallHomeReporting.1
            ciscoCallHomeMIB.1.13.1
            ciscoCallHomeMIB.1.13.2
            ciscoMgmt.310.169.1.1
            ciscoMgmt.310.169.1.2
            ciscoMgmt.310.169.1.3.1.2
            ciscoMgmt.310.169.1.3.1.3
            ciscoMgmt.310.169.1.3.1.4
            ciscoMgmt.310.169.1.3.1.5
            ciscoMgmt.310.169.1.3.1.6
            ciscoMgmt.310.169.1.3.1.7
            ciscoMgmt.310.169.1.3.1.8
            ciscoMgmt.310.169.1.3.1.9
            ciscoMgmt.310.169.1.3.1.10
            ciscoMgmt.310.169.1.3.1.11
            ciscoMgmt.310.169.1.3.1.12
            ciscoMgmt.310.169.1.3.1.13
            ciscoMgmt.310.169.1.3.1.14
            ciscoMgmt.310.169.1.3.1.15
            ciscoMgmt.310.169.1.4.1.2
            ciscoMgmt.310.169.1.4.1.3
            ciscoMgmt.310.169.1.4.1.4
            ciscoMgmt.310.169.1.4.1.5
            ciscoMgmt.310.169.1.4.1.6
            ciscoMgmt.310.169.1.4.1.7
            ciscoMgmt.310.169.1.4.1.8
            ciscoMgmt.310.169.2.1.1.2
            ciscoMgmt.310.169.2.1.1.3
            ciscoMgmt.310.169.2.1.1.4
            ciscoMgmt.310.169.2.1.1.5
            ciscoMgmt.310.169.2.1.1.6
            ciscoMgmt.310.169.2.1.1.7
            ciscoMgmt.310.169.2.1.1.8
            ciscoMgmt.310.169.2.1.1.9
            ciscoMgmt.310.169.2.1.1.10
            ciscoMgmt.310.169.2.1.1.11
            ciscoMgmt.310.169.2.2.1.3
            ciscoMgmt.310.169.2.2.1.4
            ciscoMgmt.310.169.2.2.1.5
            ciscoMgmt.310.169.2.3.1.3
            ciscoMgmt.310.169.2.3.1.4
            ciscoMgmt.310.169.2.3.1.5
            ciscoMgmt.310.169.2.3.1.6
            ciscoMgmt.310.169.2.3.1.7
            ciscoMgmt.310.169.2.3.1.8
            ciscoMgmt.310.169.3.1.1.1
            ciscoMgmt.310.169.3.1.1.2
            ciscoMgmt.310.169.3.1.1.3
            ciscoMgmt.310.169.3.1.1.4
            ciscoMgmt.310.169.3.1.1.5
            ciscoMgmt.310.169.3.1.1.6
            cIpLocalPoolNotificationsEnable
            cIpLocalPoolConfigEntry.4
            cIpLocalPoolConfigEntry.5
            cIpLocalPoolConfigEntry.6
            cIpLocalPoolConfigEntry.7
            cIpLocalPoolConfigEntry.8
            cIpLocalPoolGroupContainsEntry.2
            cIpLocalPoolGroupEntry.1
            cIpLocalPoolGroupEntry.2
            cIpLocalPoolStatsEntry.1
            cIpLocalPoolStatsEntry.2
            cIpLocalPoolStatsEntry.3
            cIpLocalPoolStatsEntry.4
            cIpLocalPoolStatsEntry.5
            cIpLocalPoolAllocEntry.3
            cIpLocalPoolAllocEntry.4
            ceDiagTestInfoEntry.2
            ceDiagTestInfoEntry.3
            ceDiagTestCustomAttributeEntry.2
            ceDiagErrorInfoEntry.2
            ciscoEntityDiagMIB.1.2.1
            ceDiagEntityEntry.1
            ceDiagEntityEntry.2
            ceDiagEntityEntry.3
            ceDiagEntityEntry.4
            ceDiagEntityCurrentTestEntry.1
            ceDiagOnDemand.1
            ceDiagOnDemand.2
            ceDiagOnDemand.3
            ceDiagOnDemandJobEntry.1
            ceDiagOnDemandJobEntry.2
            ceDiagOnDemandJobEntry.3
            ceDiagOnDemandJobEntry.4
            ceDiagScheduledJobEntry.2
            ceDiagScheduledJobEntry.3
            ceDiagScheduledJobEntry.4
            ceDiagScheduledJobEntry.5
            ceDiagScheduledJobEntry.6
            ceDiagScheduledJobEntry.7
            ceDiagScheduledJobEntry.8
            ceDiagTestPerfEntry.1
            ceDiagTestPerfEntry.2
            ceDiagTestPerfEntry.3
            ceDiagTestPerfEntry.4
            ceDiagTestPerfEntry.5
            ceDiagTestPerfEntry.6
            ceDiagTestPerfEntry.7
            ceDiagTestPerfEntry.8
            ceDiagTestPerfEntry.9
            ceDiagTestPerfEntry.10
            ceDiagHealthMonitor.1
            ceDiagHMTestEntry.1
            ceDiagHMTestEntry.2
            ceDiagHMTestEntry.3
            ceDiagHMTestEntry.4
            ceDiagHMTestEntry.5
            ceDiagHMTestEntry.6
            ceDiagHMTestEntry.7
            ceDiagHMTestEntry.8
            ceDiagEvents.1
            ceDiagEvents.2
            ceDiagEvents.3
            ceDiagEventQueryEntry.2
            ceDiagEventQueryEntry.3
            ceDiagEventQueryEntry.4
            ceDiagEventQueryEntry.5
            ceDiagEventQueryEntry.6
            ceDiagEventResultEntry.2
            ceDiagEventResultEntry.3
            ceDiagEventResultEntry.4
            ceDiagEventResultEntry.5
            ceDiagEventResultEntry.6
            ceDiagNotificationControl.1
            ceDiagNotificationControl.2
            ceDiagNotificationControl.3
            ceDiagNotificationControl.4
            cnfCIInterfaceEntry.1
            cnfCIInterfaceEntry.2
            cnfCICacheEntry.2
            cnfCICacheEntry.3
            cnfCICacheEntry.4
            cnfCICacheEntry.5
            cnfCICacheEntry.6
            cnfCICacheEntry.7
            cnfCICacheEntry.8
            cnfCICacheEntry.9
            cnfCIBridgedFlowStatsCtrlEntry.2
            cnfCIBridgedFlowStatsCtrlEntry.3
            cnfCacheInfo.4
            cnfEIExportInfoEntry.1
            cnfEIExportInfoEntry.2
            cnfEIExportInfoEntry.3
            cnfEIExportInfoEntry.4
            cnfExportInfo.2
            cnfEICollectorEntry.4
            cnfExportStatistics.1
            cnfExportStatistics.2
            cnfExportStatistics.3
            cnfExportStatistics.4
            cnfExportStatistics.5
            cnfExportStatistics.6
            cnfProtocolStatistics.1
            cnfProtocolStatistics.2
            cnfPSProtocolStatEntry.2
            cnfPSProtocolStatEntry.3
            cnfPSProtocolStatEntry.4
            cnfPSProtocolStatEntry.5
            cnfPSProtocolStatEntry.6
            cnfExportTemplate.1
            cnfTemplateEntry.2
            cnfTemplateEntry.3
            cnfTemplateEntry.4
            cnfTemplateExportInfoEntry.1
            cnfTemplateExportInfoEntry.2
            cnfTemplateExportInfoEntry.3
            cnfTemplateExportInfoEntry.4
            cnfTemplateExportInfoEntry.5
            ciscoNetflowMIB.1.7.1
            ciscoNetflowMIB.1.7.2
            ciscoNetflowMIB.1.7.3
            ciscoNetflowMIB.1.7.4
            ciscoNetflowMIB.1.7.5
            ciscoNetflowMIB.1.7.6
            ciscoNetflowMIB.1.7.7
            ciscoNetflowMIB.10.64.8.1.2
            ciscoNetflowMIB.10.64.8.1.3
            ciscoNetflowMIB.10.64.8.1.4
            ciscoNetflowMIB.10.64.8.1.5
            ciscoNetflowMIB.10.64.8.1.6
            ciscoNetflowMIB.10.64.8.1.7
            ciscoNetflowMIB.10.64.8.1.8
            ciscoNetflowMIB.10.64.8.1.9
            ciscoNetflowMIB.10.64.8.1.10
            ciscoNetflowMIB.10.64.8.1.11
            ciscoNetflowMIB.10.64.8.1.12
            ciscoNetflowMIB.10.64.8.1.13
            ciscoNetflowMIB.10.64.8.1.14
            ciscoNetflowMIB.10.64.8.1.15
            ciscoNetflowMIB.10.64.8.1.16
            ciscoNetflowMIB.10.64.8.1.17
            ciscoNetflowMIB.10.64.8.1.18
            ciscoNetflowMIB.10.64.8.1.19
            ciscoNetflowMIB.10.64.8.1.20
            ciscoNetflowMIB.10.64.8.1.21
            ciscoNetflowMIB.10.64.8.1.22
            ciscoNetflowMIB.10.64.8.1.23
            ciscoNetflowMIB.10.64.8.1.24
            ciscoNetflowMIB.10.64.8.1.25
            ciscoNetflowMIB.10.64.8.1.26
            ciscoNetflowMIB.1.7.9
            ciscoNetflowMIB.1.7.10
            ciscoNetflowMIB.1.7.11
            ciscoNetflowMIB.1.7.12
            ciscoNetflowMIB.1.7.13
            ciscoNetflowMIB.1.7.14
            ciscoNetflowMIB.1.7.15
            ciscoNetflowMIB.1.7.16
            ciscoNetflowMIB.1.7.17
            ciscoNetflowMIB.1.7.18
            ciscoNetflowMIB.1.7.19
            ciscoNetflowMIB.1.7.20
            ciscoNetflowMIB.1.7.21
            ciscoNetflowMIB.1.7.22
            ciscoNetflowMIB.1.7.23
            ciscoNetflowMIB.1.7.24
            ciscoNetflowMIB.1.7.25
            ciscoNetflowMIB.1.7.26
            ciscoNetflowMIB.1.7.27
            ciscoNetflowMIB.1.7.28
            ciscoNetflowMIB.1.7.29
            ciscoNetflowMIB.1.7.30
            ciscoNetflowMIB.1.7.31
            ciscoNetflowMIB.1.7.32
            ciscoNetflowMIB.1.7.33
            ciscoNetflowMIB.1.7.34
            ciscoNetflowMIB.1.7.35
            ciscoNetflowMIB.1.7.36
            ciscoNetflowMIB.1.7.37
            ciscoNetflowMIB.1.7.38
            ciscoMgmt.410.169.1.1
            ciscoMgmt.410.169.1.2
            ciscoMgmt.410.169.2.1.1
            cqvTerminationPeEncap
            cqvTerminationRowStatus
            cqvTranslationEntry.3
            cqvTranslationEntry.4
            cqvTranslationEntry.5
            cqvTranslationEntry.6
            cqvTranslationEntry.7
            cEigrpVpnName
            cEigrpNbrCount
            cEigrpHellosSent
            cEigrpHellosRcvd
            cEigrpUpdatesSent
            cEigrpUpdatesRcvd
            cEigrpQueriesSent
            cEigrpQueriesRcvd
            cEigrpRepliesSent
            cEigrpRepliesRcvd
            cEigrpAcksSent
            cEigrpAcksRcvd
            cEigrpInputQHighMark
            cEigrpInputQDrops
            cEigrpSiaQueriesSent
            cEigrpSiaQueriesRcvd
            cEigrpAsRouterIdType
            cEigrpAsRouterId
            cEigrpTopoRoutes
            cEigrpHeadSerial
            cEigrpNextSerial
            cEigrpXmitPendReplies
            cEigrpXmitDummies
            cEigrpActive
            cEigrpStuckInActive
            cEigrpDestSuccessors
            cEigrpFdistance
            cEigrpRouteOriginType
            cEigrpRouteOriginAddrType
            cEigrpRouteOriginAddr
            cEigrpNextHopAddressType
            cEigrpNextHopAddress
            cEigrpNextHopInterface
            cEigrpDistance
            cEigrpReportDistance
            cEigrpTopoEntry.17
            cEigrpTopoEntry.18
            cEigrpTopoEntry.19
            cEigrpPeerAddrType
            cEigrpPeerAddr
            cEigrpPeerIfIndex
            cEigrpHoldTime
            cEigrpUpTime
            cEigrpSrtt
            cEigrpRto
            cEigrpPktsEnqueued
            cEigrpLastSeq
            cEigrpVersion
            cEigrpRetrans
            cEigrpRetries
            cEigrpPeerCount
            cEigrpXmitReliableQ
            cEigrpXmitUnreliableQ
            cEigrpMeanSrtt
            cEigrpPacingReliable
            cEigrpPacingUnreliable
            cEigrpMFlowTimer
            cEigrpPendingRoutes
            cEigrpHelloInterval
            cEigrpXmitNextSerial
            cEigrpUMcasts
            cEigrpRMcasts
            cEigrpUUcasts
            cEigrpRUcasts
            cEigrpMcastExcepts
            cEigrpCRpkts
            cEigrpAcksSuppressed
            cEigrpRetransSent
            cEigrpOOSrvcd
            cEigrpAuthMode
            cEigrpAuthKeyChain
            cipUrpfDropRateWindow
            cipUrpfComputeInterval
            cipUrpfDropNotifyHoldDownTime
            cipUrpfDrops
            cipUrpfDropRate
            cipUrpfIfDrops
            cipUrpfIfSuppressedDrops
            cipUrpfIfDropRate
            cipUrpfIfDiscontinuityTime
            cipUrpfVrfIfDrops
            cipUrpfVrfIfDiscontinuityTime
            cipUrpfIfDropRateNotifyEnable
            cipUrpfIfNotifyDropRateThreshold
            cipUrpfIfNotifyDrHoldDownReset
            cipUrpfIfCheckStrict
            cipUrpfIfWhichRouteTableID
            cipUrpfIfVrfName
            cipUrpfVrfName
            cEtherCfmMaxEventIndex
            cEtherCfmEventDomainName
            cEtherCfmEventType
            cEtherCfmEventLastChange
            cEtherCfmEventServiceId
            cEtherCfmEventLclMepid
            cEtherCfmEventLclMacAddress
            cEtherCfmEventLclMepCount
            cEtherCfmEventLclIfCount
            cEtherCfmEventRmtMepid
            cEtherCfmEventRmtMacAddress
            cEtherCfmEventRmtPortState
            cEtherCfmEventRmtServiceId
            cEtherCfmEventCode
            cEtherCfmEventDeleteRow
            cContextMappingEntry.2
            cContextMappingEntry.3
            cContextMappingEntry.4
            cContextMappingEntry.5
            cContextMappingEntry.6
            cContextMappingMIBObjects.2.1.1
            cContextMappingMIBObjects.2.1.2
            cContextMappingMIBObjects.2.1.3
            cufwConnGlobalNumAttempted
            cufwConnGlobalNumSetupsAborted
            cufwConnGlobalNumPolicyDeclined
            cufwConnGlobalNumResDeclined
            cufwConnGlobalNumHalfOpen
            cufwConnGlobalNumActive
            cufwConnGlobalNumExpired
            cufwConnGlobalNumAborted
            cufwConnGlobalNumEmbryonic
            cufwConnGlobalConnSetupRate1
            cufwConnGlobalConnSetupRate5
            cufwConnGlobalNumRemoteAccess
            cufwConnResMemoryUsage
            cufwConnResActiveConnMemoryUsage
            cufwConnResHOConnMemoryUsage
            cufwConnResEmbrConnMemoryUsage
            cufwConnReptAppStats
            cufwConnReptAppStatsLastChanged
            cufwConnNumAttempted
            cufwConnNumSetupsAborted
            cufwConnNumPolicyDeclined
            cufwConnNumResDeclined
            cufwConnNumHalfOpen
            cufwConnNumActive
            cufwConnNumAborted
            cufwConnSetupRate1
            cufwConnSetupRate5
            cufwAppConnNumAttempted
            cufwAppConnNumSetupsAborted
            cufwAppConnNumPolicyDeclined
            cufwAppConnNumResDeclined
            cufwAppConnNumHalfOpen
            cufwAppConnNumActive
            cufwAppConnNumAborted
            cufwAppConnSetupRate1
            cufwAppConnSetupRate5
            cufwPolConnNumAttempted
            cufwPolConnNumSetupsAborted
            cufwPolConnNumPolicyDeclined
            cufwPolConnNumResDeclined
            cufwPolConnNumHalfOpen
            cufwPolConnNumActive
            cufwPolConnNumAborted
            cufwPolAppConnNumAttempted
            cufwPolAppConnNumSetupsAborted
            cufwPolAppConnNumPolicyDeclined
            cufwPolAppConnNumResDeclined
            cufwPolAppConnNumHalfOpen
            cufwPolAppConnNumActive
            cufwPolAppConnNumAborted
            cufwAIAuditTrailEnabled
            cufwAIAlertEnabled
            cufwInspectionStatus
            cufwUrlfFunctionEnabled
            cufwUrlfRequestsNumProcessed
            cufwUrlfRequestsProcRate1
            cufwUrlfRequestsProcRate5
            cufwUrlfRequestsNumAllowed
            cufwUrlfRequestsNumDenied
            cufwUrlfRequestsDeniedRate1
            cufwUrlfRequestsDeniedRate5
            cufwUrlfRequestsNumCacheAllowed
            cufwUrlfRequestsNumCacheDenied
            cufwUrlfAllowModeReqNumAllowed
            cufwUrlfAllowModeReqNumDenied
            cufwUrlfRequestsNumResDropped
            cufwUrlfRequestsResDropRate1
            cufwUrlfRequestsResDropRate5
            cufwUrlfNumServerTimeouts
            cufwUrlfNumServerRetries
            cufwUrlfResponsesNumLate
            cufwUrlfUrlAccRespsNumResDropped
            cufwUrlfResTotalRequestCacheSize
            cufwUrlfResTotalRespCacheSize
            cufwUrlfServerVendor
            cufwUrlfServerStatus
            cufwUrlfServerReqsNumProcessed
            cufwUrlfServerReqsNumAllowed
            cufwUrlfServerReqsNumDenied
            cufwUrlfServerNumTimeouts
            cufwUrlfServerNumRetries
            cufwUrlfServerRespsNumReceived
            cufwUrlfServerRespsNumLate
            cufwUrlfServerAvgRespTime1
            cufwUrlfServerAvgRespTime5
            cufwAaicGlobalNumBadProtocolOps
            cufwAaicGlobalNumBadPDUSize
            cufwAaicGlobalNumBadPortRange
            cufwAaicHttpNumBadProtocolOps
            cufwAaicHttpNumBadPDUSize
            cufwAaicHttpNumTunneledConns
            cufwAaicHttpNumLargeURIs
            cufwAaicHttpNumBadContent
            cufwAaicHttpNumMismatchContent
            cufwAaicHttpNumDoubleEncodedPkts
            cufwL2GlobalEnableStealthMode
            cufwL2GlobalArpCacheSize
            cufwL2GlobalEnableArpInspection
            cufwL2GlobalNumArpRequests
            cufwL2GlobalNumIcmpRequests
            cufwL2GlobalNumFloods
            cufwL2GlobalNumDrops
            cufwL2GlobalArpOverflowRate5
            cufwL2GlobalNumBadArpResponses
            cufwL2GlobalNumSpoofedArpResps
            cufwCntlUrlfServerStatusChange
            cufwCntlL2StaticMacAddressMoved
            cefFIBSummaryFwdPrefixes
            cefPrefixForwardingInfo
            cefPrefixPkts
            cefPrefixHCPkts
            cefPrefixBytes
            cefPrefixHCBytes
            cefPrefixInternalNRPkts
            cefPrefixInternalNRHCPkts
            cefPrefixInternalNRBytes
            cefPrefixInternalNRHCBytes
            cefPrefixExternalNRPkts
            cefPrefixExternalNRHCPkts
            cefPrefixExternalNRBytes
            cefPrefixExternalNRHCBytes
            cefLMPrefixSpinLock
            cefLMPrefixState
            cefLMPrefixAddr
            cefLMPrefixLen
            cefLMPrefixRowStatus
            cefPathType
            cefPathInterface
            cefPathNextHopAddr
            cefPathRecurseVrfName
            cefAdjSummaryComplete
            cefAdjSummaryIncomplete
            cefAdjSummaryFixup
            cefAdjSummaryRedirect
            cefAdjSource
            cefAdjEncap
            cefAdjFixup
            cefAdjMTU
            cefAdjForwardingInfo
            cefAdjPkts
            cefAdjHCPkts
            cefAdjBytes
            cefAdjHCBytes
            cefFESelectionSpecial
            cefFESelectionLabels
            cefFESelectionAdjLinkType
            cefFESelectionAdjInterface
            cefFESelectionAdjNextHopAddrType
            cefFESelectionAdjNextHopAddr
            cefFESelectionAdjConnId
            cefFESelectionVrfName
            cefFESelectionWeight
            cefCfgAdminState
            cefCfgOperState
            cefCfgDistributionAdminState
            cefCfgDistributionOperState
            cefCfgAccountingMap
            cefCfgLoadSharingAlgorithm
            cefCfgLoadSharingID
            cefCfgTrafficStatsLoadInterval
            cefCfgTrafficStatsUpdateRate
            cefResourceMemoryUsed
            cefResourceFailureReason
            cefIntSwitchingState
            cefIntLoadSharing
            cefIntNonrecursiveAccouting
            cefPeerOperState
            cefPeerNumberOfResets
            cefPeerFIBOperState
            cefCCGlobalAutoRepairEnabled
            cefCCGlobalAutoRepairDelay
            cefCCGlobalAutoRepairHoldDown
            cefCCGlobalErrorMsgEnabled
            cefCCGlobalFullScanAction
            cefCCGlobalFullScanStatus
            cefCCEnabled
            cefCCCount
            cefCCPeriod
            cefCCQueriesSent
            cefCCQueriesIgnored
            cefCCQueriesChecked
            cefCCQueriesIterated
            cefInconsistencyPrefixType
            cefInconsistencyPrefixAddr
            cefInconsistencyPrefixLen
            cefInconsistencyVrfName
            cefInconsistencyCCType
            cefInconsistencyEntity
            cefInconsistencyReason
            entLastInconsistencyDetectTime
            cefInconsistencyReset
            cefInconsistencyResetStatus
            cefStatsPrefixQueries
            cefStatsPrefixHCQueries
            cefStatsPrefixInserts
            cefStatsPrefixHCInserts
            cefStatsPrefixDeletes
            cefStatsPrefixHCDeletes
            cefStatsPrefixElements
            cefStatsPrefixHCElements
            cefSwitchingPath
            cefSwitchingDrop
            cefSwitchingHCDrop
            cefSwitchingPunt
            cefSwitchingHCPunt
            cefSwitchingPunt2Host
            cefSwitchingHCPunt2Host
            cefResourceFailureNotifEnable
            cefPeerStateChangeNotifEnable
            cefPeerFIBStateChangeNotifEnable
            cefNotifThrottlingInterval
            cefInconsistencyNotifEnable
            cermScalarsGlobalPolicyName
            cermResOwnerName
            cermResOwnerMeasurementUnit
            cermResOwnerThreshIsConfigurable
            cermResOwnerResUserCount
            cermResOwnerResGroupCount
            cermResOwnerSubTypeName
            cermResOwnerSubTypeUsagePct
            cermResOwnerSubTypeUsage
            cermResOwnerSubTypeMaxUsage
            cermResOwnerSubTypeGlobNotifSeverity
            cermResOwnerSubTypeRisingThresh
            cermResOwnerSubTypeRisingInterval
            cermResOwnerSubTypeFallingThresh
            cermResOwnerSubTypeFallingInterval
            cermResUserTypeName
            cermResUserTypeResOwnerCount
            cermResUserTypeResUserCount
            cermResUserTypeResGroupCount
            cermResUserName
            cermResUserPriority
            cermResUserResGroupId
            cermResGroupName
            cermResGroupUserInstanceCount
            cermResGroupResUserId
            cermResUserOrGroupFlag
            cermResUserOrGroupUsagePct
            cermResUserOrGroupUsage
            cermResUserOrGroupMaxUsage
            cermResUserOrGroupNotifSeverity
            cermResUserOrGroupGlobNotifSeverity
            cermResUserOrGroupThreshFlag
            cermResUserOrGroupRisingThresh
            cermResUserOrGroupRisingInterval
            cermResUserOrGroupFallingThresh
            cermResUserOrGroupFallingInterval
            cermResUserTypeResOwnerId
            cermResMonitorName
            cermResMonitorResPolicyName
            cermResMonitorPolicyName
            cermPolicyIsGlobal
            cermPolicyUserTypeName
            cermPolicyLoggingEnabled
            cermPolicySnmpNotifEnabled
            cermPolicyStorageType
            cermPolicyRowStatus
            cermPolicyRisingThreshold
            cermPolicyRisingInterval
            cermPolicyFallingThreshold
            cermPolicyFallingInterval
            cermPolicyResOwnerThreshStorageType
            cermPolicyResOwnerThreshRowStatus
            cermConfigResGroupUserTypeName
            cermConfigResGroupStorageType
            cermConfigResGroupRowStatus
            cermConfigResGroupUserStorageType
            cermConfigResGroupUserRowStatus
            cermPolicyApplyPolicyName
            cermPolicyApplyStorageType
            cermPolicyApplyRowStatus
            cermNotifsThresholdSeverity
            cermNotifsThresholdIsUserGlob
            cermNotifsThresholdValue
            cermNotifsDirection
            cermNotifsPolicyName
            cermNotifsEnabled
            ccbptPolicyIdNext
            ccbptTargetTable.1.6
            ccbptTargetTable.1.7
            ccbptTargetTable.1.8
            ccbptTargetTable.1.9
            ccbptTargetTable.1.10
            ccbptTargetTableLastChange
            crttMonIPEchoAdminTargetAddrType
            crttMonIPEchoAdminTargetAddress
            crttMonIPEchoAdminSourceAddrType
            crttMonIPEchoAdminSourceAddress
            crttMonIPEchoAdminNameServerAddrType
            crttMonIPEchoAdminNameServerAddress
            crttMonIPEchoAdminLSPSelAddrType
            crttMonIPEchoAdminLSPSelAddress
            crttMonIPEchoAdminDscp
            crttMonIPEchoAdminFlowLabel
            crttMonIPLatestRttOperAddressType
            crttMonIPLatestRttOperAddress
            crttMonIPEchoPathAdminHopAddrType
            crttMonIPEchoPathAdminHopAddress
            crttMonIPStatsCollectAddressType
            crttMonIPStatsCollectAddress
            crttMonIPLpdGrpStatsTargetPEAddrType
            crttMonIPLpdGrpStatsTargetPEAddr
            crttMonIPHistoryCollectionAddrType
            crttMonIPHistoryCollectionAddress
            cipslaPercentileRTT
            cipslaPercentileOWSD
            cipslaPercentileOWDS
            cipslaPercentileJitterSD
            cipslaPercentileJitterDS
            cipslaPercentileJitterAvg
            cipslaPercentileLatestMin
            cipslaPercentileLatestMax
            cipslaPercentileLatestAvg
            cipslaPercentileLatestNum
            cipslaPercentileLatestSum
            cipslaPercentileLatestSum2
            ipslaEthernetGrpCtrlStatus
            ipslaEthernetGrpCtrlStorageType
            ipslaEthernetGrpCtrlRttType
            ipslaEthernetGrpCtrlOwner
            ipslaEthernetGrpCtrlTag
            ipslaEthernetGrpCtrlThreshold
            ipslaEthernetGrpCtrlTimeout
            ipslaEthernetGrpCtrlProbeList
            ipslaEthernetGrpCtrlVLAN
            ipslaEthernetGrpCtrlDomainNameType
            ipslaEthernetGrpCtrlDomainName
            ipslaEthernetGrpCtrlReqDataSize
            ipslaEthernetGrpCtrlMPIDExLst
            ipslaEthernetGrpCtrlCOS
            ipslaEthernetGrpCtrlInterval
            ipslaEthernetGrpCtrlNumFrames
            ipslaEthernetGrpScheduleRttStartTime
            ipslaEthernetGrpSchedulePeriod
            ipslaEthernetGrpScheduleFrequency
            ipslaEthernetGrpCtrlEntry.21
            ipslaEthernetGrpCtrlEntry.22
            ipslaEthernetGrpReactStatus
            ipslaEthernetGrpReactStorageType
            ipslaEthernetGrpReactVar
            ipslaEthernetGrpReactThresholdType
            ipslaEthernetGrpReactThresholdRising
            ipslaEthernetGrpReactThresholdFalling
            ipslaEthernetGrpReactThresholdCountX
            ipslaEthernetGrpReactThresholdCountY
            ipslaEthernetGrpReactActionType
            ipslaEtherJAggMeasuredCmpletions
            ipslaEtherJAggMeasuredOvThrshlds
            ipslaEtherJAggMeasuredNumRTTs
            ipslaEtherJAggMeasuredRTTSums
            ipslaEtherJAggMeasuredRTTSum2Ls
            ipslaEtherJAggMeasuredRTTSum2Hs
            ipslaEtherJAggMeasuredRTTMin
            ipslaEtherJAggMeasuredRTTMax
            ipslaEtherJAggMeasuredMinPosSD
            ipslaEtherJAggMeasuredMaxPosSD
            ipslaEtherJAggMeasuredNumPosSDs
            ipslaEtherJAggMeasuredSumPosSDs
            ipslaEtherJAggMeasuredSum2PSDLs
            ipslaEtherJAggMeasuredSum2PSDHs
            ipslaEtherJAggMeasuredMinNegSD
            ipslaEtherJAggMeasuredMaxNegSD
            ipslaEtherJAggMeasuredNumNegSDs
            ipslaEtherJAggMeasuredSumNegSDs
            ipslaEtherJAggMeasuredSum2NSDLs
            ipslaEtherJAggMeasuredSum2NSDHs
            ipslaEtherJAggMeasuredMinPosDS
            ipslaEtherJAggMeasuredMaxPosDS
            ipslaEtherJAggMeasuredNumPosDSes
            ipslaEtherJAggMeasuredSumPosDSes
            ipslaEtherJAggMeasuredSum2PDSLs
            ipslaEtherJAggMeasuredSum2PDSHs
            ipslaEtherJAggMeasuredMinNegDS
            ipslaEtherJAggMeasuredMaxNegDS
            ipslaEtherJAggMeasuredNumNegDSes
            ipslaEtherJAggMeasuredSumNegDSes
            ipslaEtherJAggMeasuredSum2NDSLs
            ipslaEtherJAggMeasuredSum2NDSHs
            ipslaEtherJAggMeasuredFrmLossSDs
            ipslaEtherJAggMeasuredFrmLssDSes
            ipslaEtherJAggMeasuredFrmOutSeqs
            ipslaEtherJAggMeasuredFrmMIAes
            ipslaEtherJAggMeasuredFrmSkippds
            ipslaEtherJAggMeasuredErrors
            ipslaEtherJAggMeasuredBusies
            ipslaEtherJAggMeasuredOWSumSDs
            ipslaEtherJAggMeasuredOWSum2SDLs
            ipslaEtherJAggMeasuredOWSum2SDHs
            ipslaEtherJAggMeasuredOWMinSD
            ipslaEtherJAggMeasuredOWMaxSD
            ipslaEtherJAggMeasuredOWSumDSes
            ipslaEtherJAggMeasuredOWSum2DSLs
            ipslaEtherJAggMeasuredOWSum2DSHs
            ipslaEtherJAggMeasuredOWMinDS
            ipslaEtherJAggMeasuredOWMaxDS
            ipslaEtherJAggMeasuredNumOWs
            ipslaEtherJAggMeasuredAvgJ
            ipslaEtherJAggMeasuredAvgJSD
            ipslaEtherJAggMeasuredAvgJDS
            ipslaEtherJAggMinSucFrmLoss
            ipslaEtherJAggMaxSucFrmLoss
            ipslaEtherJAggMeasuredIAJOut
            ipslaEtherJAggMeasuredIAJIn
            ipslaEtherJAggMeasuredFrmLateAs
            ipslaEtherJAggMeasuredFrmUnPrcds
            ipslaEtherJAggMeasuredMaxPosTW
            ipslaEtherJAggMeasuredMaxNegTW
            ipslaEtherJAggMeasuredMinPosTW
            ipslaEtherJAggMeasuredMinNegTW
            ipslaEtherJAggMeasuredTxFrmsSD
            ipslaEtherJAggMeasuredTxFrmsDS
            ipslaEtherJAggMeasuredRxFrmsSD
            ipslaEtherJAggMeasuredRxFrmsDS
            ipslaEtherJAggMeasuredMinLossNumeratorSD
            ipslaEtherJAggMeasuredMinLossDenominatorSD
            ipslaEtherJAggMeasuredMaxLossNumeratorSD
            ipslaEtherJAggMeasuredMaxLossDenominatorSD
            ipslaEtherJAggMeasuredAvgLossNumeratorSD
            ipslaEtherJAggMeasuredAvgLossDenominatorSD
            ipslaEtherJAggMeasuredMinLossNumeratorDS
            ipslaEtherJAggMeasuredMinLossDenominatorDS
            ipslaEtherJAggMeasuredMaxLossNumeratorDS
            ipslaEtherJAggMeasuredMaxLossDenominatorDS
            ipslaEtherJAggMeasuredAvgLossNumeratorDS
            ipslaEtherJAggMeasuredAvgLossDenominatorDS
            ipslaEtherJAggMeasuredCumulativeLossNumeratorSD
            ipslaEtherJAggMeasuredCumulativeLossDenominatorSD
            ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorSD
            ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorSD
            ipslaEtherJAggMeasuredCumulativeLossNumeratorDS
            ipslaEtherJAggMeasuredCumulativeLossDenominatorDS
            ipslaEtherJAggMeasuredCumulativeAvgLossNumeratorDS
            ipslaEtherJAggMeasuredCumulativeAvgLossDenominatorDS
            ipslaEtherJAggMeasuredNumOverThresh
            ipslaEtherJitterLatestNumRTT
            ipslaEtherJitterLatestRTTSum
            ipslaEtherJitterLatestRTTSum2
            ipslaEtherJitterLatestRTTMin
            ipslaEtherJitterLatestRTTMax
            ipslaEtherJitterLatestMinPosSD
            ipslaEtherJitterLatestMaxPosSD
            ipslaEtherJitterLatestNumPosSD
            ipslaEtherJitterLatestSumPosSD
            ipslaEtherJitterLatestSum2PosSD
            ipslaEtherJitterLatestMinNegSD
            ipslaEtherJitterLatestMaxNegSD
            ipslaEtherJitterLatestNumNegSD
            ipslaEtherJitterLatestSumNegSD
            ipslaEtherJitterLatestSum2NegSD
            ipslaEtherJitterLatestMinPosDS
            ipslaEtherJitterLatestMaxPosDS
            ipslaEtherJitterLatestNumPosDS
            ipslaEtherJitterLatestSumPosDS
            ipslaEtherJitterLatestSum2PosDS
            ipslaEtherJitterLatestMinNegDS
            ipslaEtherJitterLatestMaxNegDS
            ipslaEtherJitterLatestNumNegDS
            ipslaEtherJitterLatestSumNegDS
            ipslaEtherJitterLatestSum2NegDS
            ipslaEtherJitterLatestFrmLossSD
            ipslaEtherJitterLatestFrmLossDS
            ipslaEtherJitterLatestFrmOutSeq
            ipslaEtherJitterLatestFrmMIA
            ipslaEtherJitterLatestFrmSkipped
            ipslaEtherJitterLatestSense
            ipslaEtherJitterLatestFrmLateA
            ipslaEtherJitterLatestMinSucFrmL
            ipslaEtherJitterLatestMaxSucFrmL
            ipslaEtherJitterLatestOWSumSD
            ipslaEtherJitterLatestOWSum2SD
            ipslaEtherJitterLatestOWMinSD
            ipslaEtherJitterLatestOWMaxSD
            ipslaEtherJitterLatestOWSumDS
            ipslaEtherJitterLatestOWSum2DS
            ipslaEtherJitterLatestOWMinDS
            ipslaEtherJitterLatestOWMaxDS
            ipslaEtherJitterLatestNumOW
            ipslaEtherJitterLatestAvgJitter
            ipslaEtherJitterLatestAvgSDJ
            ipslaEtherJitterLatestAvgDSJ
            ipslaEtherJitterLatestOWAvgSD
            ipslaEtherJitterLatestOWAvgDS
            ipslaEtherJitterLatestIAJOut
            ipslaEtherJitterLatestIAJIn
            ipslaEtherJLatestFrmUnProcessed
            ipslaEtherJitterLatestNumOverThresh
            cevcMaxNumEvcs
            cevcNumCfgEvcs
            cevcPortMode
            cevcPortMaxNumEVCs
            cevcPortMaxNumServiceInstances
            cevcUniIdentifier
            cevcUniPortType
            cevcUniServiceAttributes
            cevcPortL2ControlProtocolAction
            cevcUniCEVlanEvcEndingVlan
            cevcEvcRowStatus
            cevcEvcStorageType
            cevcEvcIdentifier
            cevcEvcType
            cevcEvcCfgUnis
            cevcEvcOperStatus
            cevcEvcActiveUnis
            cevcEvcUniId
            cevcEvcUniOperStatus
            cevcEvcLocalUniIfIndex
            cevcSIRowStatus
            cevcSIStorageType
            cevcSITargetType
            cevcSITarget
            cevcSIName
            cevcSIEvcIndex
            cevcSIAdminStatus
            cevcSIForwardingType
            cevcSICreationType
            cevcSIType
            cevcSIOperStatus
            cevcSIVlanRewriteRowStatus
            cevcSIVlanRewriteStorageType
            cevcSIVlanRewriteAction
            cevcSIVlanRewriteEncapsulation
            cevcSIVlanRewriteVlan1
            cevcSIVlanRewriteVlan2
            cevcSIVlanRewriteSymmetric
            cevcSIL2ControlProtocolAction
            cevcSICEVlanRowStatus
            cevcSICEVlanStorageType
            cevcSICEVlanEndingVlan
            cevcSIMatchRowStatus
            cevcSIMatchStorageType
            cevcSIMatchCriteriaType
            cevcSIMatchEncapRowStatus
            cevcSIMatchEncapStorageType
            cevcSIMatchEncapValid
            cevcSIMatchEncapEncapsulation
            cevcSIMatchEncapPrimaryCos
            cevcSIMatchEncapSecondaryCos
            cevcSIMatchEncapPayloadType
            cevcSIMatchEncapPayloadTypes
            cevcSIMatchEncapPriorityCos
            cevcSIPrimaryVlanRowStatus
            cevcSIPrimaryVlanStorageType
            cevcSIPrimaryVlanEndingVlan
            cevcSISecondaryVlanRowStatus
            cevcSISecondaryVlanStorageType
            cevcSISecondaryVlanEndingVlan
            cevcSIForwardBdRowStatus
            cevcSIForwardBdStorageType
            cevcSIForwardBdNumber
            cevcSIForwardBdNumberBase
            cevcSIForwardBdNumber1kBitmap
            cevcSIForwardBdNumber2kBitmap
            cevcSIForwardBdNumber3kBitmap
            cevcSIForwardBdNumber4kBitmap
            cevcEvcNotifyEnabled
            cevcMacAddress
            cevcMaxMacConfigLimit
            cevcSIID
            cevcViolationCause
            cipslaAutoGroupDescription
            cipslaAutoGroupDestEndPointName
            cipslaAutoGroupType
            cipslaAutoGroupOperTemplateName
            cipslaAutoGroupSchedulerId
            cipslaAutoGroupQoSEnable
            cipslaAutoGroupOperType
            cipslaAutoGroupStorageType
            cipslaAutoGroupRowStatus
            cipslaBaseEndPointDescription
            cipslaBaseEndPointStorageType
            cipslaBaseEndPointRowStatus
            cipslaIPEndPointStorageType
            cipslaIPEndPointRowStatus
            cipslaIPEndPointADDestPort
            cipslaIPEndPointADMeasureRetry
            cipslaIPEndPointADDestIPAgeout
            cipslaIPEndPointADStorageType
            cipslaIPEndPointADRowStatus
            cipslaReactVar
            cipslaReactThresholdType
            cipslaReactActionType
            cipslaReactThresholdRising
            cipslaReactThresholdFalling
            cipslaReactThresholdCountX
            cipslaReactThresholdCountY
            cipslaReactStorageType
            cipslaReactRowStatus
            cipslaAutoGroupSchedPeriod
            cipslaAutoGroupSchedInterval
            cipslaAutoGroupSchedLife
            cipslaAutoGroupSchedAgeout
            cipslaAutoGroupSchedMaxInterval
            cipslaAutoGroupSchedMinInterval
            cipslaAutoGroupSchedStartTime
            cipslaAutoGroupSchedStorageType
            cipslaAutoGroupSchedRowStatus
            ciscoMgmt.610.21.1.1.2
            ciscoMgmt.610.21.1.1.3
            ciscoMgmt.610.21.1.1.4
            ciscoMgmt.610.21.1.1.5
            ciscoMgmt.610.21.1.1.6
            ciscoMgmt.610.21.1.1.7
            ciscoMgmt.610.21.1.1.8
            ciscoMgmt.610.21.1.1.9
            ciscoMgmt.610.21.1.1.10
            ciscoMgmt.610.21.1.1.11
            ciscoMgmt.610.21.1.1.12
            ciscoMgmt.610.21.1.1.13
            ciscoMgmt.610.21.1.1.14
            ciscoMgmt.610.21.1.1.15
            ciscoMgmt.610.21.1.1.16
            ciscoMgmt.610.21.1.1.17
            ciscoMgmt.610.21.1.1.18
            ciscoMgmt.610.21.1.1.19
            ciscoMgmt.610.21.1.1.20
            ciscoMgmt.610.21.1.1.21
            ciscoMgmt.610.21.1.1.22
            ciscoMgmt.610.21.1.1.23
            ciscoMgmt.610.21.1.1.24
            ciscoMgmt.610.21.1.1.25
            ciscoMgmt.610.21.1.1.26
            ciscoMgmt.610.21.1.1.27
            ciscoMgmt.610.21.1.1.28
            ciscoMgmt.610.21.1.1.30
            ciscoMgmt.610.21.2.1.2
            ciscoMgmt.610.21.2.1.3
            ciscoMgmt.610.21.2.1.4
            ciscoMgmt.610.21.2.1.5
            ciscoMgmt.610.21.2.1.6
            ciscoMgmt.610.21.2.1.7
            ciscoMgmt.610.21.2.1.8
            ciscoMgmt.610.21.2.1.9
            ciscoMgmt.610.21.2.1.10
            ciscoMgmt.610.21.2.1.11
            ciscoMgmt.610.21.2.1.12
            ciscoMgmt.610.21.2.1.13
            ciscoMgmt.610.21.2.1.14
            ciscoMgmt.610.21.2.1.15
            ciscoMgmt.610.21.2.1.16
            ciscoMgmt.610.94.1.1.2
            ciscoMgmt.610.94.1.1.3
            ciscoMgmt.610.94.1.1.4
            ciscoMgmt.610.94.1.1.5
            ciscoMgmt.610.94.1.1.6
            ciscoMgmt.610.94.1.1.7
            ciscoMgmt.610.94.1.1.8
            ciscoMgmt.610.94.1.1.9
            ciscoMgmt.610.94.1.1.10
            ciscoMgmt.610.94.1.1.11
            ciscoMgmt.610.94.1.1.12
            ciscoMgmt.610.94.1.1.13
            ciscoMgmt.610.94.1.1.14
            ciscoMgmt.610.94.1.1.15
            ciscoMgmt.610.94.1.1.16
            ciscoMgmt.610.94.1.1.17
            ciscoMgmt.610.94.1.1.18
            ciscoMgmt.610.94.2.1.2
            ciscoMgmt.610.94.2.1.3
            ciscoMgmt.610.94.2.1.4
            ciscoMgmt.610.94.2.1.5
            ciscoMgmt.610.94.2.1.6
            ciscoMgmt.610.94.2.1.7
            ciscoMgmt.610.94.2.1.8
            ciscoMgmt.610.94.2.1.9
            ciscoMgmt.610.94.2.1.10
            ciscoMgmt.610.94.2.1.11
            ciscoMgmt.610.94.2.1.12
            ciscoMgmt.610.94.2.1.13
            ciscoMgmt.610.94.2.1.14
            ciscoMgmt.610.94.2.1.15
            ciscoMgmt.610.94.2.1.16
            ciscoMgmt.610.94.2.1.17
            ciscoMgmt.610.94.2.1.18
            ciscoMgmt.610.94.2.1.19
            ciscoMgmt.610.94.2.1.20
            ciscoMgmt.610.94.3.1.2
            ciscoMgmt.610.94.3.1.3
            ciscoMgmt.610.94.3.1.4
            ciscoMgmt.610.94.3.1.5
            ciscoMgmt.610.94.3.1.6
            ciscoMgmt.610.94.3.1.7
            ciscoMgmt.610.94.3.1.8
            ciscoMgmt.610.94.3.1.9
            ciscoMgmt.610.94.3.1.10
            ciscoMgmt.610.94.3.1.11
            ciscoMgmt.610.94.3.1.12
            ciscoMgmt.610.94.3.1.13
            ciscoMgmt.610.94.3.1.14
            ciscoMgmt.610.94.3.1.15
            ciscoMgmt.610.94.3.1.16
            ciscoMgmt.610.94.3.1.17
            ciscoMgmt.610.94.3.1.18
            ciscoMgmt.610.94.3.1.19
            coiIfControllerLoopback
            coiIfControllerWavelength
            coiIfControllerLaserAdminStatus
            coiIfControllerLaserOperStatus
            coiIfControllerOtnStatus
            coiIfControllerFECMode
            coiIfControllerTDCOperMode
            coiIfControllerTDCOperStatus
            coiIfControllerTDCOperSetting
            coiIfControllerPreFECBERMantissa
            coiIfControllerPreFECBERExponent
            coiIfControllerQFactor
            coiIfControllerQMargin
            coiIfControllerOTNValidIntervals
            coiIfControllerFECValidIntervals
            coiOtnIfOTUStatus
            coiOtnIfODUStatus
            coiOtnNearEndThreshValue
            coiOtnNearEndThreshStorageType
            coiOtnNearEndThreshStatus
            coiOtnFarEndThreshValue
            coiOtnFarEndThreshStorageType
            coiOtnFarEndThreshStatus
            coiOtnNearEndCurrentFCs
            coiOtnNearEndCurrentESs
            coiOtnNearEndCurrentSESs
            coiOtnNearEndCurrentUASs
            coiOtnNearEndCurrentBBEs
            coiOtnNearEndCurrentESRs
            coiOtnNearEndCurrentSESRs
            coiOtnNearEndCurrentBBERs
            coiOtnFarEndCurrentFCs
            coiOtnFarEndCurrentESs
            coiOtnFarEndCurrentSESs
            coiOtnFarEndCurrentUASs
            coiOtnFarEndCurrentBBEs
            coiOtnFarEndCurrentESRs
            coiOtnFarEndCurrentSESRs
            coiOtnFarEndCurrentBBERs
            coiOtnNearEndIntervalFCs
            coiOtnNearEndIntervalESs
            coiOtnNearEndIntervalSESs
            coiOtnNearEndIntervalUASs
            coiOtnNearEndIntervalBBEs
            coiOtnNearEndIntervalESRs
            coiOtnNearEndIntervalSESRs
            coiOtnNearEndIntervalBBERs
            coiOtnNearEndIntervalValidData
            coiOtnFarEndIntervalFCs
            coiOtnFarEndIntervalESs
            coiOtnFarEndIntervalSESs
            coiOtnFarEndIntervalUASs
            coiOtnFarEndIntervalBBEs
            coiOtnFarEndIntervalESRs
            coiOtnFarEndIntervalSESRs
            coiOtnFarEndIntervalBBERs
            coiOtnFarEndIntervalValidData
            coiOtnIfNotifEnabled
            coiFECThreshValue
            coiFECThreshStorageType
            coiFECThreshStatus
            coiFECCurrentCorBitErrs
            coiFECCurrentCorByteErrs
            coiFECCurrentDetZeroErrs
            coiFECCurrentDetOneErrs
            coiFECCurrentUncorWords
            coiFECIntervalCorBitErrs
            coiFECIntervalCorByteErrs
            coiFECIntervalDetZeroErrs
            coiFECIntervalDetOneErrs
            coiFECIntervalUncorWords
            coiFECIntervalValidData
            ceeDot3PauseExtAdminMode
            ceeDot3PauseExtOperMode
            ceeSubInterfaceCount
            csbCallStatsInstancePhysicalIndex
            csbCallStatsSbcName
            csbCallStatsCallsHigh
            csbCallStatsRate1Sec
            csbCallStatsCallsLow
            csbCallStatsAvailableFlows
            csbCallStatsUsedFlows
            csbCallStatsPeakFlows
            csbCallStatsTotalFlows
            csbCallStatsUsedSigFlows
            csbCallStatsPeakSigFlows
            csbCallStatsTotalSigFlows
            csbCallStatsAvailablePktRate
            csbCallStatsUnclassifiedPkts
            csbCallStatsRTPPktsSent
            csbCallStatsRTPPktsRcvd
            csbCallStatsRTPPktsDiscard
            csbCallStatsRTPOctetsSent
            csbCallStatsRTPOctetsRcvd
            csbCallStatsRTPOctetsDiscard
            csbCallStatsNoMediaCount
            csbCallStatsRouteErrors
            csbCallStatsAvailableTranscodeFlows
            csbCallStatsActiveTranscodeFlows
            csbCallStatsPeakTranscodeFlows
            csbCallStatsTotalTranscodeFlows
            csbCurrPeriodicStatsActiveCalls
            csbCurrPeriodicStatsActivatingCalls
            csbCurrPeriodicStatsDeactivatingCalls
            csbCurrPeriodicStatsTotalCallAttempts
            csbCurrPeriodicStatsFailedCallAttempts
            csbCurrPeriodicStatsCallRoutingFailure
            csbCurrPeriodicStatsCallResourceFailure
            csbCurrPeriodicStatsCallMediaFailure
            csbCurrPeriodicStatsCallSigFailure
            csbCurrPeriodicStatsActiveCallFailure
            csbCurrPeriodicStatsCongestionFailure
            csbCurrPeriodicStatsCallSetupPolicyFailure
            csbCurrPeriodicStatsCallSetupNAPolicyFailure
            csbCurrPeriodicStatsCallSetupRoutingPolicyFailure
            csbCurrPeriodicStatsCallSetupCACPolicyFailure
            csbCurrPeriodicStatsCallSetupCACCallLimitFailure
            csbCurrPeriodicStatsCallSetupCACRateLimitFailure
            csbCurrPeriodicStatsCallSetupCACBandwidthFailure
            csbCurrPeriodicStatsCallSetupCACMediaLimitFailure
            csbCurrPeriodicStatsCallSetupCACMediaUpdateFailure
            csbCurrPeriodicStatsTimestamp
            csbCurrPeriodicStatsTranscodedCalls
            csbCurrPeriodicStatsTransratedCalls
            csbCurrPeriodicStatsTotalCallUpdateFailure
            csbCurrPeriodicStatsActiveIpv6Calls
            csbCurrPeriodicStatsActiveEmergencyCalls
            csbCurrPeriodicStatsActiveE2EmergencyCalls
            csbCurrPeriodicStatsImsRxActiveCalls
            csbCurrPeriodicStatsImsRxCallSetupFaiures
            csbCurrPeriodicStatsImsRxCallRenegotiationAttempts
            csbCurrPeriodicStatsImsRxCallRenegotiationFailures
            csbCurrPeriodicStatsAudioTranscodedCalls
            csbCurrPeriodicStatsFaxTranscodedCalls
            csbCurrPeriodicStatsRtpDisallowedFailures
            csbCurrPeriodicStatsSrtpDisallowedFailures
            csbCurrPeriodicStatsNonSrtpCalls
            csbCurrPeriodicStatsSrtpNonIwCalls
            csbCurrPeriodicStatsSrtpIwCalls
            csbCurrPeriodicStatsDtmfIw2833Calls
            csbCurrPeriodicStatsDtmfIwInbandCalls
            csbCurrPeriodicStatsDtmfIw2833InbandCalls
            csbCurrPeriodicStatsTotalTapsRequested
            csbCurrPeriodicStatsTotalTapsSucceeded
            csbCurrPeriodicStatsCurrentTaps
            csbCurrPeriodicIpsecCalls
            csbHistoryStatsActiveCalls
            csbHistoryStatsTotalCallAttempts
            csbHistoryStatsFailedCallAttempts
            csbHistoryStatsCallRoutingFailure
            csbHistoryStatsCallResourceFailure
            csbHistoryStatsCallMediaFailure
            csbHistoryStatsFailSigFailure
            csbHistoryStatsActiveCallFailure
            csbHistoryStatsCongestionFailure
            csbHistoryStatsCallSetupPolicyFailure
            csbHistoryStatsCallSetupNAPolicyFailure
            csbHistoryStatsCallSetupRoutingPolicyFailure
            csbHistoryStatsCallSetupCACPolicyFailure
            csbHistoryStatsCallSetupCACCallLimitFailure
            csbHistoryStatsCallSetupCACRateLimitFailure
            csbHistoryStatsCallSetupCACBandwidthFailure
            csbHistoryStatsCallSetupCACMediaLimitFailure
            csbHistoryStatsCallSetupCACMediaUpdateFailure
            csbHistoryStatsTimestamp
            csbHistroyStatsTranscodedCalls
            csbHistroyStatsTransratedCalls
            csbHistoryStatsTotalCallUpdateFailure
            csbHistoryStatsActiveIpv6Calls
            csbHistoryStatsActiveEmergencyCalls
            csbHistoryStatsActiveE2EmergencyCalls
            csbHistoryStatsImsRxActiveCalls
            csbHistoryStatsImsRxCallSetupFailures
            csbHistoryStatsImsRxCallRenegotiationAttempts
            csbHistoryStatsImsRxCallRenegotiationFailures
            csbHistoryStatsAudioTranscodedCalls
            csbHistoryStatsFaxTranscodedCalls
            csbHistoryStatsRtpDisallowedFailures
            csbHistoryStatsSrtpDisallowedFailures
            csbHistoryStatsNonSrtpCalls
            csbHistoryStatsSrtpNonIwCalls
            csbHistoryStatsSrtpIwCalls
            csbHistoryStatsDtmfIw2833Calls
            csbHistoryStatsDtmfIwInbandCalls
            csbHistoryStatsDtmfIw2833InbandCalls
            csbHistoryStatsTotalTapsRequested
            csbHistoryStatsTotalTapsSucceeded
            csbHistoryStatsCurrentTaps
            csbHistoryStatsIpsecCalls
            csbPerFlowStatsFlowType
            csbPerFlowStatsRTPPktsSent
            csbPerFlowStatsRTPPktsRcvd
            csbPerFlowStatsRTPPktsDiscard
            csbPerFlowStatsRTPOctetsSent
            csbPerFlowStatsRTPOctetsRcvd
            csbPerFlowStatsRTPOctetsDiscard
            csbPerFlowStatsRTCPPktsSent
            csbPerFlowStatsRTCPPktsRcvd
            csbPerFlowStatsRTCPPktsLost
            csbPerFlowStatsEPJitter
            csbPerFlowStatsTmanPerMbs
            csbPerFlowStatsTmanPerSdr
            csbPerFlowStatsDscpSettings
            csbPerFlowStatsAdrStatus
            csbPerFlowStatsQASettings
            csbPerFlowStatsRTPPktsLost
            csbH248StatsRequestsSent
            csbH248StatsRequestsRcvd
            csbH248StatsRequestsFailed
            csbH248StatsRequestsRetried
            csbH248StatsRepliesSent
            csbH248StatsRepliesRcvd
            csbH248StatsRepliesRetried
            csbH248StatsSegPktsSent
            csbH248StatsSegPktsRcvd
            csbH248StatsEstablishedTime
            csbH248StatsTMaxTimeoutVal
            csbH248StatsRTT
            csbH248StatsLT
            csbH248StatsRequestsSentRev1
            csbH248StatsRequestsRcvdRev1
            csbH248StatsRequestsFailedRev1
            csbH248StatsRequestsRetriedRev1
            csbH248StatsRepliesSentRev1
            csbH248StatsRepliesRcvdRev1
            csbH248StatsRepliesRetriedRev1
            csbH248StatsSegPktsSentRev1
            csbH248StatsSegPktsRcvdRev1
            csbH248StatsEstablishedTimeRev1
            csbH248StatsTMaxTimeoutValRev1
            csbH248StatsRTTRev1
            csbH248StatsLTRev1
            csbSourceAlertNotifEnabled
            csbBlackListNotifEnabled
            csbAdjacencyStatusNotifEnabled
            csbServiceStateNotifEnabled
            csbCongestionAlarmNotifEnabled
            csbSLAViolationNotifEnabled
            csbRadiusConnectionStatusNotifEnabled
            csbDiameterConnectionStatusNotifEnabled
            csbH248ControllerStatusNotifEnabled
            csbSLAViolationNotifEnabledRev1
            ciscoSessBorderCtrlrMIBObjects.73
            ciscoSessBorderCtrlrMIBObjects.74
            ciscoSessBorderCtrlrMIBObjects.75
            ciscoSessBorderCtrlrMIBObjects.76
            ciscoSessBorderCtrlrMIBObjects.77
            ciscoSessBorderCtrlrMIBObjects.78
            ciscoSessBorderCtrlrMIBObjects.79
            cneClientStatRedirectRx
            cneServerStatRedirectTx
            cneNotifEnable
            cfmFlowMonitorDescr
            cfmFlowMonitorCaps
            cfmFlowMonitorFlowCount
            cfmFlowMonitorConditionsProfile
            cfmFlowMonitorConditions
            cfmFlowMonitorAlarms
            cfmFlowMonitorAlarmSeverity
            cfmFlowMonitorAlarmCriticalCount
            cfmFlowMonitorAlarmMajorCount
            cfmFlowMonitorAlarmMinorCount
            cfmFlowMonitorAlarmWarningCount
            cfmFlowMonitorAlarmInfoCount
            cfmFlowMonitorTableChanged
            cfmFlowDescr
            cfmFlowNext
            cfmFlowCreateTime
            cfmFlowDiscontinuityTime
            cfmFlowExpirationTime
            cfmFlowDirection
            cfmFlowAdminStatus
            cfmFlowOperStatus
            cfmFlowIngressType
            cfmFlowIngress
            cfmFlowEgressType
            cfmFlowEgress
            cfmFlowTableChanged
            cfmFlowL2VlanNext
            cfmFlowL2VlanId
            cfmFlowL2VlanCos
            cfmFlowL2InnerVlanId
            cfmFlowL2InnerVlanCos
            cfmFlowL2VlanTableChanged
            cfmFlowIpNext
            cfmFlowIpAddrType
            cfmFlowIpAddrSrc
            cfmFlowIpAddrDst
            cfmFlowIpValid
            cfmFlowIpTrafficClass
            cfmFlowIpHopLimit
            cfmFlowIpEntry.8
            cfmFlowIpEntry.9
            cfmFlowIpEntry.10
            cfmFlowIpTableChanged
            cfmFlowUdpNext
            cfmFlowUdpPortSrc
            cfmFlowUdpPortDst
            cfmFlowUdpTableChanged
            cfmFlowTcpNext
            cfmFlowTcpPortSrc
            cfmFlowTcpPortDst
            cfmFlowTcpTableChanged
            cfmFlowRtpNext
            cfmFlowRtpVersion
            cfmFlowRtpSsrc
            cfmFlowRtpPayloadType
            cfmFlowRtpTableChanged
            cfmFlows.13.1.1
            cfmFlows.13.1.2
            cfmFlows.13.1.3
            cfmFlows.13.1.4
            cfmFlows.13.1.5
            cfmFlows.13.1.6
            cfmFlows.13.1.7
            cfmFlows.13.1.8
            cfmFlows.14
            cfmFlowMetricsCollected
            cfmFlowMetricsIntervalTime
            cfmFlowMetricsMaxIntervals
            cfmFlowMetricsElapsedTime
            cfmFlowMetricsIntervals
            cfmFlowMetricsInvalidIntervals
            cfmFlowMetricsConditionsProfile
            cfmFlowMetricsConditions
            cfmFlowMetricsAlarms
            cfmFlowMetricsAlarmSeverity
            cfmFlowMetricsPkts
            cfmFlowMetricsOctets
            cfmFlowMetricsBitRateUnits
            cfmFlowMetricsBitRate
            cfmFlowMetricsPktRate
            cfmFlowMetricsErrorSecsScale
            cfmFlowMetricsErrorSecsPrecision
            cfmFlowMetricsErrorSecs
            cfmFlowMetricsTransportAvailabilityScale
            cfmFlowMetricsTransportAvailabilityPrecision
            cfmFlowMetricsTransportAvailability
            cfmFlowMetricsEntry.22
            cfmFlowMetricsEntry.23
            cfmFlowMetricsEntry.24
            cfmFlowMetricsEntry.25
            cfmFlowMetricsEntry.26
            cfmFlowMetricsEntry.27
            cfmFlowMetricsEntry.28
            cfmFlowMetricsEntry.29
            cfmFlowMetricsTableChanged
            cfmFlowMetricsIntValid
            cfmFlowMetricsIntTime
            cfmFlowMetricsIntConditions
            cfmFlowMetricsIntAlarms
            cfmFlowMetricsIntAlarmSeverity
            cfmFlowMetricsIntPkts
            cfmFlowMetricsIntOctets
            cfmFlowMetricsIntBitRateUnits
            cfmFlowMetricsIntBitRate
            cfmFlowMetricsIntPktRate
            cfmFlowMetricsIntErrorSecsScale
            cfmFlowMetricsIntErrorSecsPrecision
            cfmFlowMetricsIntErrorSecs
            cfmFlowMetricsIntTransportAvailabilityScale
            cfmFlowMetricsIntTransportAvailabilityPrecision
            cfmFlowMetricsIntTransportAvailability
            cfmFlowMetricsIntEntry.18
            cfmFlowMetricsIntEntry.19
            cfmFlowMetricsIntEntry.20
            cfmFlowMetricsIntEntry.21
            cfmFlowMetricsIntEntry.22
            cfmFlowMetricsIntEntry.23
            cfmFlowMetricsIntEntry.24
            cfmFlowMetricsIntEntry.25
            cfmFlowMetricsIntEntry.26
            cfmFlowMetricsIntEntry.27
            cfmFlowMetricsIntEntry.28
            cfmConditionDescr
            cfmConditionMonitoredElement
            cfmConditionType
            cfmConditionThreshRiseScale
            cfmConditionThreshRisePrecision
            cfmConditionThreshRise
            cfmConditionThreshFallScale
            cfmConditionThreshFallPrecision
            cfmConditionThreshFall
            cfmConditionSampleType
            cfmConditionSampleWindow
            cfmConditionAlarm
            cfmConditionAlarmActions
            cfmConditionAlarmSeverity
            cfmConditionAlarmGroup
            cfmConditionTableChanged
            cfmAlarmGroupDescr
            cfmAlarmGroupConditionsProfile
            cfmAlarmGroupConditionId
            cfmAlarmGroupFlowSet
            cfmAlarmGroupFlowCount
            cfmAlarmGroupThresholdUnits
            cfmAlarmGroupThreshold
            cfmAlarmGroupRaised
            cfmAlarmGroupCurrentCount
            cfmAlarmGroupTableChanged
            cfmAlarmGroupFlowId
            cfmAlarmGroupFlowTableChanged
            cfmAlarmHistorySize
            cfmAlarmHistoryLastId
            cfmAlarmHistoryType
            cfmAlarmHistoryEntity
            cfmAlarmHistoryConditionsProfile
            cfmAlarmHistoryConditionId
            cfmAlarmHistorySeverity
            cfmAlarmHistoryTime
            cfmNotifyEnable
            cfmIpCbrMetricsCfgRateType
            cfmIpCbrMetricsCfgBitRate
            cfmIpCbrMetricsCfgRate
            cfmIpCbrMetricsCfgMediaPktSize
            cfmIpCbrMetricsValid
            cfmIpCbrMetricsLostPkts
            cfmIpCbrMetricsMrvScale
            cfmIpCbrMetricsMrvPrecision
            cfmIpCbrMetricsMrv
            cfmIpCbrMetricsEntry.10
            cfmIpCbrMetricsEntry.11
            cfmIpCbrMetricsEntry.12
            cfmIpCbrMetricsEntry.13
            cfmIpCbrMetricsEntry.14
            cfmIpCbrMetricsEntry.15
            cfmIpCbrMetricsTableChanged
            cfmIpCbrMetricsIntValid
            cfmIpCbrMetricsIntLostPkts
            cfmIpCbrMetricsIntVbMin
            cfmIpCbrMetricsIntVbMax
            cfmIpCbrMetricsIntMrUnits
            cfmIpCbrMetricsIntMr
            cfmIpCbrMetricsIntDfScale
            cfmIpCbrMetricsIntDfPrecision
            cfmIpCbrMetricsIntDf
            cfmIpCbrMetricsIntMrvScale
            cfmIpCbrMetricsIntMrvPrecision
            cfmIpCbrMetricsIntMrv
            cfmIpCbrMetricsIntEntry.13
            cfmIpCbrMetricsIntEntry.14
            cfmIpCbrMetricsIntEntry.15
            cfmIpCbrMetricsIntEntry.16
            cfmIpCbrMetricsIntEntry.17
            cfmIpCbrMetricsIntEntry.18
            cfmMdiMetricsCfgRateType
            cfmMdiMetricsCfgBitRate
            cfmMdiMetricsCfgRate
            cfmMdiMetricsCfgMediaPktSize
            cfmMdiMetricsValid
            cfmMdiMetricsLostPkts
            cfmMdiMetricsMlrScale
            cfmMdiMetricsMlrPrecision
            cfmMdiMetricsMlr
            cfmMdiMetricsEntry.10
            cfmMdiMetricsTableChanged
            cfmMdiMetricsIntValid
            cfmMdiMetricsIntLostPkts
            cfmMdiMetricsIntVbMin
            cfmMdiMetricsIntVbMax
            cfmMdiMetricsIntMrUnits
            cfmMdiMetricsIntMr
            cfmMdiMetricsIntDfScale
            cfmMdiMetricsIntDfPrecision
            cfmMdiMetricsIntDf
            cfmMdiMetricsIntMlrScale
            cfmMdiMetricsIntMlrPrecision
            cfmMdiMetricsIntMlr
            cfmMdiMetricsIntEntry.13
            cfmRtpMetricsValid
            cfmRtpMetricsExpectedPkts
            cfmRtpMetricsLostPkts
            cfmRtpMetricsFracScale
            cfmRtpMetricsFracPrecision
            cfmRtpMetricsFrac
            cfmRtpMetricsLIs
            cfmRtpMetricsAvgLDScale
            cfmRtpMetricsAvgLDPrecision
            cfmRtpMetricsAvgLD
            cfmRtpMetricsAvgLossDistance
            cfmRtpMetricsJitterScale
            cfmRtpMetricsJitterPrecision
            cfmRtpMetricsJitter
            cfmRtpMetricsMaxJitterScale
            cfmRtpMetricsMaxJitterPrecision
            cfmRtpMetricsMaxJitter
            cfmRtpMetricsEntry.18
            cfmRtpMetricsEntry.19
            cfmRtpMetricsEntry.20
            cfmRtpMetricsEntry.21
            cfmRtpMetricsEntry.22
            cfmRtpMetricsEntry.23
            cfmRtpMetricsEntry.24
            cfmRtpMetricsEntry.25
            cfmRtpMetricsEntry.26
            cfmRtpMetricsEntry.27
            cfmRtpMetricsEntry.28
            cfmRtpMetricsEntry.29
            cfmRtpMetricsEntry.30
            cfmRtpMetricsEntry.31
            cfmRtpMetricsTableChanged
            cfmRtpMetricsIntValid
            cfmRtpMetricsIntExpectedPkts
            cfmRtpMetricsIntLostPkts
            cfmRtpMetricsIntFracScale
            cfmRtpMetricsIntFracPrecision
            cfmRtpMetricsIntFrac
            cfmRtpMetricsIntLIs
            cfmRtpMetricsIntAvgLDScale
            cfmRtpMetricsIntAvgLDPrecision
            cfmRtpMetricsIntAvgLD
            cfmRtpMetricsIntAvgLossDistance
            cfmRtpMetricsIntJitterScale
            cfmRtpMetricsIntJitterPrecision
            cfmRtpMetricsIntJitter
            cfmRtpMetricsIntTransitScale
            cfmRtpMetricsIntTransitPrecision
            cfmRtpMetricsIntTransit
            cfmRtpMetricsIntMaxJitterScale
            cfmRtpMetricsIntMaxJitterPrecision
            cfmRtpMetricsIntMaxJitter
            cfmRtpMetricsIntEntry.21
            cfmRtpMetricsIntEntry.22
            cfmRtpMetricsIntEntry.23
            cfmRtpMetricsIntEntry.24
            cfmRtpMetricsIntEntry.25
            cfmRtpMetricsIntEntry.26
            cfmRtpMetricsIntEntry.27
            cfmRtpMetricsIntEntry.28
            cfmRtpMetricsIntEntry.29
            cfmRtpMetricsIntEntry.30
            cfmRtpMetricsIntEntry.31
            cfmRtpMetricsIntEntry.32
            cfmRtpMetricsIntEntry.33
            cfmRtpMetricsIntEntry.34
            cvVrfName
            cvVrfVnetTag
            cvVrfOperStatus
            cvVrfRouteDistProt
            cvVrfStorageType
            cvVrfRowStatus
            cvVrfListVrfIndex
            cvVrfListStorageType
            cvVrfListRowStatus
            cvVrfInterfaceType
            cvVrfInterfaceVnetTagOverride
            cvVrfInterfaceStorageType
            cvVrfInterfaceRowStatus
            cvInterfaceVnetTrunkEnabled
            cvInterfaceVnetVrfList
            cvVrfIfNotifEnable
            cvVnetTrunkNotifEnable
            ceqfpSystemTrafficDirection
            ceqfpSystemState
            ceqfpNumberSystemLoads
            ceqfpSystemLastLoadTime
            ceqfpFiveSecondUtilAlgo
            ceqfpOneMinuteUtilAlgo
            ceqfpFiveMinutesUtilAlgo
            ceqfpSixtyMinutesUtilAlgo
            ceqfpUtilInputPriorityPktRate
            ceqfpUtilInputPriorityBitRate
            ceqfpUtilInputNonPriorityPktRate
            ceqfpUtilInputNonPriorityBitRate
            ceqfpUtilInputTotalPktRate
            ceqfpUtilInputTotalBitRate
            ceqfpUtilOutputPriorityPktRate
            ceqfpUtilOutputPriorityBitRate
            ceqfpUtilOutputNonPriorityPktRate
            ceqfpUtilOutputNonPriorityBitRate
            ceqfpUtilOutputTotalPktRate
            ceqfpUtilOutputTotalBitRate
            ceqfpUtilProcessingLoad
            ceqfpMemoryResTotal
            ceqfpMemoryResInUse
            ceqfpMemoryResFree
            ceqfpMemoryResLowFreeWatermark
            ceqfpMemoryResRisingThreshold
            ceqfpMemoryResFallingThreshold
            ceqfpMemoryResourceEntry.8
            ceqfpMemoryResourceEntry.9
            ceqfpMemoryResourceEntry.10
            ceqfpMemoryResourceEntry.11
            ceqfpMemoryResourceEntry.12
            ceqfpMemoryResourceEntry.13
            ceqfpMemoryResourceEntry.14
            ceqfpMemoryResourceEntry.15
            ceqfpThroughputLicensedBW
            ceqfpThroughputLevel
            ceqfpThroughputSamplePeriod
            ceqfpThroughputThreshold
            ceqfpThroughputAvgRate
            ceqfpMemoryResThreshNotifEnabled
            ceqfpMemoryResCurrentRisingThresh
            ceqfpMemoryResCurrentFallingThresh
            ceqfpThroughputNotifEnabled
            cdlKey
            cdlLocationSubTypeCapability
            cdlLocationCountryCode
            cdlLocationTargetType
            cdlLocationTargetIdentifier
            cdlCivicAddrLocationValue
            cdlCivicAddrLocationStorageType
            cdlCivicAddrLocationStatus
            cdlCustomLocationValue
            cdlCustomLocationStorageType
            cdlCustomLocationStatus
            cdlGeoLatitude
            cdlGeoLatitudeResolution
            cdlGeoLongitude
            cdlGeoLongitudeResolution
            cdlGeoAltitude
            cdlGeoAltitudeType
            cdlGeoAltitudeResolution
            cdlGeoResolution
            cdlGeoStorageType
            cdlGeoStatus
            cdlLocationPreferWeightValue
            creClientTotalMaxInQLength
            creClientTotalMaxWaitQLength
            creClientTotalMaxDoneQLength
            creClientTotalAccessRejects
            creClientTotalAverageResponseDelay
            creClientSourcePortRangeStart
            creClientSourcePortRangeEnd
            creClientLastUsedSourcePort
            creClientLastUsedSourceId
            creAuthClientBadAuthenticators
            creAuthClientUnknownResponses
            creAuthClientTotalPacketsWithResponses
            creAuthClientBufferAllocFailures
            creAuthClientTotalResponses
            creAuthClientTotalPacketsWithoutResponses
            creAuthClientAverageResponseDelay
            creAuthClientMaxResponseDelay
            creAuthClientMaxBufferSize
            creAuthClientTimeouts
            creAuthClientDupIDs
            creAuthClientMalformedResponses
            creAuthClientLastUsedSourceId
            creAcctClientBadAuthenticators
            creAcctClientUnknownResponses
            creAcctClientTotalPacketsWithResponses
            creAcctClientBufferAllocFailures
            creAcctClientTotalResponses
            creAcctClientTotalPacketsWithoutResponses
            creAcctClientAverageResponseDelay
            creAcctClientMaxResponseDelay
            creAcctClientMaxBufferSize
            creAcctClientTimeouts
            creAcctClientDupIDs
            creAcctClientMalformedResponses
            creAcctClientLastUsedSourceId
            cepEntityNumReloads
            cepEntityLastReloadTime
            cepConfigPerfRange
            cepConfigRisingThreshold
            cepConfigFallingThreshold
            cepConfigThresholdNotifEnabled
            cepStatsAlgorithm
            cepStatsMeasurement
            cepIntervalTimeElapsed
            cepValidIntervalCount
            cepIntervalStatsValidData
            cepIntervalStatsRange
            cepIntervalStatsMeasurement
            cepIntervalStatsCreateTime
            cepThresholdNotifEnabled
            cepThroughputNotifEnabled
            cepThroughputLicensedBW
            cepThroughputLevel
            cepThroughputInterval
            cepThroughputThreshold
            cepThroughputAvgRate
            csbRadiusStatsClientName
            csbRadiusStatsClientType
            csbRadiusStatsSrvrName
            csbRadiusStatsAcsReqs
            csbRadiusStatsAcsRtrns
            csbRadiusStatsAcsAccpts
            csbRadiusStatsAcsRejects
            csbRadiusStatsAcsChalls
            csbRadiusStatsActReqs
            csbRadiusStatsActRetrans
            csbRadiusStatsActRsps
            csbRadiusStatsMalformedRsps
            csbRadiusStatsBadAuths
            csbRadiusStatsPending
            csbRadiusStatsTimeouts
            csbRadiusStatsUnknownType
            csbRadiusStatsDropped
            csbRfBillRealmStatsRealmName
            csbRfBillRealmStatsTotalStartAcrs
            csbRfBillRealmStatsTotalInterimAcrs
            csbRfBillRealmStatsTotalStopAcrs
            csbRfBillRealmStatsTotalEventAcrs
            csbRfBillRealmStatsSuccStartAcrs
            csbRfBillRealmStatsSuccInterimAcrs
            csbRfBillRealmStatsSuccStopAcrs
            csbRfBillRealmStatsSuccEventAcrs
            csbRfBillRealmStatsFailStartAcrs
            csbRfBillRealmStatsFailInterimAcrs
            csbRfBillRealmStatsFailStopAcrs
            csbRfBillRealmStatsFailEventAcrs
            csbSIPMthdCurrentStatsAdjName
            csbSIPMthdCurrentStatsMethodName
            csbSIPMthdCurrentStatsReqIn
            csbSIPMthdCurrentStatsReqOut
            csbSIPMthdCurrentStatsResp1xxIn
            csbSIPMthdCurrentStatsResp1xxOut
            csbSIPMthdCurrentStatsResp2xxIn
            csbSIPMthdCurrentStatsResp2xxOut
            csbSIPMthdCurrentStatsResp3xxIn
            csbSIPMthdCurrentStatsResp3xxOut
            csbSIPMthdCurrentStatsResp4xxIn
            csbSIPMthdCurrentStatsResp4xxOut
            csbSIPMthdCurrentStatsResp5xxIn
            csbSIPMthdCurrentStatsResp5xxOut
            csbSIPMthdCurrentStatsResp6xxIn
            csbSIPMthdCurrentStatsResp6xxOut
            csbSIPMthdHistoryStatsAdjName
            csbSIPMthdHistoryStatsMethodName
            csbSIPMthdHistoryStatsReqIn
            csbSIPMthdHistoryStatsReqOut
            csbSIPMthdHistoryStatsResp1xxIn
            csbSIPMthdHistoryStatsResp1xxOut
            csbSIPMthdHistoryStatsResp2xxIn
            csbSIPMthdHistoryStatsResp2xxOut
            csbSIPMthdHistoryStatsResp3xxIn
            csbSIPMthdHistoryStatsResp3xxOut
            csbSIPMthdHistoryStatsResp4xxIn
            csbSIPMthdHistoryStatsResp4xxOut
            csbSIPMthdHistoryStatsResp5xxIn
            csbSIPMthdHistoryStatsResp5xxOut
            csbSIPMthdHistoryStatsResp6xxIn
            csbSIPMthdHistoryStatsResp6xxOut
            csbSIPMthdRCCurrentStatsAdjName
            csbSIPMthdRCCurrentStatsMethodName
            csbSIPMthdRCCurrentStatsRespIn
            csbSIPMthdRCCurrentStatsRespOut
            csbSIPMthdRCHistoryStatsAdjName
            csbSIPMthdRCHistoryStatsMethodName
            csbSIPMthdRCHistoryStatsRespIn
            csbSIPMthdRCHistoryStatsRespOut
            cPtpDomainClockPortsTotal
            cPtpDomainClockPortPhysicalInterfacesTotal
            cPtpSystemDomainTotals
            cPtpClockInput1ppsEnabled
            cPtpClockInputFrequencyEnabled
            cPtpClockTODEnabled
            cPtpClockOutput1ppsEnabled
            cPtpClockOutput1ppsOffsetEnabled
            cPtpClockOutput1ppsOffsetValue
            cPtpClockOutput1ppsOffsetNegative
            cPtpClockInput1ppsInterface
            cPtpClockOutput1ppsInterface
            cPtpClockTODInterface
            cPtpSystemProfile
            cPtpClockCurrentDSStepsRemoved
            cPtpClockCurrentDSOffsetFromMaster
            cPtpClockCurrentDSMeanPathDelay
            cPtpClockParentDSParentPortIdentity
            cPtpClockParentDSParentStats
            cPtpClockParentDSOffset
            cPtpClockParentDSClockPhChRate
            cPtpClockParentDSGMClockIdentity
            cPtpClockParentDSGMClockPriority1
            cPtpClockParentDSGMClockPriority2
            cPtpClockParentDSGMClockQualityClass
            cPtpClockParentDSGMClockQualityAccuracy
            cPtpClockParentDSGMClockQualityOffset
            cPtpClockDefaultDSTwoStepFlag
            cPtpClockDefaultDSClockIdentity
            cPtpClockDefaultDSPriority1
            cPtpClockDefaultDSPriority2
            cPtpClockDefaultDSSlaveOnly
            cPtpClockDefaultDSQualityClass
            cPtpClockDefaultDSQualityAccuracy
            cPtpClockDefaultDSQualityOffset
            cPtpClockRunningState
            cPtpClockRunningPacketsSent
            cPtpClockRunningPacketsReceived
            cPtpClockTimePropertiesDSCurrentUTCOffsetValid
            cPtpClockTimePropertiesDSCurrentUTCOffset
            cPtpClockTimePropertiesDSLeap59
            cPtpClockTimePropertiesDSLeap61
            cPtpClockTimePropertiesDSTimeTraceable
            cPtpClockTimePropertiesDSFreqTraceable
            cPtpClockTimePropertiesDSPTPTimescale
            cPtpClockTimePropertiesDSSource
            cPtpClockTransDefaultDSClockIdentity
            cPtpClockTransDefaultDSNumOfPorts
            cPtpClockTransDefaultDSDelay
            cPtpClockTransDefaultDSPrimaryDomain
            cPtpClockPortName
            cPtpClockPortRole
            cPtpClockPortSyncOneStep
            cPtpClockPortCurrentPeerAddressType
            cPtpClockPortCurrentPeerAddress
            cPtpClockPortNumOfAssociatedPorts
            cPtpClockPortDSName
            cPtpClockPortDSPortIdentity
            cPtpClockPortDSAnnouncementInterval
            cPtpClockPortDSAnnounceRctTimeout
            cPtpClockPortDSSyncInterval
            cPtpClockPortDSMinDelayReqInterval
            cPtpClockPortDSPeerDelayReqInterval
            cPtpClockPortDSDelayMech
            cPtpClockPortDSPeerMeanPathDelay
            cPtpClockPortDSGrantDuration
            cPtpClockPortDSPTPVersion
            cPtpClockPortRunningName
            cPtpClockPortRunningState
            cPtpClockPortRunningRole
            cPtpClockPortRunningInterfaceIndex
            cPtpClockPortRunningIPversion
            cPtpClockPortRunningEncapsulationType
            cPtpClockPortRunningTxMode
            cPtpClockPortRunningRxMode
            cPtpClockPortRunningPacketsReceived
            cPtpClockPortRunningPacketsSent
            cPtpClockPortTransDSPortIdentity
            cPtpClockPortTransDSlogMinPdelayReqInt
            cPtpClockPortTransDSFaultyFlag
            cPtpClockPortTransDSPeerMeanPathDelay
            cPtpClockPortAssociateAddressType
            cPtpClockPortAssociateAddress
            cPtpClockPortAssociatePacketsSent
            cPtpClockPortAssociatePacketsReceived
            cPtpClockPortAssociateInErrors
            cPtpClockPortAssociateOutErrors
            cnsClkSelGlobProcessMode
            cnsClkSelGlobClockMode
            cnsClkSelGlobNetsyncEnable
            cnsClkSelGlobRevertiveMode
            cnsClkSelGlobESMCMode
            cnsClkSelGlobEECOption
            cnsClkSelGlobNetworkOption
            cnsClkSelGlobHoldoffTime
            cnsClkSelGlobWtrTime
            cnsClkSelGlobNofSources
            cnsClkSelGlobLastHoldoverSeconds
            cnsClkSelGlobCurrHoldoverSeconds
            cnsSelInpSrcName
            cnsSelInpSrcIntfType
            cnsSelInpSrcQualityLevel
            cnsSelInpSrcPriority
            cnsSelInpSrcTimestamp
            cnsSelInpSrcFSW
            cnsSelInpSrcMSW
            cnsInpSrcName
            cnsInpSrcIntfType
            cnsInpSrcPriority
            cnsInpSrcESMCCap
            cnsInpSrcSSMCap
            cnsInpSrcQualityLevelTxCfg
            cnsInpSrcQualityLevelRxCfg
            cnsInpSrcQualityLevelTx
            cnsInpSrcQualityLevelRx
            cnsInpSrcQualityLevel
            cnsInpSrcHoldoffTime
            cnsInpSrcWtrTime
            cnsInpSrcLockout
            cnsInpSrcSignalFailure
            cnsInpSrcAlarm
            cnsInpSrcAlarmInfo
            cnsInpSrcFSW
            cnsInpSrcMSW
            cnsExtOutSelNetsyncIndex
            cnsExtOutName
            cnsExtOutIntfType
            cnsExtOutQualityLevel
            cnsExtOutPriority
            cnsExtOutFSW
            cnsExtOutMSW
            cnsExtOutSquelch
            cnsT4ClkSrcName
            cnsT4ClkSrcIntfType
            cnsT4ClkSrcPriority
            cnsT4ClkSrcESMCCap
            cnsT4ClkSrcSSMCap
            cnsT4ClkSrcQualityLevelTxCfg
            cnsT4ClkSrcQualityLevelRxCfg
            cnsT4ClkSrcQualityLevelTx
            cnsT4ClkSrcQualityLevelRx
            cnsT4ClkSrcQualityLevel
            cnsT4ClkSrcHoldoffTime
            cnsT4ClkSrcWtrTime
            cnsT4ClkSrcLockout
            cnsT4ClkSrcSignalFailure
            cnsT4ClkSrcAlarm
            cnsT4ClkSrcAlarmInfo
            cnsT4ClkSrcFSW
            cnsT4ClkSrcMSW
            cnsMIBEnableStatusNotification
            cubeEnabled
            cubeVersion
            cubeTotalSessionAllowed
            cmqVoIPCallActiveConnectionId
            cmqVoIPCallActiveCallReferenceId
            cmqVoIPCallActiveRxCodecId
            cmqVoIPCallActiveRxSevConcealRatioPct
            cmqVoIPCallActiveRxCallConcealRatioPct
            cmqVoIPCallActiveRxPktLossRatioPct
            cmqVoIPCallActiveRxRoundTripTime
            cmqVoIPCallActiveRxCallDur
            cmqVoIPCallActiveRxVoiceDur
            cmqVoIPCallActiveRxPktLossConcealDur
            cmqVoIPCallActiveRxPktCntExpected
            cmqVoIPCallActiveRxPktCntNotArrived
            cmqVoIPCallActiveRxPktCntComfortNoise
            cmqVoIPCallActiveRxPktCntUnusableLate
            cmqVoIPCallActiveRxPktCntDiscarded
            cmqVoIPCallActiveRxPktCntEffLoss
            cmqVoIPCallActiveRxUnimpairedSecOK
            cmqVoIPCallActiveRxConcealSec
            cmqVoIPCallActiveRxSevConcealSec
            cmqVoIPCallActiveRxJBufMode
            cmqVoIPCallActiveRxJBufNomDelay
            cmqVoIPCallActiveRxJBufDlyNow
            cmqVoIPCallActiveRxJBufLowWater
            cmqVoIPCallActiveRxJBuffHiWater
            cmqVoIPCallActive3550JShortTermAvg
            cmqVoIPCallActive3550JCallAvg
            cmqVoIPCallActiveRxSignalLvl
            cmqVoIPCallActiveRxPred107Rscore
            cmqVoIPCallActiveRxPred107RMosListen
            cmqVoIPCallActiveRxPred107RScoreConv
            cmqVoIPCallActiveRxPred107RMosConv
            cmqVoIPCallActiveRxPred107CodecIeBase
            cmqVoIPCallActiveRxPred107CodecBPL
            cmqVoIPCallActiveRxPred107DefaultR0
            cmqVoIPCallActiveRxPred107IeEff
            cmqVoIPCallActiveRxPred107Idd
            cmqVoIPCallActiveRxPredMosLqoAvg
            cmqVoIPCallActiveRxPredMosLqoRecent
            cmqVoIPCallActiveRxPredMosLqoBaseline
            cmqVoIPCallActiveRxPredMosLqoMin
            cmqVoIPCallActiveRxPredMosLqoNumWin
            cmqVoIPCallActiveRxPredMosLqoBursts
            cmqVoIPCallActiveRxPredMosLqoFrLoss
            cmqVoIPCallActiveRxPredMosLqoVerID
            cmqVoIPCallActiveTxCodecId
            cmqVoIPCallActiveTxVadEnabled
            cmqVoIPCallActiveTxTmrCallDur
            cmqVoIPCallActiveTxTmrActSpeechDur
            cmqVoIPCallActiveTxSignalLvl
            cmqVoIPCallActiveTxNoiseFloor
            cmqCommonCallActiveNRConnectionId
            cmqCommonCallActiveNRCallReferenceId
            cmqCommonCallActiveNRCallType
            cmqCommonCallActiveNREnabledMic
            cmqCommonCallActiveNREnabledEar
            cmqCommonCallActiveNRDirMic
            cmqCommonCallActiveNRDirEar
            cmqCommonCallActiveNRLibVer
            cmqCommonCallActiveNRIntensity
            cmqCommonCallActivePreNRNoiseFloorEstMic
            cmqCommonCallActivePostNRNoiseFloorEstMic
            cmqCommonCallActivePreNRNoiseFloorEstEar
            cmqCommonCallActivePostNRNoiseFloorEstEar
            cmqCommonCallActiveASPConnectionId
            cmqCommonCallActiveASPCallReferenceId
            cmqCommonCallActiveASPCallType
            cmqCommonCallActiveASPEnabledMic
            cmqCommonCallActiveASPEnabledEar
            cmqCommonCallActiveASPDirMic
            cmqCommonCallActiveASPDirEar
            cmqCommonCallActiveASPMode
            cmqCommonCallActiveASPVer
            cmqCommonCallActiveNumSigASPTriggMic
            cmqCommonCallActiveDurSigASPTriggMic
            cmqCommonCallActiveTotNumASPTriggMic
            cmqCommonCallActiveTotASPDurMic
            cmqCommonCallActiveLoudestFreqEstForLongEpiMic
            cmqCommonCallActiveLongestDurEpiMic
            cmqCommonCallActiveNumSigASPTriggEar
            cmqCommonCallActiveDurSigASPTriggEar
            cmqCommonCallActiveTotNumASPTriggEar
            cmqCommonCallActiveTotASPDurEar
            cmqCommonCallActiveLoudestFreqEstForLongEpiEar
            cmqCommonCallActiveLongestDurEpiEar
            cmqVoIPCallHistoryConnectionId
            cmqVoIPCallHistoryCallReferenceId
            cmqVoIPCallHistoryRxCodecId
            cmqVoIPCallHistoryRxSevConcealRatioPct
            cmqVoIPCallHistoryRxCallConcealRatioPct
            cmqVoIPCallHistoryRxPktLossRatioPct
            cmqVoIPCallHistoryRxRoundTripTime
            cmqVoIPCallHistoryRxCallDur
            cmqVoIPCallHistoryRxVoiceDur
            cmqVoIPCallHistoryRxPktLossConcealDur
            cmqVoIPCallHistoryRxPktCntExpected
            cmqVoIPCallHistoryRxPktCntNotArrived
            cmqVoIPCallHistoryRxPktCntComfortNoise
            cmqVoIPCallHistoryRxPktCntUnusableLate
            cmqVoIPCallHistoryRxPktCntDiscarded
            cmqVoIPCallHistoryRxPktCntEffLoss
            cmqVoIPCallHistoryRxUnimpairedSecOK
            cmqVoIPCallHistoryRxConcealSec
            cmqVoIPCallHistoryRxSevConcealSec
            cmqVoIPCallHistoryRxJBufMode
            cmqVoIPCallHistoryRxJBufNomDelay
            cmqVoIPCallHistoryRxJBufDlyNow
            cmqVoIPCallHistoryRxJBufLowWater
            cmqVoIPCallHistoryRxJBuffHiWater
            cmqVoIPCallHistory3550JShortTermAvg
            cmqVoIPCallHistory3550JCallAvg
            cmqVoIPCallHistoryRxSignalLvl
            cmqVoIPCallHistoryRxPred107Rscore
            cmqVoIPCallHistoryRxPred107RMosListen
            cmqVoIPCallHistoryRxPred107RScoreConv
            cmqVoIPCallHistoryRxPred107RMosConv
            cmqVoIPCallHistoryRxPred107CodecIeBase
            cmqVoIPCallHistoryRxPred107CodecBPL
            cmqVoIPCallHistoryRxPred107DefaultR0
            cmqVoIPCallHistoryRxPred107IeEff
            cmqVoIPCallHistoryRxPred107Idd
            cmqVoIPCallHistoryRxPredMosLqoAvg
            cmqVoIPCallHistoryRxPredMosLqoRecent
            cmqVoIPCallHistoryRxPredMosLqoBaseline
            cmqVoIPCallHistoryRxPredMosLqoMin
            cmqVoIPCallHistoryRxPredMosLqoNumWin
            cmqVoIPCallHistoryRxPredMosLqoBursts
            cmqVoIPCallHistoryRxPredMosLqoFrLoss
            cmqVoIPCallHistoryRxPredMosLqoVerID
            cmqVoIPCallHistoryTxCodecId
            cmqVoIPCallHistoryTxVadEnabled
            cmqVoIPCallHistoryTxTmrCallDur
            cmqVoIPCallHistoryTxTmrActSpeechDur
            cmqVoIPCallHistoryTxSignalLvl
            cmqVoIPCallHistoryTxNoiseFloor
            cmqCommonCallHistoryNRConnectionId
            cmqCommonCallHistoryNRCallReferenceId
            cmqCommonCallHistoryNRCallType
            cmqCommonCallHistoryNREnabledMic
            cmqCommonCallHistoryNREnabledEar
            cmqCommonCallHistoryNRDirMic
            cmqCommonCallHistoryNRDirEar
            cmqCommonCallHistoryNRLibVer
            cmqCommonCallHistoryNRIntensity
            cmqCommonCallHistoryPreNRNoiseFloorEstMic
            cmqCommonCallHistoryPostNRNoiseFloorEstMic
            cmqCommonCallHistoryPreNRNoiseFloorEstEar
            cmqCommonCallHistoryPostNRNoiseFloorEstEar
            cmqCommonCallHistoryASPConnectionId
            cmqCommonCallHistoryASPCallReferenceId
            cmqCommonCallHistoryASPCallType
            cmqCommonCallHistoryASPEnabledMic
            cmqCommonCallHistoryASPEnabledEar
            cmqCommonCallHistoryASPDirMic
            cmqCommonCallHistoryASPDirEar
            cmqCommonCallHistoryASPMode
            cmqCommonCallHistoryASPVer
            cmqCommonCallHistoryNumSigASPTriggMic
            cmqCommonCallHistoryDurSigASPTriggMic
            cmqCommonCallHistoryTotNumASPTriggMic
            cmqCommonCallHistoryTotASPDurMic
            cmqCommonCallHistoryLoudestFreqEstForLongEpiMic
            cmqCommonCallHistoryLongestDurEpiMic
            cmqCommonCallHistoryNumSigASPTriggEar
            cmqCommonCallHistoryDurSigASPTriggEar
            cmqCommonCallHistoryTotNumASPTriggEar
            cmqCommonCallHistoryTotASPDurEar
            cmqCommonCallHistoryLoudestFreqEstForLongEpiEar
            cmqCommonCallHistoryLongestDurEpiEar
            cmqVideoCallActiveConnectionId
            cmqVideoCallActiveCallReferenceId
            cmqVideoCallActiveRxMOSInstant
            cmqVideoCallActiveRxCompressDegradeInstant
            cmqVideoCallActiveRxNetworkDegradeInstant
            cmqVideoCallActiveRxTransscodeDegradeInstant
            cmqVideoCallActiveRxMOSAverage
            cmqVideoCallActiveRxCompressDegradeAverage
            cmqVideoCallActiveRxNetworkDegradeAverage
            cmqVideoCallActiveRxTransscodeDegradeAverage
            cmqVideoCallHistoryConnectionId
            cmqVideoCallHistoryCallReferenceId
            cmqVideoCallHistoryRxMOSAverage
            cmqVideoCallHistoryRxCompressDegradeAverage
            cmqVideoCallHistoryRxNetworkDegradeAverage
            cmqVideoCallHistoryRxTransscodeDegradeAverage
            ciscoMgmt.710.196.1.1.1.1
            ciscoMgmt.710.196.1.1.1.2
            ciscoMgmt.710.196.1.1.1.3
            ciscoMgmt.710.196.1.1.1.4
            ciscoMgmt.710.196.1.1.1.5
            ciscoMgmt.710.196.1.1.1.6
            ciscoMgmt.710.196.1.1.1.7
            ciscoMgmt.710.196.1.1.1.8
            ciscoMgmt.710.196.1.1.1.9
            ciscoMgmt.710.196.1.1.1.10
            ciscoMgmt.710.196.1.1.1.11
            ciscoMgmt.710.196.1.1.1.12
            ciscoMgmt.710.196.1.2
            ciscoMgmt.710.196.1.3.1.1
            ciscoMgmt.710.196.1.3.1.2
            ciscoMgmt.710.196.1.3.1.3
            ciscoMgmt.710.196.1.3.1.4
            ciscoMgmt.710.196.1.3.1.5
            ciscoMgmt.710.196.1.3.1.6
            ciscoMgmt.710.196.1.3.1.7
            ciscoMgmt.710.196.1.3.1.8
            ciscoMgmt.710.196.1.3.1.9
            ciscoMgmt.710.196.1.3.1.10
            ciscoMgmt.710.196.1.3.1.11
            ciscoMgmt.710.196.1.3.1.12
            ciscoMgmt.710.84.1.1.1.1
            ciscoMgmt.710.84.1.1.1.2
            ciscoMgmt.710.84.1.1.1.3
            ciscoMgmt.710.84.1.1.1.4
            ciscoMgmt.710.84.1.1.1.5
            ciscoMgmt.710.84.1.1.1.6
            ciscoMgmt.710.84.1.1.1.7
            ciscoMgmt.710.84.1.1.1.8
            ciscoMgmt.710.84.1.1.1.9
            ciscoMgmt.710.84.1.1.1.10
            ciscoMgmt.710.84.1.1.1.11
            ciscoMgmt.710.84.1.1.1.12
            ciscoMgmt.710.84.1.2
            ciscoMgmt.710.84.1.3.1.1
            ciscoMgmt.710.84.1.3.1.2
            ciscoMgmt.710.84.1.3.1.3
            ciscoMgmt.710.84.1.3.1.4
            ciscoMgmt.710.84.1.3.1.5
            ciscoMgmt.710.84.1.3.1.6
            ciscoMgmt.710.84.1.3.1.7
            ciscoMgmt.710.84.1.3.1.8
            ciscoMgmt.710.84.1.3.1.9
            ciscoMgmt.710.84.1.3.1.10
            ciscoMgmt.710.84.1.3.1.11
            ciscoMgmt.710.84.1.3.1.12
            cpfrMCStorageType
            cpfrMCRowStatus
            cpfrMCMapIndex
            cpfrMCKeepAliveTimer
            cpfrMCMaxPrefixTotal
            cpfrMCMaxPrefixLearn
            cpfrMCEntranceLinksMaxUtil
            cpfrMCExitLinksMaxUtil
            cpfrMCPortNumber
            cpfrMCTracerouteProbeDelay
            cpfrMCRsvpPostDialDelay
            cpfrMCRsvpSignalingRetries
            cpfrMCNetflowExporter
            cpfrMCAdminStatus
            cpfrMCOperStatus
            cpfrMCConnStatus
            cpfrMCNumofBorderRouters
            cpfrMCNumofExits
            cpfrMCLearnState
            cpfrMCLearnStateTimeRemain
            cpfrMCPrefixCount
            cpfrMCPrefixLearned
            cpfrMCPrefixConfigured
            cpfrMCPbrMet
            cpfrMCEntry.26
            cpfrMCEntry.27
            cpfrMCEntry.28
            cpfrMCEntry.29
            cpfrMCEntry.30
            cpfrMapStorageType
            cpfrMapRowStatus
            cpfrMapName
            cpfrMapBackoffMinTimer
            cpfrMapBackoffMaxTimer
            cpfrMapBackoffStepTimer
            cpfrMapDelayType
            cpfrMapDelayRelativePercent
            cpfrMapDelayThresholdMax
            cpfrMapHolddownTimer
            cpfrMapPrefixForwardInterface
            cpfrMapJitterThresholdMax
            cpfrMapLinkGroupName
            cpfrMapFallbackLinkGroupName
            cpfrMapLossType
            cpfrMapLossRelativeAvg
            cpfrMapLossThresholdMax
            cpfrMapModeMonitor
            cpfrMapModeRouteOpts
            cpfrMapRouteMetricBgpLocalPref
            cpfrMapRouteMetricEigrpTagCommunity
            cpfrMapRouteMetricStaticTag
            cpfrMapModeSelectExitType
            cpfrMapMossThresholdMin
            cpfrMapMossPercentage
            cpfrMapNextHopAddressType
            cpfrMapNextHopAddress
            cpfrMapPeriodicTimer
            cpfrMapActiveProbeFrequency
            cpfrMapActiveProbePackets
            cpfrMapTracerouteReporting
            cpfrMapUnreachableType
            cpfrMapUnreachableRelativeAvg
            cpfrMapUnreachableThresholdMax
            cpfrMapRoundRobinResolver
            cpfrMapEntry.38
            cpfrMapEntry.39
            cpfrMapEntry.40
            cpfrMatchValid
            cpfrMatchAddrAccessList
            cpfrMatchAddrPrefixList
            cpfrMatchAddrPrefixInside
            cpfrMatchLearnMode
            cpfrMatchLearnListName
            cpfrMatchTCAccessListName
            cpfrMatchTCNbarListName
            cpfrMatchTCNbarApplPfxList
            cpfrMCResolvePriority
            cpfrMCResolveStorageType
            cpfrMCResolveRowStatus
            cpfrMCResolvePolicyType
            cpfrMCResolveVariance
            cpfrResolveMapIndex
            cpfrMCResolveMapPolicyIndex
            cpfrLearnAggregationType
            cpfrLearnAggregationPrefixLen
            cpfrLearnMethod
            cpfrLearnExpireType
            cpfrLearnExpireSessionNum
            cpfrLearnExpireTime
            cpfrLearnMonitorPeriod
            cpfrLearnPeriodInterval
            cpfrLearnPrefixesNumber
            cpfrLearnAggAccesslistName
            cpfrLearnFilterAccessListName
            cpfrLearnListStorageType
            cpfrLearnListRowStatus
            cpfrLearnListReferenceName
            cpfrLearnListSequenceNum
            cpfrLearnListMethod
            cpfrLearnListAclName
            cpfrLearnListAclFilterPfxName
            cpfrLearnListPfxName
            cpfrLearnListPfxInside
            cpfrLearnListNbarAppl
            cpfrActiveProbeStorageType
            cpfrActiveProbeRowStatus
            cpfrActiveProbeType
            cpfrActiveProbeTargetAddressType
            cpfrActiveProbeTargetAddress
            cpfrActiveProbeTargetPortNumber
            cpfrActiveProbePfrMapIndex
            cpfrActiveProbeDscpValue
            cpfrActiveProbeCodecName
            cpfrActiveProbeMapIndex
            cpfrActiveProbeMapPolicyIndex
            cpfrActiveProbeAdminStatus
            cpfrActiveProbeOperStatus
            cpfrActiveProbeAssignedPfxAddressType
            cpfrActiveProbeAssignedPfxAddress
            cpfrActiveProbeAssignedPfxLen
            cpfrActiveProbeMethod
            cpfrBRStorageType
            cpfrBRRowStatus
            cpfrBRAddressType
            cpfrBRAddress
            cpfrBRKeyName
            cpfrBROperStatus
            cpfrBRConnStatus
            cpfrBRUpTime
            cpfrBRConnFailureReason
            cpfrBRAuthFailCount
            cpfrExitStorageType
            cpfrExitRowStatus
            cpfrExitName
            cpfrExitType
            cpfrDowngradeBgpCommunity
            cpfrExitMaxUtilRxType
            cpfrExitMaxUtilRxAbsolute
            cpfrExitMaxUtilRxPercentage
            cpfrExitMaxUtilTxType
            cpfrExitMaxUtilTxAbsolute
            cpfrExitMaxUtilTxPercentage
            cpfrExitCostCalcMethod
            cpfrExitCostDiscard
            cpfrExitCostDiscardType
            cpfrExitCostDiscardAbsolute
            cpfrExitCostDiscardPercent
            cpfrExitCostEndDayOfMonth
            cpfrExitCostEndOffsetType
            cpfrExitCostEndOffset
            cpfrExitCostFixedFeeCost
            cpfrExitCostNickName
            cpfrExitCostSamplingPeriod
            cpfrExitCostRollupPeriod
            cpfrExitCostSummerTimeStart
            cpfrExitCostSummerTimeOffset
            cpfrExitCostSummerTimeEnd
            cpfrExitCapacity
            cpfrExitRxBandwidth
            cpfrExitTxBandwidth
            cpfrExitTxLoad
            cpfrExitRxLoad
            cpfrExitNickName
            cpfrExitCost1
            cpfrExitSustainedUtil1
            cpfrExitCost2
            cpfrExitSustainedUtil2
            cpfrExitCost3
            cpfrExitSustainedUtil3
            cpfrExitRollupTotal
            cpfrExitRollupDiscard
            cpfrExitRollupLeft
            cpfrExitRollupCollected
            cpfrExitRollupMomTgtUtil
            cpfrExitRollupStartingTgtUtil
            cpfrExitRollupCurrentTgtUtil
            cpfrExitRollupCumRxBytes
            cpfrExitRollupCumTxBytes
            cpfrExitRollupTimeRemain
            cpfrExitOperStatus
            cpfrExitRsvpBandwidthPool
            cpfrExitCostTierStorageType
            cpfrExitCostTierRowStatus
            cpfrExitCostTierFee
            cpfrTCBRIndex
            cpfrTCBRExitIndex
            cpfrTCMapIndex
            cpfrTCMapPolicyIndex
            cpfrTrafficClassValid
            cpfrTCSrcPrefixType
            cpfrTCSrcPrefix
            cpfrTCSrcPrefixLen
            cpfrTCSrcMinPort
            cpfrTCSrcMaxPort
            cpfrTCDstPrefixType
            cpfrTCDstPrefix
            cpfrTCDstPrefixLen
            cpfrTCDstMinPort
            cpfrTCDstMaxPort
            cpfrTCDscpValue
            cpfrTCProtocol
            cpfrTCNbarApplication
            cpfrTCStatus
            cpfrTCSType
            cpfrTCSLearnListIndex
            cpfrTCSTimeOnCurrExit
            cpfrTCSControlState
            cpfrTCSControlBy
            cpfrTCSTimeRemainCurrState
            cpfrTCSLastOOPEventTime
            cpfrTCSLastOOPReason
            cpfrTCSLastRouteChangeEvent
            cpfrTCSLastRouteChangeReason
            cpfrTCMLastUpdateTime
            cpfrTCMAge
            cpfrTCMetricsValid
            cpfrTCMActiveSTJitterAvg
            cpfrTCMMOSPercentage
            cpfrTCMAttempts
            cpfrTCMPackets
            cpfrTCMPassiveSTUnreachableAvg
            cpfrTCMPassiveSTDelayAvg
            cpfrTCMPassiveSTLossAvg
            cpfrTCMActiveSTUnreachableAvg
            cpfrTCMActiveSTDelayAvg
            cpfrTCMPassiveLTUnreachableAvg
            cpfrTCMPassiveLTDelayAvg
            cpfrTCMPassiveLTLossAvg
            cpfrTCMActiveLTUnreachableAvg
            cpfrTCMActiveLTDelayAvg
            cpfrLinkGroupRowStatus
            cpfrLinkGroupBRIndex
            cpfrLinkGroupExitIndex
            cpfrLinkGroupExitEntry.6
            cpfrLinkGroupExitEntry.7
            cpfrNbarApplListStorageType
            cpfrNbarApplListRowStatus
            cpfrNbarApplPdIndex
            cdtTemplateName
            cdtTemplateStatus
            cdtTemplateStorage
            cdtTemplateType
            cdtTemplateSrc
            cdtTemplateUsageCount
            cdtTemplateTargetStatus
            cdtTemplateTargetStorage
            cdtTemplateAssociationName
            cdtTemplateAssociationPrecedence
            cdtTemplateUsageTargetType
            cdtTemplateUsageTargetId
            cdtCommonValid
            cdtCommonDescr
            cdtCommonKeepaliveInt
            cdtCommonKeepaliveRetries
            cdtCommonVrf
            cdtCommonAddrPool
            cdtCommonIpv4AccessGroup
            cdtCommonIpv4Unreachables
            cdtCommonIpv6AccessGroup
            cdtCommonIpv6Unreachables
            cdtCommonSrvSubControl
            cdtCommonSrvRedirect
            cdtCommonSrvAcct
            cdtCommonSrvQos
            cdtCommonSrvNetflow
            cdtIfValid
            cdtIfMtu
            cdtIfCdpEnable
            cdtIfFlowMonitor
            cdtIfIpv4Unnumbered
            cdtIfIpv4SubEnable
            cdtIfIpv4Mtu
            cdtIfIpv4TcpMssAdjust
            cdtIfIpv4VerifyUniRpf
            cdtIfIpv4VerifyUniRpfAcl
            cdtIfIpv4VerifyUniRpfOpts
            cdtIfIpv6Enable
            cdtIfIpv6SubEnable
            cdtIfIpv6TcpMssAdjust
            cdtIfIpv6VerifyUniRpf
            cdtIfIpv6VerifyUniRpfAcl
            cdtIfIpv6VerifyUniRpfOpts
            cdtIfIpv6NdPrefix
            cdtIfIpv6NdPrefixLength
            cdtIfIpv6NdValidLife
            cdtIfIpv6NdPreferredLife
            cdtIfIpv6NdOpts
            cdtIfIpv6NdDadAttempts
            cdtIfIpv6NdNsInterval
            cdtIfIpv6NdReachableTime
            cdtIfIpv6NdRaIntervalUnits
            cdtIfIpv6NdRaIntervalMax
            cdtIfIpv6NdRaIntervalMin
            cdtIfIpv6NdRaLife
            cdtIfIpv6NdRouterPreference
            cdtPppValid
            cdtPppAccounting
            cdtPppAuthentication
            cdtPppAuthenticationMethods
            cdtPppAuthorization
            cdtPppLoopbackIgnore
            cdtPppMaxBadAuth
            cdtPppMaxConfigure
            cdtPppMaxFailure
            cdtPppMaxTerminate
            cdtPppTimeoutAuthentication
            cdtPppTimeoutRetry
            cdtPppChapOpts
            cdtPppChapHostname
            cdtPppChapPassword
            cdtPppMsChapV1Opts
            cdtPppMsChapV1Hostname
            cdtPppMsChapV1Password
            cdtPppMsChapV2Opts
            cdtPppMsChapV2Hostname
            cdtPppMsChapV2Password
            cdtPppPapOpts
            cdtPppPapUsername
            cdtPppPapPassword
            cdtPppEapOpts
            cdtPppEapIdentity
            cdtPppEapPassword
            cdtPppIpcpAddrOption
            cdtPppIpcpDnsOption
            cdtPppIpcpDnsPrimary
            cdtPppIpcpDnsSecondary
            cdtPppIpcpWinsOption
            cdtPppIpcpWinsPrimary
            cdtPppIpcpWinsSecondary
            cdtPppIpcpMaskOption
            cdtPppIpcpMask
            cdtPppPeerDefIpAddrOpts
            cdtPppPeerDefIpAddrSrc
            cdtPppPeerDefIpAddr
            cdtPppPeerIpAddrPoolStatus
            cdtPppPeerIpAddrPoolStorage
            cdtPppPeerIpAddrPoolName
            cdtEthernetValid
            cdtEthernetBridgeDomain
            cdtEthernetPppoeEnable
            cdtEthernetIpv4PointToPoint
            cdtEthernetMacAddr
            cdtSrvValid
            cdtSrvNetworkSrv
            cdtSrvVpdnGroup
            cdtSrvSgSrvGroup
            cdtSrvSgSrvType
            cdtSrvMulticast
            csubSessionType
            csubSessionIpAddrAssignment
            csubSessionState
            csubSessionAuthenticated
            csubSessionRedundancyMode
            csubSessionCreationTime
            csubSessionDerivedCfg
            csubSessionAvailableIdentities
            csubSessionSubscriberLabel
            csubSessionMacAddress
            csubSessionNativeVrf
            csubSessionNativeIpAddrType
            csubSessionNativeIpAddr
            csubSessionNativeIpMask
            csubSessionDomainVrf
            csubSessionDomainIpAddrType
            csubSessionDomainIpAddr
            csubSessionDomainIpMask
            csubSessionPbhk
            csubSessionRemoteId
            csubSessionCircuitId
            csubSessionNasPort
            csubSessionDomain
            csubSessionUsername
            csubSessionAcctSessionId
            csubSessionDnis
            csubSessionMedia
            csubSessionMlpNegotiated
            csubSessionProtocol
            csubSessionDhcpClass
            csubSessionTunnelName
            csubSessionLocationIdentifier
            csubSessionServiceIdentifier
            csubSessionLastChanged
            csubSessionNativeIpAddrType2
            csubSessionNativeIpAddr2
            csubSessionNativeIpMask2
            csubSessionByType
            csubSessionIfIndex
            csubAggStatsPendingSessions
            csubAggStatsUpSessions
            csubAggStatsAuthSessions
            csubAggStatsUnAuthSessions
            csubAggStatsLightWeightSessions
            csubAggStatsRedSessions
            csubAggStatsHighUpSessions
            csubAggStatsAvgSessionUptime
            csubAggStatsAvgSessionRPM
            csubAggStatsAvgSessionRPH
            csubAggStatsThrottleEngagements
            csubAggStatsTotalCreatedSessions
            csubAggStatsTotalFailedSessions
            csubAggStatsTotalUpSessions
            csubAggStatsTotalAuthSessions
            csubAggStatsTotalDiscSessions
            csubAggStatsTotalLightWeightSessions
            csubAggStatsTotalFlowsUp
            csubAggStatsDayCreatedSessions
            csubAggStatsDayFailedSessions
            csubAggStatsDayUpSessions
            csubAggStatsDayAuthSessions
            csubAggStatsDayDiscSessions
            csubAggStatsCurrTimeElapsed
            csubAggStatsCurrValidIntervals
            csubAggStatsCurrInvalidIntervals
            csubAggStatsCurrFlowsUp
            csubAggStatsCurrCreatedSessions
            csubAggStatsCurrFailedSessions
            csubAggStatsCurrUpSessions
            csubAggStatsCurrAuthSessions
            csubAggStatsCurrDiscSessions
            csubAggStatsDiscontinuityTime
            csubAggStatsIntValid
            csubAggStatsIntCreatedSessions
            csubAggStatsIntFailedSessions
            csubAggStatsIntUpSessions
            csubAggStatsIntAuthSessions
            csubAggStatsIntDiscSessions
            csubJobFinishedNotifyEnable
            csubJobIndexedAttributes
            csubJobIdNext
            csubJobMaxNumber
            csubJobMaxLife
            csubJobCount
            csubJobStatus
            csubJobStorage
            csubJobType
            csubJobControl
            csubJobState
            csubJobStartedTime
            csubJobFinishedTime
            csubJobFinishedReason
            csubJobMatchIdentities
            csubJobMatchOtherParams
            csubJobMatchSubscriberLabel
            csubJobMatchMacAddress
            csubJobMatchNativeVrf
            csubJobMatchNativeIpAddrType
            csubJobMatchNativeIpAddr
            csubJobMatchNativeIpMask
            csubJobMatchDomainVrf
            csubJobMatchDomainIpAddrType
            csubJobMatchDomainIpAddr
            csubJobMatchDomainIpMask
            csubJobMatchPbhk
            csubJobMatchRemoteId
            csubJobMatchCircuitId
            csubJobMatchNasPort
            csubJobMatchDomain
            csubJobMatchUsername
            csubJobMatchAcctSessionId
            csubJobMatchDnis
            csubJobMatchMedia
            csubJobMatchMlpNegotiated
            csubJobMatchProtocol
            csubJobMatchServiceName
            csubJobMatchDhcpClass
            csubJobMatchTunnelName
            csubJobMatchDanglingDuration
            csubJobMatchState
            csubJobMatchAuthenticated
            csubJobMatchRedundancyMode
            csubJobQuerySortKey1
            csubJobQuerySortKey2
            csubJobQuerySortKey3
            csubJobQueryResultingReportSize
            csubJobQueueJobId
            csubJobReportSession
            cfmMetadataFlowProtocolType
            cfmMetadataFlowDestAddrType
            cfmMetadataFlowDestAddr
            cfmMetadataFlowDestPort
            cfmMetadataFlowSrcAddrType
            cfmMetadataFlowSrcAddr
            cfmMetadataFlowSrcPort
            cfmMetadataFlowSSRC
            cfmMetadataFlowAttrType
            cfmMetadataFlowAttrValue
            cfmMetadataFlowAllAttrValue
            cfmMetadataFlowAllAttrPen
            cMTInitiatorEnable
            cMTInitiatorSourceInterface
            cMTInitiatorSourceAddressType
            cMTInitiatorSourceAddress
            cMTInitiatorMaxSessions
            cMTInitiatorSoftwareVersionMajor
            cMTInitiatorSoftwareVersionMinor
            cMTInitiatorProtocolVersionMajor
            cMTInitiatorProtocolVersionMinor
            cMTInitiatorConfiguredSessions
            cMTInitiatorPendingSessions
            cMTInitiatorInactiveSessions
            cMTInitiatorActiveSessions
            cMTResponderEnable
            cMTResponderMaxSessions
            cMTResponderActiveSessions
            cMTFlowSpecifierRowStatus
            cMTFlowSpecifierMetadataGlobalId
            cMTFlowSpecifierDestAddrType
            cMTFlowSpecifierDestAddr
            cMTFlowSpecifierDestPort
            cMTFlowSpecifierSourceAddrType
            cMTFlowSpecifierSourceAddr
            cMTFlowSpecifierSourcePort
            cMTFlowSpecifierIpProtocol
            cMTPathSpecifierRowStatus
            cMTPathSpecifierMetadataGlobalId
            cMTPathSpecifierDestAddrType
            cMTPathSpecifierDestAddr
            cMTPathSpecifierDestPort
            cMTPathSpecifierSourceAddrType
            cMTPathSpecifierSourceAddr
            cMTPathSpecifierSourcePort
            cMTPathSpecifierProtocolForDiscovery
            cMTPathSpecifierGatewayAddrType
            cMTPathSpecifierGatewayAddr
            cMTPathSpecifierGatewayVlanId
            cMTPathSpecifierIpProtocol
            cMTSessionParamsRowStatus
            cMTSessionParamsResponseTimeout
            cMTSessionParamsFrequency
            cMTSessionParamsInactivityTimeout
            cMTSessionParamsHistoryBuckets
            cMTSessionParamsRouteChangeReactiontime
            cMTMediaMonitorProfileRowStatus
            cMTMediaMonitorProfileMetric
            cMTMediaMonitorProfileInterval
            cMTMediaMonitorProfileRtpMaxDropout
            cMTMediaMonitorProfileRtpMaxReorder
            cMTMediaMonitorProfileRtpMinimalSequential
            cMTSystemProfileRowStatus
            cMTSystemProfileMetric
            cMTSessionRowStatus
            cMTSessionPathSpecifierName
            cMTSessionParamName
            cMTSessionProfileName
            cMTSessionFlowSpecifierName
            cMTSessionTraceRouteEnabled
            cMTScheduleRowStatus
            cMTScheduleStartTime
            cMTScheduleLife
            cMTScheduleEntryAgeout
            cMTScheduleRecurring
            cMTPathHopAddrType
            cMTPathHopAddr
            cMTPathHopType
            cMTPathHopAlternate1AddrType
            cMTPathHopAlternate1Addr
            cMTPathHopAlternate2AddrType
            cMTPathHopAlternate2Addr
            cMTPathHopAlternate3AddrType
            cMTPathHopAlternate3Addr
            cMTHopStatsMaskBitmaps
            cMTHopStatsName
            cMTHopStatsMediatraceTtl
            cMTHopStatsCollectionStatus
            cMTHopStatsIngressInterface
            cMTHopStatsEgressInterface
            cMTTraceRouteHopNumber
            cMTTraceRouteHopRtt
            cMTSessionStatusBitmaps
            cMTSessionStatusGlobalSessionId
            cMTSessionStatusOperationState
            cMTSessionStatusOperationTimeToLive
            cMTSessionRequestStatsBitmaps
            cMTSessionRequestStatsRequestTimestamp
            cMTSessionRequestStatsRequestStatus
            cMTSessionRequestStatsTracerouteStatus
            cMTSessionRequestStatsRouteIndex
            cMTSessionRequestStatsNumberOfMediatraceHops
            cMTSessionRequestStatsNumberOfNonMediatraceHops
            cMTSessionRequestStatsNumberOfValidHops
            cMTSessionRequestStatsNumberOfErrorHops
            cMTSessionRequestStatsNumberOfNoDataRecordHops
            cMTSessionRequestStatsMDGlobalId
            cMTSessionRequestStatsMDMultiPartySessionId
            cMTSessionRequestStatsMDAppName
            cMTCommonMetricsBitmaps
            cMTCommonMetricsFlowSamplingStartTime
            cMTCommonMetricsIpPktDropped
            cMTCommonMetricsIpOctets
            cMTCommonMetricsIpPktCount
            cMTCommonMetricsIpByteRate
            cMTCommonMetricsIpDscp
            cMTCommonMetricsIpTtl
            cMTCommonMetricsFlowCounter
            cMTCommonMetricsFlowDirection
            cMTCommonMetricsLossMeasurement
            cMTCommonMetricsMediaStopOccurred
            cMTCommonMetricsRouteForward
            cMTCommonMetricsIpProtocol
            cMTRtpMetricsBitmaps
            cMTRtpMetricsBitRate
            cMTRtpMetricsOctets
            cMTRtpMetricsPkts
            cMTRtpMetricsJitter
            cMTRtpMetricsLostPkts
            cMTRtpMetricsExpectedPkts
            cMTRtpMetricsLostPktEvents
            cMTRtpMetricsLossPercent
            cMTTcpMetricBitmaps
            cMTTcpMetricMediaByteCount
            cMTTcpMetricConnectRoundTripDelay
            cMTTcpMetricLostEventCount
            cMTSystemMetricBitmaps
            cMTSystemMetricCpuOneMinuteUtilization
            cMTSystemMetricCpuFiveMinutesUtilization
            cMTSystemMetricMemoryUtilization
            cMTInterfaceBitmaps
            cMTInterfaceOutSpeed
            cMTInterfaceInSpeed
            cMTInterfaceOutDiscards
            cMTInterfaceInDiscards
            cMTInterfaceOutErrors
            cMTInterfaceInErrors
            cMTInterfaceOutOctets
            cMTInterfaceInOctets
            clispExtEidRegRlocMembershipMemberSince
            clispExtEidRegRlocMembershipGleaned
            clispExtEidRegRlocMembershipConfigured
            clispExtRlocMembershipMemberSince
            clispExtRlocMembershipDiscovered
            clispExtRlocMembershipConfigured
            clispExtReliableTransportSessionState
            clispExtReliableTransportSessionLastStateChangeTime
            clispExtReliableTransportSessionEstablishmentRole
            clispExtReliableTransportSessionMessagesIn
            clispExtReliableTransportSessionMessagesOut
            clispExtReliableTransportSessionBytesIn
            clispExtReliableTransportSessionBytesOut
            clispExtGlobalStatsEidRegMoreSpecificEntryCount
            clispExtFeaturesEidRegMoreSpecificWarningThreshold
            clispExtFeaturesEidRegMoreSpecificLimit
            clispExtFeaturesMapCacheWarningThreshold
            clispExtEidRegMoreSpecificWarningThreshold
            clispExtEidRegMoreSpecificLimit
            clispExtEidRegMoreSpecificCount
            ciscoIpMRoute.1
            ciscoIpMRouteEntry.12
            ciscoIpMRouteEntry.13
            ciscoIpMRouteEntry.14
            ciscoIpMRouteEntry.15
            ciscoIpMRouteEntry.16
            ciscoIpMRouteEntry.17
            ciscoIpMRouteEntry.18
            ciscoIpMRouteEntry.19
            ciscoIpMRouteEntry.20
            ciscoIpMRouteEntry.21
            ciscoIpMRouteEntry.22
            ciscoIpMRouteEntry.23
            ciscoIpMRouteEntry.24
            ciscoIpMRouteEntry.25
            ciscoIpMRouteEntry.26
            ciscoIpMRouteEntry.27
            ciscoIpMRouteEntry.28
            ciscoIpMRouteEntry.30
            ciscoIpMRouteEntry.31
            ciscoIpMRouteEntry.32
            ciscoIpMRouteEntry.33
            ciscoIpMRouteEntry.34
            ciscoIpMRouteEntry.35
            ciscoIpMRouteEntry.36
            ciscoIpMRouteEntry.37
            ciscoIpMRouteEntry.38
            ciscoIpMRouteEntry.39
            ciscoIpMRouteEntry.40
            ciscoIpMRouteEntry.41
            ciscoIpMRouteNextHopEntry.9
            ciscoIpMRouteNextHopEntry.10
            ciscoIpMRouteNextHopEntry.11
            ciscoIpMRouteHeartBeatEntry.2
            ciscoIpMRouteHeartBeatEntry.3
            ciscoIpMRouteHeartBeatEntry.4
            ciscoIpMRouteHeartBeatEntry.5
            ciscoIpMRouteHeartBeatEntry.6
            ciscoIpMRouteHeartBeatEntry.7
            ciscoIpMRouteHeartBeatEntry.8
            ciscoIpMRouteInterfaceEntry.1
            ciscoIpMRouteInterfaceEntry.2
            ciscoIpMRouteInterfaceEntry.3
            ciscoIpMRouteInterfaceEntry.4
            ciscoIpMRouteInterfaceEntry.5
            ciscoIpMRouteInterfaceEntry.6
            qllcLSAdminEntry.1
            qllcLSAdminEntry.2
            qllcLSAdminEntry.3
            qllcLSAdminEntry.4
            qllcLSAdminEntry.5
            qllcLSAdminEntry.6
            qllcLSAdminEntry.7
            qllcLSOperEntry.1
            qllcLSOperEntry.2
            qllcLSOperEntry.3
            qllcLSOperEntry.4
            qllcLSOperEntry.5
            qllcLSOperEntry.6
            qllcLSOperEntry.7
            qllcLSOperEntry.8
            qllcLSStatsEntry.1
            qllcLSStatsEntry.2
            qllcLSStatsEntry.3
            qllcLSStatsEntry.4
            qllcLSStatsEntry.5
            qllcLSStatsEntry.6
            qllcLSStatsEntry.7
            qllcLSStatsEntry.8
            qllcLSStatsEntry.9
            qllcLSStatsEntry.10
            qllcLSStatsEntry.11
            qllcLSStatsEntry.12
            qllcLSStatsEntry.13
            qllcLSStatsEntry.14
            qllcLSStatsEntry.15
            qllcLSStatsEntry.16
            qllcLSStatsEntry.17
            qllcLSStatsEntry.18
            qllcLSStatsEntry.19
            qllcLSStatsEntry.20
            qllcLSStatsEntry.21
            qllcLSStatsEntry.22
            convQllcAdminEntry.1
            convQllcAdminEntry.2
            convQllcAdminEntry.3
            convQllcAdminEntry.4
            convQllcAdminEntry.5
            convQllcAdminEntry.6
            convQllcAdminEntry.7
            convQllcAdminEntry.8
            convQllcAdminEntry.9
            convQllcAdminEntry.10
            convQllcAdminEntry.11
            convQllcAdminEntry.12
            convQllcOperEntry.1
            convQllcOperEntry.2
            convQllcOperEntry.3
            convQllcOperEntry.4
            convQllcOperEntry.5
            convQllcOperEntry.6
            convQllcOperEntry.7
            convQllcOperEntry.8
            convQllcOperEntry.9
            convQllcOperEntry.10
            convQllcOperEntry.11
            convQllcOperEntry.12
            convQllcOperEntry.13
            convQllcOperEntry.14
            convQllcOperEntry.15
            ciscoDlswNode.1
            ciscoDlswNode.2
            ciscoDlswNode.3
            ciscoDlswNode.4
            ciscoDlswNode.5
            ciscoDlswNode.6
            ciscoDlswNode.7
            ciscoDlswNode.8
            ciscoDlswNode.9
            ciscoDlswTrapControl.1
            ciscoDlswTrapControl.2
            ciscoDlswTrapControl.3
            ciscoDlswTrapControl.4
            ciscoDlswTConnStat.1
            ciscoDlswTConnStat.2
            ciscoDlswTConnStat.3
            ciscoDlswTConnConfigEntry.2
            ciscoDlswTConnConfigEntry.3
            ciscoDlswTConnConfigEntry.4
            ciscoDlswTConnConfigEntry.5
            ciscoDlswTConnConfigEntry.6
            ciscoDlswTConnConfigEntry.7
            ciscoDlswTConnConfigEntry.8
            ciscoDlswTConnConfigEntry.9
            ciscoDlswTConnConfigEntry.10
            ciscoDlswTConnConfigEntry.11
            ciscoDlswTConnConfigEntry.12
            ciscoDlswTConnConfigEntry.13
            ciscoDlswTConnOperEntry.2
            ciscoDlswTConnOperEntry.4
            ciscoDlswTConnOperEntry.5
            ciscoDlswTConnOperEntry.6
            ciscoDlswTConnOperEntry.7
            ciscoDlswTConnOperEntry.8
            ciscoDlswTConnOperEntry.9
            ciscoDlswTConnOperEntry.10
            ciscoDlswTConnOperEntry.11
            ciscoDlswTConnOperEntry.12
            ciscoDlswTConnOperEntry.13
            ciscoDlswTConnOperEntry.14
            ciscoDlswTConnOperEntry.15
            ciscoDlswTConnOperEntry.16
            ciscoDlswTConnOperEntry.17
            ciscoDlswTConnOperEntry.18
            ciscoDlswTConnOperEntry.19
            ciscoDlswTConnOperEntry.20
            ciscoDlswTConnOperEntry.21
            ciscoDlswTConnOperEntry.22
            ciscoDlswTConnOperEntry.23
            ciscoDlswTConnOperEntry.24
            ciscoDlswTConnOperEntry.25
            ciscoDlswTConnOperEntry.26
            ciscoDlswTConnOperEntry.27
            ciscoDlswTConnOperEntry.28
            ciscoDlswTConnOperEntry.29
            ciscoDlswTConnOperEntry.30
            ciscoDlswTConnOperEntry.31
            ciscoDlswTConnOperEntry.32
            ciscoDlswTConnOperEntry.33
            ciscoDlswTConnOperEntry.34
            ciscoDlswTConnOperEntry.35
            ciscoDlswTConnOperEntry.36
            ciscoDlswTConnTcpConfigEntry.1
            ciscoDlswTConnTcpConfigEntry.2
            ciscoDlswTConnTcpConfigEntry.3
            ciscoDlswTConnTcpOperEntry.1
            ciscoDlswTConnTcpOperEntry.2
            ciscoDlswTConnTcpOperEntry.3
            ciscoDlswIfEntry.1
            ciscoDlswIfEntry.2
            ciscoDlswIfEntry.3
            ciscoDlswCircuitStat.1
            ciscoDlswCircuitStat.2
            ciscoDlswCircuitEntry.3
            ciscoDlswCircuitEntry.4
            ciscoDlswCircuitEntry.5
            ciscoDlswCircuitEntry.6
            ciscoDlswCircuitEntry.7
            ciscoDlswCircuitEntry.10
            ciscoDlswCircuitEntry.11
            ciscoDlswCircuitEntry.12
            ciscoDlswCircuitEntry.13
            ciscoDlswCircuitEntry.14
            ciscoDlswCircuitEntry.15
            ciscoDlswCircuitEntry.16
            ciscoDlswCircuitEntry.17
            ciscoDlswCircuitEntry.18
            ciscoDlswCircuitEntry.19
            ciscoDlswCircuitEntry.20
            ciscoDlswCircuitEntry.21
            ciscoDlswCircuitEntry.22
            ciscoDlswCircuitEntry.23
            ciscoDlswCircuitEntry.24
            ciscoDlswCircuitEntry.25
            ciscoDlswCircuitEntry.26
            ciscoDlswCircuitEntry.27
            ciscoDlswCircuitEntry.28
            ciscoDlswCircuitEntry.29
            ciscoDlswCircuitEntry.30
            ciscoDlswCircuitEntry.31
            ciscoAtmIfPVCs
            ciscoExperiment.10.225.1.1.13
            ciscoExperiment.10.225.1.1.14
            ciscoVpdnMgmtMIB.0.1
            ciscoVpdnMgmtMIB.0.2
            cvpdnTunnelTotal
            cvpdnSessionTotal
            cvpdnDeniedUsersTotal
            cvpdnSystemTunnelTotal
            cvpdnSystemSessionTotal
            cvpdnSystemDeniedUsersTotal
            cvpdnSystemInfo.5
            cvpdnSystemInfo.6
            cvpdnTunnelRemoteTunnelId
            cvpdnTunnelLocalName
            cvpdnTunnelRemoteName
            cvpdnTunnelRemoteEndpointName
            cvpdnTunnelLocalInitConnection
            cvpdnTunnelOrigCause
            cvpdnTunnelState
            cvpdnTunnelActiveSessions
            cvpdnTunnelDeniedUsers
            cvpdnTunnelSoftshut
            cvpdnTunnelNetworkServiceType
            cvpdnTunnelLocalIpAddress
            cvpdnTunnelSourceIpAddress
            cvpdnTunnelRemoteIpAddress
            cvpdnTunnelAttrRemoteTunnelId
            cvpdnTunnelAttrLocalName
            cvpdnTunnelAttrRemoteName
            cvpdnTunnelAttrRemoteEndpointName
            cvpdnTunnelAttrLocalInitConnection
            cvpdnTunnelAttrOrigCause
            cvpdnTunnelAttrState
            cvpdnTunnelAttrActiveSessions
            cvpdnTunnelAttrDeniedUsers
            cvpdnTunnelAttrSoftshut
            cvpdnTunnelAttrNetworkServiceType
            cvpdnTunnelAttrLocalIpAddress
            cvpdnTunnelAttrSourceIpAddress
            cvpdnTunnelAttrRemoteIpAddress
            cvpdnTunnelAttrEntry.16
            cvpdnTunnelAttrEntry.17
            cvpdnTunnelAttrEntry.18
            cvpdnTunnelAttrEntry.19
            cvpdnTunnelAttrEntry.20
            cvpdnTunnelAttrEntry.21
            cvpdnTunnelSessionUserName
            cvpdnTunnelSessionState
            cvpdnTunnelSessionCallDuration
            cvpdnTunnelSessionPacketsOut
            cvpdnTunnelSessionBytesOut
            cvpdnTunnelSessionPacketsIn
            cvpdnTunnelSessionBytesIn
            cvpdnTunnelSessionDeviceType
            cvpdnTunnelSessionDeviceCallerId
            cvpdnTunnelSessionDevicePhyId
            cvpdnTunnelSessionMultilink
            cvpdnTunnelSessionModemSlotIndex
            cvpdnTunnelSessionModemPortIndex
            cvpdnTunnelSessionDS1SlotIndex
            cvpdnTunnelSessionDS1PortIndex
            cvpdnTunnelSessionDS1ChannelIndex
            cvpdnTunnelSessionModemCallStartTime
            cvpdnTunnelSessionModemCallStartIndex
            cvpdnSessionAttrUserName
            cvpdnSessionAttrState
            cvpdnSessionAttrCallDuration
            cvpdnSessionAttrPacketsOut
            cvpdnSessionAttrBytesOut
            cvpdnSessionAttrPacketsIn
            cvpdnSessionAttrBytesIn
            cvpdnSessionAttrDeviceType
            cvpdnSessionAttrDeviceCallerId
            cvpdnSessionAttrDevicePhyId
            cvpdnSessionAttrMultilink
            cvpdnSessionAttrModemSlotIndex
            cvpdnSessionAttrModemPortIndex
            cvpdnSessionAttrDS1SlotIndex
            cvpdnSessionAttrDS1PortIndex
            cvpdnSessionAttrDS1ChannelIndex
            cvpdnSessionAttrModemCallStartTime
            cvpdnSessionAttrModemCallStartIndex
            cvpdnSessionAttrEntry.20
            cvpdnSessionAttrEntry.21
            cvpdnSessionAttrEntry.22
            cvpdnSessionAttrEntry.23
            cvpdnSessionAttrEntry.24
            cvpdnUnameToFailHistUserId
            cvpdnUnameToFailHistLocalInitConn
            cvpdnUnameToFailHistLocalName
            cvpdnUnameToFailHistRemoteName
            cvpdnUnameToFailHistSourceIp
            cvpdnUnameToFailHistDestIp
            cvpdnUnameToFailHistCount
            cvpdnUnameToFailHistFailTime
            cvpdnUnameToFailHistFailType
            cvpdnUnameToFailHistFailReason
            cvpdnUserToFailHistInfoEntry.13
            cvpdnUserToFailHistInfoEntry.14
            cvpdnUserToFailHistInfoEntry.15
            cvpdnUserToFailHistInfoEntry.16
            ciscoVpdnMgmtMIBObjects.10.36.1.2
            ciscoVpdnMgmtMIBObjects.6.1
            ciscoVpdnMgmtMIBObjects.6.2
            ciscoVpdnMgmtMIBObjects.6.3
            ciscoVpdnMgmtMIBObjects.10.100.1.2
            ciscoVpdnMgmtMIBObjects.10.100.1.3
            ciscoVpdnMgmtMIBObjects.10.100.1.4
            ciscoVpdnMgmtMIBObjects.10.100.1.5
            ciscoVpdnMgmtMIBObjects.10.100.1.6
            ciscoVpdnMgmtMIBObjects.10.100.1.7
            ciscoVpdnMgmtMIBObjects.6.5
            ciscoVpdnMgmtMIBObjects.10.144.1.3
            ciscoVpdnMgmtMIBObjects.7.1
            ciscoVpdnMgmtMIBObjects.7.2
            cCallHistoryEntry.2
            cCallHistoryEntry.3
            cCallHistoryEntry.4
            cCallHistoryEntry.5
            cCallHistoryEntry.6
            cCallHistoryEntry.7
            cCallHistoryEntry.8
            cCallHistoryEntry.9
            cCallHistoryEntry.10
            cCallHistoryEntry.11
            cCallHistoryEntry.12
            cCallHistoryEntry.13
            cCallHistoryEntry.14
            cCallHistoryEntry.15
            cCallHistoryEntry.16
            cCallHistoryEntry.17
            cCallHistoryEntry.18
            cCallHistoryEntry.19
            cCallHistoryEntry.20
            cCallHistoryIecEntry.2
            cPeerSearchType
            atmIntfPvcFailures
            atmIntfCurrentlyFailingPVcls
            atmIntfPvcFailuresTrapEnable
            atmIntfPvcNotificationInterval
            atmPreviouslyFailedPVclInterval
            atmCurrentlyFailingPVclTimeStamp
            atmPreviouslyFailedPVclTimeStamp
            atmIntfCurrentlyDownToUpPVcls
            atmIntfOAMFailedPVcls
            atmIntfCurrentlyOAMFailingPVcls
            atmPVclStatusTransition
            atmPVclStatusChangeStart
            atmPVclStatusChangeEnd
            atmPVclLowerRangeValue
            atmPVclHigherRangeValue
            atmPVclRangeStatusChangeStart
            atmPVclRangeStatusChangeEnd
            cvpdnTunnelLocalPort
            cvpdnTunnelRemotePort
            cvpdnTunnelLastChange
            cvpdnTunnelPacketsOut
            cvpdnTunnelBytesOut
            cvpdnTunnelPacketsIn
            cvpdnTunnelBytesIn
            cvpdnTunnelExtEntry.8
            cvpdnTunnelExtEntry.9
            cvpdnSessionRemoteId
            cvpdnSessionInterfaceName
            cvpdnSessionLastChange
            cvpdnSessionOutOfOrderPackets
            cvpdnSessionSequencing
            cvpdnSessionSendSequence
            cvpdnSessionRecvSequence
            cvpdnSessionRemoteSendSequence
            cvpdnSessionRemoteRecvSequence
            cvpdnSessionSentZLB
            cvpdnSessionRecvZLB
            cvpdnSessionSentRBits
            cvpdnSessionRecvRBits
            cvpdnSessionLocalWindowSize
            cvpdnSessionRemoteWindowSize
            cvpdnSessionCurrentWindowSize
            cvpdnSessionMinimumWindowSize
            cvpdnSessionATOTimeouts
            cvpdnSessionOutGoingQueueSize
            cvpdnSessionCalculationType
            cvpdnSessionAdaptiveTimeOut
            cvpdnSessionRoundTripTime
            cvpdnSessionPktProcessingDelay
            cvpdnSessionZLBTime
            cvCommonDcCallActiveConnectionId
            cvCommonDcCallActiveVADEnable
            cvCommonDcCallActiveCoderTypeRate
            cvCommonDcCallActiveCodecBytes
            cvCommonDcCallActiveInBandSignaling
            cvCommonDcCallActiveCallingName
            cvCommonDcCallActiveCallerIDBlock
            cvCommonDcCallHistoryConnectionId
            cvCommonDcCallHistoryVADEnable
            cvCommonDcCallHistoryCoderTypeRate
            cvCommonDcCallHistoryCodecBytes
            cvCommonDcCallHistoryInBandSignaling
            cvCommonDcCallHistoryCallingName
            cvCommonDcCallHistoryCallerIDBlock
            casServerStateChangeEnable
            casAddress
            casAuthenPort
            casAcctPort
            casKey
            casPriority
            casConfigRowStatus
            casAuthenRequests
            casAuthenRequestTimeouts
            casAuthenUnexpectedResponses
            casAuthenServerErrorResponses
            casAuthenIncorrectResponses
            casAuthenResponseTime
            casAuthenTransactionSuccesses
            casAuthenTransactionFailures
            casAuthorRequests
            casAuthorRequestTimeouts
            casAuthorUnexpectedResponses
            casAuthorServerErrorResponses
            casAuthorIncorrectResponses
            casAuthorResponseTime
            casAuthorTransactionSuccesses
            casAuthorTransactionFailures
            casAcctRequests
            casAcctRequestTimeouts
            casAcctUnexpectedResponses
            casAcctServerErrorResponses
            casAcctIncorrectResponses
            casAcctResponseTime
            casAcctTransactionSuccesses
            casAcctTransactionFailures
            casState
            casCurrentStateDuration
            casPreviousStateDuration
            casTotalDeadTime
            casDeadCount
            srpIfEntry.1
            srpIfEntry.2
            srpIfEntry.3
            srpIfEntry.4
            srpIfEntry.5
            srpIfEntry.6
            srpIfEntry.7
            srpIfEntry.8
            srpMACSideEntry.2
            srpMACSideEntry.3
            srpMACSideEntry.4
            srpMACSideEntry.5
            srpMACSideEntry.6
            srpMACSideEntry.7
            srpMACSideEntry.8
            srpMACSideEntry.9
            srpMACSideEntry.10
            srpMACSideEntry.11
            srpMACSideEntry.12
            srpMACSideEntry.13
            srpRingTopologyMapEntry.2
            srpRingTopologyMapEntry.3
            srpRingTopologyMapEntry.4
            srpMACCountersEntry.1
            srpMACCountersEntry.2
            srpMACCountersEntry.3
            srpMACCountersEntry.4
            srpMACCountersEntry.5
            srpMACCountersEntry.6
            srpMACCountersEntry.7
            srpMACCountersEntry.8
            srpMACCountersEntry.9
            srpMACCountersEntry.10
            srpMACCountersEntry.11
            srpMACCountersEntry.12
            srpRingCountersCurrentEntry.2
            srpRingCountersCurrentEntry.3
            srpRingCountersCurrentEntry.4
            srpRingCountersCurrentEntry.5
            srpRingCountersCurrentEntry.6
            srpRingCountersCurrentEntry.7
            srpRingCountersCurrentEntry.8
            srpRingCountersCurrentEntry.9
            srpRingCountersCurrentEntry.10
            srpRingCountersCurrentEntry.11
            srpRingCountersCurrentEntry.12
            srpRingCountersCurrentEntry.13
            srpRingCountersCurrentEntry.14
            srpRingCountersCurrentEntry.15
            srpRingCountersCurrentEntry.16
            srpRingCountersCurrentEntry.17
            srpRingCountersIntervalEntry.3
            srpRingCountersIntervalEntry.4
            srpRingCountersIntervalEntry.5
            srpRingCountersIntervalEntry.6
            srpRingCountersIntervalEntry.7
            srpRingCountersIntervalEntry.8
            srpRingCountersIntervalEntry.9
            srpRingCountersIntervalEntry.10
            srpRingCountersIntervalEntry.11
            srpRingCountersIntervalEntry.12
            srpRingCountersIntervalEntry.13
            srpRingCountersIntervalEntry.14
            srpRingCountersIntervalEntry.15
            srpRingCountersIntervalEntry.16
            srpRingCountersIntervalEntry.17
            srpRingCountersIntervalEntry.18
            srpRingCountersIntervalEntry.19
            srpHostCountersCurrentEntry.2
            srpHostCountersCurrentEntry.3
            srpHostCountersCurrentEntry.4
            srpHostCountersCurrentEntry.5
            srpHostCountersCurrentEntry.6
            srpHostCountersCurrentEntry.7
            srpHostCountersCurrentEntry.8
            srpHostCountersCurrentEntry.9
            srpHostCountersCurrentEntry.10
            srpHostCountersCurrentEntry.11
            srpHostCountersCurrentEntry.12
            srpHostCountersCurrentEntry.13
            srpHostCountersCurrentEntry.14
            srpHostCountersCurrentEntry.15
            srpHostCountersCurrentEntry.16
            srpHostCountersCurrentEntry.17
            srpHostCountersIntervalEntry.3
            srpHostCountersIntervalEntry.4
            srpHostCountersIntervalEntry.5
            srpHostCountersIntervalEntry.6
            srpHostCountersIntervalEntry.7
            srpHostCountersIntervalEntry.8
            srpHostCountersIntervalEntry.9
            srpHostCountersIntervalEntry.10
            srpHostCountersIntervalEntry.11
            srpHostCountersIntervalEntry.12
            srpHostCountersIntervalEntry.13
            srpHostCountersIntervalEntry.14
            srpHostCountersIntervalEntry.15
            srpHostCountersIntervalEntry.16
            srpHostCountersIntervalEntry.17
            srpHostCountersIntervalEntry.18
            srpErrorsCountersCurrentEntry.2
            srpErrorsCountersCurrentEntry.3
            srpErrorsCountersCurrentEntry.4
            srpErrorsCountersCurrentEntry.5
            srpErrorsCountersCurrentEntry.6
            srpErrorsCountersCurrentEntry.7
            srpErrorsCountersCurrentEntry.8
            srpErrorsCountersCurrentEntry.9
            srpErrorsCountersCurrentEntry.10
            srpErrorsCountersIntervalEntry.3
            srpErrorsCountersIntervalEntry.4
            srpErrorsCountersIntervalEntry.5
            srpErrorsCountersIntervalEntry.6
            srpErrorsCountersIntervalEntry.7
            srpErrorsCountersIntervalEntry.8
            srpErrorsCountersIntervalEntry.9
            srpErrorsCountersIntervalEntry.10
            srpErrorsCountersIntervalEntry.11
            srpErrCntCurrEntry.2
            srpErrCntCurrEntry.3
            srpErrCntCurrEntry.4
            srpErrCntCurrEntry.5
            srpErrCntCurrEntry.6
            srpErrCntCurrEntry.7
            srpErrCntCurrEntry.8
            srpErrCntCurrEntry.9
            srpErrCntIntEntry.3
            srpErrCntIntEntry.4
            srpErrCntIntEntry.5
            srpErrCntIntEntry.6
            srpErrCntIntEntry.7
            srpErrCntIntEntry.8
            srpErrCntIntEntry.9
            srpErrCntIntEntry.10
            MPLS-LDP-MIB::mplsLdpLsrId
            MPLS-LDP-MIB::mplsLdpObjects.1.2
            MPLS-LDP-MIB::mplsLdpObjects.2.1
            MPLS-LDP-MIB::mplsLdpEntityEntry.3
            MPLS-LDP-MIB::mplsLdpEntityEntry.4
            MPLS-LDP-MIB::mplsLdpEntityEntry.5
            MPLS-LDP-MIB::mplsLdpEntityEntry.6
            MPLS-LDP-MIB::mplsLdpEntityEntry.7
            MPLS-LDP-MIB::mplsLdpEntityEntry.8
            MPLS-LDP-MIB::mplsLdpEntityEntry.9
            MPLS-LDP-MIB::mplsLdpEntityEntry.10
            MPLS-LDP-MIB::mplsLdpEntityEntry.11
            MPLS-LDP-MIB::mplsLdpEntityEntry.12
            MPLS-LDP-MIB::mplsLdpEntityEntry.13
            MPLS-LDP-MIB::mplsLdpEntityEntry.14
            MPLS-LDP-MIB::mplsLdpEntityEntry.15
            MPLS-LDP-MIB::mplsLdpEntityEntry.16
            MPLS-LDP-MIB::mplsLdpEntityEntry.17
            MPLS-LDP-MIB::mplsLdpEntityEntry.18
            MPLS-LDP-MIB::mplsLdpEntityEntry.19
            MPLS-LDP-MIB::mplsLdpEntityEntry.20
            MPLS-LDP-MIB::mplsLdpEntityEntry.21
            MPLS-LDP-MIB::mplsLdpEntityEntry.22
            MPLS-LDP-MIB::mplsLdpEntityEntry.23
            MPLS-LDP-MIB::mplsLdpEntityConfGenLREntry.3
            MPLS-LDP-MIB::mplsLdpEntityConfGenLREntry.4
            MPLS-LDP-MIB::mplsLdpEntityConfGenLREntry.5
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.1
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.2
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.3
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.4
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.5
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.6
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.7
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.8
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.9
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.10
            MPLS-LDP-MIB::mplsLdpEntityAtmParmsEntry.11
            MPLS-LDP-MIB::mplsLdpEntityConfAtmLREntry.3
            MPLS-LDP-MIB::mplsLdpEntityConfAtmLREntry.4
            MPLS-LDP-MIB::mplsLdpEntityConfAtmLREntry.5
            MPLS-LDP-MIB::mplsLdpEntityConfAtmLREntry.6
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.1
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.2
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.3
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.4
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.5
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.6
            MPLS-LDP-MIB::mplsLdpEntityFrParmsEntry.7
            MPLS-LDP-MIB::mplsLdpEntityConfFrLREntry.2
            MPLS-LDP-MIB::mplsLdpEntityConfFrLREntry.3
            MPLS-LDP-MIB::mplsLdpEntityConfFrLREntry.4
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.1
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.2
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.3
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.4
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.5
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.6
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.7
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.8
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.9
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.10
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.11
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.12
            MPLS-LDP-MIB::mplsLdpEntityStatsEntry.13
            MPLS-LDP-MIB::mplsLdpPeerEntry.2
            MPLS-LDP-MIB::mplsLdpPeerEntry.3
            MPLS-LDP-MIB::mplsLdpPeerEntry.4
            MPLS-LDP-MIB::mplsLdpHelloAdjacencyEntry.2
            MPLS-LDP-MIB::mplsLdpHelloAdjacencyEntry.3
            MPLS-LDP-MIB::mplsLdpObjects.3.3
            MPLS-LDP-MIB::mplsLdpSessionEntry.1
            MPLS-LDP-MIB::mplsLdpSessionEntry.2
            MPLS-LDP-MIB::mplsLdpSessionEntry.3
            MPLS-LDP-MIB::mplsLdpSessionEntry.4
            MPLS-LDP-MIB::mplsLdpSessionEntry.5
            MPLS-LDP-MIB::mplsLdpAtmSesEntry.3
            MPLS-LDP-MIB::mplsLdpAtmSesEntry.4
            MPLS-LDP-MIB::mplsLdpFrameRelaySesEntry.2
            MPLS-LDP-MIB::mplsLdpFrameRelaySesEntry.3
            MPLS-LDP-MIB::mplsLdpSesStatsEntry.1
            MPLS-LDP-MIB::mplsLdpSesStatsEntry.2
            MPLS-LDP-MIB::mplsLdpObjects.3.8.1
            MPLS-LDP-MIB::mplsFecEntry.2
            MPLS-LDP-MIB::mplsFecEntry.3
            MPLS-LDP-MIB::mplsFecEntry.4
            MPLS-LDP-MIB::mplsFecEntry.5
            MPLS-LDP-MIB::mplsFecEntry.6
            MPLS-LDP-MIB::mplsFecEntry.7
            MPLS-LDP-MIB::mplsLdpSesInLabelMapEntry.3
            MPLS-LDP-MIB::mplsLdpSesInLabelMapEntry.4
            MPLS-LDP-MIB::mplsLdpSesOutLabelMapEntry.3
            MPLS-LDP-MIB::mplsLdpSesOutLabelMapEntry.4
            MPLS-LDP-MIB::mplsLdpSesOutLabelMapEntry.5
            MPLS-LDP-MIB::mplsLdpSesXCMapEntry.1
            MPLS-LDP-MIB::mplsLdpSesPeerAddrEntry.2
            MPLS-LDP-MIB::mplsLdpSesPeerAddrEntry.3
            MPLS-LDP-MIB::mplsXCsFecsEntry.1
            MPLS-LDP-MIB::mplsXCsFecsEntry.2
            cnatInterfaceRealm
            cnatInterfaceStorageType
            cnatInterfaceStatus
            cnatAddrBindNumberOfEntries
            cnatAddrBindGlobalAddr
            cnatAddrBindId
            cnatAddrBindDirection
            cnatAddrBindType
            cnatAddrBindCurrentIdleTime
            cnatAddrBindInTranslate
            cnatAddrBindOutTranslate
            cnatAddrPortBindNumberOfEntries
            cnatAddrPortBindGlobalAddr
            cnatAddrPortBindGlobalPort
            cnatAddrPortBindId
            cnatAddrPortBindDirection
            cnatAddrPortBindType
            cnatAddrPortBindCurrentIdleTime
            cnatAddrPortBindInTranslate
            cnatAddrPortBindOutTranslate
            cnatProtocolStatsInTranslate
            cnatProtocolStatsOutTranslate
            cnatProtocolStatsRejectCount
            ceemEventMapEntry.2
            ceemEventMapEntry.3
            ceemHistory.1
            ceemHistoryLastEventEntry
            ceemHistoryEventEntry.2
            ceemHistoryEventEntry.3
            ceemHistoryEventEntry.4
            ceemHistoryEventEntry.5
            ceemHistoryEventEntry.6
            ceemHistoryEventEntry.7
            ceemHistoryEventEntry.8
            ceemHistoryEventEntry.9
            ceemHistoryEventEntry.10
            ceemHistoryEventEntry.11
            ceemHistoryEventEntry.12
            ceemHistoryEventEntry.13
            ceemHistoryEventEntry.14
            ceemHistoryEventEntry.15
            ceemHistoryEventEntry.16
            ceemRegisteredPolicyEntry.2
            ceemRegisteredPolicyEntry.3
            ceemRegisteredPolicyEntry.4
            ceemRegisteredPolicyEntry.5
            ceemRegisteredPolicyEntry.6
            ceemRegisteredPolicyEntry.7
            ceemRegisteredPolicyEntry.8
            ceemRegisteredPolicyEntry.9
            ceemRegisteredPolicyEntry.10
            ceemRegisteredPolicyEntry.11
            ceemRegisteredPolicyEntry.12
            ceemRegisteredPolicyEntry.13
            ceemRegisteredPolicyEntry.14
            ceemRegisteredPolicyEntry.15
            ceemRegisteredPolicyEntry.16
            ceemRegisteredPolicyEntry.17
            catmIntfCurrentlyDownToUpPVcls
            catmIntfOAMFailedPVcls
            catmIntfCurrentOAMFailingPVcls
            catmIntfSegCCOAMFailedPVcls
            catmIntfCurSegCCOAMFailingPVcls
            catmIntfEndCCOAMFailedPVcls
            catmIntfCurEndCCOAMFailingPVcls
            catmIntfAISRDIOAMFailedPVcls
            catmIntfCurAISRDIOAMFailingPVcls
            catmIntfAnyOAMFailedPVcls
            catmIntfCurAnyOAMFailingPVcls
            catmIntfTypeOfOAMFailure
            catmIntfOAMRcovedPVcls
            catmIntfCurrentOAMRcovingPVcls
            catmIntfSegCCOAMRcovedPVcls
            catmIntfCurSegCCOAMRcovingPVcls
            catmIntfEndCCOAMRcovedPVcls
            catmIntfCurEndCCOAMRcovingPVcls
            catmIntfAISRDIOAMRcovedPVcls
            catmIntfCurAISRDIOAMRcovingPVcls
            catmIntfAnyOAMRcovedPVcls
            catmIntfCurAnyOAMRcovingPVcls
            catmIntfTypeOfOAMRecover
            catmIntfSegAISRDIFailedPVcls
            catmIntfCurSegAISRDIFailingPVcls
            catmIntfEndAISRDIFailedPVcls
            catmIntfCurEndAISRDIFailingPVcls
            catmIntfSegAISRDIRcovedPVcls
            catmIntfCurSegAISRDIRcovingPVcls
            catmIntfEndAISRDIRcovedPVcls
            catmIntfCurEndAISRDIRcovingPVcls
            catmPVclStatusTransition
            catmPVclStatusChangeStart
            catmPVclStatusChangeEnd
            catmPVclSegCCStatusTransition
            catmPVclSegCCStatusChangeStart
            catmPVclSegCCStatusChangeEnd
            catmPVclEndCCStatusTransition
            catmPVclEndCCStatusChangeStart
            catmPVclEndCCStatusChangeEnd
            catmPVclAISRDIStatusTransition
            catmPVclAISRDIStatusChangeStart
            catmPVclAISRDIStatusChangeEnd
            catmPVclCurFailTime
            catmPVclPrevRecoverTime
            catmPVclFailureReason
            catmPVclSegAISRDIStatTransition
            catmPVclSegAISRDIStatChangeStart
            catmPVclSegAISRDIStatChangeEnd
            catmPVclEndAISRDIStatTransition
            catmPVclEndAISRDIStatChangeStart
            catmPVclEndAISRDIStatChangeEnd
            catmPVclLowerRangeValue
            catmPVclHigherRangeValue
            catmPVclRangeStatusChangeStart
            catmPVclRangeStatusChangeEnd
            catmPVclSegCCLowerRangeValue
            catmPVclSegCCHigherRangeValue
            catmPVclSegCCRangeStatusChStart
            catmPVclSegCCRangeStatusChEnd
            catmPVclEndCCLowerRangeValue
            catmPVclEndCCHigherRangeValue
            catmPVclEndCCRangeStatusChStart
            catmPVclEndCCRangeStatusChEnd
            catmPVclAISRDILowerRangeValue
            catmPVclAISRDIHigherRangeValue
            catmPVclAISRDIRangeStatusChStart
            catmPVclAISRDIRangeStatusChEnd
            catmDownPVclLowerRangeValue
            catmDownPVclHigherRangeValue
            catmDownPVclRangeStart
            catmDownPVclRangeEnd
            catmPrevUpPVclRangeStart
            catmPrevUpPVclRangeEnd
            catmPVclRangeFailureReason
            catmPVclStatusUpTransition
            catmPVclStatusUpStart
            catmPVclStatusUpEnd
            catmPVclSegCCStatusUpTransition
            catmPVclSegCCStatusUpStart
            catmPVclSegCCStatusUpEnd
            catmPVclEndCCStatusUpTransition
            catmPVclEndCCStatusUpStart
            catmPVclEndCCStatusUpEnd
            catmPVclAISRDIStatusUpTransition
            catmPVclAISRDIStatusUpStart
            catmPVclAISRDIStatusUpEnd
            catmPVclCurRecoverTime
            catmPVclPrevFailTime
            catmPVclRecoveryReason
            catmPVclSegAISRDIStatUpTransit
            catmPVclSegAISRDIStatUpStart
            catmPVclSegAISRDIStatUpEnd
            catmPVclEndAISRDIStatUpTransit
            catmPVclEndAISRDIStatUpStart
            catmPVclEndAISRDIStatUpEnd
            catmPVclUpLowerRangeValue
            catmPVclUpHigherRangeValue
            catmPVclRangeStatusUpStart
            catmPVclRangeStatusUpEnd
            catmPVclSegCCUpLowerRangeValue
            catmPVclSegCCUpHigherRangeValue
            catmPVclSegCCRangeStatusUpStart
            catmPVclSegCCRangeStatusUpEnd
            catmPVclEndCCUpLowerRangeValue
            catmPVclEndCCUpHigherRangeValue
            catmPVclEndCCRangeStatusUpStart
            catmPVclEndCCRangeStatusUpEnd
            catmPVclAISRDIUpLowerRangeValue
            catmPVclAISRDIUpHigherRangeValue
            catmPVclAISRDIRangeStatusUpStart
            catmPVclAISRDIRangeStatusUpEnd
            catmUpPVclLowerRangeValue
            catmUpPVclHigherRangeValue
            catmUpPVclRangeStart
            catmUpPVclRangeEnd
            catmPrevDownPVclRangeStart
            catmPrevDownPVclRangeEnd
            catmPVclRangeRecoveryReason
            catmPVclSegAISRDILowerRangeValue
            catmPVclSegAISRDIHigherRangeValue
            catmPVclSegAISRDIRangeStatChStart
            catmPVclSegAISRDIRangeStatChEnd
            catmPVclEndAISRDILowerRangeValue
            catmPVclEndAISRDIHigherRngeValue
            catmPVclEndAISRDIRngeStatChStart
            catmPVclEndAISRDIRangeStatChEnd
            catmPVclSegAISRDIUpLowerRangeVal
            catmPVclSegAISRDIUpHigherRngeVal
            catmPVclSegAISRDIRngeStatUpStart
            catmPVclSegAISRDIRangeStatUpEnd
            catmPVclEndAISRDIUpLowerRangeVal
            catmPVclEndAISRDIUpHigherRngeVal
            catmPVclEndAISRDIRngeStatUpStart
            catmPVclEndAISRDIRangeStatUpEnd
            cmplsFrrMIB.1.1
            cmplsFrrMIB.1.2
            cmplsFrrMIB.1.3
            cmplsFrrMIB.1.4
            cmplsFrrMIB.1.5
            cmplsFrrMIB.1.6
            cmplsFrrMIB.1.7
            cmplsFrrMIB.1.8
            cmplsFrrMIB.1.9
            cmplsFrrMIB.1.10
            cmplsFrrMIB.1.11
            cmplsFrrMIB.1.12
            cmplsFrrMIB.1.13
            cmplsFrrMIB.1.14
            cmplsFrrConstEntry.4
            cmplsFrrConstEntry.5
            cmplsFrrConstEntry.6
            cmplsFrrConstEntry.7
            cmplsFrrConstEntry.8
            cmplsFrrConstEntry.9
            cmplsFrrConstEntry.10
            cmplsFrrConstEntry.11
            cmplsFrrConstEntry.12
            cmplsFrrConstEntry.13
            cmplsFrrMIB.10.9.2.1.2
            cmplsFrrMIB.10.9.2.1.3
            cmplsFrrMIB.10.9.2.1.4
            cmplsFrrMIB.10.9.2.1.5
            cmplsFrrMIB.10.9.2.1.6
            cmplsFrrFacRouteDBEntry.7
            cmplsFrrFacRouteDBEntry.8
            cmplsFrrFacRouteDBEntry.9
            frasBnnSdlc
            frasBnnLlc
            frasBanSdlc
            frasBanLlc
            cospfGeneralGroup.5
            cospfAreaEntry.1
            cospfAreaEntry.2
            cospfAreaEntry.3
            cospfAreaEntry.4
            cospfAreaEntry.5
            cospfLsdbEntry.2
            cospfLsdbEntry.3
            cospfLsdbEntry.4
            cospfLsdbEntry.5
            cospfIfEntry.1
            cospfIfEntry.2
            cospfVirtIfEntry.1
            cospfVirtIfEntry.2
            cospfShamLinkEntry.4
            cospfShamLinkEntry.5
            cospfShamLinkEntry.6
            cospfShamLinkEntry.7
            cospfShamLinkEntry.8
            cospfShamLinkEntry.9
            cospfLocalLsdbEntry.6
            cospfLocalLsdbEntry.7
            cospfLocalLsdbEntry.8
            cospfLocalLsdbEntry.9
            cospfVirtLocalLsdbEntry.6
            cospfVirtLocalLsdbEntry.7
            cospfVirtLocalLsdbEntry.8
            cospfVirtLocalLsdbEntry.9
            cospfShamLinkNbrEntry.4
            cospfShamLinkNbrEntry.5
            cospfShamLinkNbrEntry.6
            cospfShamLinkNbrEntry.7
            cospfShamLinkNbrEntry.8
            cospfShamLinkNbrEntry.9
            cospfShamLinksEntry.6
            cospfShamLinksEntry.7
            cospfShamLinksEntry.8
            cospfShamLinksEntry.9
            cospfShamLinksEntry.10
            cospfShamLinksEntry.11
            cospfTrapControl.1
            cospfTrapControl.2
            cospfTrapControl.3
            cospfTrapControl.4
            cDhcpv4SrvSystemDescr
            cDhcpv4SrvSystemObjectID
            cDhcpv4ServerSharedNetFreeAddrLowThreshold
            cDhcpv4ServerSharedNetFreeAddrHighThreshold
            cDhcpv4ServerSharedNetFreeAddresses
            cDhcpv4ServerSharedNetReservedAddresses
            cDhcpv4ServerSharedNetTotalAddresses
            cDhcpv4ServerSubnetMask
            cDhcpv4ServerSubnetSharedNetworkName
            cDhcpv4ServerSubnetFreeAddrLowThreshold
            cDhcpv4ServerSubnetFreeAddrHighThreshold
            cDhcpv4ServerSubnetFreeAddresses
            cDhcpv4ServerRangeSubnetMask
            cDhcpv4ServerRangeInUse
            cDhcpv4ServerRangeOutstandingOffers
            cDhcpv4ServerClientSubnetMask
            cDhcpv4ServerClientRange
            cDhcpv4ServerClientLeaseType
            cDhcpv4ServerClientTimeRemaining
            cDhcpv4ServerClientAllowedProtocol
            cDhcpv4ServerClientServedProtocol
            cDhcpv4ServerClientPhysicalAddress
            cDhcpv4ServerClientClientId
            cDhcpv4ServerClientHostName
            cDhcpv4ServerClientDomainName
            cBootpHCCountRequests
            cBootpHCCountInvalids
            cBootpHCCountReplies
            cBootpHCCountDropUnknownClients
            cBootpHCCountDropNotServingSubnet
            cDhcpv4HCCountDiscovers
            cDhcpv4HCCountOffers
            cDhcpv4HCCountRequests
            cDhcpv4HCCountDeclines
            cDhcpv4HCCountAcks
            cDhcpv4HCCountNaks
            cDhcpv4HCCountReleases
            cDhcpv4HCCountInforms
            cDhcpv4HCCountForcedRenews
            cDhcpv4HCCountInvalids
            cDhcpv4HCCountDropUnknownClient
            cDhcpv4HCCountDropNotServingSubnet
            cpwVcIndexNext
            cpwVcType
            cpwVcOwner
            cpwVcPsnType
            cpwVcSetUpPriority
            cpwVcHoldingPriority
            cpwVcInboundMode
            cpwVcPeerAddrType
            cpwVcPeerAddr
            cpwVcID
            cpwVcLocalGroupID
            cpwVcControlWord
            cpwVcLocalIfMtu
            cpwVcLocalIfString
            cpwVcRemoteGroupID
            cpwVcRemoteControlWord
            cpwVcRemoteIfMtu
            cpwVcRemoteIfString
            cpwVcOutboundVcLabel
            cpwVcInboundVcLabel
            cpwVcName
            cpwVcDescr
            cpwVcCreateTime
            cpwVcUpTime
            cpwVcAdminStatus
            cpwVcOperStatus
            cpwVcInboundOperStatus
            cpwVcOutboundOperStatus
            cpwVcTimeElapsed
            cpwVcValidIntervals
            cpwVcRowStatus
            cpwVcStorageType
            cpwVcPerfCurrentInHCPackets
            cpwVcPerfCurrentInHCBytes
            cpwVcPerfCurrentOutHCPackets
            cpwVcPerfCurrentOutHCBytes
            cpwVcPerfIntervalValidData
            cpwVcPerfIntervalTimeElapsed
            cpwVcPerfIntervalInHCPackets
            cpwVcPerfIntervalInHCBytes
            cpwVcPerfIntervalOutHCPackets
            cpwVcPerfIntervalOutHCBytes
            cpwVcPerfTotalInHCPackets
            cpwVcPerfTotalInHCBytes
            cpwVcPerfTotalOutHCPackets
            cpwVcPerfTotalOutHCBytes
            cpwVcPerfTotalDiscontinuityTime
            cpwVcPerfTotalErrorPackets
            cpwVcIdMappingVcIndex
            cpwVcPeerMappingVcIndex
            cpwVcUpDownNotifEnable
            cpwVcNotifRate
            cpwVcMplsEntry.1
            cpwVcMplsEntry.2
            cpwVcMplsEntry.3
            cpwVcMplsEntry.4
            cpwVcMplsEntry.5
            cpwVcMplsEntry.6
            cpwVcMplsEntry.7
            cpwVcMplsEntry.8
            cpwVcMplsMIB.1.2
            cpwVcMplsOutboundEntry.2
            cpwVcMplsOutboundEntry.3
            cpwVcMplsOutboundEntry.4
            cpwVcMplsOutboundEntry.5
            cpwVcMplsOutboundEntry.6
            cpwVcMplsOutboundEntry.7
            cpwVcMplsOutboundEntry.8
            cpwVcMplsOutboundEntry.9
            cpwVcMplsMIB.1.4
            cpwVcMplsInboundEntry.2
            cpwVcMplsInboundEntry.3
            cpwVcMplsInboundEntry.4
            cpwVcMplsInboundEntry.5
            cpwVcMplsInboundEntry.6
            cpwVcMplsInboundEntry.7
            cpwVcMplsInboundEntry.8
            cpwVcMplsInboundEntry.9
            cpwVcMplsNonTeMappingEntry.4
            cpwVcMplsTeMappingEntry.6
            ciscoExperiment.10.151.1.1.2
            ciscoExperiment.10.151.1.1.3
            ciscoExperiment.10.151.1.1.4
            ciscoExperiment.10.151.1.1.5
            ciscoExperiment.10.151.1.1.6
            ciscoExperiment.10.151.1.1.7
            ciscoExperiment.10.151.2.1.1
            ciscoExperiment.10.151.2.1.2
            ciscoExperiment.10.151.2.1.3
            ciscoExperiment.10.151.3.1.1
            ciscoExperiment.10.151.3.1.2
            ciscoExperiment.10.19.1.1.2
            ciscoExperiment.10.19.1.1.3
            ciscoExperiment.10.19.1.1.4
            ciscoExperiment.10.19.1.1.5
            ciscoExperiment.10.19.1.1.6
            ciscoExperiment.10.19.1.1.7
            ciscoExperiment.10.19.1.1.8
            ciscoExperiment.10.19.2.1.2
            ciscoExperiment.10.19.2.1.3
            ciscoExperiment.10.19.2.1.4
            ciscoExperiment.10.19.2.1.5
            ciscoExperiment.10.19.2.1.6
            ciscoExperiment.10.19.2.1.7
            ciscoMvpnScalars.1
            ciscoMvpnScalars.2
            ciscoMvpnGeneric.1.1.1
            ciscoMvpnGeneric.1.1.2
            ciscoMvpnGeneric.1.1.3
            ciscoMvpnGeneric.1.1.4
            ciscoMvpnConfig.1.1.1
            ciscoMvpnConfig.1.1.2
            ciscoMvpnConfig.1.1.3
            ciscoMvpnConfig.1.1.4
            ciscoMvpnConfig.2.1.1
            ciscoMvpnConfig.2.1.2
            ciscoMvpnConfig.2.1.3
            ciscoMvpnConfig.2.1.4
            ciscoMvpnConfig.2.1.5
            ciscoMvpnConfig.2.1.6
            ciscoMvpnProtocol.1.1.6
            ciscoMvpnProtocol.1.1.7
            ciscoMvpnProtocol.1.1.8
            ciscoMvpnProtocol.2.1.3
            ciscoMvpnProtocol.2.1.6
            ciscoMvpnProtocol.2.1.7
            ciscoMvpnProtocol.2.1.8
            ciscoMvpnProtocol.2.1.9
            ciscoMvpnProtocol.3.1.5
            ciscoMvpnProtocol.3.1.6
            ciscoMvpnProtocol.4.1.5
            ciscoMvpnProtocol.4.1.6
            ciscoMvpnProtocol.4.1.7
            ciscoMvpnProtocol.5.1.1
            ciscoMvpnProtocol.5.1.2
            ciiSysObject.1
            ciiSysObject.2
            ciiSysObject.3
            ciiSysObject.4
            ciiSysObject.5
            ciiSysObject.6
            ciiSysObject.8
            ciiSysObject.9
            ciiSysObject.10
            ciiSysObject.11
            ciiManAreaAddrEntry.2
            ciiAreaAddrEntry.1
            ciiSysProtSuppEntry.2
            ciiSummAddrEntry.4
            ciiSummAddrEntry.5
            ciiSummAddrEntry.6
            ciiRedistributeAddrEntry.4
            ciiRouterEntry.3
            ciiRouterEntry.4
            ciiSysLevelEntry.2
            ciiSysLevelEntry.3
            ciiSysLevelEntry.4
            ciiSysLevelEntry.5
            ciiSysLevelEntry.6
            ciiSysLevelEntry.7
            ciiSysLevelEntry.8
            ciiSysLevelEntry.9
            ciiCircEntry.2
            ciiCircEntry.3
            ciiCircEntry.4
            ciiCircEntry.5
            ciiCircEntry.6
            ciiCircEntry.8
            ciiCircEntry.9
            ciiCircEntry.10
            ciiCircEntry.11
            ciiCircEntry.12
            ciiCircEntry.13
            ciiCircEntry.14
            ciiCircEntry.15
            ciiCircLevelEntry.2
            ciiCircLevelEntry.3
            ciiCircLevelEntry.4
            ciiCircLevelEntry.5
            ciiCircLevelEntry.6
            ciiCircLevelEntry.7
            ciiCircLevelEntry.8
            ciiCircLevelEntry.9
            ciiCircLevelEntry.10
            ciiCircLevelEntry.11
            ciiCircLevelEntry.12
            ciiCircLevelEntry.13
            ciiCircLevelEntry.14
            ciiSystemCounterEntry.2
            ciiSystemCounterEntry.3
            ciiSystemCounterEntry.4
            ciiSystemCounterEntry.5
            ciiSystemCounterEntry.6
            ciiSystemCounterEntry.7
            ciiSystemCounterEntry.8
            ciiSystemCounterEntry.9
            ciiSystemCounterEntry.10
            ciiSystemCounterEntry.12
            ciiSystemCounterEntry.13
            ciiCircuitCounterEntry.2
            ciiCircuitCounterEntry.3
            ciiCircuitCounterEntry.5
            ciiCircuitCounterEntry.6
            ciiCircuitCounterEntry.7
            ciiCircuitCounterEntry.8
            ciiCircuitCounterEntry.9
            ciiCircuitCounterEntry.10
            ciiPacketCounterEntry.3
            ciiPacketCounterEntry.4
            ciiPacketCounterEntry.5
            ciiPacketCounterEntry.6
            ciiPacketCounterEntry.7
            ciiPacketCounterEntry.8
            ciiPacketCounterEntry.9
            ciiISAdjEntry.2
            ciiISAdjEntry.3
            ciiISAdjEntry.4
            ciiISAdjEntry.5
            ciiISAdjEntry.6
            ciiISAdjEntry.7
            ciiISAdjEntry.8
            ciiISAdjEntry.9
            ciiISAdjEntry.10
            ciiISAdjEntry.11
            ciiISAdjAreaAddrEntry.2
            ciiISAdjIPAddrEntry.2
            ciiISAdjIPAddrEntry.3
            ciiISAdjProtSuppEntry.1
            ciiRAEntry.2
            ciiRAEntry.3
            ciiRAEntry.4
            ciiRAEntry.5
            ciiRAEntry.6
            ciiRAEntry.7
            ciiRAEntry.8
            ciiRAEntry.11
            ciiIPRAEntry.5
            ciiIPRAEntry.6
            ciiIPRAEntry.7
            ciiIPRAEntry.8
            ciiIPRAEntry.9
            ciiIPRAEntry.10
            ciiIPRAEntry.11
            ciiIPRAEntry.12
            ciiIPRAEntry.13
            ciiIPRAEntry.14
            ciiLSPSummaryEntry.3
            ciiLSPSummaryEntry.4
            ciiLSPSummaryEntry.5
            ciiLSPSummaryEntry.6
            ciiLSPSummaryEntry.7
            ciiLSPSummaryEntry.8
            ciiLSPTLVEntry.2
            ciiLSPTLVEntry.3
            ciiLSPTLVEntry.4
            ciiLSPTLVEntry.5
            ciiLSPTLVEntry.6
            cpwAtmIf
            cpwAtmVpi
            cpwAtmVci
            cpwAtmClpQosMapping
            cpwAtmRowStatus
            cpwAtmOamCellSupported
            cpwAtmQosScalingFactor
            cpwAtmCellPacking
            cpwAtmMncp
            cpwAtmPeerMncp
            cpwAtmEncap
            cpwAtmMcptTimeout
            cpwAtmCellsReceived
            cpwAtmCellsSent
            cpwAtmCellsRejected
            cpwAtmCellsTagged
            cpwAtmHCCellsReceived
            cpwAtmHCCellsRejected
            cpwAtmHCCellsTagged
            cpwAtmAvgCellsPacked
            cpwAtmPktsReceived
            cpwAtmPktsSent
            cpwAtmPktsRejected
            cDhcpv4ServerDefaultRouterAddress
            cDhcpv4ServerSubnetStartAddress
            cDhcpv4ServerSubnetEndAddress
            cDhcpv4ServerIfLeaseLimit
            cdot3OamAdminState
            cdot3OamOperStatus
            cdot3OamMode
            cdot3OamMaxOamPduSize
            cdot3OamConfigRevision
            cdot3OamFunctionsSupported
            cdot3OamPeerMacAddress
            cdot3OamPeerVendorOui
            cdot3OamPeerVendorInfo
            cdot3OamPeerMode
            cdot3OamPeerMaxOamPduSize
            cdot3OamPeerConfigRevision
            cdot3OamPeerFunctionsSupported
            cdot3OamLoopbackStatus
            cdot3OamLoopbackIgnoreRx
            cdot3OamInformationTx
            cdot3OamInformationRx
            cdot3OamUniqueEventNotificationTx
            cdot3OamUniqueEventNotificationRx
            cdot3OamDuplicateEventNotificationTx
            cdot3OamDuplicateEventNotificationRx
            cdot3OamLoopbackControlTx
            cdot3OamLoopbackControlRx
            cdot3OamVariableRequestTx
            cdot3OamVariableRequestRx
            cdot3OamVariableResponseTx
            cdot3OamVariableResponseRx
            cdot3OamOrgSpecificTx
            cdot3OamOrgSpecificRx
            cdot3OamUnsupportedCodesTx
            cdot3OamUnsupportedCodesRx
            cdot3OamFramesLostDueToOam
            cdot3OamErrSymPeriodWindowHi
            cdot3OamErrSymPeriodWindowLo
            cdot3OamErrSymPeriodThresholdHi
            cdot3OamErrSymPeriodThresholdLo
            cdot3OamErrSymPeriodEvNotifEnable
            cdot3OamErrFramePeriodWindow
            cdot3OamErrFramePeriodThreshold
            cdot3OamErrFramePeriodEvNotifEnable
            cdot3OamErrFrameWindow
            cdot3OamErrFrameThreshold
            cdot3OamErrFrameEvNotifEnable
            cdot3OamErrFrameSecsSummaryWindow
            cdot3OamErrFrameSecsSummaryThreshold
            cdot3OamErrFrameSecsEvNotifEnable
            cdot3OamDyingGaspEnable
            cdot3OamCriticalEventEnable
            cdot3OamEventLogTimestamp
            cdot3OamEventLogOui
            cdot3OamEventLogType
            cdot3OamEventLogLocation
            cdot3OamEventLogWindowHi
            cdot3OamEventLogWindowLo
            cdot3OamEventLogThresholdHi
            cdot3OamEventLogThresholdLo
            cdot3OamEventLogValue
            cdot3OamEventLogRunningTotal
            cdot3OamEventLogEventTotal
            ciscoBfdObjects.1.1
            ciscoBfdObjects.1.3
            ciscoBfdObjects.1.4
            ciscoBfdSessEntry.2
            ciscoBfdSessEntry.3
            ciscoBfdSessEntry.4
            ciscoBfdSessEntry.5
            ciscoBfdSessEntry.6
            ciscoBfdSessEntry.7
            ciscoBfdSessDiag
            ciscoBfdSessEntry.9
            ciscoBfdSessEntry.10
            ciscoBfdSessEntry.11
            ciscoBfdSessEntry.12
            ciscoBfdSessEntry.13
            ciscoBfdSessEntry.14
            ciscoBfdSessEntry.15
            ciscoBfdSessEntry.16
            ciscoBfdSessEntry.17
            ciscoBfdSessEntry.18
            ciscoBfdSessEntry.19
            ciscoBfdSessEntry.20
            ciscoBfdSessEntry.21
            ciscoBfdSessEntry.22
            ciscoBfdSessPerfEntry.1
            ciscoBfdSessPerfEntry.2
            ciscoBfdSessPerfEntry.3
            ciscoBfdSessPerfEntry.4
            ciscoBfdSessPerfEntry.5
            ciscoBfdSessPerfEntry.6
            ciscoBfdSessPerfEntry.7
            ciscoBfdSessPerfEntry.8
            ciscoBfdSessPerfEntry.9
            ciscoBfdSessMapEntry.1
            cmplsXCExtTunnelPointer
            cmplsXCOppositeDirXCPtr
            cmplsNodeConfigGlobalId
            cmplsNodeConfigNodeId
            cmplsNodeConfigIccId
            cmplsNodeConfigRowStatus
            cmplsNodeConfigStorageType
            cmplsNodeIpMapLocalId
            cmplsNodeIccMapLocalId
            cmplsTunnelOppositeDirPtr
            cmplsTunnelExtOppositeDirTnlValid
            cmplsTunnelExtDestTnlIndex
            cmplsTunnelExtDestTnlLspIndex
            cmplsTunnelExtDestTnlValid
            cmplsTunnelReversePerfPackets
            cmplsTunnelReversePerfHCPackets
            cmplsTunnelReversePerfErrors
            cmplsTunnelReversePerfBytes
            cmplsTunnelReversePerfHCBytes
            ipxBasicSysEntry.1
            ipxBasicSysEntry.2
            ipxBasicSysEntry.3
            ipxBasicSysEntry.4
            ipxBasicSysEntry.5
            ipxBasicSysEntry.6
            ipxBasicSysEntry.7
            ipxBasicSysEntry.8
            ipxBasicSysEntry.9
            ipxBasicSysEntry.10
            ipxBasicSysEntry.11
            ipxBasicSysEntry.12
            ipxBasicSysEntry.13
            ipxBasicSysEntry.14
            ipxBasicSysEntry.15
            ipxBasicSysEntry.16
            ipxBasicSysEntry.17
            ipxBasicSysEntry.18
            ipxAdvSysEntry.1
            ipxAdvSysEntry.2
            ipxAdvSysEntry.3
            ipxAdvSysEntry.4
            ipxAdvSysEntry.5
            ipxAdvSysEntry.6
            ipxAdvSysEntry.7
            ipxAdvSysEntry.8
            ipxAdvSysEntry.9
            ipxAdvSysEntry.10
            ipxAdvSysEntry.11
            ipxAdvSysEntry.12
            ipxAdvSysEntry.13
            ipxCircEntry.1
            ipxCircEntry.2
            ipxCircEntry.3
            ipxCircEntry.4
            ipxCircEntry.5
            ipxCircEntry.6
            ipxCircEntry.7
            ipxCircEntry.8
            ipxCircEntry.9
            ipxCircEntry.10
            ipxCircEntry.11
            ipxCircEntry.12
            ipxCircEntry.13
            ipxCircEntry.14
            ipxCircEntry.15
            ipxCircEntry.16
            ipxCircEntry.17
            ipxCircEntry.18
            ipxCircEntry.19
            ipxCircEntry.20
            ipxCircEntry.21
            ipxCircEntry.22
            ipxCircEntry.23
            ipxCircEntry.24
            ipxCircEntry.25
            ipxCircEntry.26
            ipxCircEntry.27
            ipxCircEntry.28
            ipxDestEntry.1
            ipxDestEntry.2
            ipxDestEntry.3
            ipxDestEntry.4
            ipxDestEntry.5
            ipxDestEntry.6
            ipxDestEntry.7
            ipxDestEntry.8
            ipxStaticRouteEntry.1
            ipxStaticRouteEntry.2
            ipxStaticRouteEntry.3
            ipxStaticRouteEntry.4
            ipxStaticRouteEntry.5
            ipxStaticRouteEntry.6
            ipxServEntry.1
            ipxServEntry.2
            ipxServEntry.3
            ipxServEntry.4
            ipxServEntry.5
            ipxServEntry.6
            ipxServEntry.7
            ipxServEntry.8
            ipxDestServEntry.1
            ipxDestServEntry.2
            ipxDestServEntry.3
            ipxDestServEntry.4
            ipxDestServEntry.5
            ipxDestServEntry.6
            ipxDestServEntry.7
            ipxDestServEntry.8
            ipxStaticServEntry.1
            ipxStaticServEntry.2
            ipxStaticServEntry.3
            ipxStaticServEntry.4
            ipxStaticServEntry.5
            ipxStaticServEntry.6
            ipxStaticServEntry.7
            ipxStaticServEntry.8
            ipxStaticServEntry.9
            ripSysEntry.1
            ripSysEntry.2
            ripSysEntry.3
            sapSysEntry.1
            sapSysEntry.2
            sapSysEntry.3
            ripCircEntry.1
            ripCircEntry.2
            ripCircEntry.3
            ripCircEntry.4
            ripCircEntry.5
            ripCircEntry.6
            ripCircEntry.7
            ripCircEntry.8
            ripCircEntry.9
            sapCircEntry.1
            sapCircEntry.2
            sapCircEntry.3
            sapCircEntry.4
            sapCircEntry.5
            sapCircEntry.6
            sapCircEntry.7
            sapCircEntry.8
            sapCircEntry.9
            sapCircEntry.10
            atmfPortEntry.1
            atmfPortEntry.3
            atmfPortEntry.4
            atmfPortEntry.5
            atmfPortEntry.6
            atmfPortEntry.7
            atmfPortEntry.8
            atmfPhysicalGroup.2
            atmfPhysicalGroup.4
            atmfAtmLayerEntry.1
            atmfAtmLayerEntry.2
            atmfAtmLayerEntry.3
            atmfAtmLayerEntry.4
            atmfAtmLayerEntry.5
            atmfAtmLayerEntry.6
            atmfAtmLayerEntry.7
            atmfAtmLayerEntry.8
            atmfAtmLayerEntry.9
            atmfAtmLayerEntry.10
            atmfAtmLayerEntry.11
            atmfAtmLayerEntry.12
            atmfAtmLayerEntry.13
            atmfAtmLayerEntry.14
            atmfAtmLayerEntry.15
            atmfAtmStatsEntry.1
            atmfAtmStatsEntry.2
            atmfAtmStatsEntry.3
            atmfAtmStatsEntry.4
            atmfVpcEntry.1
            atmfVpcEntry.2
            atmfVpcEntry.3
            atmfVpcEntry.4
            atmfVpcEntry.5
            atmfVpcEntry.6
            atmfVpcEntry.7
            atmfVpcEntry.8
            atmfVpcEntry.9
            atmfVpcEntry.10
            atmfVpcEntry.11
            atmfVpcEntry.12
            atmfVpcEntry.13
            atmfVpcEntry.14
            atmfVpcEntry.15
            atmfVpcEntry.17
            atmfVpcEntry.18
            atmfVpcEntry.19
            atmfVpcEntry.20
            atmfVccEntry.1
            atmfVccEntry.2
            atmfVccEntry.3
            atmfVccEntry.4
            atmfVccEntry.5
            atmfVccEntry.6
            atmfVccEntry.7
            atmfVccEntry.8
            atmfVccEntry.9
            atmfVccEntry.10
            atmfVccEntry.11
            atmfVccEntry.12
            atmfVccEntry.13
            atmfVccEntry.14
            atmfVccEntry.15
            atmfVccEntry.16
            atmfVccEntry.18
            atmfVccEntry.19
            atmfVccEntry.20
            atmfVccEntry.21
            atmfVccEntry.22
            atmfVccEntry.23
            atmfAddressEntry.3
            atmfAddressEntry.4
            atmfNetPrefixEntry.3
            atmForumUni.10.100.1.1
            atmForumUni.10.100.1.2
            atmForumUni.10.100.1.3
            atmForumUni.10.100.1.4
            atmForumUni.10.100.1.5
            atmForumUni.10.100.1.6
            atmForumUni.10.100.1.7
            atmForumUni.10.100.1.8
            atmForumUni.10.100.1.9
            atmForumUni.10.100.1.10
            atmForumUni.10.1.1.1
            atmForumUni.10.1.1.2
            atmForumUni.10.1.1.3
            atmForumUni.10.1.1.4
            atmForumUni.10.1.1.5
            atmForumUni.10.1.1.6
            atmForumUni.10.1.1.7
            atmForumUni.10.1.1.8
            atmForumUni.10.1.1.9
            atmForumUni.10.1.1.10
            atmForumUni.10.1.1.11
            atmForumUni.10.144.1.1
            atmForumUni.10.144.1.2
            enterprises.310.49.6.10.10.25.1.1
            enterprises.310.49.6.1.10.4.1.2
            enterprises.310.49.6.1.10.4.1.3
            enterprises.310.49.6.1.10.4.1.4
            enterprises.310.49.6.1.10.4.1.5
            enterprises.310.49.6.1.10.4.1.6
            enterprises.310.49.6.1.10.4.1.7
            enterprises.310.49.6.1.10.4.1.8
            enterprises.310.49.6.1.10.4.1.9
            enterprises.310.49.6.1.10.9.1.1
            enterprises.310.49.6.1.10.9.1.2
            enterprises.310.49.6.1.10.9.1.3
            enterprises.310.49.6.1.10.9.1.4
            enterprises.310.49.6.1.10.9.1.5
            enterprises.310.49.6.1.10.9.1.6
            enterprises.310.49.6.1.10.9.1.7
            enterprises.310.49.6.1.10.9.1.8
            enterprises.310.49.6.1.10.9.1.9
            enterprises.310.49.6.1.10.9.1.10
            enterprises.310.49.6.1.10.9.1.11
            enterprises.310.49.6.1.10.9.1.12
            enterprises.310.49.6.1.10.9.1.13
            enterprises.310.49.6.1.10.9.1.14
            enterprises.310.49.6.1.10.16.1.3
            enterprises.310.49.6.1.10.16.1.4
            enterprises.310.49.6.1.10.16.1.5
            enterprises.310.49.6.1.10.16.1.6
            enterprises.310.49.6.1.10.16.1.7
            enterprises.310.49.6.1.10.16.1.8
            enterprises.310.49.6.1.10.16.1.9
            enterprises.310.49.6.1.10.16.1.10
            enterprises.310.49.6.1.10.16.1.11
            enterprises.310.49.6.1.10.16.1.12
            enterprises.310.49.6.1.10.16.1.13
            enterprises.310.49.6.1.10.16.1.14
            snmpMIB.1.6.1
            snmpFrameworkMIB.2.1.1
            snmpFrameworkMIB.2.1.2
            snmpFrameworkMIB.2.1.3
            snmpFrameworkMIB.2.1.4
            snmpMPDMIB.2.1.1
            snmpMPDMIB.2.1.2
            snmpMPDMIB.2.1.3
            snmpTargetMIB.1.1
            snmpTargetMIB.10.9.1.2
            snmpTargetMIB.10.9.1.3
            snmpTargetMIB.10.9.1.4
            snmpTargetMIB.10.9.1.5
            snmpTargetMIB.10.9.1.6
            snmpTargetMIB.10.9.1.7
            snmpTargetMIB.10.9.1.8
            snmpTargetMIB.10.9.1.9
            snmpTargetMIB.10.16.1.2
            snmpTargetMIB.10.16.1.3
            snmpTargetMIB.10.16.1.4
            snmpTargetMIB.10.16.1.5
            snmpTargetMIB.10.16.1.6
            snmpTargetMIB.10.16.1.7
            snmpTargetMIB.1.4
            snmpTargetMIB.1.5
            snmpNotificationMIB.10.4.1.2
            snmpNotificationMIB.10.4.1.3
            snmpNotificationMIB.10.4.1.4
            snmpNotificationMIB.10.4.1.5
            snmpNotificationMIB.10.9.1.1
            snmpNotificationMIB.10.9.1.2
            snmpNotificationMIB.10.9.1.3
            snmpNotificationMIB.10.16.1.2
            snmpNotificationMIB.10.16.1.3
            snmpNotificationMIB.10.16.1.4
            snmpNotificationMIB.10.16.1.5
            snmpProxyMIB.10.9.1.2
            snmpProxyMIB.10.9.1.3
            snmpProxyMIB.10.9.1.4
            snmpProxyMIB.10.9.1.5
            snmpProxyMIB.10.9.1.6
            snmpProxyMIB.10.9.1.7
            snmpProxyMIB.10.9.1.8
            snmpProxyMIB.10.9.1.9
            snmpUsmMIB.1.1.1
            snmpUsmMIB.1.1.2
            snmpUsmMIB.1.1.3
            snmpUsmMIB.1.1.4
            snmpUsmMIB.1.1.5
            snmpUsmMIB.1.1.6
            snmpUsmMIB.1.2.1
            snmpUsmMIB.10.9.2.1.3
            snmpUsmMIB.10.9.2.1.4
            snmpUsmMIB.10.9.2.1.5
            snmpUsmMIB.10.9.2.1.6
            snmpUsmMIB.10.9.2.1.7
            snmpUsmMIB.10.9.2.1.8
            snmpUsmMIB.10.9.2.1.9
            snmpUsmMIB.10.9.2.1.10
            snmpUsmMIB.10.9.2.1.11
            snmpUsmMIB.10.9.2.1.12
            snmpUsmMIB.10.9.2.1.13
            snmpVacmMIB.10.4.1.1
            snmpVacmMIB.10.9.1.3
            snmpVacmMIB.10.9.1.4
            snmpVacmMIB.10.9.1.5
            snmpVacmMIB.10.25.1.4
            snmpVacmMIB.10.25.1.5
            snmpVacmMIB.10.25.1.6
            snmpVacmMIB.10.25.1.7
            snmpVacmMIB.10.25.1.8
            snmpVacmMIB.10.25.1.9
            snmpVacmMIB.1.5.1
            snmpVacmMIB.10.36.2.1.3
            snmpVacmMIB.10.36.2.1.4
            snmpVacmMIB.10.36.2.1.5
            snmpVacmMIB.10.36.2.1.6
            snmpCommunityMIB.10.4.1.2
            snmpCommunityMIB.10.4.1.3
            snmpCommunityMIB.10.4.1.4
            snmpCommunityMIB.10.4.1.5
            snmpCommunityMIB.10.4.1.6
            snmpCommunityMIB.10.4.1.7
            snmpCommunityMIB.10.4.1.8
            snmpCommunityMIB.10.9.1.1
            snmpCommunityMIB.10.9.1.2
            dot1agCfmStackMdIndex
            dot1agCfmStackMaIndex
            dot1agCfmStackMepId
            dot1agCfmStackMacAddress
            ieee8021CfmStackMdIndex
            ieee8021CfmStackMaIndex
            ieee8021CfmStackMepId
            ieee8021CfmStackMacAddress
            dot1agCfmDefaultMdDefLevel
            dot1agCfmDefaultMdDefMhfCreation
            dot1agCfmDefaultMdDefIdPermission
            dot1agCfmDefaultMdStatus
            dot1agCfmDefaultMdLevel
            dot1agCfmDefaultMdMhfCreation
            dot1agCfmDefaultMdIdPermission
            ieee8021CfmDefaultMdStatus
            ieee8021CfmDefaultMdLevel
            ieee8021CfmDefaultMdMhfCreation
            ieee8021CfmDefaultMdIdPermission
            dot1agCfmVlanPrimaryVid
            dot1agCfmVlanRowStatus
            ieee8021CfmVlanPrimarySelector
            ieee8021CfmVlanRowStatus
            dot1agCfmConfigErrorListErrorType
            ieee8021CfmConfigErrorListErrorType
            dot1agCfmMdTableNextIndex
            dot1agCfmMdFormat
            dot1agCfmMdName
            dot1agCfmMdMdLevel
            dot1agCfmMdMhfCreation
            dot1agCfmMdMhfIdPermission
            dot1agCfmMdMaNextIndex
            dot1agCfmMdRowStatus
            dot1agCfmMaNetFormat
            dot1agCfmMaNetName
            dot1agCfmMaNetCcmInterval
            dot1agCfmMaNetRowStatus
            dot1agCfmMaCompPrimaryVlanId
            dot1agCfmMaCompMhfCreation
            dot1agCfmMaCompIdPermission
            dot1agCfmMaCompNumberOfVids
            dot1agCfmMaCompRowStatus
            dot1agCfmMaMepListRowStatus
            ieee8021CfmMaCompPrimarySelectorType
            ieee8021CfmMaCompPrimarySelectorOrNone
            ieee8021CfmMaCompMhfCreation
            ieee8021CfmMaCompIdPermission
            ieee8021CfmMaCompNumberOfVids
            ieee8021CfmMaCompRowStatus
            dot1agCfmMepIfIndex
            dot1agCfmMepDirection
            dot1agCfmMepPrimaryVid
            dot1agCfmMepActive
            dot1agCfmMepFngState
            dot1agCfmMepCciEnabled
            dot1agCfmMepCcmLtmPriority
            dot1agCfmMepMacAddress
            dot1agCfmMepLowPrDef
            dot1agCfmMepFngAlarmTime
            dot1agCfmMepFngResetTime
            dot1agCfmMepHighestPrDefect
            dot1agCfmMepDefects
            dot1agCfmMepErrorCcmLastFailure
            dot1agCfmMepXconCcmLastFailure
            dot1agCfmMepCcmSequenceErrors
            dot1agCfmMepCciSentCcms
            dot1agCfmMepNextLbmTransId
            dot1agCfmMepLbrIn
            dot1agCfmMepLbrInOutOfOrder
            dot1agCfmMepLbrBadMsdu
            dot1agCfmMepLtmNextSeqNumber
            dot1agCfmMepUnexpLtrIn
            dot1agCfmMepLbrOut
            dot1agCfmMepTransmitLbmStatus
            dot1agCfmMepTransmitLbmDestMacAddress
            dot1agCfmMepTransmitLbmDestMepId
            dot1agCfmMepTransmitLbmDestIsMepId
            dot1agCfmMepTransmitLbmMessages
            dot1agCfmMepTransmitLbmDataTlv
            dot1agCfmMepTransmitLbmVlanPriority
            dot1agCfmMepTransmitLbmVlanDropEnable
            dot1agCfmMepTransmitLbmResultOK
            dot1agCfmMepTransmitLbmSeqNumber
            dot1agCfmMepTransmitLtmStatus
            dot1agCfmMepTransmitLtmFlags
            dot1agCfmMepTransmitLtmTargetMacAddress
            dot1agCfmMepTransmitLtmTargetMepId
            dot1agCfmMepTransmitLtmTargetIsMepId
            dot1agCfmMepTransmitLtmTtl
            dot1agCfmMepTransmitLtmResult
            dot1agCfmMepTransmitLtmSeqNumber
            dot1agCfmMepTransmitLtmEgressIdentifier
            dot1agCfmMepRowStatus
            dot1agCfmLtrTtl
            dot1agCfmLtrForwarded
            dot1agCfmLtrTerminalMep
            dot1agCfmLtrLastEgressIdentifier
            dot1agCfmLtrNextEgressIdentifier
            dot1agCfmLtrRelay
            dot1agCfmLtrChassisIdSubtype
            dot1agCfmLtrChassisId
            dot1agCfmLtrManAddressDomain
            dot1agCfmLtrManAddress
            dot1agCfmLtrIngress
            dot1agCfmLtrIngressMac
            dot1agCfmLtrIngressPortIdSubtype
            dot1agCfmLtrIngressPortId
            dot1agCfmLtrEgress
            dot1agCfmLtrEgressMac
            dot1agCfmLtrEgressPortIdSubtype
            dot1agCfmLtrEgressPortId
            dot1agCfmLtrOrganizationSpecificTlv
            dot1agCfmMepDbRMepState
            dot1agCfmMepDbRMepFailedOkTime
            dot1agCfmMepDbMacAddress
            dot1agCfmMepDbRdi
            dot1agCfmMepDbPortStatusTlv
            dot1agCfmMepDbInterfaceStatusTlv
            dot1agCfmMepDbChassisIdSubtype
            dot1agCfmMepDbChassisId
            dot1agCfmMepDbManAddressDomain
            dot1agCfmMepDbManAddress
            Router#
            '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSnmpMib(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowSnmpMib(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()

