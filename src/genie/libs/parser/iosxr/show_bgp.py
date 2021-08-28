"""show_bgp.py

IOSXR parsers for the following show commands:
    show placement program all'
    * 'show bgp instance <WORD> af-group <WORD> configuration'
    * 'show bgp instance <WORD> session-group <WORD> configuration'
    * 'show bgp instance all all all process detail'
    * 'show bgp instance all vrf all process detail'
    * 'show bgp instance all vrf all ipv4 unicast process detail'
    * 'show bgp instance all vrf all ipv6 unicast process detail'
    * 'show bgp instance all all all neighbors detail'
    * 'show bgp instance all vrf all neighbors detail'
    * 'show bgp instance all vrf all ipv4 unicast neighbors detail'
    * 'show bgp instance all vrf all ipv6 unicast neighbors detail'
    * 'show bgp instance all all all neighbors <WORD> routes'
    * 'show bgp instance all vrf all neighbors <WORD> routes'
    * 'show bgp instance all vrf all ipv4 unicast neighbors <WORD> routes'
    * 'show bgp instance all vrf all ipv6 unicast neighbors <WORD> routes'
    * 'show bgp instance all all all neighbors <WORD> receieved routes'
    * 'show bgp instance all vrf all neighbors <WORD> receieved routes'
    * 'show bgp instance all vrf all ipv4 unicast neighbors <WORD> receieved routes'
    * 'show bgp instance all vrf all ipv6 unicast neighbors <WORD> receieved routes'
    * 'show bgp instance all all all neighbors <WORD> advertised-routes'
    * 'show bgp instance all vrf all neighbors <WORD> advertised-routes'
    * 'show bgp instance all vrf all ipv4 unicast neighbors <WORD> advertised-routes'
    * 'show bgp instance all vrf all ipv6 unicast neighbors <WORD> advertised-routes'
    * 'show bgp instance all all all summary'
    * 'show bgp instance all vrf all summary'
    * 'show bgp instance all vrf all ipv4 unicast summary'
    * 'show bgp instance all vrf all ipv6 unicast summary'
    * 'show bgp instance all all all'
    * 'show bgp instance all vrf all'
    * 'show bgp instance all vrf all ipv4 unicast'
    * 'show bgp instance all vrf all ipv6 unicast'
    * 'show bgp instances'
    * 'show bgp vrf-db vrf all'
    * 'show bgp l2vpn evpn'
    * 'show bgp l2vpn evpn advertised'
    * 'show bgp l2vpn evpn neighbors'
    * 'show bgp l2vpn evpn neighbors <neighbor>'
    * 'show bgp sessions'
    * 'show bgp instance all sessions'
    * 'show bgp instance {instance} sessions'
    * 'show bgp egress-engineering'
    * 'show bgp all all nexthops'
    * 'show bgp {address_family} {ip_address} brief'
    * 'show bgp {address_family} {ip_address} bestpath-compare'
"""

# Python
import re
import logging
import collections
from ipaddress import ip_address, ip_network
from sys import version

# Metaparser
from genie.libs.parser.base import *
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use, ListOf

# Parser
from genie.libs.parser.yang.bgp_openconfig_yang import BgpOpenconfigYang

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# ========================================
# Parser for 'show bgp egress-engineering'
# ========================================

class ShowBgpEgressEngineeringSchema(MetaParser):
    
    ''' Schema for show bgp egress-engineering '''
    schema = {
        'peer_set':{
            Any():{
                'peer_set_id': str,
                'nexthop': str,
                'version': int,
                'rn_version': int,
                'flags': str,
                'local_asn': int,
                'remote_asn': int,
                'local_rid': str,
                'remote_rid': str,
                Optional('local_address'): str,
                'first_hop': list,
                'nhid': list,
                Optional('ifh'): list,
                'label': int,
                'refcount': int,
                'rpc_set': str,
                Optional('id'): int
            },
        },
    }

class ShowBgpEgressEngineering(ShowBgpEgressEngineeringSchema):

    ''' Parser for show bgp egress-engineering'''

    cli_command = ['show bgp egress-engineering']
    

    def cli (self, output=None):
        if output is None:
            out=self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        #  Egress Engineering Peer Set: 192.168.1.2/32 (10b87210)
        p1 = re.compile(r'Egress +Engineering +Peer +Set: +(?P<prefix>[\d\/\.]+) '
        '+(?P<peer_set_id>\S+)')

        #   Version: 2, rn_version: 2
        p2 = re.compile(r'(?P<key_1>[\w\s]+): +(?P<value_1>[\S\s]+), +(?P<key_2>[\w\s]+): '
        '+(?P<value_2>\d+)')

        #    Local ASN: 1
        #     Remote ASN: 2
        #     Local RID: 10.4.1.3
        #     Remote RID: 10.4.1.4
        #     First Hop: 192.168.1.2
        #         NHID: 3
        p3 = re.compile(r'(?P<key>[\w\s]+): (?P<value>[\S\s]+)')

        for line in out.splitlines():
            line = line.strip()

            #  Egress Engineering Peer Set: 192.168.1.2/32 (10b87210)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                peer_dict = ret_dict.setdefault( 'peer_set',{}).\
                    setdefault(group['prefix'], {})
                value = group['peer_set_id'].strip('()')
                peer_dict.update({'peer_set_id' :value })
                continue

            # Version: 2, rn_version: 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                values = list(group.values())
                for val in range(0, len(values), 2):
                    update_value = int(values[val+1]) if values[val+1].isdigit() else values[val+1]
                    peer_dict.update({values[val].strip().lower().\
                        replace(' ','_') : update_value})

                continue

            #Local ASN: 1
            #     Remote ASN: 2
            #     Local RID: 10.4.1.3
            #     Remote RID: 10.4.1.4
            #  First Hop: 10.121.88.1, 10.1.0.1, 10.204.0.1
            #   NHID: 9, 10, 11
            #   IFH: 0x110, 0x130, 0x150
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['key'].strip().lower().replace(' ','_') == 'first_hop'\
                or group['key'].strip().lower().replace(' ','_') == 'nhid'\
                or group['key'].strip().lower().replace(' ','_') == 'ifh':
                    update_value = group['value'].strip(',').split(',')
                    update_value = [int(item.strip()) if item.strip().isdigit() \
                        else item.strip() for item in update_value]
                elif group['value'].isdigit():
                    update_value = int(group['value']) 
                else:
                    update_value = group['value'] 

                peer_dict.update({group['key'].strip().lower().\
                    replace(' ','_') : update_value})
                    
                continue

        return ret_dict
    

# =======================================
# Parser for 'show bgp instances'
# =======================================

class ShowBgpInstancesSchema(MetaParser):

    """Schema for show bgp instances"""

    schema = {
        'instance':{
            Any(): {
                'bgp_id': Or(int, str),
                'instance_id': int,
                'placed_grp': str,
                Optional('num_vrfs'): int,
                Optional('address_families'): list
            }
        },
        Optional('number_of_bgp_instances'): int,
    }

class ShowBgpInstances(ShowBgpInstancesSchema):

    """Parser for show bgp instances"""

    cli_command = 'show bgp instances'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p1 = re.compile(r'^(?P<instance_id>\d+) +(?P<placed_grp>[\w\_|\-]+) '
                        r'+(?P<instance>[\w\-]+) +(?P<bgp_id>[\d\.]+) '
                        r'+(?P<num_vrfs>\d+)? +(?P<address_family>[\w\s\,\-]+)$')

        p1_1 = re.compile(r'(ID +Placed-Grp +Name +AS +VRFs +Address +Families)|(\-)+')
        p2 = re.compile(r'^(?P<address_family>[(IPv|VPNv)\d Unicast\,]+)$')
        p3 = re.compile(r'^Number +of +BGP +instances\: '
                        r'+(?P<number_of_bgp_instances>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ID  Placed-Grp  Name              AS        VRFs    Address Families
            # --------------------------------------------------------------------------------
            # 0   v4_routing  test              333       0       none
            # 1   bgp2_1      test1             333       0       none
            # 2   bgp3_1      test2             333       0       none
            # 3   bgp4_1      default           100       2       IPv4 Unicast, VPNv4 Unicast,

            m = p1.match(line)
            if m:
                instance_id = m.groupdict()['instance_id']
                placed_grp = m.groupdict()['placed_grp']
                instance = m.groupdict()['instance']
                bgp_id = m.groupdict()['bgp_id']
                num_vrfs = m.groupdict()['num_vrfs']
                address_family = m.groupdict()['address_family'].lower()

                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance not in ret_dict['instance']:
                    ret_dict['instance'][instance] = {}

                if instance_id:
                    ret_dict['instance'][instance]['instance_id'] = int(instance_id)
                if bgp_id:
                    try:
                        ret_dict['instance'][instance]['bgp_id'] = int(bgp_id)
                    except:
                        ret_dict['instance'][instance]['bgp_id'] = bgp_id
                if num_vrfs:
                    ret_dict['instance'][instance]['num_vrfs'] = int(num_vrfs)

                if address_family and address_family != 'none':
                    address_family_lst = address_family.strip(',').split(',')
                    address_family_lst = [item.strip() for item in address_family_lst]

                    ret_dict['instance'][instance]['address_families'] = address_family_lst

                ret_dict['instance'][instance]['placed_grp'] = placed_grp

                continue

            # ID  Placed-Grp  Name              AS        VRFs    Address Families
            # --------------------------------------------------------------------------------
            m = p1_1.match(line)
            if m:
                continue

            #                                                     IPv6 Unicast, VPNv6 Unicast
            m = p2.match(line)
            if m:
                address_family_extra_line = m.groupdict()['address_family'].lower()
                if address_family_extra_line and address_family_extra_line != 'none':
                    address_family_extra_line = address_family_extra_line.strip(',').split(',')
                    address_family_extra_line = [item.strip() for item in address_family_extra_line]
                    address_family_lst.extend(address_family_extra_line)
                    ret_dict['instance'][instance]['address_families'] = address_family_lst

            # Number of BGP instances: 1
            m3 = p3.match(line)
            if m3:
                num = int(m3.groupdict()['number_of_bgp_instances'])
                ret_dict['number_of_bgp_instances'] = num

                continue

        return ret_dict

# =======================================
# Parser for 'show placement program all'
# =======================================

class ShowPlacementProgramAllSchema(MetaParser):

    """Schema for show placement program all"""

    schema = {
        'program':
            {Any():
                {'instance':
                    {Any():
                        {'group': str,
                        'jid': str,
                        'active': str,
                        'active_state': str,
                        'standby': str,
                        'standby_state': str
                        }
                    },
                }
            },
        }

class ShowPlacementProgramAll(ShowPlacementProgramAllSchema):

    """Parser for show placement program all"""

    cli_command = 'show placement program all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        p1 = re.compile(r'^\s*(?P<program>[a-zA_Z0-9\_\-]+)'
                        '(?:\((?P<instance>\S+)\))?'
                        ' +(?P<group>\S+)'
                        ' +(?P<jid>\S+)'
                        ' +(?P<active_rp>\S+)'
                        ' +(?P<active_state>\S+)'
                        ' +(?P<standby_rp>\S+)'
                        ' +(?P<standby_state>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # schema_server                           central-services    1177 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING
            # rcp_fs                                  central-services    1168 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED
            # bgp(test)                               Group_10_bgp2       1052 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING

            m = p1.match(line)
            if m:
                program = str(m.groupdict()['program'])
                instance = m.groupdict()['instance'] or 'default'
                group = str(m.groupdict()['group'])
                jid = str(m.groupdict()['jid'])
                active = str(m.groupdict()['active_rp'])
                standby = str(m.groupdict()['standby_rp'])
                standby_state = str(m.groupdict()['standby_state'])
                active_state = str(m.groupdict()['active_state'])

                if 'program' not in ret_dict:
                    ret_dict['program'] = {}
                if program not in ret_dict['program']:
                    ret_dict['program'][program] = {}

                if 'instance' not in ret_dict['program'][program]:
                    ret_dict['program'][program]['instance'] = {}
                if instance not in ret_dict['program'][program]['instance']:
                    ret_dict['program'][program]['instance'][instance] = {}

                ret_dict['program'][program]['instance'][instance]['group'] = group
                ret_dict['program'][program]['instance'][instance]['jid'] = jid
                ret_dict['program'][program]['instance'][instance]['active'] = active
                ret_dict['program'][program]['instance'][instance]['standby'] = standby
                ret_dict['program'][program]['instance'][instance]['standby_state'] = standby_state
                ret_dict['program'][program]['instance'][instance]['active_state'] = active_state

                continue
    
        return ret_dict


# ===================================================================
# Parser for 'show bgp instance <WORD> af-group <WORD> configuration'
# ===================================================================

class ShowBgpInstanceAfGroupConfigurationSchema(MetaParser):
    
    """Schema for show bgp instance af-group configuration"""

    schema = {
        'instance':
            {Any():
                {'pp_name':
                    {Any():
                        {Optional('default_originate'): bool,
                         Optional('address_family'): str,
                         Optional('default_originate_route_map'): str,
                         Optional('default_originate_inherit'): str,
                         Optional('maximum_prefix_max_prefix_no'): int,
                         Optional('maximum_prefix_threshold'): int,
                         Optional('maximum_prefix_restart'): int,
                         Optional('maximum_prefix_warning_only'): str,
                         Optional('next_hop_self'): bool,
                         Optional('next_hop_self_inherit'): str,
                         Optional('route_map_name_in'): str,
                         Optional('route_map_name_in_inherit'): str,
                         Optional('route_map_name_out'): str,
                         Optional('route_map_name_out_inherit'): str,
                         Optional('route_reflector_client'): bool,
                         Optional('route_reflector_client_inherit'): str,
                         Optional('send_community'): str,
                         Optional('send_comm_ebgp'): bool,
                         Optional('send_comm_ebgp_inherit'): str,
                         Optional('send_ext_comm_ebgp'): bool,
                         Optional('send_ext_comm_ebgp_inherit'): str,
                         Optional('soo'): str,
                         Optional('soo_inherit'): str,
                         Optional('soft_reconfiguration'): str,
                         Optional('soft_reconfiguration_inherit'): str,
                         Optional('allowas_in_as_number'): int,
                         Optional('allowas_in'): bool,
                         Optional('allowas_in_inherit'): str,
                         Optional('as_override'): bool,
                         Optional('as_override_inherit'): str,
                        }
                    },
                }
            },
        }

class ShowBgpInstanceAfGroupConfiguration(ShowBgpInstanceAfGroupConfigurationSchema):
    """Parser for show bgp instance af-group configuration"""

    cli_command = 'show run formal | i af-group'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        pp1 = re.compile(r'\s*router +bgp +(?P<bgp_id>\d+)'
                         '(?: +instance +(?P<instance_name>[a-zA-Z0-9]+))?'
                         ' +af-group +(?P<pp_name>[a-zA-Z0-9\-\_]+)')
        p1 = re.compile(r'^af\-group +(?P<pp>[\w\-\.\:]+) +'
                        'address\-family +(?P<af>[\w\s]+)$')
        p2 = re.compile(r'^default\-originate *(policy)? *'
                        '(?P<policy>[\w\-\.\:\s]+)? +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p3 = re.compile(r'^maximum\-prefix +'
                        '(?P<no>[\d]+)? +(?P<th>[\d]+)? +(?P<re>[\d]+)? +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p4 = re.compile(r'^next\-hop\-self +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p5 = re.compile(r'^policy +(?P<map>[\w]+) +in +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p6 = re.compile(r'^policy +(?P<map>[\w]+) +out +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p7 = re.compile(r'^route\-reflector\-client +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p8 = re.compile(r'^send\-community\-ebgp +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p9 = re.compile(r'^send\-extended\-community\-ebgp +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p10 = re.compile(r'^site\-of\-origin +(?P<soo>[\w\:]+) +'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p11 = re.compile(r'^soft\-reconfiguration +(?P<soft>[\w\s]+) +'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p12 = re.compile(r'^allowas\-in +(?P<al>\d+)? *'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p13 = re.compile(r'^as\-override *'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')

        cmd = ''

        for line1 in out.splitlines():
            line1 = line1.strip()

            # router bgp 100 af-group af_group address-family ipv4 unicast

            mm1 = pp1.match(line1)
            if mm1:
                pp_name = mm1.groupdict()['pp_name']
                if mm1.groupdict()['instance_name'] is not None:
                    instance_name = str(mm1.groupdict()['instance_name']).strip()
                else:
                    instance_name = 'default'

                # instance instance_name
                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance_name not in ret_dict['instance']:
                    ret_dict['instance'][instance_name] = {}
        
                # af-group af_group
                if 'pp_name' not in ret_dict['instance'][instance_name]:
                    ret_dict['instance'][instance_name]['pp_name'] = {}
                if pp_name not in ret_dict['instance'][instance_name]['pp_name']:
                    ret_dict['instance'][instance_name]['pp_name'][pp_name] = {}

                cmd = 'show bgp instance {instance_name} af-group {pp_name} configuration'.format(instance_name=instance_name, pp_name=pp_name)
                out = self.device.execute(cmd)

                # use for send_community key value tracker
                send_community = []
        
                for line in out.splitlines():
                    line = line.strip()
                    # af_group address-family IPv4 Unicast

                    m = p1.match(line)
                    if m:
                        af = m.groupdict()['af'].lower()
                        if af:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['address_family'] = af
                        continue
        
                    # default-originate policy allpass            []

                    m = p2.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['default_originate'] = True
        
                        if m.groupdict()['policy']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['default_originate_route_map'] = \
                                    m.groupdict()['policy'].strip()
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['default_originate_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # maximum-prefix 429 75 35                    []

                    m = p3.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['maximum_prefix_max_prefix_no'] = int(m.groupdict()['no'])
        
                        if m.groupdict()['th']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['maximum_prefix_threshold'] = int(m.groupdict()['th'])
        
                        if m.groupdict()['re']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['maximum_prefix_restart'] = int(m.groupdict()['re'])
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['maximum_prefix_warning_only'] = m.groupdict()['inherit']
                        continue
        
                    # next-hop-self                               []

                    m = p4.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['next_hop_self'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['next_hop_self_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # policy allpass in                           []

                    m = p5.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['route_map_name_in'] = m.groupdict()['map']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['route_map_name_in_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # policy allpass out                          []

                    m = p6.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['route_map_name_out'] = m.groupdict()['map']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['route_map_name_out_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # route-reflector-client                      []

                    m = p7.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['route_reflector_client'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['route_reflector_client_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # send-community-ebgp                         []

                    m = p8.match(line)
                    if m:
                        send_community.append('standard')
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['send_comm_ebgp'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['send_comm_ebgp_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # send-extended-community-ebgp                []

                    m = p9.match(line)
                    if m:
                        send_community.append('extended')
        
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['send_ext_comm_ebgp'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['send_ext_comm_ebgp_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # send_community
                    if send_community:
                        if len(send_community) == 2:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['send_community'] = 'both'
                        else:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['send_community'] = send_community[0]
        
                    # site-of-origin 100:1                        []

                    m = p10.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['soo'] = m.groupdict()['soo']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['soo_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # soft-reconfiguration inbound always         []

                    m = p11.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['soft_reconfiguration'] = m.groupdict()['soft'].strip()
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['soft_reconfiguration_inherit'] \
                                    = m.groupdict()['inherit']
                        continue
        
                    # allowas-in 10                               []

                    m = p12.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['allowas_in'] = True
        
                        if m.groupdict()['al']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['allowas_in_as_number'] = int(m.groupdict()['al'])
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['allowas_in_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # as-override                                 []

                    m = p13.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['as_override'] = True
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['as_override_inherit'] = m.groupdict()['inherit']
                        continue

        # # return empty if no attributes
        # if len(ret_dict['instance'][instance_name]['pp_name'][pp_name]) == 0:
        #     ret_dict = {}

        return ret_dict


# ========================================================================
# Parser for 'show bgp instance <WORD> session-group <WORD> configuration'
# ========================================================================

class ShowBgpInstanceSessionGroupConfigurationSchema(MetaParser):
    """ Schema for show bgp instance session-group configuration"""

    schema = {
        'instance':
            {Any():
                {'peer_session':
                    {Any():
                        {Optional('remote_as'): int,
                         Optional('remote_as_inherit'): str,
                         Optional('description'): str,
                         Optional('description_inherit'): str,
                         Optional('ebgp_multihop_enable'): bool,
                         Optional('ebgp_multihop_max_hop'): int,
                         Optional('ebgp_multihop_inherit'): str,
                         Optional('local_as_as_no'): int,
                         Optional('local_no_prepend'): bool,
                         Optional('local_dual_as'): bool,
                         Optional('local_replace_as'): bool,
                         Optional('local_as_inherit'): str,
                         Optional('password_text'): str,
                         Optional('password_text_inherit'): str,
                         Optional('shutdown'): bool,
                         Optional('shutdown_inherit'): str,
                         Optional('keepalive_interval'): int,
                         Optional('holdtime'): int,
                         Optional('ps_minimum_holdtime'): int,
                         Optional('timers_inherit'): str,
                         Optional('update_source'): str,
                         Optional('update_source_inherit'): str,
                         Optional('suppress_four_byte_as_capability'): bool,
                         Optional('suppress_4byteas_inherit'): str,
                         Optional('fall_over_bfd'): bool,
                         Optional('fall_over_bfd_inherit'): str,
                         Optional('disable_connected_check'): bool,
                         Optional('disable_connected_check_inherit'): str,
                         Optional('transport_connection_mode'): str,
                         Optional('transport_connection_mode_inherit'): str,
                        }
                    }
                }
            }
        }

class ShowBgpInstanceSessionGroupConfiguration(ShowBgpInstanceSessionGroupConfigurationSchema):

    """Parser for show bgp instance session-group configuration"""

    cli_command = 'show run formal | i session-group'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        cmd = ''
        pp1 = re.compile(r'\s*router +bgp +(?P<bgp_id>\d+)'
                         '(?: +instance +(?P<instance_name>[a-zA-Z0-9]+))?'
                         '(?: +neighbor +(?P<neighbor_id>[0-9\.\:]+) +use)?'
                         ' +session-group +(?P<ps_name>[a-zA-Z0-9\-\_]+)')
        p2 = re.compile(r'^remote\-as +(?P<as>\d+)? +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p3 = re.compile(r'^description +(?P<descr>[\w\,\.\:\-\s]+) +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p4 = re.compile(r'^ebgp\-multihop +(?P<num>\d+)? *'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p5 = re.compile(r'^local\-as +(?P<as>\d+) +(?P<v1>no\-prepend)? +'
                        '(?P<v2>replace\-as)? *(?P<v3>dual\-as)? *'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p6 = re.compile(r'^password +encrypted +(?P<psw>\w+) +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p7 = re.compile(r'^shutdown +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p8 = re.compile(r'^timers +(?P<keep>\d+) +'
                        '(?P<hold>\d+) +(?P<mim>\d+)? *'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p9 = re.compile(r'^update\-source +(?P<intf>[\w\.\/]+) +'
                        '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p10 = re.compile(r'^suppress\-4byteas +'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p11 = re.compile(r'^session\-open\-mode +(?P<mode>[\w\-]+) +'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p12 = re.compile(r'^bfd fast-detect +'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
        p13 = re.compile(r'^ignore\-connected *'
                         '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')

        for line1 in out.splitlines():
            line1 = line1.strip()

            # router bgp 100 session-group SG
            # router bgp 333 instance test session-group abcd
            # router bgp 333 instance test neighbor 10.4.1.1 use session-group LALALALLA

            mm1 = pp1.match(line1)
            if mm1:
                ps_name = str(mm1.groupdict()['ps_name'])
                if mm1.groupdict()['instance_name'] is not None:
                    instance_name = str(mm1.groupdict()['instance_name']).strip()
                else:
                    instance_name = 'default'

                # use for send_community key value tracker
                send_community = []

                # instance instance_name
                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance_name not in ret_dict['instance']:
                    ret_dict['instance'][instance_name] = {}

                # peer_session ps_name
                if 'peer_session' not in ret_dict['instance'][instance_name]:
                    ret_dict['instance'][instance_name]['peer_session'] = {}
                if ps_name not in ret_dict['instance'][instance_name]['peer_session']:
                    ret_dict['instance'][instance_name]['peer_session'][ps_name] = {}

                # Execute command with instance and session-group name
                cmd = 'show bgp instance {instance_name} session-group {ps_name} configuration'.format(instance_name=instance_name, ps_name=ps_name)
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.strip()

                    # remote-as 333                              []

                    m = p2.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['remote_as'] = int(m.groupdict()['as'])
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['remote_as_inheritl'] \
                                    = m.groupdict()['inherit']
                            continue

                    # description SG_group                       []

                    m = p3.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['description'] = m.groupdict()['descr'].strip()
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['description_inherit'] \
                                    = m.groupdict()['inherit']
                        continue

                    # ebgp-multihop 254                         []

                    m = p4.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['ebgp_multihop_enable'] = True
                        if m.groupdict()['num']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['ebgp_multihop_max_hop'] \
                                    = int(m.groupdict()['num'])
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['ebgp_multihop_inherit'] \
                                    = m.groupdict()['inherit']
                        continue

                    # local-as 200 no-prepend replace-as dual-as []

                    m = p5.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['local_as_as_no'] = int(m.groupdict()['as'])
        
                        if m.groupdict()['v1']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['local_no_prepend'] = True
                        if m.groupdict()['v2']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['local_replace_as'] = True
                        if m.groupdict()['v3']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['local_dual_as'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['local_as_inherit'] = m.groupdict()['inherit']
                        continue

                    # password encrypted 094F471A1A0A464058      []

                    m = p6.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['password_text'] = m.groupdict()['psw']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['password_text_inherit'] = m.groupdict()['inherit']
                        continue

                    # shutdown                                   []

                    m = p7.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['shutdown'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['shutdown_inherit'] = m.groupdict()['inherit']
                        continue

                    # timers 10 30 3                             []

                    m = p8.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['keepalive_interval'] = int(m.groupdict()['keep'])
        
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['holdtime'] =int(m.groupdict()['hold'])
        
                        if m.groupdict()['mim']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['ps_minimum_holdtime'] = int(m.groupdict()['mim'])
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['timers_inherit'] = m.groupdict()['inherit']
                        continue

                    # update-source Loopback0                    []

                    m = p9.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['update_source'] = m.groupdict()['intf'].lower()
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['update_source_inherit'] = m.groupdict()['inherit']
                        continue

                    # suppress-4byteas                        []

                    m = p10.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['suppress_four_byte_as_capability'] = True
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['suppress_4byteas_inherit'] = m.groupdict()['inherit']
                        continue

                    # session-open-mode active-only              []

                    m = p11.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['transport_connection_mode'] = m.groupdict()['mode']
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['transport_connection_mode_inherit'] = m.groupdict()['inherit']
                        continue

                    # bfd fast-detect                            []

                    m = p12.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['fall_over_bfd'] = True
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['fall_over_bfd_inherit'] = m.groupdict()['inherit']
                        continue

                    # ignore-connected                           []

                    m = p13.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['disable_connected_check'] = True
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['disable_connected_check_inherit'] = m.groupdict()['inherit']
                            continue

        return ret_dict


# ===========================================================
# Parser for:
# 'show bgp instance all all all process detail'
# 'show bgp instance all vrf all process detail'
# 'show bgp instance all vrf all ipv4 unicast process detail'
# 'show bgp instance all vrf all ipv6 unicast process detail'
# ===========================================================

class ShowBgpInstanceProcessDetailSchema(MetaParser):

    """Schema for:
        show bgp instance all all all process detail
        show bgp instance all vrf all process detail
        show bgp instance all vrf all ipv4 unicast process detail
        show bgp instance all vrf all ipv6 unicast process detail
    """

    schema = {
        'instance':
            {Any():
                {Optional('vrf'):
                    {Any():
                        {Optional('operation_mode'): str,
                         Optional('route_distinguisher'): str,
                         Optional('router_id'): str,
                         Optional('as_system_number_format'): str,
                         Optional('as_number'): Or(int, str),
                         Optional('default_cluster_id'): str,
                         Optional('active_cluster_id'): str,
                         Optional('fast_external_fallover'): bool,
                         Optional('platform_rlimit_max'): int,
                         Optional('max_limit_for_bmp_buffer_size'): int,
                         Optional('default_value_for_bmp_buffer_size'): int,
                         Optional('current_limit_for_bmp_buffer_size'): int,
                         Optional('current_utilization_of_bmp_buffer_limit'): int,
                         Optional('log_neighbor_changes'): bool,
                         Optional('default_local_preference'): int,
                         Optional('default_keepalive'): int,
                         Optional('non_stop_routing'): bool,
                         Optional('update_delay'): int,
                         Optional('generic_scan_interval'): int,
                         Optional('bgp_speaker_process'): int,
                         Optional('node'): str,
                         Optional('restart_count'): int,
                         Optional('sent_updates'): int,
                         Optional('received_updates'): int,
                         Optional('sent_notifications'): int,
                         Optional('received_notifications'): int,
                         Optional('always_compare_med'): bool,
                         Optional('bestpath_compare_routerid'): bool,
                         Optional('bestpath_cost_community_ignore'): bool,
                         Optional('bestpath_med_missing_at_worst'): bool,
                         Optional('enforce_first_as'): bool,
                         Optional('graceful_restart'): bool,
                         Optional('graceful_restart_helper_only'): bool,
                         Optional('graceful_restart_restart_time'): int,
                         Optional('graceful_restart_stalepath_time'): int,
                         Optional('log_neighbor_changes'): bool,
                         Optional('vrf_info'):
                            {Any():
                                {Optional('total'): int,
                                Optional('nbrs_estab'): int,
                                Optional('cfg'): int
                                },
                            },
                        Optional('att'):
                            {Any():
                                {Optional('number'): int,
                                Optional('memory_used'): int
                                }
                            },
                        Optional('pool'):
                            {Any():
                                {Optional('alloc'): int,
                                Optional('free'): int
                                }
                            },
                        Optional('message_logging_pool_summary'):
                            {Any():
                                {Optional('alloc'): int,
                                Optional('free'): int
                                }
                            },
                        Optional('bmp_pool_summary'):
                            {Any():
                                {Optional('alloc'): int,
                                Optional('free'): int
                                }
                            },
                        Optional('address_family'):
                            {Any():
                                {Optional('dampening'): bool,
                                 Optional('client_to_client_reflection'): bool,
                                 Optional('dynamic_med'): bool,
                                 Optional('dynamic_med_int'): str,
                                 Optional('dynamic_med_timer'): str,
                                 Optional('dynamic_med_periodic_timer'): str,
                                 Optional('scan_interval'): str,
                                 Optional('total_prefixes_scanned'): str,
                                 Optional('prefix_scanned_per_segment'): str,
                                 Optional('num_of_scan_segments'): str,
                                 Optional('nexthop_resolution_minimum_prefix_length'): str,
                                 Optional('main_table_version'): str,
                                 Optional('table_version_synced_to_rib'): str,
                                 Optional('table_version_acked_by_rib'): str,
                                 Optional('rib_has_not_converged'): str,
                                 Optional('rib_table_prefix_limit_reached'): str,
                                 Optional('rib_table_prefix_limit_ver'): str,
                                 Optional('permanent_network'): str,
                                 Optional('current_vrf'): str,
                                 Optional('table_state'): str,
                                 Optional('state'): str,
                                 Optional('bgp_table_version'): str,
                                 Optional('attribute_download'): str,
                                 Optional('label_retention_timer_value'): str,
                                 Optional('soft_reconfig_entries'): str,
                                 Optional('table_bit_field_size'): str,
                                 Optional('chunk_elememt_size'): str,
                                 Optional('enabled'): bool,
                                 Optional('graceful_restart'): bool,
                                 Optional('advertise_inactive_routes'): bool,
                                 Optional('ebgp_max_paths'): int,
                                 Optional('ibgp_max_paths'): int,
                                 Optional('total_paths'): int,
                                 Optional('total_prefixes'): int,
                                 Optional('thread'):
                                    {Any():
                                        {Optional('triggers'):
                                            {Any():
                                                {Optional('ver'): int,
                                                Optional('tbl_ver'): int,
                                                Optional('trig_tid'): int
                                                }
                                            },
                                        }
                                    },
                                Optional('remote_local'):
                                    {Any():
                                        {Optional('allocated'): int,
                                         Optional('freed'): int
                                        },
                                    },
                                Optional('prefixes_path'):
                                    {Any():
                                        {Optional('number'): int,
                                         Optional('mem_used'): int
                                        },
                                    },
                                }
                            },
                        },
                    },
                },
            },
        }


class ShowBgpInstanceProcessDetail(ShowBgpInstanceProcessDetailSchema):
    """Parser for:
        show bgp instance all all all process detail
        show bgp instance all vrf all process detail
        show bgp instance all vrf all ipv4 unicast process detail
        show bgp instance all vrf all ipv6 unicast process detail
        parser class - implements detail parsing mechanisms for cli, yang output.
        If there is output args in cli ,need to have below key(s) that are mandatory and used in this parser.

        - vrf_type

    """
    cli_command = ['show bgp instance {instance} all all process detail',
                   'show bgp instance {instance} {vrf_type} {vrf} process detail',
                   'show bgp instance {instance} {vrf_type} {vrf} {address_family} process detail']

    exclude = ['alloc', 'free', 'sent_notifications', 'bgp_table_version',
               'main_table_version', 'table_version_synced_to_rib',
               'table_version_acked_by_rib',
               'triggers', 'tbl_ver', 'ver', 'node', 'total_prefixes_scanned',
               'sent_updates',
               'allocated', 'freed', 'received_updates', 'num_of_scan_segments', 'state',
               'restart_count', 'memory_used', 'number']

    def cli(self, vrf_type='all', instance='all', vrf='all', address_family='', output=None):
        assert vrf_type in ['all', 'vrf']
        assert address_family in ['', 'ipv4 unicast', 'ipv6 unicast']

        if output is None:
            if vrf_type == 'all':
                out = self.device.execute(self.cli_command[0].format(instance=instance))
            else:
                if address_family:
                    out = self.device.execute(
                        self.cli_command[2].format(instance=instance,
                                                   address_family=address_family,
                                                   vrf_type=vrf_type,
                                                   vrf=vrf))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(instance=instance,
                                                   vrf_type=vrf_type,
                                                   vrf=vrf))
        else:
            out = output
        p1 = re.compile(r'^\s*BGP +instance +(?P<num>\S+): +\'(?P<instance>\S+)\'$')
        p1_1 = re.compile(r'^\s*VRF: +(?P<vrf>[a-zA-Z0-9\_]+)$')
        p1_1_1 = re.compile(r'^BGP +Process +Information: +VRF +(?P<vrf>[\S]+)$')
        p1_2 = re.compile(r'^\s*BGP *Route *Distinguisher:'
                          ' *(?P<route_distinguisher>\S+)$')
        p2 = re.compile(r'BGP *is *operating *in *'
                        '(?P<operation_mode>\w+) *mode$')
        p3 = re.compile(r'^Autonomous *System *number *format: *'
                        '(?P<as_format>[a-zA-Z]+)$')

        #Autonomous System: 65108.65108
        p4 = re.compile(r'^Autonomous *System: *(?P<as_number>[0-9\.]+)$')
        p5 = re.compile(r'^Router *ID: *(?P<router_id>[\w\.\:]+) *'
                        '(\([\w\s]+\))?$')
        p6_1 = re.compile(r'^Default *Cluster *ID: *'
                          '(?P<default_cluster_id>[\w\.\:]+) *'
                          '(\([\w\s\:\.\,]+\))?$')
        p6_2 = re.compile(r'^Active *Cluster *IDs: *'
                          '(?P<active_cluster_id>[\w\.\:]+)$')
        p7_1 = re.compile(r'^Always compare MED is enabled$')
        p7_2 = re.compile(r'^Comparing router ID for eBGP paths$')
        p7_4 = re.compile(r'^Treating missing MED as worst$')
        p8 = re.compile(r'^Fast +external +fallover +enabled$')
        p9 = re.compile(r'^Platform *RLIMIT *max: *'
                        '(?P<platform_rlimit_max>[0-9\,]+) *bytes$')
        p10 = re.compile(r'^Maximum +limit +for +BMP +buffer +size: *'
                         '(?P<size>[a-zA-Z0-9]+) *MB$')
        p11 = re.compile(r'^Default *value *for *BMP *buffer *size: *'
                         '(?P<size>[a-zA-Z0-9]+) *MB$')
        p12 = re.compile(r'^Current *limit *for *BMP *buffer *size: *'
                         '(?P<size>[a-zA-Z0-9]+) *MB$')
        p13 = re.compile(r'^Current *utilization *of *BMP *buffer *'
                         'limit: *(?P<limit>[a-zA-Z0-9]+) *B$')
        p14 = re.compile(r'^Neighbor *logging *is *(?P<nbr_logging>\w+)$')
        p15 = re.compile(r'^Enforce +first +AS +(?P<as_enabled>\w+)$')
        p16 = re.compile(r'^Default *local *preference: *'
                         '(?P<preference>[0-9]+)$')
        p17 = re.compile(r'^Default *keepalive: *(?P<keepalive>[0-9]+)$')
        p18 = re.compile(r'^Non\-stop *routing *is +(?P<status>[a-zA-Z]+)$')
        p19 = re.compile(r'^Update *delay: *(?P<update_delay>[0-9]+)$')
        p20 = re.compile(r'^Generic *scan *interval: *'
                         '(?P<scan_interval>[0-9]+)$')
        p21 = re.compile(r'^BGP *Speaker *process: *'
                         '(?P<speaker>\w+), +Node: +(?P<node>\w+)$')
        p22 = re.compile(r'^Restart *count: *(?P<restart_count>[0-9]+)$')
        p23 = re.compile(r'^(?P<vrf_info>[\w\-]+) +VRFs: +'
                         '(?P<total>[0-9]+) +'
                         '(?P<nbrs_estab>[0-9]+)/(?P<cfg>[0-9]+)$')
        p24_1 = re.compile(r'^Updates:'
                           ' *(?P<sent>[0-9]+) *(?P<received>[0-9]+)$')
        p24_2 = re.compile(r'^Notifications:'
                           ' *(?P<sent>[0-9]+) *(?P<received>[0-9]+)$')
        p26 = re.compile(r'^Pool +(?P<pool>\w+): +(?P<alloc>\d+) +'
                         '(?P<free>\d+)$')
        p25 = re.compile(r'^(?P<att>[\w\s]+): +(?P<number>[0-9]+) +'
                         '(?P<memory_used>[0-9]+)$')
        p29 = re.compile(r'^Address *family: *(?P<af>[a-zA-Z0-9\s\-\_]+)$')
        p29_1 = re.compile(r'^VRF +(?P<current_vrf>(\S+)) +Address +family:'
                           ' +(?P<af>[a-zA-Z0-9\s\-\_]+)'
                           '(?: +\(Table +(?P<table_state>[a-z]+)\))?$')
        p30 = re.compile(r'^Dampening +is +(?P<dampening>[\w\s]+)$')
        p31 = re.compile(r'^Client +reflection +is +enabled +in +global +config$')
        p31_1 = re.compile(r'^Client +reflection +is +not +enabled +in +global +config$')
        p32 = re.compile(r'^Dynamic *MED *is *(?P<dynamic_med>\w+)$')
        p33 = re.compile(r'^Dynamic *MED *interval *: *'
                         '(?P<interval>[a-zA-Z0-9\s]+)$')
        p34 = re.compile(r'^Dynamic *MED *Timer *: *'
                         '(?P<dynamic_med_timer>[a-zA-Z0-9\s]+)$')
        p35 = re.compile(r'^Dynamic *MED *Periodic *Timer *: *'
                         '(?P<timer>[a-zA-Z0-9\s]+)$')
        p36 = re.compile(r'^Scan *interval: *(?P<scan_interval>[\w\s]+)$')
        p37 = re.compile(r'^Total *prefixes *scanned: *'
                         '(?P<scan>[a-zA-Z0-9\s]+)$')
        p38 = re.compile(r'^Prefixes *scanned *per *segment: *'
                         '(?P<prefix_scan>[a-zA-Z0-9\s]+)$')
        p39 = re.compile(r'^Number *of *scan *segments: *'
                         '(?P<num_of_scan_segments>[a-zA-Z0-9\s]+)$')
        p40 = re.compile(r'^Nexthop *resolution *minimum *prefix\-length: *'
                         '(?P<length>[\w\s\(\)]+)$')
        p41 = re.compile(r'^Main *Table *Version: *(?P<main_tab_ver>[\w\s]+)$')
        p42 = re.compile(r'^Table *version *synced *to *RIB: *'
                         '(?P<rib>[a-zA-Z0-9\s]+)$')
        p43 = re.compile(r'^Table *version *acked *by *RIB: *'
                         '(?P<rib>[a-zA-Z0-9\s]+)$')
        p44 = re.compile(r'^RIB *has *not *converged: *'
                         '(?P<rib>[a-zA-Z0-9\s]+)$')
        p54 = re.compile(r'^RIB *table *prefix\-limit *reached +\? *'
                         '\[(?P<rib>\w+)\], +version +(?P<ver>\d+)$')
        p45 = re.compile(r'^Permanent +Network +(?P<status>\w+)$')
        p46 = re.compile(r'^State: *(?P<state>[a-zA-Z\s]+).$')
        p47 = re.compile(r'^BGP *Table *Version: *(?P<tab_ver>\w+)$')
        p48 = re.compile(r'^Attribute *download: *(?P<attr>[\w\s]+)$')
        p49 = re.compile(r'^Label *retention *timer *value *'
                         '(?P<timer>[a-zA-Z0-9\s]+)$')
        p50 = re.compile(r'^Soft *Reconfig *Entries: *(?P<ent>\d+)$')
        p51 = re.compile(r'^Table *bit\-field *size *: *'
                         '(?P<size>[0-9\s]+) *Chunk *element *size *: *'
                         '(?P<elememt_size>\d+)$')
        p52 = re.compile(r'^(?P<thread>\w+\s\w+) *'
                         '(?P<trigger>\w+\s\d+\s[\d\:\.]+) +(?P<ver>[0-9]+) +'
                         '(?P<tbl_ver>[0-9]+) +(?P<trig_tid>[0-9]+)$')
        p53 = re.compile(r'^(?P<remote>[\w\s\-]+): *(?P<v1>\d+) *'
                         '(?P<v2>[0-9]+)$')
        # Init dict
        ret_dict = {}

        # Seperate message logging pool and bmp pool
        flag = None

        # Init vars
        vrf = 'default'
        instance = 'default'
        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'

            m = p1.match(line)
            if m:
                instance = m.groupdict()['instance']

                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance not in ret_dict['instance']:
                    ret_dict['instance'][instance] = {}

                # Create vrf list if default VRF
                if vrf_type == 'all':
                    if 'vrf' not in ret_dict['instance'][instance]:
                        ret_dict['instance'][instance]['vrf'] = {}
                    if vrf not in ret_dict['instance'][instance]['vrf']:
                        ret_dict['instance'][instance]['vrf'][vrf] = {}
                        continue

            # VRF: VRF1

            m = p1_1.match(line)
            if m:
                ret_dict.setdefault('instance', {}).setdefault(instance, {})
                vrf = str(m.groupdict()['vrf'])
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                # seperate message logging pool and bmp pool
                flag = None

                # Init key values to default - overwritten below if configured
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['always_compare_med'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_compare_routerid'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_cost_community_ignore'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_med_missing_at_worst'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['enforce_first_as'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['fast_external_fallover'] = False
                continue
            # BGP Process Information: VRF VRF1

            m = p1_1_1.match(line)
            if m:
                vrf = str(m.groupdict()['vrf'])
                ret_dict.setdefault('instance', {}).setdefault(instance, {}).setdefault(
                    'vrf', {}).setdefault(vrf, {})
                # seperate message logging pool and bmp pool
                flag = None

                # Init key values to default - overwritten below if configured
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['always_compare_med'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_compare_routerid'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_cost_community_ignore'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_med_missing_at_worst'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['enforce_first_as'] = False
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['fast_external_fallover'] = False
                continue

            # BGP Route Distinguisher: 100:1

            m = p1_2.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])

                ret_dict['instance'][instance]['vrf'][vrf][
                    'route_distinguisher'] = route_distinguisher
                continue

            # BGP is operating in STANDALONE mode

            m = p2.match(line)
            if m:
                operation_mode = m.groupdict()['operation_mode'].lower()
                ret_dict.setdefault('instance', {}).setdefault(instance, {}).setdefault(
                    'vrf', {}).setdefault(vrf, {})
                ret_dict['instance'][instance]['vrf'][vrf][
                    'operation_mode'] = operation_mode
                continue

            # Autonomous System number format: ASPLAIN

            m = p3.match(line)
            if m:
                as_format = m.groupdict()['as_format']

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['as_system_number_format'] = as_format
                continue

            # Autonomous System: 100

            m = p4.match(line)
            if m:
                as_number = "NA"
                try:
                    as_number = int(m.groupdict()['as_number'])
                except:
                    as_number = m.groupdict()['as_number']


                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['as_number'] = as_number
                continue

            # Router ID: 10.4.1.1 (manually configured)

            m = p5.match(line)
            if m:
                router_id = m.groupdict()['router_id']

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['router_id'] = router_id
                continue

            # Default Cluster ID: 10.4.1.1
            # Default Cluster ID: 10 (manually configured)

            m = p6_1.match(line)
            if m:
                default_cluster_id = m.groupdict()['default_cluster_id']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['default_cluster_id'] = default_cluster_id
                continue

            # Active Cluster IDs:  10.4.1.1

            m = p6_2.match(line)
            if m:
                active_cluster_id = m.groupdict()['active_cluster_id']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['active_cluster_id'] = active_cluster_id
                continue

            # Always compare MED is enabled

            m = p7_1.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['always_compare_med'] = True
                continue

            # Comparing router ID for eBGP paths

            m = p7_2.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_compare_routerid'] = True
                continue

            # Treating missing MED as worst

            m = p7_4.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bestpath_med_missing_at_worst'] = True
                continue

            # Fast external fallover enabled

            m = p8.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['fast_external_fallover'] = True
                continue

            # Platform RLIMIT max: 2147483648 bytes

            m = p9.match(line)
            if m:
                platform_rlimit_max = int(m.groupdict()['platform_rlimit_max'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['platform_rlimit_max'] = platform_rlimit_max
                continue

            # Maximum limit for BMP buffer size: 409 MB

            m = p10.match(line)
            if m:
                size = int(m.groupdict()['size'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['max_limit_for_bmp_buffer_size'] = size
                continue

            # Default value for BMP buffer size: 307 MB

            m = p11.match(line)
            if m:
                size = int(m.groupdict()['size'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['default_value_for_bmp_buffer_size'] = size
                continue

            # Current limit for BMP buffer size: 307 MB

            m = p12.match(line)
            if m:
                size = int(m.groupdict()['size'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['current_limit_for_bmp_buffer_size'] = size
                continue

            # Current utilization of BMP buffer limit: 0 B

            m = p13.match(line)
            if m:
                limit = int(m.groupdict()['limit'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['current_utilization_of_bmp_buffer_limit'] = limit
                continue

            # Neighbor logging is enabled

            m = p14.match(line)
            if m:
                nbr_logging = m.groupdict()['nbr_logging']
                if nbr_logging == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['log_neighbor_changes'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['log_neighbor_changes'] = False
                continue

            # Enforce first AS enabled

            m = p15.match(line)
            if m:
                as_enabled = m.groupdict()['as_enabled']
                if as_enabled == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['enforce_first_as'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['enforce_first_as'] = False
                continue

            # Default local preference: 100

            m = p16.match(line)
            if m:
                default_local_preference = int(m.groupdict()['preference'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['default_local_preference'] = default_local_preference
                continue

            # Default keepalive: 60

            m = p17.match(line)
            if m:
                default_keepalive = int(m.groupdict()['keepalive'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['default_keepalive'] = default_keepalive
                continue

            # Non-stop routing is enabled

            m = p18.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['non_stop_routing'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['non_stop_routing'] = False
                continue

            # Update delay: 120

            m = p19.match(line)
            if m:
                update_delay = int(m.groupdict()['update_delay'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['update_delay'] = update_delay
                continue

            # Generic scan interval: 60

            m = p20.match(line)
            if m:
                scan_interval = int(m.groupdict()['scan_interval'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['generic_scan_interval'] = scan_interval
                continue

            # BGP Speaker process: 0, Node: node0_0_CPU0

            m = p21.match(line)
            if m:
                speaker = int(m.groupdict()['speaker'])
                node = m.groupdict()['node']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bgp_speaker_process'] = speaker
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['node'] = node
                continue

            # Restart count: 1

            m = p22.match(line)
            if m:
                restart_count = int(m.groupdict()['restart_count'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['restart_count'] = restart_count
                continue

                #                            Total           Nbrs Estab/Cfg
            # Default vrfs:              1               2/2
            # Non-Default vrfs:          2               4/4

            m = p23.match(line)
            if m:
                if 'vrf_info' not in ret_dict['instance'][instance]['vrf'][vrf] \
                        :
                    ret_dict['instance'][instance]['vrf'][vrf]['vrf_info'] = {}

                vrf_info = str(m.groupdict()['vrf_info']).lower()
                # vrf_info = vrf_info.replace("-","_")
                total = int(m.groupdict()['total'])
                nbrs_estab = int(m.groupdict()['nbrs_estab'])
                cfg = int(m.groupdict()['cfg'])
                if vrf_info not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['vrf_info']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['vrf_info'][vrf_info] = {}

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['vrf_info'][vrf_info]['total'] = total
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['vrf_info'][vrf_info]['nbrs_estab'] = nbrs_estab
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['vrf_info'][vrf_info]['cfg'] = cfg
                continue

            #                            Alloc           Free
            # Pool 200:                  0               0

            # Message logging pool summary:
            #                            Alloc           Free
            # BMP pool summary:
            #                            Alloc           Free
            # Pool 100:                  0               0
            if re.compile(r'Message +logging +pool +summary:$').match(line):
                flag = 'message'

            if re.compile(r'BMP +pool +summary:').match(line):
                flag = 'bmp'

            m = p26.match(line)

            if m and flag == 'message':
                if 'message_logging_pool_summary' not in ret_dict['instance'] \
                        [instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['message_logging_pool_summary'] = {}

                pool = str(m.groupdict()['pool']).lower()
                alloc = int(m.groupdict()['alloc'])
                free = int(m.groupdict()['free'])

                if pool not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['message_logging_pool_summary']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['message_logging_pool_summary'][pool] = {}

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['message_logging_pool_summary'][pool]['alloc'] = alloc
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['message_logging_pool_summary'][pool]['free'] = free
                continue
            elif m and flag == 'bmp':
                if 'bmp_pool_summary' not in ret_dict['instance'][instance] \
                        ['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['bmp_pool_summary'] = {}

                pool = str(m.groupdict()['pool']).lower()
                alloc = int(m.groupdict()['alloc'])
                free = int(m.groupdict()['free'])

                if pool not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['bmp_pool_summary']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['bmp_pool_summary'][pool] = {}

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bmp_pool_summary'][pool]['alloc'] = alloc
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['bmp_pool_summary'][pool]['free'] = free
                continue
            elif m and not flag:
                if 'pool' not in ret_dict['instance'][instance]['vrf'][vrf] \
                        :
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['pool'] = {}

                pool = str(m.groupdict()['pool']).lower()
                alloc = int(m.groupdict()['alloc'])
                free = int(m.groupdict()['free'])

                if pool not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['pool']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['pool'][pool] = {}

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['pool'][pool]['alloc'] = alloc
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['pool'][pool]['free'] = free
                continue

            #                            Sent            Received
            # Updates:                   14              24
            # Notifications:             1               0

            m = p24_1.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['sent_updates'] = int(m.groupdict()['sent'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['received_updates'] = int(m.groupdict()['received'])
                continue

            #                            Sent            Received
            # Updates:                   14              24
            # Notifications:             1               0

            m = p24_2.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['sent_notifications'] = int(m.groupdict()['sent'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['received_notifications'] = int(m.groupdict()['received'])
                continue

            #                           Number          Memory Used
            # Attributes:                6               912
            # AS Paths:                  6               480
            # Communities:               0               0
            # Extended communities:      6               480
            # PMSI Tunnel attr:          0               0
            # RIBRNH Tunnel attr:        0               0
            # PPMP attr:                 0               0
            # Tunnel Encap attr:         0               0
            # PE distinguisher labels:   0               0
            # Route Reflector Entries:   4               320
            # Nexthop Entries:           32              12800


            m = p25.match(line)
            if m and not flag:
                if 'att' not in ret_dict['instance'][instance]['vrf'][vrf] \
                        :
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['att'] = {}

                att = str(m.groupdict()['att']).lower()
                att = att.replace(" ", "_")
                number = int(m.groupdict()['number'])
                memory_used = int(m.groupdict()['memory_used'])

                if att not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['att']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['att'][att] = {}

                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['att'][att]['number'] = number
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['att'][att]['memory_used'] = memory_used
                continue

            # Address family: VPNv4 Unicast

            m = p29.match(line)
            if m:
                af = str(m.groupdict()['af']).lower()
                af.strip()
                if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'] = {}
                if af not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af] = {}
                continue

            # VRF VRF1 Address family: IPv6 Unicast
            # VRF a Address family: IPv4 Unicast (Table inactive)

            m = p29_1.match(line)
            if m:
                af = str(m.groupdict()['af']).lower()
                af.strip()
                current_vrf = str(m.groupdict()['current_vrf']).lower()
                table_state = str(m.groupdict()['table_state'])

                if 'address_family' not in ret_dict['instance'][instance] \
                        ['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'] \
                        [vrf]['address_family'] = {}
                if af not in ret_dict['instance'][instance]['vrf'] \
                        [vrf]['address_family']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af] = {}
                ret_dict['instance'][instance]['vrf'][vrf]['address_family'] \
                    [af]['current_vrf'] = current_vrf
                ret_dict['instance'][instance]['vrf'][vrf]['address_family'] \
                    [af]['table_state'] = table_state
                continue

            # Dampening is not enabled

            m = p30.match(line)
            if m:
                dampening = m.groupdict()['dampening'].lower()
                if 'not enabled' in dampening:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['dampening'] = False
                else:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['dampening'] = True
                continue

            # Client reflection is enabled in global config

            m = p31.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['client_to_client_reflection'] = True
                continue

            # Client reflection is not enabled in global config

            m = p31_1.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['client_to_client_reflection'] = False
                continue

            # Dynamic MED is Disabled

            m = p32.match(line)
            if m:
                dynamic_med = m.groupdict()['dynamic_med'].lower()
                if status == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['dynamic_med'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['dynamic_med'] = False
                continue

            # Dynamic MED interval : 10 minutes

            m = p33.match(line)
            if m:
                interval = m.groupdict()['interval']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['dynamic_med_int'] = interval
                continue

            # Dynamic MED Timer : Not Running

            m = p34.match(line)
            if m:
                timer = m.groupdict()['dynamic_med_timer']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['dynamic_med_timer'] = timer
                continue

            # Dynamic MED Periodic Timer : Not Running

            m = p35.match(line)
            if m:
                timer = m.groupdict()['timer']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['dynamic_med_periodic_timer'] = timer
                continue

            # Scan interval: 60

            m = p36.match(line)
            if m:
                scan_interval = m.groupdict()['scan_interval']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['scan_interval'] = scan_interval
                continue

            # Total prefixes scanned: 40

            m = p37.match(line)
            if m:
                scan = m.groupdict()['scan']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['total_prefixes_scanned'] = scan
                continue

            # Prefixes scanned per segment: 100000

            m = p38.match(line)
            if m:
                prefix_scan = m.groupdict()['prefix_scan']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['prefix_scanned_per_segment'] = prefix_scan
                continue

            # Number of scan segments: 1

            m = p39.match(line)
            if m:
                ret = m.groupdict()['num_of_scan_segments']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['num_of_scan_segments'] = ret
                continue

            # Nexthop resolution minimum prefix-length: 0 (not configured)

            m = p40.match(line)
            if m:
                length = m.groupdict()['length']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af][
                    'nexthop_resolution_minimum_prefix_length'] = length
                continue

            # Main Table Version: 43

            m = p41.match(line)
            if m:
                main_tab_ver = m.groupdict()['main_tab_ver']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['main_table_version'] = main_tab_ver
                continue

            # Table version synced to RIB: 43

            m = p42.match(line)
            if m:
                rib = m.groupdict()['rib']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['table_version_synced_to_rib'] = rib
                continue

            # Table version acked by RIB: 0

            m = p43.match(line)
            if m:
                rib = m.groupdict()['rib']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['table_version_acked_by_rib'] = rib
                continue

            # RIB has not converged: version 0

            m = p44.match(line)
            if m:
                rib = m.groupdict()['rib']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['rib_has_not_converged'] = rib
                continue

            # RIB table prefix-limit reached ?  [No], version 0

            m = p54.match(line)
            if m:
                rib = m.groupdict()['rib'].lower()
                ver = m.groupdict()['ver']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['rib_table_prefix_limit_reached'] = rib
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['rib_table_prefix_limit_ver'] = ver
                continue

            # Permanent Network Unconfigured

            m = p45.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['permanent_network'] = status
                continue

            # State: Normal mode.

            m = p46.match(line)
            if m:
                state = m.groupdict()['state'].lower()
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['state'] = state
                continue

            # BGP Table Version: 43

            m = p47.match(line)
            if m:
                tab_ver = m.groupdict()['tab_ver']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['bgp_table_version'] = tab_ver
                continue

            # Attribute download: Disabled

            m = p48.match(line)
            if m:
                attr = str(m.groupdict()['attr'])
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['attribute_download'] = attr
                continue

            # Label retention timer value 5 mins

            m = p49.match(line)
            if m:
                timer = m.groupdict()['timer']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['label_retention_timer_value'] = timer
                continue

            # Soft Reconfig Entries: 0

            m = p50.match(line)
            if m:
                ent = m.groupdict()['ent']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['soft_reconfig_entries'] = ent
                continue

            # Table bit-field size : 1 Chunk element size : 3

            m = p51.match(line)
            if m:
                table_bit_field_size = m.groupdict()['size']
                chunk_elememt_size = m.groupdict()['elememt_size']
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['table_bit_field_size'] = table_bit_field_size
                ret_dict['instance'][instance]['vrf'][vrf] \
                    ['address_family'][af]['chunk_elememt_size'] = chunk_elememt_size
                continue

            #                    Last 8 Triggers       Ver         Tbl Ver     Trig TID  

            # Label Thread       Jun 28 19:10:16.427   43          43          3         
            #                    Jun 28 19:10:16.417   43          43          3         
            #                    Jun 28 19:09:29.680   43          43          3         
            #                    Jun 28 19:09:29.670   43          43          3         
            #                    Jun 28 18:29:34.604   43          43          3         
            #                    Jun 28 18:29:29.595   33          43          4         
            #                    Jun 28 18:29:29.595   33          38          3         
            #                    Jun 28 18:24:52.694   33          33          3       
            #                    Total triggers: 17


            m = p52.match(line)
            if m:
                if 'thread' not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'] = {}

                thread = m.groupdict()['thread'].lower().strip()
                if thread not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread] = {}

                if 'triggers' not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]['triggers'] = {}

                trigger = m.groupdict()['trigger']
                if trigger not in ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]['triggers']:
                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]['triggers'] \
                        [trigger] = {}

                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]['triggers'] \
                        [trigger]['tbl_ver'] = int(m.groupdict()['tbl_ver'])

                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]['triggers'] \
                        [trigger]['ver'] = int(m.groupdict()['ver'])

                    ret_dict['instance'][instance]['vrf'][vrf] \
                        ['address_family'][af]['thread'][thread]['triggers'] \
                        [trigger]['trig_tid'] = int(m.groupdict()['trig_tid'])
                continue

            #                       Allocated       Freed
            # Remote Prefixes:      10              0
            # Remote Path-elems:    10              0

            #                       Number          Mem Used      
            # Remote Prefixes:      10              920         
            # Remote Path-elems:    10              630

            if re.compile(r'^Allocated +Freed$').match(line):
                flag = 'allocated'
            if re.compile(r'^Number +Mem Used$').match(line):
                flag = 'number'


            m = p53.match(line)
            if m and flag == 'allocated':
                try:
                    af
                except Exception:
                    continue
                else:
                    if 'remote_local' not in ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]:
                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['remote_local'] = {}

                    remote = m.groupdict()['remote'].lower()
                    if remote not in ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['remote_local']:
                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['remote_local'][remote] = {}

                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['remote_local'][remote] \
                            ['allocated'] = int(m.groupdict()['v1'])

                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['remote_local'][remote] \
                            ['freed'] = int(m.groupdict()['v2'])
                    flag = None
                continue
            elif m and flag == 'number':
                try:
                    af
                except Exception:
                    continue
                else:
                    if 'prefixes_path' not in ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]:
                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['prefixes_path'] = {}

                    path = m.groupdict()['remote'].lower()
                    if path not in ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['prefixes_path']:
                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['prefixes_path'][path] = {}

                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['prefixes_path'][path] \
                            ['number'] = int(m.groupdict()['v1'])

                        ret_dict['instance'][instance]['vrf'][vrf] \
                            ['address_family'][af]['prefixes_path'][path] \
                            ['mem_used'] = int(m.groupdict()['v2'])
                    flag = None
                continue

        return ret_dict

    def yang(self, vrf_type, af_type=''):

        if not vrf_type in ['all', 'vrf']:
            raise Exception("Variable 'vrf_type' can only be 'all' or 'vrf'")

        # Init vars
        map_dict = {}

        # Execute YANG 'get' operational state RPC and parse the XML
        bgpOC = BgpOpenconfigYang(self.device)
        yang_dict = bgpOC.yang()

        # Map keys from yang_dict to map_dict

        # Add default instance
        if 'instance' not in map_dict:
            map_dict['instance'] = {}
        if 'default' not in map_dict['instance']:
            map_dict['instance']['default'] = {}

        # vrf
        for vrf in yang_dict['vrf']:
            if 'vrf' not in map_dict['instance']['default']:
                map_dict['instance']['default']['vrf'] = {}
            if vrf not in map_dict['instance']['default']['vrf']:
                map_dict['instance']['default']['vrf'][vrf] = {}
                sub_dict = map_dict['instance']['default']['vrf'][vrf]
            # as_number
            sub_dict['as_number'] = yang_dict['bgp_pid']
            # router_id
            sub_dict['router_id'] = \
                yang_dict['vrf'][vrf]['router_id']
            # graceful_restart
            if 'graceful_restart' in yang_dict['vrf'][vrf]:
                sub_dict['graceful_restart'] = \
                    yang_dict['vrf'][vrf]['graceful_restart']
            # graceful_restart_helper_only
            if 'graceful_restart_helper_only' in yang_dict['vrf'][vrf]:
                sub_dict['graceful_restart_helper_only'] = \
                    yang_dict['vrf'][vrf]['graceful_restart_helper_only']
            # graceful_restart_restart_time
            if 'graceful_restart_restart_time' in yang_dict['vrf'][vrf]:
                sub_dict['graceful_restart_restart_time'] = \
                    yang_dict['vrf'][vrf]['graceful_restart_restart_time']
            # graceful_restart_stalepath_time
            if 'graceful_restart_stalepath_time' in yang_dict['vrf'][vrf]:
                sub_dict['graceful_restart_stalepath_time'] = \
                    yang_dict['vrf'][vrf]['graceful_restart_stalepath_time']
            # log_neighbor_changes
            if 'log_neighbor_changes' in yang_dict['vrf'][vrf]:
                sub_dict['log_neighbor_changes'] = \
                    yang_dict['vrf'][vrf]['log_neighbor_changes']
            # address_family
            if 'address_family' in yang_dict['vrf'][vrf]:
                for af in yang_dict['vrf'][vrf]['address_family']:
                    if 'address_family' not in sub_dict:
                        sub_dict['address_family'] = {}
                    if af not in sub_dict['address_family']:
                        sub_dict['address_family'][af] = {}
                    sub_dict['address_family'][af] = \
                        yang_dict['vrf'][vrf]['address_family'][af]

        # Return to caller
        return map_dict


# =============================================================
# Parser for:
# 'show bgp instance all all all neighbors detail'
# 'show bgp instance all vrf all neighbors detail'
# 'show bgp instance all vrf all ipv4 unicast neighbors detail'
# 'show bgp instance all vrf all ipv6 unicast neighbors detail'
# =============================================================

class ShowBgpInstanceNeighborsDetailSchema(MetaParser):

    """Schema for:
        show bgp instance all all all neighbors detail
        show bgp instance all vrf all neighbors detail
        show bgp instance all vrf all ipv4 unicast neighbors detail
        show bgp instance all vrf all ipv6 unicast neighbors detail
    """

    schema = {
        'instance':
            {Any():
                {Optional('vrf'):
                    {Any():
                        {'neighbor':
                            {Any():
                                {Optional('description'): str,
                                 Optional('peer_group'): str,
                                 Optional('send_community'): str,
                                 Optional('input_queue'): int,
                                 Optional('output_queue'): int,
                                 Optional('graceful_restart'): bool,
                                 Optional('graceful_restart_helper_only'): bool,
                                 Optional('graceful_restart_restart_time'): int,
                                 Optional('graceful_restart_stalepath_time'): int,
                                 Optional('allow_own_as'): int,
                                 Optional('minimum_advertisement_interval'): int,
                                 Optional('route_reflector_client'): bool,
                                 Optional('route_reflector_cluster_id'): int,
                                 Optional('remote_as'): int,
                                 Optional('local_as_as_no'): int,
                                 Optional('local_as_no_prepend'): bool,
                                 Optional('local_as_replace_as'): bool,
                                 Optional('local_as_dual_as'): bool,
                                 Optional('remove_private_as'): bool,
                                 Optional('keepalive_interval'): int,
                                 Optional('holdtime'): int,
                                 Optional('min_acceptable_hold_time'): int,
                                 Optional('link_state'): str,
                                 Optional('router_id'): str,
                                 Optional('session_state'): str,
                                 Optional('up_time'): str,
                                 Optional('session_state_reason'): str,
                                 Optional('nsr_state'): str,
                                 Optional('last_read'): str,
                                 Optional('last_read_before_reset'): str,
                                 Optional('ebgp_multihop'): bool,
                                 Optional('ebgp_multihop_max_hop'): int,
                                 Optional('shutdown'): bool,
                                 Optional('suppress_four_byte_as_capability'): bool,
                                 Optional('last_write'): str,
                                 Optional('attempted'): int,
                                 Optional('written'): int,
                                 Optional('second_last_write'): str,
                                 Optional('second_attempted'): int,
                                 Optional('second_written'): int,
                                 Optional('last_write_before_reset'): str,
                                 Optional('last_write_attempted'): int,
                                 Optional('last_write_written'): int,
                                 Optional('second_last_write_before_reset'): str,
                                 Optional('second_last_write_before_attempted'): int,
                                 Optional('second_last_write_before_written'): int,
                                 Optional('last_write_pulse_rcvd'): str,
                                 Optional('last_full_not_set_pulse_count'): int,
                                 Optional('last_write_pulse_rcvd_before_reset'): str,
                                 Optional('socket_status'): str,
                                 Optional('last_write_thread_event_before_reset'): str,
                                 Optional('last_write_thread_event_second_last'): str,
                                 Optional('last_ka_expiry_before_reset'): str,
                                 Optional('last_ka_expiry_before_second_last'): str,
                                 Optional('last_ka_error_before_reset'): str,
                                 Optional('last_ka_error_ka_not_sent'): str,
                                 Optional('last_ka_start_before_reset'): str,
                                 Optional('last_ka_start_before_second_last'): str,
                                 Optional('precedence'): str,
                                 Optional('non_stop_routing'): bool,
                                 Optional('tcp_initial_sync'): str,
                                 Optional('tcp_initial_sync_phase_two'): str,
                                 Optional('tcp_initial_sync_done'): str, 
                                 Optional('enforcing_first_as'): str,
                                 Optional('multiprotocol_capability'): str,
                                 Optional('bgp_negotiated_keepalive_timers'):
                                    {Optional('hold_time'): int,
                                    Optional('keepalive_interval'): int
                                    },
                                 Optional('bgp_negotiated_capabilities'):
                                    {
                                        Any(): str
                                    },
                                 Optional('message_stats_input_queue'): int,
                                 Optional('message_stats_output_queue'): int,
                                 Optional('bgp_neighbor_counters'):
                                    {Optional('messages'):
                                         {Optional('sent'):
                                            {Any(): int,
                                            },
                                         Optional('received'):
                                            {Any(): int,
                                            },
                                        },
                                    },
                                 Optional('minimum_time_between_adv_runs'): int,
                                 Optional('inbound_message'): str,
                                 Optional('outbound_message'): str,
                                 Optional('address_family'):
                                    {Any():
                                        {Optional('enabled'): bool,
                                         Optional('graceful_restart'): bool,
                                         Optional('ipv4_unicast_send_default_route'): bool,
                                         Optional('ipv6_unicast_send_default_route'): bool,
                                         Optional('prefixes_received'): int,
                                         Optional('prefixes_sent'): int,
                                         Optional('active'): bool,
                                         Optional('neighbor_version'): int,
                                         Optional('update_group'): str,
                                         Optional('filter_group'): str,
                                         Optional('refresh_request_status'): str,
                                         Optional('route_refresh_request_received'): int,
                                         Optional('route_refresh_request_sent'): int,
                                         Optional('route_map_name_in'): str,
                                         Optional('route_map_name_out'): str,
                                         Optional('accepted_prefixes'): int,
                                         Optional('best_paths'): int,
                                         Optional('exact_no_prefixes_denied'): int,
                                         Optional('cummulative_no_prefixes_denied'): int,
                                         Optional('cummulative_no_no_policy'): int,
                                         Optional('cummulative_no_failed_rt_match'): int,
                                         Optional('cummulative_no_by_orf_policy'): int,
                                         Optional('cummulative_no_by_policy'): int,
                                         Optional('prefix_advertised'): int,
                                         Optional('prefix_suppressed'): int,
                                         Optional('prefix_withdrawn'): int,
                                         Optional('maximum_prefix_max_prefix_no'): int,
                                         Optional('maximum_prefix_threshold'): str,
                                         Optional('maximum_prefix_restart'): int,
                                         Optional('maximum_prefix_warning_only'): bool,
                                         Optional('eor_status'): str,
                                         Optional('last_ack_version'): int,
                                         Optional('last_synced_ack_version'): int,
                                         Optional('outstanding_version_objects_current'): int,
                                         Optional('outstanding_version_objects_max'): int,
                                         Optional('additional_paths_operation'): str,
                                         Optional('additional_routes_local_label'): str,
                                         Optional('allowas_in'): bool,
                                         Optional('allowas_in_as_number'): int,
                                         Optional('route_reflector_client'): bool,
                                         Optional('send_community'): str,
                                         Optional('soft_configuration'): bool,
                                         Optional('as_override'): bool,
                                         Optional('default_originate'): bool,
                                         Optional('default_originate_route_map'): str,
                                         Optional('send_multicast_attributes'): bool,
                                         Optional('soo'): str
                                         },
                                    },
                                 Optional('bgp_session_transport'):
                                     {Optional('connection'):
                                        {Optional('state'): str,
                                         Optional('mode'): str,
                                         Optional('last_reset'): str,
                                         Optional('reset_reason'): str,                                                     
                                         Optional('connections_established'): int,
                                         Optional('connections_dropped'): int
                                        },
                                    Optional('transport'):
                                        {Optional('local_host'): str,
                                         Optional('local_port'): str,
                                         Optional('if_handle'): str,
                                         Optional('foreign_host'): str,
                                         Optional('foreign_port'): str,
                                         Optional('mss'): str,
                                         Optional('passive_mode'): str
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpInstanceNeighborsDetail(ShowBgpInstanceNeighborsDetailSchema):

    """ Parser for:
        show bgp instance all all all neighbors detail
        show bgp instance all vrf all neighbors detail
        show bgp instance all vrf all ipv4 unicast neighbors detail
        show bgp instance all vrf all ipv6 unicast neighbors detail
        show bgp instance <instance> vrf <vrf> <address_family> neighbors <neighbor> detail
        For checking any output with the parser ,below mandatory keys have to be in cli command.

        - vrf_type
    """

    cli_command = ['show bgp instance {instance} all all neighbors detail',
        'show bgp instance {instance} all all neighbors {neighbor} detail',
        'show bgp instance {instance} {vrf_type} {vrf} neighbors {neighbor} detail',
        'show bgp instance {instance} {vrf_type} {vrf} {address_family} neighbors {neighbor} detail',
       'show bgp instance {instance} {vrf_type} {vrf} neighbors detail',
       'show bgp instance {instance} {vrf_type} {vrf} {address_family} neighbors detail']

    exclude = ['bgp_table_version', 'rd_version', 'nsr_initial_init_ver_status', 
        'nsr_initial_initsync_version', 'filter_group', 'last_ack_version', 'neighbor_version',
        'prefix_advertised', 'prefix_withdrawn', 'update_group', 'attempted', 'keepalives', 
        'opens', 'updates', 'connections_dropped', 'connections_established', 'foreign_port', 
        'last_full_not_set_pulse_count', 'last_ka_expiry_before_reset', 'last_ka_expiry_before_second_last',
        'last_read', 'last_read_before_reset', 'last_write', 'last_write_attempted', 
        'last_write_before_reset', 'last_write_pulse_rcvd', 'last_write_pulse_rcvd_before_reset',
        'last_write_thread_event_before_reset', 'last_write_thread_event_second_last', 
        'last_write_written', 'second_attempted', 'second_last_write', 'second_last_write_before_attempted',
        'second_last_write_before_reset', 'second_last_write_before_written', 'second_written', 'up_time',
        'written', 'eor_status', 'local_port', 'last_reset', 'last_ka_start_before_reset', 'last_ka_start_before_second_last', 'totals',
        'cummulative_no_prefixes_denied', 'route_refresh_request_sent',
        'cummulative_no_by_orf_policy', 'cummulative_no_by_policy', 'cummulative_no_failed_rt_match'
        , 'cummulative_no_no_policy', 'route_refresh_request_sent']

        
    def cli(self, vrf_type='all', vrf='all', instance='all', neighbor='', address_family='', output=None):
        assert vrf_type in ['all', 'vrf']
        assert address_family in ['', 'ipv4 unicast', 'ipv6 unicast']
        if output is None:
            if vrf_type == 'all':
                if neighbor:
                    out = self.device.execute(self.cli_command[1].format(instance=instance,
                                                                         neighbor=neighbor))
                else:
                    out = self.device.execute(self.cli_command[0].format(instance=instance))

            else:
                if address_family:
                    if neighbor:
                        out = self.device.execute(self.cli_command[3].format(vrf_type=vrf_type,
                                                                     instance=instance,
                                                                     neighbor=neighbor,
                                                                     vrf=vrf,
                                                                     address_family=address_family))
                    else:
                        out = self.device.execute(self.cli_command[5].format(vrf_type=vrf_type,
                                                       instance=instance,
                                                       address_family=address_family,
                                                                             vrf=vrf))
                else:
                    if neighbor:
                        out = self.device.execute(self.cli_command[2].format(vrf_type=vrf_type,
                                                   instance=instance,
                                                   neighbor=neighbor,
                                                   vrf=vrf))
                    else:
                        out = self.device.execute(self.cli_command[4].format(vrf_type=vrf_type,
                                                   instance=instance,
                                                   vrf=vrf))
        else:
            out = output
        # Init variables
        ret_dict = {}
        p1 = re.compile(r'^BGP +instance +(?P<instance_number>[0-9]+): +'
                            '(?P<instance>[a-zA-Z0-9\-\_\']+)$')
        p2 =  re.compile(r'^\s*BGP +neighbor +is +(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
        p2_1 =  re.compile(r'^\s*BGP +neighbor +is +(?P<neighbor>[a-zA-Z0-9\.\:]+), +vrf +(?P<vrf>\S+)$')
        p3 = re.compile(r'^Remote +AS +(?P<remote_as>[0-9]+), +local +AS +(?P<local_as_as_no>[0-9]+)(?:, +(?P<local_as_no_prepend>no-prepend))?(?:, +(?P<local_as_replace_as>replace-as))?(?:, +(?P<local_as_dual_as>dual-as))?(?:, +(?P<link_state>[a-zA-Z\s]+))?$')
        p4 = re.compile(r'^Remote *router *ID *(?P<router_id>[a-zA-Z0-9\.\:]+)$')
        p5 = re.compile(r'^\s*BGP +state += +(?P<session_state>[a-zA-Z0-9]+)'
                            '(?:, +up +for +(?P<up_time>[\w\:]+))?$')
        p5_1 = re.compile(r'^\s*BGP +state += +(?P<session_state>[a-zA-Z0-9]+)(?:(?P<reason>.*))')
        p6 = re.compile(r'^NSR *State: *(?P<nsr_state>[a-zA-Z]+)$')
        p7 = re.compile(r'^Last *read *(?P<last_read>[0-9\:]+), *Last *read *before *reset *(?P<last_read_before_reset>[0-9\:]+)$')
        p8 = re.compile(r'^Hold +time +is +(?P<holdtime>[0-9]+), +keepalive'
                            ' +interval +is +(?P<keepalive_interval>[0-9]+)'
                            ' +seconds$')
        p9 = re.compile(r'^Configured +hold +time:'
                            ' +(?P<holdtime>[0-9]+), +keepalive:'
                            ' +(?P<keepalive_interval>[0-9]+), +min'
                            ' +acceptable +hold +time:'
                            ' +(?P<min_acceptable_hold_time>[0-9]+)$')
        p10 = re.compile(r'^Last *write *(?P<last_write>[0-9\:]+), *attempted *(?P<attempted>[0-9]+), *written *(?P<written>[0-9]+)$')
        p11 = re.compile(r'^Second *last *write *(?P<second_last_write>[0-9\:]+), *attempted *(?P<second_attempted>[0-9]+), *written *(?P<second_written>[0-9]+)$')
        p12 = re.compile(r'^Last *write *before *reset *(?P<last_write_before_reset>[0-9\:]+), *attempted *(?P<last_write_attempted>[0-9]+), *written *(?P<last_write_written>[0-9]+)$')
        p13 = re.compile(r'^Second *last *write *before *reset *(?P<second_last_write_before_reset>[0-9\:]+), *attempted *(?P<second_last_write_before_attempted>[0-9]+), written *(?P<second_last_write_before_written>[0-9]+)$')
        p14 =  re.compile(r'^Last *write *pulse *rcvd *(?P<last_write_pulse_rcvd>[a-zA-Z0-9\:\.\s]+) *last *full *not *set *pulse *count *(?P<last_full_not_set_pulse_count>[0-9]+)$')
        p15 = re.compile(r'^Last +write +pulse +rcvd +before +reset +(?P<last_write_pulse_rcvd_before_reset>[0-9\:]+)$')
        p15_1 = re.compile(r'^Socket *(?P<socket_status>[a-z\s\,])$')
        p16 =  re.compile(r'^Last *write *thread *event *before *reset *(?P<last_write_thread_event_before_reset>[0-9\:]+), *second *last *(?P<last_write_thread_event_second_last>[0-9\:]+)$')
        p17 = re.compile(r'^Last *KA *expiry *before *reset *(?P<last_ka_expiry_before_reset>[0-9\:]+), *second *last *(?P<last_ka_expiry_before_second_last>[0-9\:]+)$')
        p18 = re.compile(r'^Last *KA *error *before *reset *(?P<last_ka_error_before_reset>[0-9\:]+), *KA *not *sent *(?P<last_ka_error_ka_not_sent>[0-9\:]+)$')
        p19 =  re.compile(r'^Last *KA *start *before *reset *(?P<last_ka_start_before_reset>[0-9\:]+), *second *last *(?P<last_ka_start_before_second_last>[0-9\:]+)$')
        p20 =  re.compile(r'^Precedence: *(?P<precedence>[a-z]+)$')
        p21 =  re.compile(r'^Non-stop +routing +is +enabled$')
        p22 =  re.compile(r'^TCP *Initial *Sync :(?: *(?P<tcp_initial_sync>[a-zA-Z0-9\-\s]+))?$')
        p23 = re.compile(r'^TCP *Initial *Sync *phase *Two :(?: *(?P<tcp_initial_sync_phase_two>[a-zA-Z0-9\-\s]+))?$')
        p24 = re.compile(r'^TCP *Initial *Sync *Done :(?: *(?P<tcp_initial_sync_done>[a-zA-Z0-9\-\s]+))?$')
        p25 = re.compile(r'^Enforcing *first *AS is *(?P<enforcing_first_as>[a-z]+)$')
        p26 =  re.compile(r'^Multi-protocol *capability *(?P<multiprotocol_capability>[a-zA-Z\s]+)$')
        p27 = re.compile(r'^Neighbor +capabilities: +Adv +Rcvd$')
        p27_1= re.compile(r'^(Address +family +)?(?P<name>[a-zA-Z0-9\s\-]+): *(?P<adv>(Y|y)es|(N|n)o) *(?P<rcvd>(Y|y)es|(N|n)o+)$')
        p28 = re.compile(r'^InQ *depth: *(?P<message_stats_input_queue>[0-9]+), *OutQ *depth: *(?P<message_stats_output_queue>[0-9]+)$')
        p29 = re.compile(r'^(?P<name>[a-zA-Z\s]+) *: *'
                            '(?P<last_sent>\w+ *\d+ *[\d\:\.]+) *'
                            '(?P<sent>[0-9]+) *'
                            '(?P<last_received>\w+ *\d+ *[\d\:\.\-]+) *'
                            '(?P<received>[0-9]+)$')
        p29_1 = re.compile(r'^(?P<name>[a-zA-Z\s]+) *: *'
                            '(?P<last_sent>[\-]+) *'
                            '(?P<sent>[0-9]+) *'
                            '(?P<last_received>[\-]+) *'
                            '(?P<received>[0-9]+)$')
        p30 = re.compile(r'^Minimum *time *between *advertisement *runs *is *(?P<minimum_time_between_adv_runs>[0-9]+) *secs$')
        p31 = re.compile(r'^Inbound *message *logging *enabled, *(?P<inbound_message>[0-9]+) *messages *buffered$')
        p32 = re.compile(r'^Outbound *message *logging *enabled, *(?P<outbound_message>[0-9]+) *messages *buffered$')
        p33 = re.compile(r'^For +Address +Family *: +(?P<address_family>[\S\s]+)$')
        p34 = re.compile(r'^BGP +neighbor +version'
                            ' +(?P<neighbor_version>[0-9]+)$')
        p35 = re.compile(r'^Update +group: +(?P<update_group>[0-9\.]+) +Filter-group: +(?P<filter_group>[0-9\.]+) +(?P<refresh_request_status>[a-zA-Z\s]+)$')
        p36 = re.compile(r'^Route *refresh *request: *received *(?P<route_refresh_request_received>[0-9]+), *sent *(?P<route_refresh_request_sent>[0-9]+)$')
        p37 = re.compile(r'^Policy *for *incoming *advertisements *is *(?P<route_map_name_in>[\w\-\_]+)$')
        p38 = re.compile(r'^Policy *for *outgoing *advertisements *is *(?P<route_map_name_out>[\w\-\_]+)$')
        p39 = re.compile(r'^(?P<accepted_prefixes>[0-9]+) *accepted *prefixes, *(?P<best_paths>[0-9]+) *are *bestpaths$')
        p40 = re.compile(r'^Exact *no\. *of *prefixes *denied *: *(?P<exact_no_prefixes_denied>[0-9]+)\.$')
        p41 = re.compile(r'^Cumulative *no\. *of *prefixes *denied: *(?P<cummulative_no_prefixes_denied>[0-9]+)\.$')
        p42 = re.compile(r'^No *policy: *(?P<cummulative_no_no_policy>[0-9]+), *Failed *RT *match: *(?P<cummulative_no_failed_rt_match>[0-9]+)$')
        p43 = re.compile(r'^By *ORF *policy: *(?P<cummulative_no_by_orf_policy>[0-9]+), *By *policy: *(?P<cummulative_no_by_policy>[0-9]+)$')
        p44 = re.compile(r'^Prefix +advertised +(?P<prefix_advertised>[0-9]+), +suppressed +(?P<prefix_suppressed>[0-9]+), +withdrawn +(?P<prefix_withdrawn>[0-9]+)$')
        p45 = re.compile(r'^Maximum +prefixes +allowed'
                        ' +(?P<maximum_prefix_max_prefix_no>[0-9]+)$')
        p46 = re.compile(r'^Threshold +for +(?P<warn>warning)? *message +(?P<threshold_warning_message>[0-9\%]+), +restart +interval +(?P<threshold_restart_interval>[0-9]+) +min$')
        p47 = re.compile(r'^An *EoR *(?P<eor_status>[a-z\-\s]+)$')
        p48 = re.compile(r'^Last *ack *version *(?P<last_ack_version>[0-9]+), *Last *synced *ack *version *(?P<last_synced_ack_version>[0-9]+)$')
        p49 = re.compile(r'^Outstanding +version +objects: +current +(?P<outstanding_version_objects_current>[0-9]+), +max +(?P<outstanding_version_objects_max>[0-9]+)$')
        p50 = re.compile(r'^Additional-paths +operation: +(?P<additional_paths_operation>[a-zA-Z]+)$')
        p50_1 = re.compile(r'^Advertise +routes +with +local-label +via +(?P<additional_routes_local_label>[a-zA-Z\s]+)$')
        p50_2 = re.compile(r'^Send +Multicast +Attributes$')
        p51 = re.compile(r'^Connections *(?P<bgp_state>\w+) *'
                            '(?P<num>[0-9]+)\; *dropped *(?P<connections_dropped>[0-9]+)$')
        p52 = re.compile(r'^Local *host: *(?P<local_host>[\w\.\:]+), *Local *port: *(?P<local_port>[0-9]+), *IF *Handle: *(?P<if_handle>[a-z0-9]+)$')
        p53 = re.compile(r'^Foreign *host: *(?P<foreign_host>[\w\.\:]+), *Foreign *port: *(?P<foreign_port>[0-9]+)$')
        p54 = re.compile(r'^Last *reset *(?P<last_reset>[0-9\:]+)$')
        p55 = re.compile(r'^Capability +4-byte-as +suppress +is +configured$')
        p56 = re.compile(r'^Description: +(?P<description>[\w\s\,\.\:\-]+)$')
        p57 = re.compile(r'^Private +AS +number +removed +from +updates +to +this +neighbor$')
        p58 = re.compile(r'^Administratively +shut +down$')
        p59 = re.compile(r'^External +BGP +neighbor +may +be +up +to +'
                            '(?P<hop>\d+) +hops +away$')
        p60 = re.compile(r'^TCP +open +mode: +(?P<mode>[\w\s]+)$')
        p61 = re.compile(r'^My +AS +number +is +allowed +(?P<num>\d+) +'
                            'times +in +received +updates$')
        p62 = re.compile(r'^Route\-Reflector +Client$')
        p63 = re.compile(r'^(?P<send_com>\w+) +community +attribute +sent +to +this +neighbor$')
        p64 = re.compile(r'^Inbound +soft +reconfiguration +allowed$')
        p65 = re.compile(r'^AS +override +is +set$')
        p66 = re.compile(r'^Default +information +originate: +(?P<route_map>[\w\s\-]:)$')
        p67 = re.compile(r'^site\-of\-origin +(?P<soo>[\w\:]+)$')
        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'

            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                instance_number = int(m.groupdict()['instance_number'])
                instance = instance.replace("'","")
                # Set instance
                ret_dict.setdefault('instance', {}).setdefault(instance, {})
                continue

            # BGP neighbor is 10.16.2.2

            m = p2.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                vrf = 'default'
                ret_dict.setdefault('instance', {}).setdefault(instance, {})
                # Set vrf
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                # Set neighbor
                if 'neighbor' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]['neighbor'] = {}
                if neighbor not in ret_dict['instance'][instance]['vrf'][vrf]['neighbor']:
                    ret_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor] = {}
                sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]
                continue

            # BGP neighbor is 10.1.5.5, vrf VRF1

            m = p2_1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                vrf = str(m.groupdict()['vrf'])
                ret_dict.setdefault('instance',{}).setdefault(instance,{})
                # Set vrf
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                # Set neighbor
                if 'neighbor' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]['neighbor'] = {}
                if neighbor not in ret_dict['instance'][instance]['vrf'][vrf]['neighbor']:
                    ret_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor] = {}
                sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]
                
                # Default values - overwritten if configured
                sub_dict['suppress_four_byte_as_capability'] = False
                sub_dict['remove_private_as'] = False
                sub_dict['shutdown'] = False
                continue
            
            # Remote AS 200, local AS 100, external link
            # Remote AS 200, local AS 100, no-prepend, replace-as, dual-as, external link
            m = p3.match(line)
            if m:
                sub_dict['remote_as'] = int(m.groupdict()['remote_as'])
                if m.groupdict()['link_state']:
                    sub_dict['link_state'] = m.groupdict()['link_state']
                sub_dict['local_as_as_no'] = int(m.groupdict()['local_as_as_no'])

                if m.groupdict()['local_as_no_prepend']:
                    sub_dict['local_as_no_prepend'] = True
                else:
                    sub_dict['local_as_no_prepend'] = False
                if m.groupdict()['local_as_replace_as']:
                    sub_dict['local_as_replace_as'] = True
                else:
                    sub_dict['local_as_replace_as'] = False
                if m.groupdict()['local_as_dual_as']:
                    sub_dict['local_as_dual_as'] = True
                else:
                    sub_dict['local_as_dual_as'] = False
                continue

            # Remote router ID 10.1.5.5

            m = p4.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])

                sub_dict['router_id'] = router_id
                continue

            # BGP state = Established, up for 00:53:54

            m = p5.match(line)
            if m:
                session_state = str(m.groupdict()['session_state']).lower()

                sub_dict['session_state'] = session_state
                if m.groupdict()['up_time']:
                    sub_dict['up_time'] = str(m.groupdict()['up_time'])
                continue

            # BGP state = Idle (No route to multi-hop neighbor)

            m = p5_1.match(line)
            if m:
                session_state = str(m.groupdict()['session_state']).lower()
                sub_dict['session_state'] = session_state
                if m.groupdict()['reason']:
                    sub_dict['session_state_reason'] =  str(m.groupdict()['reason'])
                continue

            # NSR State: None

            m = p6.match(line)
            if m:
                nsr_state = str(m.groupdict()['nsr_state'])

                sub_dict['nsr_state'] = nsr_state
                continue

            # Last read 00:00:51, Last read before reset 00:00:00

            m = p7.match(line)
            if m:
                last_read = str(m.groupdict()['last_read'])
                last_read_before_reset = str(m.groupdict()['last_read_before_reset'])

                sub_dict['last_read'] = last_read
                sub_dict['last_read_before_reset'] = last_read_before_reset
                continue

            # Hold time is 180, keepalive interval is 60 seconds

            m = p8.match(line)
            if m:
                sub_dict['holdtime'] = int(m.groupdict()['holdtime'])
                sub_dict['keepalive_interval'] = \
                    int(m.groupdict()['keepalive_interval'])
                continue

            # Configured hold time: 180, keepalive: 60, min acceptable hold time: 3

            m = p9.match(line)
            if m:
                sub_dict['holdtime'] = int(m.groupdict()['holdtime'])
                sub_dict['keepalive_interval'] = \
                    int(m.groupdict()['keepalive_interval'])
                sub_dict['min_acceptable_hold_time'] = \
                    int(m.groupdict()['min_acceptable_hold_time'])
                continue

            # Last write 00:00:38, attempted 19, written 19

            m = p10.match(line)
            if m:
                last_write = str(m.groupdict()['last_write'])
                attempted = int(m.groupdict()['attempted'])
                written = int(m.groupdict()['written'])

                sub_dict['last_write'] = last_write
                sub_dict['attempted'] = attempted
                sub_dict['written'] = written
                continue

            # Second last write 00:01:38, attempted 19, written 19

            m = p11.match(line)
            if m:
                second_last_write = str(m.groupdict()['second_last_write'])
                second_attempted = int(m.groupdict()['second_attempted'])
                second_written = int(m.groupdict()['second_written'])

                sub_dict['second_last_write'] = second_last_write
                sub_dict['second_attempted'] = second_attempted
                sub_dict['second_written'] = second_written
                continue

            # Last write before reset 00:00:00, attempted 0, written 0

            m = p12.match(line)
            if m:
                last_write_before_reset = str(m.groupdict()['last_write_before_reset'])
                last_write_attempted = int(m.groupdict()['last_write_attempted'])
                last_write_written = int(m.groupdict()['last_write_written'])

                sub_dict['last_write_before_reset'] = last_write_before_reset
                sub_dict['last_write_attempted'] = last_write_attempted
                sub_dict['last_write_written'] = last_write_written
                continue

            # Second last write before reset 00:00:00, attempted 0, written 0

            m = p13.match(line)
            if m:
                second_last_write_before_reset =  str(m.groupdict()['second_last_write_before_reset'])
                second_last_write_before_attempted = int(m.groupdict()['second_last_write_before_attempted'])
                second_last_write_before_written = int(m.groupdict()['second_last_write_before_written'])

                sub_dict['second_last_write_before_reset'] = second_last_write_before_reset
                sub_dict['second_last_write_before_attempted'] = second_last_write_before_attempted
                sub_dict['second_last_write_before_written'] = second_last_write_before_written
                continue

            # Last write pulse rcvd  Jun 28 19:17:44.716 last full not set pulse count 113

            m = p14.match(line)
            if m:
                last_write_pulse_rcvd = str(m.groupdict()['last_write_pulse_rcvd'])
                last_full_not_set_pulse_count = int(m.groupdict()['last_full_not_set_pulse_count'])

                sub_dict['last_write_pulse_rcvd'] = last_write_pulse_rcvd
                sub_dict['last_full_not_set_pulse_count'] = last_full_not_set_pulse_count
                continue

            # Last write pulse rcvd before reset 00:00:00

            m = p15.match(line)
            if m:
                last_write_pulse_rcvd_before_reset = str(m.groupdict()['last_write_pulse_rcvd_before_reset'])

                sub_dict['last_write_pulse_rcvd_before_reset'] = last_write_pulse_rcvd_before_reset
                continue

            # Socket not armed for io, armed for read, armed for write

            m = p15_1.match(line)
            if m:
                socket_status = str(m.groupdict()['socket_status'])

                sub_dict['socket_status'] =socket_status
                continue

            # Last write thread event before reset 00:00:00, second last 00:00:00

            m = p16.match(line)
            if m:
                last_write_thread_event_before_reset = str(m.groupdict()['last_write_thread_event_before_reset'])
                last_write_thread_event_second_last = str(m.groupdict()['last_write_thread_event_second_last'])

                sub_dict['last_write_thread_event_before_reset'] = last_write_thread_event_before_reset
                sub_dict['last_write_thread_event_second_last'] = last_write_thread_event_second_last
                continue

            # Last KA expiry before reset 00:00:00, second last 00:00:00

            m = p17.match(line)
            if m:
                last_ka_expiry_before_reset =  str(m.groupdict()['last_ka_expiry_before_reset'])
                last_ka_expiry_before_second_last = str(m.groupdict()['last_ka_expiry_before_second_last'])

                sub_dict['last_ka_expiry_before_reset'] = last_ka_expiry_before_reset
                sub_dict['last_ka_expiry_before_second_last'] = last_ka_expiry_before_second_last
                continue

            # Last KA error before reset 00:00:00, KA not sent 00:00:00

            m = p18.match(line)
            if m:
                last_ka_error_before_reset = str(m.groupdict()['last_ka_error_before_reset'])
                last_ka_error_ka_not_sent = str(m.groupdict()['last_ka_error_ka_not_sent'])

                sub_dict['last_ka_error_before_reset'] = last_ka_error_before_reset
                sub_dict['last_ka_error_ka_not_sent'] = last_ka_error_ka_not_sent
                continue
            
            # Last KA start before reset 00:00:00, second last 00:00:00

            m = p19.match(line)
            if m:
                last_ka_start_before_reset = str(m.groupdict()['last_ka_start_before_reset'])
                last_ka_start_before_second_last = str(m.groupdict()['last_ka_start_before_second_last'])

                sub_dict['last_ka_start_before_reset'] = last_ka_start_before_reset
                sub_dict['last_ka_start_before_second_last'] = last_ka_start_before_second_last
                continue

            # Precedence: internet
            m = p20.match(line)
            if m:
                precedence = str(m.groupdict()['precedence'])

                sub_dict['precedence'] = precedence
                continue

            # Non-stop routing is enabled

            m = p21.match(line)
            if m:
                sub_dict['non_stop_routing'] = True
                continue

            # TCP Initial Sync :              ---                   

            m = p22.match(line)
            if m:
                tcp_initial_sync = str(m.groupdict()['tcp_initial_sync'])

                sub_dict['tcp_initial_sync'] = tcp_initial_sync
                continue

            # TCP Initial Sync Phase Two :    ---

            m = p23.match(line)
            if m:
                tcp_initial_sync_phase_two = str(m.groupdict()['tcp_initial_sync_phase_two'])

                sub_dict['tcp_initial_sync_phase_two'] = tcp_initial_sync_phase_two
                continue

            # TCP Initial Sync Done :         ---
            m = p24.match(line)
            if m:
                tcp_initial_sync_done = str(m.groupdict()['tcp_initial_sync_done']) 

                sub_dict['tcp_initial_sync_done'] = tcp_initial_sync_done
                continue             
            
            # Enforcing first AS is enabled

            m = p25.match(line)
            if m:
                enforcing_first_as = str(m.groupdict()['enforcing_first_as'])

                sub_dict['enforcing_first_as'] = enforcing_first_as
                continue

            # Multi-protocol capability not received

            m = p26.match(line)
            if m:
                multiprotocol_capability = str(m.groupdict()['multiprotocol_capability'])

                sub_dict['multiprotocol_capability'] = multiprotocol_capability
                continue

            # Neighbor capabilities:            Adv         Rcvd

            m = p27.match(line)
            if m:
                if 'bgp_negotiated_capabilities' not in sub_dict:
                    sub_dict['bgp_negotiated_capabilities'] = {}

            #    Route refresh:                  Yes         No
            #    4-byte AS:                      Yes         No
            #    Address family IPv4 Unicast:    Yes         Yes

            m = p27_1.match(line)
            if m:
                name = m.groupdict()['name'].lower()
                adv = 'advertised' if m.groupdict()['adv'].lower() == 'yes' else ''
                rcvd = 'received' if m.groupdict()['rcvd'].lower() == 'yes' else ''
                # mapping ops name

                if 'enhanced refresh' in name:
                    name = 'enhanced_refresh'
                elif '4-byte' in name:
                    name = 'four_octets_asn'
                elif 'restart' in name:
                    name = 'graceful_restart'
                elif 'multi' in name:
                    name = 'multisession'
                elif 'switchover' in name:
                    name = 'stateful_switchover'
                else:
                    name = name.replace(' ', '_')
                sub_dict['bgp_negotiated_capabilities'][name] = adv + ' ' + rcvd
                continue

            #  Message stats:
            #    InQ depth: 0, OutQ depth: 0

            m = p28.match(line)
            if m:
                message_stats_output_queue = int(m.groupdict()['message_stats_output_queue'])
                message_stats_input_queue = int(m.groupdict()['message_stats_input_queue'])

                sub_dict['message_stats_output_queue'] = message_stats_output_queue
                sub_dict['message_stats_input_queue'] = message_stats_input_queue
                continue
           
            #                    Last_Sent               Sent  Last_Rcvd               Rcvd
            #    Open:           Jun 28 18:24:28.875        1  Jun 28 18:24:28.875        1
            #    Notification:   ---                        0  ---                        0
            #    Notification:   Feb  2 15:59:59.043        1  ---                        0
            #    Update:         Jun 28 18:28:43.838        2  Jun 28 18:24:29.135        1
            #    Keepalive:      Jun 28 19:17:44.616       55  Jun 28 19:17:31.987       54
            #    Route_Refresh:  ---                        0  ---                        0
            #    Total:                                    58                            56

            m = p29.match(line)


            m1 = p29_1.match(line)
            if m or m1:
                if 'bgp_neighbor_counters' not in sub_dict:
                    sub_dict['bgp_neighbor_counters'] = {}
                if 'messages' not in sub_dict['bgp_neighbor_counters']:
                    sub_dict['bgp_neighbor_counters']['messages'] = {}
                if 'sent' not in sub_dict['bgp_neighbor_counters']['messages']:
                    sub_dict['bgp_neighbor_counters']['messages']['sent'] = {}
                if 'received' not in sub_dict['bgp_neighbor_counters']['messages']:
                    sub_dict['bgp_neighbor_counters']['messages']['received'] = {}
                
                # keep the name same as ops
                m = m or m1
                name = m.groupdict()['name'].lower() + 's'
                sub_dict['bgp_neighbor_counters']['messages']['sent'][name] = \
                    int(m.groupdict()['sent'])
                sub_dict['bgp_neighbor_counters']['messages']['received'][name] = \
                    int(m.groupdict()['received'])
                continue

            # Minimum time between advertisement runs is 0 secs

            m = p30.match(line)
            if m:
                minimum_time_between_adv_runs = int(m.groupdict()['minimum_time_between_adv_runs'])

                sub_dict['minimum_time_between_adv_runs'] = minimum_time_between_adv_runs
                continue

            # Inbound message logging enabled, 3 messages buffered

            m = p31.match(line)
            if m:
                inbound_message = str(m.groupdict()['inbound_message'])

                sub_dict['inbound_message'] = inbound_message
                continue

            # Outbound message logging enabled, 3 messages buffered

            m =p32.match(line)
            if m:
                outbound_message = str(m.groupdict()['outbound_message'])

                sub_dict['outbound_message'] = outbound_message
                continue

            # For Address Family: IPv4 Unicast

            m = p33.match(line)            
            if m:
                address_family = str(m.groupdict()['address_family']).lower()
                address_family.strip()

                if 'address_family' not in sub_dict:
                    sub_dict['address_family'] = {}
                if address_family not in sub_dict['address_family']:
                    sub_dict['address_family'][address_family] = {}
                    continue
            
            # BGP neighbor version 43

            m = p34.match(line)
            if m:
                sub_dict['address_family'][address_family]['neighbor_version'] =\
                    int(m.groupdict()['neighbor_version'])
                continue
            
            # Update group: 0.2 Filter-group: 0.2  No Refresh request being processed

            m = p35.match(line)
            if m:
                update_group = str(m.groupdict()['update_group'])
                filter_group = str(m.groupdict()['filter_group'])
                refresh_request_status = str(m.groupdict()['refresh_request_status'])

                sub_dict['address_family'][address_family]['update_group'] = update_group
                sub_dict['address_family'][address_family]['filter_group'] = filter_group
                sub_dict['address_family'][address_family]['refresh_request_status'] = refresh_request_status
                continue

            # Route refresh request: received 0, sent 0

            m = p36.match(line)
            if m:
                route_refresh_request_received = int(m.groupdict()['route_refresh_request_received'])
                route_refresh_request_sent = int(m.groupdict()['route_refresh_request_sent'])

                sub_dict['address_family'][address_family]['route_refresh_request_received'] = route_refresh_request_received
                sub_dict['address_family'][address_family]['route_refresh_request_sent'] = route_refresh_request_sent
                continue

            # Policy for incoming advertisements is all-pass

            m = p37.match(line)
            if m:
                route_map_name_in = m.groupdict()['route_map_name_in']

                sub_dict['address_family'][address_family]['route_map_name_in'] = route_map_name_in
                continue

            # Policy for outgoing advertisements is all-pass

            m = p38.match(line)
            if m:
                route_map_name_out = m.groupdict()['route_map_name_out']

                sub_dict['address_family'][address_family]['route_map_name_out'] = route_map_name_out
                continue

            # 0 accepted prefixes, 0 are bestpaths

            m = p39.match(line)
            if m:
                accepted_prefixes = int(m.groupdict()['accepted_prefixes'])
                best_paths = int(m.groupdict()['best_paths'])

                sub_dict['address_family'][address_family]['accepted_prefixes'] = accepted_prefixes
                sub_dict['address_family'][address_family]['best_paths'] = best_paths
                continue

            # Exact no. of prefixes denied : 0.

            m = p40.match(line)
            if m:
                exact_no_prefixes_denied = int(m.groupdict()['exact_no_prefixes_denied'])

                sub_dict['address_family'][address_family]['exact_no_prefixes_denied'] = exact_no_prefixes_denied
                continue
            
            # Cumulative no. of prefixes denied: 5.

            m = p41.match(line)
            if m:
                cummulative_no_prefixes_denied = int(m.groupdict()['cummulative_no_prefixes_denied'])

                sub_dict['address_family'][address_family]['cummulative_no_prefixes_denied'] = cummulative_no_prefixes_denied
                continue            

            # No policy: 5, Failed RT match: 0

            m = p42.match(line)
            if m:
                cummulative_no_no_policy = int(m.groupdict()['cummulative_no_no_policy'])
                cummulative_no_failed_rt_match = int(m.groupdict()['cummulative_no_failed_rt_match'])

                sub_dict['address_family'][address_family]['cummulative_no_no_policy'] = cummulative_no_no_policy
                sub_dict['address_family'][address_family]['cummulative_no_failed_rt_match'] = cummulative_no_failed_rt_match
                continue

            # By ORF policy: 0, By policy: 0

            m = p43.match(line)
            if m:
                cummulative_no_by_orf_policy = int(m.groupdict()['cummulative_no_by_orf_policy'])
                cummulative_no_by_policy = int(m.groupdict()['cummulative_no_by_policy'])

                sub_dict['address_family'][address_family]['cummulative_no_by_orf_policy'] = cummulative_no_by_orf_policy
                sub_dict['address_family'][address_family]['cummulative_no_by_policy'] = cummulative_no_by_policy
                continue

            # Prefix advertised 10, suppressed 0, withdrawn 0

            m = p44.match(line)
            if m:
                prefix_advertised = int(m.groupdict()['prefix_advertised'])
                prefix_suppressed = int(m.groupdict()['prefix_suppressed'])
                prefix_withdrawn = int(m.groupdict()['prefix_withdrawn'])

                sub_dict['address_family'][address_family]['prefix_advertised'] = prefix_advertised
                sub_dict['address_family'][address_family]['prefix_suppressed'] = prefix_suppressed
                sub_dict['address_family'][address_family]['prefix_withdrawn'] = prefix_withdrawn
                continue

            # Maximum prefixes allowed 1048576

            m = p45.match(line)
            if m:
                sub_dict['address_family'][address_family]\
                    ['maximum_prefix_max_prefix_no'] = \
                        int(m.groupdict()['maximum_prefix_max_prefix_no'])
                continue

            # Threshold for warning message 75%, restart interval 0 min

            m = p46.match(line)
            if m:
                threshold_warning_message = m.groupdict()['threshold_warning_message']
                threshold_restart_interval = int(m.groupdict()['threshold_restart_interval'])
                if m.groupdict()['warn']:
                    sub_dict['address_family'][address_family]['maximum_prefix_warning_only'] = True
                sub_dict['address_family'][address_family]['maximum_prefix_threshold'] = threshold_warning_message
                sub_dict['address_family'][address_family]['maximum_prefix_restart'] = threshold_restart_interval
                continue

            # An EoR was not received during read-only mode

            m = p47.match(line)
            if m:
                eor_status = str(m.groupdict()['eor_status'])

                sub_dict['address_family'][address_family]['eor_status'] = eor_status
                continue         

            # Last ack version 43, Last synced ack version 0

            m = p48.match(line)
            if m:
                last_synced_ack_version = int(m.groupdict()['last_synced_ack_version'])
                last_ack_version = int(m.groupdict()['last_ack_version'])

                sub_dict['address_family'][address_family]['last_synced_ack_version'] = last_synced_ack_version
                sub_dict['address_family'][address_family]['last_ack_version'] = last_ack_version
                continue
            
            # Outstanding version objects: current 0, max 1

            m = p49.match(line)
            if m:
                outstanding_version_objects_current = int(m.groupdict()['outstanding_version_objects_current'])
                outstanding_version_objects_max = int(m.groupdict()['outstanding_version_objects_max'])

                sub_dict['address_family'][address_family]['outstanding_version_objects_current'] = outstanding_version_objects_current
                sub_dict['address_family'][address_family]['outstanding_version_objects_max'] = outstanding_version_objects_max
                continue

            # Additional-paths operation: None

            m = p50.match(line)
            if m:
                additional_paths_operation = str(m.groupdict()['additional_paths_operation'])

                sub_dict['address_family'][address_family]['additional_paths_operation'] = additional_paths_operation
                continue

            # Advertise routes with local-label via Unicast SAFI

            m = p50_1.match(line)
            if m:
                additional_routes_local_label = str(m.groupdict()['additional_routes_local_label'])

                sub_dict['address_family'][address_family]['additional_routes_local_label'] = additional_routes_local_label
                continue

            # Send Multicast Attributes
            m = p50_2.match(line)
            if m:
                sub_dict['address_family'][address_family]['send_multicast_attributes'] = True
                continue

            # Connections established 1; dropped 0

            m = p51.match(line)
            if m:
                if 'bgp_session_transport' not in sub_dict:
                    sub_dict['bgp_session_transport'] = {}
                if 'connection' not in sub_dict['bgp_session_transport']:
                    sub_dict['bgp_session_transport']['connection'] = {}

                connections_established = int(m.groupdict()['num'])
                connections_dropped = int(m.groupdict()['connections_dropped'])

                bgp_state = m.groupdict()['bgp_state']
                sub_dict['bgp_session_transport']['connection']['state'] = bgp_state

                sub_dict['bgp_session_transport']['connection']['connections_established'] = connections_established
                sub_dict['bgp_session_transport']['connection']['connections_dropped'] = connections_dropped
                continue

            # Local host: 10.1.5.1, Local port: 179, IF Handle: 0x00000060

            m = p52.match(line)
            if m:
                if 'bgp_session_transport' not in sub_dict:
                    sub_dict['bgp_session_transport'] = {}
                if 'transport' not in sub_dict['bgp_session_transport']:
                    sub_dict['bgp_session_transport']['transport'] = {}

                local_host = m.groupdict()['local_host']
                local_port = str(m.groupdict()['local_port'])
                if_handle = m.groupdict()['if_handle']

                sub_dict['bgp_session_transport']['transport']['local_host'] = local_host
                sub_dict['bgp_session_transport']['transport']['local_port'] = local_port
                sub_dict['bgp_session_transport']['transport']['if_handle'] = if_handle
                continue

            # Foreign host: 10.1.5.5, Foreign port: 11052

            m = p53.match(line)
            if m:
                if 'bgp_session_transport' not in sub_dict:
                    sub_dict['bgp_session_transport'] = {}
                if 'transport' not in sub_dict['bgp_session_transport']:
                    sub_dict['bgp_session_transport']['transport'] = {}

                foreign_host = m.groupdict()['foreign_host']
                foreign_port = str(m.groupdict()['foreign_port'])

                sub_dict['bgp_session_transport']['transport']['foreign_host'] = foreign_host
                sub_dict['bgp_session_transport']['transport']['foreign_port'] = foreign_port
                continue

            # Last reset 00:00:00

            m = p54.match(line)
            if m:
                if 'bgp_session_transport' not in sub_dict:
                    sub_dict['bgp_session_transport'] = {}
                if 'connection' not in sub_dict['bgp_session_transport']:
                    sub_dict['bgp_session_transport']['connection'] = {}

                last_reset = m.groupdict()['last_reset']

                sub_dict['bgp_session_transport']['connection']['last_reset'] = last_reset
                # TODO when have output -- reset_reason
                continue


            # ######################################
            # add the lines for missing keys of ops
            # ######################################

            # Capability 4-byte-as suppress is configured

            m = p55.match(line)
            if m:
                sub_dict['suppress_four_byte_as_capability'] = True
                continue

            # Description: PEER

            m = p56.match(line)
            if m:
                sub_dict['description'] = m.groupdict()['description']
                
            # Private AS number removed from updates to this neighbor

            m = p57.match(line)
            if m:
                sub_dict['remove_private_as'] = True
                continue
                
            # Administratively shut down

            m = p58.match(line)
            if m:
                sub_dict['shutdown'] = True
                continue
                
            # External BGP neighbor may be up to 222 hops away

            m = p59.match(line)
            if m:
                sub_dict['ebgp_multihop'] = True
                sub_dict['ebgp_multihop_max_hop'] = int(m.groupdict()['hop'])
                continue

            # TCP open mode: passive only

            m = p60.match(line)
            if m:
                if 'bgp_session_transport' not in sub_dict:
                    sub_dict['bgp_session_transport'] = {}
                if 'connection' not in sub_dict['bgp_session_transport']:
                    sub_dict['bgp_session_transport']['connection'] = {}

                mode = m.groupdict()['mode']
                mode == 'passive-only' if mode == 'passive only' else mode

                sub_dict['bgp_session_transport']['connection']['mode'] = mode
                # TODO when have output -- reset_reason
                continue

            # My AS number is allowed 3 times in received updates

            m = p61.match(line)
            if m:
                sub_dict['address_family'][address_family]['allowas_in'] = True
                sub_dict['address_family'][address_family]['allowas_in_as_number'] = \
                    int(m.groupdict()['num'])
                continue

            # Route-Reflector Client

            m = p62.match(line)
            if m:
                sub_dict['address_family'][address_family]['route_reflector_client'] = True
                continue

            # Extended community attribute sent to this neighbor

            m = p63.match(line)
            if m:
                sub_dict['address_family'][address_family]['send_community'] = \
                    m.groupdict()['send_com'].lower()
                continue

            # Inbound soft reconfiguration allowed

            m = p64.match(line)
            if m:
                sub_dict['address_family'][address_family]['soft_configuration'] = True
                continue

            # AS override is set

            m = p65.match(line)
            if m:
                sub_dict['address_family'][address_family]['as_override'] = True
                continue

            # Default information originate: default sent

            m = p66.match(line)
            if m:
                sub_dict['address_family'][address_family]['default_originate'] = True
                sub_dict['address_family'][address_family]['default_originate_route_map'] = \
                    m.groupdict()['route_map'].strip()
                continue

            # site-of-origin 100:100

            m = p67.match(line)
            if m:
                sub_dict['address_family'][address_family]['soo'] = m.groupdict()['soo']
                continue

        return ret_dict

    def yang(self, vrf_type, af_type=''):

        if not vrf_type in ['all', 'vrf']:
            raise Exception("Variable 'vrf_type' can only be 'all' or 'vrf'")

        map_dict = {}

        # Execute YANG 'get' operational state RPC and parse the XML
        bgpOC = BgpOpenconfigYang(self.device)
        yang_dict = bgpOC.yang()

        # Map keys from yang_dict to map_dict

        # Add default instance
        if 'instance' not in map_dict:
            map_dict['instance'] = {}
        if 'default' not in map_dict['instance']:
            map_dict['instance']['default'] = {}

        # vrf
        for vrf in yang_dict['vrf']:
            if 'vrf' not in map_dict['instance']['default']:
                map_dict['instance']['default']['vrf'] = {}
            if vrf not in map_dict['instance']['default']['vrf']:
                map_dict['instance']['default']['vrf'][vrf] = {}
                sub_dict = map_dict['instance']['default']['vrf'][vrf]

            # neighbor
            for neighbor in yang_dict['vrf'][vrf]['neighbor']:
                if 'neighbor' not in sub_dict:
                    sub_dict['neighbor'] = {}
                if neighbor not in sub_dict['neighbor']:
                    sub_dict['neighbor'][neighbor] = {}
                # Set all keys
                sub_dict['neighbor'][neighbor] = \
                    yang_dict['vrf'][vrf]['neighbor'][neighbor]

        # Return to caller
        return map_dict


# =============================================================================
# Parser for:
# 'show bgp instance all all all neighbors <neighbor> received routes'
# 'show bgp instance all vrf all neighbors <neighbor> received routes'
# 'show bgp instance all vrf all ipv4 unicast neighbors <neighbor> received routes'
# 'show bgp instance all vrf all ipv6 unicast neighbors <neighbor> received routes'
# =============================================================================

class ShowBgpInstanceNeighborsReceivedRoutesSchema(MetaParser):
    
    """Schema for:
        show bgp instance all all all neighbors <neighbor> received routes
        show bgp instance all vrf all neighbors <neighbor> received routes
        show bgp instance all vrf all ipv4 unicast neighbors <neighbor> received routes
        show bgp instance all vrf all ipv6 unicast neighbors <neighbor> received routes
        show bgp instance <instance> vrf <vrf> <address_family> neighbors <neighbor> received routes
    """

    schema = {'instance':
                {Any():
                    {Optional('vrf'):
                        {Any():
                            {Optional('address_family'):
                                {Any():
                                    {Optional('router_identifier'): str,
                                     Optional('route_distinguisher'): str,
                                     Optional('local_as'): Or(int, str,),
                                     Optional('state'): str,
                                     Optional('vrf_id'): str,
                                     Optional('generic_scan_interval'): int,
                                     Optional('non_stop_routing'): bool,
                                     Optional('table_state'): str,
                                     Optional('table_id'): str,
                                     Optional('rd_version'): int,
                                     Optional('routing_table_version'): int,
                                     Optional('nsr_initial_initsync_version'): str,
                                     Optional('nsr_initial_init_ver_status'): str,
                                     Optional('nsr_issu_sync_group_versions'): str,
                                     Optional('processed_prefixes'): int,
                                     Optional('processed_paths'): int,
                                     Optional('scan_interval'): int,
                                     Optional('route_distinguisher'): str,
                                     Optional('default_vrf'): str,
                                     Optional('received'):
                                        {Any():
                                            {Optional('index'):
                                                {Any():
                                                    {Optional('status_codes'): str,
                                                    Optional('next_hop'): str,
                                                    Optional('metric'): str,
                                                    Optional('locprf'): str,
                                                    Optional('weight'): str,
                                                    Optional('path'): str,
                                                    Optional('origin_codes'): str
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            }

class ShowBgpInstanceNeighborsReceivedRoutes(ShowBgpInstanceNeighborsReceivedRoutesSchema):

    """Parser for:
        show bgp instance all all all neighbors <neighbor> received routes
        show bgp instance all vrf all neighbors <neighbor> received routes
        show bgp instance all vrf all ipv4 unicast neighbors <neighbor> received routes
        show bgp instance all vrf all ipv6 unicast neighbors <neighbor> received routes
        show bgp instance <instance> vrf <vrf> <address_family> neighbors <neighbor> received routes
        For checking any output with the parser ,below mandatory keys have to be in cli command.

        - vrf_type
    """
    cli_command = ['show bgp instance {instance} all all neighbors {neighbor} {route_type}',
                   'show bgp instance {instance} {vrf_type} {vrf} {address_family} neighbors {neighbor} {route_type}',
                   'show bgp instance {instance} {vrf_type} {vrf} neighbors {neighbor} {route_type}']

    def cli(self, vrf_type='all', neighbor='', vrf='all', instance='all', address_family='', route_type='received routes', output=None):

        assert vrf_type in ['all', 'vrf']
        assert route_type in ['received routes', 'routes']
        assert address_family in ['', 'ipv4 unicast', 'ipv6 unicast']

        if output is None:
            if vrf_type == 'all':
                out = self.device.execute(self.cli_command[0].format(instance=instance,
                                                                         neighbor=neighbor,
                                                                         route_type=route_type))
            else:
                if address_family:
                    out = self.device.execute(self.cli_command[1].format(instance=instance,
                                                                         neighbor=neighbor,
                                                                         address_family=address_family,
                                                                         vrf_type=vrf_type,
                                                                         vrf=vrf,
                                                                         route_type=route_type))
                else:
                    out = self.device.execute(self.cli_command[2].format(instance=instance,
                                                                         neighbor=neighbor,
                                                                         vrf_type=vrf_type,
                                                                         vrf=vrf,
                                                                         route_type=route_type))

        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = None
        address_family = None

        if vrf_type == 'all':
            vrf = 'default'
            af = ''
        elif vrf_type == 'vrf':
            vrf = None
            if address_family == 'ipv6 unicast':
                af = 'vpnv6 unicast'
            else:
                af = 'vpnv4 unicast'

        # handle route table name
        routes = 'received' if 'received' in route_type else 'routes'
        p1 = re.compile(r'^BGP *instance *(?P<instance_number>[0-9]+): *(?P<instance>[a-zA-Z0-9\-\_\']+)$')
        p15 = re.compile(r'^BGP *VRF *(?P<vrf>[a-zA-Z0-9]+), *'
                            'state: *(?P<state>[a-zA-Z]+)$')
        p15_1 = re.compile(r'^BGP Route Distinguisher: *(?P<route_distinguisher>\S+)')
        p16 = re.compile(r'^\s*VRF *ID: *(?P<vrf_id>[a-z0-9]+)$')
        p2 = re.compile(r'^Address *Family: *(?P<address_family>[a-zA-Z0-9\s]+)$')
        p3 = re.compile(r'^BGP *router *identifier *(?P<router_identifier>[0-9\.]+), *'
                        r'local *AS *number *(?P<local_as>[0-9\.]+)$')
        p4 = re.compile(r'^BGP *generic *scan *interval *(?P<generic_scan_interval>[0-9]+) +secs$')
        p5 = re.compile(r'^(?P<non_stop_routing>(Non-stop routing is enabled))$')
        p6 = re.compile(r'^BGP *table *state: *(?P<table_state>[a-zA-Z]+)$')
        p7 = re.compile(r'^Table *ID: *(?P<table_id>[a-z0-9]+) *RD *version: *(?P<rd_version>[0-9]+)$')
        p8 = re.compile(r'^BGP *main *routing *table *version *(?P<bgp_table_version>[0-9]+)$')
        p9 = re.compile(r'^BGP *NSR *Initial *initsync *version *(?P<nsr_initial_initsync_version>[0-9]+) *\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')
        p10 = re.compile(r'^BGP *NSR/ISSU *Sync-Group *versions *(?P<nsr_issu_sync_group_versions>[0-9\/\s]+)$')
        p11 = re.compile(r'^BGP *scan *interval *(?P<scan_interval>[0-9\S]+) *secs$')
        p12 = re.compile(r'^Route +Distinguisher: *(?P<route_distinguisher>\S+) *'
                            '(\(default +for +vrf +(?P<default_vrf>[a-zA-Z0-9]+)\))?$')
        p13 = re.compile(r'^(?P<status_codes>(i|s|x|S|d|h|\*|\>|\s)+)? *'
                            '(?P<prefix>(?P<ip>[\w\.\:\/\[\]]+)\/(?P<mask>\d+))?( +'
                            '(?P<next_hop>[\w\.\:]+) *(?P<number>[\d\.\s\{\}]+)?'
                            '(?: *(?P<origin_codes>(i|e|\?)))?)?$')      
        p13_1 = re.compile(r'(?P<path>[\d\.\s]+)'
                        ' *(?P<origin_codes>(i|e|\?))?$')

        p14 = re.compile(r'^Processed *(?P<processed_prefixes>[0-9]+) *'
                            'prefixes, *(?P<processed_paths>[0-9]+) *paths$')

        #    Network            Next Hop            Metric LocPrf Weight Path
        #                       10.4.1.1                    100      0    i
        p17 = re.compile(r'^(?P<next_hop>[\w\.\:]+) +((?P<metric>[0-9]+))? +'
                            '(?P<locprf>[0-9]+) +(?P<weight>[0-9]+) '
                            '*(?P<path>[\S]+)$')

        for line in out.splitlines():
            line = line.strip()

            if not line:
                continue

            # BGP instance 0: 'default'

            m = p1.match(line)
            if m:
                instance = m.groupdict()['instance']
                instance = instance.replace("'","")
                instance_number = str(m.groupdict()['instance_number'])

                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance not in ret_dict['instance']:
                    ret_dict['instance'][instance] = {}
                    continue

            #BGP VRF VRF2, state: Active

            m = p15.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                state = m.groupdict()['state'].lower()
                ret_dict.setdefault('instance', {}).setdefault(instance, {})
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                continue

            # BGP Route Distinguisher: 200:2

            m = p15_1.match(line)
            if m:
                route_distinguisher = m.groupdict()['route_distinguisher']
                continue

            # VRF ID: 0x60000002

            m = p16.match(line)
            if m:
                vrf_id = m.groupdict()['vrf_id']
                continue

            # Network            Next Hop            Metric LocPrf Weight Path
            #                    10.4.1.1                    300      1    i

            m = p17.match(line)
            if m:
                if m.groupdict()['metric']:
                    sub_dict[routes][prefix]['index'][index]['metric'] = \
                        m.groupdict()['metric']

                sub_dict[routes][prefix]['index'][index]['next_hop'] = \
                    m.groupdict()['next_hop']
                sub_dict[routes][prefix]['index'][index]['locprf'] = \
                    m.groupdict()['locprf']
                sub_dict[routes][prefix]['index'][index]['weight'] = \
                    m.groupdict()['weight']
                sub_dict[routes][prefix]['index'][index]['path'] = \
                    m.groupdict()['path'].strip()
                continue

            # Address Family: VPNv4 Unicast

            m = p2.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                continue


            # BGP router identifier 10.4.1.1, local AS number 100

            m = p3.match(line)
            if m:
                router_identifier = m.groupdict()['router_identifier']
                try:
                    local_as = int(m.groupdict()['local_as'])
                except Exception:
                    local_as = m.groupdict()['local_as']
                continue

            # BGP generic scan interval 60 secs

            m = p4.match(line)
            if m:
                generic_scan_interval = int(m.groupdict()['generic_scan_interval'])
                # sub_dict['generic_scan_interval'] = generic_scan_interval
                continue

            # Non-stop routing is enabled

            m = p5.match(line)
            if m:
                non_stop_routing = True
                continue

            # BGP table state: Active

            m = p6.match(line)
            if m:
                table_state = str(m.groupdict()['table_state']).lower()
                continue

            # Table ID: 0x0   RD version: 0

            m = p7.match(line)
            if m:
                table_id = m.groupdict()['table_id']
                rd_version = int(m.groupdict()['rd_version'])
                continue

            # BGP main routing table version 43

            m = p8.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                continue

            # BGP NSR Initial initsync version 11 (Reached)

            m = p9.match(line)
            if m:
                nsr_initial_initsync_version = m.groupdict()['nsr_initial_initsync_version']
                nsr_initial_init_ver_status = str(m.groupdict()['nsr_initial_init_ver_status']).lower()
                continue

            # BGP NSR/ISSU Sync-Group versions 0/0

            m = p10.match(line)
            if m:
                nsr_issu_sync_group_versions = m.groupdict()['nsr_issu_sync_group_versions']
                continue

            # BGP scan interval 60 secs

            m = p11.match(line)
            if m:
               scan_interval = int(m.groupdict()['scan_interval'])
               continue

            # Route Distinguisher: 200:1 (default for vrf VRF1)

            m = p12.match(line)
            if m:
                rd = m.groupdict()['route_distinguisher']
                addr = (address_family or af) + ' RD ' + rd
                if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                if address_family not in ret_dict['instance'][instance]['vrf'][vrf]['address_family']:
                    sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['address_family'][addr] = {}
                try:
                    sub_dict['state'] = state
                except Exception:
                    pass                    

                try:
                    sub_dict['vrf_id'] = vrf_id
                except Exception:
                    pass                    

                try:
                    sub_dict['router_identifier'] = router_identifier
                except Exception:
                    pass                    

                try:
                    sub_dict['route_distinguisher'] = route_distinguisher
                except Exception:
                    pass                    

                try:
                    sub_dict['local_as'] = local_as
                except Exception:
                    pass

                try:
                    sub_dict['generic_scan_interval'] = generic_scan_interval
                except Exception:
                    pass                    

                try:
                    sub_dict['non_stop_routing'] = non_stop_routing
                except Exception:
                    pass

                try:
                    sub_dict['table_state'] = table_state
                except Exception:
                    pass

                try:
                    sub_dict['table_id'] = table_id
                except Exception:
                    pass

                try:
                    sub_dict['rd_version'] = rd_version
                except Exception:
                    pass                    

                try:
                    sub_dict['routing_table_version'] = bgp_table_version
                except Exception:
                    pass

                try:
                    sub_dict['nsr_initial_initsync_version'] = nsr_initial_initsync_version
                except Exception:
                    pass

                try:
                    sub_dict['nsr_initial_init_ver_status'] = nsr_initial_init_ver_status
                except Exception:
                    pass

                try:
                    sub_dict['nsr_issu_sync_group_versions'] = nsr_issu_sync_group_versions
                except Exception:
                    pass

                try:
                    sub_dict['scan_interval'] = scan_interval
                except Exception:
                    pass

                continue
                    
            # *>i10.9.6.0/24        10.64.4.4               2219    100      0 400 33299 51178 47751 {27016} e
            # *> 2001:db8:cdc9:121::/64     2001:db8:20:1:5::5
            # *>i[T][L15][L1x1][N[c12365][b10.4.1.1][s10.16.2.2]][P[p10.4.1.1/32]]/800

            m = p13.match(line)
            if m:
                try:
                    sub_dict
                except Exception:
                    addr = address_family or af
                    if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                        ret_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                    if address_family not in ret_dict['instance'][instance]['vrf'][vrf]['address_family']:
                        sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['address_family'][addr] = {}
                    try:
                        sub_dict['state'] = state
                    except Exception:
                        pass                    

                    try:
                        sub_dict['vrf_id'] = vrf_id
                    except Exception:
                        pass                    

                    try:
                        sub_dict['router_identifier'] = router_identifier
                    except Exception:
                        pass                    

                    try:
                        sub_dict['route_distinguisher'] = route_distinguisher
                    except Exception:
                        pass                    

                    try:
                        sub_dict['local_as'] = local_as
                    except Exception:
                        pass

                    try:
                        sub_dict['generic_scan_interval'] = generic_scan_interval
                    except Exception:
                        pass                    

                    try:
                        sub_dict['non_stop_routing'] = non_stop_routing
                    except Exception:
                        pass

                    try:
                        sub_dict['table_state'] = table_state
                    except Exception:
                        pass

                    try:
                        sub_dict['table_id'] = table_id
                    except Exception:
                        pass

                    try:
                        sub_dict['rd_version'] = rd_version
                    except Exception:
                        pass                    

                    try:
                        sub_dict['routing_table_version'] = bgp_table_version
                    except Exception:
                        pass

                    try:
                        sub_dict['nsr_initial_initsync_version'] = nsr_initial_initsync_version
                    except Exception:
                        pass

                    try:
                        sub_dict['nsr_initial_init_ver_status'] = nsr_initial_init_ver_status
                    except Exception:
                        pass

                    try:
                        sub_dict['nsr_issu_sync_group_versions'] = nsr_issu_sync_group_versions
                    except Exception:
                        pass

                    try:
                        sub_dict['scan_interval'] = scan_interval
                    except Exception:
                        pass
                    
                status_codes = str(m.groupdict()['status_codes'])
                status_codes = status_codes.replace(" ", "")
                next_hop = m.groupdict()['next_hop']
                prefix = m.groupdict()['prefix']
                if routes not in sub_dict:
                    sub_dict[routes] = {}

                if prefix:
                    index = 1
                    pre_net = prefix            
                else:
                    prefix = pre_net
                    index += 1
                
                if prefix not in sub_dict[routes]:
                    sub_dict[routes][prefix] = {}

                if 'index' not in sub_dict[routes][prefix]:
                    sub_dict[routes][prefix]['index'] = {}

                if index not in sub_dict[routes][prefix]['index']:
                    sub_dict[routes][prefix]['index'][index] = {}

                sub_dict[routes][prefix]['index'][index]['next_hop'] = next_hop
                sub_dict[routes][prefix]['index'][index]['status_codes'] = status_codes

                # dealing with the group of metric, locprf, weight, path
                group_num = m.groupdict()['number']

                if group_num:
                    # metric   locprf  weight path
                    # 2219      211       0 200 33299 51178 47751 {27016}
                    m1 = re.compile(r'^(?P<metric>[0-9]+)  +'
                                 '(?P<locprf>[0-9]+)  +'
                                 '(?P<weight>[0-9]+) '
                                 '(?P<path>[0-9\.\{\}\s]+)$').match(group_num)
    
                    # metric   locprf  weight path
                    # 2219                0 200 33299 51178 47751 {27016}
                    # locprf   weight path
                    # 211         0 200 33299 51178 47751 {27016} 65000.65000
    
                    m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,20})'
                                 '(?P<weight>[0-9]+) '
                                 '(?P<path>[0-9\.\{\}\s]+)$').match(group_num)
    
                    # weight path
                    # 0 200 33299 51178 47751 {27016} 65000.65000
                    m3 = re.compile(r'^(?P<weight>[0-9]+) '
                                 '(?P<path>(([\d\.]+\s)|(\{[\d\.]+\}\s))+)$')\
                               .match(group_num)

                    if m1:
                        sub_dict[routes][prefix]['index'][index]['metric'] = \
                            m1.groupdict()['metric']
                        sub_dict[routes][prefix]['index'][index]['locprf'] = \
                            m1.groupdict()['locprf']
                        sub_dict[routes][prefix]['index'][index]['weight'] = \
                            m1.groupdict()['weight']
                        sub_dict[routes][prefix]['index'][index]['path'] = \
                            m1.groupdict()['path'].strip()
                    elif m2:
                        if len(m2.groupdict()['space']) > 8:
                            sub_dict[routes][prefix]['index'][index]['metric'] = \
                                m2.groupdict()['value']
                        else:
                            sub_dict[routes][prefix]['index'][index]['locprf'] = \
                                m2.groupdict()['value']
    
                        sub_dict[routes][prefix]['index'][index]['weight'] = \
                            m2.groupdict()['weight']
                        sub_dict[routes][prefix]['index'][index]['path'] = \
                            m2.groupdict()['path'].strip()
                    elif m3:
                        sub_dict[routes][prefix]['index'][index]['weight'] = \
                            m3.groupdict()['weight']
                        sub_dict[routes][prefix]['index'][index]['path'] = \
                            m3.groupdict()['path'].strip()

                if m.groupdict()['origin_codes']:
                    sub_dict[routes][prefix]['index'][index]['origin_codes'] = \
                        m.groupdict()['origin_codes']
                continue

            # 4518 29612 22247 10519 16562 61158 60788 61783 20566 5674

            m = p13_1.match(line)
            if m:
                if 'path' in sub_dict[routes][prefix]['index'][index]:
                    sub_dict[routes][prefix]['index'][index]['path'] += \
                        ' ' + m.groupdict()['path'].strip()

                if m.groupdict()['origin_codes']:
                    sub_dict[routes][prefix]['index'][index]['origin_codes'] = \
                        m.groupdict()['origin_codes']

            # Processed 5 prefixes, 5 paths

            m = p14.match(line)
            if m:
                processed_prefixes = int(m.groupdict()['processed_prefixes'])
                processed_paths = int(m.groupdict()['processed_paths'])
                sub_dict['processed_prefixes'] = processed_prefixes
                sub_dict['processed_paths'] = processed_paths                    
                continue
    
        return ret_dict 


# ===============================================================================
# Parser for:
# 'show bgp instance all all all neighbors <WORD> advertised-routes'
# 'show bgp instance all vrf all neighbors <WORD> advertised-routes'
# 'show bgp instance all vrf all ipv4 unicast neighbors <WORD> advertised-routes'
# 'show bgp instance all vrf all ipv6 unicast neighbors <WORD> advertised-routes'
# ===============================================================================

class ShowBgpInstanceNeighborsAdvertisedRoutesSchema(MetaParser):

    """ Schema for:
        show bgp instance all all all neighbors <neighbor> advertised-routes
        show bgp instance all vrf all neighbors <neighbor> advertised-routes
        show bgp instance all vrf all ipv4 unicast neighbors <neighbor> advertised-routes
        show bgp instance all vrf all ipv6 unicast neighbors <neighbor> advertised-routes
        show bgp instance <instance> vrf <vrf> <address_family> neighbors <neighbor> advertised-routes

    """

    schema = {'instance':
                {Any():
                    {Optional('vrf'):
                        {Any():
                            {Optional('address_family'):
                                {Any():
                                    {Optional('route_distinguisher'): str,
                                     Optional('default_vrf'): str,
                                     Optional('processed_prefixes'): str,
                                     Optional('processed_paths'): str,
                                     Optional('advertised'):
                                        {Any():
                                            {Optional('index'):
                                                {Any():
                                                    {Optional('froms'): str,
                                                    Optional('path'): str,
                                                    Optional('origin_code'): str,
                                                    Optional('status_codes'): str,
                                                    Optional('next_hop'): str,
                                                    Optional('metric'): str,
                                                    Optional('locprf'): str,
                                                    Optional('weight'): str,
                                                    Optional('path'): str
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    }
                },
            }

class ShowBgpInstanceNeighborsAdvertisedRoutes(ShowBgpInstanceNeighborsAdvertisedRoutesSchema):

    """ Parser for:
        show bgp instance all all all neighbors <neighbor> advertised-routes
        show bgp instance all vrf all neighbors <neighbor> advertised-routes
        show bgp instance all vrf all ipv4 unicast neighbors <neighbor> advertised-routes
        show bgp instance all vrf all ipv6 unicast neighbors <neighbor> advertised-routes
        show bgp instance <instance> vrf <vrf> <address_family> neighbors <neighbor> advertised-routes
        For checking any output with the parser ,below mandatory keys have to be in cli command.

        - vrf_type
    """
    cli_command = ['show bgp instance {instance} all all neighbors {neighbor} advertised-routes',
                   'show bgp instance {instance} {vrf_type} {vrf} {address_family} neighbors {neighbor} advertised-routes',
                   'show bgp instance {instance} {vrf_type} {vrf} neighbors {neighbor} advertised-routes']

    def cli(self, vrf_type='all', neighbor='', vrf='all', instance='all', address_family='', output=None):
        assert vrf_type in ['all', 'vrf']
        assert address_family in ['', 'ipv4 unicast', 'ipv6 unicast']
        if output is None:
            if vrf_type == 'all':
                out = self.device.execute(self.cli_command[0].format(instance=instance,
                                                                  neighbor=neighbor))
            else:
                if address_family:
                    out = self.device.execute(self.cli_command[1].format(instance=instance,
                                                                  neighbor=neighbor,
                                                                  address_family=address_family,
                                                                  vrf_type=vrf_type, vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[2].format(instance=instance,
                                                                  neighbor=neighbor,
                                                                  vrf_type=vrf_type, vrf=vrf))
        else:
            out = output

        ret_dict = {}

        if vrf_type == 'all':
            vrf = 'default'
            af = ''
        elif vrf_type == 'vrf':
            if vrf != 'all':
                input_vrf = vrf
            vrf = None
            if address_family == 'ipv6 unicast':
                af = 'vpnv6 unicast'
            else:
                af = 'vpnv4 unicast'
        address_family = None
        p1 = re.compile(
            r'^BGP *instance *(?P<instance_number>[0-9]+): *(?P<instance>['
            r'a-zA-Z0-9\-\_\']+)$')
        p2 = re.compile(r'^VRF: *(?P<vrf>[a-zA-Z0-9\_]+)$')
        p7 = re.compile(r'^Address *Family: *(?P<address_family>[a-zA-Z0-9\s]+)$')
        p3 = re.compile(r'^Route *Distinguisher: *(?P<route_distinguisher>\S+) *'
                        '(\(default *for *vrf (?P<default_vrf>[0-9A-Z]+)\))?$')
        p4 = re.compile(
            r'^(?P<prefix>(?P<ip>[\w\.\:]+)/(?P<mask>\d+)) *(?P<next_hop>[\w\.\:]+) *('
            r'?P<froms>[\w\.\:]+) *'
            r'(?P<path>[\d\.\{\}\s]+)?(?P<origin_code>[e|i\?])?$')
        p5_1 = re.compile(r'(?P<path>[\d\.\{\}\s]+)(?P<origin_code>e|i)?$')
        p6 = re.compile(
            r'^Processed *(?P<processed_prefixes>[0-9]+) *prefixes, *(?P<processed_paths>[0-9]+) *paths$')

        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'

            m = p1.match(line)
            if m:
                instance = m.groupdict()['instance']
                instance = instance.replace("'","")

                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance not in ret_dict['instance']:
                    ret_dict['instance'][instance] = {}
                    continue

            # VRF: VRF2

            m = p2.match(line)
            if m:
                ret_dict.setdefault('instance', {}).setdefault(instance, {})
                vrf = m.groupdict()['vrf']
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                    continue

            # Address Family: VPNv4 Unicast

            m = p7.match(line)
            if m and vrf == 'default':
                address_family = m.groupdict()['address_family'].lower()
                if vrf_type == 'all' and vrf == 'default':
                    if 'vrf' not in ret_dict['instance'][instance]:
                        ret_dict['instance'][instance]['vrf'] = {}
                    if vrf not in ret_dict['instance'][instance]['vrf']:
                        ret_dict['instance'][instance]['vrf'][vrf] = {}
                        continue

            # Route Distinguisher: 200:2 (default for vrf VRF2)

            m = p3.match(line)
            if m:
                rd = m.groupdict()['route_distinguisher']
                addr = (address_family or af) + ' RD ' + rd
                default_vrf = m.groupdict()['default_vrf']
                if not vrf:
                    ret_dict.setdefault('instance', {}).setdefault(instance, {}).setdefault('vrf', {}).setdefault(input_vrf, {})
                    vrf=input_vrf
                if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                if address_family not in ret_dict['instance'][instance]['vrf'][vrf]['address_family']:
                    sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['address_family'][addr] = {}
                sub_dict['route_distinguisher'] = rd
                sub_dict['default_vrf'] = default_vrf if default_vrf else 'default'
                continue

            # Network            Next Hop        From            AS Path
            # 10.169.1.0/24        10.186.5.1        10.16.2.2         100 300 33299 51178 47751 {27016}e
            # 2001:db8:cdc9:121::/64     10.4.1.1         2001:db8:20:1:5::5
            # 10.4.1.1/32         10.4.1.1         Local           ?
            # 10.8.8.8/32        10.10.10.108    Local           65108.65108?

            m = p4.match(line)
            if m:
                try:
                    sub_dict
                except Exception:
                    addr = address_family or af
                    if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                        ret_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                    if address_family not in ret_dict['instance'][instance]['vrf'][vrf]['address_family']:
                        sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['address_family'][addr] = {}
                if m:
                    prefix = m.groupdict()['prefix']
                    next_hop = m.groupdict()['next_hop']
                    froms = m.groupdict()['froms']
                    path = m.groupdict()['path']
                    origin_code = m.groupdict()['origin_code']
                if prefix:
                    index = 1
                    pre_net = prefix
                else:
                    prefix = pre_net
                    index += 1
                if 'advertised' not in sub_dict:
                    sub_dict['advertised'] = {}

                if prefix not in sub_dict['advertised']:
                    sub_dict['advertised'][prefix] = {}
                if 'index' not in sub_dict['advertised'][prefix]:
                    sub_dict['advertised'][prefix]['index'] = {}
                if index not in sub_dict['advertised'][prefix]['index']:
                    sub_dict['advertised'][prefix]['index'][index] = {}

                if froms:
                    sub_dict['advertised'][prefix]['index'][index]['froms'] = froms
                if path:
                    sub_dict['advertised'][prefix]['index'][index]['path'] = path
                if origin_code:
                    sub_dict['advertised'][prefix]['index'][index]['origin_code'] = origin_code
                if next_hop:
                    sub_dict['advertised'][prefix]['index'][index]['next_hop'] = next_hop
                    continue

            #                                                    200 33299 51178 47751 {27017}e
            #                                                    200 33299 51178 65000.47751 {27017}e

            m = p5_1.match(line)
            if m:
                path = m.groupdict()['path']
                origin_code = m.groupdict()['origin_code']
                if path:
                    sub_dict['advertised'][prefix]['index'][index]['path'] = path
                if origin_code:
                    sub_dict['advertised'][prefix]['index'][index]['origin_code'] = origin_code
                    continue

            # Processed 5 prefixes, l5 paths

            m = p6.match(line)
            if m:
                processed_prefixes = str(m.groupdict()['processed_prefixes'])
                processed_paths = str(m.groupdict()['processed_paths'])

                sub_dict['processed_prefixes'] = processed_prefixes
                sub_dict['processed_paths'] = processed_paths
                continue

        return ret_dict


# ====================================================================
# Parser for:
# 'show bgp instance all all all neighbors <WORD> routes'
# 'show bgp instance all vrf all neighbors <WORD> routes'
# 'show bgp instance all vrf all ipv4 unicast neighbors <WORD> routes'
# 'show bgp instance all vrf all ipv6 unicast neighbors <WORD> routes'
# ====================================================================

class ShowBgpInstanceNeighborsRoutesSchema(MetaParser):

    """Schema for:
        show bgp instance all all all neighbors <neighbor> routes
        show bgp instance all vrf all neighbors <neighbor> routes
        show bgp instance all vrf all ipv4 unicast neighbors <neighbor> routes
        show bgp instance all vrf all ipv6 unicast neighbors <neighbor> routes
    """

    schema = {
        'instance':
            {Any():
                {Optional('vrf'):
                    {Any():
                        {Optional('address_family'):
                            {Any():
                                {Optional('router_identifier'): str,
                                 Optional('local_as'): Or(int, str,),
                                 Optional('state'): str,
                                 Optional('vrf_id'): str,
                                 Optional('generic_scan_interval'): int,
                                 Optional('non_stop_routing'): bool,
                                 Optional('table_state'): str,
                                 Optional('table_id'): str,
                                 Optional('rd_version'): int,
                                 Optional('routing_table_version'): int,
                                 Optional('nsr_initial_initsync_version'): str,
                                 Optional('nsr_initial_init_ver_status'): str,
                                 Optional('nsr_issu_sync_group_versions'): str,
                                 Optional('processed_prefixes'): int,
                                 Optional('processed_paths'): int,
                                 Optional('scan_interval'): int,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('routes'):
                                    {Any():
                                        {Optional('index'):
                                            {Any():
                                                {Optional('status_codes'): str,
                                                Optional('next_hop'): str,
                                                Optional('metric'): str,
                                                Optional('locprf'): str,
                                                Optional('weight'): str,
                                                Optional('path'): str,
                                                Optional('origin_codes'): str
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpInstanceNeighborsRoutes(ShowBgpInstanceNeighborsRoutesSchema, ShowBgpInstanceNeighborsReceivedRoutes):
    
    """ Parser for:
        show bgp instance all all all neighbors <WORD> routes
        show bgp instance all vrf all neighbors <WORD> routes
        show bgp instance <instance> vrf <vrf> neighbors <WORD> routes
        show bgp instance <instance> all all neighbors <WORD> routes
        show bgp instance all vrf all ipv4 unicast neighbors <WORD> routes
        show bgp instance all vrf all ipv6 unicast neighbors <WORD> routes
        For checking any output with the parser ,below mandatory keys have to be in cli command.

        - vrf_type
    """

    def cli(self, vrf_type='all', neighbor='', vrf='all', instance='all', address_family='', route_type='routes', output=None):
        if 'received' in route_type:
            self.schema = ShowBgpInstanceNeighborsReceivedRoutes.schema.copy()
        return super().cli(neighbor=neighbor, vrf_type=vrf_type, address_family=address_family,
            route_type=route_type, vrf=vrf, instance=instance, output=output)


# ====================================================
# Parser for:
# 'show bgp instance all all all summary'
# 'show bgp instance all vrf all summary'
# 'show bgp instance all vrf all ipv4 unicast summary'
# 'show bgp instance all vrf all ipv6 unicast summary'
# ====================================================

class ShowBgpInstanceSummarySchema(MetaParser):

    """ Schema for:
        show bgp instance all all all summary
        show bgp instance all vrf all summary
        show bgp instance all vrf all ipv4 unicast summary
        show bgp instance all vrf all ipv6 unicast summary
    """

    schema = {
        'instance':
            {Any():
                {Optional('vrf'):
                    {Any():
                        {Optional('address_family'):
                            {Any():
                                {Optional('route_distinguisher'): str,
                                Optional('bgp_table_version'): int,
                                Optional('local_as'): Or(int, str),
                                Optional('bgp_vrf'): str,
                                Optional('router_id'): str,
                                Optional('non_stop_routing'): str,
                                Optional('table_state'): str,
                                Optional('table_id'): str,
                                Optional('rd_version'): int,
                                Optional('generic_scan_interval'): int,
                                Optional('nsr_initial_initsync_version'): int,
                                Optional('nsr_initial_init_ver_status'): str,
                                Optional('nsr_issu_sync_group_versions'): str,
                                Optional('scan_interval'): int,
                                Optional('operation_mode'): str,
                                Optional('vrf_id'): str,
                                Optional('instance_number'): str,
                                Optional('vrf_state'): str,
                                Optional('process'):
                                    {Any():
                                        {'rcvtblver': int,
                                        'brib_rib': int,
                                        'labelver': int,
                                        'importver': int,
                                        'sendtblver': int,
                                        'standbyver': int}}}},
                        Optional('neighbor'):
                            {Any():        
                                {'remote_as': Or(int, str),
                                'address_family':
                                    {Any():
                                        {'tbl_ver': int,
                                        'spk': int,   
                                        'msg_rcvd': int,
                                        'msg_sent': int,
                                        'input_queue': int,
                                        'output_queue': int,
                                        'up_down': str,
                                        'state_pfxrcd': str,
                                        Optional('route_distinguisher'): str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowBgpInstanceSummary(ShowBgpInstanceSummarySchema):

    """ Parser for:
        show bgp instance all all all summary
        show bgp instance all vrf all summary
        show bgp instance all vrf all ipv4 unicast summary
        show bgp instance all vrf all ipv6 unicast summary
        show bgp instance <instance> all all summary
        show bgp instance <instance> vrf <vrf> <address_family> summary
        For checking any output with the parser ,below mandatory keys have to be in cli command.

        - vrf_type
    """

    cli_command = ['show bgp instance {instance} all all summary',
                   'show bgp instance {instance} {vrf_type} {vrf} {address_family} summary',
                   'show bgp instance {instance} {vrf_type} {vrf} summary']

    exclude = ['bgp_table_version', 'brib_rib', 'importver', 'labelver', 'rcvtblver',
        'sendtblver', 'rd_version', 'msg_rcvd', 'msg_sent', 'tbl_ver', 'up_down',
        'nsr_initial_initsync_version', 'nsr_initial_init_ver_status',
        'nsr_issu_sync_group_versions', 'standbyver']

    def cli(self, instance='all', vrf_type='all', vrf='all', address_family='', output=None):

        assert vrf_type in ['all', 'vrf']
        # assert address_family in ['', 'ipv4 unicast', 'ipv6 unicast']
        if output is None:
            if vrf_type == 'all':
                out = self.device.execute(self.cli_command[0].format(instance=instance,
                                                                     vrf_type=vrf_type))
            else:
                if address_family:
                    out = self.device.execute(self.cli_command[1].format(instance=instance,
                                                                     address_family=address_family,
                                                                     vrf_type=vrf_type,
                                                                     vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[2].format(instance=instance,
                                                                     vrf_type=vrf_type,
                                                                     vrf=vrf))
        else:
            out = output
        p1 = re.compile(r'^\s*BGP *instance *(?P<instance_number>[0-9]+):'
                        ' *(?P<instance>[a-zA-Z0-9\-\_\']+)$')
        p2 = re.compile(r'^\s*VRF: *(?P<vrf>[\S]+)$')
        p3 = re.compile(r'^\s*Address *Family:'
                        ' *(?P<address_family>[\S\s]+)$')
        p4 = re.compile(r'^\s*BGP *VRF *(?P<bgp_vrf>[a-zA-Z0-9]+), *state:'
                        ' *(?P<vrf_state>[a-zA-Z]+)$')
        p5 = re.compile(r'^\s*BGP *Route *Distinguisher:'
                        ' *(?P<route_distinguisher>\S+)$')
        p6 = re.compile(r'^\s*VRF *ID: *(?P<vrf_id>[a-z0-9]+)$')
        p7 = re.compile(r'^\s*BGP *router *identifier'
                        ' *(?P<router_id>[0-9\.]+)\, *local *AS *number'
                        ' *(?P<local_as>[0-9\.]+)$')
        p8 = re.compile(r'^\s*BGP *generic *scan *interval'
                        ' *(?P<generic_scan_interval>[0-9]+) *secs$')
        p9 = re.compile(r'^\s*Non-stop *routing *is'
                        ' *(?P<non_stop_routing>[A-Za-z]+)$')
        p10 = re.compile(r'^\s*BGP *table *state:'
                         ' *(?P<table_state>[a-zA-Z]+)$')
        p11 = re.compile(r'^\s*Table *ID: *(?P<table_id>[a-z0-9]+)'
                         ' *RD *version: (?P<rd_version>[0-9]+)$')
        p12 = re.compile(r'^\s*BGP *main *routing *table *version'
                         ' *(?P<bgp_table_version>[0-9]+)$')
        p13 = re.compile(r'^\s*BGP *NSR *Initial *initsync *version'
                         ' *(?P<nsr_initial_initsync_version>[0-9]+)'
                         ' *\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')
        p14 = re.compile(r'^\s*BGP *NSR/ISSU *Sync-Group *versions'
                         ' *(?P<nsr_issu_sync_group_versions>[0-9\/]+)$')
        p15 = re.compile(
            r'^\s*BGP *generic *scan *interval *(?P<scan_interval>[0-9]+) *secs$')
        p16 = re.compile(
            r'^\s*BGP *is *operating *in *(?P<operation_mode>[a-zA-Z]+) *mode.$')
        p17 = re.compile(r'^\s*(?P<process>[a-zA-Z]+) *(?P<rcvtblver>[0-9]+)'
                         ' *(?P<brib_rib>[0-9]+) *(?P<labelver>[0-9]+)'
                         ' *(?P<importver>[0-9]+) *(?P<sendtblver>[0-9]+)'
                         ' *(?P<standbyver>[0-9]+)$')
        p17_1 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
        p17_2 = re.compile(r'^\s*(?P<spk>[0-9]+)\s+(?P<remote_as>[0-9\.]+)'
                           '\s+(?P<msg_rcvd>[0-9]+)\s+(?P<msg_sent>[0-9]+)'
                           '\s+(?P<tbl_ver>[0-9]+)\s+(?P<input_queue>[0-9]+)'
                           '\s+(?P<output_queue>[0-9]+)\s+(?P<up_down>[a-z0-9\:]+)'
                           '\s+(?P<state_pfxrcd>.+)$')
        p17_3 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<spk>[0-9]+)'
                           ' +(?P<remote_as>[0-9\.]+) +(?P<msg_rcvd>[0-9]+)'
                           ' +(?P<msg_sent>[0-9]+)'
                           ' +(?P<tbl_ver>[0-9]+) +(?P<input_queue>[0-9]+)'
                           ' +(?P<output_queue>[0-9]+) +(?P<up_down>[a-z0-9\:]+)'
                           ' +(?P<state_pfxrcd>.+)$')

        # Init vars
        bgp_instance_summary_dict = {}
        data_on_nextline = False

        if vrf_type == 'all':
            vrf = 'default'
            af_default = None
        elif vrf_type == 'vrf':
            if vrf != 'all':
                input_vrf = vrf
            vrf = None
            if address_family == 'ipv6 unicast':
                af_default = 'vpnv6 unicast'
            else:
                af_default = 'vpnv4 unicast'

        # init the route_distinguisher when all all all command
        route_distinguisher = None

        for line in out.splitlines():
            line = line.rstrip()

            # BGP instance 0: 'default' 

            m = p1.match(line)
            if m:
                instance = m.groupdict()['instance']
                instance = instance.replace("'","")
                instance_number = str(m.groupdict()['instance_number'])
                if 'instance' not in bgp_instance_summary_dict:
                    bgp_instance_summary_dict['instance'] = {}
                if instance not in bgp_instance_summary_dict['instance']:
                    bgp_instance_summary_dict['instance'][instance] = {}
                # VRF is default - init dictionary here
                if vrf_type == 'all' and vrf == 'default':
                    if 'vrf' not in bgp_instance_summary_dict['instance'][instance]:
                        bgp_instance_summary_dict['instance'][instance]['vrf'] = {}
                    if vrf not in bgp_instance_summary_dict['instance'][instance]['vrf']:
                        bgp_instance_summary_dict['instance'][instance]['vrf'][vrf] = {}
                        continue

            # VRF: VRF1

            m = p2.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if 'vrf' not in bgp_instance_summary_dict['instance'][instance]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'] = {}
                if vrf not in bgp_instance_summary_dict['instance'][instance]['vrf']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf] = {}
                # Address family is default - init af dictionary here
                if vrf_type == 'vrf' and af_default:
                    address_family = af_default
                    original_address_family = address_family
                    if 'address_family' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]:
                        bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                    if address_family not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family']:
                        bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family] = {}
                        continue
            
            # Address Family: VPNv4 Unicast

            m = p3.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                if 'address_family' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                if address_family not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family] = {}
                continue

            # BGP VRF VRF1, state: Active
            # BGP VRF vrf1, state: Active

            m = p4.match(line)
            if m:
                if not vrf:
                    vrf_dict = bgp_instance_summary_dict.setdefault('instance', {}).setdefault(instance, {}).setdefault('vrf', {}).setdefault(input_vrf,{})
                    if vrf_type == 'vrf' and af_default:
                        address_family = af_default
                        vrf_dict.setdefault('address_family', {}).setdefault(address_family, {})
                    vrf = input_vrf
                else:
                    vrf_dict = bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]
                bgp_vrf = m.groupdict()['bgp_vrf'].lower()
                vrf_state = m.groupdict()['vrf_state'].lower()
                vrf_dict['address_family'][address_family]['bgp_vrf'] = bgp_vrf
                vrf_dict['address_family'][address_family]['vrf_state'] = vrf_state
                continue

            # BGP Route Distinguisher: 200:1

            m = p5.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['route_distinguisher'] = route_distinguisher
                continue
            
            # VRF ID: 0x60000001

            m = p6.match(line)
            if m:
                vrf_id = str(m.groupdict()['vrf_id'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['vrf_id'] = vrf_id
                continue 

            # BGP router identifier 10.229.11.11, local AS number 100

            m = p7.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                try:
                    local_as = int(m.groupdict()['local_as'])
                except:
                    local_as = m.groupdict()['local_as']
                sub = bgp_instance_summary_dict.setdefault('instance', {}).setdefault(instance, {})\
                        .setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {})\
                        .setdefault(address_family, {})
                sub['router_id'] = router_id
                sub['local_as'] = local_as
                continue

            # BGP generic scan interval 60 secs

            m = p8.match(line)
            if m:
                generic_scan_interval = int(m.groupdict()['generic_scan_interval'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['generic_scan_interval'] = generic_scan_interval
                continue

            # Non-stop routing is enabled

            m = p9.match(line)
            if m:
                non_stop_routing = str(m.groupdict()['non_stop_routing'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['non_stop_routing'] = non_stop_routing
                continue

            # BGP table state: Active

            m = p10.match(line)
            if m:
                table_state = str(m.groupdict()['table_state']).lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['table_state'] = table_state
                continue

            # Table ID: 0x0   RD version: 0

            m = p11.match(line)
            if m:
                table_id = str(m.groupdict()['table_id'])
                rd_version = int(m.groupdict()['rd_version'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['table_id'] = table_id
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['rd_version'] = rd_version
                continue

            # BGP main routing table version 63

            m = p12.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['bgp_table_version'] =  bgp_table_version       
                continue

            # BGP NSR Initial initsync version 11 (Reached)

            m = p13.match(line)
            if m:
                nsr_initial_initsync_version = int(m.groupdict()['nsr_initial_initsync_version'])
                nsr_initial_init_ver_status = str(m.groupdict()['nsr_initial_init_ver_status']).lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['nsr_initial_initsync_version'] = nsr_initial_initsync_version
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['nsr_initial_init_ver_status'] = nsr_initial_init_ver_status
                continue

            # BGP NSR/ISSU Sync-Group versions 0/0

            m = p14.match(line)
            if m:
                nsr_issu_sync_group_versions = str(m.groupdict()['nsr_issu_sync_group_versions'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['nsr_issu_sync_group_versions'] = nsr_issu_sync_group_versions
                continue

            # BGP scan interval 60 secs

            m = p15.match(line)
            if m:
                scan_interval = int(m.groupdict()['scan_interval'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['scan_interval'] = scan_interval
                continue

            # BGP is operating in STANDALONE mode.

            m = p16.match(line)
            if m:
                operation_mode = str(m.groupdict()['operation_mode']).lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['operation_mode'] = operation_mode
                continue

            # Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
            # Speaker              63         63         63         63          63           0

            m = p17.match(line)
            if m:
                process = str(m.groupdict()['process'])
                if 'process' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'] = {}
                if process not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process] = {}
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process]['rcvtblver'] =  int(m.groupdict()['rcvtblver'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process]['brib_rib'] =  int(m.groupdict()['brib_rib'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process]['labelver'] =  int(m.groupdict()['labelver'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process]['importver'] =  int(m.groupdict()['importver'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process]['sendtblver'] =  int(m.groupdict()['sendtblver'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['process'][process]['standbyver'] =  int(m.groupdict()['standbyver'])
                continue 

            # Neighbor        Spk    AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
            # 2001:db8:20:1:5::5

            m = p17_1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                data_on_nextline = True
                if 'neighbor' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'] = {}
                if neighbor not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor] = {}
                    continue
            
            # Neighbor        Spk    AS         msg_rcvd msg_sent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
            #                   3   200             0       0        0    0    0 00:00:00 Idle
            #                   0   200             0       0        0    0    0 00:00:00 Idle (Admin)!
            #                   0   60000.60001     0       0        0    0    0 00:00:00 Idle (Admin)!

            m = p17_2.match(line)
            if m and data_on_nextline:
                data_on_nextline = False
                if 'address_family' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'] = {}
                if address_family not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family] = {}

                try:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'] = int(m.groupdict()['remote_as'])
                except:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'] = m.groupdict()['remote_as']
                
                if route_distinguisher is not None:
                        bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['route_distinguisher'] =  route_distinguisher
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['spk'] = int(m.groupdict()['spk'])                
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['msg_sent'] = int(m.groupdict()['msg_sent'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['input_queue'] = int(m.groupdict()['input_queue'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['output_queue'] = int(m.groupdict()['output_queue'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['up_down'] =  str(m.groupdict()['up_down'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd'])
                continue

            # Neighbor        Spk    AS msg_rcvd msg_sent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
            # 10.1.5.5          0   200      60      62       63    0    0 00:57:32          0
            # 10.16.2.2           0   100       0       0        0    0    0 00:00:00 Idle
            # 10.0.0.35         0   200       0       0        0    0    0 00:00:00 Idle (Admin)!

            m = p17_3.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                if 'neighbor' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'] = {}
                if neighbor not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor] = {}

                if 'address_family' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'] = {}
                if address_family not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family] = {}

                try:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'] = int(m.groupdict()['remote_as'])
                except:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'] = m.groupdict()['remote_as']
                if route_distinguisher is not None:
                        bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['route_distinguisher'] =  route_distinguisher
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['spk'] = int(m.groupdict()['spk'])                
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['msg_sent'] = int(m.groupdict()['msg_sent'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['input_queue'] = int(m.groupdict()['input_queue'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['output_queue'] = int(m.groupdict()['output_queue'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['up_down'] =  str(m.groupdict()['up_down'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family]['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd'])
                continue
                
        return bgp_instance_summary_dict


# ============================================
# Parser for:
# 'show bgp instance all all all'
# 'show bgp instance all vrf all'
# 'show bgp instance all vrf all ipv4 unicast'
# 'show bgp instance all vrf all ipv6 unicast'
# ============================================

class ShowBgpInstanceAllAllSchema(MetaParser):

    """ Schema for:
        show bgp instance all all all
        show bgp instance all vrf all
        show bgp instance all vrf all ipv4 unicast
        show bgp instance all vrf all ipv6 unicast
    """

    schema = {
        'instance':
            {Any():
                {Optional('vrf'):
                    {Any():
                        {Optional('address_family'):
                            {Any():
                                {Optional('router_identifier'): str,
                                 Optional('vrf_id'): str,
                                 Optional('instance_number'): str,
                                 Optional('local_as'): Or(int, str),
                                 Optional('vrf_state'): str,
                                 Optional('bgp_vrf'): str,
                                 Optional('generic_scan_interval'): str,
                                 Optional('non_stop_routing'): bool,
                                 Optional('table_state'): str,
                                 Optional('table_id'): str,
                                 Optional('rd_version'): int,
                                 Optional('bgp_table_version'): int,
                                 Optional('nsr_initial_initsync_version'): str,
                                 Optional('nsr_issu_sync_group_versions'): str,
                                 Optional('nsr_initial_init_ver_status'): str,
                                 Optional('processed_prefix'): int,
                                 Optional('processed_paths'): int,
                                 Optional('scan_interval'): int,
                                 Optional('default_vrf'): str,
                                 Optional('route_distinguisher'): str,
                                 Optional('prefix'):
                                    {Any():
                                        {Optional('index'): 
                                            {Any(): 
                                                {
                                                Optional('next_hop'): str,
                                                Optional('status_codes'): str,
                                                Optional('metric'): str,
                                                Optional('locprf'): str,
                                                Optional('weight'): str,
                                                Optional('path'): str,
                                                Optional('origin_codes'): str
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ============================================================
# Parser for:
#   * show bgp instance all all all
#   * show bgp instance all vrf all
#   * show bgp instance all vrf all ipv4 unicast
#   * show bgp instance all vrf all ipv6 unicast
#   * show bgp instance {instance} all all
#   * show bgp instance {instance} vrf {vrf} {address_family}
# ============================================================
class ShowBgpInstanceAllAll(ShowBgpInstanceAllAllSchema):

    '''Parser for:
        show bgp instance all all all
        show bgp instance all vrf all
        show bgp instance all vrf all ipv4 unicast
        show bgp instance all vrf all ipv6 unicast
        show bgp instance {instance} all all
        show bgp instance {instance} vrf {vrf} {address_family}
    '''

    cli_command = ['show bgp instance {instance} all all',
                   'show bgp instance {instance} {vrf_type} {vrf}',
                   'show bgp instance {instance} {vrf_type} {vrf} {address_family}']

    exclude = ['bgp_table_version', 'rd_version', 'nsr_initial_init_ver_status', 'nsr_initial_initsync_version']

    def cli(self, vrf_type='all', address_family='', instance='all', vrf='all', output=None):

        # Verify vrf_type and address_family
        assert vrf_type in ['all', 'vrf']
        assert address_family in ['', 'ipv4 unicast', 'ipv6 unicast']

        # Execute command
        if output is None:
            if vrf_type == 'all':
                output = self.device.execute(self.cli_command[0].\
                                             format(instance=instance))
            else:
                if address_family:
                    output = self.device.execute(self.cli_command[2].\
                                                 format(instance=instance,
                                                 address_family=address_family,
                                                 vrf_type=vrf_type,
                                                 vrf=vrf))
                else:
                    output = self.device.execute(self.cli_command[1].\
                                                 format(instance=instance,
                                                        vrf_type=vrf_type,
                                                        vrf=vrf))
        # Init
        parsed_dict = {}
        last_prefix = None

        # Determind VRF and AF
        if vrf_type == 'all':
            vrf = 'default'
            af_default = None
        elif vrf_type == 'vrf':
            if vrf != 'all':
                input_vrf = vrf
            # Reset vrf
            vrf = None
            if address_family == 'ipv6 unicast':
                af_default = 'vpnv6 unicast'
            else:
                af_default = 'vpnv4 unicast'

        # BGP instance 0: 'default'
        p1 = re.compile(r'^\s*BGP +instance +(?P<instance_number>[0-9]+):'
                        r' +(?P<instance>(\S+))$')

        # VRF: VRF1
        p2 = re.compile(r'^\s*VRF: +(?P<vrf>(\S+))$')

        # Address Family: VPNv6 Unicast
        p3 = re.compile(r'^\s*Address +Family: +(?P<address_family>[\S\s]+)$')

        # BGP VRF VRF1, state: Active
        p4 = re.compile(r'^\s*BGP +VRF +(?P<bgp_vrf>(\S+)), +state:'
                        r' +(?P<vrf_state>(\S+))$')

        # BGP Route Distinguisher: 200:1
        # BGP Route Distinguisher: 172.16.2.90:1

        # VRF ID: 0x60000001
        p5 = re.compile(r'^\s*VRF +ID: +(?P<vrf_id>(\S+))$')

        # BGP router identifier 10.4.1.1, local AS number 100
        # BGP router identifier 10.10.10.108, local AS number 65108.65108
        p6 = re.compile(r'^\s*BGP +router +identifier +(?P<router_identifier>(\S+)),'
                        r' +local +AS +number +(?P<local_as>([\d\.]+))$')

        # BGP generic scan interval 60 secs
        p7 =  re.compile(r'^\s*BGP +generic +scan +interval'
                         r' +(?P<interval>(\d+)) +secs$')

        # Non-stop routing is enabled
        p8 = re.compile(r'^\s*Non-stop +routing is enabled$')

        # BGP table state: Active
        p9 = re.compile(r'^\s*BGP +table +state: +(?P<table_state>[a-zA-Z]+)$')

        # Table ID: 0xe0000010   RD version: 43
        p10 = re.compile(r'^\s*Table +ID: +(?P<table_id>[a-z0-9]+) +RD +version:'
                         r' +(?P<rd_version>[0-9]+)$')

        # BGP main routing table version 43
        p11 = re.compile(r'^\s*BGP +main +routing +table +version'
                         r' +(?P<bgp_table_version>[0-9]+)$')

        # BGP NSR Initial initsync version 11 (Reached)
        p12 = re.compile(r'^\s*BGP +NSR +Initial +initsync +version'
                         r' +(?P<nsr_initial_initsync_version>[0-9]+)'
                         r' +\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')

        # BGP NSR/ISSU Sync-Group versions 0/0
        p13 = re.compile(r'^\s*BGP +NSR/ISSU +Sync-Group +versions'
                         r' +(?P<nsr_issu_sync_group_versions>[0-9\/\s]+)$')

        # BGP scan interval 60 secs 
        p14 = re.compile(r'^\s*BGP +scan +interval +(?P<scan_interval>[0-9]+)'
                         r' +secs$')

        # Route Distinguisher: 200:1 (default for vrf VRF1)
        # Route Distinguisher: 172.16.2.90:1000 (default for vrf EVPN-Multicast-BTV)
        # Route Distinguisher: 172.16.2.88:1000
        p15 = re.compile(r'^\s*Route +Distinguisher:'
                         r' +(?P<route_distinguisher>\S+)'
                         r'(?: +\(default +for +vrf +(?P<default_vrf>\S+)\))?$')

        # *> 2001:db8:cdc9:190::/64   2001:db8:20:1:5::5
        # *>i[2][0][48][0014.01ff.0001][32][10.249.249.10]/136
        # *> [1][10.4.1.1:1][1234.bcff.5d7f.3e11.0505][12564523]/111
        p16_1 = re.compile(r'^\s*(?P<status_codes>(i|s|x|S|d|h|\*|\>|\s)+)'
                           r' *(?P<prefix>(?P<ip>[a-z0-9\.\:\[\]]+)\/(?P<mask>\d+))'
                           r'(?: +(?P<next_hop>\S+))?$')

        # 2219             0 200 33299 51178 47751 {27016} e
        # 2219             0 200 33299 51178 47751 {27016} 65107.65107 e
        p16_2 = re.compile(r'^\s*(?P<metric>[0-9]+) +(?P<weight>[0-9]+)'
                           r' +(?P<path>[0-9\.\{\}\s]+) '
                           r'+(?P<origin_codes>(i|e|\?))$')

        # Network            Next Hop   Metric LocPrf Weight Path
        # 172.16.2.88                        0    100      0 ?
        # 172.16.2.88                             100      0 i
        # 0.0.0.0                                          0 i
        p16_3 = re.compile(r'^\s*(?P<next_hop>(\S+))(?: +(?P<metric>(\d+)))?'
                           r'(?: +(?P<locprf>(\d+)))? +(?P<weight>(\d+))'
                           r' +(?P<origin_codes>(\?|i|e))$')

        # *> 10.1.1.0/24        10.186.5.5              2219             0 200 33299 51178 47751 {27016} e
        # * i                   10.64.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        # *>i10.9.2.0/24        10.64.4.4               2219    100      0 400 33299 51178 47751 {27016} e
        # *>i10.169.1.0/24      10.64.4.4               2219    100      0 300 33299 51178 47751 {27016} e
        # *>i192.168.111.0/24       10.189.99.98                                                    0       0 i
        # *> 10.7.7.7/32        10.10.10.107             0             0 65107.65107 ?
        p16 = re.compile(r'^(?P<status_codes>(i|s|x|S|d|h|\*|\>|\s)+)'
                         r' *(?P<prefix>(?P<ip>[0-9\.\:\[\]]+)\/(?P<mask>\d+))?'
                         r' +(?P<next_hop>\S+) +(?P<number>[\d\.\s\{\}]+)'
                         r'(?: *(?P<origin_codes>(i|e|\?)))?$')

        #                                                                 65107.65107 ?
        p17 = re.compile(r'(?P<path>[\d\.\s]+)'
                         r' *(?P<origin_codes>(i|e|\?))?$')

        # Processed 40 prefixes, 50 paths
        p18 = re.compile(r'^\s*Processed +(?P<processed_prefix>[0-9]+)'
                         r' +prefixes, +(?P<processed_paths>[0-9]+) +paths$')

        for line in output.splitlines():
            line = line.rstrip()

            # BGP instance 0: 'default'
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance'].replace("'","")
                instance_number = group['instance_number']
                inst_dict = parsed_dict.setdefault('instance', {}).\
                                        setdefault(instance, {})
                # VRF is default - init dictionary here
                if vrf_type == 'all' and vrf == 'default':
                    vrf_dict = inst_dict.setdefault('vrf', {}).\
                                         setdefault(vrf, {})
                continue

            # VRF: VRF1
            m = p2.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf_dict = inst_dict.setdefault('vrf', {}).setdefault(vrf, {})
                # Address family is default - init ipv4 unicast dictionary here
                if vrf_type == 'vrf' and af_default:
                    address_family = af_default
                    original_address_family = address_family
                    af_dict = vrf_dict.setdefault('address_family', {}).\
                                       setdefault(address_family, {})
                continue

            # Address Family: VPNv4 Unicast
            # Address family: IPv6 Labeled-unicast
            m = p3.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                original_address_family = address_family
                af_dict = vrf_dict.setdefault('address_family', {}).\
                                       setdefault(address_family, {})
                af_dict['instance_number'] = instance_number
                continue

            # BGP VRF VRF1, state: Active
            m = p4.match(line)
            if m:
                group = m.groupdict()
                # if no vrf key, set it to be the user input
                if not vrf:
                    vrf = input_vrf
                    vrf_dict = inst_dict.setdefault('vrf', {}).setdefault(vrf,{})
                    if vrf_type == 'vrf' and af_default:
                        address_family = af_default
                        original_address_family = address_family
                        af_dict = vrf_dict.setdefault('address_family', {}).\
                                           setdefault(address_family, {})
                # Set keys
                af_dict['bgp_vrf'] = group['bgp_vrf'].lower()
                af_dict['vrf_state'] = group['vrf_state'].lower()
                continue

            # VRF ID: 0x60000001
            m = p5.match(line)
            if m:
                vrf_id = m.groupdict()['vrf_id']
                af_dict['vrf_id'] = vrf_id
                continue

            # BGP router identifier 10.4.1.1, local AS number 100
            # BGP router identifier 10.10.10.108, local AS number 65108.65108
            m = p6.match(line)
            if m:
                group = m.groupdict()
                af_dict['router_identifier'] = group['router_identifier']
              
                try:
                    af_dict['local_as']= int(group['local_as'])
                except:
                    af_dict['local_as']= group['local_as']
                continue 

            # BGP generic scan interval 60 secs 
            m = p7.match(line)
            if m:
                af_dict['generic_scan_interval'] = m.groupdict()['interval']
                continue          

            # Non-stop routing is enabled
            m = p8.match(line)
            if m:
                af_dict['non_stop_routing'] = True
                continue

            # BGP table state: Active
            m = p9.match(line)
            if m:
                af_dict['table_state'] = m.groupdict()['table_state'].lower()
                continue

            # Table ID: 0x0   RD version: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                af_dict['table_id'] = group['table_id']
                af_dict['rd_version'] = int(group['rd_version'])
                continue

            # BGP main routing table version 43
            m = p11.match(line)
            if m:
                af_dict['bgp_table_version'] = int(m.groupdict()['bgp_table_version'])
                continue

            # BGP NSR Initial initsync version 11 (Reached)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                af_dict['nsr_initial_initsync_version'] = group['nsr_initial_initsync_version']
                af_dict['nsr_initial_init_ver_status'] = group['nsr_initial_init_ver_status'].lower()
                continue

            # BGP NSR/ISSU Sync-Group versions 0/0
            m = p13.match(line)
            if m:
                af_dict['nsr_issu_sync_group_versions'] = \
                                m.groupdict()['nsr_issu_sync_group_versions']
                continue

            # BGP scan interval 60 secs
            m = p14.match(line)
            if m:
               af_dict['scan_interval'] = int(m.groupdict()['scan_interval'])
               continue

            # Route Distinguisher: 200:1 (default for vrf VRF1)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                rd = group['route_distinguisher']
                # Set af
                address_family = original_address_family + ' RD ' + rd
                # New dict
                af_dict = vrf_dict.setdefault('address_family', {}).\
                                   setdefault(address_family, {})
                # Set keys
                af_dict['route_distinguisher'] = rd
                if group['default_vrf']:
                    af_dict['default_vrf'] = group['default_vrf'].lower()
                continue

            # *> 2001:db8:cdc9:190::/64   2001:db8:20:1:5::5
            # *>i[2][0][48][0014.01ff.0001][32][10.249.249.10]/136
            m = p16_1.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix']
                if prefix:
                    last_prefix = prefix
                    index = 1
                else:
                    index += 1
                # Set dict
                pfx_dict = af_dict.setdefault('prefix', {}).setdefault(last_prefix, {}).\
                                   setdefault('index', {}).setdefault(index, {})
                # Set keys
                pfx_dict['status_codes'] = group['status_codes'].strip().replace(" ", "")
                if group['next_hop']:
                    pfx_dict['next_hop'] = group['next_hop']
                continue

            # 2219             0 200 33299 51178 47751 {27016} e
            # 2219             0 200 33299 51178 47751 {27016} 65107.65107 e
            m = p16_2.match(line)
            if m:
                group = m.groupdict()
                pfx_dict['metric'] = group['metric']
                pfx_dict['weight'] = group['weight']
                pfx_dict['path'] = group['path']
                pfx_dict['origin_codes'] = group['origin_codes']
                continue

            # Network            Next Hop   Metric LocPrf Weight Path
            # 172.16.2.88                        0    100      0 ?
            # 172.16.2.88                             100      0 i
            m = p16_3.match(line)
            if m:
                group = m.groupdict()
                pfx_dict['next_hop'] = group['next_hop']
                if group['metric']:
                    pfx_dict['metric'] = group['metric']
                if group['locprf']:
                    pfx_dict['locprf'] = group['locprf']
                pfx_dict['weight'] = group['weight']
                pfx_dict['origin_codes'] = group['origin_codes']
                continue

            # *> 10.1.1.0/24        10.186.5.5              2219             0 200 33299 51178 47751 {27016} e
            # * i                   10.64.4.4               2219    100      0 400 33299 51178 47751 {27016} e
            # *>i10.9.2.0/24        10.64.4.4               2219    100      0 400 33299 51178 47751 {27016} e
            # *>i10.169.1.0/24      10.64.4.4               2219    100      0 300 33299 51178 47751 {27016} e
            # *>i192.168.111.0/24       10.189.99.98                                                    0       0 i
            # *> 10.7.7.7/32        10.10.10.107             0             0 65107.65107 ?
            m = p16.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix']
                if prefix:
                    last_prefix = prefix
                    index = 1
                else:
                    index += 1
                # Set dict
                pfx_dict = af_dict.setdefault('prefix', {}).setdefault(last_prefix, {}).\
                                   setdefault('index', {}).setdefault(index, {})
                # Set keys
                pfx_dict['next_hop'] = group['next_hop']
                pfx_dict['status_codes'] = group['status_codes'].strip().replace(" ", "")
                if group['origin_codes']:
                    pfx_dict['origin_codes'] = group['origin_codes']
                
                # Parse and set the numbers
                group_num = group['number']
                m1 = re.compile(r'^(?P<metric>[0-9]+)  +(?P<locprf>[0-9]+)  +(?P<weight>[0-9]+) (?P<path>[0-9\.\{\}\s]+)$').match(group_num)
                m2 = re.compile(r'^(?P<value>[0-9]+)(?P<space>\s{2,20})(?P<weight>[0-9]+) (?P<path>[0-9\.\{\}\s]+)$').match(group_num)
                m3 = re.compile(r'^(?P<weight>[0-9]+) (?P<path>(([\d\.]+\s)|(\{[\d\.]+\}\s))+)$').match(group_num)
                m4 = re.compile(r'^(?P<locprf>(\d+)) +(?P<weight>(\d+))$').match(group_num.strip())
                if m1:
                    pfx_dict['metric'] = m1.groupdict()['metric']
                    pfx_dict['locprf'] = m1.groupdict()['locprf']
                    pfx_dict['weight'] = m1.groupdict()['weight']
                    pfx_dict['path'] = m1.groupdict()['path'].strip()
                elif m2:
                    if len(m2.groupdict()['space']) > 8:
                        pfx_dict['metric'] = m2.groupdict()['value']
                    else:
                        pfx_dict['locprf'] = m2.groupdict()['value']

                    pfx_dict['weight'] = m2.groupdict()['weight']
                    pfx_dict['path'] = m2.groupdict()['path'].strip()
                elif m3:
                    pfx_dict['weight'] = m3.groupdict()['weight']
                    pfx_dict['path'] = m3.groupdict()['path'].strip()
                elif m4:
                    pfx_dict['locprf'] = m4.groupdict()['locprf']
                    pfx_dict['weight'] = m4.groupdict()['weight']
                continue

            #                                                                 65107.65107 ?
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if 'path' in pfx_dict:
                    pfx_dict['path'] += ' ' + group['path'].strip()
                if m.groupdict()['origin_codes']:
                    pfx_dict['origin_codes'] = group['origin_codes']
                continue

            # Processed 40 prefixes, 50 paths
            m = p18.match(line)
            if m:
                group = m.groupdict()
                af_dict['processed_prefix'] = int(group['processed_prefix'])
                af_dict['processed_paths'] = int(group['processed_paths'])
                continue

        return parsed_dict 


################################################################################

"""Schema for 'show bgp sessions'"""
class ShowBgpSessionsSchema(MetaParser):
    schema = {
        'instance': {
            Any(): {
                'vrf': {
                    Any(): {
                        'neighbors': {
                            Any(): {
                                'spk': int,
                                'as_number': int,
                                'in_q': int,
                                'out_q': int,
                                'nbr_state': str,
                                'nsr_state': str
                            }
                        }
                    }
                }
            }
        }
    }

# ==============================
# Parser for 'show bgp sessions'
# ==============================

class ShowBgpSessions(ShowBgpSessionsSchema):
    """Parser for show bgp sessions"""

    # TODO schema
    cli_command = 'show bgp sessions'
    def cli(self, output=None):
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}
        instance = 'default'

        # 10.36.3.3         default                 0 65000     0     0  Established  None
        # 2001:1:1:1::1   default                 0 65000     0     0  Established  None
        # 10.1.7.212     default                 0 10396     0     0  Established  NSR Ready
        p1 = re.compile(r'^(?P<neighbor>\S+) +(?P<vrf>\S+) +(?P<spk>\d+) +'
            '(?P<as_number>\d+) +(?P<in_q>\d+) +(?P<out_q>\d+) +'
            '(?P<nbr_state>\w+) +(?P<nsr_state>[\w\s]+)$')

        # 2001:db8:4401:4453::6f9
        p1_1 = re.compile(r'^(?P<neighbor>[\w\d:]+)$')

        # default 0 65000 0 0 Established NSR Ready
        p1_2 = re.compile(r'^(?P<vrf>\S+) +(?P<spk>\d+) +'
                          r'(?P<as_number>\d+) +(?P<in_q>\d+) +(?P<out_q>\d+) +'
                          r'(?P<nbr_state>\w+) +(?P<nsr_state>[\w\s]+)$')

        # BGP instance 0: 'default'
        p2 = re.compile(r'^BGP +instance +\d+: +\'(?P<instance>\S+)\'$')

        for line in out.splitlines():
            line = line.strip()

            # 10.36.3.3         default                 0 65000     0     0  Established  None
            # 2001:1:1:1::1   default                 0 65000     0     0  Established  None
            # 10.1.7.212     default                 0 10396     0     0  Established  NSR Ready
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                neighbor = group['neighbor']
                spk = int(group['spk'])
                as_number = int(group['as_number'])
                in_q = int(group['in_q'])
                out_q = int(group['out_q'])
                nbr_state = group['nbr_state']
                nsr_state = group['nsr_state']

                neighbor_dict = ret_dict.setdefault('instance', {}). \
                                    setdefault(instance, {}). \
                                    setdefault('vrf', {}). \
                                    setdefault(vrf, {}). \
                                    setdefault('neighbors', {}). \
                                    setdefault(neighbor, {})

                neighbor_dict.update({'spk': spk})
                neighbor_dict.update({'as_number': as_number})
                neighbor_dict.update({'in_q': in_q})
                neighbor_dict.update({'out_q': out_q})
                neighbor_dict.update({'nbr_state': nbr_state})
                neighbor_dict.update({'nsr_state': nsr_state})
                continue

            # 2001:db8:4401:4453::6f9
            m = p1_1.match(line)
            if m:
                neighbor = m.groupdict()['neighbor']
                continue

            # default 0 65000 0 0 Established NSR Ready
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict = ret_dict.setdefault('instance', {}). \
                                            setdefault(instance, {}). \
                                            setdefault('vrf', {}). \
                                            setdefault(group['vrf'], {}). \
                                            setdefault('neighbors', {}). \
                                            setdefault(neighbor, {})

                neighbor_dict['spk'] = int(group['spk'])
                neighbor_dict['as_number'] = int(group['as_number'])
                neighbor_dict['in_q'] = int(group['in_q'])
                neighbor_dict['out_q'] = int(group['out_q'])
                neighbor_dict['nbr_state'] = group['nbr_state']
                neighbor_dict['nsr_state'] = group['nsr_state']
                continue

            # BGP instance 0: 'default'
            m = p2.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance']
                continue

        return ret_dict

# ===========================================
# Parser for 
#   * 'show bgp instance {instance} sessions'
# ===========================================

class ShowBgpInstanceSessions(ShowBgpSessions):
    """Parser for show bgp instance {instance} sessions"""

    cli_command = 'show bgp instance {instance} sessions'
    def cli(self, instance, output=None):
        out = output if output else self.device.execute(
                self.cli_command.format(instance=instance))
        return super().cli(output=out)

# ===========================================
# Parser for 
#   * 'show bgp instance all sessions'
# ===========================================

class ShowBgpInstanceAllSessions(ShowBgpSessions):
    """Parser for show bgp instance all sessions"""

    cli_command = 'show bgp instance all sessions'
    def cli(self, output=None):
        out = output if output else self.device.execute(
                self.cli_command)
        return super().cli(output=out)

# ====================================
# Schema for 'show bgp vrf-db vrf all'
# ====================================
class ShowBgpVrfDbVrfAllSchema(MetaParser):
    ''' Schema for:
        * 'show bgp vrf-db vrf all'
    '''

    schema = {
        'vrf': 
            {Any():
                {'id': str,
                'rd': str,
                'ref': int,
                'afs': list,
                },
            },
        }

# ====================================
# Parser for 'show bgp vrf-db vrf all'
# ====================================
class ShowBgpVrfDbVrfAll(ShowBgpVrfDbVrfAllSchema):
    ''' Parser for:
        * 'show bgp vrf-db vrf all'
    '''

    cli_command = 'show bgp vrf-db vrf all'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init
        parsed_dict = {}
        vrf_dict = {}

        # VRF                              ID          RD                REF AFs
        # default                          0x60000000  0:0:0             8   v4u, Vv4u, v6u, 
        # NOVI-TST                         0x60000001  172.16.2.88:0     4   v4u
        # test_ipv6_overlay                0x0         0:0:0             2   v4u, v6u
        # BTV-nPVR-MULTICAST-IAAS          0x60000004  172.16.2.88:1     4   v4u
        # ES:GLOBAL                        -           172.16.2.88:0     2   L2evpn
        # VPWS:2000                        -           172.16.2.88:2000  2   L2evpn
        # VPWS:2078                        -           172.16.2.88:2078  2   L2evpn
        # VPWS:10293                       -           172.16.2.88:10293 2   L2evpn
        # EVPN-Multicast-BTV               -           172.16.2.88:1000  2   L2evpn
        p1 = re.compile(r'^(?P<vrf>(\S+)) +(?P<id>([x0-9\-]+)) +(?P<rd>(\S+))'
                         ' +(?P<ref>(\d+)) +(?P<afs>(.*))$')

        #                                                                  Vv6u, L2evpn
        p2 = re.compile(r'^(?P<item>([a-zA-Z0-9\,\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            # VRF                              ID          RD                REF AFs
            # default                          0x60000000  0:0:0             8   v4u, Vv4u, v6u, 
            # NOVI-TST                         0x60000001  172.16.2.88:0     4   v4u
            # test_ipv6_overlay                0x0         0:0:0             2   v4u, v6u
            # BTV-nPVR-MULTICAST-IAAS          0x60000004  172.16.2.88:1     4   v4u
            # ES:GLOBAL                        -           172.16.2.88:0     2   L2evpn
            # VPWS:2000                        -           172.16.2.88:2000  2   L2evpn
            # VPWS:2078                        -           172.16.2.88:2078  2   L2evpn
            # VPWS:10293                       -           172.16.2.88:10293 2   L2evpn
            # EVPN-Multicast-BTV               -           172.16.2.88:1000  2   L2evpn
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                                        setdefault(group['vrf'], {})
                vrf_dict['id'] = group['id']
                vrf_dict['rd'] = group['rd']
                vrf_dict['ref'] = int(group['ref'])
                vrf_dict['afs'] = group['afs'].strip().replace(",", "").split()
                continue

            #                                                                  Vv6u, L2evpn
            m = p2.match(line)
            if m:
                if vrf_dict:
                    afs = m.groupdict()['item'].strip().replace(",", "").split()
                    vrf_dict['afs'].extend(afs)
                continue

        return parsed_dict


# ===========================================================
# Parser for:
# 'show bgp l2vpn evpn'
# ===========================================================

class ShowBgpL2vpnEvpnSchema(MetaParser):

    """Schema for:
        show bgp l2vpn evnpn
    """

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {
                         Optional('router_identifier'): str,
                         Optional('local_as'): int,
                         Optional('generic_scan_interval'): str,
                         Optional('non_stop_routing'): str,
                         Optional('table_state'): str,
                         Optional('table_id'): str,
                         Optional('rd_version'): int,
                         Optional('bgp_table_version'): int,
                         Optional('local_router_id'): str,
                         Optional('route_distinguisher'): str,
                         Optional('nsr_initial_initsync_version'): str,
                         Optional('nsr_initial_init_ver_status'): str,
                         Optional('nsr_issu_sync_group_versions'): str,
                         Optional('scan_interval'): int,
                         Optional('default_vrf'): str,
                         Optional('aggregate_address_ipv4_address'): str,
                         Optional('aggregate_address_ipv4_mask'): str,
                         Optional('aggregate_address_as_set'): bool,
                         Optional('aggregate_address_summary_only'): bool,
                         Optional('v6_aggregate_address_ipv6_address'): str,
                         Optional('v6_aggregate_address_as_set'): bool,
                         Optional('v6_aggregate_address_summary_only'): bool,
                         Optional('processed_prefix'): int,
                         Optional('processed_paths'): int,
                         Optional('prefixes'):
                            {Any(): 
                                {'index': 
                                    {Any(): 
                                        {Optional('next_hop'): str,
                                         Optional('status_codes'): str,
                                         Optional('path_type'): str,
                                         Optional('metric'): int,
                                         Optional('localprf'): int,
                                         Optional('weight'): int,
                                         Optional('path'): str,
                                         Optional('origin_codes'): str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
        

# ================================
# Parser for 'show bgp l2vpn evpn'
# ================================

class ShowBgpL2vpnEvpn(ShowBgpL2vpnEvpnSchema):
    """Parser for show bgp l2vpn evpn"""

    cli_command = 'show bgp l2vpn evpn'
    exclude = [
      'bgp_table_version',
      'status_codes',
      'local_router_id',
      'path_type',
      'weight']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init dictionary
        parsed_dict = {}
        af_dict = {}
        prefix_dict = {}
        prefix_index_dict = {}
        vrf_name = 'default'
        address_family = 'l2vpn evpn'
        original_address_family = address_family
        # Init vars
        index = 1
        data_on_nextline = False
        bgp_table_version = local_router_id = ''
        prefix = ''

        p = re.compile(r'^\s*Network +Next Hop +Metric +LocPrf +Weight Path$')
        p1 = re.compile(r'^\s*BGP +routing +table +information +for +VRF'
                            ' +(?P<vrf_name>\S+), +address +family'
                            ' +(?P<address_family>[\w\s\-\_]+)$')
        p2 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+), +(L|l)ocal'
                            ' +(R|r)outer +ID +is +(?P<local_router_id>[0-9\.]+)$')
        p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            '(?P<prefix>[\w\.\:\/\[\]\,]{3,})'
                            '(?: *(?P<next_hop>[\w\.\:\/\[\]\,]+))?$')
        p3_1_1 = re.compile(r'^(?P<status_codes>(s|x|S|d|h|\*|\>)+)(?P<path_type>'
                            '(i|e|c|l|a|r|I))(?P<prefix>[\w\.\/]+) '
                            '+(?P<next_hop>[\w\.\/]+) +'
                            '(?P<metric>\d+) +(?P<localprf>\d+) '
                            '+(?P<weight>\d+) +(?P<path>[\d ]+) +'
                            '(?P<origin_codes>(i|e|\?|\||&))$')
        p3_1_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            ' (?P<path_type>(i|e|c|l|a|r|I)) '
                            '(?: *(?P<next_hop>[\w\.\:\/\[\]\,]+))?$')
        p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))'
                            '(?P<prefix>[\w\.\:\/\[\]\,]+)'
                            ' +(?P<next_hop>[\w\.\:]+)'
                            ' +(?P<numbers>[\w\s\(\)\{\}]+)'
                            ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
        p3_2_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                            '(?P<prefix>[\w\.\:\/\[\]\,]+)'
                            ' +(?P<next_hop>[\w\.\:]+)'
                            ' +(?P<numbers>[\w\s\(\)\{\}\?]+)$')
        p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            ' *(?P<next_hop>[\w\.\:]{8,})'
                            '(?: +(?P<numbers>[\w\s\(\)\{\}]+))?'
                            ' +(?P<origin_codes>(i|e|\?|\|))$')
        p3_3_1 = re.compile(r'^\s*(?P<status_codes>(\*\>|s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            '( *(?P<origin_codes>(i|e|\?|\&|\|)+))'
                            ' +(?P<next_hop>[\w\.\:]+)'
                            ' +(?P<numbers>[\w\s\(\)\{\}\?]+)$')
        p3_3_2 = re.compile(r'^\s*(?P<numbers>[0-9\s\(\)\{\}]+)? +'
                            '(?P<origin_codes>(i|e|\?|\|))$')
        p3_4 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+)$')
        p4 = re.compile(r'^\s*Route +Distinguisher *: +(?P<route_distinguisher>(\S+))'
                            '(?: +\(((VRF +(?P<default_vrf>\S+))|'
                            '((?P<default_vrf1>\S+)VNI +(?P<vni>\d+)'
                            '|(default +for +vrf +(?P<default_vrf2>\S+))))\))?$')
        
        p5 = re.compile(r'^\s*BGP *router *identifier *(?P<router_identifier>[0-9\.]+)'
                         ', *local *AS *number *(?P<local_as>[0-9]+)$')
        p6 =  re.compile(r'^\s*BGP *generic *scan *interval *'
                            '(?P<generic_scan_interval>[0-9]+) *secs$')
        p7 = re.compile(r'^\s*Non-stop *routing *is'
                        ' *(?P<non_stop_routing>[A-Za-z]+)$')
        p8 = re.compile(r'^\s*BGP *table *state: *(?P<table_state>[a-zA-Z]+)$')
        p9 = re.compile(r'^\s*Table *ID: *(?P<table_id>[a-z0-9]+)'
                         ' *RD *version: (?P<rd_version>[0-9]+)$')
        p10 = re.compile(r'^\s*BGP *main *routing *table *version'
                         ' *(?P<bgp_table_version>[0-9]+)$')
        p11 = re.compile(r'^\s*BGP *NSR *Initial *initsync *version *'
                            '(?P<nsr_initial_initsync_version>[0-9]+)'
                          ' *\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')
        p12 = re.compile(r'^\s*BGP *NSR/ISSU *Sync-Group *versions *'
                            '(?P<nsr_issu_sync_group_versions>[0-9\/\s]+)$')
        p13 = re.compile(r'^\s*BGP *scan *interval *(?P<scan_interval>[0-9\s]+) *secs$')
        p14 = re.compile(r'^(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                            '(?P<path_type>(i|e|c|l|a|r|I))? *(?P<prefix>[\w\.\/\[\]\,]+)$')
        p15 = re.compile(r'^(?P<next_hop>[\w\.\:]+) *(?P<number>[\d\s\{\}]+)?'
                            '(?: *(?P<origin_codes>(i|e|\?)))$')
        p16 = re.compile(r'^\s*Processed +(?P<processed_prefix>[0-9]+) +prefixes, +'
                            '(?P<processed_paths>[0-9]+) +paths$')

        for line in out.splitlines():
            line = line.strip()

            # Network            Next Hop            Metric     LocPrf     Weight Path
            m = p.match(line)
            if m:
                continue

            # BGP routing table information for VRF VRF1, address family IPv4 Unicast
            m = p1.match(line)
            if m:
                # Get values
                vrf_name = m.groupdict()['vrf_name']
                address_family = m.groupdict()['address_family'].lower()
                original_address_family = address_family

                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                  .setdefault('address_family', {}).setdefault(address_family, {})
                continue

            # BGP table version is 35, local router ID is 10.229.11.11
            # BGP table version is 381, Local Router ID is 10.4.1.2
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = m.groupdict()['local_router_id']
                af_dict.update({'bgp_table_version': bgp_table_version})
                af_dict.update({'local_router_id': local_router_id})
                continue

            #                     2001:db8:400:13b1:21a:1ff:feff:161/128
            m = p3_4.match(line)
            if m:
                # Get keys
                if 'njected' not in line and 'next_hop' in m.groupdict():
                    next_hop = m.groupdict()['next_hop']

                    if data_on_nextline:
                        data_on_nextline =  False
                    else:
                        index += 1

                    # Init dict
                    index_dict = af_dict.setdefault('prefixes', {}).setdefault(prefix, {})\
                      .setdefault('index', {}).setdefault(index, {})

                    # Set keys
                    index_dict.update({'next_hop': next_hop})
                continue

            # * i                   2001:db8:400:a2bb:0:abcd:5678:3
            m = p3_1_2.match(line)
            if m:
                # Get keys
                if 'njected' not in line and 'next_hop' in m.groupdict():
                    next_hop = m.groupdict()['next_hop']
                    status_codes = m.groupdict()['status_codes']
                    path_type = m.groupdict()['path_type']

                    index += 1

                    # Init dict
                    index_dict = af_dict.setdefault('prefixes', {}).setdefault(prefix, {})\
                      .setdefault('index', {}).setdefault(index, {})

                    # Set keys
                    index_dict.update({'next_hop': next_hop})
                    index_dict.update({'status_codes': status_codes})
                    index_dict.update({'path_type': path_type})
                continue
            
            # *> [3][0][32][192.168.19.35]/70
            m = p14.match(line)
            if m:
                group = m.groupdict()
                status_codes = group['status_codes'].strip()
                prefix = group['prefix']
                current_index = prefix_index_dict.get(prefix, 0) + 1
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                        .setdefault('address_family', {}).setdefault(address_family, {})
                
                prefix_dict = af_dict.setdefault('prefixes', {}). \
                                setdefault(prefix, {}). \
                                setdefault('index', {}). \
                                setdefault(current_index, {})
                
                prefix_dict.update({'status_codes': status_codes})
                prefix_index_dict.update({prefix: current_index})
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath
            # Network            Next Hop         Metric   LocPrf   Weight Path
            
            # *>i[2]:[77][7,0][10.69.9.9,1,151587081][10.135.1.1,22][10.106.101.1,10.76.1.30]/616
            # *>i2001:db8:aaaa:1::/113       ::ffff:10.106.101.1
            m = p3_1.match(line)
            # *>i10.111.8.3/32     10.84.66.66           2000        100          0 200 i
            # *>i10.111.8.4/32     10.84.66.66           2000        100          0 200 i
            m1 = p3_1_1.match(line)

            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                status_codes = m.groupdict()['status_codes']
                path_type = m.groupdict()['path_type']
                prefix = m.groupdict()['prefix']
                if status_codes == None or path_type == None or prefix == None:
                    continue
            
                # Set keys
                index_dict = af_dict.setdefault('prefixes', {}).setdefault(prefix, {})\
                  .setdefault('index', {}).setdefault(index, {})
                index_dict.update({'status_codes': status_codes})
                index_dict.update({'path_type': path_type})
                if m.groupdict()['next_hop']:
                    index_dict.update({'next_hop': m.groupdict()['next_hop']})
                if 'metric' in m.groupdict():
                    index_dict.update({'metric': int(m.groupdict()['metric'])})
                if 'localprf' in m.groupdict():
                    index_dict.update({'localprf': int(m.groupdict()['localprf'])})
                if 'weight' in m.groupdict():
                    index_dict.update({'weight': int(m.groupdict()['weight'])})
                if 'path' in m.groupdict():
                    index_dict.update({'path': m.groupdict()['path'].strip()})
                if 'origin_codes' in m.groupdict():                
                    index_dict.update({'origin_codes': m.groupdict()['origin_codes']})
                
                # Check if aggregate_address_ipv4_address
                if path_type and 'a' in path_type:
                    address, mask = prefix.split("/")
                    if ':' in prefix:
                        index_dict.update({'v6_aggregate_address_ipv6_address': prefix})
                        index_dict.update({'v6_aggregate_address_as_set': True})
                        index_dict.update({'v6_aggregate_address_summary_only': True})
                    else:
                        index_dict.update({'aggregate_address_ipv4_address': address})
                        index_dict.update({'aggregate_address_ipv4_mask': mask})
                        index_dict.update({'aggregate_address_as_set': True})
                        index_dict.update({'aggregate_address_summary_only': True})
                continue


            #                     0.0.0.0               100      32768 i
            #                     10.106.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            # *>i                 10.106.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            m = p3_3.match(line)

            # * e                   10.70.2.2                                      0 100 300 ?
            # *>e                   10.70.1.2                                      0 100 300 ?
            m1 = p3_3_1.match(line)
            m = m if m else m1
            if m and not prefix_dict:
                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = m.groupdict()['status_codes']
                if m.groupdict()['path_type']:
                    path_type = m.groupdict()['path_type']
                next_hop = m.groupdict()['next_hop']
                origin_codes = m.groupdict()['origin_codes']

                # Set keys
                index_dict = af_dict.setdefault('prefixes', {}).setdefault(prefix, {})\
                  .setdefault('index', {}).setdefault(index, {})
                
                index_dict.update({'next_hop': next_hop})
                if origin_codes:
                    index_dict.update({'origin_codes': origin_codes})
                if status_codes:
                    index_dict.update({'status_codes': status_codes})
                if m.groupdict()['path_type']:
                    index_dict.update({'path_type': path_type})

                try:
                    # Set values of status_codes and path_type from prefix line
                    index_dict.update({'status_codes': status_codes})
                    index_dict.update({'path_type': path_type})
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    index_dict.update({'metric': int(m1.groupdict()['metric'])})
                    index_dict.update({'localprf': int(m1.groupdict()['localprf'])})
                    index_dict.update({'weight': int(m1.groupdict()['weight'])})
                    # Set path
                    if 'path' in m1.groupdict():
                        index_dict.update({'path': m1.groupdict()['path'].strip()})
                elif m2:
                    index_dict.update({'weight': int(m2.groupdict()['weight'])})
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        index_dict.update({'metric': int(m2.groupdict()['value'])})
                    else:
                        index_dict.update({'localprf': int(m2.groupdict()['value'])})
                    # Set path
                    if m2.groupdict()['path']:
                        index_dict.update({'path': m2.groupdict()['path'].strip()})
                elif m3:
                    index_dict.update({'weight': int(m3.groupdict()['weight'])})
                    index_dict.update({'path': m3.groupdict()['path'].strip()})
                continue

            # 100      33445 i
            m = p3_3_2.match(line)
            if m:
                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    index_dict.update({'metric': int(m1.groupdict()['metric'])})
                    index_dict.update({'localprf': int(m1.groupdict()['localprf'])})
                    index_dict.update({'weight': int(m1.groupdict()['weight'])})
                    # Set path
                    if m1.groupdict()['path']:
                        index_dict.update({'path': m1.groupdict()['path'].strip()})
                elif m2:
                    index_dict.update({'weight': int(m2.groupdict()['weight'])})
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        index_dict.update({'metric': int(m2.groupdict()['value'])})
                    else:
                        index_dict.update({'localprf': int(m2.groupdict()['value'])})
                    # Set path
                    if m2.groupdict()['path']:
                        index_dict.update({'path': m.groupdict()['path'].strip()})
                elif m3:
                    index_dict.update({'weight': int(m3.groupdict()['weight'])})
                    index_dict.update({'path': m3.groupdict()['path'].strip()})
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # Route Distinguisher: 100:100     (VRF VRF1)
            # Route Distinguisher: 2:100    (VRF vpn2)
            # Route Distinguisher: 10.49.1.0:3    (L3VNI 9100)
            # Route Distinguisher: 172.16.2.88:1000 (default for vrf EVPN-Multicast-BTV)
            m = p4.match(line)
            if m:
                route_distinguisher = m.groupdict()['route_distinguisher']
                new_address_family = original_address_family + ' RD ' + route_distinguisher
                
                # Set keys
                naf_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                  .setdefault('address_family', {}).setdefault(new_address_family, {})
                naf_dict.update({'bgp_table_version': bgp_table_version})
                naf_dict.update({'local_router_id': local_router_id})
                naf_dict.update({'route_distinguisher': route_distinguisher})

                if m.groupdict()['default_vrf']:
                    naf_dict.update({'default_vrf': m.groupdict()['default_vrf']})
                elif m.groupdict()['default_vrf1']:
                    naf_dict.update({'default_vrf': m.groupdict()['default_vrf1']})                            

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                  .setdefault('address_family', {}).setdefault(address_family, {})
                continue


            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>a10.121.0.0/8       0.0.0.0                  100      32768 i
            # *>i10.21.33.33/32   10.36.3.3         0        100          0 ?
            # l10.34.34.0/24      0.0.0.0                  100      32768 i
            # *>i2001::33/128     ::ffff:10.36.3.3  0        100          0 ?
            # *>l[2]:[0]:[0]:[48]:[0000.19ff.f320]:[0]:[0.0.0.0]/216
            # *>i                 10.186.0.2        0        100          0 ?
            # *>l10.4.1.0/24        0.0.0.0                            100      32768 i
            # *>r10.16.1.0/24        0.0.0.0                4444        100      32768 ?
            # *>r10.16.2.0/24        0.0.0.0                4444        100      32768 ?
            # *>i10.49.0.0/16     10.106.101.1                            100          0 10 20 30 40 50 60 70 80 90 i
            # *>i10.4.2.0/24     10.106.102.4                            100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            m = p3_2.match(line)

            # *&i10.145.1.0/24        192.168.151.2                0        100          0 ?
            m1 = p3_2_1.match(line)
            m = m if m else m1
            if m:
                # New prefix, reset index count
                index = 1
                
                # Get keys
                status_codes = m.groupdict()['status_codes']
                path_type = m.groupdict()['path_type']
                prefix = m.groupdict()['prefix']
                next_hop = m.groupdict()['next_hop']
                origin_codes = m.groupdict()['origin_codes']

                # Init dict
                index_dict = af_dict.setdefault('prefixes', {}).setdefault(prefix, {})\
                  .setdefault('index', {}).setdefault(index, {})
                index_dict.update({'next_hop': next_hop})
                index_dict.update({'origin_codes': origin_codes})
                index_dict.update({'status_codes': status_codes})
                index_dict.update({'path_type': path_type})

                # Parse numbers
                numbers = m.groupdict()['numbers']
                
                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    index_dict.update({'metric': int(m1.groupdict()['metric'])})
                    index_dict.update({'localprf': int(m1.groupdict()['localprf'])})
                    index_dict.update({'weight': int(m1.groupdict()['weight'])})
                    # Set path
                    if m1.groupdict()['path']:
                        index_dict.update({'path': m1.groupdict()['path'].strip()})
                elif m2:
                    index_dict.update({'weight': int(m2.groupdict()['weight'])})
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        index_dict.update({'metric': int(m2.groupdict()['value'])})
                    else:
                        index_dict.update({'localprf': int(m2.groupdict()['value'])})
                    # Set path
                    if m2.groupdict()['path']:
                        index_dict.update({'path': m.groupdict()['path'].strip()})
                elif m3:
                    index_dict.update({'weight': int(m3.groupdict()['weight'])})
                    index_dict.update({'path': m3.groupdict()['path'].strip()})

                # Check if aggregate_address_ipv4_address
                if 'a' in path_type:
                    address, mask = prefix.split("/")
                    if ':' in prefix:
                        index_dict.update({'v6_aggregate_address_ipv6_address': prefix})
                        index_dict.update({'v6_aggregate_address_as_set': True})
                        index_dict.update({'v6_aggregate_address_summary_only': True})
                    else:
                        index_dict.update({'aggregate_address_ipv4_address': address})
                        index_dict.update({'aggregate_address_ipv4_mask': mask})
                        index_dict.update({'aggregate_address_as_set': True})
                        index_dict.update({'aggregate_address_summary_only': True})
                continue
                # BGP router identifier 10.4.1.1, local AS number 100

            m = p5.match(line)
            if m:
                router_identifier = m.groupdict()['router_identifier']
                local_as = int(m.groupdict()['local_as'])
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'router_identifier': router_identifier})
                af_dict.update({'local_as': local_as})
                continue
            
            # BGP generic scan interval 60 secs 

            m = p6.match(line)
            if m:
                generic_scan_interval = m.groupdict()['generic_scan_interval']
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'generic_scan_interval': generic_scan_interval})
                continue
            
            # Non-stop routing is enabled

            m = p7.match(line)
            if m:
                non_stop_routing = str(m.groupdict()['non_stop_routing'])
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'non_stop_routing': non_stop_routing})
                continue
            
            # BGP table state: Active

            m = p8.match(line)
            if m:
                table_state = m.groupdict()['table_state'].lower()
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'table_state': table_state})
                continue
            
            # Table ID: 0x0   RD version: 0

            m = p9.match(line)
            if m:
                table_id = str(m.groupdict()['table_id'])
                rd_version = int(m.groupdict()['rd_version'])
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'table_id': table_id})
                af_dict.update({'rd_version': rd_version})
                continue
            
            # BGP main routing table version 43

            m = p10.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'bgp_table_version': bgp_table_version})
                continue
            
            # BGP NSR Initial initsync version 11 (Reached)

            m = p11.match(line)
            if m:
                nsr_initial_initsync_version = m.groupdict()['nsr_initial_initsync_version']
                nsr_initial_init_ver_status = str(m.groupdict()['nsr_initial_init_ver_status']).lower()
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'nsr_initial_initsync_version': nsr_initial_initsync_version})
                af_dict.update({'nsr_initial_init_ver_status': nsr_initial_init_ver_status})
                continue
            
            # BGP NSR/ISSU Sync-Group versions 0/0

            m = p12.match(line)
            if m:
                nsr_issu_sync_group_versions = m.groupdict()['nsr_issu_sync_group_versions']
                # Set af_dict
                af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
                af_dict.update({'nsr_issu_sync_group_versions': nsr_issu_sync_group_versions})
                continue
            
            # BGP scan interval 60 secs

            m = p13.match(line)
            if m:
               scan_interval = int(m.groupdict()['scan_interval'])
               # Set af_dict
               af_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf_name, {})\
                    .setdefault('address_family', {}).setdefault(address_family, {})
               af_dict.update({'scan_interval': scan_interval})
               continue
            
            # 0.0.0.0                                0 i
            m = p15.match(line)
            if m:
                group = m.groupdict()
                
                if prefix_dict:
                    
                    next_hop = group['next_hop']

                    prefix_dict.update({'next_hop': next_hop})
                    
                    # dealing with the group of metric, locprf, weight, path
                    group_num = group['number']

                    if group_num:
                        # metric   locprf  weight path
                        # 2219      211       0 200 33299 51178 47751 {27016}
                        m1 = re.compile(r'^(?P<metric>[0-9]+)  +'
                                    '(?P<locprf>[0-9]+)  +'
                                    '(?P<weight>[0-9]+) '
                                    '(?P<path>[0-9\{\}\s]+)$').match(group_num)
        
                        # metric   locprf  weight path
                        # 2219                0 200 33299 51178 47751 {27016}
                        # locprf   weight path
                        # 211         0 200 33299 51178 47751 {27016}
        
                        m2 = re.compile(r'^(?P<value>[0-9]+)'
                                    '(?P<space>\s{2,20})'
                                    '(?P<weight>[0-9]+) '
                                    '(?P<path>[0-9\{\}\s]+)$').match(group_num)
        
                        # weight path
                        # 0 200 33299 51178 47751 {27016}
                        m3 = re.compile(r'^(?P<weight>[0-9]+) '
                                    '(?P<path>((\d+\s)|(\{\d+\}\s))+)$')\
                                .match(group_num)
        
                        if m1:
                            prefix_dict['metric'] = m1.groupdict()['metric']
                            prefix_dict['localprf'] =  int(m1.groupdict()['locprf'])
                            prefix_dict['weight'] = int(m1.groupdict()['weight'])
                            prefix_dict['path'] = m1.groupdict()['path'].strip()
                        elif m2:
                            if len(m2.groupdict()['space']) > 8:
                                prefix_dict['metric'] = m2.groupdict()['value']
                            else:
                                prefix_dict['localprf'] = \
                                   int(m2.groupdict()['value'])
        
                            prefix_dict['weight'] = \
                                int(m2.groupdict()['weight'])
                            prefix_dict['path'] = \
                                m2.groupdict()['path'].strip()
                        elif m3:
                            prefix_dict['weight'] = \
                                int(m3.groupdict()['weight'])
                            prefix_dict['path'] = \
                                m3.groupdict()['path'].strip()

                    if m.groupdict()['origin_codes']:
                        prefix_dict['origin_codes'] = \
                            m.groupdict()['origin_codes']
                continue
            
            # Processed 40 prefixes, 50 paths
            m = p16.match(line)
            if m:
                processed_prefix = int(m.groupdict()['processed_prefix'])
                processed_paths = int(m.groupdict()['processed_paths'])
                af_dict['processed_prefix'] = processed_prefix
                af_dict['processed_paths'] = processed_paths
                continue
        return parsed_dict

# ===========================================
# Schema for 'show bgp l2vpn evpn advertised'
# ===========================================
class ShowBgpL2vpnEvpnAdvertisedSchema(MetaParser):
    '''Schema for:
        * 'show bgp l2vpn evpn advertised'
    '''

    schema = {
        'neighbor': 
            {Any():
                {'address_family':
                    {Any():
                        {'advertised':
                            {Any():
                                {'index':
                                    {Any():
                                        {'neighbor': str,
                                        'neighbor_router_id': str,
                                        'flags': list,
                                        'rx_path_id': int,
                                        'local_path_id': int,
                                        'version': int,
                                        'inbound_attributes':
                                            {'nexthop': str,
                                            'community_attributes': str,
                                            Optional('origin'): str,
                                            Optional('aspath'): str,
                                            Optional('community'): list,
                                            Optional('extended_community'): list,
                                            },
                                        'outbound_attributes':
                                            {'nexthop': str,
                                            'community_attributes': str,
                                            Optional('origin'): str,
                                            Optional('aspath'): str,
                                            Optional('community'): list,
                                            Optional('extended_community'): list,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===========================================
# Parser for 'show bgp l2vpn evpn advertised'
# ===========================================
class ShowBgpL2vpnEvpnAdvertised(ShowBgpL2vpnEvpnAdvertisedSchema):
    '''Parser for:
        * 'show bgp l2vpn evpn advertised'
    '''

    cli_command = 'show bgp l2vpn evpn advertised'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init
        parsed_dict = {}
        index = 1

        # Route Distinguisher: 10.196.7.7:3
        p1 = re.compile(r'^Route +Distinguisher: +(?P<rd>(\S+))$')

        # [2][0][48][7777.77ff.7779][0]/104 is advertised to 10.55.0.10
        # [1][0009.08ff.0d0c.0403.0201][0]/120 is advertised to 10.100.5.5
        p2 = re.compile(r'^(?P<prefix>\[[^/]+\])/(?P<prefix_length>(\d+)) +is'
                         ' +advertised +to +(?P<neighbor>(\S+))$')

        #  Path info:
        p3 = re.compile(r'^Path info:$')

        #    neighbor: Local           neighbor router id: 10.1.8.8
        #    neighbor: Local           neighbor router id: 10.196.7.7
        p4 = re.compile(r'^neighbor: +(?P<neighbor>(\S+)) +neighbor +router'
                         ' +id: +(?P<neighbor_router_id>(\S+))$')

        #    valid  redistributed  best  import-candidate
        p5 = re.compile(r'^(?P<flags>(valid.*))$')

        #    Received Path ID 0, Local Path ID 0, version 12
        p6 = re.compile(r'^Received +Path +ID +(?P<rx_path_id>(\d+)), +Local'
                         ' +Path +ID +(?P<local_path_id>(\d+)), +version'
                         ' (?P<version>(\d+))$')

        #  Attributes after inbound policy was applied:
        #  Attributes after outbound policy was applied:
        p7 = re.compile(r'^Attributes +after +(?P<type>(outbound|inbound))'
                         ' +policy +was +applied:$')

        #    next hop: 10.1.8.8
        p8 = re.compile(r'^next +hop:(?: +(?P<nexthop>(\S+)))?$')

        #    EXTCOMM
        #    ORG AS EXTCOMM
        p9 = re.compile(r'^(?P<community_attributes>(EXTCOMM|ORG AS EXTCOMM))$')

        #    origin: IGP  
        p10 = re.compile(r'^origin:(?: +(?P<origin>.*))?$')

        #    aspath: 
        p11 = re.compile(r'^aspath:(?: +(?P<aspath>.*))?$')

        #    community: no-export
        p12 = re.compile(r'^community:(?: +(?P<community>.*))?$')

        #    extended community: SoO:0.0.0.0:0 RT:100:7
        p13 = re.compile(r'^extended +community:(?: +(?P<extended_community>.*))?$')

        for line in out.splitlines():
            line = line.strip()

            # Route Distinguisher: 10.196.7.7:3
            m = p1.match(line)
            if m:
                af = 'l2vpn evpn RD ' + m.groupdict()['rd']
                continue

            # [2][0][48][7777.77ff.7779][0]/104 is advertised to 10.55.0.10
            # [1][0009.08ff.0d0c.0403.0201][0]/120 is advertised to 10.100.5.5
            m = p2.match(line)
            if m:
                group = m.groupdict()
                adv = group['prefix'] + "/" + group['prefix_length']
                adv_dict = parsed_dict.setdefault('neighbor', {}).\
                                        setdefault(group['neighbor'], {}).\
                                        setdefault('address_family', {}).\
                                        setdefault(af, {}).\
                                        setdefault('advertised', {}).\
                                        setdefault(adv, {}).\
                                        setdefault('index', {}).\
                                        setdefault(index, {})
                index += 1
                continue

            #  Path info:
            m = p3.match(line)
            if m:
                continue

            #    neighbor: Local           neighbor router id: 10.1.8.8
            #    neighbor: Local           neighbor router id: 10.196.7.7
            m = p4.match(line)
            if m:
                group = m.groupdict()
                adv_dict['neighbor'] = group['neighbor']
                adv_dict['neighbor_router_id'] = group['neighbor_router_id']
                continue

            #    valid  redistributed  best  import-candidate
            m = p5.match(line)
            if m:
                adv_dict['flags'] = m.groupdict()['flags'].split()
                continue

            # Received Path ID 0, Local Path ID 0, version 193217
            m = p6.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    adv_dict[key] = int(value)
                continue

            #  Attributes after inbound policy was applied:
            #  Attributes after outbound policy was applied:
            m = p7.match(line)
            if m:
                attr_dict = adv_dict.\
                            setdefault(m.groupdict()['type']+"_attributes", {})
                attr_dict['community_attributes'] = ""
                continue

            #    next hop: 10.1.8.8
            m = p8.match(line)
            if m:
                value = m.groupdict()['nexthop']
                attr_dict['nexthop'] = value if value != None else ""
                continue

            #    EXTCOMM
            #    ORG AS EXTCOMM
            m = p9.match(line)
            if m:
                attr_dict['community_attributes'] = m.groupdict()['community_attributes']
                continue

            #    origin: IGP
            m = p10.match(line)
            if m:
                value = m.groupdict()['origin']
                attr_dict['origin'] = value if value != None else ""
                continue

            #    aspath:
            m = p11.match(line)
            if m:
                value = m.groupdict()['aspath']
                attr_dict['aspath'] = value if value != None else ""
                continue

            #    community: no-export
            m = p12.match(line)
            if m:
                value = m.groupdict()['community']
                attr_dict['community'] = value.split() if value != None else []
                continue

            #    extended community: SoO:0.0.0.0:0 RT:100:7
            m = p13.match(line)
            if m:
                value = m.groupdict()['extended_community']
                attr_dict['extended_community'] = value.split() if value != None else []
                continue

        return parsed_dict


class ShowBgpL2vpnEvpnNeighbors(ShowBgpInstanceNeighborsDetail):

    """Parser for show bgp l2vpn evpn neighbors
                  show bgp l2vpn evpn neighbors <neighbor>
    """

    cli_command = ['show bgp l2vpn evpn neighbors', 'show bgp l2vpn evpn neighbors {neighbor}']

    def cli(self, neighbor='', output=None):
        if output is None:
            if neighbor:
                out = self.device.execute(self.cli_command[1].format(neighbor=neighbor))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        result_dict = super().cli(output=out)

        return result_dict


class ShowBgpNeighbors(ShowBgpInstanceNeighborsDetail):

    """Parser for show bgp neighbors
                  show bgp neighbors {neighbor}
                  show bgp vrf {vrf} neighbors
                  show bgp vrf {vrf} neighbors {neighbor}
                  show bgp {address_family} neighbors
                  show bgp {address_family} neighbors {neighbor}
                  show bgp vrf {vrf} {address_family} neighbors
                  show bgp vrf {vrf} {address_family} neighbors {neighbor}
    """

    cli_command = ['show bgp neighbors',
                   'show bgp neighbors {neighbor}',
                   'show bgp vrf {vrf} neighbors',
                   'show bgp vrf {vrf} neighbors {neighbor}',
                   'show bgp {address_family} neighbors',
                   'show bgp {address_family} neighbors {neighbor}',
                   'show bgp vrf {vrf} {address_family} neighbors',
                   'show bgp vrf {vrf} {address_family} neighbors {neighbor}']

    def cli(self, neighbor='', vrf='', address_family='', output=None):

        if neighbor:
            if vrf and address_family:
                cmd = self.cli_command[7].format(vrf=vrf, address_family=address_family,
                                                 neighbor=neighbor)
            elif address_family:
                cmd = self.cli_command[5].format(address_family=address_family,
                                                 neighbor=neighbor)
            elif vrf:
                cmd = self.cli_command[3].format(vrf=vrf, neighbor=neighbor)
            else:
                cmd = self.cli_command[1].format(neighbor=neighbor)
        else:
            if vrf and address_family:
                cmd = self.cli_command[6].format(vrf=vrf, address_family=address_family)
            elif address_family:
                cmd = self.cli_command[4].format(address_family=address_family)
            elif vrf:
                cmd = self.cli_command[2].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

        out = output or self.device.execute(cmd)

        return super().cli(output=out)


class ShowBgpSummary(ShowBgpInstanceSummary):

    ''' Parser for:
        * 'show bgp summary'
        * 'show bgp {address_family} summary'
    '''

    cli_command = ['show bgp {address_family} summary',
                   'show bgp summary']

    def cli(self, address_family='', output=None):

        if address_family:
            cmd = self.cli_command[0].format(address_family=address_family)
        else:
            cmd = self.cli_command[1]

        out = output or self.device.execute(cmd)
        if not address_family:
            address_family = 'ipv4 unicast'

        # Call super
        return super().cli(output=out, address_family=address_family)

# vim: ft=python ts=8 sw=4 et


# ===========================================
# Schema for 'show bgp nexthops {ipaddress}'
# ===========================================
class ShowBgpNexthopsSchema(MetaParser):
    '''Schema for:
        * 'show bgp nexthops {ipaddress}'
    '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'nexthop': {
                            Any(): {
                                'nexthop_id': str,
                                'version': str,
                                'nexthop_flags': str,
                                'nexthop_handle': str,
                                'rib_related_information': {
                                    'first_interface_handle': {
                                        Any(): {
                                            'gateway_tbl_id': str,
                                            'gateway_flags': str,
                                            'gateway_handle': str,
                                            'gateway': str,
                                            'resolving_route': str,
                                            'paths': int,
                                            'rib_nexthop_id': str,
                                            'status': str,
                                            'metric': int,
                                            'registration': str,
                                            'completed': str,
                                            'events': str,
                                            'last_received': str,
                                            'last_gw_update': str,
                                            'reference_count': int,
                                        },
                                    }
                                },
                                'prefix_related_information': {
                                    'active_tables': str,
                                    'metrics': str,
                                    'reference_counts': int,
                                },
                                'interface_handle': str,
                                'attr_ref_count': int,
                            }
                        }
                    }
                }
            }
        }
    }


# ===========================================
# Parser for 'show bgp nexthops {ipaddress}'
# ===========================================
class ShowBgpNexthops(ShowBgpNexthopsSchema):
    '''Parser for:
        * 'show bgp nexthops {ipaddress}'
    '''

    cli_command = ['show bgp nexthops {ipaddress}']

    def cli(self, ipaddress, output=None):

        if output is None:
            if ipaddress:
                out = self.device.execute(self.cli_command[0].format(ipaddress=ipaddress))
        else:
            out = output

        # Initialize dictionaries
        ret_dict = {}
        ipaddress_dict = {}
        nexthop_address_dict = {}
        nexthop_dict = {}        


        # VRF: default
        p1 = re.compile(r'^VRF:\s+(?P<vrf>([\w]+))$')

        # Nexthop ID: 0x6000074, Version: 0x0
        p2 = re.compile(r'^Nexthop ID:\s+(?P<nexthop_id>([\w]+)),\s+Version:\s+((?P<version>[\w]+))$')

        # Nexthop Flags: 0x00000000
        p3 = re.compile(r'^Nexthop Flags:\s+((?P<nexthop_flags>[\w]+))$')

        # Nexthop Handle: 0x7fba00aafccc
        p4 = re.compile(r'^Nexthop Handle:\s+((?P<nexthop_handle>[\w]+))$')

        # Firsthop interface handle 0x0c001cc0
        p5 = re.compile(r'^Firsthop interface handle\s+((?P<first_interface_handle>[\w]+))$')

        # Gateway TBL Id: 0xe0000000    Gateway Flags: 0x00000080
        p6 = re.compile(r'^Gateway TBL Id:\s+((?P<gateway_tbl_id>[\w]+)\s+)Gateway Flags:\s+((?P<gateway_flags>[\w]+))$')

        # Gateway Handle: 0x7fba14059ce0
        p7 = re.compile(r'^Gateway Handle:\s+((?P<gateway_handle>[\w]+))$')

        # Gateway: reachable, non-Connected route, prefix length 32
        p8 = re.compile(r'^Gateway:\s+((?P<gateway>[\s\S]+))$')

        # Resolving Route: 10.4.16.16/32 (static)
        p9 = re.compile(r'^Resolving Route:\s+((?P<resolving_route>[\s\S]+))$')        

        # Paths: 0
        p10 = re.compile(r'^Paths:\s+((?P<paths>[\d]+)\s*)$')

        # RIB Nexhop ID: 0x0
        p11 = re.compile(r'^RIB Nexhop ID:\s+((?P<rib_nexthop_id>[\w]+))$')

        # Status: [Reachable][Not Connected][Not Local]
        p12 = re.compile(r'^Status:\s+((?P<status>[\s\S]+))$')

        # Metric: 0
        p13 = re.compile(r'^Metric:\s+((?P<metric>[\d]+))$')

        # Registration: Asynchronous, Completed: 00:02:15
        p14 = re.compile(r'^Registration:\s+(?P<registration>[\w]+),\s+Completed:\s+((?P<completed>[\w\:]+))$')

        # Events: Critical (1)/Non-critical (0)
        p15 = re.compile(r'^Events:\s+((?P<events>[\s\S]+))$')

        # Last Received: 00:02:14 (Critical)
        p16 = re.compile(r'^Last Received:\s+((?P<last_received>[\s\S]+))$')

        # Last gw update: (Crit-notif) 00:02:14(rib)
        p17 = re.compile(r'^Last gw update:\s+((?P<last_gw_update>[\s\S]+))$')

        # Reference Count: 1
        p18 = re.compile(r'^Reference Count:\s+((?P<reference_count>[\d]+))$')

        # Active Tables: [IPv4 Unicast]
        p19 = re.compile(r'^Active Tables:\s+((?P<active_tables>[\s\S]+))$')

        # Metrices: [0x0]
        p20 = re.compile(r'^Metrices:\s+((?P<metrics>[\s\S]+))$')

        # Reference Counts: [1]
        p21 = re.compile(r'^Reference Counts:\s+(\[(?P<reference_counts>[\d]+)\])$')

        # Interface Handle: 0x0
        p22 = re.compile(r'^Interface Handle:\s+((?P<interface_handle>[\w]+))$')                        

        # Attr ref-count: 4
        p23 = re.compile(r'^Attr ref-count:\s+((?P<attr_ref_count>[\d]+))$')
        
        for line in out.splitlines():
            line = line.strip()
                
            # VRF: default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']

                #define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {})
                
                #define def_dict dictionary and assigned to vrf_dict
                def_dict = vrf_dict.setdefault(vrf,{})

                #define af_dict dictionary and set to 'address_family'
                af_dict = def_dict.setdefault('address_family',{})                
                continue
            
            # Nexthop ID: 0x6000074, Version: 0x0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                #update nexthop_address_dict               
                nexthop_address_dict.update({'nexthop_id': group['nexthop_id']})
                nexthop_address_dict.update({'version': group['version']})
                continue

            # Nexthop Flags: 0x00000000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                #update nexthop_address_dict
                nexthop_address_dict.update({'nexthop_flags': group['nexthop_flags']})
                continue

            # Nexthop Handle: 0x7fba00aafccc
            m = p4.match(line)
            if m:
                group = m.groupdict()
                nexthop_address_dict.update({'nexthop_handle': group['nexthop_handle']})  
                rib_related_dict = nexthop_address_dict.setdefault('rib_related_information',{})
                continue

            # Firsthop interface handle 0x0c001cc0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                #set first_interface_handle_dict
                first_interface_handle = group['first_interface_handle']
                first_interface_handle_dict = rib_related_dict.setdefault('first_interface_handle',{})\
                                                                .setdefault(first_interface_handle,{})                                                                             
                continue            

            # Gateway TBL Id: 0xe0000000    Gateway Flags: 0x00000080
            m = p6.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'gateway_tbl_id':group['gateway_tbl_id']})
                first_interface_handle_dict.update({'gateway_flags':group['gateway_flags']})
                continue
            
            # Gateway Handle: 0x7fba14059ce0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'gateway_handle':group['gateway_handle']})
                continue 
            
            # Gateway: reachable, non-Connected route, prefix length 32
            m = p8.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'gateway':group['gateway']})
                continue         
            
            # Resolving Route: 10.4.16.16/32 (static)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'resolving_route':group['resolving_route']})
                continue 

            # Paths: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'paths':int(group['paths'])}) 
                continue       

            # RIB Nexhop ID: 0x0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'rib_nexthop_id':group['rib_nexthop_id']})
                continue 
            
            # Status: [Reachable][Not Connected][Not Local]
            m = p12.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'status':group['status']})
                continue         
            
            # Metric: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'metric':int(group['metric'])})
                continue                      

            # Registration: Asynchronous, Completed: 00:02:15
            m = p14.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'registration':group['registration']})
                first_interface_handle_dict.update({'completed':group['completed']})
                continue   

            # Events: Critical (1)/Non-critical (0)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'events':group['events']})
                continue   

            # Last Received: 00:02:14 (Critical)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'last_received':group['last_received']})
                continue   

            # Last gw update: (Crit-notif) 00:02:14(rib)
            m = p17.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'last_gw_update':group['last_gw_update']})
                continue                                      

            # Reference Count: 1
            m = p18.match(line)
            if m:
                group = m.groupdict()
                #update first_interface_handle_dict
                first_interface_handle_dict.update({'reference_count':int(group['reference_count'])})                
                continue      

            # Active Tables: [IPv4 Unicast]
            m = p19.match(line)
            if m:
                group = m.groupdict()
                #set prefix_related_dict
                prefix_related_dict = nexthop_address_dict.setdefault('prefix_related_information',{}) 
                #remove [] from [IPv4]
                active_tables = group['active_tables'].replace('[','').replace(']','')
                #update prefix_related_dict
                prefix_related_dict.update({'active_tables':active_tables})
                
                #update top ipaddress_dict with child nexthop_address_dict dictionary
                ipaddress_dict.update({ipaddress:nexthop_address_dict})

                #update top nexthop_dict with child ipaddress_dict dictionary
                nexthop_dict.update({'nexthop':ipaddress_dict})

                #update top af_dict with child nexthop_dict dictionary
                af_dict.update({active_tables:nexthop_dict})
                continue  

            # Metrices: [0x0]
            m = p20.match(line)
            if m:
                group = m.groupdict()
                metrics = group['metrics'].replace('[','').replace(']','')
                #update prefix_related_dict
                prefix_related_dict.update({'metrics':metrics})
                continue 

            # Reference Counts: [1]
            m = p21.match(line)
            if m:
                group = m.groupdict()
                #update prefix_related_dict
                prefix_related_dict.update({'reference_counts':int(group['reference_counts'])})
                continue   

            # Interface Handle: 0x0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                #update nexthop_address_dict
                nexthop_address_dict.update({'interface_handle': group['interface_handle']})
                continue   

            # Attr ref-count: 4
            m = p23.match(line)
            if m:
                group = m.groupdict()
                #update nexthop_address_dict
                nexthop_address_dict.update({'attr_ref_count': int(group['attr_ref_count'])})  
                continue  

        return ret_dict


# ===========================================
# Schema for 'show bgp all all nexthops'
# ===========================================
class ShowBgpAllAllNexthopsSchema(MetaParser):
    '''Schema for:
        * 'show bgp all all nexthops'
    '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('total_next_hop'):{
                            'time_spent_secs': float
                        },
                        Optional('maximum_next_hop'): {
                            'received': str,
                            'best_paths_deleted': int,
                            'best_paths_changed': int,
                            'time_spent_secs': float
                        },
                        Optional('last_notification'): {
                            'received': str,
                            'time_spent_secs': float
                        },
                        Optional('gateway_address_family'): str,
                        Optional('table_id'): str,
                        Optional('next_hop_count'): int,
                        Optional('critical_trigger_delay'): str,
                        Optional('non_critical_trigger_delay'): str,
                        Optional('next_hop_version'):int,
                        Optional('rib_version'):int,
                        Optional('epe_table_version'): int,
                        Optional('epe_label_version'): int,
                        Optional('epe_downloaded_version'): int,
                        Optional('epe_standby_version'): int,
                        Optional('next_hops'):{
                            Any():{
                                'status': ListOf(str),
                                'metric': int,
                                'tbl_id': str,
                                'notf': str,
                                'last_rib_event': str,
                                'ref_count': str
                            }
                        }
                    }
                }
            }
        }
    }


# ===========================================
# Parser for 'show bgp all all nexthops'
# ===========================================
class ShowBgpAllAllNexthops(ShowBgpAllAllNexthopsSchema):
    '''Parser for:
        * 'show bgp all all nexthops'
    '''

    cli_command = ['show bgp all all nexthops']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Initialize dictionaries
        ret_dict = {}

        # reference dict
        ref_dict = {}

        # Address Family: VPNv4 Unicast
        p1 =  re.compile(r'^Address +Family: +(?P<address_family>[\S\s]+)$')

        # Total Nexthop Processing
        p2 = re.compile(r'^Total +Nexthop +Processing$')

        # Maximum Nexthop Processing
        p3 = re.compile(r'^Maximum +Nexthop +Processing$')

        # Last Notification Processing
        p4 = re.compile(r'^Last +Notification +Processing$')

        # Time Spent: 0.000 secs
        p5 = re.compile(r'^Time +Spent: +(?P<time_spent_secs>[\d\.]+) secs$')

        # Received: 00:00:00
        p6 = re.compile(r'^Received: +(?P<received>.+)$')

        # Bestpaths Deleted: 0
        p7 = re.compile(r'^Bestpaths +Deleted: +(?P<best_paths_deleted>[\S\s]+)$')

        # Bestpaths Changed: 0
        p8 = re.compile(r'^Bestpaths +Changed: +(?P<best_paths_changed>[\S\s]+)$')

        # Gateway Address Family: IPv4 Unicast
        p9 = re.compile(r'^Gateway +Address +Family: +(?P<gateway_address_family>[\S\s]+)$')

        # Table ID: 0xe0000000
        p10 = re.compile(r'^Table +ID: +(?P<table_id>[\S\s]+)$')

        # Nexthop Count: 2
        p11 = re.compile(r'^Nexthop +Count: +(?P<next_hop_count>[\S\s]+)$')

        # Critical Trigger Delay: 0msec
        p12 = re.compile(r'^Critical +Trigger +Delay: +(?P<critical_trigger_delay>[\S\s]+)$')

        # Non-critical Trigger Delay: 10000msec
        p13 = re.compile(r'^Non-critical +Trigger +Delay: +(?P<non_critical_trigger_delay>[\S\s]+)$')

        # Nexthop Version: 1, RIB version: 1
        p14 = re.compile(r'^Nexthop +Version: +(?P<next_hop_version>[\d]+), +RIB +version:'
                         r' +(?P<rib_version>\d+)$')

        # EPE Table Version: 1, EPE Label version: 1
        p15 = re.compile(r'^EPE +Table +Version: +(?P<epe_table_version>[\d]+), +EPE +Label '
                         r'+version: +(?P<epe_label_version>[\d]+)$')

        # EPE Downloaded Version: 1, EPE Standby Version: 1
        p16 = re.compile(r'^EPE +Downloaded +Version: +(?P<epe_downloaded_version>[\d]+), '
                         r'+EPE +Standby +Version: +(?P<epe_standby_version>[\d]+)$')

        # 108.10.10.1     [R][NC][NL]          2   e0000000   1/0    00:13:49 (Cri)        1/4
        p17 = re.compile('^(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<status>[\S]+)\s+'
                         '(?P<metric>\d+)\s+(?P<tbl_id>\S+)\s+(?P<notf>\S+)\s+(?P<last_rib_event>\S+'
                         '\s\(\w+\))\s+(?P<ref_count>\S+)$')

        # 2000:108:10:10::1
        p18 = re.compile(r'^(?P<next_hop_ipv6>[a-fA-F\d\:]+)$')

        # [R][NC][NL]          1   e0800000   1/0    00:12:06 (Cri)        0/3
        p19 = re.compile(r'^(?P<status>[\S]+)\s+(?P<metric>\d+)\s+(?P<tbl_id>\S+)\s+(?P<notf>\S+)\s+'
                         r'(?P<last_rib_event>\S+\s\(\w+\))\s+(?P<ref_count>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Address Family: VPNv4 Unicast
            m = p1.match(line)
            if m:
                group = m.groupdict()
                address_family = group['address_family']

                # define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {})

                # define def_dict dictionary and assigned to vrf_dict
                def_dict = vrf_dict.setdefault('default', {})

                # define af_dict dictionary and set to 'address_family'
                af_dict = def_dict.setdefault('address_family', {})\
                          .setdefault(address_family, {})
                continue

            # Total Nexthop Processing
            m = p2.match(line)
            if m:
                ref_dict = af_dict.setdefault('total_next_hop', {})

            # Maximum Nexthop Processing
            m = p3.match(line)
            if m:
                ref_dict = af_dict.setdefault('maximum_next_hop', {})

            # Last Notification Processing
            m = p4.match(line)
            if m:
                ref_dict = af_dict.setdefault('last_notification', {})

            # Time Spent: 0.000 secs
            m = p5.match(line)
            if m:
                group = m.groupdict()
                time_spent_secs = float(group['time_spent_secs'])
                ref_dict.update({'time_spent_secs':time_spent_secs})
                continue

            # Received: 00:00:00
            m = p6.match(line)
            if m:
                group = m.groupdict()
                received = group['received']
                ref_dict.update({'received' : received})
                continue

            # Bestpaths Deleted: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                best_path_deleted = int(group['best_paths_deleted'])
                af_dict['maximum_next_hop']['best_paths_deleted'] = best_path_deleted
                continue

            # Bestpaths Changed: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                best_path_changed = int(group['best_paths_changed'])
                af_dict['maximum_next_hop']['best_paths_changed'] =  best_path_changed
                continue

            # Gateway Address Family: IPv4 Unicast
            m = p9.match(line)
            if m:
                group = m.groupdict()
                gateway_address_family = group['gateway_address_family']
                af_dict.setdefault('gateway_address_family', gateway_address_family)
                continue

            # Table ID: 0xe0000000
            m = p10.match(line)
            if m:
                group = m.groupdict()
                table_id = group['table_id']
                af_dict.setdefault('table_id', table_id)
                continue

            # Nexthop Count: 2
            m = p11.match(line)
            if m:
                group = m.groupdict()
                next_hop_count = int(group['next_hop_count'])
                af_dict.setdefault('next_hop_count', next_hop_count)
                continue

            # Critical Trigger Delay: 0msec
            m = p12.match(line)
            if m:
                group = m.groupdict()
                critical_trigger_delay = group['critical_trigger_delay']
                af_dict.setdefault('critical_trigger_delay', critical_trigger_delay)
                continue

            # Non-critical Trigger Delay: 10000msec
            m = p13.match(line)
            if m:
                group = m.groupdict()
                non_critical_trigger_delay = group['non_critical_trigger_delay']
                af_dict.setdefault('non_critical_trigger_delay', non_critical_trigger_delay)
                continue

            # Nexthop Version: 1, RIB version: 1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                next_hop_version = int(group['next_hop_version'])
                rib_version = int(group['rib_version'])
                af_dict.update({
                    'next_hop_version': next_hop_version,
                    'rib_version': rib_version
                })
                continue

            # EPE Table Version: 1, EPE Label version: 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                epe_table_version = int(group['epe_table_version'])
                epe_label_version = int(group['epe_label_version'])
                af_dict.update({
                    'epe_table_version': epe_table_version,
                    'epe_label_version': epe_label_version
                })
                continue

            # EPE Downloaded Version: 1, EPE Standby Version: 1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                epe_downloaded_version = int(group['epe_downloaded_version'])
                epe_standby_version = int(group['epe_standby_version'])
                af_dict.update({
                    'epe_downloaded_version': epe_downloaded_version,
                    'epe_standby_version': epe_standby_version
                })
                continue

            # 108.10.10.1     [R][NC][NL]          2   e0000000   1/0    00:13:49 (Cri)        1/4
            m = p17.match(line)
            if m:
                group = m.groupdict()
                next_hop = group['next_hop']
                status_dict = af_dict.setdefault('next_hops', {}).setdefault(next_hop, {})
                status_dict.update({
                    'status' : group['status'].replace("[", "").split("]")[:-1],
                    'metric' :  int(group['metric']),
                    'tbl_id' : group['tbl_id'],
                    'notf' : group['notf'],
                    'last_rib_event' : group['last_rib_event'],
                    'ref_count' : group['ref_count']
                })
                continue

            # 2000:108:10:10::1
            m = p18.match(line)
            if m:
                group = m.groupdict()
                next_hop_ipv6 = group['next_hop_ipv6']
                status_dict = af_dict.setdefault('next_hops', {}).setdefault(next_hop_ipv6, {})
                continue

            # [R][NC][NL]          1   e0800000   1/0    00:12:06 (Cri)        0/3
            m = p19.match(line)
            if m:
                group = m.groupdict()
                status_dict.update({
                    'status': group['status'].replace("[", "").split("]")[:-1],
                    'metric': int(group['metric']),
                    'tbl_id': group['tbl_id'],
                    'notf': group['notf'],
                    'last_rib_event': group['last_rib_event'],
                    'ref_count': group['ref_count']
                })
                continue

        return ret_dict


# ==========================================================
# Schema for 'show bgp {address_family} {ip_address} brief'
# ==========================================================
class ShowBgpBriefSchema(MetaParser):
    '''Schema for:
        * 'show bgp {address_family} {ip_address} brief'
    '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'network': {
                            Any(): {
                                'next_hops': {
                                    Any(): {
                                        'metric': int,
                                        'locprf': int,
                                        'weight': int,
                                        'path': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# ==========================================================
# Parser for 'show bgp {address_family} {ip_address} brief'
# ==========================================================
class ShowBgpBrief(ShowBgpBriefSchema):
    '''Parser for:
        * 'show bgp {address_family} {ip_address} brief'
    '''

    cli_command = ['show bgp {address_family} {ip_address} brief']

    def cli(self, address_family, ip_address, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0].\
                                      format(address_family=address_family,\
                                      ip_address=ip_address))
        else:
            out = output

        # Initialize dictionaries
        ret_dict = {}

        # *> 111.111.111.111/32 108.10.0.2               0           100 65401 i
        # *                     108.11.0.2               0             0 65401 i
        p1 = re.compile('^.*\s(?P<next_hop>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
                        '(?P<metric>\d+)\s+(?P<locprf>\d+)\s+(?P<weight>\d+)\s+'
                        '(?P<path>\D)$')

        for line in out.splitlines():
            line = line.strip()

            # *> 111.111.111.111/32 108.10.0.2               0           100 65401 i
            # *                     108.11.0.2               0             0 65401 i
            m = p1.match(line)
            if m:
                # define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {})

                # define def_dict dictionary and assigned to vrf_dict
                def_dict = vrf_dict.setdefault('default', {})

                # define af_dict dictionary and set to 'address_family'
                af_dict = def_dict.setdefault('address_family', {}) \
                          .setdefault(address_family, {})

                # define net_dict and assigned to af_dict dictionary
                net_dict = af_dict.setdefault('network', {}) \
                           .setdefault(ip_address, {})

                group = m.groupdict()
                next_hop = group['next_hop']

                # define next_hops_dict and assigned to net_dict dictionary
                next_hops_dict = net_dict.setdefault('next_hops', {}) \
                                 .setdefault(next_hop, {})

                next_hops_dict.update({
                    'metric': int(group['metric']),
                    'locprf': int(group['locprf']),
                    'weight': int(group['weight']),
                    'path': group['path']
                })
                continue

        return ret_dict



# ======================================================================
# Schema for 'show bgp {address_family} {ip_address} bestpath-compare'
# ======================================================================
class ShowBgpBestpathCompareSchema(MetaParser):
    '''Schema for:
        * 'show bgp {address_family} {ip_address} bestpath-compare'
    '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'network': {
                            Any(): {
                                Optional('versions'): {
                                    Optional('process'):{
                                        Optional(Any()):{
                                            Optional('brib/rib'): int,
                                            Optional('send_tbl_ver'): int,
                                        }
                                    },
                                },
                                Optional('last_modified'): str,
                                Optional('available_paths'): int,
                                Optional('best_path'): int,
                                Optional('paths'): {
                                    Optional(Any()):{
                                        Optional('paths_to_update_groups'): ListOf(str),
                                        Optional('next_hop'): str,
                                        Optional('gateway'): str,
                                        Optional('originator'): str,
                                        Optional('metric'): int,
                                        Optional('localpref'): int,
                                        Optional('weight'): int,
                                        Optional('status_codes'): str,
                                        Optional('origin_codes'): str,
                                        Optional('received_path_id'): int,
                                        Optional('local_path_id'): int,
                                        Optional('version'): int,
                                        Optional('origin_as_validity'): str
                                    }
                                },
                            }
                        }
                    }
                }
            }
        }
    }

# ======================================================================
# Parser for 'show bgp {address_family} {ip_address} bestpath-compare'
# ======================================================================
class ShowBgpBestpathCompare(ShowBgpBestpathCompareSchema):
    '''Parser for:
        * 'show bgp {address_family} {ip_address} bestpath-compare'
    '''

    cli_command = ['show bgp {address_family} {ip_address} bestpath-compare']

    def cli(self, address_family, ip_address, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0].\
                                      format(address_family=address_family,\
                                             ip_address=ip_address))
        else:
            out = output

        # Initialize dictionary
        ret_dict = {}
        next_line_update_group = False

        # Speaker                  5           5
        p1 = re.compile('^(?P<process>\w+)\s+(?P<brib_rib>\d+)\s+(?P<send_tbl_ver>\d+)$')

        # Last Modified: Mar  9 02:23:41.504 for 00:00:35
        p2 = re.compile('^Last +Modified: (?P<last_modified>.*)$')

        # Paths: (2 available, best #1)
        p3 = re.compile('^Paths: +\((?P<available_paths>\d+) +available\, '
                        '+best +\#(?P<best_path>\d+)\)$')

        # Path #1: Received by speaker 0
        p4 = re.compile('^Path+ #(?P<path_num>\d+).*$')

        # Advertised IPv4 Unicast paths to update-groups (with more than one peer):
        p5 = re.compile('^.*(?P<group2>update-groups).*$')

        # Not advertised to any peer
        p6 = re.compile(r'^Not +advertised +to +any +peer$')

        # 0.1 0.3
        p7 = re.compile('^(?P<group1>[\d\.]+)(?: +(?P<group2>[\d\.]+))$')

        # 108.10.0.2 from 108.10.0.2 (192.68.33.108)
        p8 = re.compile('^((?P<next_hop>[0-9\.]+)+ from +(?P<gateway>[0-9\.]+) '
                        '+\((?P<originator>[0-9\.]+)\))$')

        # Origin IGP, metric 0, localpref 100, weight 100, valid, external, best, group-best
        p9 = re.compile('^Origin +(?P<origin>[a-zA-Z]+),(?: '
                        '+metric (?P<metric>[0-9]+),?)?(?: '
                        '+localpref (?P<localpref>[0-9]+),?)?(?: '
                        '+weight (?P<weight>[0-9]+),?)?(?: '
                        '+(?P<valid>valid?,))?(?: '
                        '+(?P<state>(internal|external|local)\,?))?(\,)?(?: '
                        '(?P<best>best))?(\,)?(?: (?P<group_best>group-best))?$')

        #  Received Path ID 0, Local Path ID 0, version 0
        p10 = re.compile('^Received Path ID (?P<received_path_id>(\d+)), Local Path ID '
                        '(?P<local_path_id>(\d+)), version (?P<version>(\d+))$')

        # Origin-AS validity: (disabled)
        p11 = re.compile('^Origin-AS validity: \((?P<origin_as_validity>\w+)\)$')

        for line in out.splitlines():
            line = line.strip()

            #  Speaker                  5           5
            m = p1.match(line)
            if m:
                # define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {})

                # define def_dict dictionary and assigned to vrf_dict
                def_dict = vrf_dict.setdefault('default', {})

                # define af_dict dictionary and set to 'address_family'
                af_dict = def_dict.setdefault('address_family', {}) \
                          .setdefault(address_family, {})

                # define net_dict and assigned to af_dict dictionary
                net_dict = af_dict.setdefault('network', {}) \
                           .setdefault(ip_address, {})

                group = m.groupdict()
                process = group['process']

                # define ver_dict and assigned to net_dict dictionary
                ver_dict = net_dict.setdefault('versions', {})

                # define process_dict and assigned to ver_dict dictionary
                process_dict = ver_dict.setdefault('process', {}).\
                                        setdefault(process, {})

                process_dict.update({
                    'brib/rib': int(group['brib_rib']),
                    'send_tbl_ver': int(group['send_tbl_ver'])
                })
                continue

            # Last Modified: Mar  9 02:23:41.504 for 00:00:35
            m = p2.match(line)
            if m:
                group = m.groupdict()
                net_dict.update({'last_modified': group['last_modified']})
                continue

            # Paths: (2 available, best #1)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                net_dict.update({
                    'available_paths': int(group['available_paths']),
                    'best_path': int(group['best_path'])
                })
                #Initialize paths_dict
                paths_dict = net_dict.setdefault('paths', {})
                continue

            # Path #1: Received by speaker 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path = int(group['path_num'])
                each_path_dict = paths_dict.setdefault(path,{})
                continue

            #  Advertised IPv4 Unicast paths to update-groups (with more than one peer):
            m = p5.match(line)
            if m:
                next_line_update_group = True
                continue

            # Not advertised to any peer
            m = p6.match(line)
            if m:
                next_line_update_group = False
                continue

            # 0.1 0.3
            m = p7.match(line)
            if m and next_line_update_group:
                group = m.group()
                update_group = group.split(" ")
                next_line_update_group = False

                try:
                    if update_group:
                        each_path_dict['paths_to_update_groups'] = update_group
                except Exception:
                    pass
                continue

            #  108.10.0.2 from 108.10.0.2 (192.68.33.108)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                each_path_dict.update({
                    'next_hop': group['next_hop'],
                    'gateway': group['gateway'],
                    'originator': group['originator']
                })
                continue

            # Origin IGP, metric 0, localpref 100, valid, external
            # Origin IGP, metric 0, localpref 100, weight 100, valid, external, best, group-best
            m = p9.match(line)
            if m:
                group = m.groupdict()
                status_codes = ''
                if group['metric']:
                    each_path_dict['metric'] = int(group['metric'])
                if group['localpref']:
                    each_path_dict['localpref'] = int(group['localpref'])
                if group['weight']:
                    each_path_dict['weight'] = int(group['weight'])

                if group['origin']:
                    origin = str(group['origin'])
                    if origin == 'incomplete':
                        each_path_dict['origin_codes'] = '?'
                    elif origin == 'EGP':
                        each_path_dict['origin_codes'] = 'e'
                    else:
                        each_path_dict['origin_codes'] = 'i'

                if group['valid']:
                    status_codes += '*'
                if group['best']:
                    status_codes = status_codes.rstrip()
                    status_codes += '>'
                if group['state']:
                    state = group['state']
                    if state == 'internal':
                        status_codes += 'i'
                each_path_dict['status_codes'] = status_codes
                continue

            # Received Path ID 0, Local Path ID 0, version 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                each_path_dict.update({
                    'received_path_id': int(group['received_path_id']),
                    'local_path_id': int(group['local_path_id']),
                    'version': int(group['version'])
                })
                continue

            # Origin-AS validity: (disabled)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                each_path_dict.update({
                    'origin_as_validity': group['origin_as_validity']
                })
                continue
        return ret_dict
