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

    * 'show bgp sessions'
    * 'show bgp vrf-db vrf all'
    * 'show bgp l2vpn evpn'
    * 'show bgp l2vpn evpn advertised'

"""

# Python
import re
import logging
import collections
from ipaddress import ip_address, ip_network

# Metaparser
from genie.libs.parser.base import *
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# Parser
from genie.libs.parser.yang.bgp_openconfig_yang import BgpOpenconfigYang

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# =======================================
# Parser for 'show bgp instances'
# =======================================

class ShowBgpInstancesSchema(MetaParser):

    """Schema for show bgp instances"""

    schema = {
        'instance':
            {Any():
                {'bgp_id': int,
                 'instance_id': int,
                 'placed_grp': str,
                 'num_vrfs': int,
                 Optional('address_families'): list
                }
            },
        }

class ShowBgpInstances(ShowBgpInstancesSchema):

    """Parser for show bgp instances"""

    def cli(self):

        out = self.device.execute('show bgp instances')
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ID  Placed-Grp  Name              AS        VRFs    Address Families
            # --------------------------------------------------------------------------------
            # 0   v4_routing  test              333       0       none
            # 1   bgp2_1      test1             333       0       none
            # 2   bgp3_1      test2             333       0       none
            # 3   bgp4_1      default           100       2       IPv4 Unicast, VPNv4 Unicast,
            p1 = re.compile(r'^(?P<instance_id>\d+)'
                             ' +(?P<placed_grp>[\w\-]+)'
                             ' +(?P<instance>[\w\-]+)'
                             ' +(?P<bgp_id>\d+)'
                             ' +(?P<num_vrfs>\d+)'
                             ' +(?P<address_family>[\w\s\,\-]+)$')
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
                    ret_dict['instance'][instance]['bgp_id'] = int(bgp_id)
                if num_vrfs:
                    ret_dict['instance'][instance]['num_vrfs'] = int(num_vrfs)

                if address_family and address_family != 'none':
                    address_family_lst = address_family.strip(',').split(',')
                    address_family_lst = [item.strip() for item in address_family_lst]

                    ret_dict['instance'][instance]['address_families'] = address_family_lst

                ret_dict['instance'][instance]['placed_grp'] = placed_grp

                continue

            #                                                     IPv6 Unicast, VPNv6 Unicast
            p2 = re.compile(r'^(?P<address_family>[\w\s\,]+)$')
            m = p2.match(line)
            if m:
                address_family_extra_line = m.groupdict()['address_family'].lower()

                if address_family_extra_line and address_family_extra_line != 'none':
                    address_family_extra_line = address_family_extra_line.strip(',').split(',')
                    address_family_extra_line = [item.strip() for item in address_family_extra_line]
                    address_family_lst.extend(address_family_extra_line)
                    ret_dict['instance'][instance]['address_families'] = address_family_lst
    
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

    def cli(self):

        out = self.device.execute('show placement program all')
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # schema_server                           central-services    1177 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING
            # rcp_fs                                  central-services    1168 0/0/CPU0       RUNNING                  NONE           NOT_SPAWNED
            # bgp(test)                               Group_10_bgp2       1052 0/RSP1/CPU0    RUNNING                  0/RSP0/CPU0    RUNNING
            p1 = re.compile(r'^\s*(?P<program>[a-zA_Z0-9\_\-]+)'
                             '(?:\((?P<instance>\S+)\))?'
                             ' +(?P<group>\S+)'
                             ' +(?P<jid>\S+)'
                             ' +(?P<active_rp>\S+)'
                             ' +(?P<active_state>\S+)'
                             ' +(?P<standby_rp>\S+)'
                             ' +(?P<standby_state>\S+)$')
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

    def cli(self):

        ret_dict = {}

        cmd = 'show run formal | i af-group'
        conf = self.device.execute(cmd)

        for line1 in conf.splitlines():
            line1 = line1.strip()

            # router bgp 100 af-group af_group address-family ipv4 unicast
            pp1 = re.compile(r'\s*router +bgp +(?P<bgp_id>\d+)'
                              '(?: +instance +(?P<instance_name>[a-zA-Z0-9]+))?'
                              ' +af-group +(?P<pp_name>[a-zA-Z0-9\-\_]+)')
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
                    p1 = re.compile(r'^af\-group +(?P<pp>[\w\-\.\:]+) +'
                                     'address\-family +(?P<af>[\w\s]+)$')
                    m = p1.match(line)
                    if m:
                        af = m.groupdict()['af'].lower()
                        if af:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['address_family'] = af
                        continue
        
                    # default-originate policy allpass            []
                    p2 = re.compile(r'^default\-originate *(policy)? *'
                                     '(?P<policy>[\w\-\.\:\s]+)? +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p3 = re.compile(r'^maximum\-prefix +'
                                     '(?P<no>[\d]+)? +(?P<th>[\d]+)? +(?P<re>[\d]+)? +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p4 = re.compile(r'^next\-hop\-self +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p4.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['next_hop_self'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['next_hop_self_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # policy allpass in                           []
                    p5 = re.compile(r'^policy +(?P<map>[\w]+) +in +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p5.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['route_map_name_in'] = m.groupdict()['map']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['route_map_name_in_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # policy allpass out                          []
                    p6 = re.compile(r'^policy +(?P<map>[\w]+) +out +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p6.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['route_map_name_out'] = m.groupdict()['map']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['route_map_name_out_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # route-reflector-client                      []
                    p7 = re.compile(r'^route\-reflector\-client +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p7.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['route_reflector_client'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['route_reflector_client_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # send-community-ebgp                         []
                    p8 = re.compile(r'^send\-community\-ebgp +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p9 = re.compile(r'^send\-extended\-community\-ebgp +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p10 = re.compile(r'^site\-of\-origin +(?P<soo>[\w\:]+) +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p10.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                            ['soo'] = m.groupdict()['soo']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['pp_name'][pp_name]\
                                ['soo_inherit'] = m.groupdict()['inherit']
                        continue
        
                    # soft-reconfiguration inbound always         []
                    p11 = re.compile(r'^soft\-reconfiguration +(?P<soft>[\w\s]+) +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p12 = re.compile(r'^allowas\-in +(?P<al>\d+)? *'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p13 = re.compile(r'^as\-override *'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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

    def cli(self):

        ret_dict = {}

        cmd = 'show run formal | i session-group'
        conf = self.device.execute(cmd)

        for line1 in conf.splitlines():
            line1 = line1.strip()

            # router bgp 100 session-group SG
            # router bgp 333 instance test session-group abcd
            # router bgp 333 instance test neighbor 1.1.1.1 use session-group LALALALLA
            pp1 = re.compile(r'\s*router +bgp +(?P<bgp_id>\d+)'
                              '(?: +instance +(?P<instance_name>[a-zA-Z0-9]+))?'
                              '(?: +neighbor +(?P<neighbor_id>[0-9\.\:]+) +use)?'
                              ' +session-group +(?P<ps_name>[a-zA-Z0-9\-\_]+)')
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
                    p2 = re.compile(r'^remote\-as +(?P<as>\d+)? +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p3 = re.compile(r'^description +(?P<descr>[\w\,\.\:\-\s]+) +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p4 = re.compile(r'^ebgp\-multihop +(?P<num>\d+)? *'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p5 = re.compile(r'^local\-as +(?P<as>\d+) +(?P<v1>no\-prepend)? +'
                                     '(?P<v2>replace\-as)? *(?P<v3>dual\-as)? *'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p6 = re.compile(r'^password +encrypted +(?P<psw>\w+) +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p6.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['password_text'] = m.groupdict()['psw']
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['password_text_inherit'] = m.groupdict()['inherit']
                        continue

                    # shutdown                                   []
                    p7 = re.compile(r'^shutdown +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p7.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['shutdown'] = True
        
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session']\
                                [ps_name]['shutdown_inherit'] = m.groupdict()['inherit']
                        continue

                    # timers 10 30 3                             []
                    p8 = re.compile(r'^timers +(?P<keep>\d+) +'
                                     '(?P<hold>\d+) +(?P<mim>\d+)? *'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                    p9 = re.compile(r'^update\-source +(?P<intf>[\w\.\/]+) +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p9.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['update_source'] = m.groupdict()['intf'].lower()
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['update_source_inherit'] = m.groupdict()['inherit']
                        continue

                    # suppress-4byteas                        []
                    p10 = re.compile(r'^suppress\-4byteas +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p10.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['suppress_four_byte_as_capability'] = True
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['suppress_4byteas_inherit'] = m.groupdict()['inherit']
                        continue

                    # session-open-mode active-only              []
                    p11 = re.compile(r'^session\-open\-mode +(?P<mode>[\w\-]+) +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p11.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['transport_connection_mode'] = m.groupdict()['mode']
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['transport_connection_mode_inherit'] = m.groupdict()['inherit']
                        continue

                    # bfd fast-detect                            []
                    p12 = re.compile(r'^bfd fast-detect +'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
                    m = p12.match(line)
                    if m:
                        ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                            ['fall_over_bfd'] = True
                        if m.groupdict()['inherit']:
                            ret_dict['instance'][instance_name]['peer_session'][ps_name]\
                                ['fall_over_bfd_inherit'] = m.groupdict()['inherit']
                        continue

                    # ignore-connected                           []
                    p13 = re.compile(r'^ignore\-connected *'
                                     '\[(?P<inherit>[\w\-\.\:\s]+)?\]$')
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
                         Optional('as_number'): int,
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
    """

    def cli(self, vrf_type, af_type=''):

        assert vrf_type in ['all', 'vrf']
        assert af_type in ['', 'ipv4 unicast', 'ipv6 unicast']

        out = self.device.execute('show bgp instance all {vrf_type} all {af_type} process detail'.format(vrf_type=vrf_type, af_type=af_type))

        # Init dict
        ret_dict = {}
        
        # Seperate message logging pool and bmp pool
        flag = None
        
        # Init vars
        if vrf_type == 'all':
            vrf = 'default'
        elif vrf_type == 'vrf':
            vrf = None

        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'
            p1 = re.compile(r'^\s*BGP +instance +(?P<num>\S+): +\'(?P<instance>\S+)\'$')
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
            p1_1 = re.compile(r'^\s*VRF: +(?P<vrf>[a-zA-Z0-9]+)$')
            m = p1_1.match(line)
            if m:
                vrf = str(m.groupdict()['vrf'])
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                # seperate message logging pool and bmp pool
                flag = None

                # Init key values to default - overwritten below if configured
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['always_compare_med'] = False
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bestpath_compare_routerid'] = False
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bestpath_cost_community_ignore'] = False
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bestpath_med_missing_at_worst'] = False
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['enforce_first_as'] = False
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['fast_external_fallover'] = False
                continue

            # BGP Route Distinguisher: 100:1
            p1_2 = re.compile(r'^\s*BGP *Route *Distinguisher:'
                              ' *(?P<route_distinguisher>[0-9\:]+)$')
            m = p1_2.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])

                ret_dict['instance'][instance]['vrf'][vrf]['route_distinguisher'] = route_distinguisher
                continue
            
            # BGP is operating in STANDALONE mode
            p2 = re.compile(r'BGP *is *operating *in *'
                             '(?P<operation_mode>\w+) *mode$')
            m = p2.match(line)
            if m:
                operation_mode = m.groupdict()['operation_mode'].lower()

                ret_dict['instance'][instance]['vrf'][vrf]['operation_mode'] = operation_mode
                continue

            # Autonomous System number format: ASPLAIN
            p3 = re.compile(r'^Autonomous *System *number *format: *'
                             '(?P<as_format>[a-zA-Z]+)$')
            m = p3.match(line)
            if m:
                as_format = m.groupdict()['as_format']

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['as_system_number_format'] = as_format
                continue

            # Autonomous System: 100
            p4 = re.compile(r'^Autonomous *System: *(?P<as_number>[0-9]+)$')
            m = p4.match(line)
            if m:
                as_number = int(m.groupdict()['as_number'])

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['as_number'] = as_number
                continue

            # Router ID: 1.1.1.1 (manually configured)
            p5 = re.compile(r'^Router *ID: *(?P<router_id>[\w\.\:]+) *'
                             '(\([\w\s]+\))?$')
            m = p5.match(line)
            if m:
                router_id = m.groupdict()['router_id']
                
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['router_id'] = router_id
                continue

            # Default Cluster ID: 1.1.1.1
            # Default Cluster ID: 10 (manually configured)
            p6_1 = re.compile(r'^Default *Cluster *ID: *'
                             '(?P<default_cluster_id>[\w\.\:]+) *'
                             '(\([\w\s\:\.\,]+\))?$')
            m = p6_1.match(line)
            if m:
                default_cluster_id = m.groupdict()['default_cluster_id']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['default_cluster_id'] = default_cluster_id
                continue

            # Active Cluster IDs:  1.1.1.1
            p6_2 = re.compile(r'^Active *Cluster *IDs: *'
                             '(?P<active_cluster_id>[\w\.\:]+)$')
            m = p6_2.match(line)
            if m:
                active_cluster_id = m.groupdict()['active_cluster_id']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['active_cluster_id'] = active_cluster_id
                continue

            # Always compare MED is enabled
            p7_1 = re.compile(r'^Always compare MED is enabled$')
            m = p7_1.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['always_compare_med'] = True
                continue

            # Comparing router ID for eBGP paths
            p7_2 = re.compile(r'^Comparing router ID for eBGP paths$')
            m = p7_2.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bestpath_compare_routerid'] = True
                continue

            # Treating missing MED as worst
            p7_4 = re.compile(r'^Treating missing MED as worst$')
            m = p7_4.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bestpath_med_missing_at_worst'] = True
                continue

            # Fast external fallover enabled
            p8 = re.compile(r'^Fast +external +fallover +enabled$')
            m = p8.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                        ['fast_external_fallover'] = True
                continue

            #Platform RLIMIT max: 2147483648 bytes
            p9 = re.compile(r'^Platform *RLIMIT *max: *'
                             '(?P<platform_rlimit_max>[0-9\,]+) *bytes$')
            m = p9.match(line)
            if m:
                platform_rlimit_max = int(m.groupdict()['platform_rlimit_max'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['platform_rlimit_max'] = platform_rlimit_max 
                continue

            #Maximum limit for BMP buffer size: 409 MB
            p10 = re.compile(r'^Maximum +limit +for +BMP +buffer +size: *'
                              '(?P<size>[a-zA-Z0-9]+) *MB$')
            m = p10.match(line)
            if m:
                size = int(m.groupdict()['size'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['max_limit_for_bmp_buffer_size'] = size
                continue

            #Default value for BMP buffer size: 307 MB
            p11 = re.compile(r'^Default *value *for *BMP *buffer *size: *'
                              '(?P<size>[a-zA-Z0-9]+) *MB$')
            m = p11.match(line)
            if m:
                size = int(m.groupdict()['size'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['default_value_for_bmp_buffer_size'] = size
                continue

            #Current limit for BMP buffer size: 307 MB
            p12 = re.compile(r'^Current *limit *for *BMP *buffer *size: *'
                              '(?P<size>[a-zA-Z0-9]+) *MB$')
            m = p12.match(line)
            if m:
                size = int(m.groupdict()['size'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['current_limit_for_bmp_buffer_size'] = size
                continue

            #Current utilization of BMP buffer limit: 0 B
            p13 = re.compile(r'^Current *utilization *of *BMP *buffer *'
                              'limit: *(?P<limit>[a-zA-Z0-9]+) *B$')
            m = p13.match(line)
            if m:
                limit = int(m.groupdict()['limit'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['current_utilization_of_bmp_buffer_limit'] = limit
                continue

            # Neighbor logging is enabled
            p14 = re.compile(r'^Neighbor *logging *is *(?P<nbr_logging>\w+)$')
            m = p14.match(line)
            if m:
                nbr_logging = m.groupdict()['nbr_logging']
                if nbr_logging == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['log_neighbor_changes'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['log_neighbor_changes'] = False
                continue

            # Enforce first AS enabled
            p15 = re.compile(r'^Enforce +first +AS +(?P<as_enabled>\w+)$')
            m = p15.match(line)
            if m:
                as_enabled = m.groupdict()['as_enabled']
                if as_enabled == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['enforce_first_as'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['enforce_first_as'] = False
                continue

            #Default local preference: 100
            p16 = re.compile(r'^Default *local *preference: *'
                              '(?P<preference>[0-9]+)$')
            m = p16.match(line)
            if m:
                default_local_preference = int(m.groupdict()['preference'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['default_local_preference'] = default_local_preference
                continue

            #Default keepalive: 60
            p17 = re.compile(r'^Default *keepalive: *(?P<keepalive>[0-9]+)$')
            m = p17.match(line)
            if m:
                default_keepalive = int(m.groupdict()['keepalive'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['default_keepalive'] = default_keepalive
                continue

            # Non-stop routing is enabled
            p18 = re.compile(r'^Non\-stop *routing *is +(?P<status>[a-zA-Z]+)$')
            m = p18.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['non_stop_routing'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['non_stop_routing'] = False
                continue
            
            #Update delay: 120
            p19 = re.compile(r'^Update *delay: *(?P<update_delay>[0-9]+)$')
            m = p19.match(line)
            if m:
                update_delay = int(m.groupdict()['update_delay'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['update_delay'] = update_delay
                continue

            #Generic scan interval: 60 
            p20 = re.compile(r'^Generic *scan *interval: *'
                              '(?P<scan_interval>[0-9]+)$')
            m = p20.match(line)
            if m:
                scan_interval = int(m.groupdict()['scan_interval'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['generic_scan_interval'] = scan_interval
                continue

            #BGP Speaker process: 0, Node: node0_0_CPU0
            p21 = re.compile(r'^BGP *Speaker *process: *'
                              '(?P<speaker>\w+), +Node: +(?P<node>\w+)$')
            m = p21.match(line)
            if m:
                speaker = int(m.groupdict()['speaker'])
                node = m.groupdict()['node']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bgp_speaker_process'] = speaker
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['node'] = node
                continue

            #Restart count: 1
            p22 =  re.compile(r'^Restart *count: *(?P<restart_count>[0-9]+)$')
            m = p22.match(line)
            if m:
                restart_count = int(m.groupdict()['restart_count'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['restart_count'] = restart_count
                continue 

            #                            Total           Nbrs Estab/Cfg
            # Default vrfs:              1               2/2
            # Non-Default vrfs:          2               4/4
            p23 = re.compile(r'^(?P<vrf_info>[\w\-]+) +VRFs: +'
                              '(?P<total>[0-9]+) +'
                              '(?P<nbrs_estab>[0-9]+)/(?P<cfg>[0-9]+)$')
            m = p23.match(line)
            if m:
                if 'vrf_info' not in ret_dict['instance'][instance]['vrf'][vrf]\
                    :
                    ret_dict['instance'][instance]['vrf'][vrf]['vrf_info'] = {}

                vrf_info = str(m.groupdict()['vrf_info']).lower()
                # vrf_info = vrf_info.replace("-","_")
                total = int(m.groupdict()['total'])
                nbrs_estab = int(m.groupdict()['nbrs_estab'])
                cfg = int(m.groupdict()['cfg'])
                if vrf_info not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['vrf_info']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['vrf_info'][vrf_info] = {}

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['vrf_info'][vrf_info]['total'] = total
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['vrf_info'][vrf_info]['nbrs_estab'] = nbrs_estab
                ret_dict['instance'][instance]['vrf'][vrf]\
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

            p26 = re.compile(r'^Pool +(?P<pool>\w+): +(?P<alloc>\d+) +'
                              '(?P<free>\d+)$')
            m = p26.match(line)

            if m and flag == 'message':
                if 'message_logging_pool_summary' not in ret_dict['instance']\
                    [instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['message_logging_pool_summary'] = {}

                pool = str(m.groupdict()['pool']).lower()
                alloc = int(m.groupdict()['alloc'])
                free = int(m.groupdict()['free'])

                if pool not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['message_logging_pool_summary']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['message_logging_pool_summary'][pool] = {}

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['message_logging_pool_summary'][pool]['alloc'] = alloc
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['message_logging_pool_summary'][pool]['free'] = free
                continue
            elif m and flag == 'bmp':
                if 'bmp_pool_summary' not in ret_dict['instance'][instance]\
                        ['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['bmp_pool_summary'] = {}

                pool = str(m.groupdict()['pool']).lower()
                alloc = int(m.groupdict()['alloc'])
                free = int(m.groupdict()['free'])

                if pool not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bmp_pool_summary']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['bmp_pool_summary'][pool] = {}

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bmp_pool_summary'][pool]['alloc'] = alloc
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['bmp_pool_summary'][pool]['free'] = free
                continue
            elif m and not flag:
                if 'pool' not in ret_dict['instance'][instance]['vrf'][vrf]\
                    :
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['pool'] = {}

                pool = str(m.groupdict()['pool']).lower()
                alloc = int(m.groupdict()['alloc'])
                free = int(m.groupdict()['free'])

                if pool not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['pool']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['pool'][pool] = {}

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['pool'][pool]['alloc'] = alloc
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['pool'][pool]['free'] = free
                continue

            #                            Sent            Received
            # Updates:                   14              24              
            # Notifications:             1               0   
            p24_1 = re.compile(r'^Updates:'
                              ' *(?P<sent>[0-9]+) *(?P<received>[0-9]+)$')
            m = p24_1.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['sent_updates'] = int(m.groupdict()['sent'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['received_updates'] = int(m.groupdict()['received'])
                continue

            #                            Sent            Received
            # Updates:                   14              24              
            # Notifications:             1               0   
            p24_2 = re.compile(r'^Notifications:'
                              ' *(?P<sent>[0-9]+) *(?P<received>[0-9]+)$')
            m = p24_2.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['sent_notifications'] = int(m.groupdict()['sent'])
                ret_dict['instance'][instance]['vrf'][vrf]\
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
            
            p25 = re.compile(r'^(?P<att>[\w\s]+): +(?P<number>[0-9]+) +'
                              '(?P<memory_used>[0-9]+)$')
            m = p25.match(line)
            if m and not flag:
                if 'att' not in ret_dict['instance'][instance]['vrf'][vrf]\
                    :
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['att'] = {}

                att = str(m.groupdict()['att']).lower()
                att = att.replace(" ","_")
                number = int(m.groupdict()['number'])
                memory_used = int(m.groupdict()['memory_used'])

                if att not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['att']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['att'][att] = {}

                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['att'][att]['number'] = number
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['att'][att]['memory_used'] = memory_used
                continue

            # Address family: VPNv4 Unicast
            p29 = re.compile(r'^Address *family: *(?P<af>[a-zA-Z0-9\s\-\_]+)$')
            m = p29.match(line)
            if m:
                af = str(m.groupdict()['af']).lower()
                af.strip()
                if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'] = {}
                if af not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af] = {}
                continue

            # VRF VRF1 Address family: IPv6 Unicast
            # VRF a Address family: IPv4 Unicast (Table inactive)
            p29_1 = re.compile(r'^VRF +(?P<current_vrf>(\S+)) +Address +family:'
                                ' +(?P<af>[a-zA-Z0-9\s\-\_]+)'
                                '(?: +\(Table +(?P<table_state>[a-z]+)\))?$')
            m = p29_1.match(line)
            if m:
                af = str(m.groupdict()['af']).lower()
                af.strip()
                current_vrf = str(m.groupdict()['current_vrf']).lower()
                table_state = str(m.groupdict()['table_state'])
                
                if 'address_family' not in ret_dict['instance'][instance]\
                    ['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf']\
                        [vrf]['address_family'] = {}
                if af not in ret_dict['instance'][instance]['vrf']\
                    [vrf]['address_family']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af] = {}
                ret_dict['instance'][instance]['vrf'][vrf]['address_family']\
                        [af]['current_vrf'] = current_vrf
                ret_dict['instance'][instance]['vrf'][vrf]['address_family']\
                        [af]['table_state'] = table_state
                continue

            # Dampening is not enabled
            p30 = re.compile(r'^Dampening +is +(?P<dampening>[\w\s]+)$')
            m = p30.match(line)
            if m:
                dampening = m.groupdict()['dampening'].lower()
                if 'not enabled' in dampening:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['dampening'] = False
                else:                    
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['dampening'] = True
                continue

            # Client reflection is enabled in global config
            p31 = re.compile(r'^Client +reflection +is +enabled +in +global +config$')
            m = p31.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['client_to_client_reflection'] = True
                continue

            # Client reflection is not enabled in global config
            p31_1 = re.compile(r'^Client +reflection +is +not +enabled +in +global +config$')
            m = p31_1.match(line)
            if m:
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['client_to_client_reflection'] = False
                continue

            # Dynamic MED is Disabled
            p32 = re.compile(r'^Dynamic *MED *is *(?P<dynamic_med>\w+)$')
            m = p32.match(line)
            if m:
                dynamic_med = m.groupdict()['dynamic_med'].lower()
                if status == 'enabled':
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['dynamic_med'] = True
                else:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['dynamic_med'] = False
                continue

            # Dynamic MED interval : 10 minutes
            p33 = re.compile(r'^Dynamic *MED *interval *: *'
                              '(?P<interval>[a-zA-Z0-9\s]+)$')
            m = p33.match(line)
            if m:
                interval = m.groupdict()['interval']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['dynamic_med_int'] = interval
                continue

            # Dynamic MED Timer : Not Running
            p34 = re.compile(r'^Dynamic *MED *Timer *: *'
                              '(?P<dynamic_med_timer>[a-zA-Z0-9\s]+)$')
            m = p34.match(line)
            if m:
                timer = m.groupdict()['dynamic_med_timer']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['dynamic_med_timer'] = timer
                continue

            # Dynamic MED Periodic Timer : Not Running
            p35 = re.compile(r'^Dynamic *MED *Periodic *Timer *: *'
                              '(?P<timer>[a-zA-Z0-9\s]+)$')
            m = p35.match(line)
            if m:
                timer = m.groupdict()['timer']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['dynamic_med_periodic_timer'] = timer
                continue

            # Scan interval: 60
            p36 = re.compile(r'^Scan *interval: *(?P<scan_interval>[\w\s]+)$')
            m = p36.match(line)
            if m:
                scan_interval = m.groupdict()['scan_interval']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['scan_interval'] = scan_interval
                continue

            # Total prefixes scanned: 40
            p37 = re.compile(r'^Total *prefixes *scanned: *'
                              '(?P<scan>[a-zA-Z0-9\s]+)$')
            m = p37.match(line)
            if m:
                scan = m.groupdict()['scan']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['total_prefixes_scanned'] = scan
                continue

            # Prefixes scanned per segment: 100000
            p38 = re.compile(r'^Prefixes *scanned *per *segment: *'
                              '(?P<prefix_scan>[a-zA-Z0-9\s]+)$')
            m = p38.match(line)
            if m:
                prefix_scan = m.groupdict()['prefix_scan']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['prefix_scanned_per_segment'] = prefix_scan
                continue

            # Number of scan segments: 1
            p39 = re.compile(r'^Number *of *scan *segments: *'
                              '(?P<num_of_scan_segments>[a-zA-Z0-9\s]+)$')
            m = p39.match(line)
            if m:
                ret = m.groupdict()['num_of_scan_segments']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['num_of_scan_segments'] = ret
                continue

            # Nexthop resolution minimum prefix-length: 0 (not configured)
            p40 = re.compile(r'^Nexthop *resolution *minimum *prefix\-length: *'
                              '(?P<length>[\w\s\(\)]+)$')
            m = p40.match(line)
            if m:
                length = m.groupdict()['length']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['nexthop_resolution_minimum_prefix_length'] = length
                continue
            
            # Main Table Version: 43
            p41 = re.compile(r'^Main *Table *Version: *(?P<main_tab_ver>[\w\s]+)$')
            m = p41.match(line)
            if m:
                main_tab_ver = m.groupdict()['main_tab_ver']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['main_table_version'] = main_tab_ver
                continue
            
            # Table version synced to RIB: 43
            p42 = re.compile(r'^Table *version *synced *to *RIB: *'
                              '(?P<rib>[a-zA-Z0-9\s]+)$')
            m = p42.match(line)
            if m:
                rib = m.groupdict()['rib']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['table_version_synced_to_rib'] = rib
                continue

            # Table version acked by RIB: 0
            p43 = re.compile(r'^Table *version *acked *by *RIB: *'
                              '(?P<rib>[a-zA-Z0-9\s]+)$')
            m = p43.match(line)
            if m:
                rib = m.groupdict()['rib']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['table_version_acked_by_rib'] = rib
                continue

            # RIB has not converged: version 0
            p44 = re.compile(r'^RIB *has *not *converged: *'
                              '(?P<rib>[a-zA-Z0-9\s]+)$')
            m = p44.match(line)
            if m:
                rib = m.groupdict()['rib']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['rib_has_not_converged'] = rib
                continue

            # RIB table prefix-limit reached ?  [No], version 0
            p45 = re.compile(r'^RIB *table *prefix\-limit *reached +\? *'
                              '\[(?P<rib>\w+)\], +version +(?P<ver>\d+)$')
            m = p45.match(line)
            if m:
                rib = m.groupdict()['rib'].lower()
                ver = m.groupdict()['ver']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['rib_table_prefix_limit_reached'] = rib
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['rib_table_prefix_limit_ver'] = ver
                continue

            # Permanent Network Unconfigured
            p45 = re.compile(r'^Permanent +Network +(?P<status>\w+)$')
            m = p45.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['permanent_network'] = status
                continue

            # State: Normal mode.
            p46 = re.compile(r'^State: *(?P<state>[a-zA-Z\s]+).$')
            m = p46.match(line)
            if m:
                state = m.groupdict()['state'].lower()
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['state'] = state
                continue

            # BGP Table Version: 43
            p47 = re.compile(r'^BGP *Table *Version: *(?P<tab_ver>\w+)$')
            m = p47.match(line)
            if m:
                tab_ver = m.groupdict()['tab_ver']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['bgp_table_version'] = tab_ver
                continue

            # Attribute download: Disabled
            p48 = re.compile(r'^Attribute *download: *(?P<attr>[\w\s]+)$')
            m = p48.match(line)
            if m:
                attr = str(m.groupdict()['attr'])
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['attribute_download'] = attr
                continue

            # Label retention timer value 5 mins
            p49 = re.compile(r'^Label *retention *timer *value *'
                              '(?P<timer>[a-zA-Z0-9\s]+)$')
            m = p49.match(line)
            if m:
                timer = m.groupdict()['timer']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['label_retention_timer_value'] = timer
                continue

            # Soft Reconfig Entries: 0
            p50 = re.compile(r'^Soft *Reconfig *Entries: *(?P<ent>\d+)$')
            m = p50.match(line)
            if m:
                ent = m.groupdict()['ent']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['soft_reconfig_entries'] = ent
                continue
            
            # Table bit-field size : 1 Chunk element size : 3
            p51 = re.compile(r'^Table *bit\-field *size *: *'
                              '(?P<size>[0-9\s]+) *Chunk *element *size *: *'
                              '(?P<elememt_size>\d+)$')
            m = p51.match(line)
            if m:
                table_bit_field_size = m.groupdict()['size']
                chunk_elememt_size = m.groupdict()['elememt_size']
                ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['table_bit_field_size'] = table_bit_field_size
                ret_dict['instance'][instance]['vrf'][vrf]\
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

            p52 = re.compile(r'^(?P<thread>\w+\s\w+) *'
                              '(?P<trigger>\w+\s\d+\s[\d\:\.]+) +(?P<ver>[0-9]+) +'
                              '(?P<tbl_ver>[0-9]+) +(?P<trig_tid>[0-9]+)$')
            m = p52.match(line)
            if m:
                if 'thread' not in  ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'] = {}

                thread = m.groupdict()['thread'].lower().strip()
                if thread not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['thread']:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'][thread] = {}

                if 'triggers' not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['thread'][thread]:
                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'][thread]['triggers'] = {}

                trigger = m.groupdict()['trigger']
                if trigger not in ret_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][af]['thread'][thread]['triggers']:

                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'][thread]['triggers']\
                            [trigger] = {}

                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'][thread]['triggers']\
                            [trigger]['tbl_ver'] = int(m.groupdict()['tbl_ver'])

                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'][thread]['triggers']\
                            [trigger]['ver'] = int(m.groupdict()['ver'])

                    ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['thread'][thread]['triggers']\
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

            p53 = re.compile(r'^(?P<remote>[\w\s\-]+): *(?P<v1>\d+) *'
                              '(?P<v2>[0-9]+)$')
            m = p53.match(line)
            if m and flag == 'allocated':
                try:
                    af
                except Exception:
                    continue
                else:
                    if 'remote_local' not in  ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]:
                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['remote_local'] = {}

                    remote = m.groupdict()['remote'].lower()
                    if remote not in ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['remote_local']:
                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['remote_local'][remote] = {}

                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['remote_local'][remote]\
                                ['allocated'] = int(m.groupdict()['v1'])

                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['remote_local'][remote]\
                                ['freed'] = int(m.groupdict()['v2'])
                    flag = None
                continue
            elif m and flag == 'number':
                try:
                    af
                except Exception:
                    continue
                else:
                    if 'prefixes_path' not in  ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]:
                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['prefixes_path'] = {}

                    path = m.groupdict()['remote'].lower()
                    if path not in ret_dict['instance'][instance]['vrf'][vrf]\
                        ['address_family'][af]['prefixes_path']:
                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['prefixes_path'][path] = {}

                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['prefixes_path'][path]\
                                ['number'] = int(m.groupdict()['v1'])

                        ret_dict['instance'][instance]['vrf'][vrf]\
                            ['address_family'][af]['prefixes_path'][path]\
                                ['mem_used'] = int(m.groupdict()['v2'])
                    flag = None
                continue

        return ret_dict


    def yang(self, vrf_type , af_type=''):

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
                                    {Optional('route_refresh'): str,
                                     Optional('four_octets_asn'): str,
                                     Optional('vpnv4_unicast'): str,
                                     Optional('vpnv6_unicast'): str,
                                     Optional('ipv4_unicast'): str,
                                     Optional('ipv6_unicast'): str,
                                     Optional('graceful_restart'): str,
                                     Optional('enhanced_refresh'): str,
                                     Optional('multisession'): str,
                                     Optional('stateful_switchover'): str
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
    """

    def cli(self, vrf_type, af_type=''):

        assert vrf_type in ['all', 'vrf']
        assert af_type in ['', 'ipv4 unicast', 'ipv6 unicast']

        out = self.device.execute('show bgp instance all {vrf_type} all {af_type} neighbors detail'.format(vrf_type=vrf_type, af_type=af_type))

        # Init variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'
            p1 = re.compile(r'^BGP +instance +(?P<instance_number>[0-9]+): +'
                             '(?P<instance>[a-zA-Z0-9\-\_\']+)$')
            m = p1.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                instance_number = int(m.groupdict()['instance_number'])
                instance = instance.replace("'","")
                # Set instance
                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}
                if instance not in ret_dict['instance']:
                    ret_dict['instance'][instance] = {}
                continue

            # BGP neighbor is 2.2.2.2
            p2 =  re.compile(r'^\s*BGP +neighbor +is +(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
            m = p2.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                vrf = 'default'
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
            p2_1 =  re.compile(r'^\s*BGP +neighbor +is +(?P<neighbor>[a-zA-Z0-9\.\:]+), +vrf +(?P<vrf>[a-zA-Z0-9]+)$')
            m = p2_1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                vrf = str(m.groupdict()['vrf'])
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
            p3 = re.compile(r'^Remote +AS +(?P<remote_as>[0-9]+), +local +AS'
                             ' +(?P<local_as_as_no>[0-9]+)'
                             '(?:, +(?P<link_state>[a-zA-Z\s]+))?$')
            m = p3.match(line)
            if m:
                sub_dict['remote_as'] = int(m.groupdict()['remote_as'])
                if m.groupdict()['link_state']:
                    sub_dict['link_state'] = m.groupdict()['link_state']
                sub_dict['local_as_as_no'] = int(m.groupdict()['local_as_as_no'])

                # Default the values - overwritten if configured
                sub_dict['local_as_no_prepend'] = False
                sub_dict['local_as_replace_as'] = False
                sub_dict['local_as_dual_as'] = False
                continue

            # Remote router ID 10.1.5.5
            p4 = re.compile(r'^Remote *router *ID *(?P<router_id>[a-zA-Z0-9\.\:]+)$')
            m = p4.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])

                sub_dict['router_id'] = router_id
                continue

            # BGP state = Established, up for 00:53:54
            p5 = re.compile(r'^\s*BGP +state += +(?P<session_state>[a-zA-Z0-9]+)'
                             '(?:, +up +for +(?P<up_time>[\w\:]+))?$')
            m = p5.match(line)
            if m:
                session_state = str(m.groupdict()['session_state']).lower()

                sub_dict['session_state'] = session_state
                if m.groupdict()['up_time']:
                    sub_dict['up_time'] = str(m.groupdict()['up_time'])
                continue

            # BGP state = Idle (No route to multi-hop neighbor)
            p5_1 = re.compile(r'^\s*BGP +state += +(?P<session_state>[a-zA-Z0-9]+)(?:(?P<reason>.*))')
            m = p5_1.match(line)
            if m:
                session_state = str(m.groupdict()['session_state']).lower()
                sub_dict['session_state'] = session_state
                if m.groupdict()['reason']:
                    sub_dict['session_state_reason'] =  str(m.groupdict()['reason'])
                continue

            # NSR State: None
            p6 = re.compile(r'^NSR *State: *(?P<nsr_state>[a-zA-Z]+)$')
            m = p6.match(line)
            if m:
                nsr_state = str(m.groupdict()['nsr_state'])

                sub_dict['nsr_state'] = nsr_state
                continue

            # Last read 00:00:51, Last read before reset 00:00:00
            p7 = re.compile(r'^Last *read *(?P<last_read>[0-9\:]+), *Last *read *before *reset *(?P<last_read_before_reset>[0-9\:]+)$')
            m = p7.match(line)
            if m:
                last_read = str(m.groupdict()['last_read'])
                last_read_before_reset = str(m.groupdict()['last_read_before_reset'])

                sub_dict['last_read'] = last_read
                sub_dict['last_read_before_reset'] = last_read_before_reset
                continue

            # Hold time is 180, keepalive interval is 60 seconds
            p8 = re.compile(r'^Hold +time +is +(?P<holdtime>[0-9]+), +keepalive'
                             ' +interval +is +(?P<keepalive_interval>[0-9]+)'
                             ' +seconds$')
            m = p8.match(line)
            if m:
                sub_dict['holdtime'] = int(m.groupdict()['holdtime'])
                sub_dict['keepalive_interval'] = \
                    int(m.groupdict()['keepalive_interval'])
                continue

            # Configured hold time: 180, keepalive: 60, min acceptable hold time: 3
            p9 = re.compile(r'^Configured +hold +time:'
                             ' +(?P<holdtime>[0-9]+), +keepalive:'
                             ' +(?P<keepalive_interval>[0-9]+), +min'
                             ' +acceptable +hold +time:'
                             ' +(?P<min_acceptable_hold_time>[0-9]+)$')
            m = p9.match(line)
            if m:
                sub_dict['holdtime'] = int(m.groupdict()['holdtime'])
                sub_dict['keepalive_interval'] = \
                    int(m.groupdict()['keepalive_interval'])
                sub_dict['min_acceptable_hold_time'] = \
                    int(m.groupdict()['min_acceptable_hold_time'])
                continue

            # Last write 00:00:38, attempted 19, written 19
            p10 = re.compile(r'^Last *write *(?P<last_write>[0-9\:]+), *attempted *(?P<attempted>[0-9]+), *written *(?P<written>[0-9]+)$')
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
            p11 = re.compile(r'^Second *last *write *(?P<second_last_write>[0-9\:]+), *attempted *(?P<second_attempted>[0-9]+), *written *(?P<second_written>[0-9]+)$')
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
            p12 = re.compile(r'^Last *write *before *reset *(?P<last_write_before_reset>[0-9\:]+), *attempted *(?P<last_write_attempted>[0-9]+), *written *(?P<last_write_written>[0-9]+)$')
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
            p13 = re.compile(r'^Second *last *write *before *reset *(?P<second_last_write_before_reset>[0-9\:]+), *attempted *(?P<second_last_write_before_attempted>[0-9]+), written *(?P<second_last_write_before_written>[0-9]+)$')
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
            p14 =  re.compile(r'^Last *write *pulse *rcvd *(?P<last_write_pulse_rcvd>[a-zA-Z0-9\:\.\s]+) *last *full *not *set *pulse *count *(?P<last_full_not_set_pulse_count>[0-9]+)$')
            m = p14.match(line)
            if m:
                last_write_pulse_rcvd = str(m.groupdict()['last_write_pulse_rcvd'])
                last_full_not_set_pulse_count = int(m.groupdict()['last_full_not_set_pulse_count'])

                sub_dict['last_write_pulse_rcvd'] = last_write_pulse_rcvd
                sub_dict['last_full_not_set_pulse_count'] = last_full_not_set_pulse_count
                continue

            # Last write pulse rcvd before reset 00:00:00
            p15 = re.compile(r'^Last +write +pulse +rcvd +before +reset +(?P<last_write_pulse_rcvd_before_reset>[0-9\:]+)$')
            m = p15.match(line)
            if m:
                last_write_pulse_rcvd_before_reset = str(m.groupdict()['last_write_pulse_rcvd_before_reset'])

                sub_dict['last_write_pulse_rcvd_before_reset'] = last_write_pulse_rcvd_before_reset
                continue

            # Socket not armed for io, armed for read, armed for write
            p15_1 = re.compile(r'^Socket *(?P<socket_status>[a-z\s\,])$')
            m = p15_1.match(line)
            if m:
                socket_status = str(m.groupdict()['socket_status'])

                sub_dict['socket_status'] =socket_status
                continue

            # Last write thread event before reset 00:00:00, second last 00:00:00
            p16 =  re.compile(r'^Last *write *thread *event *before *reset *(?P<last_write_thread_event_before_reset>[0-9\:]+), *second *last *(?P<last_write_thread_event_second_last>[0-9\:]+)$')
            m = p16.match(line)
            if m:
                last_write_thread_event_before_reset = str(m.groupdict()['last_write_thread_event_before_reset'])
                last_write_thread_event_second_last = str(m.groupdict()['last_write_thread_event_second_last'])

                sub_dict['last_write_thread_event_before_reset'] = last_write_thread_event_before_reset
                sub_dict['last_write_thread_event_second_last'] = last_write_thread_event_second_last
                continue

            # Last KA expiry before reset 00:00:00, second last 00:00:00
            p17 = re.compile(r'^Last *KA *expiry *before *reset *(?P<last_ka_expiry_before_reset>[0-9\:]+), *second *last *(?P<last_ka_expiry_before_second_last>[0-9\:]+)$')
            m = p17.match(line)
            if m:
                last_ka_expiry_before_reset =  str(m.groupdict()['last_ka_expiry_before_reset'])
                last_ka_expiry_before_second_last = str(m.groupdict()['last_ka_expiry_before_second_last'])

                sub_dict['last_ka_expiry_before_reset'] = last_ka_expiry_before_reset
                sub_dict['last_ka_expiry_before_second_last'] = last_ka_expiry_before_second_last
                continue

            # Last KA error before reset 00:00:00, KA not sent 00:00:00
            p18 = re.compile(r'^Last *KA *error *before *reset *(?P<last_ka_error_before_reset>[0-9\:]+), *KA *not *sent *(?P<last_ka_error_ka_not_sent>[0-9\:]+)$')
            m = p18.match(line)
            if m:
                last_ka_error_before_reset = str(m.groupdict()['last_ka_error_before_reset'])
                last_ka_error_ka_not_sent = str(m.groupdict()['last_ka_error_ka_not_sent'])

                sub_dict['last_ka_error_before_reset'] = last_ka_error_before_reset
                sub_dict['last_ka_error_ka_not_sent'] = last_ka_error_ka_not_sent
                continue
            
            # Last KA start before reset 00:00:00, second last 00:00:00
            p19 =  re.compile(r'^Last *KA *start *before *reset *(?P<last_ka_start_before_reset>[0-9\:]+), *second *last *(?P<last_ka_start_before_second_last>[0-9\:]+)$')
            m = p19.match(line)
            if m:
                last_ka_start_before_reset = str(m.groupdict()['last_ka_start_before_reset'])
                last_ka_start_before_second_last = str(m.groupdict()['last_ka_start_before_second_last'])

                sub_dict['last_ka_start_before_reset'] = last_ka_start_before_reset
                sub_dict['last_ka_start_before_second_last'] = last_ka_start_before_second_last
                continue

            # Precedence: internet
            p20 =  re.compile(r'^Precedence: *(?P<precedence>[a-z]+)$') 
            m = p20.match(line)
            if m:
                precedence = str(m.groupdict()['precedence'])

                sub_dict['precedence'] = precedence
                continue

            # Non-stop routing is enabled
            p21 =  re.compile(r'^Non-stop +routing +is +enabled$')
            m = p21.match(line)
            if m:
                sub_dict['non_stop_routing'] = True
                continue

            # TCP Initial Sync :              ---                   
            p22 =  re.compile(r'^TCP *Initial *Sync :(?: *(?P<tcp_initial_sync>[a-zA-Z0-9\-\s]+))?$')
            m = p22.match(line)
            if m:
                tcp_initial_sync = str(m.groupdict()['tcp_initial_sync'])

                sub_dict['tcp_initial_sync'] = tcp_initial_sync
                continue

            # TCP Initial Sync Phase Two :    ---
            p23 = re.compile(r'^TCP *Initial *Sync *phase *Two :(?: *(?P<tcp_initial_sync_phase_two>[a-zA-Z0-9\-\s]+))?$')
            m = p23.match(line)
            if m:
                tcp_initial_sync_phase_two = str(m.groupdict()['tcp_initial_sync_phase_two'])

                sub_dict['tcp_initial_sync_phase_two'] = tcp_initial_sync_phase_two
                continue

            # TCP Initial Sync Done :         ---
            p24 = re.compile(r'^TCP *Initial *Sync *Done :(?: *(?P<tcp_initial_sync_done>[a-zA-Z0-9\-\s]+))?$') 
            m = p24.match(line)
            if m:
                tcp_initial_sync_done = str(m.groupdict()['tcp_initial_sync_done']) 

                sub_dict['tcp_initial_sync_done'] = tcp_initial_sync_done
                continue             
            
            # Enforcing first AS is enabled
            p25 = re.compile(r'^Enforcing *first *AS is *(?P<enforcing_first_as>[a-z]+)$')
            m = p25.match(line)
            if m:
                enforcing_first_as = str(m.groupdict()['enforcing_first_as'])

                sub_dict['enforcing_first_as'] = enforcing_first_as
                continue

            # Multi-protocol capability not received
            p26 =  re.compile(r'^Multi-protocol *capability *(?P<multiprotocol_capability>[a-zA-Z\s]+)$')
            m = p26.match(line)
            if m:
                multiprotocol_capability = str(m.groupdict()['multiprotocol_capability'])

                sub_dict['multiprotocol_capability'] = multiprotocol_capability
                continue

            # Neighbor capabilities:            Adv         Rcvd
            p27 = re.compile(r'^Neighbor +capabilities: +Adv +Rcvd$')
            m = p27.match(line)
            if m:
                if 'bgp_negotiated_capabilities' not in sub_dict:
                    sub_dict['bgp_negotiated_capabilities'] = {}

            #    Route refresh:                  Yes         No
            #    4-byte AS:                      Yes         No
            #    Address family IPv4 Unicast:    Yes         Yes
            p27_1= re.compile(r'^(?P<name>[a-zA-Z0-9\s\-]+): *(?P<adv>(Y|y)es|(N|n)o) *(?P<rcvd>(Y|y)es|(N|n)o+)$')
            m = p27_1.match(line)
            if m:
                name = m.groupdict()['name'].lower()
                adv = 'advertised' if m.groupdict()['adv'].lower() == 'yes' else ''
                rcvd = 'received' if m.groupdict()['rcvd'].lower() == 'yes' else ''
                # mapping ops name
                if 'route refresh' in name:
                    name = 'route_refresh'
                if 'enhanced refresh' in name:
                    name = 'enhanced_refresh'
                if '4-byte' in name:
                    name = 'four_octets_asn'
                if 'vpnv4' in name:
                    name = 'vpnv4_unicast'
                if 'vpnv6' in name:
                    name = 'vpnv6_unicast'
                if 'ipv4' in name:
                    name = 'ipv4_unicast'
                if 'ipv6' in name:
                    name = 'ipv6_unicast'
                if 'restart' in name:
                    name = 'graceful_restart'
                if 'multi' in name:
                    name = 'multisession'
                if 'switchover' in name:
                    name = 'stateful_switchover'
                sub_dict['bgp_negotiated_capabilities'][name] = adv + ' ' + rcvd
                continue

            #  Message stats:
            #    InQ depth: 0, OutQ depth: 0
            p28 = re.compile(r'^InQ *depth: *(?P<message_stats_input_queue>[0-9]+), *OutQ *depth: *(?P<message_stats_output_queue>[0-9]+)$')
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
            p29 = re.compile(r'^(?P<name>[a-zA-Z\s]+) *: *'
                              '(?P<last_sent>\w+ *\d+ *[\d\:\.]+) *'
                              '(?P<sent>[0-9]+) *'
                              '(?P<last_received>\w+ *\d+ *[\d\:\.\-]+) *'
                              '(?P<received>[0-9]+)$')
            m = p29.match(line)

            p29_1 = re.compile(r'^(?P<name>[a-zA-Z\s]+) *: *'
                              '(?P<last_sent>[\-]+) *'
                              '(?P<sent>[0-9]+) *'
                              '(?P<last_received>[\-]+) *'
                              '(?P<received>[0-9]+)$')
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
            p30 = re.compile(r'^Minimum *time *between *advertisement *runs *is *(?P<minimum_time_between_adv_runs>[0-9]+) *secs$')
            m = p30.match(line)
            if m:
                minimum_time_between_adv_runs = int(m.groupdict()['minimum_time_between_adv_runs'])

                sub_dict['minimum_time_between_adv_runs'] = minimum_time_between_adv_runs
                continue

            # Inbound message logging enabled, 3 messages buffered
            p31 = re.compile(r'^Inbound *message *logging *enabled, *(?P<inbound_message>[0-9]+) *messages *buffered$')
            m = p31.match(line)
            if m:
                inbound_message = str(m.groupdict()['inbound_message'])

                sub_dict['inbound_message'] = inbound_message
                continue

            # Outbound message logging enabled, 3 messages buffered
            p32 = re.compile(r'^Outbound *message *logging *enabled, *(?P<outbound_message>[0-9]+) *messages *buffered$')
            m =p32.match(line)
            if m:
                outbound_message = str(m.groupdict()['outbound_message'])

                sub_dict['outbound_message'] = outbound_message
                continue

            # For Address Family: IPv4 Unicast
            p33 = re.compile(r'^For +Address +Family *: +(?P<address_family>[a-zA-Z0-9\s]+)$')
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
            p34 = re.compile(r'^BGP +neighbor +version'
                              ' +(?P<neighbor_version>[0-9]+)$')
            m = p34.match(line)
            if m:
                sub_dict['address_family'][address_family]['neighbor_version'] =\
                    int(m.groupdict()['neighbor_version'])
                continue
            
            # Update group: 0.2 Filter-group: 0.2  No Refresh request being processed
            p35 = re.compile(r'^Update +group: +(?P<update_group>[0-9\.]+) +Filter-group: +(?P<filter_group>[0-9\.]+) +(?P<refresh_request_status>[a-zA-Z\s]+)$')
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
            p36 = re.compile(r'^Route *refresh *request: *received *(?P<route_refresh_request_received>[0-9]+), *sent *(?P<route_refresh_request_sent>[0-9]+)$')
            m = p36.match(line)
            if m:
                route_refresh_request_received = int(m.groupdict()['route_refresh_request_received'])
                route_refresh_request_sent = int(m.groupdict()['route_refresh_request_sent'])

                sub_dict['address_family'][address_family]['route_refresh_request_received'] = route_refresh_request_received
                sub_dict['address_family'][address_family]['route_refresh_request_sent'] = route_refresh_request_sent
                continue

            # Policy for incoming advertisements is all-pass
            p37 = re.compile(r'^Policy *for *incoming *advertisements *is *(?P<route_map_name_in>[\w\-\_]+)$')
            m = p37.match(line)
            if m:
                route_map_name_in = m.groupdict()['route_map_name_in']

                sub_dict['address_family'][address_family]['route_map_name_in'] = route_map_name_in
                continue

            # Policy for outgoing advertisements is all-pass
            p38 = re.compile(r'^Policy *for *outgoing *advertisements *is *(?P<route_map_name_out>[\w\-\_]+)$')
            m = p38.match(line)
            if m:
                route_map_name_out = m.groupdict()['route_map_name_out']

                sub_dict['address_family'][address_family]['route_map_name_out'] = route_map_name_out
                continue

            # 0 accepted prefixes, 0 are bestpaths
            p39 = re.compile(r'^(?P<accepted_prefixes>[0-9]+) *accepted *prefixes, *(?P<best_paths>[0-9]+) *are *bestpaths$')
            m = p39.match(line)
            if m:
                accepted_prefixes = int(m.groupdict()['accepted_prefixes'])
                best_paths = int(m.groupdict()['best_paths'])

                sub_dict['address_family'][address_family]['accepted_prefixes'] = accepted_prefixes
                sub_dict['address_family'][address_family]['best_paths'] = best_paths
                continue

            # Exact no. of prefixes denied : 0.
            p40 = re.compile(r'^Exact *no\. *of *prefixes *denied *: *(?P<exact_no_prefixes_denied>[0-9]+)\.$')
            m = p40.match(line)
            if m:
                exact_no_prefixes_denied = int(m.groupdict()['exact_no_prefixes_denied'])

                sub_dict['address_family'][address_family]['exact_no_prefixes_denied'] = exact_no_prefixes_denied
                continue
            
            # Cumulative no. of prefixes denied: 5.
            p41 = re.compile(r'^Cumulative *no\. *of *prefixes *denied: *(?P<cummulative_no_prefixes_denied>[0-9]+)\.$')
            m = p41.match(line)
            if m:
                cummulative_no_prefixes_denied = int(m.groupdict()['cummulative_no_prefixes_denied'])

                sub_dict['address_family'][address_family]['cummulative_no_prefixes_denied'] = cummulative_no_prefixes_denied
                continue            

            # No policy: 5, Failed RT match: 0
            p42 = re.compile(r'^No *policy: *(?P<cummulative_no_no_policy>[0-9]+), *Failed *RT *match: *(?P<cummulative_no_failed_rt_match>[0-9]+)$')
            m = p42.match(line)
            if m:
                cummulative_no_no_policy = int(m.groupdict()['cummulative_no_no_policy'])
                cummulative_no_failed_rt_match = int(m.groupdict()['cummulative_no_failed_rt_match'])

                sub_dict['address_family'][address_family]['cummulative_no_no_policy'] = cummulative_no_no_policy
                sub_dict['address_family'][address_family]['cummulative_no_failed_rt_match'] = cummulative_no_failed_rt_match
                continue

            # By ORF policy: 0, By policy: 0
            p43 = re.compile(r'^By *ORF *policy: *(?P<cummulative_no_by_orf_policy>[0-9]+), *By *policy: *(?P<cummulative_no_by_policy>[0-9]+)$')
            m = p43.match(line)
            if m:
                cummulative_no_by_orf_policy = int(m.groupdict()['cummulative_no_by_orf_policy'])
                cummulative_no_by_policy = int(m.groupdict()['cummulative_no_by_policy'])

                sub_dict['address_family'][address_family]['cummulative_no_by_orf_policy'] = cummulative_no_by_orf_policy
                sub_dict['address_family'][address_family]['cummulative_no_by_policy'] = cummulative_no_by_policy
                continue

            # Prefix advertised 10, suppressed 0, withdrawn 0
            p44 = re.compile(r'^Prefix +advertised +(?P<prefix_advertised>[0-9]+), +suppressed +(?P<prefix_suppressed>[0-9]+), +withdrawn +(?P<prefix_withdrawn>[0-9]+)$')
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
            p45 = re.compile(r'^Maximum +prefixes +allowed'
                              ' +(?P<maximum_prefix_max_prefix_no>[0-9]+)$')
            m = p45.match(line)
            if m:
                sub_dict['address_family'][address_family]\
                    ['maximum_prefix_max_prefix_no'] = \
                        int(m.groupdict()['maximum_prefix_max_prefix_no'])
                continue

            # Threshold for warning message 75%, restart interval 0 min
            p46 = re.compile(r'^Threshold +for +(?P<warn>warning)? *message +(?P<threshold_warning_message>[0-9\%]+), +restart +interval +(?P<threshold_restart_interval>[0-9]+) +min$')
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
            p47 = re.compile(r'^An *EoR *(?P<eor_status>[a-z\-\s]+)$')
            m = p47.match(line)
            if m:
                eor_status = str(m.groupdict()['eor_status'])

                sub_dict['address_family'][address_family]['eor_status'] = eor_status
                continue         

            # Last ack version 43, Last synced ack version 0
            p48 = re.compile(r'^Last *ack *version *(?P<last_ack_version>[0-9]+), *Last *synced *ack *version *(?P<last_synced_ack_version>[0-9]+)$')
            m = p48.match(line)
            if m:
                last_synced_ack_version = int(m.groupdict()['last_synced_ack_version'])
                last_ack_version = int(m.groupdict()['last_ack_version'])

                sub_dict['address_family'][address_family]['last_synced_ack_version'] = last_synced_ack_version
                sub_dict['address_family'][address_family]['last_ack_version'] = last_ack_version
                continue
            
            # Outstanding version objects: current 0, max 1
            p49 = re.compile(r'^Outstanding +version +objects: +current +(?P<outstanding_version_objects_current>[0-9]+), +max +(?P<outstanding_version_objects_max>[0-9]+)$')
            m = p49.match(line)
            if m:
                outstanding_version_objects_current = int(m.groupdict()['outstanding_version_objects_current'])
                outstanding_version_objects_max = int(m.groupdict()['outstanding_version_objects_max'])

                sub_dict['address_family'][address_family]['outstanding_version_objects_current'] = outstanding_version_objects_current
                sub_dict['address_family'][address_family]['outstanding_version_objects_max'] = outstanding_version_objects_max
                continue

            # Additional-paths operation: None
            p50 = re.compile(r'^Additional-paths +operation: +(?P<additional_paths_operation>[a-zA-Z]+)$')
            m = p50.match(line)
            if m:
                additional_paths_operation = str(m.groupdict()['additional_paths_operation'])

                sub_dict['address_family'][address_family]['additional_paths_operation'] = additional_paths_operation
                continue

            # Advertise routes with local-label via Unicast SAFI
            p50_1 = re.compile(r'^Advertise +routes +with +local-label +via +(?P<additional_routes_local_label>[a-zA-Z\s]+)$')
            m = p50_1.match(line)
            if m:
                additional_routes_local_label = str(m.groupdict()['additional_routes_local_label'])

                sub_dict['address_family'][address_family]['additional_routes_local_label'] = additional_routes_local_label
                continue

            # Connections established 1; dropped 0
            p51 = re.compile(r'^Connections *(?P<bgp_state>\w+) *'
                              '(?P<num>[0-9]+)\; *dropped *(?P<connections_dropped>[0-9]+)$')
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
            p52 = re.compile(r'^Local *host: *(?P<local_host>[\w\.\:]+), *Local *port: *(?P<local_port>[0-9]+), *IF *Handle: *(?P<if_handle>[a-z0-9]+)$')
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
            p53 = re.compile(r'^Foreign *host: *(?P<foreign_host>[\w\.\:]+), *Foreign *port: *(?P<foreign_port>[0-9]+)$')
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
            p54 = re.compile(r'^Last *reset *(?P<last_reset>[0-9\:]+)$')
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
            p55 = re.compile(r'^Capability +4-byte-as +suppress +is +configured$')
            m = p55.match(line)
            if m:
                sub_dict['suppress_four_byte_as_capability'] = True
                continue

            # Description: PEER
            p56 = re.compile(r'^Description: +(?P<description>[\w\s\,\.\:\-]+)$')
            m = p56.match(line)
            if m:
                sub_dict['description'] = m.groupdict()['description']
                
            # Private AS number removed from updates to this neighbor
            p57 = re.compile(r'^Private +AS +number +removed +from +updates +to +this +neighbor$')
            m = p57.match(line)
            if m:
                sub_dict['remove_private_as'] = True
                continue
                
            # Administratively shut down
            p58 = re.compile(r'^Administratively +shut +down$')
            m = p58.match(line)
            if m:
                sub_dict['shutdown'] = True
                continue
                
            # External BGP neighbor may be up to 222 hops away
            p59 = re.compile(r'^External +BGP +neighbor +may +be +up +to +'
                              '(?P<hop>\d+) +hops +away$')
            m = p59.match(line)
            if m:
                sub_dict['ebgp_multihop'] = True
                sub_dict['ebgp_multihop_max_hop'] = int(m.groupdict()['hop'])
                continue

            # TCP open mode: passive only
            p60 = re.compile(r'^TCP +open +mode: +(?P<mode>[\w\s]+)$')
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
            p61 = re.compile(r'^My +AS +number +is +allowed +(?P<num>\d+) +'
                              'times +in +received +updates$')
            m = p61.match(line)
            if m:
                sub_dict['address_family'][address_family]['allowas_in'] = True
                sub_dict['address_family'][address_family]['allowas_in_as_number'] = \
                    int(m.groupdict()['num'])
                continue

            # Route-Reflector Client
            p62 = re.compile(r'^Route\-Reflector +Client$')
            m = p62.match(line)
            if m:
                sub_dict['address_family'][address_family]['route_reflector_client'] = True
                continue

            # Extended community attribute sent to this neighbor
            p63 = re.compile(r'^(?P<send_com>\w+) +community +attribute +sent +to +this +neighbor$')
            m = p63.match(line)
            if m:
                sub_dict['address_family'][address_family]['send_community'] = \
                    m.groupdict()['send_com'].lower()
                continue

            # Inbound soft reconfiguration allowed
            p64 = re.compile(r'^Inbound +soft +reconfiguration +allowed$')
            m = p64.match(line)
            if m:
                sub_dict['address_family'][address_family]['soft_configuration'] = True
                continue

            # AS override is set
            p65 = re.compile(r'^AS +override +is +set$')
            m = p65.match(line)
            if m:
                sub_dict['address_family'][address_family]['as_override'] = True
                continue

            # Default information originate: default sent
            p66 = re.compile(r'^Default +information +originate: +(?P<route_map>[\w\s\-]:)$')
            m = p66.match(line)
            if m:
                sub_dict['address_family'][address_family]['default_originate'] = True
                sub_dict['address_family'][address_family]['default_originate_route_map'] = \
                    m.groupdict()['route_map'].strip()
                continue

            # site-of-origin 100:100
            p67 = re.compile(r'^site\-of\-origin +(?P<soo>[\w\:]+)$')
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
        show bgp instance all vrf all ipv6 unicast neighbors <neighbor> received routes"""

    schema = {'instance':
                {Any():
                    {Optional('vrf'):
                        {Any():
                            {Optional('address_family'):
                                {Any():
                                    {Optional('router_identifier'): str,
                                     Optional('route_distinguisher'): str,
                                     Optional('local_as'): int,
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
    """

    def cli(self, neighbor, vrf_type, af_type='', route_type='received routes'):

        assert vrf_type in ['all', 'vrf']
        assert route_type in ['received routes', 'routes']
        assert af_type in ['', 'ipv4 unicast', 'ipv6 unicast']

        cmd = 'show bgp instance all {vrf_type} all {af_type} neighbors {neighbor} {route}'\
              .format(neighbor=neighbor, vrf_type=vrf_type, af_type=af_type, route=route_type)
        out = self.device.execute(cmd)

        # Init vars
        ret_dict = {}
        instance = None
        address_family = None

        if vrf_type == 'all':
            vrf = 'default'
            af = ''
        elif vrf_type == 'vrf':
            vrf = None
            if af_type == 'ipv6 unicast':
                af = 'vpnv6 unicast'
            else:
                af = 'vpnv4 unicast'

        # handle route table name
        routes = 'received' if 'received' in route_type else 'routes'

        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'
            p1 = re.compile(r'^BGP *instance *(?P<instance_number>[0-9]+): *(?P<instance>[a-zA-Z0-9\-\_\']+)$')
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
            p15 = re.compile(r'^BGP *VRF *(?P<vrf>[a-zA-Z0-9]+), *'
                              'state: *(?P<state>[a-zA-Z]+)$')
            m = p15.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                state = m.groupdict()['state'].lower()

                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                continue

            # BGP Route Distinguisher: 200:2
            p15_1 = re.compile(r'^BGP Route Distinguisher: *(?P<route_distinguisher>[0-9\:]+)')
            m = p15_1.match(line)
            if m:
                route_distinguisher = m.groupdict()['route_distinguisher']
                continue

            # VRF ID: 0x60000002
            p16 = re.compile(r'^\s*VRF *ID: *(?P<vrf_id>[a-z0-9]+)$')
            m = p16.match(line)
            if m:
                vrf_id = m.groupdict()['vrf_id']
                continue


            # Address Family: VPNv4 Unicast
            p2 = re.compile(r'^Address *Family: *(?P<address_family>[a-zA-Z0-9\s]+)$')
            m = p2.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                continue


            # BGP router identifier 1.1.1.1, local AS number 100
            p3 = re.compile(r'^BGP *router *identifier *(?P<router_identifier>[0-9\.]+), *local *AS *number *(?P<local_as>[0-9]+)$')
            m = p3.match(line)
            if m:
                router_identifier = m.groupdict()['router_identifier']
                local_as = int(m.groupdict()['local_as'])
                continue

            # BGP generic scan interval 60 secs
            p4 = re.compile(r'^BGP *generic *scan *interval *(?P<generic_scan_interval>[0-9]+) +secs$')
            m = p4.match(line)
            if m:
                generic_scan_interval = int(m.groupdict()['generic_scan_interval'])
                # sub_dict['generic_scan_interval'] = generic_scan_interval
                continue

            # Non-stop routing is enabled
            p5 = re.compile(r'^(?P<non_stop_routing>(Non-stop routing is enabled))$')
            m = p5.match(line)
            if m:
                non_stop_routing = True
                continue

            # BGP table state: Active
            p6 = re.compile(r'^BGP *table *state: *(?P<table_state>[a-zA-Z]+)$')
            m = p6.match(line)
            if m:
                table_state = str(m.groupdict()['table_state']).lower()
                continue

            # Table ID: 0x0   RD version: 0
            p7 = re.compile(r'^Table *ID: *(?P<table_id>[a-z0-9]+) *RD *version: *(?P<rd_version>[0-9]+)$')
            m = p7.match(line)
            if m:
                table_id = m.groupdict()['table_id']
                rd_version = int(m.groupdict()['rd_version'])
                continue

            # BGP main routing table version 43
            p8 = re.compile(r'^BGP *main *routing *table *version *(?P<bgp_table_version>[0-9]+)$')
            m = p8.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                continue

            # BGP NSR Initial initsync version 11 (Reached)
            p9 = re.compile(r'^BGP *NSR *Initial *initsync *version *(?P<nsr_initial_initsync_version>[0-9]+) *\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')
            m = p9.match(line)
            if m:
                nsr_initial_initsync_version = m.groupdict()['nsr_initial_initsync_version']
                nsr_initial_init_ver_status = str(m.groupdict()['nsr_initial_init_ver_status']).lower()
                continue

            # BGP NSR/ISSU Sync-Group versions 0/0
            p10 = re.compile(r'^BGP *NSR/ISSU *Sync-Group *versions *(?P<nsr_issu_sync_group_versions>[0-9\/\s]+)$')
            m = p10.match(line)
            if m:
                nsr_issu_sync_group_versions = m.groupdict()['nsr_issu_sync_group_versions']
                continue

            # BGP scan interval 60 secs
            p11 = re.compile(r'^BGP *scan *interval *(?P<scan_interval>[0-9\S]+) *secs$')
            m = p11.match(line)
            if m:
               scan_interval = int(m.groupdict()['scan_interval'])
               continue

            # Route Distinguisher: 200:1 (default for vrf VRF1)
            p12 = re.compile(r'^Route +Distinguisher: *(?P<route_distinguisher>[0-9\:]+) *'
                              '(\(default +for +vrf +(?P<default_vrf>[a-zA-Z0-9]+)\))?$')
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
                    
           # *>i46.2.6.0/24        4.4.4.4               2219    100      0 400 33299 51178 47751 {27016} e
            # *> 615:11:11::/64     2001:db8:20:1:5::5
            p13 = re.compile(r'^(?P<status_codes>(i|s|x|S|d|h|\*|\>|\s)+)? *'
                              '(?P<prefix>(?P<ip>[\w\.\:]+)/(?P<mask>\d+))? +'
                              '(?P<next_hop>[\w\.\:]+) *(?P<number>[\d\s\{\}]+)?'
                              '(?: *(?P<origin_codes>(i|e|\?)))?$')
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
            p13_1 = re.compile(r'(?P<path>[\d\s]+)'
                            ' *(?P<origin_codes>(i|e|\?))?$')
            m = p13_1.match(line)
            if m:
                if 'path' in sub_dict[routes][prefix]['index'][index]:
                    sub_dict[routes][prefix]['index'][index]['path'] += \
                        ' ' + m.groupdict()['path'].strip()

                if m.groupdict()['origin_codes']:
                    sub_dict[routes][prefix]['index'][index]['origin_codes'] = \
                        m.groupdict()['origin_codes']

            # Processed 5 prefixes, 5 paths
            p14 = re.compile(r'^Processed *(?P<processed_prefixes>[0-9]+) *'
                              'prefixes, *(?P<processed_paths>[0-9]+) *paths$')
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
    """

    def cli(self, neighbor, vrf_type, af_type=''):
        
        assert vrf_type in ['all', 'vrf']
        assert af_type in ['', 'ipv4 unicast', 'ipv6 unicast']
        
        cmd = 'show bgp instance all {vrf_type} all {af_type} neighbors {neighbor} advertised-routes'\
              .format(neighbor=neighbor, af_type=af_type, vrf_type=vrf_type)
        out = self.device.execute(cmd)

        ret_dict = {}
        address_family = None

        if vrf_type == 'all':
            vrf = 'default'
            af = ''
        elif vrf_type == 'vrf':
            vrf = None
            if af_type == 'ipv6 unicast':
                af = 'vpnv6 unicast'
            else:
                af = 'vpnv4 unicast'

        for line in out.splitlines():
            line = line.strip()

            # BGP instance 0: 'default'
            p1 = re.compile(r'^BGP *instance *(?P<instance_number>[0-9]+): *(?P<instance>[a-zA-Z0-9\-\_\']+)$')
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
            p2 = re.compile(r'^VRF: *(?P<vrf>[a-zA-Z0-9]+)$')
            m = p2.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if 'vrf' not in ret_dict['instance'][instance]:
                    ret_dict['instance'][instance]['vrf'] = {}
                if vrf not in ret_dict['instance'][instance]['vrf']:
                    ret_dict['instance'][instance]['vrf'][vrf] = {}
                    continue

            # Address Family: VPNv4 Unicast
            p7 = re.compile(r'^Address *Family: *(?P<address_family>[a-zA-Z0-9\s]+)$')
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
            p3 = re.compile(r'^Route *Distinguisher: *(?P<route_distinguisher>[0-9\:]+) *'
                             '(\(default *for *vrf (?P<default_vrf>[0-9A-Z]+)\))?$')
            m = p3.match(line)
            if m:
                rd = m.groupdict()['route_distinguisher']
                addr = (address_family or af) + ' RD ' + rd
                default_vrf = m.groupdict()['default_vrf']
                if 'address_family' not in ret_dict['instance'][instance]['vrf'][vrf]:
                    ret_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                if address_family not in ret_dict['instance'][instance]['vrf'][vrf]['address_family']:
                    sub_dict = ret_dict['instance'][instance]['vrf'][vrf]['address_family'][addr] = {}
                sub_dict['route_distinguisher'] = rd
                sub_dict['default_vrf'] = default_vrf if default_vrf else 'default'
                continue

            # Network            Next Hop        From            AS Path
            # 46.1.1.0/24        20.1.5.1        2.2.2.2         100 300 33299 51178 47751 {27016}e
            # 615:11:11::/64     1.1.1.1         2001:db8:20:1:5::5
            # 1.1.1.1/32         1.1.1.1         Local           ?
            p4 = re.compile(r'^(?P<prefix>(?P<ip>[\w\.\:]+)/(?P<mask>\d+)) *(?P<next_hop>[\w\.\:]+) *(?P<froms>[\w\.\:]+) *'
                             '(?P<path>[\d\{\}\s]+)?(?P<origin_code>[e|i\?])?$')
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
            p5_1 = re.compile(r'(?P<path>[\d\{\}\s]+)(?P<origin_code>e|i)?$')
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
            p6 = re.compile(r'^Processed *(?P<processed_prefixes>[0-9]+) *prefixes, *(?P<processed_paths>[0-9]+) *paths$')
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
                                 Optional('local_as'): int,
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

class ShowBgpInstanceNeighborsRoutes(ShowBgpInstanceNeighborsRoutesSchema):
    
    """ Parser for:
        show bgp instance all all all neighbors <WORD> routes
        show bgp instance all vrf all neighbors <WORD> routes
        show bgp instance all vrf all ipv4 unicast neighbors <WORD> routes
        show bgp instance all vrf all ipv6 unicast neighbors <WORD> routes
    """

    def cli(self, neighbor, vrf_type, af_type=''):
        return ShowBgpInstanceNeighborsReceivedRoutes.cli(
            self, neighbor=neighbor, vrf_type=vrf_type, af_type=af_type, route_type='routes')


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
                                Optional('local_as'): int,
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
                                {'remote_as': int,
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
    """

    def cli(self, vrf_type, af_type=''):

        assert vrf_type in ['all', 'vrf']
        assert af_type in ['', 'ipv4 unicast', 'ipv6 unicast']
        cmd = 'show bgp instance all {vrf_type} all {af_type} summary'.format(vrf_type=vrf_type, af_type=af_type)
        out = self.device.execute(cmd)

        # Init vars
        bgp_instance_summary_dict = {}
        data_on_nextline = False

        if vrf_type == 'all':
            vrf = 'default'
            af_default = None
        elif vrf_type == 'vrf':
            vrf = None
            if af_type == 'ipv6 unicast':
                af_default = 'vpnv6 unicast'
            else:
                af_default = 'vpnv4 unicast'

        # init the route_distinguisher when all all all command
        route_distinguisher = None

        for line in out.splitlines():
            line = line.rstrip()

            # BGP instance 0: 'default' 
            p1 = re.compile(r'^\s*BGP *instance *(?P<instance_number>[0-9]+):'
                             ' *(?P<instance>[a-zA-Z0-9\-\_\']+)$')
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
            p2 = re.compile(r'^\s*VRF: *(?P<vrf>[a-zA-Z0-9]+)$')
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
            p3 = re.compile(r'^\s*Address *Family:'
                            ' *(?P<address_family>[a-zA-Z0-9\s]+)$')
            m = p3.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                if 'address_family' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                if address_family not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family] = {}
                continue

            # BGP VRF VRF1, state: Active
            p4 = re.compile(r'^\s*BGP *VRF *(?P<bgp_vrf>[A-Z0-9]+), *state:'
                             ' *(?P<vrf_state>[a-zA-Z]+)$')
            m = p4.match(line)
            if m:
                bgp_vrf = m.groupdict()['bgp_vrf'].lower()
                vrf_state = m.groupdict()['vrf_state'].lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['bgp_vrf'] = bgp_vrf
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['vrf_state'] = vrf_state
                continue

            # BGP Route Distinguisher: 200:1
            p5 = re.compile(r'^\s*BGP *Route *Distinguisher:'
                             ' *(?P<route_distinguisher>[0-9\:]+)$')
            m = p5.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['route_distinguisher'] = route_distinguisher
                continue

            # VRF ID: 0x60000001
            p6 = re.compile(r'^\s*VRF *ID: *(?P<vrf_id>[a-z0-9]+)$')
            m = p6.match(line)
            if m:
                vrf_id = str(m.groupdict()['vrf_id'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['vrf_id'] = vrf_id
                continue 

            # BGP router identifier 11.11.11.11, local AS number 100
            p7 = re.compile(r'^\s*BGP *router *identifier'
                            ' *(?P<router_id>[0-9\.]+)\, *local *AS *number'
                            ' *(?P<local_as>[0-9]+)$')
            m = p7.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                local_as = int(m.groupdict()['local_as'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['router_id'] = router_id
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['local_as'] = local_as
                continue

            # BGP generic scan interval 60 secs
            p8 = re.compile(r'^\s*BGP *generic *scan *interval'
                             ' *(?P<generic_scan_interval>[0-9]+) *secs$')
            m = p8.match(line)
            if m:
                generic_scan_interval = int(m.groupdict()['generic_scan_interval'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['generic_scan_interval'] = generic_scan_interval
                continue

            # Non-stop routing is enabled
            p9 = re.compile(r'^\s*Non-stop *routing *is'
                             ' *(?P<non_stop_routing>[A-Za-z]+)$')
            m = p9.match(line)
            if m:
                non_stop_routing = str(m.groupdict()['non_stop_routing'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['non_stop_routing'] = non_stop_routing
                continue

            # BGP table state: Active
            p10 = re.compile(r'^\s*BGP *table *state:'
                              ' *(?P<table_state>[a-zA-Z]+)$')
            m = p10.match(line)
            if m:
                table_state = str(m.groupdict()['table_state']).lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['table_state'] = table_state
                continue

            # Table ID: 0x0   RD version: 0
            p11 = re.compile(r'^\s*Table *ID: *(?P<table_id>[a-z0-9]+)'
                              ' *RD *version: (?P<rd_version>[0-9]+)$')
            m = p11.match(line)
            if m:
                table_id = str(m.groupdict()['table_id'])
                rd_version = int(m.groupdict()['rd_version'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['table_id'] = table_id
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['rd_version'] = rd_version
                continue

            # BGP main routing table version 63
            p12 = re.compile(r'^\s*BGP *main *routing *table *version'
                              ' *(?P<bgp_table_version>[0-9]+)$')
            m = p12.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['bgp_table_version'] =  bgp_table_version       
                continue

            # BGP NSR Initial initsync version 11 (Reached)
            p13 = re.compile(r'^\s*BGP *NSR *Initial *initsync *version'
                              ' *(?P<nsr_initial_initsync_version>[0-9]+)'
                              ' *\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')
            m = p13.match(line)
            if m:
                nsr_initial_initsync_version = int(m.groupdict()['nsr_initial_initsync_version'])
                nsr_initial_init_ver_status = str(m.groupdict()['nsr_initial_init_ver_status']).lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['nsr_initial_initsync_version'] = nsr_initial_initsync_version
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['nsr_initial_init_ver_status'] = nsr_initial_init_ver_status
                continue

            # BGP NSR/ISSU Sync-Group versions 0/0
            p14 = re.compile(r'^\s*BGP *NSR/ISSU *Sync-Group *versions'
                              ' *(?P<nsr_issu_sync_group_versions>[0-9\/]+)$')
            m = p14.match(line)
            if m:
                nsr_issu_sync_group_versions = str(m.groupdict()['nsr_issu_sync_group_versions'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['nsr_issu_sync_group_versions'] = nsr_issu_sync_group_versions
                continue

            # BGP scan interval 60 secs
            p15 = re.compile(r'^\s*BGP *generic *scan *interval *(?P<scan_interval>[0-9]+) *secs$')
            m = p15.match(line)
            if m:
                scan_interval = int(m.groupdict()['scan_interval'])
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['scan_interval'] = scan_interval
                continue

            # BGP is operating in STANDALONE mode.
            p16 = re.compile(r'^\s*BGP *is *operating *in *(?P<operation_mode>[a-zA-Z]+) *mode.$')
            m = p16.match(line)
            if m:
                operation_mode = str(m.groupdict()['operation_mode']).lower()
                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['operation_mode'] = operation_mode
                continue

            # Process       RcvTblVer   bRIB/RIB   LabelVer  ImportVer  SendTblVer  StandbyVer
            # Speaker              63         63         63         63          63           0
            p17 = re.compile(r'^\s*(?P<process>[a-zA-Z]+) *(?P<rcvtblver>[0-9]+)'
                              ' *(?P<brib_rib>[0-9]+) *(?P<labelver>[0-9]+)'
                              ' *(?P<importver>[0-9]+) *(?P<sendtblver>[0-9]+)'
                              ' *(?P<standbyver>[0-9]+)$')
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
            p17_1 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
            m = p17_1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor'])
                data_on_nextline = True
                if 'neighbor' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'] = {}
                if neighbor not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor] = {}
                    continue
            
            # Neighbor        Spk    AS msg_rcvd msg_sent   TblVer  InQ OutQ  Up/Down  St/PfxRcd
            #                   3   200       0       0        0    0    0 00:00:00 Idle
            p17_2 = re.compile(r'^\s*(?P<spk>[0-9]+) +(?P<remote_as>[0-9]+)'
                                ' +(?P<msg_rcvd>[0-9]+) +(?P<msg_sent>[0-9]+)'
                                ' +(?P<tbl_ver>[0-9]+) +(?P<input_queue>[0-9]+)'
                                ' +(?P<output_queue>[0-9]+) +(?P<up_down>[a-z0-9\:]+)'
                                ' +(?P<state_pfxrcd>\S+)$')
            m = p17_2.match(line)
            if m and data_on_nextline:
                data_on_nextline = False
                if 'address_family' not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'] = {}
                if address_family not in bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']:
                    bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family'][address_family] = {}

                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'] = int(m.groupdict()['remote_as'])
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
            # 2.2.2.2           0   100       0       0        0    0    0 00:00:00 Idle
            p17_3 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<spk>[0-9]+)'
                              ' +(?P<remote_as>[0-9]+) +(?P<msg_rcvd>[0-9]+)'
                              ' +(?P<msg_sent>[0-9]+)'
                              ' +(?P<tbl_ver>[0-9]+) +(?P<input_queue>[0-9]+)'
                              ' +(?P<output_queue>[0-9]+) +(?P<up_down>[a-z0-9\:]+)'
                              ' +(?P<state_pfxrcd>\S+)$')
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

                bgp_instance_summary_dict['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'] = int(m.groupdict()['remote_as'])
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
                                 Optional('local_as'): int,
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
                                                {'next_hop': str,
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

class ShowBgpInstanceAllAll(ShowBgpInstanceAllAllSchema):

    """Parser for:
        show bgp instance all all all
        show bgp instance all vrf all
        show bgp instance all vrf all ipv4 unicast
        show bgp instance all vrf all ipv6 unicast
    """

    def cli(self, vrf_type, af_type=''):

        assert vrf_type in ['all', 'vrf']
        assert af_type in ['', 'ipv4 unicast', 'ipv6 unicast']

        cmd = 'show bgp instance all {vrf_type} all {af_type}'.format(vrf_type=vrf_type, af_type=af_type)
        out = self.device.execute(cmd)

        bgp_instance_all_all_dict = {}

        if vrf_type == 'all':
            vrf = 'default'
            af_default = None
        elif vrf_type == 'vrf':
            vrf = None
            if af_type == 'ipv6 unicast':
                af_default = 'vpnv6 unicast'
            else:
                af_default = 'vpnv4 unicast'

        # init the route_distinguisher when all all all command

        for line in out.splitlines():
            line = line.rstrip()

            # BGP instance 0: 'default'
            p1 = re.compile(r'^\s*BGP *instance *(?P<instance_number>[0-9]+):'
                             ' *(?P<instance>[a-zA-Z0-9\-\_\']+)$')
            m = p1.match(line)
            if m:
                instance = m.groupdict()['instance']
                instance = instance.replace("'","")
                instance_number = str(m.groupdict()['instance_number'])
                if 'instance' not in bgp_instance_all_all_dict:
                    bgp_instance_all_all_dict['instance'] = {}
                if instance not in bgp_instance_all_all_dict['instance']:
                    bgp_instance_all_all_dict['instance'][instance] = {}
                # VRF is default - init dictionary here
                if vrf_type == 'all' and vrf == 'default':
                    if 'vrf' not in bgp_instance_all_all_dict['instance'][instance]:
                        bgp_instance_all_all_dict['instance'][instance]['vrf'] = {}
                    if vrf not in bgp_instance_all_all_dict['instance'][instance]['vrf']:
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf] = {}
                        continue

            # VRF: VRF1
            p2 = re.compile(r'^\s*VRF: *(?P<vrf>[a-zA-Z0-9]+)$')
            m = p2.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if 'vrf' not in bgp_instance_all_all_dict['instance'][instance]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'] = {}
                if vrf not in bgp_instance_all_all_dict['instance'][instance]['vrf']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf] = {}
                # Address family is default - init ipv4 unicast dictionary here
                if vrf_type == 'vrf' and af_default:
                    address_family = af_default
                    original_address_family = address_family
                    if 'address_family' not in bgp_instance_all_all_dict['instance']\
                                                        [instance]['vrf'][vrf]:
                        bgp_instance_all_all_dict['instance'][instance]['vrf']\
                                                    [vrf]['address_family'] = {}
                    if address_family not in bgp_instance_all_all_dict['instance']\
                                    [instance]['vrf'][vrf]['address_family']:
                        bgp_instance_all_all_dict['instance'][instance]['vrf']\
                                    [vrf]['address_family'][address_family] = {}
                        continue

                   
            # Address Family: VPNv4 Unicast
            p3 = re.compile(r'^\s*Address *Family: *(?P<address_family>[a-zA-Z0-9\s]+)$')
            m = p3.match(line)
            if m:
                address_family = m.groupdict()['address_family'].lower()
                original_address_family = address_family
                if 'address_family' not in bgp_instance_all_all_dict['instance']\
                                                        [instance]['vrf'][vrf]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                                                        ['address_family'] = {}
                if address_family not in bgp_instance_all_all_dict['instance']\
                                    [instance]['vrf'][vrf]['address_family']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                                        ['address_family'][address_family] = {}
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                ['address_family'][address_family]['instance_number'] = instance_number
                continue

            # BGP VRF VRF1, state: Active
            p4 = re.compile(r'^\s*BGP *VRF *(?P<bgp_vrf>[A-Z0-9]+), *state:'
                             ' *(?P<vrf_state>[a-zA-Z]+)$')
            m = p4.match(line)
            if m:
                bgp_vrf = m.groupdict()['bgp_vrf'].lower()
                vrf_state = m.groupdict()['vrf_state'].lower()
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][address_family]['bgp_vrf'] = bgp_vrf
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                ['address_family'][address_family]['vrf_state'] = vrf_state
                continue

            # VRF ID: 0x60000001    
            p5 = re.compile(r'^\s*VRF *ID: *(?P<vrf_id>[a-zA-Z0-9]+)$')
            m = p5.match(line)
            if m:
                vrf_id = m.groupdict()['vrf_id']

                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][address_family]['vrf_id'] = vrf_id
                continue

            # BGP router identifier 1.1.1.1, local AS number 100
            p6 = re.compile(r'^\s*BGP *router *identifier *(?P<router_identifier>[0-9\.]+),'
                            ' *local *AS *number *(?P<local_as>[0-9]+)$')
            m = p6.match(line)
            if m:
                router_identifier = m.groupdict()['router_identifier']
                local_as = int(m.groupdict()['local_as'])
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                    [address_family]['router_identifier'] = router_identifier
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                    [address_family]['local_as'] = local_as
                continue 

            # BGP generic scan interval 60 secs 
            p7 =  re.compile(r'^\s*BGP *generic *scan *interval *(?P<generic_scan_interval>[0-9]+) *secs$')
            m = p7.match(line)
            if m:
                generic_scan_interval = m.groupdict()['generic_scan_interval']
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                [address_family]['generic_scan_interval'] = generic_scan_interval
                continue          

            # Non-stop routing is enabled
            p8 = re.compile(r'^\s*(?P<non_stop_routing>(Non-stop routing is enabled))$')
            m = p8.match(line)
            if m:
                non_stop_routing = True
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                [address_family]['non_stop_routing'] = non_stop_routing
                continue

            # BGP table state: Active
            p9 = re.compile(r'^\s*BGP *table *state: *(?P<table_state>[a-zA-Z]+)$')
            m = p9.match(line)
            if m:
                table_state = m.groupdict()['table_state'].lower()
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                    [address_family]['table_state'] = table_state
                continue

            # Table ID: 0x0   RD version: 0
            p10 = re.compile(r'^\s*Table *ID: *(?P<table_id>[a-z0-9]+) *RD *version:'
                            ' *(?P<rd_version>[0-9]+)$')
            m = p10.match(line)
            if m:
                table_id = m.groupdict()['table_id']
                rd_version = int(m.groupdict()['rd_version'])
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                ['address_family'][address_family]['table_id'] = table_id
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                ['address_family'][address_family]['rd_version'] = rd_version
                continue

            # BGP main routing table version 43
            p11 = re.compile(r'^\s*BGP *main *routing *table *version *(?P<bgp_table_version>[0-9]+)$')
            m = p11.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                ['address_family'][address_family]['bgp_table_version'] = bgp_table_version
                continue

            # BGP NSR Initial initsync version 11 (Reached)
            p12 = re.compile(r'^\s*BGP *NSR *Initial *initsync *version'
                ' *(?P<nsr_initial_initsync_version>[0-9]+) *\((?P<nsr_initial_init_ver_status>[a-zA-Z]+)\)$')
            m = p12.match(line)
            if m:
                nsr_initial_initsync_version = m.groupdict()['nsr_initial_initsync_version']
                nsr_initial_init_ver_status = str(m.groupdict()['nsr_initial_init_ver_status']).lower()
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                [address_family]['nsr_initial_initsync_version'] = nsr_initial_initsync_version
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                [address_family]['nsr_initial_init_ver_status'] = nsr_initial_init_ver_status
                continue

            # BGP NSR/ISSU Sync-Group versions 0/0
            p13 = re.compile(r'^\s*BGP *NSR/ISSU *Sync-Group *versions *(?P<nsr_issu_sync_group_versions>[0-9\/\s]+)$')
            m = p13.match(line)
            if m:
                nsr_issu_sync_group_versions = m.groupdict()['nsr_issu_sync_group_versions']
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
                [address_family]['nsr_issu_sync_group_versions'] = nsr_issu_sync_group_versions
                continue

            # BGP scan interval 60 secs
            p14 = re.compile(r'^\s*BGP *scan *interval *(?P<scan_interval>[0-9\s]+) *secs$')
            m = p14.match(line)
            if m:
               scan_interval = int(m.groupdict()['scan_interval'])
               bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']\
               [address_family]['scan_interval'] = int(scan_interval)
               continue

            # Route Distinguisher: 200:1 (default for vrf VRF1)
            p15 = re.compile(r'^\s*Route +Distinguisher: *(?P<route_distinguisher>[0-9\:]+)'
                '(?: +\(default +for +vrf +(?P<default_vrf>[a-zA-Z0-9]+)\))?$')
            m = p15.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                address_family = original_address_family + ' RD ' + route_distinguisher
                default_vrf = str(m.groupdict()['default_vrf']).lower()   
                if 'address_family' not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'] = {}
                if address_family not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family] = {}
                try:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][address_family]['default_vrf'] = default_vrf
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]\
                    ['address_family'][address_family]['route_distinguisher'] = route_distinguisher
                except Exception:
                    pass

            p16_1 = re.compile(r'^\s*(?P<status_codes>(i|s|x|S|d|h|\*|\>|\s)+) *(?P<prefix>(?P<ip>[\w\:]+)/(?P<mask>\d+)) *(?P<next_hop>[\w\:]+)$')
            m = p16_1.match(line)
            if m:
                status_codes = str(m.groupdict()['status_codes'])
                status_codes = status_codes.replace(" ", "") 
                next_hop = m.groupdict()['next_hop']
                prefix = m.groupdict()['prefix']

                if prefix:
                    index = 1
                    last_prefix = prefix
                
                if 'prefix' not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'] = {}

                if last_prefix not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix] = {}

                if 'index' not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'] = {}

                if index not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index] = {}

                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['next_hop'] = next_hop
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['status_codes'] = status_codes
                    continue

            #2219             0 200 33299 51178 47751 {27016} e
            p16_2 = re.compile(r'^\s*(?P<metric>[0-9]+) *(?P<weight>[0-9]+) *(?P<path>[0-9\{\}\s]+) (?P<origin_codes>(i|e|\?))$')
            m = p16_2.match(line)
            if m:
                metric = str(m.groupdict()['metric'])
                weight = str(m.groupdict()['weight'])
                path = str(m.groupdict()['path'])
                origin_codes = str(m.groupdict()['origin_codes'])
                if m:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['metric'] = metric    
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['weight'] = weight
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['path'] = path
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['origin_codes'] = origin_codes
                    continue
                    
            # prefix key
            p16 = re.compile(r'^(?P<status_codes>(i|s|x|S|d|h|\*|\>|\s)+) *(?P<prefix>(?P<ip>[\w\.\:]+)/(?P<mask>\d+))? +(?P<next_hop>[\w\.\:]+) +(?P<number>[\d\s\{\}]+)(?: *(?P<origin_codes>(i|e|\?)))?$')
            m = p16.match(line)
            if m:
                status_codes = str(m.groupdict()['status_codes'])
                status_codes = status_codes.replace(" ", "")
                next_hop = m.groupdict()['next_hop']
                prefix = m.groupdict()['prefix']

                if prefix:
                    index = 1
                    last_prefix = prefix
            
                else:
                    prefix = last_prefix
                    index = index + 1
                
                if 'prefix' not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'] = {}

                if last_prefix not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix] = {}

                if 'index' not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'] = {}

                if index not in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index] = {}

                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['next_hop'] = next_hop
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['status_codes'] = status_codes

                    group_num = m.groupdict()['number']

                    m1 = re.compile(r'^(?P<metric>[0-9]+)  +(?P<locprf>[0-9]+)  +(?P<weight>[0-9]+) (?P<path>[0-9\{\}\s]+)$').match(group_num)

                    m2 = re.compile(r'^(?P<value>[0-9]+)(?P<space>\s{2,20})(?P<weight>[0-9]+) (?P<path>[0-9\{\}\s]+)$').match(group_num)

                    m3 = re.compile(r'^(?P<weight>[0-9]+) (?P<path>((\d+\s)|(\{\d+\}\s))+)$').match(group_num)

                    if m1:
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['metric'] = m1.groupdict()['metric']
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['locprf'] = m1.groupdict()['locprf']
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['weight'] = m1.groupdict()['weight']
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                    elif m2:
                        if len(m2.groupdict()['space']) > 8:
                            bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['metric'] = m2.groupdict()['value']
                        else:
                            bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['locprf'] = m2.groupdict()['value']

                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['weight'] = m2.groupdict()['weight']
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                    elif m3:
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['weight'] = m3.groupdict()['weight']
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()

                    if m.groupdict()['origin_codes']:
                        bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['origin_codes'] = m.groupdict()['origin_codes']
                    continue

            p17 = re.compile(r'(?P<path>[\d\s]+)'
                            ' *(?P<origin_codes>(i|e|\?))?$')
            m = p17.match(line)
            if m:
                if 'path' in bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['path'] += ' ' + m.groupdict()['path'].strip()

                if m.groupdict()['origin_codes']:
                    bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['prefix'][last_prefix]['index'][index]['origin_codes'] = m.groupdict()['origin_codes']
                continue

            # Processed 40 prefixes, 50 paths
            p18 = re.compile(r'^\s*Processed +(?P<processed_prefix>[0-9]+) +prefixes, +(?P<processed_paths>[0-9]+) +paths$')
            m = p18.match(line)
            if m:
                processed_prefix = int(m.groupdict()['processed_prefix'])
                processed_paths = int(m.groupdict()['processed_paths'])
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['processed_prefix'] = processed_prefix
                bgp_instance_all_all_dict['instance'][instance]['vrf'][vrf]['address_family'][address_family]['processed_paths'] = processed_paths
                continue

        return bgp_instance_all_all_dict 


################################################################################

# ==============================
# Parser for 'show bgp sessions'
# ==============================

class ShowBgpSessions(MetaParser):
    """Parser for show bgp sessions"""

    # TODO schema

    def cli(self):
        """parsing mechanism: cli
        """

        cmd = 'show bgp sessions'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


# ====================================
# Parser for 'show bgp vrf-db vrf all'
# ====================================

class ShowBgpVrfDbVrfAll(MetaParser):
    """Parser for show bgp vrf-db vrf all"""

    # TODO schema

    def cli(self):
        """ parsing mechanism: cli
        """

        cmd = 'show bgp vrf-db vrf all'

        out = self.device.execute(cmd)

        result = {
            'entries': [],
        }

        vrf_entry = None
        afs_col = None

        for line in out.splitlines():
            line = line.rstrip()

            if not line:
                continue

            if afs_col is not None:
                # Continuation of address families column

                if len(line) >= afs_col \
                        and line[:afs_col].isspace():
                    # default                          0x60000000  0:0:0           6   v4u, Vv4u,
                    #                                                                  L2evpn
                    assert vrf_entry['afs'][-1] == ''
                    vrf_entry['afs'][-1:] = [s.strip() for s in line[afs_col:].split(',')]
                    if vrf_entry['afs'][-1] != '':
                        afs_col = None
                    continue

                logger.warning('Failed to parse continuation of VRF address families')
                afs_col = None

            # VRF                              ID          RD              REF AFs

            # irb1                             0x6000003a  192.0.0.0:2     4   v4u
            # default                          0x60000000  0:0:0           6   v4u, Vv4u,
            # bd1                              -           192.0.0.3:1     2   L2evpn
            # bd2                              -           192.0.0.3:2     2   L2evpn
            # ES:GLOBAL                        -           192.0.0.3:0     2   L2evpn
            m = re.match(r'^(?P<name>\S+)' r' +(?:-|(?P<id>0x[A-Fa-f0-9]+))' r' +(?P<rd>\S+)' r' +(?P<refs>\d+)' r' +(?P<afs>.+)' r'$', line)
            if m:
                vrf_entry = {
                    'name': m.group('name'),
                    'id': m.group('id') and eval(m.group('id')),
                    'rd': m.group('rd'),
                    'refs': int(m.group('refs')),
                    'afs': [s.strip() for s in m.group('afs').split(',')],
                }
                result['entries'].append(vrf_entry)
                # NOTE: a ',' at the end of afs will leave an empty element which will be completed later
                if vrf_entry['afs'][-1] == '':
                    afs_col = m.span('afs')[0]
                continue

        return result


# ================================
# Parser for 'show bgp l2vpn evpn'
# ================================

class ShowBgpL2vpnEvpn(MetaParser):
    """Parser for show bgp l2vpn evpn"""

    # TODO schema

    def __init__(self, rd=None, prefix=None, route_type=None, **kwargs):
        self.rd = rd
        self.prefix = prefix
        self.route_type = route_type
        super().__init__(**kwargs)

    def cli(self):
        """ parsing mechanism: cli
        """

        is_detail = False
        cmd = 'show bgp l2vpn evpn'
        if self.rd is not None:
            cmd += ' rd {}'.format(self.rd)
        if self.prefix is not None:
            cmd += ' {}'.format(self.prefix)
            is_detail = True
        if self.route_type is not None:
            cmd += ' route-type {}'.format(self.route_type)

        # XXXJST Workaround Csccon issue that doesn't quote Tcl arguments properly
        cmd = re.escape(cmd)
        out = self.device.execute(cmd)
        out = re.sub(r'\r+\n', r'\n', out)

        result = {
            'rds': collections.OrderedDict(),
        }

        def finalize_network_entry(network_entry):
            m = re.match(r'^(?P<prefix>\S+)/(?P<prefix_len>\d+)$', network_entry['network'])
            assert m, network_entry['network']
            network_entry.update(m.groupdict())
            for k, func in (
                    ('network', ip_network),
                    ('prefix', ip_address),
                    ('prefix_len', int),
            ):
                v = network_entry.get(k, None)
                if v is not None:
                    v = v.strip()
                    try:
                        v = func(v)
                    except (ValueError, TypeError):
                        pass
                    network_entry[k] = v

        def finalize_path_entry(path_entry):
            for k, func in (
                    ('nexthop', ip_address),
                    ('metric', int),
                    ('localpref', int),
                    ('weight', int),
            ):
                v = path_entry.get(k, None)
                if v is not None:
                    v = v.strip() or None
                    if v is not None:
                        try:
                            v = func(v)
                        except (ValueError, TypeError):
                            pass
                    path_entry[k] = v
            path_entry['status_codes'] = tuple((path_entry['status_codes'] or '').replace(' ', ''))

        if is_detail:

            lines = out.splitlines()
            while lines:
                orig_line = lines.pop(0)
                line = orig_line.rstrip()

                # BGP routing table entry for [2][0][48][fc00.0001.0006][0]/104, Route Distinguisher: 192.0.0.0:1
                # Versions:
                #   Process           bRIB/RIB  SendTblVer
                #   Speaker                114         114
                #     Local Label: 64000
                # Last Modified: Dec  5 14:54:21.410 for 1d00h
                # Paths: (2 available, best #1)
                #   Advertised to update-groups (with more than one peer):
                #     0.2
                #   Path #1: Received by speaker 0
                #   Advertised to update-groups (with more than one peer):
                #     0.2
                #   Local
                #     0.0.0.0 from 0.0.0.0 (192.0.0.0)
                #       Origin IGP, localpref 100, valid, redistributed, best, group-best, import-candidate, rib-install
                #       Received Path ID 0, Local Path ID 0, version 114
                #       Extended community: SoO:192.0.0.0:1 RT:4:1
                #       EVPN ESI: 0001.2222.2222.2200.000a
                #   Path #2: Received by speaker 0
                #   Not advertised to any peer
                #   65002
                #     192.0.0.1 from 192.0.0.1 (192.0.0.1)
                #       Received Label 68097
                #       Origin IGP, localpref 100, valid, external, group-best, import-candidate, imported, rib-install
                #       Received Path ID 0, Local Path ID 0, version 0
                #       Extended community: SoO:192.0.0.0:1 RT:4:1
                #       EVPN ESI: 0001.2222.2222.2200.000a
                #       Source AFI: L2VPN EVPN, Source VRF: default, Source Route Distinguisher: 192.0.0.1:1

                logger.debug('Unmatched line: %r', line)

        else:

            m_network_heading = None
            lines = out.splitlines()
            while lines:
                orig_line = lines.pop(0)
                line = orig_line.rstrip()

                if not m_network_heading:

                    # BGP router identifier 192.0.0.1, local AS number 100
                    m = re.match(r'^BGP router identifier (?P<router_id>\d+\.\d+\.\d+\.\d+), local AS number (?P<local_asn>\d+)$', line)
                    if m:
                        result['router_id'] = ip_address(m.group('router_id'))
                        result['local_asn'] = int(m.group('local_asn'))
                        continue

                    # BGP generic scan interval 60 secs
                    # Non-stop routing is enabled
                    # BGP table state: Active
                    # Table ID: 0x0   RD version: 0
                    # BGP main routing table version 41
                    # BGP NSR Initial initsync version 7 (Reached)
                    # BGP NSR/ISSU Sync-Group versions 0/0
                    # BGP scan interval 60 secs

                    # Status codes: s suppressed, d damped, h history, * valid, > best
                    #               i - internal, r RIB-failure, S stale, N Nexthop-discard
                    # Origin codes: i - IGP, e - EGP, ? - incomplete

                    #    Network            Next Hop            Metric LocPrf Weight Path
                    m = re.match(r'(?P<status_codes>   )(?P<network>Network +)(?P<nexthop>Next Hop +)(?P<metric>Metric +)(?P<localpref>LocPrf +)(?P<weight>Weight )(?P<path>Path)$', line)
                    if m:
                        m_network_heading = m
                        # Notes:
                        #  - Network column value could be too long to fit. In this case, the first line will contain only path status codes and the network, the following line will contain Next Hop and the other columns.
                        #  - Values for Metric and LocPrf are optional
                        #  - Path column always contains the path's origin code which could be preceeded be an aspath specification
                        #  - After the first path, more paths for the same network can appear with a blank network column

                        _re_status_codes = r'[sdh*>irSN ]' * len(m_network_heading.group('status_codes'))
                        _re_skip_status_codes = r' ' * len(m_network_heading.group('status_codes'))
                        _re_path_end = r'\S+(?: +\d+)?(?: +\d+)? +\d+(?: +(?:\S.* )?\S)$'
                        _re_network_lookahead = r'(?=[0-9:\[])'
                        _re_network = _re_network_lookahead + r'.' * len(m_network_heading.group('network'))
                        _re_skip_network = r' ' * len(m_network_heading.group('network'))
                        re_net_and_first_path = _re_status_codes + _re_network + _re_path_end
                        re_status_and_net = r'(?P<status_codes>' + _re_status_codes + ')' + r'(?P<network>' + _re_network_lookahead + '\S+)$'
                        re_continued_first_path = _re_skip_status_codes + _re_skip_network + _re_path_end
                        re_more_path = _re_status_codes + _re_skip_network + _re_path_end

                        logger.debug('re_net_and_first_path = %r', re_net_and_first_path)
                        logger.debug('re_status_and_net = %r', re_status_and_net)
                        logger.debug('re_continued_first_path = %r', re_continued_first_path)
                        logger.debug('re_more_path = %r', re_more_path)

                        # Example:
                        #   re_net_and_first_path = '[sdh*>irSN ][sdh*>irSN ][sdh*>irSN ](?=[0-9:\\[])...................\\S+(?: +\\d+)?(?: +\\d+)? +\\d+(?: +(?:\\S.* )?\\S)$'
                        #   re_status_and_net = '(?P<status_codes>[sdh*>irSN ][sdh*>irSN ][sdh*>irSN ])(?P<network>(?=[0-9:\\[])\\S+)$'
                        #   re_continued_first_path = '                      \\S+(?: +\\d+)?(?: +\\d+)? +\\d+(?: +(?:\\S.* )?\\S)$'
                        #   re_more_path = '[sdh*>irSN ][sdh*>irSN ][sdh*>irSN ]                   \\S+(?: +\\d+)?(?: +\\d+)? +\\d+(?: +(?:\\S.* )?\\S)$'

                        path_slices = {
                            'status_codes': slice(*m_network_heading.span('status_codes')),
                            'network': slice(*m_network_heading.span('network')),
                            'nexthop': slice(*m_network_heading.span('nexthop')),
                            'metric': slice(*m_network_heading.span('metric')),
                            'localpref': slice(*m_network_heading.span('localpref')),
                            'weight': slice(*m_network_heading.span('weight')),
                            'path': slice(m_network_heading.start('path'), None),
                        }

                        def extract_path_entry(line):
                            path_entry = {k: line[v].strip() or None for k, v in path_slices.items()}
                            path = path_entry.pop('path')
                            m = re.match(r'^(?:(?P<aspath>.+) )?(?P<origin_code>\S)$', path)
                            assert m, (line, path)
                            path_entry.update(m.groupdict())
                            return path_entry

                        continue

                if m_network_heading:

                    # Route Distinguisher: 192.0.0.4:0
                    # Route Distinguisher: 192.0.0.5:0 (default for vrf ES:GLOBAL)
                    # Route Distinguisher: 192.0.0.5:1 (default for vrf bd1)
                    m = re.match(r'^Route Distinguisher: (?P<rd>\S+)(?: \(default for vrf (?P<vrf>\S+)\))?$', line)
                    if m:
                        rd_entry = {
                            'rd': m.group('rd'),
                            'vrf': m.group('vrf'),
                            'networks': collections.OrderedDict(),
                        }
                        rd_key = rd_entry['rd']
                        assert rd_key not in result['rds']
                        result['rds'][rd_key] = rd_entry
                        network_entry = None
                        path_entry = None
                        continue

                    m = re.match(re_net_and_first_path, line)
                    if m:
                        path_entry = extract_path_entry(line)
                        network_entry = {
                            'network': path_entry.pop('network'),
                            'paths': collections.OrderedDict(),
                        }
                        finalize_network_entry(network_entry)
                        rd_entry['networks'][str(network_entry['network'])] = network_entry
                        finalize_path_entry(path_entry)
                        network_entry['paths'][str(path_entry['nexthop'])] = path_entry
                        continue

                    # *>i[4][0001.2222.2222.2200.000a][32][192.0.0.4]/128
                    # *> [1][192.0.0.1:1][0001.2222.2222.2200.000a][4294967295]/184
                    m = re.match(re_status_and_net, line)
                    if m:
                        line2 = lines.pop(0).rstrip()
                        #                       0.0.0.0                                0 i
                        #                       192.0.0.4                     100      0 i
                        m2 = re.match(re_continued_first_path, line2)
                        assert m2, (line, line2)
                        path_entry = extract_path_entry(line2)
                        path_entry.update(m.groupdict())
                        network_entry = {
                            'network': path_entry.pop('network'),
                            'paths': collections.OrderedDict(),
                        }
                        finalize_network_entry(network_entry)
                        rd_entry['networks'][str(network_entry['network'])] = network_entry
                        finalize_path_entry(path_entry)
                        network_entry['paths'][str(path_entry['nexthop'])] = path_entry
                        continue

                    # * i                   192.0.0.4                     100      0 i
                    m = re.match(re_more_path, line)
                    if m:
                        path_entry = extract_path_entry(line)
                        path_entry.pop('network')
                        finalize_path_entry(path_entry)
                        network_entry['paths'][str(path_entry['nexthop'])] = path_entry
                        continue

                # Processed 36 prefixes, 40 paths
                m = re.match(r'^Processed (?P<prefixes_cnt>\d+) prefixes, (?P<paths_cnt>\d+) paths$', line)
                if m:
                    result.setdefault('stats', {})
                    result['stats'].update({
                        'prefixes_cnt': int(m.group('prefixes_cnt')),
                        'paths_cnt': int(m.group('paths_cnt')),
                    })
                    continue

                logger.debug('Unmatched line: %r', line)

        return result


# ===========================================
# Parser for 'show bgp l2vpn evpn advertised'
# ===========================================

class ShowBgpL2vpnEvpnAdvertised(MetaParser):
    """Parser class for 'show bgp l2vpn evpn advertised' CLI."""

    # TODO schema

    def cli(self):
        cmd = 'show bgp l2vpn evpn advertised'.format()

        out = self.device.execute(cmd)

        result = {
            'entries': [],
        }

        attr_strings = (
            'MET',
            'ORG',
            'AS',
            'LOCAL',
            'AGG',
            'COMM',
            'ATOM',
            'EXTCOMM',
            'ATTRSET',
            'LBLIDX',
        )
        re_attr_string = r'(?:' + r'|'.join(attr_strings) + ')'

        entry = None
        for line in out.splitlines():
            line = line.rstrip()

            # [2][0][48][7777.7777.0002][0]/104 is advertised to 100.0.0.10
            m = re.match(r'^(?P<prefix>\[[^/]+\])/(?P<prefix_length>[0-9]+) is advertised to (?P<neighbor>\S+)$', line)
            if m:
                entry = m.groupdict()
                result['entries'].append(entry)
                entry.update({
                    'paths': [],
                })
                path_info = None
                attr_info = None
                continue

            #  Path info:
            m = re.match(r'^ +Path info:$', line)
            if m:
                assert 'path_info' not in entry
                path_info = entry['path_info'] = {}
                continue

            #    neighbor: Local           neighbor router id: 8.8.8.8
            m = re.match(r'^ +neighbor: (?P<neighbor>\S+) +neighbor router id: (?P<neighbor_router_id>\S+)$', line)
            if m:
                if attr_info:
                    attr_info.update(m.groupdict())
                else:
                    path_info.update(m.groupdict())
                continue

            #    valid  redistributed  best  import-candidate
            m = re.match(r'^ +(?P<flags>[A-Za-z-]+(?:  [A-Za-z-]+)*)$', line)
            if m:
                path_info['flags'] = m.group('flags').split()

            # Received Path ID 0, Local Path ID 0, version 193217
            m = re.match(r'^ *Received Path ID (?P<rx_path_id>\d+), Local Path ID (?P<local_path_id>\d+), version (?P<pelem_version>\d+)$', line)
            if m:
                path_info = m.groupdict()
                entry['paths'].append(path_info)
                continue

            #  Attributes after inbound policy was applied:
            m = re.match(r'^ *Attributes after inbound policy was applied:$', line)
            if m:
                assert 'attr_in' not in path_info
                attr_info = path_info['attr_in'] = {}
                continue

            #  Attributes after outbound policy was applied:
            m = re.match(r'^ *Attributes after outbound policy was applied:$', line)
            if m:
                assert 'attr_out' not in path_info
                attr_info = path_info['attr_out'] = {}
                continue

            #    next hop: 8.8.8.8
            m = re.match(r'^ +next hop: (?P<next_hop>\S+)$', line)
            if m:
                attr_info.update(m.groupdict())
                continue

            #    EXTCOMM
            #    ORG AS EXTCOMM
            m = re.match(r'^(?: +' + re_attr_string + r')+$', line)
            if m:
                attr_info['attributes'] = set(line.split())
                continue

            #    origin: IGP
            m = re.match(r'^ +origin: (?P<origin>.+)$', line)
            if m:
                attr_info.update(m.groupdict())
                continue

            #    aspath:
            m = re.match(r'^ +aspath: (?P<aspath>.+)$', line)
            if m:
                attr_info.update(m.groupdict())
                continue

            #    community: no-export
            m = re.match(r'^ +community: (?P<comms>.+)$', line)
            if m:
                attr_info['comms'] = m.group('comms').split()
                continue

            #    extended community: SoO:0.0.0.0:0 RT:100:7
            m = re.match(r'^ +extended community: (?P<extcomms>.+)$', line)
            if m:
                attr_info['extcomms'] = extcomms = []
                s = ' ' + m.group('extcomms')
                while s:
                    ms = re.match(' +(?P<type>[^:]+):(?P<value>[^ +]+)(?P<next_extcomm> +.+)?$', s)
                    assert ms
                    extcomm = ms.groupdict()
                    s = extcomm.pop('next_extcomm')
                    extcomms.append(extcomm)
                continue

        return result


# vim: ft=python ts=8 sw=4 et
