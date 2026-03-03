'''   show_hsr.py

IOSXE parsers for the following show commands:

    *'show hsr ring detail
    show platform fpga-profile active
    show hsr ring vlan-filter-drop-count
    show hsr ring multicast-filter-drop
    show hsr ring allowed-vlan
    show hsr ring multicast-filter'

'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowHsrRingDetailSchema(MetaParser):
    """ Schema for show hsr ring detail """
    schema = {
        'hsr_ring': {
            Any(): {
                'layer_type': str,
                'operation_mode': str,
                'ports': str,
                'maxports': str,
                'port_state': str,
                'protocol': str,
                'redbox_mode': str,
                'ports_in_ring': {
                    Any(): {
                        'logical_slot_port': str,
                        'port_state': str,
                        'protocol': str,
                    }
                },
                'ring_parameters': {
                    'redbox_macaddr': str,
                    'node_forget_time': str,
                    'node_reboot_interval': str,
                    'entry_forget_time': str,
                    'proxy_node_forget_time': str,
                    'supervision_frame_cos_option': str,
                    'supervision_frame_cfi_option': str,
                    'supervision_vlan_tag_option': str,
                    'supervision_frame_macda': str,
                    'supervision_frame_vlan_id': str,
                    'supervision_frame_time': str,
                    'life_check_interval': str,
                    'pause_time': str,
                    'fpgamode_dualuplinkenhancement': str,
                }
            }
        }
    }
            
class ShowHsrRingDetail(ShowHsrRingDetailSchema):
    """ Parser for show hsr ring detail """
    cli_command = ['show hsr ring detail']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        parsed_dict = {}
        ring_dict = {}

        # HSR-ring: HS1
        p1 = re.compile(r'HSR-ring:\s(?P<hsr_ring_id>HS\d+)')

        # Layer type = L2
        p2 = re.compile(r'Layer\s*type\s*=\s*(?P<layer_type>\w+)')

        # Operation Mode = mode-H
        p3 = re.compile(r'Operation\s*Mode\s*=\s*(?P<operation_mode>\S+)')

        # Ports: 2\s*Maxports = 2
        p4 = re.compile(r'Ports:\s*(?P<ports>\d+)\s*Maxports\s*=\s*(?P<maxports>\d+)')

        # Port state = hsr-ring is In use
        p5 = re.compile(r'Port\s*state\s*=\s*hsr-ring\s*is\s*(?P<port_state>\S+)')

        # Protocol = Disabled  Redbox Mode = hsr-hsr
        p6 = re.compile(r'Protocol\s*=\s*(?P<protocol>\S+)\s*Redbox\s*Mode\s*=\s*(?P<redbox_mode>\S+)')

        # 1) Port: Gi1/4
        p7 = re.compile(r'\d+\)\s*Port:\s*(?P<port>\S+)')

        # Logical slot/port = 1/4\s*Port state = Not-In use (link down)
        p8 = re.compile(r'Logical\s*slot\/port\s*=\s*(?P<logical_slot_port>\S+)\s*Port\s*state\s*=\s*(?P<port_state>\S+)')

        # Protocol = Disabled
        p9 = re.compile(r'Protocol\s*=\s*(?P<protocol>\S+)')

        # Ring Parameters:
        p10 = re.compile(r'Ring\s*Parameters:')

        # Redbox MacAddr: 0000.0000.0000
        p11 = re.compile(r'Redbox\s*MacAddr:\s*(?P<redbox_macaddr>\S+)')

        # Node Forget Time: 60000 ms
        p12 = re.compile(r'Node\s*Forget\s*Time:\s*(?P<node_forget_time>.+)$')

        # Node Reboot Interval: 60000 ms
        p13 = re.compile(r'Node\s*Reboot\s*Interval:\s*(?P<node_reboot_interval>.+)$')

        # Entry Forget Time: 60000 ms
        p14 = re.compile(r'Entry\s*Forget\s*Time:\s*(?P<entry_forget_time>.+)$')

        # Proxy Node Forget Time: 60000 ms
        p15 = re.compile(r'Proxy\s*Node\s*Forget\s*Time:\s*(?P<proxy_node_forget_time>.+)$')

        # Supervision Frame COS Option: 0
        p16 = re.compile(r'Supervision\s*Frame\s*COS\s*option:\s*(?P<supervision_frame_cos_option>\S+)')

        # Supervision Frame CFI Option: 0
        p17 = re.compile(r'Supervision\s*Frame\s*CFI\s*option:\s*(?P<supervision_frame_cfi_option>\S+)')

        # Supervision Frame VLAN Tag Option: Disabled
        p18 = re.compile(r'Supervision\s*Frame\s*VLAN\s*Tag\s*option:\s*(?P<supervision_vlan_tag_option>\S+)')

        # Supervision Frame MACDA: 0x00
        p19 = re.compile(r'Supervision\s*Frame\s*MacDa:\s*(?P<supervision_frame_macda>\S+)')

        # Supervision Frame VLAN id: 0
        p20 = re.compile(r'Supervision\s*Frame\s*VLAN\s*id:\s*(?P<supervision_frame_vlan_id>\S+)')

        # Supervision Frame Time: 0
        p21 = re.compile(r'Supervision\s*Frame\s*Time:\s*(?P<supervision_frame_time>.+)$')

        # Life Check Interval: 0
        p22 = re.compile(r'Life\s*Check\s*Interval:\s*(?P<life_check_interval>.+)$')

        # Pause Time: 0
        p23 = re.compile(r'Pause\s*Time:\s*(?P<pause_time>.+)$')

        # fpgamode-DualUplinkEnhancement: Enabled
        p24 = re.compile(r'fpgamode-DualUplinkEnhancement:\s*(?P<fpgamode_dualuplinkenhancement>\S+)')

        for line in out.splitlines():
            line = line.strip()

            # HSR-ring: HS1
            m = p1.match(line)
            if m:
                hsr_ring_id = m.group('hsr_ring_id')
                ring_dict = parsed_dict.setdefault('hsr_ring', {}).setdefault(hsr_ring_id, {})
                continue

            # Layer type = L2
            m = p2.match(line)
            if m:
                ring_dict['layer_type'] = m.group('layer_type')
                continue

            # Operation Mode = mode-H
            m = p3.match(line)
            if m:
                ring_dict['operation_mode'] = m.group('operation_mode')
                continue

            # Ports: 2\s*Maxports = 2
            m = p4.match(line)
            if m:
                ring_dict['ports'] = m.group('ports')
                ring_dict['maxports'] = m.group('maxports')
                continue

            # Port state = hsr-ring is In use
            m = p5.match(line)
            if m:
                ring_dict['port_state'] = m.group('port_state')
                continue

            # Protocol = Disabled  Redbox Mode = hsr-hsr
            m = p6.match(line)
            if m:
                ring_dict['protocol'] = m.group('protocol')
                ring_dict['redbox_mode'] = m.group('redbox_mode')
                continue

            # 1) Port: Gi1/4
            m = p7.match(line)
            if m:
                port_id = m.group('port')
                port_dict = ring_dict.setdefault('ports_in_ring', {}).setdefault(port_id, {})
                continue

            # Logical slot/port = 1/4\s*Port state = Not-In use (link down)
            m = p8.match(line)
            if m:
                port_dict['logical_slot_port'] = m.group('logical_slot_port')
                port_dict['port_state'] = m.group('port_state')
                continue

            # Protocol = Disabled
            m = p9.match(line)
            if m:
                port_dict['protocol'] = m.group('protocol')
                continue

            # Ring Parameters:
            m = p10.match(line)
            if m:
                param_dict = ring_dict.setdefault('ring_parameters', {})
                continue

            # Redbox MacAddr: 0000.0000.0000
            m = p11.match(line)
            if m:
                param_dict['redbox_macaddr'] = m.group('redbox_macaddr')
                continue

            # Node Forget Time: 60000 ms
            m = p12.match(line)
            if m:
                param_dict['node_forget_time'] = m.group('node_forget_time')
                continue

            # Node Reboot Interval: 60000 ms
            m = p13.match(line)
            if m:
                param_dict['node_reboot_interval'] = m.group('node_reboot_interval')
                continue

            # Entry Forget Time: 60000 ms
            m = p14.match(line)
            if m:
                param_dict['entry_forget_time'] = m.group('entry_forget_time')
                continue

            # Proxy Node Forget Time: 60000 ms
            m = p15.match(line)
            if m:
                param_dict['proxy_node_forget_time'] = m.group('proxy_node_forget_time')
                continue

            # Supervision Frame COS Option: 0
            m = p16.match(line)
            if m:
                param_dict['supervision_frame_cos_option'] = m.group('supervision_frame_cos_option')
                continue

            # Supervision Frame CFI Option: 0
            m = p17.match(line)
            if m:
                param_dict['supervision_frame_cfi_option'] = m.group('supervision_frame_cfi_option')
                continue

            # Supervision Frame VLAN Tag Option: Disabled
            m = p18.match(line)
            if m:
                param_dict['supervision_vlan_tag_option'] = m.group('supervision_vlan_tag_option')
                continue

            # Supervision Frame MACDA: 0x00
            m = p19.match(line)
            if m:
                param_dict['supervision_frame_macda'] = m.group('supervision_frame_macda')
                continue

            # Supervision Frame VLAN id: 0
            m = p20.match(line)
            if m:
                param_dict['supervision_frame_vlan_id'] = m.group('supervision_frame_vlan_id')
                continue

            # Supervision Frame Time: 0
            m = p21.match(line)
            if m:
                param_dict['supervision_frame_time'] = m.group('supervision_frame_time')
                continue

            # Life Check Interval: 0
            m = p22.match(line)
            if m:
                param_dict['life_check_interval'] = m.group('life_check_interval')
                continue

            # Pause Time: 0
            m = p23.match(line)
            if m:
                param_dict['pause_time'] = m.group('pause_time')
                continue

            # fpgamode-DualUplinkEnhancement: Enabled
            m = p24.match(line)
            if m:
                param_dict['fpgamode_dualuplinkenhancement'] = m.group('fpgamode_dualuplinkenhancement')
                continue

        return parsed_dict

# Schema for 'show platform fpga-profile active'
class ShowPlatformFpgaProfileActiveSchema(MetaParser):
    """Schema for show platform fpga-profile active"""
    schema = {
        'active_fpga_profile': str,
        'active_feature_set': str,
        'fpga_profile_upon_reload': str,
        'feature_set_upon_reload': str,
    }

# Parser for 'show platform fpga-profile active'
class ShowPlatformFpgaProfileActive(ShowPlatformFpgaProfileActiveSchema):
    """Parser for show platform fpga-profile active"""

    cli_command = 'show platform fpga-profile active'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # Active FPGA profile : hsr-quadbox
        p1 = re.compile(r'Active\s*FPGA\s*profile\s*:\s*(?P<active_fpga_profile>.+)')
        # Active feature set : HSR-HSR quadbox
        p2 = re.compile(r'Active\s*feature\s*set\s*:\s*(?P<active_feature_set>.+)')
        # FPGA profile upon reload : hsr-quadbox
        p3 = re.compile(r'FPGA\s*profile\s*upon\s*reload\s*:\s*(?P<fpga_profile_upon_reload>.+)')
        # Feature set upon reload : HSR-HSR quadbox
        p4 = re.compile(r'Feature\s*set\s*upon\s*reload\s*:\s*(?P<feature_set_upon_reload>.+)')

        for line in out.splitlines():
            line = line.strip()

            # Active FPGA profile : hsr-quadbox
            m = p1.match(line)
            if m:
                parsed_dict['active_fpga_profile'] = m.group('active_fpga_profile')
                continue

            # Active feature set : HSR-HSR quadbox
            m = p2.match(line)
            if m:
                parsed_dict['active_feature_set'] = m.group('active_feature_set')
                continue

            # FPGA profile upon reload : hsr-quadbox
            m = p3.match(line)
            if m:
                parsed_dict['fpga_profile_upon_reload'] = m.group('fpga_profile_upon_reload')
                continue

            # Feature set upon reload : HSR-HSR quadbox
            m = p4.match(line)
            if m:
                parsed_dict['feature_set_upon_reload'] = m.group('feature_set_upon_reload')
                continue

        return parsed_dict

# Schema for 'show hsr ring vlan-filter-drop-count'
class ShowHsrRingVlanFilterDropCountSchema(MetaParser):
    """Schema for show hsr ring vlan-filter-drop-count"""
    schema = {
        'hsr_ring': {
            Any(): {
                'vlan_filter_drop_count': int
            }
        }
    }

# Parser for 'show hsr ring vlan-filter-drop-count'
class ShowHsrRingVlanFilterDropCount(ShowHsrRingVlanFilterDropCountSchema):
    """Parser for show hsr ring vlan-filter-drop-count"""

    cli_command = 'show hsr ring vlan-filter-drop-count'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # HSR-ring: HS1
        p1 = re.compile(r'^HSR-ring:\s*(?P<hsr_ring>\S+)$')
        # VLAN filter drop count : 0
        p2 = re.compile(r'^VLAN\s*filter\s*drop\s*count\s*:\s*(?P<vlan_filter_drop_count>\d+)$')

        current_ring = None

        for line in out.splitlines():
            line = line.strip()

            # HSR-ring: HS1
            m = p1.match(line)
            if m:
                current_ring = m.group('hsr_ring')
                parsed_dict.setdefault('hsr_ring', {})[current_ring] = {}
                continue

            # VLAN filter drop count : 0
            m = p2.match(line)
            if m and current_ring:
                parsed_dict['hsr_ring'][current_ring]['vlan_filter_drop_count'] = int(m.group('vlan_filter_drop_count'))
                continue

        return parsed_dict

# Schema for 'show hsr ring multicast-filter-drop'
class ShowHsrRingMulticastFilterDropSchema(MetaParser):
    """Schema for show hsr ring multicast-filter-drop"""
    schema = {
        'hsr_ring': {
            Any(): {
                'multicast_filter_drop_count': int
            }
        }
    }

# Parser for 'show hsr ring multicast-filter-drop'
class ShowHsrRingMulticastFilterDrop(ShowHsrRingMulticastFilterDropSchema):
    """Parser for show hsr ring multicast-filter-drop"""

    cli_command = 'show hsr ring multicast-filter-drop'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # HSR-ring: HS1
        p1 = re.compile(r'^HSR-ring:\s*(?P<hsr_ring>\S+)$')
        # Multicast filter drop count : 0
        p2 = re.compile(r'^Multicast\s*filter\s*drop\s*count\s*:\s*(?P<multicast_filter_drop_count>\d+)$')

        current_ring = None

        for line in out.splitlines():
            line = line.strip()

            # HSR-ring: HS1
            m = p1.match(line)
            if m:
                current_ring = m.group('hsr_ring')
                parsed_dict.setdefault('hsr_ring', {})[current_ring] = {}
                continue

            # Multicast filter drop count : 0
            m = p2.match(line)
            if m and current_ring:
                parsed_dict['hsr_ring'][current_ring]['multicast_filter_drop_count'] = int(m.group('multicast_filter_drop_count'))
                continue

        return parsed_dict

# Schema for 'show hsr ring allowed-vlan'
class ShowHsrRingAllowedVlanSchema(MetaParser):
    """Schema for show hsr ring allowed-vlan"""
    schema = {
        'hsr_ring': {
            Any(): {
                'vlan_allowed_list': list
            }
        }
    }

# Parser for 'show hsr ring allowed-vlan'
class ShowHsrRingAllowedVlan(ShowHsrRingAllowedVlanSchema):
    """Parser for show hsr ring allowed-vlan"""

    cli_command = 'show hsr ring allowed-vlan'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # HSR-ring: HS1
        p1 = re.compile(r'^HSR-ring:\s*(?P<hsr_ring>\S+)$')
        # vlan_allowed_list: 1-4094
        p2 = re.compile(r'^(?P<vlan_allowed_list>[\d\-\,]+)$')

        current_ring = None

        for line in out.splitlines():
            line = line.strip()

            # HSR-ring: HS1
            m = p1.match(line)
            if m:
                current_ring = m.group('hsr_ring')
                parsed_dict.setdefault('hsr_ring', {})[current_ring] = {}
                continue

            # 1-10,20,30-40
            m = p2.match(line)
            if m and current_ring:
                vlan_list = m.group('vlan_allowed_list')
                # Split the VLAN list into individual ranges or values
                parsed_dict['hsr_ring'][current_ring]['vlan_allowed_list'] = vlan_list.split(',')
                continue

        return parsed_dict

# Schema for 'show hsr ring multicast-filter'
class ShowHsrRingMulticastFilterSchema(MetaParser):
    """Schema for show hsr ring multicast-filter"""
    schema = {
        'hsr_ring': {
            Any(): {
                'filters': {
                    Any(): {
                        'address': str,
                        'mask': str
                    }
                }
            }
        }
    }

# Parser for 'show hsr ring multicast-filter'
class ShowHsrRingMulticastFilter(ShowHsrRingMulticastFilterSchema):
    """Parser for show hsr ring multicast-filter"""

    cli_command = 'show hsr ring multicast-filter'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # HSR-ring: HS1
        p1 = re.compile(r'^HSR-ring:\s*(?P<hsr_ring>\S+)$')
        # filter_no: 1  address: 0100.5e00.0001  mask: ffff.ffff.ffff
        p2 = re.compile(r'^(?P<filter_no>\d+)\s+(?P<address>[0-9a-fA-F\.]+)\s+(?P<mask>[0-9a-fA-F\.]+)$')

        current_ring = None

        for line in out.splitlines():
            line = line.strip()

            # HSR-ring: HS1
            m = p1.match(line)
            if m:
                current_ring = m.group('hsr_ring')
                parsed_dict.setdefault('hsr_ring', {})[current_ring] = {'filters': {}}
                continue

            # 1 0100.5e00.0001 ffff.ffff.ffff
            m = p2.match(line)
            if m and current_ring:
                filter_no = int(m.group('filter_no'))
                address = m.group('address')
                mask = m.group('mask')
                parsed_dict['hsr_ring'][current_ring]['filters'][filter_no] = {
                    'address': address,
                    'mask': mask
                }
                continue

        return parsed_dict


