"""
CHEETAH parsers for the following show commands:

    * show interfaces wired {ifnum}

"""
# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, ListOf

class ShowInterfacesWiredSchema(MetaParser):

    """
    Schema for
        * show interfaces wired {ifnum}
    """

    schema = {
        'interface': {
            Any(description="Placeholder for interface name"): {
                'mac_address': str,
                Optional('status'): str,
                'ip_address': str,
                'broadcast_address': str,
                'netmask': str,
                'duplex': str,
                'speed': int,
                'input_load_interval': str,
                'input_rate_bps': str,
                'input_pps': str,
                'output_load_interval': str,
                'output_rate_bps': str,
                'output_pps': str,
                'mtu': int,
                'metric': int,
                'type': str,
                Optional('collisions'): int,
                Optional('txqueuelen'): int,
                'statistics': {
                    'rx_pkts_cumulative_total': int,
                    'rx_pkts_last_5_sec': int,
                    'tx_pkts_cumulative_total': int,
                    'tx_pkts_last_5_sec': int,
                    Optional('rx_bytes_cumulative_total'): int,
                    Optional('rx_bytes_last_5_sec'): int,
                    Optional('tx_bytes_cumulative_total'): int,
                    Optional('tx_bytes_last_5_sec'): int,
                    Optional('rx_octets_cumulative_total'): int,
                    Optional('rx_octets_last_5_sec'): int,
                    Optional('tx_octets_cumulative_total'): int,
                    Optional('tx_octets_last_5_sec'): int,
                    Optional('rx_drops_cumulative_total'): int,
                    Optional('rx_drops_last_5_sec'): int,
                    Optional('rx_err_cumulative_total'): int,
                    Optional('rx_err_last_5_sec'): int,
                    Optional('tx_err_cumulative_total'): int,
                    Optional('tx_err_last_5_sec'): int,
                    Optional('id'): int,
                    Optional('type'): int
                }
            }
        }
    }


class ShowInterfacesWired(ShowInterfacesWiredSchema):

    """
    Parser for
        * show interfaces wired {ifnum}
    """

    cli_command = "show interfaces wired {ifnum}"

    def cli(self, ifnum, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(ifnum=ifnum))

        ret_dict = {}

        # wired0    Link encap:Ethernet  HWaddr 5C:5A:C7:52:01:DC eMac Status: UP
        # wired0    Link encap:Ethernet  HWaddr D4:C9:3C:E6:B8:48
        p1 = re.compile(r'^(?P<name>\w+)\s+Link encap:Ethernet\s+HWaddr (?P<mac_address>[\w:]+)(?: eMac Status: (?P<status>\w+))?$')

        # inet addr: 9.2.46.109  Bcast: 9.2.46.255  Mask: 255.255.255.0
        p1_1 = re.compile(r'^inet +addr: (?P<ip_address>[0-9\.]+|unassigned)\s+Bcast:\s+(?P<broadcast_address>[0-9\.]+)\s+Mask:\s+(?P<netmask>[0-9\.]+)$')

        # UP BROADCAST RUNNING PROMISC MULTICAST  MTU:2400  Metric:1
        p1_2 = re.compile(r'^(?P<attributes>[\w\s]+)?\s+MTU:(?P<mtu>\d+)\s+Metric:(?P<metric>\d+)$')

        # collisions:0 txqueuelen:80
        p1_3 = re.compile(r'^collisions:(?P<collisions>\d+) txqueuelen:(?P<txqueuelen>\d+)$')

        # full Duplex, 1000 Mb/s
        p1_4 = re.compile(r'^(?P<duplex>\w+) Duplex, (?P<speed>\d+) Mb\/s$')

        # 5 minute input rate 25514 bits/sec, 20 packets/sec
        # 5 minute input rate n/a bits/sec, n/a packets/sec
        p1_5 = re.compile(r'^(?P<load_interval>[\w\s]+) input rate (?P<input_rate_bps>\d+|n\/a) bits\/sec,'
                          r'\s+(?P<input_pps>\d+|n\/a) packets\/sec$')

        # 5 minute output rate 4911 bits/sec, 1 packets/sec
        # 5 minute output rate n/a bits/sec, n/a packets/sec
        p1_6 = re.compile(r'^(?P<load_interval>[\w\s]+) output rate (?P<output_rate_bps>\d+|n\/a) bits\/sec, '
                          r'(?P<output_pps>\d+|n\/a) packets\/sec$')

        # ID         :               0             TYPE       :               0
        p1_7 = re.compile(r'^ID\s+:\s+(?P<id>\d+)\s+TYPE\s+:\s+(?P<type>\d+)$')

        # RX PKTS    :       216610184/14          TX PKTS    :         8818878/1
        p1_8 = re.compile(r'^RX PKTS\s+:\s+(?P<rx_pkts_cumulative_total>\d+)\/(?P<rx_pkts_last_5_sec>\d+)\s+'
                          r'TX PKTS\s+:\s+(?P<tx_pkts_cumulative_total>\d+)\/(?P<tx_pkts_last_5_sec>\d+)$')

        # RX OCTETS  :       349752895/54141       TX OCTETS  :        61400488/1453
        p1_9 = re.compile(r'^RX OCTETS\s+:\s+(?P<rx_oct_cumulative_total>\d+)\/(?P<rx_oct_last_5_sec>\d+)\s+'
                          r'TX OCTETS\s+:\s+(?P<tx_oct_cumulative_total>\d+)\/(?P<tx_oct_last_5_sec>\d+)$')

        # RX ERR     :              52/0           TX ERR     :               0/0
        p1_10 = re.compile(r'^RX ERR\s+:\s+(?P<rx_err_cumulative_total>\d+)\/(?P<rx_err_last_5_sec>\d+)\s+'
                           r'TX ERR\s+:\s+(?P<tx_err_cumulative_total>\d+)\/(?P<tx_err_last_5_sec>\d+)$')

        # RX BYTES   :     35331894561/1232        TX BYTES   :      1854544178/68
        p1_11 = re.compile(r'^RX BYTES\s+:\s+(?P<rx_byt_cumulative_total>\d+)\/(?P<rx_byt_last_5_sec>\d+)\s+'
                           r'TX BYTES\s+:\s+(?P<tx_byt_cumulative_total>\d+)\/(?P<tx_byt_last_5_sec>\d+)$')

        # RX DROPS   :               0/0
        p1_12 = re.compile(r'^RX DROPS\s+:\s+(?P<rx_drop_cumulative_total>\d+)\/(?P<rx_drop_last_5_sec>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # wired0    Link encap:Ethernet  HWaddr 5C:5A:C7:52:01:DC eMac Status: UP
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                name = match_dict['name']
                iface_dict = ret_dict.setdefault('interface',{}).setdefault(name, {})
                statistics = iface_dict.setdefault('statistics',{})
                iface_dict['type'] = 'ethernet'
                iface_dict['mac_address'] = match_dict['mac_address']
                iface_dict.update({'status': match_dict['status'].lower()} if match_dict['status'] else {})
                continue

            # inet addr: 9.2.46.109  Bcast: 9.2.46.255  Mask: 255.255.255.0
            m = p1_1.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['ip_address'] = match_dict['ip_address']
                iface_dict['broadcast_address'] = match_dict['broadcast_address']
                iface_dict['netmask'] = match_dict['netmask']
                continue

            # UP BROADCAST RUNNING PROMISC MULTICAST  MTU:2400  Metric:1
            m = p1_2.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['mtu'] = int(match_dict['mtu'])
                iface_dict['metric'] = int(match_dict['metric'])
                continue

            # collisions:0 txqueuelen:80
            m = p1_3.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['collisions'] = int(match_dict['collisions'])
                iface_dict['txqueuelen'] = int(match_dict['txqueuelen'])
                continue

            # full Duplex, 1000 Mb/s
            m = p1_4.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['duplex'] = match_dict['duplex']
                iface_dict['speed'] = int(match_dict['speed'])
                continue

            # 5 minute input rate 25514 bits/sec, 20 packets/sec
            # 5 minute input rate n/a bits/sec, n/a packets/sec
            m = p1_5.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['input_load_interval'] = match_dict['load_interval']
                iface_dict['input_rate_bps'] = match_dict['input_rate_bps']
                iface_dict['input_pps'] = match_dict['input_pps']
                continue

            # 5 minute output rate 4911 bits/sec, 1 packets/sec
            # 5 minute output rate n/a bits/sec, n/a packets/sec
            m = p1_6.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['output_load_interval'] = match_dict['load_interval']
                iface_dict['output_rate_bps'] = match_dict['output_rate_bps']
                iface_dict['output_pps'] = match_dict['output_pps']
                continue

            # ID         :               0             TYPE       :               0
            m = p1_7.match(line)
            if m:
                match_dict = m.groupdict()
                statistics['id'] = int(match_dict['id'])
                statistics['type'] = int(match_dict['type'])
                continue

            # RX PKTS    :         2123343/141         TX PKTS    :          109143/6
            m = p1_8.match(line)
            if m:
                match_dict = m.groupdict()
                statistics['rx_pkts_cumulative_total'] = int(match_dict['rx_pkts_cumulative_total'])
                statistics['rx_pkts_last_5_sec'] = int(match_dict['rx_pkts_last_5_sec'])
                statistics['tx_pkts_cumulative_total'] = int(match_dict['tx_pkts_cumulative_total'])
                statistics['tx_pkts_last_5_sec'] = int(match_dict['tx_pkts_last_5_sec'])
                continue

            # RX OCTETS  :       349752895/54141       TX OCTETS  :        61400488/1453
            m = p1_9.match(line)
            if m:
                match_dict = m.groupdict()
                statistics['rx_octets_cumulative_total'] = int(match_dict['rx_oct_cumulative_total'])
                statistics['rx_octets_last_5_sec'] = int(match_dict['rx_oct_last_5_sec'])
                statistics['tx_octets_cumulative_total'] = int(match_dict['tx_oct_cumulative_total'])
                statistics['tx_octets_last_5_sec'] = int(match_dict['tx_oct_last_5_sec'])
                continue

            # RX ERR     :              52/0           TX ERR     :               0/0
            m = p1_10.match(line)
            if m:
                match_dict = m.groupdict()
                statistics['rx_err_cumulative_total'] = int(match_dict['rx_err_cumulative_total'])
                statistics['rx_err_last_5_sec'] = int(match_dict['rx_err_last_5_sec'])
                statistics['tx_err_cumulative_total'] = int(match_dict['tx_err_cumulative_total'])
                statistics['tx_err_last_5_sec'] = int(match_dict['tx_err_last_5_sec'])
                continue

            # RX BYTES   :     35331894561/1232        TX BYTES   :      1854544178/68
            m = p1_11.match(line)
            if m:
                match_dict = m.groupdict()
                statistics['rx_bytes_cumulative_total'] = int(match_dict['rx_byt_cumulative_total'])
                statistics['rx_bytes_last_5_sec'] = int(match_dict['rx_byt_last_5_sec'])
                statistics['tx_bytes_cumulative_total'] = int(match_dict['tx_byt_cumulative_total'])
                statistics['tx_bytes_last_5_sec'] = int(match_dict['tx_byt_last_5_sec'])
                continue

            # RX DROPS   :               0/0
            m = p1_12.match(line)
            if m:
                match_dict = m.groupdict()
                statistics['rx_drops_cumulative_total'] = int(match_dict['rx_drop_cumulative_total'])
                statistics['rx_drops_last_5_sec'] = int(match_dict['rx_drop_last_5_sec'])
                continue

        return ret_dict



class ShowInterfacesDot11radioSchema(MetaParser):

    """
    Schema for
        * show interfaces dot11radio {ifnum}
    """

    schema = {
        'interface':{
            Any(description='Placeholder for interface name'): {
                'admin_state': str,
                'protocol_state': str,
                'hardware': str,
                'channel': str,
                'radio_mac_address': str,
                'mac_address': str,
                'attributes': str,
                'mtu': int,
                'metric': int,
                'rx': {
                    'packets': int,
                    'errors': int,
                    'drop': int,
                    'overrun': int,
                    'frame': int
                },
                'tx': {
                    'packets': int,
                    'errors': int,
                    'drop': int,
                    'overrun': int,
                    'carrier': int
                },
                'collisions': int,
                'txqueuelen':int,
                'rx_bytes': int,
                'tx_bytes': int,
                'interrupt': int,
                'memory': str,
                'ml_type': {
                    Any(description='Placeholder for ml/non_ml type'): { # ML_TYPE: NON_ML	DOT11 Statistics / ML_TYPE: ML	DOT11 Statistics
                        'statistics': {
                            Any(description='Placeholder for cumulative_total/last_five_seconds'): {
                                'host_rx_k_bytes': int,
                                'host_tx_k_bytes': int,
                                'unicast_rx': int,
                                'unicast_tx': int,
                                'broadcasts_rx': int,
                                'broadcasts_tx': int,
                                'beacons_rx': int,
                                'beacons_tx': int,
                                'probes_rx': int,
                                'probes_tx': int,
                                'multicast_rx': int,
                                'multicast_tx': int,
                                'mgmt_pkts_rx': int,
                                'mgmt_pkts_tx': int,
                                'ctrl_frame_rx': int,
                                'ctrl_frame_tx': int,
                                'rts_received':int,
                                'rts_transmitted':int,
                                'duplicate_frames': int,
                                'cts_not_received': int,
                                'mic_err': int,
                                'wep_err': int,
                                'fcs_error': int,
                                'retries': int,
                                'key_index_err': int,
                                'tx_failures': int,
                                'tx_drops': int
                            }
                        }
                    }
                },
                'beacons_missed': {
                    '0-30s': int,
                    '31-60s': int,
                    '61-90s': int,
                    '90s+': int
                },
                Optional('vap_rx_statistics'): {
                    'vap': int,
                    'ssid': str,
                    'mgmt': str,
                    'data': str,
                    'bk': str,
                    'be': str,
                    'vi': str,
                    'vo':str,
                    'data_bytes': str
                },
                Optional('vap_tx_statistics'): {
                    'vap': int,
                    'ssid': str,
                    'mgmt': str,
                    'beacon': str,
                    'data': str,
                    'bk': str,
                    'be': str,
                    'vi': str,
                    'vo':str,
                    'data_bytes': str,
                    'qos_retries': str,
                    'amdpu_subframe_retries': str
                }
            }
        }
    }


class ShowInterfacesDot11radio(ShowInterfacesDot11radioSchema):

    """
    Parser for
        * show interfaces dot11radio {ifnum}
    """

    cli_command = "show interfaces dot11radio {ifnum}"

    def cli(self, ifnum, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(ifnum=ifnum))

        ret_dict = {}

        # Dot11Radio0 is UP, line protocol is UP
        p1 = re.compile(r'^(?P<name>\w+) is (?P<admin_state>\w+), line protocol is (?P<protocol_state>\w+)$')

        # Hardware is 802.11 2.4G Radio, channel is 1
        p1_1 = re.compile(r'^Hardware is (?P<hardware>.*?), channel is (?P<channel>\d+)$')

        # Radio MAC is 5C:5A:C7:CB:7C:A0
        p1_2 = re.compile(r'^Radio MAC is (?P<radio_mac_address>[\w:]+)$')

        # Dot11Radio0     Link encap:Ethernet  HWaddr 5C:5A:C7:CB:7C:A0
        p1_3 = re.compile(r'^(?P<name>\w+)\s+Link encap:Ethernet\s+HWaddr (?P<mac_address>[\w:]+)$')

        # UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
        p1_4 = re.compile(r'^(?P<attributes>[\w\s]+)?\s+MTU:(?P<mtu>\d+)\s+Metric:(?P<metric>\d+)$')

        # RX packets:26749820 errors:0 dropped:0 overruns:0 frame:0
        p1_5 = re.compile('^RX packets:(?P<packets>\d+) errors:(?P<error>\d+) dropped:(?P<drop>\d+) overruns:(?P<overrun>\d+) frame:(?P<frame>\d+)$')

        # TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
        p1_6 = re.compile('^TX packets:(?P<packets>\d+) errors:(?P<error>\d+) dropped:(?P<drop>\d+) overruns:(?P<overrun>\d+) carrier:(?P<carrier>\d+)$')

        # collisions:0 txqueuelen:1000
        p1_7 = re.compile(r'^collisions:(?P<collisions>\d+) txqueuelen:(?P<txqueuelen>\d+)$')

        # RX bytes:3849651069 (3.5 GiB)  TX bytes:0 (0.0 B)
        p1_8 = re.compile(r'^RX bytes:(?P<rx_bytes>\d+) \([\d.\s\w]+\)\s+TX bytes:(?P<tx_bytes>\d+) \([\d.\s\w]+\)$')

        # Interrupt:65 Memory:f8000000-f8200000
        p1_9 = re.compile(r'^Interrupt:(?P<interrupt>\d+) Memory:(?P<memory>[\w-]+)$')

        # ML_TYPE: NON_ML	DOT11 Statistics (Cumulative Total/Last 5 Seconds):
        p1_10 = re.compile(r'^(ML_TYPE: (?P<ml_type>[\w_]+)\s+)?DOT11 Statistics \(Cumulative Total\/Last 5 Seconds\):$')

        # Host Rx K Bytes:             0/0        Host Tx K Bytes:             0/0
        p1_11 = re.compile(r'^Host Rx K Bytes:\s+(?P<host_rx_cumulative>\d+)\/(?P<host_rx_last_5sec>\d+)'
                           r'\s+Host Tx K Bytes:\s+(?P<host_tx_cumulative>\d+)\/(?P<host_tx_last_5sec>\d+)$')

        # Unicasts Rx:                 0/0        Unicasts Tx:                 0/0
        p1_12 = re.compile(r'^Unicasts Rx:\s+(?P<unicasts_rx_cumulative>\d+)\/(?P<unicasts_rx_last_5sec>\d+)'
                           r'\s+Unicasts Tx:\s+(?P<unicasts_tx_cumulative>\d+)\/(?P<unicasts_tx_last_5sec>\d+)$')

        # Broadcasts Rx:               0/0        Broadcasts Tx:               0/0
        p1_13 = re.compile(r'^Broadcasts Rx:\s+(?P<broadcasts_rx_cumulative>\d+)\/(?P<broadcasts_rx_last_5sec>\d+)'
                           r'\s+Broadcasts Tx:\s+(?P<broadcasts_tx_cumulative>\d+)\/(?P<broadcasts_tx_last_5sec>\d+)$')

        # Beacons Rx:           42662813/2219     Beacons Tx:                  0/0
        p1_14 = re.compile(r'^Beacons Rx:\s+(?P<beacons_rx_cumulative>\d+)\/(?P<beacons_rx_last_5sec>\d+)'
                           r'\s+Beacons Tx:\s+(?P<beacons_tx_cumulative>\d+)\/(?P<beacons_tx_last_5sec>\d+)$')

        # Probes Rx:              208124/16       Probes Tx:                   0/0
        p1_15 = re.compile(r'^Probes Rx:\s+(?P<probes_rx_cumulative>\d+)\/(?P<probes_rx_last_5sec>\d+)'
                           r'\s+Probes Tx:\s+(?P<probes_tx_cumulative>\d+)\/(?P<probes_tx_last_5sec>\d+)$')

        # Multicasts Rx:               0/0        Multicasts Tx:               0/0
        p1_16 = re.compile(r'^Multicasts Rx:\s+(?P<multicasts_rx_cumulative>\d+)\/(?P<multicasts_rx_last_5sec>\d+)'
                           r'\s+Multicasts Tx:\s+(?P<multicasts_tx_cumulative>\d+)\/(?P<multicasts_tx_last_5sec>\d+)$')

        # Mgmt Packets Rx:      42870937/2235     Mgmt Packets Tx:             0/0
        p1_17 = re.compile(r'^Mgmt Packets Rx:\s+(?P<mgmt_rx_pkts_cumulative>\d+)\/(?P<mgmt_rx_pkts_last_5sec>\d+)'
                           r'\s+Mgmt Packets Tx:\s+(?P<mgmt_tx_pkts_cumulative>\d+)\/(?P<mgmt_tx_pkts_last_5sec>\d+)$')

        # Ctrl Frames Rx:          93989/15       Ctrl Frames Tx:              0/0
        p1_18 = re.compile(r'^Ctrl Frames Rx:\s+(?P<ctrl_frame_rx_cumulative>\d+)\/(?P<ctrl_frame_rx_last_5sec>\d+)'
                           r'\s+Ctrl Frames Tx:\s+(?P<ctrl_frame_tx_cumulative>\d+)\/(?P<ctrl_frame_tx_last_5sec>\d+)$')

        # RTS received:            12523/2        RTS transmitted:             0/0
        p1_19 = re.compile(r'^RTS received:\s+(?P<rts_received_rx_cumulative>\d+)\/(?P<rts_received_rx_last_5sec>\d+)'
                           r'\s+RTS transmitted:\s+(?P<rts_received_tx_cumulative>\d+)\/(?P<rts_received_tx_last_5sec>\d+)$')

        # Duplicate frames:            0/0        CTS not received:            0/0
        p1_20 = re.compile(r'^Duplicate frames:\s+(?P<duplicate_frames_rx_cumulative>\d+)\/(?P<duplicate_frames_rx_last_5sec>\d+)'
                           r'\s+CTS not received:\s+(?P<cts_not_received_cumulative>\d+)\/(?P<cts_not_received_last_5sec>\d+)$')

        # MIC errors:                  0/0        WEP errors:                  0/0
        p1_21 = re.compile(r'^MIC errors:\s+(?P<mic_err_cumulative>\d+)\/(?P<mic_err_last_5sec>\d+)'
                           r'\s+WEP errors:\s+(?P<wep_err_cumulative>\d+)\/(?P<wep_err_last_5sec>\d+)$')

        # FCS errors:            5300255/231      Retries:                     0/0
        p1_22 = re.compile(r'^FCS errors:\s+(?P<fcs_errors_rx_cumulative>\d+)\/(?P<fcs_errors_rx_last_5sec>\d+)'
                           r'\s+Retries:\s+(?P<retries_tx_cumulative>\d+)\/(?P<retries_tx_last_5sec>\d+)$')

        # Key Index errors:            0/0        Tx Failures:                 0/0
        p1_23 = re.compile(r'^Key Index errors:\s+(?P<key_index_err_rx_cumulative>\d+)\/(?P<key_index_err_rx_last_5sec>\d+)'
                           r'\s+Tx Failures:\s+(?P<tx_failures_cumulative>\d+)\/(?P<tx_failures_last_5sec>\d+)$')

        #  Tx Drops:                    0/0
        p1_24 = re.compile(r'^Tx Drops:\s+(?P<tx_drops_cumulative>\d+)\/(?P<tx_drops_last_5sec>\d+)$')

        # Beacons missed: 0-30s 31-60s 61-90s 90s+
        p1_25 = re.compile(r'^Beacons missed: (?P<beacon_missed>[\w\s\-+]+)$')

        # 0      0      0    0
        p1_26 = re.compile(r'^(?P<values>[\d\s]+)$')

        # Vap RX statistics:
        p1_27 = re.compile(r'^Vap RX statistics:$')

        # Vap TX statistics:
        p1_28 = re.compile(r'^Vap TX statistics:$')

        # vap         ssid  MGMT DATA [BK  BE  VI VO] Bytes(Data)
        # 1 JEY_OPEN_WGB 944/0  0/0 0/0 0/0 0/0 0/0         0/0
        p1_29 = re.compile(r'^(?P<vap_id>\d+)\s+(?P<ssid>[\w_]+)\s+(?P<mgmt>[\d\/]+)\s+'
                           r'(?P<data>[\d\/]+)\s+(?P<bk>[\d\/]+)\s+(?P<be>[\d\/]+)\s+'
                           r'(?P<vi>[\d\/]+)\s+(?P<vo>[\d\/]+)\s+(?P<data_bytes>[\d\/]+)$')

        # vap         ssid  MGMT      Beacon     DATA [BK  BE  VI VO] Bytes(Data) QosRetries AMDPU-SubFrameRetries
        # 1   JEY_OPEN_WGB 813/0 23654269/48 181306/0 0/0 0/0 0/0 0/0         0/0        0/0                   0/0
        p1_30 = re.compile(r'^(?P<vap_id>\d+)\s+(?P<ssid>[\w_]+)\s+(?P<mgmt>[\d\/]+)\s+(?P<beacon>[\d\/]+)\s+'
                           r'(?P<data>[\d\/]+)\s+(?P<bk>[\d\/]+)\s+(?P<be>[\d\/]+)\s+(?P<vi>[\d\/]+)\s+'
                           r'(?P<vo>[\d\/]+)\s+(?P<data_bytes>[\d\/]+)\s+(?P<qos_retries>[\d\/]+)?\s+'
                           r'(?P<amdpu_subframe_retries>[\d\/]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Dot11Radio0 is UP, line protocol is UP
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                name = match_dict['name']
                iface_dict = ret_dict.setdefault('interface',{}).setdefault(name, {})
                iface_dict['admin_state'] = match_dict['admin_state'].lower()
                iface_dict['protocol_state'] = match_dict['protocol_state'].lower()
                continue

            # Hardware is 802.11 2.4G Radio, channel is 1
            m = p1_1.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['hardware'] = match_dict['hardware']
                iface_dict['channel'] = match_dict['channel']
                continue

            # Radio MAC is 5C:5A:C7:CB:7C:A0
            m = p1_2.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['radio_mac_address'] = match_dict['radio_mac_address']
                continue

            # Dot11Radio0     Link encap:Ethernet  HWaddr 5C:5A:C7:CB:7C:A0
            m = p1_3.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['mac_address'] = match_dict['mac_address']
                continue

            # UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
            m = p1_4.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['attributes'] = match_dict['attributes'].lower()
                iface_dict['mtu'] = int(match_dict['mtu'])
                iface_dict['metric'] = int(match_dict ['metric'])
                continue

            # RX packets:26749820 errors:0 dropped:0 overruns:0 frame:0
            m = p1_5.match(line)
            if m:
                match_dict = m.groupdict()
                rx_dict = iface_dict.setdefault('rx', {})
                rx_dict['packets'] = int(match_dict['packets'])
                rx_dict['errors'] = int(match_dict['error'])
                rx_dict['drop'] = int(match_dict['drop'])
                rx_dict['overrun'] = int(match_dict['overrun'])
                rx_dict['frame'] = int(match_dict['frame'])
                continue

            # TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
            m = p1_6.match(line)
            if m:
                match_dict = m.groupdict()
                tx_dict = iface_dict.setdefault('tx', {})
                tx_dict['packets'] = int(match_dict['packets'])
                tx_dict['errors'] = int(match_dict['error'])
                tx_dict['drop'] = int(match_dict['drop'])
                tx_dict['overrun'] = int(match_dict['overrun'])
                tx_dict['carrier'] = int(match_dict['carrier'])
                continue

            # collisions:0 txqueuelen:1000
            m = p1_7.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['collisions'] = int(match_dict['collisions'])
                iface_dict['txqueuelen'] = int(match_dict['txqueuelen'])
                continue

            # RX bytes:3849651069 (3.5 GiB)  TX bytes:0 (0.0 B)
            m = p1_8.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['rx_bytes'] = int(match_dict['rx_bytes'])
                iface_dict['tx_bytes'] = int(match_dict['tx_bytes'])
                continue

            # Interrupt:65 Memory:f8000000-f8200000
            m = p1_9.match(line)
            if m:
                match_dict = m.groupdict()
                iface_dict['interrupt'] = int(match_dict['interrupt'])
                iface_dict['memory'] = match_dict['memory']
                continue

            # ML_TYPE: NON_ML	DOT11 Statistics (Cumulative Total/Last 5 Seconds):
            m = p1_10.match(line)
            if m:
                match_dict = m.groupdict()
                if match_dict['ml_type']:
                    ml_type = iface_dict.setdefault('ml_type', {}).setdefault(match_dict['ml_type'].lower(), {})
                else:
                    ml_type = iface_dict.setdefault('ml_type', {}).setdefault("default", {})
                statistics = ml_type.setdefault('statistics', {})
                cumulative = statistics.setdefault('cumulative_total', {})
                last_5_sec = statistics.setdefault('last_5_seconds', {})
                continue

            # Host Rx K Bytes:             0/0        Host Tx K Bytes:             0/0
            m = p1_11.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['host_rx_k_bytes'] = int(match_dict['host_rx_cumulative'])
                cumulative['host_tx_k_bytes'] = int(match_dict['host_tx_cumulative'])
                last_5_sec['host_rx_k_bytes'] = int(match_dict['host_rx_last_5sec'])
                last_5_sec['host_tx_k_bytes'] = int(match_dict['host_tx_last_5sec'])
                continue

            # Unicasts Rx:                 0/0        Unicasts Tx:                 0/0
            m = p1_12.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['unicast_rx'] = int(match_dict['unicasts_rx_cumulative'])
                cumulative['unicast_tx'] = int(match_dict['unicasts_tx_cumulative'])
                last_5_sec['unicast_rx'] = int(match_dict['unicasts_rx_last_5sec'])
                last_5_sec['unicast_tx'] = int(match_dict['unicasts_tx_last_5sec'])
                continue

            # Broadcasts Rx:               0/0        Broadcasts Tx:               0/0
            m = p1_13.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['broadcasts_rx'] = int(match_dict['broadcasts_rx_cumulative'])
                cumulative['broadcasts_tx'] = int(match_dict['broadcasts_tx_cumulative'])
                last_5_sec['broadcasts_rx'] = int(match_dict['broadcasts_rx_last_5sec'])
                last_5_sec['broadcasts_tx'] = int(match_dict['broadcasts_tx_last_5sec'])
                continue

            # Beacons Rx:           42662813/2219     Beacons Tx:                  0/0
            m = p1_14.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['beacons_rx'] = int(match_dict['beacons_rx_cumulative'])
                cumulative['beacons_tx'] = int(match_dict['beacons_tx_cumulative'])
                last_5_sec['beacons_rx'] = int(match_dict['beacons_rx_last_5sec'])
                last_5_sec['beacons_tx'] = int(match_dict['beacons_tx_last_5sec'])
                continue

            # Probes Rx:              208124/16       Probes Tx:                   0/0
            m = p1_15.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['probes_rx'] = int(match_dict['probes_rx_cumulative'])
                cumulative['probes_tx'] = int(match_dict['probes_tx_cumulative'])
                last_5_sec['probes_rx'] = int(match_dict['probes_rx_last_5sec'])
                last_5_sec['probes_tx'] = int(match_dict['probes_tx_last_5sec'])
                continue

            # Multicasts Rx:               0/0        Multicasts Tx:               0/0
            m = p1_16.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['multicast_rx'] = int(match_dict['multicasts_rx_cumulative'])
                cumulative['multicast_tx'] = int(match_dict['multicasts_tx_cumulative'])
                last_5_sec['multicast_rx'] = int(match_dict['multicasts_rx_last_5sec'])
                last_5_sec['multicast_tx'] = int(match_dict['multicasts_tx_last_5sec'])
                continue

            # Mgmt Packets Rx:      42870937/2235     Mgmt Packets Tx:             0/0
            m = p1_17.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['mgmt_pkts_rx'] = int(match_dict['mgmt_rx_pkts_cumulative'])
                cumulative['mgmt_pkts_tx'] = int(match_dict['mgmt_tx_pkts_cumulative'])
                last_5_sec['mgmt_pkts_rx'] = int(match_dict['mgmt_rx_pkts_last_5sec'])
                last_5_sec['mgmt_pkts_tx'] = int(match_dict['mgmt_tx_pkts_last_5sec'])
                continue

            # Ctrl Frames Rx:          93989/15       Ctrl Frames Tx:              0/0
            m = p1_18.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['ctrl_frame_rx'] = int(match_dict['ctrl_frame_rx_cumulative'])
                cumulative['ctrl_frame_tx'] = int(match_dict['ctrl_frame_tx_cumulative'])
                last_5_sec['ctrl_frame_rx'] = int(match_dict['ctrl_frame_rx_last_5sec'])
                last_5_sec['ctrl_frame_tx'] = int(match_dict['ctrl_frame_tx_last_5sec'])
                continue

            # RTS received:            12523/2        RTS transmitted:             0/0
            m = p1_19.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['rts_received'] = int(match_dict['rts_received_rx_cumulative'])
                cumulative['rts_transmitted'] = int(match_dict['rts_received_tx_cumulative'])
                last_5_sec['rts_received'] = int(match_dict['rts_received_rx_last_5sec'])
                last_5_sec['rts_transmitted'] = int(match_dict['rts_received_tx_last_5sec'])
                continue

            # Duplicate frames:            0/0        CTS not received:            0/0
            m = p1_20.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['duplicate_frames'] = int(match_dict['duplicate_frames_rx_cumulative'])
                cumulative['cts_not_received'] = int(match_dict['cts_not_received_cumulative'])
                last_5_sec['duplicate_frames'] = int(match_dict['duplicate_frames_rx_last_5sec'])
                last_5_sec['cts_not_received'] = int(match_dict['cts_not_received_last_5sec'])
                continue

            # MIC errors:                  0/0        WEP errors:                  0/0
            m = p1_21.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['mic_err'] = int(match_dict['mic_err_cumulative'])
                cumulative['wep_err'] = int(match_dict['wep_err_cumulative'])
                last_5_sec['mic_err'] = int(match_dict['mic_err_last_5sec'])
                last_5_sec['wep_err'] = int(match_dict['wep_err_last_5sec'])
                continue

            # FCS errors:            5300255/231      Retries:                     0/0
            m = p1_22.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['fcs_error'] = int(match_dict['fcs_errors_rx_cumulative'])
                cumulative['retries'] = int(match_dict['retries_tx_cumulative'])
                last_5_sec['fcs_error'] = int(match_dict['fcs_errors_rx_last_5sec'])
                last_5_sec['retries'] = int(match_dict['retries_tx_last_5sec'])
                continue

            # Key Index errors:            0/0        Tx Failures:                 0/0
            m = p1_23.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['key_index_err'] = int(match_dict['key_index_err_rx_cumulative'])
                cumulative['tx_failures'] = int(match_dict['tx_failures_cumulative'])
                last_5_sec['key_index_err'] = int(match_dict['key_index_err_rx_last_5sec'])
                last_5_sec['tx_failures'] = int(match_dict['tx_failures_last_5sec'])
                continue

            #  Tx Drops:                    0/0
            m = p1_24.match(line)
            if m:
                match_dict = m.groupdict()
                cumulative['tx_drops'] = int(match_dict['tx_drops_cumulative'])
                last_5_sec['tx_drops'] = int(match_dict['tx_drops_last_5sec'])
                continue

            # Beacons missed: 0-30s 31-60s 61-90s 90s+
            m = p1_25.match(line)
            if m:
                match_dict = m.groupdict()
                beacon_missed = match_dict['beacon_missed'].split()
                continue

            # 0      0      0    0
            m = p1_26.match(line)
            if m and beacon_missed:
                match_dict = m.groupdict()
                values = map(int, match_dict['values'].split())
                iface_dict.setdefault('beacons_missed', {})
                result = dict(zip(beacon_missed, values))
                iface_dict['beacons_missed'] = result
                continue

            # Vap RX statistics:
            m = p1_27.match(line)
            if m:
                vap_rx_statistics = iface_dict.setdefault('vap_rx_statistics', {})
                continue

            # Vap TX statistics:
            m = p1_28.match(line)
            if m:
                vap_tx_statistics = iface_dict.setdefault('vap_tx_statistics', {})
                continue

            # vap         ssid  MGMT DATA [BK  BE  VI VO] Bytes(Data)
            # 1 JEY_OPEN_WGB 944/0  0/0 0/0 0/0 0/0 0/0         0/0
            m = p1_29.match(line)
            if m:
                match_dict = m.groupdict()
                vap_rx_statistics['vap'] = int(match_dict['vap_id'])
                vap_rx_statistics['ssid'] = match_dict['ssid']
                vap_rx_statistics['mgmt'] = match_dict['mgmt']
                vap_rx_statistics['data'] = match_dict['data']
                vap_rx_statistics['bk'] = match_dict['bk']
                vap_rx_statistics['be'] = match_dict['be']
                vap_rx_statistics['vi'] = match_dict['vi']
                vap_rx_statistics['vo'] = match_dict['vo']
                vap_rx_statistics['data_bytes'] = match_dict['data_bytes']
                continue

            # vap         ssid  MGMT      Beacon     DATA [BK  BE  VI VO] Bytes(Data) QosRetries AMDPU-SubFrameRetries
            #   1 JEY_OPEN_WGB 813/0 23654269/48 181306/0 0/0 0/0 0/0 0/0         0/0        0/0                   0/0
            m = p1_30.match(line)
            if m:
                match_dict = m.groupdict()
                vap_tx_statistics['vap'] = int(match_dict['vap_id'])
                vap_tx_statistics['ssid'] = match_dict['ssid']
                vap_tx_statistics['mgmt'] = match_dict['mgmt']
                vap_tx_statistics['beacon'] = match_dict['beacon']
                vap_tx_statistics['data'] = match_dict['data']
                vap_tx_statistics['bk'] = match_dict['bk']
                vap_tx_statistics['be'] = match_dict['be']
                vap_tx_statistics['vi'] = match_dict['vi']
                vap_tx_statistics['vo'] = match_dict['vo']
                vap_tx_statistics['data_bytes'] = match_dict['data_bytes']
                vap_tx_statistics['qos_retries'] = match_dict['qos_retries']
                vap_tx_statistics['amdpu_subframe_retries'] = match_dict['amdpu_subframe_retries']
                continue

        return ret_dict
