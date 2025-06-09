# Copyright (c) 2024 by Cisco Systems, Inc.
# All rights reserved.
'''  show_esmc.py

IOSXE parsers for the following show commands:
    * 'show esmc detail'
    * 'show esmc'
    * 'show esmc interface {interface} detail'
    * 'show esmc interface {interface}'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Any


class ShowESMCDetailSchema(MetaParser):
    ''' Schema for:
        * 'show esmc detail'
    '''
    schema = {
        'interfaces': {
            Any(): {
                'admin_configs': {
                    'mode': str,
                    'esmc_tx': str,
                    'esmc_rx': str,
                    'ql_tx': str,
                    'ql_rx': str,
                },
                'operational_status': {
                    'port_status': str,
                    'ql_receive': str,
                    'ql_transmit': str,
                    'ql_rx_overrided': str,
                    'esmc_info_rate': int,
                    'esmc_expiry': int,
                    'esmc_tx_timer': str,
                    'esmc_rx_timer': str,
                    'esmc_tx_interval_count': int,
                    'esmc_info_pkts_in': int,
                    'esmc_info_pkts_out': int,
                    'esmc_event_pkts_in': int,
                    'esmc_event_pkts_out': int,
                }
            },
        },
    }


# =============================
# Parser for 'show esmc detail'
# =============================
class ShowESMCDetail(ShowESMCDetailSchema):
    ''' Parser for:
        * 'show esmc detail'
    '''
    cli_command = 'show esmc detail'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Interface: GigabitEthernet0/0/2
        p0 = re.compile(r'^Interface\s*:\s*'
                        r'(?P<interface>.+)$')

        # Mode: Synchronous
        p1 = re.compile(r'Mode\s*:\s*'
                        r'(?P<mode>.+)$')

        # ESMC TX: Enable
        p2 = re.compile(r'ESMC\s+TX\s*:\s*'
                        r'(?P<esmc_tx>.+)$')

        # ESMC RX: Enable
        p3 = re.compile(r'ESMC\s+RX\s*:\s*'
                        r'(?P<esmc_rx>.+)$')

        # QL TX: -
        p4 = re.compile(r'QL\s+TX\s*:\s*'
                        r'(?P<ql_tx>.+)$')

        # QL RX: -
        p5 = re.compile(r'QL\s+RX\s*:\s*'
                        r'(?P<ql_rx>.+)$')

        # Port status: UP
        p6 = re.compile(r'Port\s+status\s*:\s*'
                        r'(?P<port_status>.+)$')

        # QL Receive: QL-SEC
        p7 = re.compile(r'QL\s+Receive\s*:\s*'
                        r'(?P<ql_receive>.+)$')

        # QL Transmit: QL-DNU
        p8 = re.compile(r'QL\s+Transmit\s*:\s*'
                        r'(?P<ql_transmit>.+)$')

        # QL rx overrided: -
        p9 = re.compile(r'QL\s+rx\s+overrided\s*:\s*'
                        r'(?P<ql_rx_overrided>.+)$')

        # ESMC Information rate: 1 packet/second
        p10 = re.compile(r'ESMC\s+Information\s+rate\s*:\s*'
                         r'(?P<esmc_info_rate>\d+)\s*packet/second$')

        # ESMC Expiry: 5 second
        p11 = re.compile(r'ESMC\s+Expiry\s*:\s*'
                         r'(?P<esmc_expiry>\d+)\s*second$')

        # ESMC Tx Timer: Running
        p12 = re.compile(r'ESMC\s+Tx\s+Timer\s*:\s*'
                         r'(?P<esmc_tx_timer>.+)$')

        # ESMC Rx Timer: Running
        p13 = re.compile(r'ESMC\s+Rx\s+Timer\s*:\s*'
                         r'(?P<esmc_rx_timer>.+)$')

        # ESMC Tx interval count: 1
        p14 = re.compile(r'ESMC\s+Tx\s+interval\s+count\s*:\s*'
                         r'(?P<esmc_tx_interval_count>\d+)$')

        # ESMC INFO pkts in: 579392
        p15 = re.compile(r'ESMC\s+INFO\s+pkts\s+in\s*:\s*'
                         r'(?P<esmc_info_pkts_in>\d+)$')

        # ESMC INFO pkts out: 579545
        p16 = re.compile(r'ESMC\s+INFO\s+pkts\s+out\s*:\s*'
                         r'(?P<esmc_info_pkts_out>\d+)$')

        # ESMC EVENT pkts in: 0
        p17 = re.compile(r'ESMC\s+EVENT\s+pkts\s+in\s*:\s*'
                         r'(?P<esmc_event_pkts_in>\d+)$')

        # ESMC EVENT pkts out: 14
        p18 = re.compile(r'ESMC\s+EVENT\s+pkts\s+out\s*:\s*'
                         r'(?P<esmc_event_pkts_out>\d+)$')

        # Init vars
        parsed_dict = {}
        admin_configs_dict = {}
        operational_status_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface: GigabitEthernet0/0/2
            m = p0.match(line)
            if m:
                interface = m.groupdict()['interface']
                # convert interface name to long name
                interface = \
                    Common.convert_intf_name(interface)
                admin_configs_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface, {}). \
                    setdefault('admin_configs', {})
                operational_status_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface, {}). \
                    setdefault('operational_status', {})
                continue

            # Mode: Synchronous
            m = p1.match(line)
            if m:
                admin_configs_dict['mode'] = m.groupdict()['mode']
                continue

            # ESMC TX: Enable
            m = p2.match(line)
            if m:
                admin_configs_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC RX: Enable
            m = p3.match(line)
            if m:
                admin_configs_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # QL TX: -
            m = p4.match(line)
            if m:
                admin_configs_dict['ql_tx'] = m.groupdict()['ql_tx']
                continue

            # QL RX: -
            m = p5.match(line)
            if m:
                admin_configs_dict['ql_rx'] = m.groupdict()['ql_rx']
                continue

            # Port status: UP
            m = p6.match(line)
            if m:
                operational_status_dict['port_status'] = \
                    m.groupdict()['port_status']
                continue

            # QL Receive: QL-SEC
            m = p7.match(line)
            if m:
                operational_status_dict['ql_receive'] = \
                    m.groupdict()['ql_receive']
                continue

            # QL Transmit: QL-DNU
            m = p8.match(line)
            if m:
                operational_status_dict['ql_transmit'] = \
                    m.groupdict()['ql_transmit']
                continue

            # QL rx overrided: -
            m = p9.match(line)
            if m:
                operational_status_dict['ql_rx_overrided'] = \
                    m.groupdict()['ql_rx_overrided']
                continue

            # ESMC Information rate: 1 packet/second
            m = p10.match(line)
            if m:
                operational_status_dict['esmc_info_rate'] = \
                    int(m.groupdict()['esmc_info_rate'])
                continue

            # ESMC Expiry: 5 second
            m = p11.match(line)
            if m:
                operational_status_dict['esmc_expiry'] = \
                    int(m.groupdict()['esmc_expiry'])
                continue

            # ESMC Tx Timer: Running
            m = p12.match(line)
            if m:
                operational_status_dict['esmc_tx_timer'] = \
                    m.groupdict()['esmc_tx_timer']
                continue

            # ESMC Rx Timer: Running
            m = p13.match(line)
            if m:
                operational_status_dict['esmc_rx_timer'] = \
                    m.groupdict()['esmc_rx_timer']
                continue

            # ESMC Tx interval count: 1
            m = p14.match(line)
            if m:
                operational_status_dict['esmc_tx_interval_count'] = \
                    int(m.groupdict()['esmc_tx_interval_count'])
                continue

            # ESMC INFO pkts in: 579392
            m = p15.match(line)
            if m:
                operational_status_dict['esmc_info_pkts_in'] = \
                    int(m.groupdict()['esmc_info_pkts_in'])
                continue

            # ESMC INFO pkts out: 579545
            m = p16.match(line)
            if m:
                operational_status_dict['esmc_info_pkts_out'] = \
                    int(m.groupdict()['esmc_info_pkts_out'])
                continue

            # ESMC EVENT pkts in: 0
            m = p17.match(line)
            if m:
                operational_status_dict['esmc_event_pkts_in'] = \
                    int(m.groupdict()['esmc_event_pkts_in'])
                continue

            # ESMC EVENT pkts out: 14
            m = p18.match(line)
            if m:
                operational_status_dict['esmc_event_pkts_out'] = \
                    int(m.groupdict()['esmc_event_pkts_out'])
                continue

        return parsed_dict


class ShowESMCSchema(MetaParser):
    ''' Schema for:
        * 'show esmc'
    '''
    schema = {
        'interfaces': {
            Any(): {
                'admin_configs': {
                    'mode': str,
                    'esmc_tx': str,
                    'esmc_rx': str,
                    'ql_tx': str,
                    'ql_rx': str,
                },
                'operational_status': {
                    'port_status': str,
                    'ql_receive': str,
                    'ql_transmit': str,
                    'ql_rx_overrided': str,
                    'esmc_info_rate': int,
                    'esmc_expiry': int,
                }
            },
        },
    }


# ======================
# Parser for 'show esmc'
# ======================
class ShowESMC(ShowESMCSchema):
    ''' Parser for:
        * 'show esmc'
    '''
    cli_command = 'show esmc'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Interface: GigabitEthernet0/0/2
        p0 = re.compile(r'^Interface\s*:\s*'
                        r'(?P<interface>.+)$')

        # Mode: Synchronous
        p1 = re.compile(r'Mode\s*:\s*'
                        r'(?P<mode>.+)$')

        # ESMC TX: Enable
        p2 = re.compile(r'ESMC\s+TX\s*:\s*'
                        r'(?P<esmc_tx>.+)$')

        # ESMC RX: Enable
        p3 = re.compile(r'ESMC\s+RX\s*:\s*'
                        r'(?P<esmc_rx>.+)$')

        # QL TX: -
        p4 = re.compile(r'QL\s+TX\s*:\s*'
                        r'(?P<ql_tx>.+)$')

        # QL RX: -
        p5 = re.compile(r'QL\s+RX\s*:\s*'
                        r'(?P<ql_rx>.+)$')

        # Port status: UP
        p6 = re.compile(r'Port\s+status\s*:\s*'
                        r'(?P<port_status>.+)$')

        # QL Receive: QL-SEC
        p7 = re.compile(r'QL\s+Receive\s*:\s*'
                        r'(?P<ql_receive>.+)$')

        # QL Transmit: QL-DNU
        p8 = re.compile(r'QL\s+Transmit\s*:\s*'
                        r'(?P<ql_transmit>.+)$')

        # QL rx overrided: -
        p9 = re.compile(r'QL\s+rx\s+overrided\s*:\s*'
                        r'(?P<ql_rx_overrided>.+)$')

        # ESMC Information rate: 1 packet/second
        p10 = re.compile(r'ESMC\s+Information\s+rate\s*:\s*'
                         r'(?P<esmc_info_rate>\d+)\s*packet/second$')

        # ESMC Expiry: 5 second
        p11 = re.compile(r'ESMC\s+Expiry\s*:\s*'
                         r'(?P<esmc_expiry>\d+)\s*second$')

        # Init vars
        parsed_dict = {}
        admin_configs_dict = {}
        operational_status_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface: GigabitEthernet0/0/2
            m = p0.match(line)
            if m:
                interface = m.groupdict()['interface']
                # convert interface name to long name
                interface = \
                    Common.convert_intf_name(interface)
                admin_configs_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface, {}). \
                    setdefault('admin_configs', {})
                operational_status_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface, {}). \
                    setdefault('operational_status', {})
                continue

            # Mode: Synchronous
            m = p1.match(line)
            if m:
                admin_configs_dict['mode'] = m.groupdict()['mode']
                continue

            # ESMC TX: Enable
            m = p2.match(line)
            if m:
                admin_configs_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC RX: Enable
            m = p3.match(line)
            if m:
                admin_configs_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # QL TX: -
            m = p4.match(line)
            if m:
                admin_configs_dict['ql_tx'] = m.groupdict()['ql_tx']
                continue

            # QL RX: -
            m = p5.match(line)
            if m:
                admin_configs_dict['ql_rx'] = m.groupdict()['ql_rx']
                continue

            # Port status: UP
            m = p6.match(line)
            if m:
                operational_status_dict['port_status'] = \
                    m.groupdict()['port_status']
                continue

            # QL Receive: QL-SEC
            m = p7.match(line)
            if m:
                operational_status_dict['ql_receive'] = \
                    m.groupdict()['ql_receive']
                continue

            # QL Transmit: QL-DNU
            m = p8.match(line)
            if m:
                operational_status_dict['ql_transmit'] = \
                    m.groupdict()['ql_transmit']
                continue

            # QL rx overrided: -
            m = p9.match(line)
            if m:
                operational_status_dict['ql_rx_overrided'] = \
                    m.groupdict()['ql_rx_overrided']
                continue

            # ESMC Information rate: 1 packet/second
            m = p10.match(line)
            if m:
                operational_status_dict['esmc_info_rate'] = \
                    int(m.groupdict()['esmc_info_rate'])
                continue

            # ESMC Expiry: 5 second
            m = p11.match(line)
            if m:
                operational_status_dict['esmc_expiry'] = \
                    int(m.groupdict()['esmc_expiry'])
                continue

        return parsed_dict


class ShowESMCInterfaceDetailSchema(MetaParser):
    ''' Schema for:
        * 'show esmc interface {interface} detail'
    '''
    schema = {
        Any(): {
            'admin_configs': {
                'mode': str,
                'esmc_tx': str,
                'esmc_rx': str,
                'ql_tx': str,
                'ql_rx': str,
            },
            'operational_status': {
                'port_status': str,
                'ql_receive': str,
                'ql_transmit': str,
                'ql_rx_overrided': str,
                'esmc_info_rate': int,
                'esmc_expiry': int,
                'esmc_tx_timer': str,
                'esmc_rx_timer': str,
                'esmc_tx_interval_count': int,
                'esmc_info_pkts_in': int,
                'esmc_info_pkts_out': int,
                'esmc_event_pkts_in': int,
                'esmc_event_pkts_out': int,
            }
        },
    }


# ===================================================
# Parser for 'show esmc interface {interface} detail'
# ===================================================
class ShowESMCInterfaceDetail(ShowESMCInterfaceDetailSchema):
    ''' Parser for:
        * 'show esmc interface {interface} detail'
    '''
    cli_command = 'show esmc interface {interface} detail'

    def cli(self, interface, output=None):

        if output is None:
            output = self.device. \
                execute(self.cli_command.format(interface=interface))

        # Interface: GigabitEthernet0/0/2
        p0 = re.compile(r'^Interface\s*:\s*'
                        r'(?P<intf>.+)$')

        # Mode: Synchronous
        p1 = re.compile(r'Mode\s*:\s*'
                        r'(?P<mode>.+)$')

        # ESMC TX: Enable
        p2 = re.compile(r'ESMC\s+TX\s*:\s*'
                        r'(?P<esmc_tx>.+)$')

        # ESMC RX: Enable
        p3 = re.compile(r'ESMC\s+RX\s*:\s*'
                        r'(?P<esmc_rx>.+)$')

        # QL TX: -
        p4 = re.compile(r'QL\s+TX\s*:\s*'
                        r'(?P<ql_tx>.+)$')

        # QL RX: -
        p5 = re.compile(r'QL\s+RX\s*:\s*'
                        r'(?P<ql_rx>.+)$')

        # Port status: UP
        p6 = re.compile(r'Port\s+status\s*:\s*'
                        r'(?P<port_status>.+)$')

        # QL Receive: QL-SEC
        p7 = re.compile(r'QL\s+Receive\s*:\s*'
                        r'(?P<ql_receive>.+)$')

        # QL Transmit: QL-DNU
        p8 = re.compile(r'QL\s+Transmit\s*:\s*'
                        r'(?P<ql_transmit>.+)$')

        # QL rx overrided: -
        p9 = re.compile(r'QL\s+rx\s+overrided\s*:\s*'
                        r'(?P<ql_rx_overrided>.+)$')

        # ESMC Information rate: 1 packet/second
        p10 = re.compile(r'ESMC\s+Information\s+rate\s*:\s*'
                         r'(?P<esmc_info_rate>\d+)\s*packet/second$')

        # ESMC Expiry: 5 second
        p11 = re.compile(r'ESMC\s+Expiry\s*:\s*'
                         r'(?P<esmc_expiry>\d+)\s*second$')

        # ESMC Tx Timer: Running
        p12 = re.compile(r'ESMC\s+Tx\s+Timer\s*:\s*'
                         r'(?P<esmc_tx_timer>.+)$')

        # ESMC Rx Timer: Running
        p13 = re.compile(r'ESMC\s+Rx\s+Timer\s*:\s*'
                         r'(?P<esmc_rx_timer>.+)$')

        # ESMC Tx interval count: 1
        p14 = re.compile(r'ESMC\s+Tx\s+interval\s+count\s*:\s*'
                         r'(?P<esmc_tx_interval_count>\d+)$')

        # ESMC INFO pkts in: 579392
        p15 = re.compile(r'ESMC\s+INFO\s+pkts\s+in\s*:\s*'
                         r'(?P<esmc_info_pkts_in>\d+)$')

        # ESMC INFO pkts out: 579545
        p16 = re.compile(r'ESMC\s+INFO\s+pkts\s+out\s*:\s*'
                         r'(?P<esmc_info_pkts_out>\d+)$')

        # ESMC EVENT pkts in: 0
        p17 = re.compile(r'ESMC\s+EVENT\s+pkts\s+in\s*:\s*'
                         r'(?P<esmc_event_pkts_in>\d+)$')

        # ESMC EVENT pkts out: 14
        p18 = re.compile(r'ESMC\s+EVENT\s+pkts\s+out\s*:\s*'
                         r'(?P<esmc_event_pkts_out>\d+)$')

        # Init vars
        parsed_dict = {}
        admin_configs_dict = {}
        operational_status_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface: GigabitEthernet0/0/2
            m = p0.match(line)
            if m:
                intf = m.groupdict()['intf']
                # convert interface name to long name
                intf = Common.convert_intf_name(intf)
                admin_configs_dict = parsed_dict.setdefault(intf, {}).setdefault('admin_configs', {})
                operational_status_dict = parsed_dict.setdefault(intf, {}).setdefault('operational_status', {})
                continue

            # Mode: Synchronous
            m = p1.match(line)
            if m:
                admin_configs_dict['mode'] = m.groupdict()['mode']
                continue

            # ESMC TX: Enable
            m = p2.match(line)
            if m:
                admin_configs_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC RX: Enable
            m = p3.match(line)
            if m:
                admin_configs_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # QL TX: -
            m = p4.match(line)
            if m:
                admin_configs_dict['ql_tx'] = m.groupdict()['ql_tx']
                continue

            # QL RX: -
            m = p5.match(line)
            if m:
                admin_configs_dict['ql_rx'] = m.groupdict()['ql_rx']
                continue

            # Port status: UP
            m = p6.match(line)
            if m:
                operational_status_dict['port_status'] = m.groupdict()['port_status']
                continue

            # QL Receive: QL-SEC
            m = p7.match(line)
            if m:
                operational_status_dict['ql_receive'] = m.groupdict()['ql_receive']
                continue

            # QL Transmit: QL-DNU
            m = p8.match(line)
            if m:
                operational_status_dict['ql_transmit'] = m.groupdict()['ql_transmit']
                continue

            # QL rx overrided: -
            m = p9.match(line)
            if m:
                operational_status_dict['ql_rx_overrided'] = m.groupdict()['ql_rx_overrided']
                continue

            # ESMC Information rate: 1 packet/second
            m = p10.match(line)
            if m:
                operational_status_dict['esmc_info_rate'] = int(m.groupdict()['esmc_info_rate'])
                continue

            # ESMC Expiry: 5 second
            m = p11.match(line)
            if m:
                operational_status_dict['esmc_expiry'] = \
                    int(m.groupdict()['esmc_expiry'])
                continue

            # ESMC Tx Timer: Running
            m = p12.match(line)
            if m:
                operational_status_dict['esmc_tx_timer'] = \
                    m.groupdict()['esmc_tx_timer']
                continue

            # ESMC Rx Timer: Running
            m = p13.match(line)
            if m:
                operational_status_dict['esmc_rx_timer'] = \
                    m.groupdict()['esmc_rx_timer']
                continue

            # ESMC Tx interval count: 1
            m = p14.match(line)
            if m:
                operational_status_dict['esmc_tx_interval_count'] = \
                    int(m.groupdict()['esmc_tx_interval_count'])
                continue

            # ESMC INFO pkts in: 579392
            m = p15.match(line)
            if m:
                operational_status_dict['esmc_info_pkts_in'] = \
                    int(m.groupdict()['esmc_info_pkts_in'])
                continue

            # ESMC INFO pkts out: 579545
            m = p16.match(line)
            if m:
                operational_status_dict['esmc_info_pkts_out'] = \
                    int(m.groupdict()['esmc_info_pkts_out'])
                continue

            # ESMC EVENT pkts in: 0
            m = p17.match(line)
            if m:
                operational_status_dict['esmc_event_pkts_in'] = \
                    int(m.groupdict()['esmc_event_pkts_in'])
                continue

            # ESMC EVENT pkts out: 14
            m = p18.match(line)
            if m:
                operational_status_dict['esmc_event_pkts_out'] = \
                    int(m.groupdict()['esmc_event_pkts_out'])
                continue

        return parsed_dict


class ShowESMCInterfaceSchema(MetaParser):
    ''' Schema for:
        * 'show esmc interface {interface}'
    '''
    schema = {
        Any(): {
            'admin_configs': {
                'mode': str,
                'esmc_tx': str,
                'esmc_rx': str,
                'ql_tx': str,
                'ql_rx': str,
            },
            'operational_status': {
                'port_status': str,
                'ql_receive': str,
                'ql_transmit': str,
                'ql_rx_overrided': str,
                'esmc_info_rate': int,
                'esmc_expiry': int
            }
        },
    }


# ============================================
# Parser for 'show esmc interface {interface}'
# ============================================
class ShowESMCInterface(ShowESMCInterfaceSchema):
    ''' Parser for:
        * 'show esmc interface {interface}'
    '''
    cli_command = 'show esmc interface {interface}'

    def cli(self, interface, output=None):

        if output is None:
            output = self.device. \
                execute(self.cli_command.format(interface=interface))

        # Interface: GigabitEthernet0/0/2
        p0 = re.compile(r'^Interface\s*:\s*'
                        r'(?P<intf>.+)$')

        # Mode: Synchronous
        p1 = re.compile(r'Mode\s*:\s*'
                        r'(?P<mode>.+)$')

        # ESMC TX: Enable
        p2 = re.compile(r'ESMC\s+TX\s*:\s*'
                        r'(?P<esmc_tx>.+)$')

        # ESMC RX: Enable
        p3 = re.compile(r'ESMC\s+RX\s*:\s*'
                        r'(?P<esmc_rx>.+)$')

        # QL TX: -
        p4 = re.compile(r'QL\s+TX\s*:\s*'
                        r'(?P<ql_tx>.+)$')

        # QL RX: -
        p5 = re.compile(r'QL\s+RX\s*:\s*'
                        r'(?P<ql_rx>.+)$')

        # Port status: UP
        p6 = re.compile(r'Port\s+status\s*:\s*'
                        r'(?P<port_status>.+)$')

        # QL Receive: QL-SEC
        p7 = re.compile(r'QL\s+Receive\s*:\s*'
                        r'(?P<ql_receive>.+)$')

        # QL Transmit: QL-DNU
        p8 = re.compile(r'QL\s+Transmit\s*:\s*'
                        r'(?P<ql_transmit>.+)$')

        # QL rx overrided: -
        p9 = re.compile(r'QL\s+rx\s+overrided\s*:\s*'
                        r'(?P<ql_rx_overrided>.+)$')

        # ESMC Information rate: 1 packet/second
        p10 = re.compile(r'ESMC\s+Information\s+rate\s*:\s*'
                         r'(?P<esmc_info_rate>\d+)\s*packet/second$')

        # ESMC Expiry: 5 second
        p11 = re.compile(r'ESMC\s+Expiry\s*:\s*'
                         r'(?P<esmc_expiry>\d+)\s*second$')

        # Init vars
        parsed_dict = {}
        admin_configs_dict = {}
        operational_status_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface: GigabitEthernet0/0/2
            m = p0.match(line)
            if m:
                intf = m.groupdict()['intf']
                # convert interface name to long name
                intf = Common.convert_intf_name(intf)
                admin_configs_dict = parsed_dict.setdefault(intf, {}).setdefault('admin_configs', {})
                operational_status_dict = parsed_dict.setdefault(intf, {}).setdefault('operational_status', {})
                continue

            # Mode: Synchronous
            m = p1.match(line)
            if m:
                admin_configs_dict['mode'] = m.groupdict()['mode']
                continue

            # ESMC TX: Enable
            m = p2.match(line)
            if m:
                admin_configs_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC RX: Enable
            m = p3.match(line)
            if m:
                admin_configs_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # QL TX: -
            m = p4.match(line)
            if m:
                admin_configs_dict['ql_tx'] = m.groupdict()['ql_tx']
                continue

            # QL RX: -
            m = p5.match(line)
            if m:
                admin_configs_dict['ql_rx'] = m.groupdict()['ql_rx']
                continue

            # Port status: UP
            m = p6.match(line)
            if m:
                operational_status_dict['port_status'] = m.groupdict()['port_status']
                continue

            # QL Receive: QL-SEC
            m = p7.match(line)
            if m:
                operational_status_dict['ql_receive'] = m.groupdict()['ql_receive']
                continue

            # QL Transmit: QL-DNU
            m = p8.match(line)
            if m:
                operational_status_dict['ql_transmit'] = m.groupdict()['ql_transmit']
                continue

            # QL rx overrided: -
            m = p9.match(line)
            if m:
                operational_status_dict['ql_rx_overrided'] = m.groupdict()['ql_rx_overrided']
                continue

            # ESMC Information rate: 1 packet/second
            m = p10.match(line)
            if m:
                operational_status_dict['esmc_info_rate'] = int(m.groupdict()['esmc_info_rate'])
                continue

            # ESMC Expiry: 5 second
            m = p11.match(line)
            if m:
                operational_status_dict['esmc_expiry'] = int(m.groupdict()['esmc_expiry'])
                continue

        return parsed_dict
