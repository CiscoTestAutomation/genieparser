"""show_cef.py

IOSXE parsers for the following show commands:

    * show cef path set id <id> detail | in Replicate oce:
    * show cef uid
    * show cef path sets summary
    * show cef interface <interface>
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

class ShowCefInterfacePolicyStatisticsSchema(MetaParser):
    """Schema for show cef interface policy-statistics"""
    
    schema = {
            'interfaces': {
                Any() : {
                    'status': str,
                    'if_number': int,
                    'corr_hwidb_fast_if_number': int,
                    'corr_hwidb_firstsw_if_number': int
                },
            },
        }

class ShowCefInterfacePolicyStatistics(ShowCefInterfacePolicyStatisticsSchema):
    """Parser for show cef interface policy-statistics"""

    cli_command = 'show cef interface policy-statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # AppGigabitEthernet1/0/1 is up (if_number 73)
        p1 = re.compile(r"^(?P<intf>.*)\s+is\s+(?P<status>\w+)\s+\(if_number\s+(?P<if_number>\d+)\)$")
        #   Corresponding hwidb fast_if_number 73
        p1_1 = re.compile(r"^\s+Corresponding\s+hwidb\s+fast_if_number\s+(?P<corr_hwidb_fast_if_number>\d+)$")
        #   Corresponding hwidb firstsw->if_number 73
        p1_2 = re.compile(r"^\s+Corresponding\s+hwidb\s+firstsw->if_number\s+(?P<corr_hwidb_firstsw_if_number>\d+)$")

        ret_dict = {}

        for line in output.splitlines():

            #TwentyFiveGigE1/1/2 is down (if_number 72)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                int_name = dict_val['intf']
                ret_dict.setdefault('Interfaces', {})\
                    .setdefault(int_name, {})
                data_dict  = ret_dict['interfaces'][int_name]
                data_dict['status'] = dict_val['status']
                data_dict['if_number'] = int(dict_val['if_number'])
                continue

            #Corresponding hwidb fast_if_number 72
            match_obj = p1_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                data_dict['corr_hwidb_fast_if_number'] = int(dict_val['corr_hwidb_fast_if_number'])
                continue

            #Corresponding hwidb firstsw->if_number 72
            match_obj = p1_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                data_dict['corr_hwidb_firstsw_if_number'] = int(dict_val['corr_hwidb_firstsw_if_number'])
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
                }
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

        return ret_dict
