''' show_mrp.py
IOSXE parsers for the following show commands:
    * show mrp ports
    * show platform software fed switch active ifm mappings
    * show mrp ring <ring-id> statistics all
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ==========================
# Schema for:
#  * 'show mrp ports'
# ==========================
class ShowMrpPortsSchema(MetaParser):
    """Schema for show mrp ports """
    schema = {
            'mrp_rings': {
                Any(): {
                    str: str,
                    },
                },
            }
# ==========================
# Parser for:
#  * 'show mrp ports'
# ==========================
class ShowMrpPorts(ShowMrpPortsSchema):
    """Parser for show mrp ports """
    cli_command = 'show mrp ports'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        result_dict = {}

        #Ring ID : 1
        p1 = re.compile(r"^Ring ID\s+\:\s+(?P<ring_id>\d+)$")
        #Gi1/0/1                 Forwarding
        #Gi1/0/2                 Blocked
        #n/a                     n/a
        #Gi1/0/1                 Disabled
        p2 = re.compile(r"^(?P<portname>\S+)\s+(?P<port_status>(Forwarding|Blocked|n\/a|Not Connected|Disabled|Unknown))$")

        for line in output.splitlines():

            #Ring ID : 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mrp_ring_dict = result_dict.setdefault('mrp_rings', {})
                ring_dict = mrp_ring_dict.setdefault(group['ring_id'], {})
            #Gi1/0/1                 Forwarding
            #Gi1/0/2                 Blocked
            #n/a                     n/a
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({Common.convert_intf_name(group['portname']) : group['port_status']})

        return result_dict

# ==========================
# Schema for:
#  * 'show mrp ring'
# ==========================
class ShowMrpRingSchema(MetaParser):
    """Schema for show mrp ring """
    schema = {
            'mrp_rings': {
                Any(): {
                    Optional('ring') : str,
                    Optional('profile') : str,
                    Optional('mode') : str,
                    Optional('priority') : str,
                    Optional('operation_mode') : str,
                    Optional('from') : str,
                    Optional('license') : str,
                    Optional('gateway') : {
                        Optional('status') : str,
                        },
                    Optional('best_manager') : {
                        Optional('mac_address') : str,
                        Optional('priority') : str,
                        },
                    Optional('network_topology') : str,
                    Optional('network_status') : str,
                    Optional('port1') : {
                        Optional('mac_address') : str,
                        Optional('interface') : str,
                        Optional('status') : str,
                        },
                    Optional('port2') : {
                        Optional('mac_address') : str,
                        Optional('interface') : str,
                        Optional('status') : str,
                        },
                    Optional('vlan_id') : str,
                    Optional('domain_name') : str,
                    Optional('domain_id') : str,
                    Optional('topology_change_request_interval') : str,
                    Optional('topology_change_repeat_count') : str,
                    Optional('short_test_frame_interval') : str,
                    Optional('default_test_frame_interval') : str,
                    Optional('operational_test_frame_interval') : str,
                    Optional('test_monitoring_interval_count') : str,
                    Optional('test_monitoring_extended_interval_count') : str,
                    Optional('link_down_timer_interval') : str,
                    Optional('link_up_timer_interval') : str,
                    Optional('link_change_up_or_down_count') : str,
                    },
                },
            }
# ==========================
# Parser for:
#  * 'show mrp ring'
# ==========================
class ShowMrpRing(ShowMrpRingSchema):
    """Parser for:
        * show mrp ring
        * show mrp ring {ring_id}
    """
    cli_command = ["show mrp ring" ,
            "show mrp ring {ring_id}"]

    def cli(self, ring_id=None, output=None):
        if not output:
            if not ring_id:
                output = self.device.execute(self.cli_command[0])
            else:
                output = self.device.execute(self.cli_command[1].format(ring_id = ring_id))

        #MRP ring 4
        p1 = re.compile(r"^MRP\s+ring\s+(?P<ring_id>\d+)$")
        #MRP ring 18 not configured
        p2 = re.compile(r"^MRP ring\s+(?P<ring_id>\d+)\s+not configured$")
        #Profile         : 200 ms
        p3 = re.compile(r"^Profile\s+\:\s+(?P<profile>\d+)\s+ms$")
        #Mode            : Auto-Manager
        p4 = re.compile(r"^Mode\s+\:\s+(?P<mode>(Auto\-Manager|Manager|Client))$")
        #Priority        : 40960
        p5 = re.compile(r"^Priority\s+\:\s+(?P<priority>\d+)$")
        #Operational Mode: Client
        p6 = re.compile(r"^Operational Mode(\s+)?\:\s+(?P<operation_mode>(Manager|Client))$")
        #From            : CLI
        p7 = re.compile(r"^From\s+:\s+(?P<from>CLI)$")
        #License         : Not Applicable
        p8 = re.compile(r"^License\s+:\s+(?P<license>Not\sApplicable)$")
        #Gateway         :
        p9 = re.compile(r"^Gateway\s+\:$")
        # Status         : Disabled
        p9_1 = re.compile(r"^\s+Status\s+\:\s+(?P<status>(Disabled|Enabled))$")
        #Best Manager    :
        p10 = re.compile(r"^Best Manager\s+\:$")
        # MAC Address    : 04:A7:41:4D:20:07
        p10_1 = re.compile(r"^\s+MAC Address\s+\:\s+(?P<mac_address>(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2}))$")
        # Priority       : 40960
        p10_2 = re.compile(r"^\s+Priority\s+\:\s+(?P<priority>\d+)$")
        #Network Topology: Ring
        p11 = re.compile(r"^Network Topology(\s+)?\:\s+(?P<network_topology>Ring)$")
        #Network Status  : CLOSED
        p12 = re.compile(r"^Network Status\s+\:\s+(?P<network_status>(CLOSED|OPEN|UNKNOWN))$")
        #Port1:                                     Port2:
        p13 = re.compile(r"^Port1:\s+Port2\:$")
        # MAC Address    :6C:03:09:A0:07:87          MAC Address    :6C:03:09:A0:07:88
        p13_1 = re.compile(r"^\s+MAC Address\s+\:(?P<mac_address1>(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2}))\s+MAC Address\s+:(?P<mac_address2>(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2}))")
        # Interface      :Gi1/0/7                    Interface      :Gi1/0/8
        p13_2 = re.compile(r"^\s+Interface\s+\:(?P<interface1>\S+)\s+Interface\s+\:(?P<interface2>\S+)$")
        # Status         :Forwarding                 Status         :Forwarding
        p13_3 = re.compile(r"^\s+Status\s+\:(?P<status1>(Forwarding|Blocked|Not Connected))\s+Status\s+\:(?P<status2>(Forwarding|Blocked|Not Connected))$")
        #VLAN ID     : 141
        p14 = re.compile(r"^VLAN ID\s+\:\s+(?P<vlan_id>\d+)$")
        #Domain Name : RING4
        p15 = re.compile(r"^Domain Name\s+\:\s+(?P<domain_name>[\w\s]+)$")
        #Domain ID   : FFFFFFFF-FFFF-FFFF-FFFF-AAAAAAAAAAAE
        p16 = re.compile(r"^Domain ID\s+\:\s+(?P<domain_id>[\w\-]*)$")
        #Topology Change Request Interval        : 10ms
        p17 = re.compile(r"^Topology Change Request Interval\s+:\s+(?P<topology_change_request_interval>\d+)ms$")
        #Topology Change Repeat Count            : 3
        p18 = re.compile(r"^Topology Change Repeat Count\s+:\s+(?P<topology_change_repeat_count>\d+)$")
        #Short Test Frame Interval               : 10ms
        p19 = re.compile(r"^Short Test Frame Interval\s+\s:\s+(?P<short_test_frame_interval>\d+)ms$")
        #Default Test Frame Interval             : 20ms
        p20 = re.compile(r"^Default Test Frame Interval\s+\s:\s+(?P<default_test_frame_interval>\d+)ms$")
        #Operational Test Frame Interval         : 20ms
        p21 = re.compile(r"^Operational Test Frame Interval\s+\s:\s+(?P<operational_test_frame_interval>\d+)ms$")
        #Test Monitoring Interval Count          : 3
        p22 = re.compile(r"^Test Monitoring Interval Count\s+:\s+(?P<test_monitoring_interval_count>\d+)$")
        #Test Monitoring Extended Interval Count : N/A
        p23 = re.compile(r"^Test Monitoring Extended Interval Count\s+:\s+(?P<test_monitoring_extended_interval_count>((N\/A)|(\d+)))$")
        #Link Down Timer Interval        : 20 ms
        p24 = re.compile(r"^Link Down Timer Interval\s+:\s+(?P<link_down_timer_interval>\d+)\s+ms$")
        #Link Up Timer Interval          : 20 ms
        p25 = re.compile(r"^Link Up Timer Interval\s+:\s+(?P<link_up_timer_interval>\d+)\s+ms$")
        #Link Change (Up or Down) count  :  4 ms
        p26 = re.compile(r"^Link Change \(Up or Down\) count\s+:\s+(?P<link_change_up_or_down_count>\d+)\s+ms$")

        result_dict = {}

        for line in output.splitlines():

            #MRP ring 4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mrp_ring_dict = result_dict.setdefault('mrp_rings', {})
                ring_dict = mrp_ring_dict.setdefault(group['ring_id'], {})

            #MRP ring 18 not configured
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mrp_ring_dict = result_dict.setdefault('mrp_rings', {})
                ring_dict = mrp_ring_dict.setdefault(group['ring_id'], {})
                ring_dict.update({'ring' : 'not configured'})

            #Profile         : 200 ms
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'profile' : group['profile']})

            #Mode            : Auto-Manager
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'mode' : group['mode']})

            #Priority        : 40960
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'priority' : group['priority']})

            #Operational Mode: Client
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'operation_mode' : group['operation_mode']})

            #From            : CLI
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'from' : group['from']})

            #License         : Not Applicable
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'license' : group['license']})

            #Gateway         :
            m = p9.match(line)
            if m:
                gateway_dict = ring_dict.setdefault('gateway', {})
            # Status         : Disabled
            m = p9_1.match(line)
            if m:
                group = m.groupdict()
                gateway_dict.update({'status' : group['status']})

            #Best Manager    :
            m = p10.match(line)
            if m:
                best_mgr_dict = ring_dict.setdefault('best_manager', {})
            # MAC Address    : 04:A7:41:4D:20:07
            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                best_mgr_dict.update({'mac_address' : group['mac_address']})
            # Priority       : 40960
            m = p10_2.match(line)
            if m:
                group = m.groupdict()
                best_mgr_dict.update({'priority' : group['priority']})

            #Network Topology: Ring
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'network_topology' : group['network_topology']})

            #Network Status  : CLOSED
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'network_status' : group['network_status']})

            #Port1:                                     Port2:
            m = p13.match(line)
            if m:
                port1_dict = ring_dict.setdefault('port1', {})
                port2_dict = ring_dict.setdefault('port2', {})
            # MAC Address    :6C:03:09:A0:07:87          MAC Address    :6C:03:09:A0:07:88
            m = p13_1.match(line)
            if m:
                group = m.groupdict()
                port1_dict.update({"mac_address" : group['mac_address1']})
                port2_dict.update({"mac_address" : group['mac_address2']})
            # Interface      :Gi1/0/7                    Interface      :Gi1/0/8
            m = p13_2.match(line)
            if m:
                group = m.groupdict()
                port1_dict.update({"interface" : Common.convert_intf_name(group['interface1'])})
                port2_dict.update({"interface" : Common.convert_intf_name(group['interface2'])})
            # Status         :Forwarding                 Status         :Forwarding
            m = p13_3.match(line)
            if m:
                group = m.groupdict()
                port1_dict.update({"status" : group['status1']})
                port2_dict.update({"status" : group['status2']})

            #VLAN ID     : 141
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'vlan_id' : group['vlan_id']})

            #Domain Name : RING4
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'domain_name' : group['domain_name'].strip()})

            #Domain ID   : FFFFFFFF-FFFF-FFFF-FFFF-AAAAAAAAAAAE
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'domain_id' : group['domain_id']})

            #Topology Change Request Interval        : 10ms
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'topology_change_request_interval' : group['topology_change_request_interval']})

            #Topology Change Repeat Count            : 3
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'topology_change_repeat_count' : group['topology_change_repeat_count']})

            #Short Test Frame Interval               : 10ms
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'short_test_frame_interval' : group['short_test_frame_interval']})

            #Default Test Frame Interval             : 20ms
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'default_test_frame_interval' : group['default_test_frame_interval']})

            #Operational Test Frame Interval         : 20ms
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'operational_test_frame_interval' : group['operational_test_frame_interval']})

            #Test Monitoring Interval Count          : 3
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'test_monitoring_interval_count' : group['test_monitoring_interval_count']})

            #Test Monitoring Extended Interval Count : N/A
            m = p23.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'test_monitoring_extended_interval_count' : group['test_monitoring_extended_interval_count']})

            #Link Down Timer Interval        : 20 ms
            m = p24.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'link_down_timer_interval' : group['link_down_timer_interval']})

            #Link Up Timer Interval          : 20 ms
            m = p25.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'link_up_timer_interval' : group['link_up_timer_interval']})

            #Link Change (Up or Down) count  :  4 ms
            m = p26.match(line)
            if m:
                group = m.groupdict()
                ring_dict.update({'link_change_up_or_down_count' : group['link_change_up_or_down_count']})

        return result_dict


class ShowPlatformMrpMappingsSchema(MetaParser):
    """Schema for show platform mrp mappings """

    schema = {
        'mrp_rings': {
            Any(): {
                Optional('ring_instance'): str
            }
        }
    }

class ShowPlatformMrpMappings(ShowPlatformMrpMappingsSchema):
    """Parser for: show platform mrp mappings"""

    cli_command = 'show platform mrp mappings'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        #MRP Ring-id Instance Mappings
        p1 = re.compile(r"^Ring-id\s+Ring-instance$")

        #2                     3
        p2 = re.compile(r"^(?P<ring_id>\d+)\s+(?P<ring_instance>\d+)$")

        for line in output.splitlines():

            # MRP Ring-id Instance Mappings
            m = p1.match(line)
            if m:
                mrp_ring_dict = ret_dict.setdefault('mrp_rings', {})

            #2                     3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ring_id_dict = mrp_ring_dict.setdefault(group['ring_id'], {})
                ring_id_dict['ring_instance'] = group['ring_instance']

        return ret_dict

# ===========================================
#  * Parser for
#  * show mrp ring <ring-id> statistics all
# ============================================

class ShowMrpRingStatisticsAllSchema(MetaParser):
            """Schema for show mrp ring {ring_id} statistics all"""
            schema = {
                'ring_id': {
                    Any(): {
                        'ring_state': str,
                        'beacon_interval': int,
                        'ports': {
                            Any(): {
                                'interface': str,
                                'beacon_rx': int,
                                'beacon_tx': int,
                                'beacon_drop': int,
                                'nack_rx': int,
                                'nack_tx': int,
                                'nack_drop': int,
                                'propagate_rx': int,
                                'propagate_tx': int,
                                'propagate_drop': int,
                            }
                        },
                        Optional('node_event_statistics'): {
                            Optional('auto_manager_stats'): {
                                Any(): int
                            }
                        }
                    }
                }
            } 

class ShowMrpRingStatisticsAll(ShowMrpRingStatisticsAllSchema):
            """Parser for show mrp ring {ring_id} statistics all"""

            cli_command = 'show mrp ring {ring_id} statistics all'

            def cli(self, ring_id, output = None):
                if output is None:
                    output = self.device.execute(self.cli_command.format(ring_id = ring_id))

                ret_dict = {}
                port = None
                mrp_ring_dict = None
                auto_mgr_stats = None

                # MRP Ring 20 Beacon statistics
                p1 = re.compile(r"^MRP Ring (?P<ring_id>\d+) Beacon statistics$")
                # Ring state     : OPEN
                p2 = re.compile(r"^Ring state\s*:\s*(?P<ring_state>\S+)$")
                # Beacon Interval: 20
                p3 = re.compile(r"^Beacon Interval\s*:\s*(?P<beacon_interval>\d+)$")
                # Port-1 GigabitEthernet1/0/7 statistics:
                p4 = re.compile(r"^Port-(?P<port_num>\d+)\s+(?P<interface>\S+)\s+statistics:$")
                # Beacon RX      : 0
                p5 = re.compile(r"^Beacon RX\s*:\s*(?P<beacon_rx>\d+)$")
                # Beacon TX      : 0
                p6 = re.compile(r"^Beacon TX\s*:\s*(?P<beacon_tx>\d+)$")
                # Beacon Drop    : 0
                p7 = re.compile(r"^Beacon Drop\s*:\s*(?P<beacon_drop>\d+)$")
                # NAck RX        : 0
                p8 = re.compile(r"^NAck RX\s*:\s*(?P<nack_rx>\d+)$")
                # NAck TX        : 0
                p9 = re.compile(r"^NAck TX\s*:\s*(?P<nack_tx>\d+)$")
                # NAck Drop      : 0
                p10 = re.compile(r"^NAck Drop\s*:\s*(?P<nack_drop>\d+)$")
                # Propagate RX   : 0
                p11 = re.compile(r"^Propagate RX\s*:\s*(?P<propagate_rx>\d+)$")
                # Propagate TX   : 0
                p12 = re.compile(r"^Propagate TX\s*:\s*(?P<propagate_tx>\d+)$")
                # Propagate Drop : 0
                p13 = re.compile(r"^Propagate Drop\s*:\s*(?P<propagate_drop>\d+)$")
                # MRP Node event Statistics for Ring 20 :
                p14 = re.compile(r"^MRP Node event Statistics for Ring (?P<ring_id>\d+) :$")
                # MRP Auto Manager stats: Events -----------------------------
                p15 = re.compile(r"^MRP Auto Manager stats: Events")
                # auto_manager_conf_notif_events      = 1
                p16 = re.compile(r"^(?P<event_name>\w[\w\d_]+)\s*=\s*(?P<event_value>\d+)$")

                for line in output.splitlines():
                    line = line.strip()
                    if not line:
                        continue

                    # MRP Ring 20 Beacon statistics
                    m = p1.match(line)
                    if m:
                        ring_id_val = int(m.group('ring_id'))
                        mrp_rings = ret_dict.setdefault('ring_id', {})
                        mrp_ring_dict = mrp_rings.setdefault(ring_id_val, {})
                        continue

                    # Ring state     : OPEN
                    m = p2.match(line)
                    if m and mrp_ring_dict is not None:
                        mrp_ring_dict['ring_state'] = m.group('ring_state')
                        continue

                    # Beacon Interval: 20
                    m = p3.match(line)
                    if m and mrp_ring_dict is not None:
                        mrp_ring_dict['beacon_interval'] = int(m.group('beacon_interval'))
                        continue
                    
                    # Port-1 GigabitEthernet1/0/7 statistics:
                    m = p4.match(line)
                    if m and mrp_ring_dict is not None:
                        port_num = int(m.group('port_num'))
                        interface = m.group('interface')
                        ports = mrp_ring_dict.setdefault('ports', {})
                        port = ports.setdefault(port_num, {})
                        port['interface'] = Common.convert_intf_name(interface)
                        continue

                    # Beacon RX      : 0
                    m = p5.match(line)
                    if m and port is not None:
                        port['beacon_rx'] = int(m.group('beacon_rx'))
                        continue

                    # Beacon TX      : 0
                    m = p6.match(line)
                    if m and port is not None:
                        port['beacon_tx'] = int(m.group('beacon_tx'))
                        continue

                    # Beacon Drop    : 0
                    m = p7.match(line)
                    if m and port is not None:
                        port['beacon_drop'] = int(m.group('beacon_drop'))
                        continue

                    # NAck RX        : 0
                    m = p8.match(line)
                    if m and port is not None:
                        port['nack_rx'] = int(m.group('nack_rx'))
                        continue

                    # NAck TX        : 0
                    m = p9.match(line)
                    if m and port is not None:
                        port['nack_tx'] = int(m.group('nack_tx'))
                        continue

                    # NAck Drop      : 0
                    m = p10.match(line)
                    if m and port is not None:
                        port['nack_drop'] = int(m.group('nack_drop'))
                        continue

                    # Propagate RX   : 0
                    m = p11.match(line)
                    if m and port is not None:
                        port['propagate_rx'] = int(m.group('propagate_rx'))
                        continue
                    
                    # Propagate TX   : 0
                    m = p12.match(line)
                    if m and port is not None:
                        port['propagate_tx'] = int(m.group('propagate_tx'))
                        continue
                    
                    # Propagate Drop : 0
                    m = p13.match(line)
                    if m and port is not None:
                        port['propagate_drop'] = int(m.group('propagate_drop'))
                        continue

                    # MRP Node event Statistics for Ring 20 :
                    m = p14.match(line)
                    if m and mrp_ring_dict is not None:
                        node_stats = mrp_ring_dict.setdefault('node_event_statistics', {})
                        continue
                    
                    # MRP Auto Manager stats: Events -----------------------------
                    m = p15.match(line)
                    if m and mrp_ring_dict is not None:
                        node_stats = mrp_ring_dict.setdefault('node_event_statistics', {})
                        auto_mgr_stats = node_stats.setdefault('auto_manager_stats', {})
                        continue

                    # auto_manager_conf_notif_events      = 1
                    m = p16.match(line)
                    if m and auto_mgr_stats is not None:
                        event_name = m.group('event_name')
                        event_value = int(m.group('event_value'))
                        auto_mgr_stats[event_name] = event_value
                        continue

                return ret_dict
            