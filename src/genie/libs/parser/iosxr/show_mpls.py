''' show_mpls.py

IOSXR parsers for the following show commands:
    * 'show mpls ldp interface'
    * 'show mpls label range'
    * 'show mpls ldp neighbor'
    * 'show mpls ldp neighbor {interface}'
    * 'show mpls ldp neighbor detail'
    * 'show mpls ldp neighbor {interface} detail'
    * 'show mpls ldp neighbor brief'
    * 'show mpls label table detail'
    * 'show mpls label table private'
    * 'show mpls interfaces'
    * 'show mpls interfaces {interface}'
    * 'show mpls forwarding'
    * 'show mpls forwarding vrf {vrf}'
    * 'show mpls ldp igp sync'
    * 'show mpls ldp graceful-restart'
    * 'show mpls ldp nsr summary'
    * 'show mpls traffic-eng tunnels tabular'
    * 'show mpls traffic-eng tunnels {tunnel_id}'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, ListOf, And,\
                                         Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# ======================================================
# Parser for 'show mpls ldp interface'
# ======================================================
class ShowMplsLdpInterfaceSchema(MetaParser):

    """Schema for show mpls ldp interface"""

    schema =  {
        'vrf': {
            Any(): {  
                'vrf_index': str,
                'interfaces': {
                    Any(): { 
                    'interface_index': str,
                        Optional('enabled'): {
                            Any(): {
                                'via': str,
                            }
                        },
                        Optional('disabled'): {
                            Any(): {
                                'via': str,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowMplsLdpInterface(ShowMplsLdpInterfaceSchema):

    '''Parser for show mpls ldp interface'''

    cli_command = ['show mpls ldp interface']

    """
    Interface HundredGigE0/5/0/0 (0xe0000c0)
        VRF: 'default' (0x60000000)
        Disabled: 
    Interface HundredGigE0/5/0/0.100 (0xe0001c0)
        VRF: 'default' (0x60000000)
        Disabled: 
    Interface TenGigE0/3/0/0 (0xa0004c0)
        VRF: 'default' (0x60000000)
        Enabled via config: LDP interface
    Interface TenGigE0/3/0/1.100 (0xa001940)
        VRF: 'default' (0x60000000)
        Disabled: 
    """

    def cli (self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        #Init returned dictionary        
        ret_dict = {}

        #Interface HundredGigE0/5/0/0.100 (0xe0001c0)
        p1 = re.compile(r'Interface\s+(?P<interface_name>[\w\/\.]+)\s+\((?P<interface_index>[\w]+)\)\s*$') 

        #VRF: 'default' (0x60000000)
        p2_1 = re.compile(r'(^VRF\:\s+(?P<vrf>\'(\w)+\')\s+\((?P<vrf_index>[\s\S]+)\)\s*$)') 

        #Enabled via config: LDP interface
        p2_2 = re.compile(r'^Enabled\s+via\s+(?P<via>[\w]+):\s+(?P<enabled>.*?)$') 

        #Disabled:
        #Disabled via config: LDP interface
        p2_3 = re.compile(r'^(?P<dis>Disabled\:)|Disabled\s+via\s+(?P<via>[\w]+):\s+(?P<disabled>.*?)$')                 

        for line in out.splitlines():
            line = line.strip()

            #Interface HundredGigE0/5/0/0.100 (0xe0001c0)
            m1 = p1.match(line)
                           
            if m1:
                interface_group = m1.groupdict()
                inter_name = interface_group['interface_name']
                inter_index = interface_group['interface_index']
                continue
            
            #VRF: 'default' (0x60000000)
            m2_1 = p2_1.match(line)
            if m2_1:
                vrf_group = m2_1.groupdict()
                #remove single code from 'default'
                vrf = vrf_group['vrf'].replace("'","")
                vrf_index = vrf_group['vrf_index']
                
                #define top level dictionary vrf and set to 'vrf'
                top_dict = ret_dict.setdefault('vrf', {})
                
                #define sub-default dictionary and set to 'default'
                def_dict = top_dict.setdefault(vrf, {})
                
                #set 'sub-default' dictionary
                def_dict['vrf_index'] = vrf_index  

                #define sub-interface dictionary and set to 'interfaces'
                int_dict = def_dict.setdefault('interfaces', {})

                #set sub-interfaces dictionary
                int_dict[inter_name] = {'interface_index':inter_index}
                
                #update top level dictionary 'sub-default dictionalry'                           
                top_dict.update({vrf:def_dict})
                continue                
            
            #Enabled via config: LDP interface
            m2_2 = p2_2.match(line)
            if m2_2:
                enabled_group = m2_2.groupdict()
                enabled = enabled_group['enabled']
                via = enabled_group['via']

                #define enabled_dict sub-dictionary within interface dictionary and set to 'enabled'
                enabled_dict = int_dict[inter_name].setdefault('enabled', {}).setdefault(enabled, {})

                #set enabled_dict
                enabled_dict['via'] = via                
                continue                

            #Disabled:
            m2_3 = p2_3.match(line)
            if m2_3:
                disabled_group = m2_3.groupdict()

                #Disabled via config: LDP interface | Disabled:
                disabled = disabled_group['disabled']

                #via:'config'  disable:'LDP interface'
                if disabled_group['via']:
                    via = disabled_group['via']

                    #define disabled_dic dictionary within interface dictionary and set to 'disabled'
                    disabled_dict = int_dict[inter_name].setdefault('disabled', {}).setdefault(disabled, {})
                    # disabled_dict['disabled'] = disabled
                    disabled_dict['via'] = via 
                
                #Disabled:      
                else:
                    disabled = disabled_group['disabled']

                    #define disabled_dic dictionary within interface dictionary and set to 'disabled'
                    disabled_dict = int_dict[inter_name].setdefault('disabled', {})
                continue               
        return ret_dict


# ======================================================
# Parser for 'show mpls label range'
# ======================================================
class ShowMplsLabelRangeSchema(MetaParser):

    """Schema for show mpls label range"""

    schema =  {
        'range_for_dynamic_labels':
			{'min_range': int,
			'max_range': int 	 
			},	 
	    }


class ShowMplsLabelRange(ShowMplsLabelRangeSchema):

    '''Parser for show mpls label range'''

    cli_command = ['show mpls label range']

    def cli (self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        # Init vars        
        mpls_dict = {}
        #Range for dynamic labels: Min/Max: 24000/1048575
        
        p1 = re.compile(r'Range +for +dynamic +labels: +Min/Max: +(?P<min_range>\d+)/(?P<max_range>\d+)')

        for line in out.splitlines():
            line = line.strip()

            #Range for dynamic labels: Min/Max: 24000/1048575
            m = p1.match(line)
            if m:
                group = m.groupdict()
                range_dict = mpls_dict.setdefault('range_for_dynamic_labels', {})
                range_dict.update({'min_range': int(group['min_range'])})
                range_dict.update({'max_range': int(group['max_range'])})
                continue
            
        return mpls_dict


# ==============================================
# Parser for 'show mpls ldp discovery'
# ==============================================
class ShowMplsLdpDiscoverySchema(MetaParser):

    """Schema for show mpls ldp discovery
                  show mpls ldp discovery detail
                  show mpls ldp afi-all discovery
                  show mpls ldp discovery <ldp>
                  show mpls ldp vrf <vrf> discovery
                  show mpls ldp vrf <vrf> discovery detail
    """

    schema = {
        'vrf': {
            Any(): {
                Optional('local_ldp_identifier'): {
                    Any(): {
                        Optional('discovery_sources'): {
                            'interfaces': {
                                Any(): {
                                    Optional('source_ip_addr'): str,
                                    Optional('transport_ip_addr'): str,
                                    Optional('xmit'): bool,
                                    Optional('recv'): bool,
                                    Optional('hello_interval_ms'): int,
                                    Optional('hello_due_time_ms'): int,
                                    Optional('quick_start'): str,
                                    Optional('ldp_id'): {
                                        Any(): {
                                            Optional('established_date'): str,
                                            Optional('established_elapsed'): str,
                                            Optional('holdtime_sec'): int,
                                            Optional('expiring_in'): float,
                                            Optional('proposed_local'): int,
                                            Optional('proposed_peer'): int,
                                            Optional('source_ip_addr'): str,
                                            Optional('transport_ip_addr'): str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowMplsLdpDiscovery(ShowMplsLdpDiscoverySchema):
    
    """Parser for show mpls ldp discovery
                  show mpls ldp discovery detail
                  show mpls ldp afi-all discovery
                  show mpls ldp discovery <ldp>
                  show mpls ldp vrf <vrf> discovery
                  show mpls ldp vrf <vrf> discovery detail
    """

    cli_command = ['show mpls ldp discovery',
                   'show mpls ldp discovery detail',
                   'show mpls ldp afi-all discovery',
                   'show mpls ldp discovery {ldp}',
                   'show mpls ldp vrf {vrf} discovery',
                   'show mpls ldp vrf {vrf} discovery detail']

    def cli(self, all="", detail="", vrf="", ldp="", output=None):
        if output is None:
            if vrf:
                if detail:
                    cmd = self.cli_command[5].format(vrf=vrf)
                else:
                    cmd = self.cli_command[4].format(vrf=vrf)
            elif ldp:
                cmd = self.cli_command[3].format(ldp=ldp)
            elif all:
                cmd = self.cli_command[2].format(ldp=ldp)
            elif detail:
                cmd = self.cli_command[1].format(ldp=ldp)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = "default"

        # initial return dictionary
        result_dict = {}
        discovery_flag = False
        targeted_flag = False

        # Local LDP Identifier: 10.52.26.119:0 
        p1 = re.compile(r'^Local +LDP +Identifier: ' 
                        '(?P<local_ldp_identifier>[\d\.\:]+)$') 

        # Discovery Sources: 
        p2 = re.compile(r'^Discovery +Sources:$') 

        # Bundle-Ether1 : xmit/recv 
        # TenGigE0/0/0/4.2096 (0x14c0) : xmit
        # Bundle-Ether3 (0x8000260) : xmit/recv
        p3 = re.compile(r'^((?P<interface>\S+) +)(\S.*|): *(?P<xmit>xmit)?\/?(?P<recv>recv)?$') 

        # VRF: 'default' (0x60000000) 
        p4 = re.compile(r'^VRF: \'(?P<vrf>\S+)\' +\(\d+x\d+\)$') 

        # LDP Id: 10.12.31.251:0
        # LDP Id: 10.52.31.244:0, Transport address: 10.52.31.244 
        p5 = re.compile(r'^(?P<ldp_tdp>\w+) +Id:(?P<space>\s{1,2})?(?P<ldp_tdp_id>[\d\.\:]+)(,' 
                        ' +Transport +address: +(?P<transport_ip_addr>[\d\.]+)|)$')

        # Hold time: 15 sec (local:15 sec, peer:15 sec) 
        p6 = re.compile(r'^Hold +time: +(?P<holdtime_sec>\d+) +sec ' 
                        '\(local:(?P<proposed_local>\d+) +sec, ' 
                        'peer:(?P<proposed_peer>\d+) +sec\)$') 

        # (expiring in 12.5 sec)
        p7 = re.compile(r'\(expiring +in +(?P<expiring_in>\d.*) +sec\)$')

        # Established: Nov  6 14:39:26.164 (5w2d ago) 
        p8 = re.compile(r'^Established: +(?P<established_date>\S.*) +\((?P<established_elapsed>\S*) +ago\)$') 

        # Source address: 10.166.0.57; Transport address: 10.52.31.247
        p9 = re.compile(r'^Source +address: +(?P<source_ip_addr>[\d\.]+);'
                        ' +Transport +address: +(?P<transport_ip_addr>[\d\.]+)$')

        # Hello interval: 5 sec (due in 2.3 sec)
        p10 = re.compile(r'^Hello +interval: +(?P<hello_interval>\d+) +sec'
                        ' +\(due +in +(?P<hello_due_time>\S+ \S+)\)$')

        # Quick-start: Enabled
        p11 = re.compile(r'^Quick-start: +(?P<quick_start>\S+)$')

        # 10.1.1.1 -> 10.3.3.3 (active), xmit/recv
        p12 = re.compile(r'^(?P<source>[\d\.]+) +\-> +(?P<destination>[\d\.]+)'
                            ' +\((?P<status>(active|passive|active\/passive)+)\),'
                            ' +(?P<xmit>xmit)?\/?(?P<recv>recv)?$')

        # TODO Unlike iosxe, 'Hello interval', 'quick-start', 'hold time', 'established' 
        # are also used for interfaces, hence Targeted Hello is omitted.
        # Targeted Hellos:
        # p13 = re.compile(r'^Targeted +Hellos:$')

        for line in out.splitlines(): 
            line = line.strip()
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})
                local_ldp_identifier_dict = ldp_dict.setdefault('local_ldp_identifier', {}). \
                            setdefault(group['local_ldp_identifier'], {})
                continue

            # Discovery Sources: 
            m = p2.match(line) 
            if m:  
                discovery_flag = True 
                targeted_flag = False
                continue 

            # Targeted Hellos:
            # m = p13.match(line)
            # if m:
            #     discovery_flag = False
            #     targeted_flag = True
            #     continue
            
            # Bundle-Ether1 : xmit/recv 
            m = p3.match(line) 
            if m:  
                group = m.groupdict()
                interface = group['interface'] if group['interface'] else "default" 
                interface_dict = local_ldp_identifier_dict.setdefault('discovery_sources', {}).setdefault('interfaces', {}).setdefault(interface, {}) 
                interface_dict.update({'xmit': True if group['xmit'] else False}) 
                interface_dict.update({'recv': True if group['recv'] else False}) 
                continue 

            # VRF: 'default' (0x60000000) 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                # group['vrf']
                continue

            # LDP Id: 10.52.31.244:0, Transport address: 10.52.31.244 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_tdp = group['ldp_tdp'].lower()
                if discovery_flag:
                    ldp_dict = interface_dict.setdefault('{}_id'.format(ldp_tdp), {}).setdefault(
                        group['ldp_tdp_id'], {})

                if group['transport_ip_addr']:
                    interface_dict.update({'transport_ip_addr': group['transport_ip_addr']})

                # if targeted_flag:
                #     if targeted_dict:
                #         targeted_dict.update({'{}_id'.format(ldp_tdp): group['ldp_tdp_id']})
                continue

            # Hold time: 15 sec (local:15 sec, peer:15 sec) 
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({k: int(v) for k, v in group.items() if v})
                continue

            # (expiring in 12.5 sec)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'expiring_in': float(group['expiring_in'])})

            # Established: Nov  6 14:39:26.164 (5w2d ago) 
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'established_date': group['established_date']})
                ldp_dict.update({'established_elapsed': group['established_elapsed']})

            # Source address: 10.166.0.57; Transport address: 10.52.31.247
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if 'source_ip_addr' in interface_dict.keys():
                    ldp_dict.update({k: v for k, v in group.items() if v})
                else:
                    interface_dict.update({k: v for k, v in group.items() if v})
                continue

            # Hello interval: 5 sec (due in 2.3 sec)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'hello_interval_ms': 1000*int(group['hello_interval'])})
                if ' sec' in group['hello_due_time']:
                    hello_due_time_ms = int(1000*float(group['hello_due_time'].split(' ')[0]))
                else: 
                    hello_due_time_ms = int(group['hello_due_time'].split(' ')[0])
                interface_dict.update({'hello_due_time_ms': hello_due_time_ms})
                continue

            # Quick-start: Enabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'quick_start': group['quick_start'].lower()})
                continue

            #  10.81.1.1 -> 172.16.94.33 (active), xmit/recv
            m = p12.match(line)
            if m:
                group = m.groupdict()
                targeted_dict = local_ldp_identifier_dict.setdefault('targeted_hellos', {}). \
                    setdefault(group['source'], {}). \
                    setdefault(group['destination'], {})
                targeted_dict.update({'xmit': True if group['xmit'] else False})
                targeted_dict.update({'recv': True if group['recv'] else False})
                targeted_dict.update({'active': True if group['status'] == 'active' else False})
                continue
            
        return result_dict


# ==============================================
#   Show mpls ldp discovery detail
# ==============================================
class ShowMplsLdpDiscoveryDetailSchema(MetaParser):
    """
    Schema for show mpls ldp discovery detail
    """
    schema = {
        'vrf': {
            Optional('local_ldp_identifier'): str,
            'vrfs': ListOf({
                'vrf_name': str,
                'interfaces': ListOf({
                    Optional('interface'): str,
                    Optional('vrf_hex'): str,
                    Optional('source_ip_addr'): str,
                    Optional('transport_ip_addr'): str,
                    Optional('xmit'): str,
                    Optional('recv'): str,
                    Optional('hello_interval_ms'): str,
                    Optional('hello_due_time_ms'): str,
                    Optional('quick_start'): str,
                    Optional('ldp_id'): {
                        Optional('network_addr'): str,
                        "ldp_entries": ListOf({
                            Optional('source_ip_addr'): str,
                            Optional('transport_ip_addr'): str,
                            Optional('holdtime_sec'): str,
                            Optional('proposed_local'): str,
                            Optional('proposed_peer'): str,
                            Optional('expiring_in'): str,
                            Optional('established_date'): str,
                            Optional('established_elapsed'): str,
                            Optional('last_session_connection_failures'): ListOf({
                                Optional('timestamp'): str,
                                Optional('reason'): str,
                                Optional('last_up_for'): str,
                            })
                        })
                    }
                })
            })
        }
    }


class ShowMplsLdpDiscoveryDetail(ShowMplsLdpDiscoveryDetailSchema):
    """
        Parser for show mpls ldp discovery detail
    """
    cli_command = 'show mpls ldp discovery detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        discovery_flag = False

        # Local LDP Identifier: 10.94.1.1:0
        p1 = re.compile(r'^Local +LDP +Identifier: '
                        '(?P<local_ldp_identifier>[\d\.\:]+)$')

        # Discovery Sources:
        p2 = re.compile(r'^Discovery +Sources:$')

        # TenGigE0/3/0/0 (0xa0004c0) : xmit/recv
        p3 = re.compile(r'^(?P<interface>\S+) \((?P<interface_hex>[\w]+)\)'
                        ' : (?P<xmit>xmit)?\/?(?P<recv>recv)?$')

        # VRF: 'default' (0x60000000)
        p4 = re.compile(r'^VRF: \'(?P<vrf>\S+)\' +\((?P<vrf_hex>[\w]+)\)$')

        # LDP Id: 10.144.96.96:0
        p5 = re.compile(r'^(?P<ldp_tdp>\w+) +Id:\s*(?P<ldp_tdp_id>[\S]+)$')

        # Source address: 10.120.0.1; Transport address: 10.94.1.1
        p6 = re.compile(r'^Source +address: +(?P<source_ip_addr>[\d\.]+);'
                        ' +Transport +address: +(?P<transport_ip_addr>[\d\.]+)$')

        # Hold time: 15 sec (local:15 sec, peer:45 sec)
        p7 = re.compile(r'^Hold +time: +(?P<holdtime_sec>\d+) +sec '
                        '\(local:(?P<proposed_local>\d+) +sec, '
                        'peer:(?P<proposed_peer>\d+) +sec\)$')

        # (expiring in 11 sec)
        # (expiring in 14.5 sec)
        p8 = re.compile(r'^\(expiring +in +(?P<expiring_in>\d.*) +sec\)$')

        # Established: Nov  6 14:39:26.164 (5w2d ago)
        p9 = re.compile(r'^Established: +(?P<established_date>\S.*) '
                        '+\((?P<established_elapsed>\S*) +ago\)$')

        # Hello interval: 5 sec (due in 563 msec)
        p10 = re.compile(r'^Hello +interval: +(?P<hello_interval>\d+) +sec'
                        ' +\(due +in +(?P<hello_due_time>\S+ +\S+)\)$')

        # Quick-start: Enabled
        p11 = re.compile(r'^Quick-start: +(?P<quick_start>\S+)$')

        # Last session connection failures:
        p12 = re.compile(r'^Last +session +connection +failures:$')

        #     Jan  4 05:20:34.814: User cleared session manually
        #     Jan  4 05:28:48.641: User cleared session manually
        p13 = re.compile(r'^(?P<timestamp>[A-Z][a-z]{2}\s+[0-9]{1,2}\s[0-9:.]+)'
                         ':\s+(?P<reason>[\w\s]+)$')

        #         (Last up for 00:06:56)
        #         (Last up for 00:08:05)
        p14 = re.compile(r'\(Last +up +for +(?P<last_up_for>[\d:]+)\)$')

        for line in out.splitlines():
            line = line.strip()

            # Local LDP Identifier: 10.94.1.1:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_dict = result_dict.setdefault('vrf', {})
                ldp_dict.update(
                    {'local_ldp_identifier': group['local_ldp_identifier']})
                continue

            # Discovery Sources:
            m = p2.match(line)
            if m:
                discovery_flag = True
                continue

            # TenGigE0/3/0/0 (0xa0004c0) : xmit/recv
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface'] if group['interface'] \
                    else "default"

                interface_dict = {'interface': interface}
                interface_dict.update(
                    {'xmit': 'True' if group['xmit'] else 'False'})
                interface_dict.update(
                    {'recv': 'True' if group['recv'] else 'False'})
                continue

            # VRF: 'default' (0x60000000)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_name = group['vrf'] if group['vrf'] else "default"
                vrf_list = result_dict.setdefault('vrf', {}).\
                    setdefault('vrfs', [])

                vrf = next(
                    (i for i in vrf_list if i['vrf_name'] == vrf_name), None)

                if vrf is None:
                    vrf = {'vrf_name': vrf_name, 'interfaces': []}
                    vrf_list.append(vrf)

                if interface:
                    vrf_hex = group['vrf_hex']
                    interface_dict.update({'vrf_hex': vrf_hex})
                    vrf['interfaces'].append(interface_dict)

                continue

            # LDP Id: 10.144.96.96:0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_tdp = group['ldp_tdp'].lower()
                ldp_tdp_id = group['ldp_tdp_id']
                if discovery_flag:
                    ldp_dict = interface_dict.\
                        setdefault('{}_id'.format(ldp_tdp), {})

                    net_addr = next((i for i in ldp_dict
                                    if i['network_addr'] == ldp_tdp_id
                                    ), None)

                    if net_addr is None:
                        net_addr = {
                            'network_addr': ldp_tdp_id,
                            'ldp_entries': []
                        }
                        ldp_dict.update(net_addr)

                continue

            # Source address: 10.166.0.57; Transport address: 10.52.31.247
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if 'source_ip_addr' in interface_dict.keys():
                    item_dict = {k: v for k, v in group.items() if v}
                    net_addr['ldp_entries'].append(item_dict)
                else:
                    interface_dict.update(
                        {k: v for k, v in group.items() if v})
                continue

            # Hold time: 15 sec (local:15 sec, peer:45 sec)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                item_dict.update(
                    {k: v for k, v in group.items() if v})
                continue

            # (expiring in 14.5 sec)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                item_dict.update(
                    {'expiring_in': group['expiring_in']})

            m = p9.match(line)
            if m:
                group = m.groupdict()
                item_dict.update({
                    'established_date': group['established_date'],
                    'established_elapsed': group['established_elapsed']
                })

            # Hello interval: 5 sec (due in 563 msec)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'hello_interval_ms': str(
                    1000*int(group['hello_interval']))})
                if ' sec' in group['hello_due_time']:
                    hello_due_time_ms = str(
                        int(1000*float(group['hello_due_time'].split(' ')[0])))
                else:
                    hello_due_time_ms = str(
                        int(group['hello_due_time'].split(' ')[0]))
                interface_dict.update({'hello_due_time_ms': hello_due_time_ms})
                continue

            # Quick-start: Enabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update(
                    {'quick_start': group['quick_start'].lower()})
                continue

            # Last session connection failures:
            m = p12.match(line)
            if m:
                item_dict['last_session_connection_failures'] = []

            m = p13.match(line)
            if m:
                group = m.groupdict()
                connection_failure_dict = {
                    'timestamp': group['timestamp'],
                    'reason': group['reason']
                }

                item_dict['last_session_connection_failures'].append(
                    connection_failure_dict)
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                connection_failure_dict.update(
                    {'last_up_for': group['last_up_for']})

        return result_dict


# ======================================================
# Parser for 'show mpls ldp neighbor'
# ======================================================
class ShowMplsLdpNeighborSchema(MetaParser):
    
    """Schema for 
     show mpls ldp neighbor
     show mpls ldp neighbor {interface}
     show mpls ldp neighbor detail
     show mpls ldp neighbor {interface} detail
     """

    schema = {
        'vrf':{
            Any():{ 
                'peers':{
    	        	Any():{
                        'label_space_id':{
                            Any():{
                                'tcp_connection': str,
    	        		        Optional('local_ldp_ident'): str,
    	        		        Optional('graceful_restart'): str,
    	        		        Optional('session_holdtime'): int,
                                Optional('session_holdtime_ms'): int,
                                Optional('password'): str,
    	        		        'state': str,
    	        		        'msg_sent': int,
    	        		        'msg_rcvd': int,
    	        		        'neighbor': str,
                                Optional('last_tib_rev_sent'): int,
                                'uptime': str,
                                Optional('uid'): int,
                                Optional('peer_id'): int,
                                Optional('address_family'):{
                                    Any():{
    	        		                'ldp_discovery_sources': {
    	        		                	Optional('interface'):{
    	        		                		Any():{
    	        		                			Optional('ip_address'):{
                                                        Any():{
                                                            Optional('holdtime_ms'): int,
                                                            Optional('hello_interval_ms'): int,
                                                            Optional('holdtime'): int,
                                                            Optional('hello_interval'): int,
                                                            Optional('holdtime_str'): str,
                                                        },
                                                    },
    	        		                		},
    	        		                	},
    	        		                	Optional('targeted_hello'):{
    	        		                		Any():{
    	        		                			Any():{
    	        		                				Optional('active'): bool,
                                                        Optional('holdtime_ms'): int,
                                                        Optional('hello_interval_ms'): int,
                                                        Optional('holdtime'): int,
                                                        Optional('hello_interval'): int,
                                                        Optional('holdtime_str'): str,
    	        		                			},
    	        		                		},
    	        		                	},
    	        		                },
                	        		    Optional('address_bound'): list,
                                    }
                                },
    	        		        Optional('peer_holdtime'): int,
    	        		        Optional('ka_interval'): int,
    	        		        Optional('peer_holdtime_ms'): int,
    	        		        Optional('ka_interval_ms'): int,
    	        		        Optional('peer_state'): str,
    	        		        Optional('clients'): str,
    	        		        Optional('inbound_label_filtering'): str,
    	        		        Optional('session_protection'):{
    	        		        	'session_state': str,
    	        		        	Optional('duration_int'): int,
                                    Optional('duration_str'): str,
    	        		        },
    	        		        Optional('nsr'): str,
    	        		        Optional('capabilities'): {
    	        		        	Optional('sent'): {
    	        		        		Any(): str,
    	        		        	},
    	        		        	Optional('received'): {
    	        		        		Any(): str,
    	        		        	},
    	        		        },
                            },
                        },
    	        	},
    	        },
            }
        }
    }


class ShowMplsLdpNeighbor(ShowMplsLdpNeighborSchema):

    """Parser for
     show mpls ldp neighbor
     show mpls ldp neighbor {interface}
      """

    cli_command = ['show mpls ldp neighbor', 'show mpls ldp vrf {vrf} neighbor',
     'show mpls ldp neighbor {interface}', 'show mpls ldp vrf {vrf} neighbor {interface}']

    def cli(self, vrf="", interface=None, output=None):
        if output is None:
            if vrf and interface:
                out = self.device.execute(self.cli_command[3].\
                    format(vrf=vrf, interface=interface))
            elif not vrf and interface:
                out = self.device.execute(self.cli_command[2].\
                    format(interface=interface))
            elif vrf and not interface:
                out = self.device.execute(self.cli_command[1].\
                    format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])

        else:
            out = output
        
        if not vrf:
            vrf = 'default'

        # initial return dictionary
        mpls_dict = {}
        target_flag = False
        interface_flag = False
        receive_flag = False
        sent_flag = False 

        # Peer LDP Identifier: 10.16.0.2:0
        # Peer LDP Ident: 10.169.197.252:0; Local LDP Ident 10.169.197.254:0
        p1 = re.compile(r'^Peer +LDP +(Ident|Identifier): *'
        '(?P<peer_ldp>[\d\.]+):(?P<label_space_id>\d+)(; '
        '+Local +LDP +(Ident|Identifier) +(?P<local_ldp>\S+)$)?')

        # TCP connection: 10.16.0.2:646 - 10.16.0.9:38143
        p2 = re.compile(r'^TCP +connection: *(?P<tcp_connection>[\S\s]+)$')
        
        # Graceful Restart: No
        p3 = re.compile(r'^Graceful +Restart: +(?P<graceful_restart>[\S\s]+)$')

        # Session Holdtime: 180 sec
        p4 = re.compile(r'Session Holdtime: +(?P<session_holdtime>\d+)'
        ' +(?P<rate>(sec|ms))$')

        # Password: not required, none, in use
        p5 = re.compile(r'^Password: +(?P<password>[\S\s]+)$')

        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream
        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
        #     State: Oper; Msgs sent/rcvd: 5855/6371; Downstream on demand
        #     State: Oper; Msgs sent/rcvd: 24710/24702; Downstream-Unsolicited
        p6 = re.compile(r'^State: *(?P<state>\w+); +Msgs +sent\/rcvd:'
        ' *(?P<msg_sent>\d+)\/(?P<msg_rcvd>\d+)(;'
        ' +(?P<neighbor>[\w\s/-]+))?(; +Last +TIB +rev +sent +'
        '(?P<last_tib_rev_sent>\d+))?$')

        #  Up time: 04:26:14
        #  Up time: 3d21h; UID: 4; Peer Id 0
        p7 = re.compile(r'^Up +time: *(?P<up_time>[\w\:]+)(; '
        '+UID: *(?P<uid>\d+); +Peer +Id +(?P<peer_id>\d+);?)?$')

        #     LDP discovery sources:
        #       ATM3/0.1
        #
        #      IPv4: (1)
        #       GigabitEthernet0/0/0/1
        #      IPv6: (0)
        p8 = re.compile(r'(?P<address_family>(IPv4|IPv6)): +\((?P<number>\d)\)')

        #       GigabitEthernet0/0/0, Src IP addr: 10.169.197.93
        p9 = re.compile(r'(?P<interface>[A-Za-z-]+[\d/.]+)((,|;)'
        ' +Src +IP +addr: *(?P<src_ip_address>[\d\.]+))?$')

        #'Targeted Hello (10.36.3.3 ->172.20.22.22, active, passive)'
        # 'Targeted Hello 192.168.189.2 ->192.168.189.4, active, passive;'
        #'Targeted Hello (10.4.1.1 ->10.16.2.2, active)'
        #'Targeted Hello (10.4.1.1 ->10.16.2.2, passive)'
        #'Targeted Hello 10.4.1.1 ->10.16.2.2, passive'
        #'Targeted Hello 10.4.1.1 ->10.16.2.2, passive;'
        #'Targeted Hello 10.4.1.1 ->10.16.2.2, active;'
        #'Targeted Hello 10.4.1.1 ->10.16.2.2, active'
        #'Targeted Hello 10.36.3.3 ->172.20.22.22'
        # 'Targeted Hello (10.36.3.3 ->172.20.22.22)'
        p10 = re.compile(r'Targeted +Hello +\(?(?P<ldp_ip>[\d/.]+)'
        '\s*->\s*(?P<tdp_ip>[\d/.]+),?\s*'
        '(?P<key1>[\S\s]+)+(,|;)? +(?P<key2>passive)?')

        # holdtime: 15000 ms, hello interval: 5000 ms
        # holdtime: infinite, hello interval: 10000 ms
        p11 = re.compile(r'^holdtime: *(?P<holdtime>(\d+|\w+)) '
        '*(?P<hold_rate>(ms|sec))?, +hello +interval: '
        '*(?P<hello_interval>\d+) +(?P<hello_rate>(ms|sec))$')

        # Addresses bound to this peer:
        # IPv4: (4)
        #   10.16.0.7        10.16.27.7       10.16.78.7       10.16.79.7       
        # IPv6: (0)
        p12 = re.compile(r'(?P<address_bound_peer_ldp>[\d\.\s]+)$')

        # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
        p13 = re.compile(r'^Peer +holdtime: *(?P<peer_holdtime>\d+) +'
        '(?P<peer_rate>(ms|sec)); +KA +interval: '
        '*(?P<ka_interval>\d+) +(?P<ka_rate>(ms|sec));'
        ' +Peer +state: +(?P<peer_state>\S+)$')
        
        # Clients: Dir Adj Client
        p14 = re.compile(r'^Clients: +(?P<clients>[\S\s]+)$')

        # Inbound label filtering: accept acl 'pfx_acl2'
        p15 = re.compile(r'^Inbound +label +filtering: +'
        '(?P<inbound_label_filtering>[\S\s]+)$') 

        #Enabled, state: Ready
        #LDP Session Protection: enabled, state: protecting
        p16 = re.compile(r'(LDP +Session +Protection:? )?(E|e)nabled, +state: '
        '+(?P<session_state>\w+)$')

        #Duration: 30 seconds
        #duration: infinite
        p17 = re.compile(r'(D|d)uration: +(?P<duration>(\d+|\w+)) *(seconds)?')

        # NSR: Disabled
        # LDP NSR: Enabled
        p18 = re.compile(r'(LDP\s+)?NSR: +(?P<nsr>\w+)$')

        #  Capabilities:
        #  Capabilities Sent:
        p19 = re.compile(r'^Capabilities+(\sSent)?:')

        #  Capabilities Recieved:
        #  Recieved:
        p20 = re.compile(r'(Capabilities\s+)?Received:')

        # 0x508  (MP: Point-to-Multipoint (P2MP))
        # 0x509  (MP: Multipoint-to-Multipoint (MP2MP))
        p21 = re.compile(r'(?P<key>\S+) +\((?P<value>MP: +\S+ +\(\S+\))\)')

        # 0x50b  (Typed Wildcard FEC)
        p22 = re.compile(r'(?P<key>\S+) +\((?P<value>Typed +Wildcard +FEC)\)')

        for line in out.splitlines():
            line = line.strip()
            # Peer LDP Identifier: 10.16.0.2:0
            # Peer LDP Ident: 10.169.197.252:0; Local LDP Ident 10.169.197.254:0
            m = p1.match(line)
            if m: 
                group = m.groupdict()
                peer_dict = mpls_dict.setdefault('vrf', {}).setdefault(vrf,{}).setdefault('peers', {}).\
                    setdefault(group['peer_ldp'], {}).\
                    setdefault('label_space_id', {}).\
                    setdefault(int(group['label_space_id']), {})
                if group['local_ldp']:
                    peer_dict.update({'local_ldp_ident':group['local_ldp'] })
                continue
            
            # TCP connection: 10.16.0.2:646 - 10.16.0.9:38143
            m = p2.match(line)
            if m: 
                group = m.groupdict()
                peer_dict.update({'tcp_connection': group['tcp_connection']})
                continue

            # Graceful Restart: No
            m = p3.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'graceful_restart': group ['graceful_restart']})
                continue

            # Session Holdtime: 180 sec
            # Session Holdtime: 180000 ms
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key = 'session_holdtime' if group['rate'] == 'sec' \
                    else 'session_holdtime_ms' 
                peer_dict.update({key: int(group['session_holdtime'])}) 
                continue

            # Password: not required, none, in use
            m = p5.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'password': group['password']})
                continue
            
            # State: Oper; Msgs sent/rcvd: 824/825; Downstream
            # State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
            m = p6.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'state': group['state']})
                peer_dict.update({'msg_sent': int(group['msg_sent'])})
                peer_dict.update({'msg_rcvd': int(group['msg_rcvd'])})
                if group['neighbor']:
                    peer_dict.update({'neighbor': group['neighbor']})
                if group['last_tib_rev_sent']:
                    peer_dict.update({'last_tib_rev_sent': int(group['last_tib_rev_sent'])})
                continue

            #  Up time: 04:26:14
            #  Up time: 3d21h; UID: 4; Peer Id 0
            #  p7 = re.compile(r'^Up +time: *(?P<up_time>[\w\:]+)(; +UID: *(?P<uid>\d+); +Peer +Id +(?P<peer_id>\d+))?$')
            m = p7.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'uptime': group['up_time']})
                if group['uid']:
                    peer_dict.update({'uid': int(group['uid'])})
                if group['peer_id']:
                    peer_dict.update({'peer_id': int(group['peer_id'])})
                continue

            #      IPv4: (1)
            #       GigabitEthernet0/0/0/1
            #      IPv6: (0)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if int(group['number']) !=0:
                    address_dict = peer_dict.setdefault('address_family', {}).\
                                        setdefault(group['address_family'].lower(), {})      
                continue

            # LDP discovery sources:
            #       GigabitEthernet0/0/0, Src IP addr: 10.169.197.93
            #       ATM3/0.1
            #
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_source_dict = address_dict.setdefault('ldp_discovery_sources',{}).\
                                            setdefault('interface',{}).\
                                            setdefault(group['interface'],{})
                target_flag = False
                interface_flag = True
                if group['src_ip_address']:
                    ldp_source_ip_address_dict = ldp_source_dict.setdefault('ip_address',{}).\
                                                    setdefault(group['src_ip_address'],{})
                    
                continue
        
            #'Targeted Hello (10.36.3.3 ->172.20.22.22, active, passive)'
            #'Targeted Hello 192.168.189.2 ->192.168.189.4, active, passive;'
            #'Targeted Hello (10.4.1.1 ->10.16.2.2, active)'
            #'Targeted Hello (10.4.1.1 ->10.16.2.2, passive)'
            #'Targeted Hello 10.4.1.1 ->10.16.2.2, passive'
            #'Targeted Hello 10.4.1.1 ->10.16.2.2, passive;'
            #'Targeted Hello 10.4.1.1 ->10.16.2.2, active;'
            #'Targeted Hello 10.4.1.1 ->10.16.2.2, active'
            #'Targeted Hello 10.36.3.3 ->172.20.22.22'
            # 'Targeted Hello (10.36.3.3 ->172.20.22.22)'
            m = p10.match(line)
            if m:
                group = m.groupdict()
                target_dict = address_dict.setdefault('ldp_discovery_sources',{}).\
                                        setdefault('targeted_hello',{}).\
                                        setdefault(group['ldp_ip'],{}).\
                                        setdefault(group['tdp_ip'], {})
                interface_flag = False
                target_flag = True
                if group['key1'] == 'active' and not group['key2']:
                    target_dict.update({'active': True})
                else:
                    target_dict.update({'active': False}) 

                continue

            # holdtime: 15000 ms, hello interval: 5000 ms
            # holdtime: infinite, hello interval: 10000 ms
            m = p11.match(line)
            if m:
                group = m.groupdict()
                #if interface_flag:
                if group['hold_rate']:
                    hold_key = 'holdtime' if group['hold_rate'] == 'sec' \
                        else 'holdtime_ms'
                    hold_val = int(group['holdtime'])
                else:
                    hold_key = 'holdtime_str'    

                hello_key = 'hello_interval' if group['hello_rate'] == 'sec' \
                    else 'hello_interval_ms'
                hello_val =  int(group['hello_interval'])
                if interface_flag:
                    ldp_source_ip_address_dict.update({hold_key:hold_val})
                    ldp_source_ip_address_dict.update({hello_key:hello_val})
                    interface_flag = False
                if target_flag:
                    target_dict.update({hold_key:group['holdtime']})
                    target_dict.update({hello_key:hello_val})
                    target_flag = False
                
                continue
            
            #   10.16.0.7        10.16.27.7       10.16.78.7       10.16.79.7       
            m = p12.match(line)
            if m:
                group = m.groupdict()
                address_bound_list = group['address_bound_peer_ldp'].split()
                if 'address_bound' not in address_dict:
                    address_dict.update({'address_bound': address_bound_list})
                else:
                    address_dict['address_bound'].extend(address_bound_list)
            
                continue
            
            # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
            m = p13.match(line)
            if m:
                group = m.groupdict()
                peer_key = 'peer_holdtime' if group['peer_rate'] == 'sec' \
                    else 'peer_holdtime_ms'
                interval_key = 'ka_interval'  if group['ka_rate'] == 'sec' \
                    else 'ka_interval_ms'
                peer_dict.update({peer_key: int(group['peer_holdtime'])})
                peer_dict.update({interval_key: int(group['ka_interval'])})
                peer_dict.update({'peer_state': group['peer_state']})

                continue
            
            # Clients: Dir Adj Client
            m = p14.match(line)
            if m: 
                group = m.groupdict()
                peer_dict.update({'clients': group['clients']})

                continue
            
            # Inbound label filtering: accept acl 'pfx_acl2'
            m = p15.match(line)
            if m: 
                group = m.groupdict()
                peer_dict.update({'inbound_label_filtering': group['inbound_label_filtering']})

                continue
            
            #Enabled, state: Ready
            #LDP Session Protection: enabled, state: protecting
            m = p16.match(line)
            if m:
                group = m.groupdict()
                session_dict = peer_dict.setdefault('session_protection', {})
                session_dict.update({'session_state': group['session_state']})

                continue
            #Duration: 30 seconds
            #duration: infinite
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if group['duration'].isdigit():
                    session_dict.update({'duration_int': int(group['duration'])})
                else: 
                    session_dict.update({'duration_str': group['duration']})

                continue

            # NSR: Disabled
            # LDP NSR: Enabled
            m = p18.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'nsr': group['nsr']})
                
                continue

            #  Capabilities:
            #  Capabilities Sent:
            m = p19.match(line)
            if m:
                sent_flag = True
                sent_dict = peer_dict.setdefault('capabilities',{}).\
                                        setdefault('sent',{})
                continue

            #  Capabilities Recieved:
            #  Recieved:
            m = p20.match(line)
            if m:
                receive_flag = True
                sent_flag = False
                recieved_dict = peer_dict.setdefault('capabilities', {}).\
                    setdefault('received', {})

                continue
            # 0x508  (MP: Point-to-Multipoint (P2MP))
            # 0x509  (MP: Multipoint-to-Multipoint (MP2MP))
            m = p21.match(line)
            if m:
                group = m.groupdict() 
                if sent_flag:
                    sent_dict.update({group['key'] :group['value']})
                if receive_flag:
                    recieved_dict.update({group['key'] :group['value']})
                
                continue
            
            # 0x50b  (Typed Wildcard FEC)
            m = p22.match(line)
            if m:
                group = m.groupdict() 
                if sent_flag:
                    sent_dict.update({group['key'] :group['value']})
                if receive_flag:
                    recieved_dict.update({group['key'] :group['value']})
                
                continue

        return mpls_dict


class ShowMplsLdpNeighborDetail(ShowMplsLdpNeighbor):
    """Parser for show mpls ldp neighbor detail,
                  show mpls ldp neighbor {interface} detail"""

    cli_command = ['show mpls ldp neighbor detail', 'show mpls ldp vrf {vrf} neighbor detail', 
    'show mpls ldp neighbor {interface} detail', 'show mpls ldp vrf {vrf} {interface} detail']

    def cli(self, vrf="", interface=None, output=None):
        if output is None:
            if vrf and interface:
                out = self.device.execute(self.cli_command[3].\
                    format(vrf=vrf, interface=interface))
            elif not vrf and interface:
                out = self.device.execute(self.cli_command[2].\
                    format(interface=interface))
            elif vrf and not interface:
                out = self.device.execute(self.cli_command[1].\
                    format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])

        else:
            out = output

        return super().cli(vrf=vrf, interface=interface, output=out)


# ======================================================
# Parser for 'show mpls ldp neighbor brief'
# ======================================================
class ShowMplsLdpNeighborBriefSchema(MetaParser):
    
    """Schema for show mpls ldp neighbor brief"""

    schema = {
        'peer': { 
            Any(): { 
                'gr': str,
                Optional('nsr'): str,
                'up_time': str,
                Optional('discovery'): {
                    Optional('discovery'): int,
                    Optional('ipv4'): int,
                    Optional('ipv6'): int,
                },
                Optional('addresses'): {
                    Optional('address'): int,
                    Optional('ipv4'): int,
                    Optional('ipv6'): int,
                },
                Optional('labels'): {
                    Optional('ipv4'): int,
                    Optional('ipv6'): int,
                },
            },
        },
    }


class ShowMplsLdpNeighborBrief(ShowMplsLdpNeighborBriefSchema):

    """Parser for show mpls ldp neighbor brief"""

    cli_command = 'show mpls ldp neighbor brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Init vars
        mpls_dict = {}
        peer = ''

        # Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
        #                                         ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
        # -----------------  --  ---  ----------  ----------  ----------  ------------
        # 10.205.2.254:0     Y   Y    31w0d       2     0     10    0     77     0
        p1 = re.compile(r'^(?P<peer>[\d\.:]+)\s+(?P<gr>[\w]+)\s+'
                         '(?P<nsr>[\w]+)\s+(?P<up_time>[\w\d\:]+)\s+'
                         '(?P<discovery_ipv4>[\d]+)\s+(?P<discovery_ipv6>[\d]+)\s+'
                         '(?P<addresses_ipv4>[\d]+)\s+(?P<addresses_ipv6>[\d]+)\s+'
                         '(?P<labels_ipv4>[\d]+)\s+(?P<labels_ipv6>[\d]+)$')

        # Peer              GR Up Time         Discovery Address
        # ----------------- -- --------------- --------- -------
        # 10.36.3.3:0         Y  00:01:04                3       8
        # 10.16.2.2:0         N  00:01:02                2       5
        p2 = re.compile(r'^(?P<peer>[\d\.:]+) +(?P<gr>[\w]+) +(?P<up_time>[\d\:]+) +'
                         '(?P<discovery>(\d+)) +(?P<address>(\d+))$')

        # Peer               GR  NSR  Up Time     Discovery  Address  IPv4 Label
        # -----------------  --  ---  ----------  ---------  -------  ----------
        # 10.16.2.2:0          N   Y    01:39:50            1        4          19
        # 10.36.3.3:0          N   N    01:38:04            1        3           5
        p3 = re.compile(r'^(?P<peer>[\d\.:]+) +(?P<gr>(\w+)) +(?P<nsr>(\w+)) +(?P<up_time>[\d\:]+) +'
                         '(?P<discovery>(\d+)) +(?P<address>(\d+)) +(?P<labels_ipv4>(\d+))$')

        for line in out.splitlines():
            line = line.strip()

            # Peer               GR  NSR  Up Time     Discovery   Addresses     Labels
            #                                         ipv4  ipv6  ipv4  ipv6  ipv4   ipv6
            # -----------------  --  ---  ----------  ----------  ----------  ------------
            # 10.205.2.254:0     Y   Y    31w0d       2     0     10    0     77     0
            m = p1.match(line)
            if m:
                peer = m.groupdict()['peer']
                mpls_dict.setdefault('peer', {}).setdefault(peer, {})
                mpls_dict['peer'][peer]['gr'] = m.groupdict()['gr']
                mpls_dict['peer'][peer]['nsr'] = m.groupdict()['nsr']
                mpls_dict['peer'][peer]['up_time'] = m.groupdict()['up_time']

                mpls_dict['peer'][peer]['discovery'] = {}
                mpls_dict['peer'][peer]['discovery']['ipv4'] = int(m.groupdict()['discovery_ipv4'])
                mpls_dict['peer'][peer]['discovery']['ipv6'] = int(m.groupdict()['discovery_ipv6'])

                mpls_dict['peer'][peer]['addresses'] = {}
                mpls_dict['peer'][peer]['addresses']['ipv4'] = int(m.groupdict()['addresses_ipv4'])
                mpls_dict['peer'][peer]['addresses']['ipv6'] = int(m.groupdict()['addresses_ipv6'])

                mpls_dict['peer'][peer]['labels'] = {}
                mpls_dict['peer'][peer]['labels']['ipv4'] = int(m.groupdict()['labels_ipv4'])
                mpls_dict['peer'][peer]['labels']['ipv6'] = int(m.groupdict()['labels_ipv6'])
                continue

            # Peer              GR Up Time         Discovery Address
            # ----------------- -- --------------- --------- -------
            # 10.36.3.3:0         Y  00:01:04                3       8
            # 10.16.2.2:0         N  00:01:02                2       5
            m = p2.match(line)
            if m:
                peer = m.groupdict()['peer']
                gr = m.groupdict()['gr']
                up_time = m.groupdict()['up_time']
                discovery = int(m.groupdict()['discovery'])
                address = int(m.groupdict()['address'])

                peer_dict = mpls_dict.setdefault('peer', {}).setdefault(peer, {})
                peer_dict['gr'] = gr
                peer_dict['up_time'] = up_time

                discovery_dict = peer_dict.setdefault('discovery', {})
                discovery_dict['discovery'] = discovery

                address_dict = peer_dict.setdefault('addresses', {})
                address_dict['address'] = address

                continue

            # Peer               GR  NSR  Up Time     Discovery  Address  IPv4 Label
            # -----------------  --  ---  ----------  ---------  -------  ----------
            # 10.16.2.2:0          N   Y    01:39:50            1        4          19
            # 10.36.3.3:0          N   N    01:38:04            1        3           5
            m = p3.match(line)
            if m:
                peer = m.groupdict()['peer']
                gr = m.groupdict()['gr']
                nsr = m.groupdict()['nsr']
                up_time = m.groupdict()['up_time']
                discovery = int(m.groupdict()['discovery'])
                address = int(m.groupdict()['address'])
                labels_ipv4 = int(m.groupdict()['labels_ipv4'])

                peer_dict = mpls_dict.setdefault('peer', {}).setdefault(peer, {})
                peer_dict['gr'] = gr
                peer_dict['up_time'] = up_time
                peer_dict['nsr'] = nsr

                discovery_dict = peer_dict.setdefault('discovery', {})
                discovery_dict['discovery'] = discovery

                address_dict = peer_dict.setdefault('addresses', {})
                address_dict['address'] = address

                label_dict = peer_dict.setdefault('labels', {})
                label_dict['ipv4'] = labels_ipv4

                continue

        return mpls_dict


# ======================================================
# Schema for 'show mpls label table detail'
# ======================================================
class ShowMplsLabelTableDetailSchema(MetaParser):
    
    """Schema for 
    show mpls label table detail
    show mpls label table private
    """

    schema = {
        'table': {
            Any(): {
                'label': {
                    Any(): {
                        'owner': {
                            Any():{
                                'state': str,
                                'rewrite': str,
                            },
                        },
                        Optional('label_type'): {
                            Any(): {
                                Optional('vers'): int,
                                Optional('start_label'): int,
                                Optional('size'): int,
                                Optional('app_notify'): int,
                                Optional('index'): int,
                                Optional('type'): int,
                                Optional('interface'): str,
                                Optional('nh'): str,
                                Optional('default'): bool,
                                Optional('prefix'): str,
                            },
                        }
                    },
                }
            },
        }
    }


# ======================================================
# Parser for 'show mpls label table detail'
# ======================================================
class ShowMplsLabelTableDetail(ShowMplsLabelTableDetailSchema):

    """
    Parser for show mpls label table detail
    """
    cli_command = ['show mpls label table detail']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        # Init vars
        mpls_dict = {}
        table = ''

        # Table Label   Owner                           State  Rewrite
        # ----- ------- ------------------------------- ------ -------
        # 0     0       LSD(A)                          InUse  Yes
        # 0     16000   ISIS(A):SR                      InUse  No
        # 0     16001   LDP:lsd_test_ut                 InUse  No
        #               Static:lsd_test_ut              InUse  No
        p1 = re.compile(r'(?P<table>\d+\s+)?(?P<label>\d+\s+)?(?P<owner>[\S]+)'
        '\s+(?P<state>\S+)\s+(?P<rewrite>\w+)$')

        # (Lbl-blk SRGB, vers:0, (start_label=16000, size=8000)
        # (Lbl-blk SRLB, vers:0, (start_label=15000, size=1000, app_notify=0)
        p2 = re.compile(r'^\((?P<label_type>[\S\s]+),\s+vers:(?P<vers>\d+),'
            '\s+\(start_label=(?P<start_label>\d+),\s+size=(?P<size>\d+)'
            '(,\s+app_notify=(?P<app_notify>\d+))?\)$')

        # (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        p3 = re.compile(r'^\((?P<sr_label_type>[\S\s]+),\s+vers:(?P<vers>\d+),'
            '\s+index=(?P<index>\d+),\s+type=(?P<type>\d+),\s+intf=(?P<interface>\S+),'
            '\s+nh=(?P<nh>\S+)\)$')
            
        # (IPv4, vers:0, default, 10.4.1.1/24)
        # (IPv4, vers:0, , 10.229.10.10/15)
        p4 = re.compile(r'^\((?P<label_type>[\S\s]+),\s+vers:(?P<vers>\d+),'
        ' +(?P<default>default)?, +(?P<prefix>\S+)\)$')

        for line in out.splitlines():
            line = line.strip()

            # Table Label   Owner                           State  Rewrite
            # ----- ------- ------------------------------- ------ -------
            # 0     0       LSD(A)                          InUse  Yes
            # 0     16001   LDP:lsd_test_ut                 InUse  No
            #       Static:lsd_test_ut                      InUse  No
            m = p1.match(line)
            if m:
                label_list = ['state', 'rewrite']
                if (m.groupdict()['table']) and (m.groupdict()['label']):
                    table = int(m.groupdict()['table'].strip())
                    label = int(m.groupdict()['label'].strip())
                    final_dict = mpls_dict.setdefault('table', {}).\
                                setdefault(table, {}).\
                                setdefault('label', {}).\
                                setdefault(label, {}).\
                                setdefault('owner', {})
                
                owner_dict = final_dict.setdefault(m.groupdict()['owner'], {})
                for key in label_list:
                    owner_dict.update({key:m.groupdict()[key]})
                continue

            # (Lbl-blk SRGB, vers:0, (start_label=16000, size=8000)
            # (Lbl-blk SRLB, vers:0, (start_label=15000, size=1000, app_notify=0)
            m = p2.match(line)
            if m:
                label_type = m.groupdict()['label_type']
                latest_dict = mpls_dict.setdefault('table', {}).setdefault(table, {}).\
                        setdefault('label', {}).setdefault(label, {}).\
                            setdefault('label_type', {}).setdefault(label_type, {})
                label_list = ['vers', 'start_label', 'size']
                for key in label_list:
                    latest_dict.update({key:int(m.groupdict()[key])})
                if m.groupdict()['app_notify']:
                    latest_dict.update({'app_notify':int(m.groupdict()['app_notify'])})
                continue

            # (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
            m = p3.match(line)
            if m:
                label_type = m.groupdict()['sr_label_type']
                latest_dict = mpls_dict.setdefault('table', {}).setdefault(table, {}).\
                        setdefault('label', {}).setdefault(label, {}).\
                            setdefault('label_type', {}).setdefault(label_type, {})
                label_list = ['vers', 'index', 'type']
                for key in label_list:
                    latest_dict.update({key:int(m.groupdict()[key])})
                latest_dict.update({'interface':m.groupdict()['interface']})
                latest_dict.update({'nh':m.groupdict()['nh']})
                continue

            # (IPv4, vers:0, default, 10.4.1.1/24)
            # (IPv4, vers:0, , 10.229.10.10/15)
            m = p4.match(line)
            if m:
                label_type = m.groupdict()['label_type']
                latest_dict = mpls_dict.setdefault('table', {}).setdefault(table, {}).\
                        setdefault('label', {}).setdefault(label, {}).\
                            setdefault('label_type', {}).setdefault(label_type, {})
                latest_dict.update({'vers':int(m.groupdict()['vers'])})
                latest_dict.update({'default':True if m.groupdict()['default'] != None\
                    else False})
                latest_dict.update({'prefix':m.groupdict()['prefix']})

        return mpls_dict


# ======================================================
# Parser for 'show mpls label table private'
# ======================================================
class ShowMplsLabelTablePrivate(ShowMplsLabelTableDetail):

    """
    Parser for show mpls label table private
    """

    cli_command = ['show mpls label table private']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        return super().cli(output=out)


# ======================================================
# Schema for 'show mpls interfaces'
# ======================================================
class ShowMplsInterfacesSchema(MetaParser):
    schema = {
        'interfaces': {
            Any(): {
                'ldp': str,
                'tunnel': str,
                'static': str,
                'enabled': str,
            }
        },
    }


# ======================================================
# Parser for 'show mpls interfaces'
# ======================================================
class ShowMplsInterfaces(ShowMplsInterfacesSchema):
    cli_command = ['show mpls interfaces',
        'show mpls interfaces {interface}']

    def cli(self, interface=None, output=None):

        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(
                                          interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # GigabitEthernet0/0/0/0     No       No       No       Yes
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<ldp>No|Yes) +'
                r'(?P<tunnel>No|Yes) +(?P<static>No|Yes) +'
                r'(?P<enabled>No|Yes)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/0     No       No       No       Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.get('interface'))
                ldp = group.get('ldp')
                tunnel = group.get('tunnel')
                static = group.get('static')
                enabled = group.get('enabled')
                interface_dict = ret_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'ldp' : ldp})
                interface_dict.update({'tunnel': tunnel})
                interface_dict.update({'static': static})
                interface_dict.update({'enabled': enabled})
                continue

        return ret_dict


# ======================================================
# Schema for
#   * 'show mpls forwarding vrf {vrf}'
# ======================================================
class ShowMplsForwardingVrfSchema(MetaParser):
    schema = {
        'vrf': {
            Any(): {
                'local_label': {
                    Any(): {
                        'outgoing_label': {
                            Any(): {
                                'prefix_or_id': {
                                    Any(): {
                                        'outgoing_interface': {
                                            Any(): {
                                                Optional('next_hop'): str,
                                                'bytes_switched': int,
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================================
# Parser for
#   * 'show mpls forwarding vrf {vrf}'
# ======================================================
class ShowMplsForwardingVrf(ShowMplsForwardingVrfSchema):

    cli_command = ['show mpls forwarding vrf {vrf}']

    def cli(self, vrf, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0].format(vrf=vrf))
        else:
            out = output

        ret_dict = {}

        # 16001  Pop         SR Pfx (idx 1)     Gi0/0/0/0    10.1.3.1        0
        p1 = re.compile(r'^((?P<local_label>\d+) +)?(?P<outgoing_label>\S+) '
                        r'+(?P<prefix_or_id>.+?) +(?P<outgoing_interface>\S+) '
                        r'+(?P<next_hop>\S+) +(?P<bytes_switched>\d+)$')

        # 24006  Aggregate   VRF1: Per-VRF Aggr[V]   \
        p2 = re.compile(r'^(?P<local_label>\d+) +(?P<outgoing_label>\S+) '
                        r'+(?P<prefix_or_id>.+?) +\\$')

        # VRF1                         832
        p3 = re.compile(r'^(?P<outgoing_interface>\S+) +((?P<next_hop>\S+) +)?'
                        r'(?P<bytes_switched>\d+)$')

        # Gi0/0/0/0.390 fe80::f816:3eff:fe53:2cc7   \
        p4 = re.compile(r'^(?P<outgoing_interface>\S+) +(?P<next_hop>\S+) +\\$')

        # 3747484
        p5 = re.compile(r'^(?P<bytes_switched>\d+)$')

        pre_label = ''
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # 16001  Pop         SR Pfx (idx 1)     Gi0/0/0/0    10.1.3.1        0
            #        Unlabelled  10.13.90.0/24      Gi0/0/0/1.90 10.23.90.3      0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                local_label = group.get('local_label') or pre_label
                outgoing_label = group.get('outgoing_label')
                prefix_or_id = group.get('prefix_or_id').strip()
                outgoing_interface = Common.convert_intf_name(group.get('outgoing_interface'))
                next_hop = group.get('next_hop')
                bytes_switched = group.get('bytes_switched')

                local_label_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('local_label', {}).setdefault(local_label, {}). \
                    setdefault('outgoing_label', {}).setdefault(outgoing_label, {}). \
                    setdefault('prefix_or_id', {}).setdefault(prefix_or_id, {}). \
                    setdefault('outgoing_interface', {}).setdefault(outgoing_interface, {})

                if next_hop:
                    local_label_dict.update({'next_hop': next_hop})
                local_label_dict.update({'bytes_switched': int(bytes_switched)})

                pre_label = local_label or pre_label
                continue

            # 24006  Aggregate   VRF1: Per-VRF Aggr[V]   \
            m = p2.match(line)
            if m:
                group = m.groupdict()
                local_label = group.get('local_label') or pre_label
                outgoing_label = group.get('outgoing_label')
                prefix_or_id = group.get('prefix_or_id').strip()
                pre_label = local_label or pre_label
                continue

            # VRF1                         832
            m = p3.match(line)
            if m:
                group = m.groupdict()
                outgoing_interface = Common.convert_intf_name(
                    group.get('outgoing_interface'))
                next_hop = group.get('next_hop')
                bytes_switched = group.get('bytes_switched')

                local_label_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('local_label', {}).setdefault(local_label, {}). \
                    setdefault('outgoing_label', {}).setdefault(outgoing_label, {}). \
                    setdefault('prefix_or_id', {}).setdefault(prefix_or_id, {}). \
                    setdefault('outgoing_interface', {}).setdefault(outgoing_interface, {})

                if next_hop:
                    local_label_dict.update({'next_hop': next_hop})
                local_label_dict.update({'bytes_switched': int(bytes_switched)})
                continue

            # Gi0/0/0/0.390 fe80::f816:3eff:fe53:2cc7   \
            m = p4.match(line)
            if m:
                group = m.groupdict()
                outgoing_interface = Common.convert_intf_name(group.get('outgoing_interface'))
                next_hop = group.get('next_hop')
                continue

            # 3747484
            m = p5.match(line)
            if m:
                group = m.groupdict()
                bytes_switched = group.get('bytes_switched')

                local_label_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('local_label', {}).setdefault(local_label, {}). \
                    setdefault('outgoing_label', {}).setdefault(outgoing_label, {}). \
                    setdefault('prefix_or_id', {}).setdefault(prefix_or_id, {}). \
                    setdefault('outgoing_interface', {}).setdefault(outgoing_interface, {})

                if next_hop:
                    local_label_dict.update({'next_hop': next_hop})
                local_label_dict.update({'bytes_switched': int(bytes_switched)})
                continue

        return ret_dict


# ======================================================
# Schema for
#   * 'show mpls forwarding'
# ======================================================
class ShowMplsForwardingSchema(MetaParser):
    schema = {
        'local_label': {
            Any(): {
                'outgoing_label': {
                    Any(): {
                        'prefix_or_id': {
                            Any(): {
                                'outgoing_interface': {
                                    Any(): {
                                        Optional('next_hop'): str,
                                        'bytes_switched': int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================================
# Parser for 
#   * 'show mpls forwarding'
# ======================================================
class ShowMplsForwarding(ShowMplsForwardingSchema, ShowMplsForwardingVrf):

    cli_command = ['show mpls forwarding']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        vrf = 'default'
        ret_dict = super().cli(vrf=vrf, output=out).get(
                    'vrf', {}).get('default', {})

        return ret_dict


# ======================================================
# Parser for 'show mpls ldp bindings'
# ======================================================
class ShowMplsLdpBindingsSchema(MetaParser):

    """Schema for 'show mpls ldp bindings' """

    schema =  {
        'lib_entry': {
            Any(): {
                'rev': int,
                'local_binding': {
                    'label': str
                },
                Optional('remote_bindings'): {
                    Optional('peer_count'): int,
                    'label': {
                        Any(): { 
                            'lsr_id': {
                                Any(): {
                                    'label': str,
                                    'lsr_id': str
                                }
                            }
                        }
                    },
                }
            }
        }
    }

class ShowMplsLdpBindings(ShowMplsLdpBindingsSchema):

    """ Parser for 'show mpls ldp bindings' """

    cli_command = ['show mpls ldp bindings']

    def cli (self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        
        # intialize bindings dictionary for parsed results
        result_dict = {}

        # 10.145.95.95/32, rev 20
        # 10.9.9.98/32 , rev 6 
        p1 = re.compile(r'^(?P<lib_entry>[\d\.\/]+) ?, +rev +(?P<rev>\d+)')
        
        # Local binding: label: ImpNull
        # local binding: label:IMP-NULL
        p2 = re.compile(r'^[lL]ocal +binding: +label: ?(?P<local_label>\S+)')
        
        # Remote bindings: (2 peers)
        # remote bindings : 
        p3 = re.compile(r'^[rR]emote +bindings ?:(?: +\((?P<peer_count>\d+) +peers\))?')
        
        # 10.145.95.95:0       16002
        # lsr:10.255.255.255:0, label:16 
        p4 = re.compile(r'^(?:lsr:)?(?P<lsr_id>[\d\.\:]+),? +(?:label:)?(?P<remote_label>\S+)')
        

        for line in output.splitlines():
            line = line.strip() # strip whitespace from beginning and end

            # 10.145.95.95/32, rev 20
            # 10.9.9.98/32 , rev 6 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lib_entry_dict = result_dict.setdefault('lib_entry', {}).setdefault(group['lib_entry'], {})
                lib_entry_dict.update({'rev': int(group['rev'])})
                continue
            
            # Local binding: label: ImpNull
            # local binding: label:IMP-NULL
            m = p2.match(line)
            if m:
                group = m.groupdict()
                local_dict = lib_entry_dict.setdefault('local_binding', {})
                local_dict.update({'label': group['local_label']})
                continue
                
            # Remote bindings: (2 peers)
            # remote bindings : 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                remote_dict = lib_entry_dict.setdefault('remote_bindings', {})
                if group['peer_count']: 
                    remote_dict.update({'peer_count': int(group['peer_count'])})
                continue

            # 10.145.95.95:0       16002
            # lsr:10.255.255.255:0, label:16 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                    
                lsr_id = remote_dict.setdefault('label', {}).\
                            setdefault(group['remote_label'],{}).\
                            setdefault('lsr_id', {}).\
                            setdefault(group['lsr_id'],{})
                            
                lsr_id.update({'label': group['remote_label']})
                lsr_id.update({'lsr_id': group['lsr_id']})
                continue
                
            
        return result_dict


# ==============================================
#  Schema for show mpls ldp parameters
# ==============================================

class ShowMplsLdpParametersSchema(MetaParser):
    """ Schema for
        * show mpls ldp parameters
    """
    schema = {
        "ldp-parameters": {
            "role": str,
            "protocol-version": str,
            "router-id": str,
            "null-label": {
                "null-label-ipv4-address": str
            },
            "session": {
                "session-holdtime-sec": int,
                "session-keepalive-interval-sec": int,
                "session-backoff": {
                    "backoff-initial-sec": int,
                    "backoff-maximum-sec": int
                },
                "global-md5-password": str
            },
            "discovery": {
                "discovery-link-hellos": {
                    "link-hellos-hold-time-sec": int,
                    "link-hellos-interval-sec": int
                },
                "discovery-target-hellos": {
                    "target-hellos-hold-time-sec": int,
                    "target-hellos-interval-sec": int
                },
                "discovery-quick-start": str,
                "discovery-transport-address": {
                    "transport-ipv4-address": str
                },
            },
            "graceful-restart": {
                "graceful-restart-status": str,
                "graceful-restart-reconnect-timeout": {
                    "reconnect-timeout-time-sec": int,
                    "reconnect-timeout-forward-state-holdtime-sec": int
                }
            },
            "nsr": {
                "nsr-status": str,
                Optional("nsr-sync-ed-status"): str
            },
            "timeouts": {
                "housekeeping-periodic-timer-timeouts-sec": int,
                "local-binding-timeouts-sec": int,
                "forward-state-lsd-timeouts-sec": int
            },
            "delay-af-bind-peer-sec": int,
            "max": {
                "interfaces": {
                    "max-interfaces-units": int,
                    Optional("attached-interfaces-units"): int,
                    Optional("te-tunnel-interfaces-units"): int
                },
                "max-peers-units": int
            },
            "oor-state": {
                "oor-memory": str
            },
        },
    }


# ==============================================
#  Parser for show mpls ldp parameters
# ==============================================

class ShowMplsLdpParameters(ShowMplsLdpParametersSchema):
    """ For Parsing
        * show mpls ldp parameters
    """

    cli_command = 'show mpls ldp parameters'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # LDP Parameters:
        p1 = re.compile(r'^LDP +Parameters:$')

        # Role: Active
        p2 = re.compile(r'^Role: +(?P<role_value>\w+)$')

        # Protocol Version: 1
        p3 = re.compile(r'^Protocol +Version: +(?P<protocol_version_number>\S+)$')

        # Router ID: 10.4.1.1
        p4 = re.compile(r'^Router +ID: +(?P<router_id_ip>[\d.]+)$')

        # Null Label:
        p5 = re.compile(r'^Null +Label:$')

        # IPv4: Implicit
        p6 = re.compile(r'^IPv4: +(?P<null_labels_ipv4>\w+)$')

        # Session:
        p7 = re.compile(r'^Session:$')

        # Hold time: 180 sec
        p8 = re.compile(r'^Hold +time: +(?P<hold_time_seconds>\d+) +sec$')

        # Keepalive interval: 60 sec
        p9 = re.compile(r'^Keepalive +interval: +(?P<keepalive_interval_seconds>\d+) +sec$')

        # Backoff: Initial:15 sec, Maximum:120 sec
        p10 = re.compile(
            r'^Backoff: +Initial:(?P<initial_seconds>\d+) +sec'
            r', +Maximum:(?P<maximum_seconds>\d+) +sec$')

        # Global MD5 password: Disabled
        p11 = re.compile(
            r'^Global +MD5 +password: +(?P<global_md5_password>\w+)$')

        # Discovery:
        p12 = re.compile(r'^Discovery:$')

        # Link Hellos: Holdtime:15 sec, Interval:5 sec
        p13 = re.compile(
            r'^Link +Hellos: +Holdtime:(?P<link_hellos_hold_time_seconds>\d+) +sec,'
            r' +Interval:(?P<link_hellos_interval_seconds>\d+) +sec$')

        # Targeted Hellos: Holdtime:90 sec, Interval:10 sec
        p14 = re.compile(
            r'^Targeted +Hellos: +Holdtime:(?P<targeted_hellos_hold_time_seconds>\d+) +sec'
            r', +Interval:(?P<targeted_hellos_interval_seconds>\d+) +sec$')

        # Quick-start: Enabled (by default)
        p15 = re.compile(r'^Quick-start: +(?P<quick_start>.*)$')

        # Transport address:
        p16 = re.compile(r'^Transport +address:$')

        # IPv4: 10.4.1.1
        p17 = re.compile(r'^IPv4: +(?P<transport_address_ipv4_ip>[\d.]+)$')

        # Graceful Restart:
        p18 = re.compile(r'^Graceful +Restart:$')

        # Enabled
        p19 = re.compile(r'^(?P<graceful_restart_value>(Enabled|Disabled))$')

        # Reconnect Timeout:120 sec, Forwarding State Holdtime:180 sec
        p20 = re.compile(
            r'^Reconnect +Timeout:(?P<reconnect_timeout_seconds>\d+) +sec,'
            r' +Forwarding +State +Holdtime:(?P<forwarding_state_holdtime_seconds>\d+) +sec$')

        # NSR: Enabled, Sync-ed
        p21 = re.compile(r'^NSR: +(?P<nsr_value>\w+)(, +(?P<synced_value>Sync-ed))?$')

        # Timeouts:
        p22 = re.compile(r'^Timeouts:$')

        # Housekeeping periodic timer: 10 sec
        p23 = re.compile(
            r'^Housekeeping +periodic +timer: +(?P<housekeeping_periodic_timer_seconds>\d+) +sec$')

        # Local binding: 300 sec
        p24 = re.compile(r'^Local +binding: +(?P<local_binding_seconds>\d+) +sec$')

        # Forwarding state in LSD: 360 sec
        p25 = re.compile(
            r'^Forwarding +state +in +LSD: +(?P<forwarding_state_lsd_seconds>\d+) +sec$')

        # Delay in AF Binding withdrawl from peer: 180 sec
        p26 = re.compile(
            r'^Delay +in +AF +Binding +Withdrawl +from +peer:'
            r' +(?P<delay_af_binding_peer_seconds>\d+) +sec$')

        # Max:
        p27 = re.compile(r'^Max:$')

        # 5000 interfaces (4000 attached, 1000 TE tunnel), 2000 peers
        p28 = re.compile(
            r'^(?P<max_interface_number>\d+) +interfaces(,| )(\(| )'
            r'((?P<attached_interfaces_number>\d+) +attached(\)|,))?'
            r'((,| )*)?((?P<te_tunnel_number>\d+) +TE +tunnel\))?((,| )*)?((?P<peers_number>\d+) +peers)?')

        # OOR state
        p29 = re.compile(r'^OOR +state$')

        # Memory: Normal
        p30 = re.compile(
            r'^Memory: +(?P<oor_memory_value>(Normal|Major|Critical))$')

        # Looping through each line
        for line in out.splitlines():
            line = line.strip()

            # LDP Parameters:
            m = p1.match(line)
            if m:
                parameters_dict = ret_dict.setdefault('ldp-parameters', {})
                continue

            # Role: Active
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['role'] = group['role_value']
                continue

            # Protocol Version: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['protocol-version'] = group['protocol_version_number']
                continue

            # Router ID: 10.4.1.1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['router-id'] = group['router_id_ip']
                continue

            # Null Label:
            m = p5.match(line)
            if m:
                null_label_dict = parameters_dict.setdefault('null-label', {})
                continue

            # ipv4: Implicit
            m = p6.match(line)
            if m:
                group = m.groupdict()
                null_label_dict['null-label-ipv4-address'] = group['null_labels_ipv4']
                continue

            # Session:
            m = p7.match(line)
            if m:
                session_dict = parameters_dict.setdefault('session', {})
                continue

            # Hold time: 180 sec
            m = p8.match(line)
            if m:
                group = m.groupdict()
                session_dict['session-holdtime-sec'] = int(group['hold_time_seconds'])
                continue

            # Keepalive interval: 60 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                session_dict['session-keepalive-interval-sec'] = int(group['keepalive_interval_seconds'])
                continue

            # Backoff: Initial:15 sec, Maximum:120 sec
            m = p10.match(line)
            if m:
                group = m.groupdict()
                backoff_dict = session_dict.setdefault('session-backoff', {})
                backoff_dict['backoff-initial-sec'] = int(group['initial_seconds'])
                backoff_dict['backoff-maximum-sec'] = int(group['maximum_seconds'])
                continue

            # Global MD5 password: Disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                session_dict['global-md5-password'] = group['global_md5_password']
                continue

            # Discovery:
            m = p12.match(line)
            if m:
                discovery_dict = parameters_dict.setdefault('discovery', {})
                continue

            # Link Hellos: Holdtime:15 sec, Interval:5 sec
            m = p13.match(line)
            if m:
                group = m.groupdict()
                link_hellos_dict = discovery_dict.setdefault('discovery-link-hellos', {})
                link_hellos_dict['link-hellos-hold-time-sec'] = int(group['link_hellos_hold_time_seconds'])
                link_hellos_dict['link-hellos-interval-sec'] = int(group['link_hellos_interval_seconds'])
                continue

            # Targeted Hellos: Holdtime:90 sec, Interval:10 sec
            m = p14.match(line)
            if m:
                group = m.groupdict()
                target_hellos_dict = discovery_dict.setdefault('discovery-target-hellos', {})
                target_hellos_dict['target-hellos-hold-time-sec'] = int(group['targeted_hellos_hold_time_seconds'])
                target_hellos_dict['target-hellos-interval-sec'] = int(group['targeted_hellos_interval_seconds'])
                continue

            # Quick-start: Enabled (by default)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                discovery_dict['discovery-quick-start'] = group['quick_start']
                continue

            # Transport address:
            m = p16.match(line)
            if m:
                transport_address_dict = discovery_dict.setdefault('discovery-transport-address', {})
                continue

            # IPv4: 10.4.1.1
            m = p17.match(line)
            if m:
                group = m.groupdict()
                transport_address_dict['transport-ipv4-address'] = group['transport_address_ipv4_ip']
                continue

            # Graceful Restart:
            m = p18.match(line)
            if m:
                graceful_restart_dict = parameters_dict.setdefault('graceful-restart', {})
                continue

            # Enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                graceful_restart_dict['graceful-restart-status'] = group['graceful_restart_value']
                continue

            # Reconnect Timeout:120 sec, Forwarding State Holdtime:180 sec
            m = p20.match(line)
            if m:
                group = m.groupdict()
                reconnect_timeout_dict =\
                    graceful_restart_dict.setdefault('graceful-restart-reconnect-timeout', {})
                reconnect_timeout_dict['reconnect-timeout-time-sec'] =\
                    int(group['reconnect_timeout_seconds'])
                reconnect_timeout_dict['reconnect-timeout-forward-state-holdtime-sec'] =\
                    int(group['forwarding_state_holdtime_seconds'])
                continue

            # NSR: Enabled, Sync-ed
            m = p21.match(line)
            if m:
                group = m.groupdict()
                nrs_dict = parameters_dict.setdefault('nsr', {})
                nrs_dict['nsr-status'] = group['nsr_value']

                if group['synced_value']:
                    nrs_dict['nsr-sync-ed-status'] = group['synced_value']
                continue

            # Timeouts:
            m = p22.match(line)
            if m:
                timeouts_dict = parameters_dict.setdefault('timeouts', {})
                continue

            # Housekeeping periodic timer: 10 sec
            m = p23.match(line)
            if m:
                group = m.groupdict()
                timeouts_dict['housekeeping-periodic-timer-timeouts-sec'] =\
                    int(group['housekeeping_periodic_timer_seconds'])
                continue

            # Local binding: 300 sec
            m = p24.match(line)
            if m:
                group = m.groupdict()
                timeouts_dict['local-binding-timeouts-sec'] =\
                    int(group['local_binding_seconds'])
                continue

            # Forwarding state in LSD: 360 sec
            m = p25.match(line)
            if m:
                group = m.groupdict()
                timeouts_dict['forward-state-lsd-timeouts-sec'] =\
                    int(group['forwarding_state_lsd_seconds'])
                continue

            # Delay in AF Binding Withdrawl from peer: 180 sec
            m = p26.match(line)
            if m:
                group = m.groupdict()
                parameters_dict['delay-af-bind-peer-sec'] =\
                    int(group['delay_af_binding_peer_seconds'])
                continue

            # Max:
            m = p27.match(line)
            if m:
                max_dict = parameters_dict.setdefault('max', {})
                continue

            # 5000 interfaces (4000 attached, 1000 TE tunnel), 2000 peers
            m = p28.match(line)
            if m:
                group = m.groupdict()

                max_interfaces_dict = max_dict.setdefault('interfaces', {})
                max_interfaces_dict['max-interfaces-units'] =\
                    int(group['max_interface_number'])

                if group['attached_interfaces_number']:
                    max_interfaces_dict['attached-interfaces-units'] =\
                        int(group['attached_interfaces_number'])

                if group['te_tunnel_number']:
                    max_interfaces_dict['te-tunnel-interfaces-units'] = \
                        int(group['te_tunnel_number'])

                max_dict['max-peers-units'] = \
                    int(group['peers_number'])
                continue

            # OOR state
            m = p29.match(line)
            if m:
                oor_state_dict = parameters_dict.setdefault('oor-state', {})
                continue

            # Memory: Normal
            m = p30.match(line)
            if m:
                group = m.groupdict()
                oor_state_dict['oor-memory'] = group['oor_memory_value']
                continue

        return ret_dict


# ================================================
#   Show mpls ldp igp sync
# ================================================
class ShowMplsLdpIgpSyncSchema(MetaParser):
    """
    Schema for show mpls ldp igp sync
    """
    schema = {
        'vrf': {
            Any(): {
                Optional('vrf_index'): str,
                'interfaces': {
                    Any(): {
                        Optional('sync'): {
                        Optional('status'): str,
                        Optional('delay'): str,
                        Optional('peers'):{
                            Any():{
                                Optional('graceful_restart'): bool
                            }
                          }
                        }
                    },
                },
            },
        }
    }

class ShowMplsLdpIgpSync(ShowMplsLdpIgpSyncSchema):
    """
        Parser for show mpls ldp igp sync
    """
    cli_command = ['show mpls ldp igp sync']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Vrf is default
        vrf = "default"

        # initial return dictionary
        ret_dict = {}

        # HundredGigE0/0/0/0:
        p1 = re.compile(r'^(?P<interface>[\w]+[\/\d]+):$')

        # VRF: 'default' (0x60000000)
        p2 = re.compile(r'^VRF:\s+\'(?P<vrf>\S+)\'\s+\((?P<vrf_index>.+)\)$')

        # Sync delay: Disabled
        p3 = re.compile(r'^Sync +delay:\s+(?P<delay>\S+)$')

        # Sync status: Ready
        p4 = re.compile(r'^Sync +status:\s+(?P<status>.+)$')

        # 63.63.63.63:0   (GR)
        p5 = re.compile(r'^(?P<peers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,3})\s+?(?P<gr_flag>\(GR\))?$')

        for line in out.splitlines():
            line = line.strip()


            # HundredGigE0/0/0/0:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                continue

            # VRF: 'default' (0x60000000)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {})
                interface_dict = vrf_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                vrf_dict.update({'vrf_index': group['vrf_index']})
                continue

            # Sync delay: Disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sync_dict = interface_dict.setdefault('sync', {})
                sync_dict.update({'delay': group['delay']})
                continue

            # Sync status: Ready
            m = p4.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                sync_status_dict = sync_dict.setdefault('status', status)
                continue

            # 63.63.63.63:0   (GR)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                peers = group['peers']
                peers_dict = sync_dict.setdefault('peers', {}).\
                    setdefault(peers, {})

                if group['gr_flag']:
                    gr_flag = True
                    peers_dict.update({'graceful_restart': gr_flag})
                continue

        return ret_dict


# ================================================
#   show mpls ldp graceful-restart
# ================================================
class ShowMplsLdpGracefulRestartSchema(MetaParser):
    """
    Schema for show mpls ldp graceful-restart
    """
    schema = {
        'vrf': {
            'default': {
                'forwarding_state_hold_timer': str,
                'gr_neighbors': int,
                'neighbor_id': {
                    Any(): {
                        Optional('up'): str,
                        Optional('connect_count'): str,
                        Optional('liveness_timer'): str,
                        Optional('recovery_timer'): str
                        }
                    },
                },
            },
        }


class ShowMplsLdpGracefulRestart(ShowMplsLdpGracefulRestartSchema):
    """
        Parser for show mpls ldp graceful-restart
    """
    cli_command = ['show mpls ldp graceful-restart']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Forwarding State Hold timer : Not Running
        p1 = re.compile(r'^Forwarding +State +Hold +timer\s+:\s+(?P<state_hold_timer>.+)$')

        # GR Neighbors                : 1
        p2 = re.compile(r'^GR +Neighbors\s+:\s+(?P<gr_neighbors>.+)$')

        # 17.17.17.17      Y        4                -                   -
        # 17.17.17.17      Y        4                5                   6
        p3 = re.compile(r'^(?P<neighbor_id>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<up>\w+)\s+'
                        r'(?P<connect_count>[\d\-]+)\s+(?P<liveness_timer>[\d\-]+)\s+'
                        r'(?P<recovery_timer>[\d\-]+)$')


        for line in out.splitlines():
            line = line.strip()

            # Forwarding State Hold timer : Not Running
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault('default', {})
                vrf_dict.update({'forwarding_state_hold_timer': group['state_hold_timer']})
                continue

            # GR Neighbors                : 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict.update({'gr_neighbors': int(group['gr_neighbors'])})

            # 17.17.17.17      Y        4                -                   -
            # 17.17.17.17      Y        4                5                   6
            m = p3.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict = vrf_dict.setdefault('neighbor_id', {}).\
                    setdefault(group['neighbor_id'], {})

                neighbor_dict.update({
                    'up': group['up'],
                    'connect_count': group['connect_count'],
                    'liveness_timer': group['liveness_timer'],
                    'recovery_timer': group['recovery_timer']
                })

        return ret_dict

# ================================================
#   show mpls ldp nsr summary
# ================================================
class ShowMplsLdpNsrSummarySchema(MetaParser):
    """
    Schema for show mpls ldp nsr summary
    """
    schema = {
        'sessions': {
            'total': int,
            'nsr_eligible': int,
            'sync_ed': int,
            Optional('oper'): int,
            Optional('ready'): int
        }
    }

class ShowMplsLdpNsrSummary(ShowMplsLdpNsrSummarySchema):
    """
        Parser for show mpls ldp nsr summary
    """
    cli_command = ['show mpls ldp nsr summary']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Total: 1, NSR-eligible: 1, Sync-ed: 1
        p1 = re.compile(r'^Total:\s+(?P<total>\d+)\,\s+NSR-eligible:\s+'
                        r'(?P<nsr_eligible>\d+)\,\s+Sync-ed:\s+(?P<sync_ed>\d+)$')

        # (1 Oper)
        p2 = re.compile(r'^\((?P<oper>\d+)\s+Oper\)$')

        # (1 Ready)
        p3 = re.compile(r'^\((?P<ready>\d+)\s+Ready\)$')

        for line in out.splitlines():
            line = line.strip()

            # Total: 1, NSR-eligible: 1, Sync-ed: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sessions_dict = ret_dict.setdefault('sessions', {})
                sessions_dict.update({
                 'total': int(group['total']),
                 'nsr_eligible': int(group['nsr_eligible']),
                 'sync_ed': int(group['sync_ed'])
                })
                continue

            # (1 Oper)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sessions_dict.update({'oper': int(group['oper'])})
                continue

            # (1 Ready)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                sessions_dict.update({'ready': int(group['ready'])})
                continue

        return ret_dict


# ======================================================
# Schema for 'show mpls traffic-eng tunnels tabular'
# ======================================================
class ShowMplsTrafficEngTunnelsTabularSchema(MetaParser):
    """Schema for
    show mpls traffic-eng tunnels tabular
    """

    schema = {
        'vrf': {
            Any(): {
                'tunnel': {
                    Any(): {
                        'lsp_id': int,
                        'destination_address': str,
                        'source_address': str,
                        'tunnel_state': str,
                        'frr_state': str,
                        'lsp_role': str,
                        Optional('path_prot'): str
                        }
                    },
                }
            },
        }

class ShowMplsTrafficEngTunnelsTabular(ShowMplsTrafficEngTunnelsTabularSchema):
    """
        Parser for show mpls traffic-eng tunnels tabular
    """
    cli_command = ['show mpls traffic-eng tunnels tabular']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # tunnel-te50000     4 109.109.109.109     17.17.17.17     up  Ready Head Inact
        p1 = re.compile(r'^(?P<tunnel>\S+)\s+(?P<lsp_id>\d+)\s+(?P<destination_address>\S+)\s+'
                        r'(?P<source_address>\S+)\s+(?P<tunnel_state>\w+)\s+(?P<frr_state>\w+)\s+'
                        r'(?P<lsp_role>\w+)[\s+]?(?P<path_prot>[\w]+)?$')

        for line in out.splitlines():
            line = line.strip()

            # tunnel-te50000     4 109.109.109.109     17.17.17.17     up  Ready Head Inact
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tunnel = group.pop('tunnel')
                lsp_id = int(group.pop('lsp_id'))
                vrf_dict = ret_dict.setdefault('vrf', {}).setdefault('default', {})
                tunnel_dict = vrf_dict.setdefault('tunnel', {}).\
                    setdefault(tunnel, {})
                tunnel_dict.update({'lsp_id': lsp_id})
                tunnel_dict.update(
                    {k: v for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


# ======================================================
# Schema for 'show mpls traffic-eng tunnels {tunnel_id}'
# ======================================================
class ShowMplsTrafficEngTunnelsTunnelidSchema(MetaParser):
    """Schema for
    show mpls traffic-eng tunnels {tunnel_id}
    """

    schema = {
        'tunnel': {
            Any(): {
                'destination': str,
                'ifhandle': str,
                'signalled_name': str,
                'status':{
                    'admin': str,
                    'oper': str,
                    'path': str,
                    'signalling': str,
                    Optional('path_option'): {
                        Optional(Any()): {
                            Optional('type'): str,
                            Optional('path_weight'): int,
                            Optional('accumulative_metrics'): {
                                Optional('te'): int,
                                Optional('igp'): int,
                                Optional('path'): int,
                            }
                        }
                    },
                    Optional('last_pcalc_error'): {
                        'time': str,
                        'info': str,
                        'reverselink': str
                    },
                    'g_pid': str,
                    'bandwidth_requested': int,
                    'bandwidth_requested_unit': str,
                    'creation_time': str,
                },
                'config_parameters': {
                    'bandwidth': int,
                    'bandwidth_unit': str,
                    'priority': int,
                    'affinity': str,
                    'metric_type': str,
                    'path_selection': {
                        'tiebreaker': str
                    },
                    'hop_limit': str,
                    'cost_limit': str,
                    'delay_limit': str,
                    'delay_measurement': str,
                    'path_invalidation_timeout': int,
                    'path_invalidation_timeout_unit': str,
                    'action': str,
                    'autoroute': str,
                    'lockdown': str,
                    'policy_class': str,
                    'forward_class': int,
                    'forward_class_state': str,
                    'forwarding_adjacency': str,
                    'autoroute_destinations': int,
                    'loadshare': int,
                    'loadshare_state': str,
                    'auto_bw': str,
                    'auto_capacity': str,
                    'fast_reroute': str,
                    'protection_desired': str,
                    'path_protection': str,
                    'bfd_fast_detection': str,
                    'reoptimization_after_affinity_failure': str,
                    'soft_preemption': str,
                },
                'history': {
                    'tunnel_up_time': str,
                    'current_lsp': {
                        'uptime': str
                    },
                    'reopt_lsp': {
                        'lsp_failure': {
                            'lsp': str,
                            'lsp_status': str,
                            'date_time': str
                        }
                    },
                    'prior_lsp': {
                        'id': int,
                        'path_option': int,
                        'removal_trigger': str
                    }
                },
                'path_info': {
                    Any():{
                        'node_hop_count': int,
                        'hop': {
                            Any(): {
                                'ip_address': str
                            }
                        }
                    }
                },
                'displayed': {
                    'heads_displayed': int,
                    'total_heads': int,
                    'midpoints_displayed': int,
                    'total_midpoints': int,
                    'tails_displayed': int,
                    'total_tails': int,
                    'status': {
                        'up': int,
                        'down': int,
                        'recovering': int,
                        'recovered_heads': int
                    }
                }
            }
        }
    }

class ShowMplsTrafficEngTunnelsTunnelid(ShowMplsTrafficEngTunnelsTunnelidSchema):
    """
        Parser for show mpls traffic-eng tunnels {tunnel_id}
    """
    cli_command = ['show mpls traffic-eng tunnels {tunnel_id}']

    def cli(self, output=None, tunnel_id=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(tunnel_id=tunnel_id))
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Name: tunnel-te50000  Destination: 109.109.109.109  Ifhandle:0x20e0
        p1 = re.compile(r'^Name:\s+(?P<tunnel>\S+)\s+Destination:\s+(?P<destination>\S+)'
                        r'\s+Ifhandle:(?P<ifhandle>\S+)$')

        # Signalled-Name: 50000_F17-ASR9922_F109-ASR9001
        p2 = re.compile(r'^Signalled-Name:\s+(?P<signalled_name>\S+)$')

        # Admin:    up Oper:   up   Path:  valid   Signalling: connected
        p3 = re.compile(r'^Admin:\s+(?P<admin>\S+)\s+Oper:\s+(?P<oper>\S+)\s+Path:\s+(?P<path>\S+)'
                        r'\s+Signalling:\s+(?P<signalling>\S+)$')

        # path option 10,  type explicit 50000-EPath_10 (Basis for Setup, path weight 160)
        p4 = re.compile(r'^path +option\s+(?P<path_option>\d+),\s+type\s+(?P<type>\S+)'
                        r'\s+?(?P<path_name>\S+)?\s+\((?P<path_status>.*),\s+path weight\s+(?P<path_weight>\d+)\)$')

        # path option 20,  type explicit 50000-EPath_20
        # path option 100,  type dynamic
        p4_1 = re.compile(r'^path +option\s+(?P<path_option>\d+),\s+type\s+(?P<type>\S+)'
                          r'[\s+]?(?P<path_name>\S+)?$')

        # Accumulative metrics: TE 160 IGP 160 Delay 600000
        p5 = re.compile(r'^Accumulative +metrics:\s+TE\s+(?P<te>\d+)\s+IGP\s+'
                        r'(?P<igp>\d+)\s+Delay\s+(?P<path>\d+)$')

        # Last PCALC Error: Tue Apr 27 16:21:21 2021
        p6 = re.compile(r'^Last PCALC Error:(?P<last_pcalc_error>.+)$')

        # Info: No path to destination, 109.109.109.109 (reverselink)
        p7 = re.compile(r'^Info:\s+(?P<info>.*)\, (?P<reverselink>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+$')

        # G-PID: 0x0800 (derived from egress interface properties)
        p8 = re.compile(r'^G-PID:\s+(?P<g_pid>\S+).+$')

        # Bandwidth Requested: 0 kbps  CT0
        p9 = re.compile(r'^Bandwidth Requested:\s+(?P<bandwidth_requested>\S+)\s+'
                        r'(?P<bandwidth_requested_unit>\S+).+$')

        # Creation Time: Tue Apr 27 16:21:14 2021 (01:36:30 ago)
        p10 = re.compile(r'^Creation Time:\s+(?P<creation_time>.+)$')

        # Bandwidth:        0 kbps (CT0) Priority:  3  3 Affinity: 0x0/0xffff
        p11 = re.compile(r'^Bandwidth:\s+(?P<bandwidth>\d+)\s+(?P<bandwidth_unit>\S+)'
                         r'.*Priority:\s+(?P<priority>\d+).*Affinity:\s+(?P<affinity>\S+)$')

        # Metric Type: IGP (interface)
        p12 = re.compile(r'^Metric Type:\s+(?P<metric_type>.+)$')

        # Tiebreaker: Min-fill (default)
        p13 = re.compile(r'^Tiebreaker:\s+(?P<tiebreaker>.+)$')

        # Hop-limit: disabled
        p14 = re.compile(r'^Hop-limit:\s+(?P<hop_limit>.+)$')

        # Cost-limit: disabled
        p15 = re.compile(r'^Cost-limit:\s+(?P<cost_limit>.+)$')

        # Delay-limit: disabled
        p16 = re.compile(r'^Delay-limit:\s+(?P<delay_limit>.+)$')

        # Delay-measurement: disabled
        p17 = re.compile(r'^Delay-measurement:\s+(?P<delay_measurement>.+)$')

        # Path-invalidation timeout: 10000 msec (default), Action: Tear (default)
        p18 = re.compile(r'^Path-invalidation timeout:\s+(?P<timeout>\d+)\s+(?P<timeout_unit>\S+)'
                         r'.*,\s+Action:\s+(?P<action>\S+).+$')

        # AutoRoute:  enabled  LockDown: disabled   Policy class: not set
        p19 = re.compile(r'^AutoRoute:\s+(?P<autoroute>\S+)\s+LockDown:\s+(?P<lockdown>.+)\s+'
                         r'Policy class:\s+(?P<policy_class>.+)$')

        # Forward class: 0 (not enabled)
        p20 = re.compile(r'^Forward class:\s+(?P<forward_class>\S+)\s+\((?P<forward_class_state>.+)?\)$')

        # Forwarding-Adjacency: disabled
        p21 = re.compile(r'^Forwarding-Adjacency:\s+(?P<forwarding_adjacency>.+)$')

        # Autoroute Destinations: 0
        p22 = re.compile(r'^Autoroute Destinations:\s+(?P<autoroute_destinations>.+)$')

        # Loadshare:          0 equal loadshares
        p23 = re.compile(r'^Loadshare:\s+(?P<loadshare>\d+)\s+(?P<loadshare_state>.+)$')

        # Auto-bw: disabled
        p24 = re.compile(r'^Auto-bw:\s+(?P<auto_bw>.+)$')

        # Auto-Capacity: Disabled:
        p25 = re.compile(r'^Auto-Capacity:\s+(?P<auto_capacity>\w+)\:?$')

        # Fast Reroute: Enabled, Protection Desired: Any
        p26 = re.compile(r'^Fast Reroute:\s+(?P<fast_reroute>\S+), Protection Desired:'
                         r'\s+(?P<protection_desired>.+)$')

        # Path Protection: Not Enabled
        p27 = re.compile(r'^Path Protection:\s+(?P<path_protection>.+)$')

        # BFD Fast Detection: Disabled
        p28 = re.compile(r'^BFD Fast Detection:\s+(?P<bfd_fast_detection>.+)$')

        # Reoptimization after affinity failure: Enabled
        p29 = re.compile(r'^Reoptimization after affinity failure:\s+(?P<reoptimization>.+)$')

        # Soft Preemption: Disabled
        p30 = re.compile(r'^Soft Preemption:\s+(?P<soft_preemption>.+)$')

        # Tunnel has been up for: 01:36:23 (since Tue Apr 27 16:21:21 JST 2021)
        p31 = re.compile(r'^Tunnel has been up for:\s+(?P<tunnel_up_time>.+)$')

        # Uptime: 00:26:32 (since Tue Apr 27 17:31:12 JST 2021)
        p32 = re.compile(r'^Uptime:\s+(?P<uptime>.+)$')

        # LSP not signalled, identical to the [CURRENT] LSP
        p33 = re.compile(r'^LSP\s+(?P<lsp>.+),\s+(?P<lsp_status>.+)$')

        # Date/Time: Tue Apr 27 16:26:11 JST 2021 [01:31:33 ago]
        p34 = re.compile(r'^Date/Time:\s+(?P<date_time>.+)$')

        # ID: 5 Path Option: 20
        p35 = re.compile(r'^ID:\s+(?P<id>\d+)\s+Path Option:\s+(?P<path_option>\d+)$')

        # Removal Trigger: reoptimization completed
        p36 = re.compile(r'^Removal Trigger:\s+(?P<removal_trigger>.+)$')

        # Path info (OSPF mpls1 area 0):
        p37 = re.compile(r'^Path info \((?P<path_info>.+)\):$')

        # Node hop count: 2
        p38 = re.compile(r'^Node hop count:\s+(?P<node_hop_count>.+)$')

        # Hop0: 20.50.0.1
        # Hop1: 21.50.0.2
        # Hop2: 109.109.109.109
        p39 = re.compile(r'^Hop(?P<hop>\d+):\s+(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        # Displayed 1 (of 9) heads, 0 (of 10) midpoints, 0 (of 6) tails
        p40 = re.compile(r'^Displayed\s+(?P<heads_displayed>\d+)\s+\(of\s+(?P<total_heads>\d+)\)'
                         r'\s+heads,\s+(?P<midpoints_displayed>\d+)\s+\(of\s+(?P<total_midpoints>\d+)'
                         r'\)\s+midpoints,\s+(?P<tails_displayed>\d+)\s+\(of\s+(?P<total_tails>\d+)\)\s+tails$')

        # Displayed 1 up, 0 down, 0 recovering, 0 recovered heads
        p41 = re.compile(r'^Displayed\s+(?P<up>\d+)\s+up,\s+(?P<down>\d+)\s+down,'
                         r'\s+(?P<recovering>\d+)\s+recovering,\s+(?P<recovered_heads>\d+).+$')


        for line in out.splitlines():
            line = line.strip()

            # Name: tunnel-te50000  Destination: 109.109.109.109  Ifhandle:0x20e0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tunnel_dict = ret_dict.setdefault('tunnel', {}).setdefault(group['tunnel'], {})
                tunnel_dict.update({
                    'destination': group['destination'],
                    'ifhandle': group['ifhandle']
                })
                continue

            # Signalled-Name: 50000_F17-ASR9922_F109-ASR9001
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tunnel_dict.update({'signalled_name': group['signalled_name']})
                continue

            # Admin:    up Oper:   up   Path:  valid   Signalling: connected
            m = p3.match(line)
            if m:
                group = m.groupdict()
                status_dict = tunnel_dict.setdefault('status', {})
                status_dict.update(
                    {k: v for k, v in group.items() if v is not None}
                )
                continue

            # path option 10,  type explicit 50000-EPath_10 (Basis for Setup, path weight 160)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path_option = int(group['path_option'])
                path_option_dict = status_dict.setdefault('path_option', {}).setdefault(path_option, {})
                path_option_dict.update({
                      'type': group['type'],
                     'path_weight': int(group['path_weight'])
                })
                continue

            # path option 20,  type explicit 50000-EPath_20
            # path option 100,  type dynamic
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                path_option = int(group['path_option'])
                path_option_dict = status_dict.setdefault('path_option', {}).setdefault(path_option, {})
                path_option_dict.update({'type': group['type']})
                continue

            # Accumulative metrics: TE 160 IGP 160 Delay 600000
            m = p5.match(line)
            if m:
                group = m.groupdict()
                accumulative_metrics_dict = path_option_dict.setdefault('accumulative_metrics', {})
                accumulative_metrics_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

            # Last PCALC Error: Tue Apr 27 16:21:21 2021
            m = p6.match(line)
            if m:
                group = m.groupdict()
                last_pcalc_error_dict = status_dict.setdefault('last_pcalc_error', {})
                last_pcalc_error_dict.update({'time': group['last_pcalc_error']})
                continue

            # Info: No path to destination, 109.109.109.109 (reverselink)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                last_pcalc_error_dict.update({
                    'info': group['info'],
                    'reverselink': group['reverselink']
                })
                continue

            # G-PID: 0x0800 (derived from egress interface properties)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'g_pid': group['g_pid']})
                continue

            # Bandwidth Requested: 0 kbps  CT0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'bandwidth_requested': int(group['bandwidth_requested']),
                                    'bandwidth_requested_unit': group['bandwidth_requested_unit']})
                continue

            # Creation Time: Tue Apr 27 16:21:14 2021 (01:36:30 ago)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({'creation_time': group['creation_time']})
                continue

            # Bandwidth:        0 kbps (CT0) Priority:  3  3 Affinity: 0x0/0xffff
            m = p11.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict = tunnel_dict.setdefault('config_parameters', {})
                config_parameters_dict.update({'bandwidth': int(group['bandwidth']),
                                               'bandwidth_unit': group['bandwidth_unit'],
                                               'priority': int(group['priority']),
                                               'affinity': group['affinity']})
                continue

            # Metric Type: IGP (interface)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'metric_type': group['metric_type']})
                continue

            # Tiebreaker: Min-fill (default)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                path_selection = config_parameters_dict.setdefault('path_selection', {})
                path_selection.update({'tiebreaker': group['tiebreaker']})
                continue

            # Hop-limit: disabled
            m = p14.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'hop_limit': group['hop_limit']})
                continue

            # Cost-limit: disabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'cost_limit': group['cost_limit']})
                continue

            # Delay-limit: disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'delay_limit': group['delay_limit']})
                continue

            # Delay-measurement: disabled
            m = p17.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'delay_measurement': group['delay_measurement']})
                continue

            # Path-invalidation timeout: 10000 msec (default), Action: Tear (default)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'path_invalidation_timeout': int(group['timeout']),
                                               'path_invalidation_timeout_unit': group['timeout_unit'],
                                               'action': group['action']})
                continue

            # AutoRoute:  enabled  LockDown: disabled   Policy class: not set
            m = p19.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update(
                    {k: v for k, v in group.items() if v is not None}
                )
                continue

            # Forward class: 0 (not enabled)
            m = p20.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'forward_class': int(group['forward_class']),
                                               'forward_class_state': group['forward_class_state']})
                continue

            # Forwarding-Adjacency: disabled
            m = p21.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'forwarding_adjacency': group['forwarding_adjacency']})
                continue

            # Autoroute Destinations: 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'autoroute_destinations': int(group['autoroute_destinations'])})
                continue

            # Loadshare:          0 equal loadshares
            m = p23.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'loadshare': int(group['loadshare']),
                                               'loadshare_state': group['loadshare_state']})
                continue

            # Auto-bw: disabled
            m = p24.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'auto_bw': group['auto_bw']})
                continue

            # Auto-Capacity: Disabled:
            m = p25.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'auto_capacity': group['auto_capacity']})
                continue

            # Fast Reroute: Enabled, Protection Desired: Any
            m = p26.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'fast_reroute': group['fast_reroute'],
                                               'protection_desired': group['protection_desired']})
                continue

            # Path Protection: Not Enabled
            m = p27.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'path_protection': group['path_protection']})
                continue

            # BFD Fast Detection: Disabled
            m = p28.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'bfd_fast_detection': group['bfd_fast_detection']})
                continue

            # Reoptimization after affinity failure: Enabled
            m = p29.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'reoptimization_after_affinity_failure': group['reoptimization']})
                continue

            # Soft Preemption: Disabled
            m = p30.match(line)
            if m:
                group = m.groupdict()
                config_parameters_dict.update({'soft_preemption': group['soft_preemption']})
                continue

            # Tunnel has been up for: 01:36:23 (since Tue Apr 27 16:21:21 JST 2021)
            m = p31.match(line)
            if m:
                group = m.groupdict()
                history_dict = tunnel_dict.setdefault('history', {})
                history_dict.update({'tunnel_up_time': group['tunnel_up_time']})
                continue

            # Uptime: 00:26:32 (since Tue Apr 27 17:31:12 JST 2021)
            m = p32.match(line)
            if m:
                group = m.groupdict()
                current_lsp_dict = history_dict.setdefault('current_lsp', {})
                current_lsp_dict.update({'uptime': group['uptime']})
                continue

            # LSP not signalled, identical to the [CURRENT] LSP
            m = p33.match(line)
            if m:
                group = m.groupdict()
                reopt_lsp_dict = history_dict.setdefault('reopt_lsp', {}).\
                    setdefault('lsp_failure', {})
                reopt_lsp_dict.update({'lsp': group['lsp'],
                                       'lsp_status': group['lsp_status']})
                continue

            # Date/Time: Tue Apr 27 16:26:11 JST 2021 [01:31:33 ago]
            m = p34.match(line)
            if m:
                group = m.groupdict()
                reopt_lsp_dict.update({'date_time': group['date_time']})
                continue

            # ID: 5 Path Option: 20
            m = p35.match(line)
            if m:
                group = m.groupdict()
                prior_lsp_dict = history_dict.setdefault('prior_lsp', {})
                prior_lsp_dict.update({'id': int(group['id']),
                                       'path_option': int(group['path_option'])})
                continue

            # Removal Trigger: reoptimization completed
            m = p36.match(line)
            if m:
                group = m.groupdict()
                prior_lsp_dict.update({'removal_trigger': group['removal_trigger']})
                continue

            # Path info (OSPF mpls1 area 0):
            m = p37.match(line)
            if m:
                group = m.groupdict()
                path_info_temp_dict = tunnel_dict.setdefault('path_info', {}).\
                    setdefault(group['path_info'], {})
                continue

            # Node hop count: 2
            m = p38.match(line)
            if m:
                group = m.groupdict()
                path_info_temp_dict.update({'node_hop_count': int(group['node_hop_count'])})
                continue

            # Hop0: 20.50.0.1
            # Hop1: 21.50.0.2
            # Hop2: 109.109.109.109
            m = p39.match(line)
            if m:
                group = m.groupdict()
                hop_dict = path_info_temp_dict.setdefault('hop', {}). \
                    setdefault(int(group['hop']), {})
                hop_dict.update({'ip_address': group['ip_address']})
                continue

            # Displayed 1 (of 9) heads, 0 (of 10) midpoints, 0 (of 6) tails
            m = p40.match(line)
            if m:
                group = m.groupdict()
                displayed_dict = tunnel_dict.setdefault('displayed', {})
                displayed_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

            # Displayed 1 up, 0 down, 0 recovering, 0 recovered heads
            m = p41.match(line)
            if m:
                group = m.groupdict()
                displayed_status_dict = displayed_dict.setdefault('status', {})
                displayed_status_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict



