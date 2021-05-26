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
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
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

