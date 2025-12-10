"""show_cef.py

IOSXE parsers for the following show commands:

    * show cef path set id <id> detail | in Replicate oce:
    * show cef uid
    * show cef path sets summary
    * show cef interface <interface>
    * show cef table consistency-check
    * show cef interface {interface_name} policy-statistics {direction}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowCefPathSetIdDetailReplicateOceSchema(MetaParser):
    """Schema for:
        show cef path set id <id> detail | in Replicate oce:
    """
    schema = {
        'replicate_oce': {
             Any():{
                 'uid':int
             },
         },
    }

class ShowCefPathSetIdDetailReplicateOce(ShowCefPathSetIdDetailReplicateOceSchema):
    """Parser for:
        show cef path set id <id> detail | in Replicate oce:
        """
    cli_command = 'show cef path set id {cef_id} detail | in Replicate oce:'

    def cli(self, cef_id='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(cef_id=cef_id))

        ret_dict = {}
        
        ###Replicate oce: 0x7F9E40C59340 UID:6888
        p1=re.compile(r"^Replicate\s+oce:\s+(?P<replicate_oce>\S+)\s+UID:(?P<uid>\S+)$")

        for line in output.splitlines():
            line = line.strip()
            
            ##Replicate oce: 0x7F9E40C59340 UID:6888
            m1=p1.match(line)
            if m1:
                r=m1.groupdict()
                uid_dict=ret_dict.setdefault('replicate_oce',{}).setdefault(r['replicate_oce'],{})
                uid_dict['uid']=int(r['uid'])
        return ret_dict
        
class ShowCefUidSchema(MetaParser):
    """Schema for:
        show cef uid
    """
    schema = {
        'cef_unique_ids': {
            'cef_unique_ids_stats': list,
            'ids_maximum': int,
            'ids_free': int,
            'ids_active': int,
            'ids_pending_to_re_use': int,
            'ids_total_generated': int,
            'ids_total_reserved': int,
            'ids_total_deleted': int,
            'maximum_groups': int,
            'free_groups': int,
            'active_groups': int,
            'client_key': {
                'client_key_nodes': int,
                'uid_table_entries': int,
                'uid_table_config_size': int
            },
        },
    }

class ShowCefUid(ShowCefUidSchema):
    """Parser for:
        show cef uid
        """
    cli_command = 'show cef uid'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
                
        ###CEF Unique IDs Stats: global space
        ###CEF Unique IDs Stats: platform space
        p1=re.compile(r"^CEF\s+Unique\s+IDs\s+Stats:\s+(?P<value>[a-zA-Z ]+)$")
        
        ###CEF UID Client Key Stats
        p2=re.compile(r"CEF\s+UID\s+Client\s+Key\s+Stats")
        
        ##IDs Maximum : 16777216
        p3=re.compile(r"^IDs\s+Maximum\s+:\s+(?P<ids_maximum>\d+)$")

        ##IDs Free : 16777212 
        p4=re.compile(r"^IDs\s+Free\s+:\s+(?P<ids_free>\d+)$")

        ##IDs Active : 4
        p5=re.compile(r"^IDs\s+Active\s+:\s+(?P<ids_active>\d+)$")

        ##IDs Pending re-use TO : 0
        p6=re.compile(r"^IDs\s+Pending\s+re\-use\s+TO\s+:\s+(?P<ids_pending_to_re_use>\d+)$")

        ##IDs Total Generated : 4
        p7=re.compile(r"^IDs\s+Total\s+Generated\s+:\s+(?P<ids_total_generated>\d+)$")

        ##IDs Total Reserved : 0
        p8=re.compile(r"^IDs\s+Total\s+Reserved\s+:\s+(?P<ids_total_reserved>\d+)$")

        ##IDs Total Reserved : 0
        p9=re.compile(r"^IDs\s+Total\s+Deleted\s+:\s+(?P<ids_total_deleted>\d+)$")
        
        ##Groups Maximum : 2048
        p10=re.compile(r"^Groups\s+Maximum\s+:\s+(?P<maximum_groups>\d+)$")

        ##Groups Free : 2047
        p11=re.compile(r"^Groups\s+Free\s+:\s+(?P<free_groups>\d+)$")

        ##Groups Active : 1
        p12=re.compile(r"^Groups\s+Active\s+:\s+(?P<active_groups>\d+)$")

        ##Client Key nodes : 4
        p13=re.compile(r"^Client\s+Key\s+nodes\s+:\s+(?P<client_key_nodes>\d+)$")

        ##UID Table Entries : 4
        p14=re.compile(r"^UID\s+Table\s+Entries\s+:\s+(?P<uid_table_entries>\d+)$")

        ##UID Table config size: 16777216
        p15=re.compile(r"^UID\s+Table\s+config\s+size:\s+(?P<uid_table_config_size>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            
            ##CEF Unique IDs Stats: global space
            m = p1.match(line)
            if m:
                r = m.groupdict()
                cef_ids_dict=ret_dict.setdefault('cef_unique_ids',{})
                ids_stats_list = cef_ids_dict.setdefault('cef_unique_ids_stats', [])
                ids_stats_list.append(r['value'])
                continue
                
            ##CEF UID Client Key Stats
            m = p2.match(line)
            if m:
                client_key_dict=cef_ids_dict.setdefault('client_key',{})
                continue
             
            ##IDs Maximum : 16777216             
            m = p3.match(line)
            if m: 
                cef_ids_dict.update({'ids_maximum':int(m.groupdict()['ids_maximum'])})
                continue

            ##IDs Maximum : 16777216             
            m = p4.match(line)
            if m: 
                cef_ids_dict.update({'ids_free':int(m.groupdict()['ids_free'])})
                continue
                
            ##IDs Active : 4     
            m = p5.match(line)
            if m: 
                cef_ids_dict.update({'ids_active':int(m.groupdict()['ids_active'])})      
                continue

            ##IDs Pending re-use TO : 0 
            m = p6.match(line)
            if m: 
                cef_ids_dict.update({'ids_pending_to_re_use':int(m.groupdict()['ids_pending_to_re_use'])})
                continue
                
            ##IDs Total Generated : 4
            m = p7.match(line)
            if m: 
                cef_ids_dict.update({'ids_total_generated':int(m.groupdict()['ids_total_generated'])})
                continue

            ##IDs Total Generated : 4
            m = p8.match(line)
            if m: 
                cef_ids_dict.update({'ids_total_reserved':int(m.groupdict()['ids_total_reserved'])})
                continue
                
            ##IDs Total Deleted : 0
            m = p9.match(line)
            if m: 
                cef_ids_dict.update({'ids_total_deleted':int(m.groupdict()['ids_total_deleted'])})
                continue
       
            ##Groups Maximum : 2048
            m = p10.match(line)
            if m: 
                cef_ids_dict.update({'maximum_groups':int(m.groupdict()['maximum_groups'])}) 
                continue
   
            ##Groups Maximum : 2048
            m = p11.match(line)
            if m: 
                cef_ids_dict.update({'free_groups':int(m.groupdict()['free_groups'])})
                continue   
                
            ##Groups Active : 1
            m = p12.match(line)
            if m: 
                cef_ids_dict.update({'active_groups':int(m.groupdict()['active_groups'])})
                continue  

            ##Client Key nodes : 4
            m = p13.match(line)
            if m: 
                client_key_dict.update({'client_key_nodes':int(m.groupdict()['client_key_nodes'])})
                continue  

            ##UID Table Entries : 4
            m = p14.match(line)
            if m: 
                client_key_dict.update({'uid_table_entries':int(m.groupdict()['uid_table_entries'])}) 
                continue  

            ##UID Table config size
            m = p15.match(line)
            if m: 
                client_key_dict.update({'uid_table_config_size':int(m.groupdict()['uid_table_config_size'])})
                continue  
                
        return ret_dict

class ShowCefPathSetsSummarySchema(MetaParser):
    """Schema for:
        show cef path sets summary
    """
    schema = {
        'path_set_id': {
            Any():{
                'path_num': int,
            },
        },
    }

class ShowCefPathSetsSummary(ShowCefPathSetsSummarySchema):
    """Parser for:
        show cef path sets summary
        """
    cli_command = 'show cef path sets summary'

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        ##Path Set Id 0x00000002   Num Paths 1
        p1=re.compile(r"^Path\s+Set\s+Id\s+(?P<path_set_id>\S+)\s+Num\s+Paths\s+(?P<path_num>\d+)$")
        
        for line in output.splitlines():
            line=line.strip()
            m=p1.match(line)
            if m:
                r=m.groupdict()
                path_set_dict=ret_dict.setdefault('path_set_id',{}).setdefault(r['path_set_id'],{})
                path_set_dict['path_num']=int(r['path_num'])
            continue
            
        return ret_dict

# ==============================================
#  Schema for show cef interface policy-statistics
# ==============================================
class ShowCefInterfacePolicyStatisticsSchema(MetaParser):
    """Schema for show cef interface policy-statistics"""
    """Schema for show cef interface {interface_name} policy-statistics {direction}"""

    schema = {
        'interfaces': {
            Any(): {
                'status': str,
                'if_number': int,
                Optional('corr_hwidb_fast_if_number'): int,
                Optional('corr_hwidb_firstsw_if_number'): int,
                Optional('policy_accounting_status'): str,
                Optional('direction'): str,
                Optional('policy_statistics'): {
                    Any(): {  # Index number
                        'packets': int,
                        'bytes': int,
                    }
                }
            }
        }
    }

# ==============================================
#  Parser for show cef interface policy-statistics
# ==============================================
class ShowCefInterfacePolicyStatistics(ShowCefInterfacePolicyStatisticsSchema):
    """Parser for show cef interface policy-statistics"""
    """Parser for show cef interface {interface_name} policy-statistics {direction}"""

    cli_command = ['show cef interface policy-statistics',
                   'show cef interface {interface_name} policy-statistics {direction}']

    def cli(self, interface_name="", direction="", output=None):
        if output is None:
            if interface_name and direction:
                cmd = self.cli_command[1].format(interface_name=interface_name, direction=direction)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}

        # GigabitEthernet0/0/2 is up (if_number 10)
        p1 = re.compile(r'^(?P<interface>\S+)\s+is\s+(?P<status>\w+)\s+\(if_number\s+(?P<if_number>\d+)\)$')

        # Corresponding hwidb fast_if_number 10
        p2 = re.compile(r'^Corresponding\s+hwidb\s+fast_if_number\s+(?P<fast_if_number>\d+)$')

        # Corresponding hwidb firstsw->if_number 10
        p3 = re.compile(r'^Corresponding\s+hwidb\s+firstsw->if_number\s+(?P<firstsw_if_number>\d+)$')

        # BGP based Policy accounting on output is enabled
        p4 = re.compile(r'^(?P<policy_type>[\w\s]+)\s+Policy\s+accounting\s+on\s+(?P<direction>\w+)\s+is\s+(?P<status>\w+)$')

        # Index         Packets           Bytes
        p5 = re.compile(r'^Index\s+Packets\s+Bytes$')

        # 1              10            1000
        p6 = re.compile(r'^(?P<index>\d+)\s+(?P<packets>\d+)\s+(?P<bytes>\d+)$')

        current_interface = None

        for line in output.splitlines():
            line = line.strip()

            if not line:
                continue

            # GigabitEthernet0/0/2 is up (if_number 10)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name = group['interface']
                current_interface = interface_name

                interface_dict = ret_dict.setdefault('interfaces', {})
                intf_dict = interface_dict.setdefault(interface_name, {})

                intf_dict['status'] = group['status']
                intf_dict['if_number'] = int(group['if_number'])
                continue

            # Corresponding hwidb fast_if_number 10
            m = p2.match(line)
            if m and current_interface:
                group = m.groupdict()
                interface_dict = ret_dict['interfaces'][current_interface]
                interface_dict['corr_hwidb_fast_if_number'] = int(group['fast_if_number'])
                continue

            # Corresponding hwidb firstsw->if_number 10
            m = p3.match(line)
            if m and current_interface:
                group = m.groupdict()
                interface_dict = ret_dict['interfaces'][current_interface]
                interface_dict['corr_hwidb_firstsw_if_number'] = int(group['firstsw_if_number'])
                continue

            # BGP based Policy accounting on output is enabled
            m = p4.match(line)
            if m and current_interface:
                group = m.groupdict()
                interface_dict = ret_dict['interfaces'][current_interface]
                interface_dict['policy_accounting_status'] = f"{group['policy_type']} Policy accounting on {group['direction']} is {group['status']}"
                interface_dict['direction'] = group['direction']
                continue

            # Skip header line
            m = p5.match(line)
            if m:
                continue

            # Statistics entries
            m = p6.match(line)
            if m and current_interface:
                group = m.groupdict()
                interface_dict = ret_dict['interfaces'][current_interface]

                # Initialize policy_statistics if not already present
                if 'policy_statistics' not in interface_dict:
                    interface_dict['policy_statistics'] = {}

                stats_dict = interface_dict['policy_statistics']
                index = group['index']
                stats_dict[index] = {
                    'packets': int(group['packets']),
                    'bytes': int(group['bytes'])
                }
                continue

        return ret_dict

class ShowCefInterfaceSchema(MetaParser):
    '''Schema for show cef interface {interface}'''
    schema = {
        'interface': {
            Any(): {
                'state': str,
                'if_number': int,
                'fast_if_number': int,
                'firstsw_if_number': int,
                Optional('internet_address'): str,
                'hardware_idb': str,
                'fast_switching_type': int,
                'interface_type': int,
                'cef_switching': str,
                Optional('vpn_forwarding_table'): str,
                'input_fast_flags': str,
                'output_fast_flags': str,
                'ifindex': str,
                'slot': int,
                'slot_unit': int,
                'mtu': int
            }
        }
    }

class ShowCefInterface(ShowCefInterfaceSchema):
    '''Parser for show cef interface {interface}'''

    cli_command = 'show cef interface {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))
        
        # GigabitEthernet1/0/5 is down (if_number 13)
        p1 = re.compile(r'^(?P<interface>\S+)\s+is\s+(?P<state>\w+)\s+\(if_number\s+(?P<if_number>\d+)\)$')

        # Corresponding hwidb fast_if_number 13
        p2 = re.compile(r'^Corresponding hwidb fast_if_number (?P<fast_if_number>\d+)$')

        # Corresponding hwidb firstsw->if_number 13
        p3 = re.compile(r'^Corresponding hwidb firstsw->if_number (?P<firstsw_if_number>\d+)$')

        # Internet address is 192.168.0.131/24
        p4 = re.compile(r'^Internet address is (?P<internet_address>\S+)$')

        # Hardware idb is GigabitEthernet1/0/5
        p5 = re.compile(r'^Hardware idb is (?P<hardware_idb>\S+)$')

        # Fast switching type 1, interface type 146
        p6 = re.compile(r'^Fast switching type (?P<fast_switching_type>\d+), interface type (?P<interface_type>\d+)$')

        # IP CEF switching disabled
        p7 = re.compile(r'^IP CEF switching (?P<cef_switching>\w+)$')

        # VPN Forwarding table "Mgmt-vrf"
        p8 = re.compile(r'^VPN Forwarding table\s+\"(?P<vpn_forwarding_table>\S+)\"$')

        # Input fast flags 0x0, Output fast flags 0x0
        p9 = re.compile(r'^Input fast flags (?P<input_fast_flags>\S+), Output fast flags (?P<output_fast_flags>\S+)$')

        # ifindex 12(12)
        p10 = re.compile(r'^ifindex (?P<ifindex>\S+)$')

        # Slot 1 (1) Slot unit 5 VC -1
        p11 = re.compile(r'^Slot\s+(?P<slot>\d+)\s+\(\d+\)\s+Slot\s+unit\s+(?P<slot_unit>\d+)\s+VC\s+-\d+$')

        # IP MTU 0
        p12 = re.compile(r'^IP MTU\s+(?P<mtu>\d+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # GigabitEthernet1/0/5 is down (if_number 13)
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(m.groupdict()['interface'], {})
                int_dict['state'] = m.groupdict()['state']
                int_dict['if_number'] = int(m.groupdict()['if_number'])
                continue

            # Corresponding hwidb fast_if_number 13
            m = p2.match(line)
            if m:
                int_dict['fast_if_number'] = int(m.groupdict()['fast_if_number'])
                continue

            # Corresponding hwidb firstsw->if_number 13
            m = p3.match(line)
            if m:
                int_dict['firstsw_if_number'] = int(m.groupdict()['firstsw_if_number'])
                continue

            # Internet address is 192.168.0.131/24
            m = p4.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Hardware idb is GigabitEthernet1/0/5
            m = p5.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Fast switching type 1, interface type 146
            m = p6.match(line)
            if m:
                int_dict['fast_switching_type'] = int(m.groupdict()['fast_switching_type'])
                int_dict['interface_type'] = int(m.groupdict()['interface_type'])
                continue

            # IP CEF switching disabled
            m = p7.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # VPN Forwarding table "Mgmt-vrf"
            m = p8.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Input fast flags 0x0, Output fast flags 0x0
            m = p9.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # ifindex 12(12)
            m = p10.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Slot 1 (1) Slot unit 5 VC -1
            m = p11.match(line)
            if m:
                int_dict['slot'] = int(m.groupdict()['slot'])
                int_dict['slot_unit'] = int(m.groupdict()['slot_unit'])
                continue

            # IP MTU 0
            m = p12.match(line)
            if m:
                int_dict['mtu'] = int(m.groupdict()['mtu'])
                continue
        
        return ret_dict

class ShowCefInterfaceInternalSchema(MetaParser):
    '''Schema for show cef interface {interface} internal'''
    schema = {
        'interface': {
            Any(): {
                'state': str,
                'if_number': int,
                'fast_if_number': int,
                'firstsw_if_number': int,
                Optional('internet_address'): str,
                'hardware_idb': str,
                'fast_switching_type': int,
                'interface_type': int,
                'cef_switching': str,
                Optional('vpn_forwarding_table'): str,
                'input_fast_flags': str,
                'output_fast_flags': str,
                'ifindex': str,
                'slot': int,
                'slot_unit': int,
                'mtu': int,
                Optional('input_features'): str,
                'suppressed_input_features': str,
                'flags': str,
                'hardware_flags': str,
                'vrf': str,
                'status_flags':{
                    'hwidb': str,
                    'fibhwidb': str
                },
                'subblocks':{
                    Optional('ipv4'): {
                        Optional('address'): str,
                        Optional('broadcast_address'): str,
                        Optional('mtu'): int,
                        Optional('discarded_packets'): int
                    },
                    Optional('ipv6'): {
                        Optional('discarded_packets'): int
                    }
                },
                Optional('ip_unicast_rpf_check'): bool,
            }
        }
    }

class ShowCefInterfaceInternal(ShowCefInterfaceInternalSchema):
    '''Parser for show cef interface {interface} internal'''

    cli_command = 'show cef interface {interface} internal'

    def cli(self, interface=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))
        
        # GigabitEthernet0/0 is up (if_number 6) ['2]
        p1 = re.compile(r'^(?P<interface>\S+)\s+is\s+(?P<state>\w+)\s+\(if_number\s+(?P<if_number>\d+)\).+$')

        # Corresponding hwidb fast_if_number 13
        p2 = re.compile(r'^Corresponding hwidb fast_if_number (?P<fast_if_number>\d+)$')

        # Corresponding hwidb firstsw->if_number 13
        p3 = re.compile(r'^Corresponding hwidb firstsw->if_number (?P<firstsw_if_number>\d+)$')

        # Internet address is 192.168.0.131/24
        p4 = re.compile(r'^Internet address is (?P<internet_address>\S+)$')

        # Hardware idb is GigabitEthernet1/0/5
        p5 = re.compile(r'^Hardware idb is (?P<hardware_idb>\S+)$')

        # Fast switching type 1, interface type 146
        p6 = re.compile(r'^Fast switching type (?P<fast_switching_type>\d+), interface type (?P<interface_type>\d+)$')

        # IP CEF switching disabled
        p7 = re.compile(r'^IP CEF switching (?P<cef_switching>\w+)$')

        # VPN Forwarding table "Mgmt-vrf"
        p8 = re.compile(r'^VPN Forwarding table\s+\"(?P<vpn_forwarding_table>\S+)\"$')

        # Input fast flags 0x0, Output fast flags 0x0
        p9 = re.compile(r'^Input fast flags (?P<input_fast_flags>\S+), Output fast flags (?P<output_fast_flags>\S+)$')

        # ifindex 158(158) ['2]
        p10 = re.compile(r'^ifindex (?P<ifindex>\S+)\s+.+$')

        # Slot 1 (1) Slot unit 5 VC -1
        p11 = re.compile(r'^Slot\s+(?P<slot>\d+)\s+\(\d+\)\s+Slot\s+unit\s+(?P<slot_unit>\d+)\s+VC\s+-\d+$')

        # IP MTU 0
        p12 = re.compile(r'^IP MTU\s+(?P<mtu>\d+)$')

        # Input features: IP not enabled discard
        p13 = re.compile(r'^Input features:\s+(?P<input_features>.+)$')

        # Suppressed input features: MCI Check
        p14 = re.compile(r'^Suppressed input features:\s+(?P<suppressed_input_features>.+)$')

        # Flags 0x26000, hardware flags 0x5
        p15 = re.compile(r'^Flags\s+(?P<flags>\S+), hardware flags\s+(?P<hardware_flags>\S+)$')

        # VRF: Mgmt-vrf(1)
        p16 = re.compile(r'^VRF:\s+(?P<vrf>.+)$')

        # hwidb    status 210040 status2 200010 status3 0 status4 22
        p17 = re.compile(r'^hwidb\s+(?P<hwidb>.+)$')

        # fibhwidb status 210040 status2 200010 status3 0 status4 22
        p18 = re.compile(r'^fibhwidb\s+(?P<fibhwidb>.+)$')

        # IPv4: Internet address is 192.168.0.131/24
        p19 = re.compile(r'^IPv4: Internet address is\s+(?P<address>\S+)$')

        # Broadcast address 255.255.255.255
        p20 = re.compile(r'^Broadcast address\s+(?P<broadcast_address>[\d\.]+)$')

        # Protocol discard for IPv4 - discarded packets: 0
        # Protocol discard for IPv6 - discarded packets: 0
        p21 = re.compile(r'^Protocol discard for\s+(?P<protocol>(IPv4|IPv6))\s+- discarded packets:\s+(?P<discarded_packets>\d+)$')

        # IP unicast RPF check is enabled
        p22 = re.compile(r'^IP unicast RPF check is enabled$')

        ret_dict = dict()
        subblock_flag = False

        for line in output.splitlines():
            line = line.strip()

            # GigabitEthernet0/0 is up (if_number 6) ['2]
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(m.groupdict()['interface'], {})
                int_dict['state'] = m.groupdict()['state']
                int_dict['if_number'] = int(m.groupdict()['if_number'])
                continue

            # Corresponding hwidb fast_if_number 13
            m = p2.match(line)
            if m:
                int_dict['fast_if_number'] = int(m.groupdict()['fast_if_number'])
                continue

            # Corresponding hwidb firstsw->if_number 13
            m = p3.match(line)
            if m:
                int_dict['firstsw_if_number'] = int(m.groupdict()['firstsw_if_number'])
                continue

            # Internet address is 192.168.0.131/24
            m = p4.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Hardware idb is GigabitEthernet1/0/5
            m = p5.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Fast switching type 1, interface type 146
            m = p6.match(line)
            if m:
                int_dict['fast_switching_type'] = int(m.groupdict()['fast_switching_type'])
                int_dict['interface_type'] = int(m.groupdict()['interface_type'])
                continue

            # IP CEF switching disabled
            m = p7.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # VPN Forwarding table "Mgmt-vrf"
            m = p8.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Input fast flags 0x0, Output fast flags 0x0
            m = p9.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # ifindex 158(158) ['2]
            m = p10.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Slot 1 (1) Slot unit 5 VC -1
            m = p11.match(line)
            if m:
                int_dict['slot'] = int(m.groupdict()['slot'])
                int_dict['slot_unit'] = int(m.groupdict()['slot_unit'])
                continue

            # IP MTU 0
            m = p12.match(line)
            if m:
                if not subblock_flag:
                    int_dict['mtu'] = int(m.groupdict()['mtu'])
                else:
                    ip4_block_dict['mtu'] = int(m.groupdict()['mtu'])
                continue

            # Input features: IP not enabled discard
            m = p13.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue
            
            # Suppressed input features: MCI Check
            m = p14.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # Flags 0x26000, hardware flags 0x5
            m = p15.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # VRF: Mgmt-vrf(1)
            m = p16.match(line)
            if m:
                int_dict.update(m.groupdict())
                continue

            # hwidb    status 210040 status2 200010 status3 0 status4 22
            m = p17.match(line)
            if m:
                st_flg_dict = int_dict.setdefault('status_flags', {})
                st_flg_dict.update(m.groupdict())
                continue

            # fibhwidb status 210040 status2 200010 status3 0 status4 22
            m = p18.match(line)
            if m:
                st_flg_dict.update(m.groupdict())
                continue

            # IPv4: Internet address is 192.168.0.131/24
            m = p19.match(line)
            if m:
                subblock_flag = True
                ip4_block_dict = int_dict.setdefault('subblocks', {}).setdefault('ipv4', {})
                ip4_block_dict.update(m.groupdict())
                continue

            # Broadcast address 255.255.255.255
            m = p20.match(line)
            if m:
                ip4_block_dict.update(m.groupdict())
                continue

            # Protocol discard for IPv4 - discarded packets: 0
            # Protocol discard for IPv6 - discarded packets: 0
            m = p21.match(line)
            if m:
                block_dict = int_dict.setdefault('subblocks', {}).setdefault(
                    'ipv4' if 'IPv4' in m.groupdict()['protocol'] else 'ipv6', {}
                )
                block_dict['discarded_packets'] = int(m.groupdict()['discarded_packets'])
                continue

            # IP unicast RPF check is enabled
            m = p22.match(line)
            if m:
                int_dict.update({'ip_unicast_rpf_check': True})
                continue

        return ret_dict


# ======================================
# Schema for:
#   * 'show cef table consistency-check'
# ======================================
class ShowCefTableConsistencyCheckSchema(MetaParser):

    """ Schema for:
        * 'show cef table consistency-check'
    """

    schema = {
        'consistency_checker_master_control': str,
        Optional('ipv4'): {
            'table_consistency_checker_state': {
                Any(): {
                    'status': str,
                    Optional('prefixes_checked'): int,
                    Optional('check_interval'): int,
                    'queries_sent': int,
                    'queries_ignored': int,
                    'queries_checked': int,
                    'queries_iterated': int,
                }
            },
            'checksum_data_checking': str,
            'inconsistency_error_messages': str,
            'inconsistency_auto_repair': str,
            Optional('auto_repair_delay'): int,
            Optional('auto_repair_holddown'): int,
            'inconsistency_auto_repair_runs': int,
            'inconsistency_statistics_confirmed': int,
            'inconsistency_statistics_recorded': str,
        },
        Optional('ipv6'): {
            'table_consistency_checker_state': {
                Any(): {
                    'status': str,
                    Optional('prefixes_checked'): int,
                    Optional('check_interval'): int,
                    'queries_sent': int,
                    'queries_ignored': int,
                    'queries_checked': int,
                    'queries_iterated': int,
                }
            },
            'checksum_data_checking': str,
            'inconsistency_error_messages': str,
            'inconsistency_auto_repair': str,
            Optional('auto_repair_delay'): int,
            Optional('auto_repair_holddown'): int,
            'inconsistency_auto_repair_runs': int,
            'inconsistency_statistics_confirmed': int,
            'inconsistency_statistics_recorded': str,
        },
        Optional('binding_label'): {
            'table_consistency_checker_state': {
                Any(): {
                    'status': str,
                    Optional('prefixes_checked'): int,
                    Optional('check_interval'): int,
                    'queries_sent': int,
                    'queries_ignored': int,
                    'queries_checked': int,
                    'queries_iterated': int,
                }
            },
            'checksum_data_checking': str,
            'inconsistency_error_messages': str,
            'inconsistency_auto_repair': str,
            Optional('auto_repair_delay'): int,
            Optional('auto_repair_holddown'): int,
            'inconsistency_auto_repair_runs': int,
            'inconsistency_statistics_confirmed': int,
            'inconsistency_statistics_recorded': str,
        }
    }


# ======================================
# Parser for:
#   * 'show cef table consistency-check'
# ======================================
class ShowCefTableConsistencyCheck(ShowCefTableConsistencyCheckSchema):

    ''' Parser for:
        * 'show cef table consistency-check'
    '''

    cli_command = 'show cef table consistency-check'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        parsed_dict = {}

        # Consistency checker master control: enabled
        p1 = re.compile(r'^Consistency\s+checker\s+master\s+control:\s+(?P<control>\w+)$')

        # IPv4:, IPv6:, Binding-Label:
        p2 = re.compile(r'^(?P<section>IPv4|IPv6|Binding-Label):$')

        #  lc-detect: disabled
        #  full-scan-rib-ios: enabled [1000 prefixes checked every 60s]
        p3 = re.compile(r'^\s+(?P<checker_type>[\w-]+):\s+(?P<status>\w+)(?:\s+\[(?P<prefixes>\d+)\s+prefixes\s+checked\s+every\s+(?P<interval>\d+)s\])?$')

        #   0/0/0/0 queries sent/ignored/checked/iterated
        p4 = re.compile(r'^\s+(?P<sent>\d+)\/(?P<ignored>\d+)\/(?P<checked>\d+)\/(?P<iterated>\d+)\s+queries\s+sent/ignored/checked/iterated$')

        # Checksum data checking disabled
        p5 = re.compile(r'^\s+Checksum\s+data\s+checking\s+(?P<status>\w+)$')

        # Inconsistency error messages are disabled
        p6 = re.compile(r'^\s+Inconsistency\s+error\s+messages\s+are\s+(?P<status>\w+)$')

        # Inconsistency auto-repair is enabled (10s delay, 300s holddown)
        p7 = re.compile(r'^\s+Inconsistency\s+auto-repair\s+is\s+(?P<status>\w+)(?:\s+\((?P<delay>\d+)s\s+delay,\s+(?P<holddown>\d+)s\s+holddown\))?$')

        # Inconsistency auto-repair runs: 0
        p8 = re.compile(r'^\s+Inconsistency\s+auto-repair\s+runs:\s+(?P<runs>\d+)$')

        # Inconsistency statistics: 0 confirmed, 0/16 recorded
        p9 = re.compile(r'^\s+Inconsistency\s+statistics:\s+(?P<confirmed>\d+)\s+confirmed,\s+(?P<recorded>\S+)\s+recorded$')

        current_section = None
        current_checker = None

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # Match master control
            m = p1.match(line)
            if m:
                parsed_dict['consistency_checker_master_control'] = m.groupdict()['control']
                continue

            # Match section headers (IPv4, IPv6, Binding-Label)
            m = p2.match(line)
            if m:
                section = m.groupdict()['section'].lower().replace('-', '_')
                current_section = section
                parsed_dict[current_section] = {}
                parsed_dict[current_section]['table_consistency_checker_state'] = {}
                continue

            # Match checker types
            m = p3.match(line)
            if m and current_section:
                checker_type = m.groupdict()['checker_type']
                status = m.groupdict()['status']
                prefixes = m.groupdict().get('prefixes')
                interval = m.groupdict().get('interval')
                
                current_checker = checker_type
                checker_dict = parsed_dict[current_section]['table_consistency_checker_state'][checker_type] = {}
                checker_dict['status'] = status
                
                if prefixes:
                    checker_dict['prefixes_checked'] = int(prefixes)
                if interval:
                    checker_dict['check_interval'] = int(interval)
                continue

            # Match query statistics
            m = p4.match(line)
            if m and current_section and current_checker:
                checker_dict = parsed_dict[current_section]['table_consistency_checker_state'][current_checker]
                checker_dict['queries_sent'] = int(m.groupdict()['sent'])
                checker_dict['queries_ignored'] = int(m.groupdict()['ignored'])
                checker_dict['queries_checked'] = int(m.groupdict()['checked'])
                checker_dict['queries_iterated'] = int(m.groupdict()['iterated'])
                continue

            # Match checksum data checking
            m = p5.match(line)
            if m and current_section:
                parsed_dict[current_section]['checksum_data_checking'] = m.groupdict()['status']
                continue

            # Match inconsistency error messages
            m = p6.match(line)
            if m and current_section:
                parsed_dict[current_section]['inconsistency_error_messages'] = m.groupdict()['status']
                continue

            # Match inconsistency auto-repair
            m = p7.match(line)
            if m and current_section:
                status = m.groupdict()['status']
                delay = m.groupdict().get('delay')
                holddown = m.groupdict().get('holddown')
                
                parsed_dict[current_section]['inconsistency_auto_repair'] = status
                if delay:
                    parsed_dict[current_section]['auto_repair_delay'] = int(delay)
                if holddown:
                    parsed_dict[current_section]['auto_repair_holddown'] = int(holddown)
                continue

            # Match auto-repair runs
            m = p8.match(line)
            if m and current_section:
                parsed_dict[current_section]['inconsistency_auto_repair_runs'] = int(m.groupdict()['runs'])
                continue

            # Match inconsistency statistics
            m = p9.match(line)
            if m and current_section:
                parsed_dict[current_section]['inconsistency_statistics_confirmed'] = int(m.groupdict()['confirmed'])
                parsed_dict[current_section]['inconsistency_statistics_recorded'] = m.groupdict()['recorded']
                continue

        return parsed_dict
