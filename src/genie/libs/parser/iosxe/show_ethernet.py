"""show_ethernet.py

IOSXE parsers for the following show commands:
    * show ethernet cfm maintenance-points remote detail
    * show ethernet cfm statistics
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


# =======================================================================
# Parser Schema for 'show ethernet cfm maintenance-points remote detail'
# =======================================================================


class ShowEthernetCfmMaintenancePointsRemoteDetailSchema(MetaParser):
    """Schema for "show ethernet cfm maintenance-points remote detail" """

    schema = {
                'version': str,
                'mac_address': str,
                'domain_name': str,
                'domain_id': str,
                'ma_name': str,
                'level': int,
                'evc': str,
                'bridge_domain': int,
                'mpid': int,
                'incoming_port': str,
                'cc_lifetime': str,
                'age_of_last_cc_message': int,
                'cc_packet_statistics': str,
                'mep_interface_status': str,
                'mep_port_status': str,
                'receive_rdi': str
            }


# ================================================================
# Parser for 'show ethernet cfm maintenance-points remote detail'
# ================================================================


class ShowEthernetCfmMaintenancePointsRemoteDetail(ShowEthernetCfmMaintenancePointsRemoteDetailSchema):
    """ parser for "show ethernet cfm maintenance-points remote detail" """

    cli_command = "show ethernet cfm maintenance-points remote detail"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Version: IEEE-CFM
        p1 = re.compile(r'^(Version:+\s+(?P<version>[A-Z-]+))$')

        # MAC Address: 7070.8bba.3801
        p2 = re.compile(r'^(MAC\sAddress:\s(?P<mac_address>([0-9a-fA-F].?){12})$)')

        # Domain Name: UNINET
        p3 = re.compile(r'^(Domain\sName:\s(?P<domain_name>\w+)$)')

        # Domain ID: UNINET
        p4 = re.compile(r'^(Domain\sID:\s(?P<domain_id>\w+)$)')

        # MA Name: UNINET_VERLEANDROVALLE-17_5005
        p5 = re.compile(r'^(MA\sName:\s(?P<ma_name>[A-Z0-9-_]+)$)')

        # Level: 7
        p6 = re.compile(r'^(Level:\s(?P<level>\d+$))')

        # EVC: UNINET_VERLEANDROVALLE-17_5005
        p7 = re.compile(r'^(EVC:\s(?P<evc>[A-Z0-9-_]+)$)')

        # Bridge Domain: 100
        p8 = re.compile(r'^(Bridge\sDomain:\s(?P<bridge_domain>\d+$)$)')

        # MPID: 1562
        p9 = re.compile(r'^(MPID:\s(?P<mpid>\d+$)$)')

        # Incoming Port(s): Gi2/0/4
        p10 = re.compile(r'^(Incoming\sPort\((s)\):\s(?P<incoming_port>[A-Za-z0-9/ -_]+)$)')

        # CC Lifetime(sec): 3.500
        p11 = re.compile(r'^(CC\sLifetime\((sec)\):\s(?P<cc_lifetime>(\d.+|\d+))$)')

        # Age of Last CC Message(sec): 0
        p12 = re.compile(r'^(Age\sof\sLast\sCC\sMessage\((sec)\):\s(?P<age_of_last_cc_message>(\d.+|\d+))$)')

        # CC Packet Statistics: 28091/0 (Received/Error)
        p13 = re.compile(r'^(CC\sPacket\sStatistics:\s(?P<cc_packet_statistics>[0-9/]+))')

        # MEP interface status: Up
        p14 = re.compile(r'^(MEP\sinterface\sstatus:\s(?P<mep_interface_status>\w+)$)')

        # MEP port status: Up
        p15 = re.compile(r'^(MEP\sport\sstatus:\s(?P<mep_port_status>\w+)$)')

        # Receive RDI: FALSE
        p16 = re.compile(r'^(Receive\sRDI:\s(?P<receive_rdi>\w+)$)')

        for line in output.splitlines():
            line = line.strip()

            # Version: IEEE-CFM
            m = p1.match(line)
            if m:
                group = m.groupdict()
                version = group['version']
                parsed_dict.update({'version': version})
                continue

            # MAC Address: 7070.8bba.3801
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_address = group['mac_address']
                parsed_dict.update({'mac_address': mac_address})
                continue

            # Domain Name: UNINET
            m = p3.match(line)
            if m:
                group = m.groupdict()
                domain_name = group['domain_name']
                parsed_dict.update({'domain_name': domain_name})
                continue

            # Domain ID: UNINET
            m = p4.match(line)
            if m:
                group = m.groupdict()
                domain_id = group['domain_id']
                parsed_dict.update({'domain_id': domain_id})
                continue

            # MA Name: UNINET_VERLEANDROVALLE-17_5005
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ma_name = group['ma_name']
                parsed_dict.update({'ma_name': ma_name})
                continue

            # Level: 7
            m = p6.match(line)
            if m:
                group = m.groupdict()
                level = int(group['level'])
                parsed_dict.update({'level': level})
                continue

            # EVC: UNINET_VERLEANDROVALLE-17_5005
            m = p7.match(line)
            if m:
                group = m.groupdict()
                evc = group['evc']
                parsed_dict.update({'evc': evc})
                continue

            # Bridge Domain: 100
            m = p8.match(line)
            if m:
                group = m.groupdict()
                bridge_domain = int(group['bridge_domain'])
                parsed_dict.update({'bridge_domain': bridge_domain})
                continue

            # MPID: 1562
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mpid = int(group['mpid'])
                parsed_dict.update({'mpid': mpid})
                continue

            # Incoming Port(s): Gi2/0/4
            m = p10.match(line)
            if m:
                group = m.groupdict()
                incoming_port = group['incoming_port']
                parsed_dict.update({'incoming_port': incoming_port})
                continue

            # CC Lifetime(sec): 3.500
            m = p11.match(line)
            if m:
                group = m.groupdict()
                cc_lifetime = group['cc_lifetime']
                parsed_dict.update({'cc_lifetime': cc_lifetime})
                continue

            # Age of Last CC Message(sec): 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                age_of_last_cc_message = int(group['age_of_last_cc_message'])
                parsed_dict.update({'age_of_last_cc_message': age_of_last_cc_message})
                continue

            # CC Packet Statistics: 28091/0 (Received/Error)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                cc_packet_statistics = group['cc_packet_statistics']
                parsed_dict.update({'cc_packet_statistics': cc_packet_statistics})
                continue

            # MEP interface status: Up
            m = p14.match(line)
            if m:
                group = m.groupdict()
                mep_interface_status = group['mep_interface_status']
                parsed_dict.update({'mep_interface_status': mep_interface_status})
                continue

            # MEP port status: Up
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mep_port_status = group['mep_port_status']
                parsed_dict.update({'mep_port_status': mep_port_status})
                continue

            # Receive RDI: FALSE
            m = p16.match(line)
            if m:
                group = m.groupdict()
                receive_rdi = group['receive_rdi']
                parsed_dict.update({'receive_rdi': receive_rdi})
                continue

        return parsed_dict


# ==================================================
# Parser Schema for 'show ethernet cfm statistics '
# ==================================================


class ShowEthernetCfmStatisticsSchema(MetaParser):
    """Schema for "show ethernet cfm statistics" """

    schema = {
        'brain_mac': str,
        'domain_name': str,
        'ma_name': str,
        'mpid': {
            Any(): {
                'counters_last_clearing': str,
                'ccms': {
                    'transmitted': int,
                    'rcvd_seq_errors': int
                },
                'ltrs': {
                    'unexpected_received': int,
                    'total_tx_ltr': int,
                    'total_rx_valid_ltr': int,
                    'total_rx_invalid_ltr': int,
                    'rx_invalid_relay_action': int
                },
                'ltms': {
                    'total_tx_ltm': int,
                    'total_rx_valid_ltm': int,
                    'total_rx_invalid_ltm': int
                },
                'lbrs': {
                    'transmitted': int,
                    'rcvd_seq_errors': int,
                    'rcvd_in_order': int,
                    'rcvd_bad_msdu': int,
                    'rx_invalid_lbr': int,
                },
                'lbms': {
                    'total_tx_lbm': int,
                    'total_rx_valid_lbm': int,
                    'total_rx_invalid_lbm': int
                }
            }
        }
    }


# ==========================================
# Parser for 'show ethernet cfm statistics'
# ==========================================

class ShowEthernetCfmStatistics(ShowEthernetCfmStatisticsSchema):
    """ parser for "show ethernet cfm statistics" """

    cli_command = "show ethernet cfm statistics"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # BRAIN MAC: 4c77.6dad.ea53
        p1 = re.compile(r'^(BRAIN\sMAC:+\s+(?P<brain_mac>([0-9a-fA-F].?){12}$))')

        # DomainName: UNINET
        p2 = re.compile(r'^(DomainName:\s(?P<domain_name>\w+)$)')

        # MA Name: UNINET_VERLEANDROVALLE-17_5005
        p3 = re.compile(r'^(MA\sName:\s(?P<ma_name>\w+[-_]+\w+)$)')

        # MPID: 1561
        p4 = re.compile(r'^(MPID:\s(?P<mpid>\d+$)$)')

        # Last clearing of counters: never
        p5 = re.compile(r'^(Last\sclearing\sof\scounters:\s(?P<counters_last_clearing>\w+)$)')

        # CCMs:
        p6 = re.compile(r'^(CCMs:)$')

        # Transmitted:              28029     Rcvd Seq Errors:        0
        p7 = re.compile(r'^(Transmitted:\s+(?P<transmitted>\d+)\s+(Rcvd\sSeq\sErrors:\s+(?P<rcvd_seq_errors>\d+))$)')

        # Unexpected Rcvd:              0
        p8 = re.compile(r'^(Unexpected\sRcvd:\s+(?P<unexpected_received>\d+)$)')

        # Total Tx LTR:                 0
        p9 = re.compile(r'^(Total\sTx\sLTR:\s+(?P<total_tx_ltr>\d+)$)')

        # Total Rx Valid LTR:           0
        p10 = re.compile(r'^(Total\sRx\sValid\sLTR:\s+(?P<total_rx_valid_ltr>\d+)$)')

        # Total Rx Invalid LTR:         0
        p11 = re.compile(r'^(Total\sRx\sInvalid\sLTR:\s+(?P<total_rx_invalid_ltr>\d+)$)')

        # Rx Invalid Relay Action:      0
        p12 = re.compile(r'^(Rx\sInvalid\sRelay\sAction:\s+(?P<rx_invalid_relay_action>\d+)$)')

        # Total Tx LTM:                 0
        p13 = re.compile(r'^(Total\sTx\sLTM:\s+(?P<total_tx_ltm>\d+)$)')

        # Total Rx Valid LTM:           0
        p14 = re.compile(r'^(Total\sRx\sValid\sLTM:\s+(?P<total_rx_valid_ltm>\d+)$)')

        # Total Rx Invalid LTM:         0
        p15 = re.compile(r'^(Total\sRx\sInvalid\sLTM:\s+(?P<total_rx_invalid_ltm>\d+)$)')

        # LBRs:
        p16 = re.compile(r'(^LBRs:)$')

        # Rcvd in order:                0   Rcvd Bad MSDU:          0
        p17 = re.compile(r'^(Rcvd\sin\sorder:\s+(?P<rcvd_in_order>\d+)\s+(Rcvd\sBad\sMSDU:\s+(?P<rcvd_bad_msdu>\d+))$)')

        # Rx Invalid LBR:               0
        p18 = re.compile(r'^(Rx\sInvalid\sLBR:\s+(?P<rx_invalid_lbr>\d+)$)')

        # Total Tx LBM:                 0
        p19 = re.compile(r'^(Total\sTx\sLBM:\s+(?P<total_tx_lbm>\d+)$)')

        # Total Rx Valid LBM:           0
        p20 = re.compile(r'^(Total\sRx\sValid\sLBM:\s+(?P<total_rx_valid_lbm>\d+)$)')

        # Total Rx Invalid LBM:         0
        p21 = re.compile(r'^(Total\sRx\sInvalid\sLBM:\s+(?P<total_rx_invalid_lbm>\d+)$)')

        for line in output.splitlines():
            line = line.strip()

            # BRAIN MAC: 4c77.6dad.ea53
            m = p1.match(line)
            if m:
                group = m.groupdict()
                brain_mac = group['brain_mac']
                parsed_dict.update({'brain_mac': brain_mac})
                continue

            # DomainName: UNINET
            m = p2.match(line)
            if m:
                group = m.groupdict()
                domain_name = group['domain_name']
                parsed_dict.update({'domain_name': domain_name})
                continue

            # MA Name: UNINET_VERLEANDROVALLE-17_5005
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ma_name = group['ma_name']
                parsed_dict.update({'ma_name': ma_name})
                continue

            # MPID: 1561
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mpid = group['mpid']
                mpid_dict = parsed_dict.setdefault('mpid', {}).setdefault(mpid, {})
                continue

            # Last clearing of counters: never
            m = p5.match(line)
            if m:
                group = m.groupdict()
                counters_last_clearing = group['counters_last_clearing']
                mpid_dict['counters_last_clearing'] = counters_last_clearing
                continue

            # CCMs
            if p6.match(line):
                checkline_flows = "CCMs"
                ccms_dict = mpid_dict.setdefault("ccms", {})
                continue

            # LBRs
            if p16.match(line):
                checkline_flows = "LBRs"
                lbrs_dict = mpid_dict.setdefault("lbrs", {})
                continue

            # Transmitted:              28029    Rcvd Seq Errors:        0
            if p7.match(line):
                m = p7.match(line)
                group = m.groupdict()
                transmitted = int(group["transmitted"])
                rcvd_seq_errors = int(group["rcvd_seq_errors"])
                if checkline_flows == "CCMs":
                    ccms_dict.update({"transmitted": transmitted})
                    ccms_dict["rcvd_seq_errors"] = rcvd_seq_errors
                if checkline_flows == "LBRs":
                    lbrs_dict.update({"transmitted": transmitted})
                    lbrs_dict["rcvd_seq_errors"] = rcvd_seq_errors
                continue

            # Unexpected Rcvd:              0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                unexpected_received = int(group['unexpected_received'])
                ltrs_dict = mpid_dict.setdefault('ltrs', {})
                ltrs_dict['unexpected_received'] = unexpected_received
                continue

            # Total Tx LTR:                 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                total_tx_ltr = int(group['total_tx_ltr'])
                ltrs_dict['total_tx_ltr'] = total_tx_ltr
                continue

            # Total Rx Valid LTR:           0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                total_rx_valid_ltr = int(group['total_rx_valid_ltr'])
                ltrs_dict['total_rx_valid_ltr'] = total_rx_valid_ltr
                continue

            # Total Rx Invalid LTR:         0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                total_rx_invalid_ltr = int(group['total_rx_invalid_ltr'])
                ltrs_dict['total_rx_invalid_ltr'] = total_rx_invalid_ltr
                continue

            # Rx Invalid Relay Action:      0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                rx_invalid_relay_action = int(group['rx_invalid_relay_action'])
                ltrs_dict['rx_invalid_relay_action'] = rx_invalid_relay_action
                continue

            # Total Tx LTM:                 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                total_tx_ltm = int(group['total_tx_ltm'])
                ltms_dict = mpid_dict.setdefault('ltms', {})
                ltms_dict['total_tx_ltm'] = total_tx_ltm
                continue

            # Total Rx Valid LTM:           0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                total_rx_valid_ltm = int(group['total_rx_valid_ltm'])
                ltms_dict['total_rx_valid_ltm'] = total_rx_valid_ltm
                continue

            # Total Rx Invalid LTM:         0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                total_rx_invalid_ltm = int(group['total_rx_invalid_ltm'])
                ltms_dict['total_rx_invalid_ltm'] = total_rx_invalid_ltm
                continue

            # Rcvd in order:                0   Rcvd Bad MSDU:          0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                rcvd_in_order = int(group['rcvd_in_order'])
                rcvd_bad_msdu = int(group['rcvd_bad_msdu'])
                lbrs_dict['rcvd_in_order'] = rcvd_in_order
                lbrs_dict['rcvd_bad_msdu'] = rcvd_bad_msdu
                continue

            # Rx Invalid LBR:               0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                rx_invalid_lbr = int(group['rx_invalid_lbr'])
                lbrs_dict['rx_invalid_lbr'] = rx_invalid_lbr
                continue

            # Total Tx LBM:                 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                total_tx_lbm = int(group['total_tx_lbm'])
                lbms_dict = mpid_dict.setdefault('lbms', {})
                lbms_dict['total_tx_lbm'] = total_tx_lbm
                continue

            # Total Rx Valid LBM:           0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                total_rx_valid_lbm = int(group['total_rx_valid_lbm'])
                lbms_dict['total_rx_valid_lbm'] = total_rx_valid_lbm
                continue

            # Total Rx Invalid LBM:         0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                total_rx_invalid_lbm = int(group['total_rx_invalid_lbm'])
                lbms_dict['total_rx_invalid_lbm'] = total_rx_invalid_lbm
                continue

        return parsed_dict
