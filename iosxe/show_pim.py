''' show_mcast.py

IOSXE parsers for the following show commands:

    * show ipv6 pim interface
    * show ipv6 pim vrf <WROD> interface 

'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional


# =============================================
# Parser for 'show ipv6 pim interface'
# Parser for 'show ipv6 pim vrf <WROD> interface'
# =============================================

class ShowIpv6PimInterfaceSchema(MetaParser):

    # Schema for 'show ipv6 pim interface'
    # Schema for 'show ipv6 pim vrf <WROD> interface'

    schema = {'vrf': {
                Any(): {
                    'interface': {
                        Any() :{
                            'dr_priority': int,
                            'hello_interval': int,
                            'neighbor_count': int,
                            'pim_enabled': bool,
                            Optional('dr_address'): str,
                            Optional('address'): list,
                        },
                    }
                },
            }
        }

class ShowIpv6PimInterface(ShowIpv6PimInterfaceSchema):

    # Parser for 'show ipv6 pim interface'
    # Parser for 'show ipv6 pim vrf <WROD> interface'

    def cli(self, vrf=''):

        # set vrf infomation
        if vrf:
            cmd = 'show ipv6 pim vrf {} interface'.format(vrf)
        else:
            cmd = 'show ipv6 pim interface'
            vrf = 'default'

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1   on    1     30     1
            p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+) +(?P<status>(on|off))'
                             ' +(?P<nbr_count>\d+) +(?P<hello_int>\d+) +(?P<dr_pri>\d+)$')
            m = p1.match(line)
            if m:
                intf = m.groupdict()['intf']
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'interface' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interface'] = {}
                if intf not in ret_dict['vrf'][vrf]['interface']:
                    ret_dict['vrf'][vrf]['interface'][intf] = {}

                if m.groupdict()['status'].lower() == 'on':
                    ret_dict['vrf'][vrf]['interface'][intf]['pim_enabled'] = True
                else:
                    ret_dict['vrf'][vrf]['interface'][intf]['pim_enabled'] = False

                ret_dict['vrf'][vrf]['interface'][intf]['dr_priority'] = \
                    int(m.groupdict()['dr_pri'])

                ret_dict['vrf'][vrf]['interface'][intf]['hello_interval'] = \
                    int(m.groupdict()['hello_int'])

                ret_dict['vrf'][vrf]['interface'][intf]['neighbor_count'] = \
                    int(m.groupdict()['nbr_count'])
                continue

            # Address: FE80::5054:FF:FE2C:6CDF
            # Address: ::
            p2 = re.compile(r'^Address *: +(?P<address>[\s\w\:\.]+)$')
            m = p2.match(line)
            if m:
                address = m.groupdict()['address']
                if re.search('\w+', address):
                    ret_dict['vrf'][vrf]['interface'][intf]['address'] = address.split()
                continue

            # DR     : FE80::5054:FF:FEAC:64B3
            # DR     : not elected
            p3 = re.compile(r'^DR *: +(?P<dr_address>[\w\:\.]+)$')
            m = p3.match(line)
            if m:
                ret_dict['vrf'][vrf]['interface'][intf]['dr_address'] = \
                        m.groupdict()['dr_address']
                continue

        return ret_dict

# ==============================================
#  show ipv6 pim bsr candidate-rp
#  show ipv6 pim vrf <vrf_name> bsr candidate-rp
# ==============================================
class ShowIpv6PimBsrCandidateRpSchema(MetaParser):
    # show ipv6 pim bsr candidate-rp
    # show ipv6 pim vrf <vrf_name> bsr candidate-rp
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'rp': {
                            'bsr': {
                                Any(): {
                                    Optional('address'): str,
                                    Optional('holdtime'): int,
                                    Optional('priority'): int,
                                    Optional('mode'): str,
                                    Optional('interval'): int,
                                },
                                Optional('rp_candidate_next_advertisement'): str,
                            },
                        },
                    },
                },
            },
        }
    }


class ShowIpv6PimBsrCandidateRp(ShowIpv6PimBsrCandidateRpSchema):
    # Parser for 'show ipv6 pim bsr candidate-rp'
    # Parser for 'show ipv6 pim vrf <vrf_name> bsr candidate-rp'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ipv6 pim vrf {} bsr candidate-rp'.format(vrf)
        else:
            cmd = 'show ipv6 pim bsr candidate-rp'
            vrf = 'default'

        # initial variables
        ret_dict = {}
        af_name = 'ipv6'
        address = priority = holdtime = interval = mode = ""
        next_advertisement = ""

        # execute command to get output
        out = self.device.execute(cmd)

        for line in out.splitlines():
            line = line.strip()

            # PIMv2 C-RP information
            # Candidate RP: 2001:3:3:3::3 SM
            p1 = re.compile(r'^\s*Candidate RP: +(?P<candidate_rp_address>[\w\:\.]+)'
                            ' +(?P<mode>\w+)$')
            m = p1.match(line)
            if m:
                address = m.groupdict()['candidate_rp_address']
                mode = m.groupdict()['mode']
                continue

            # Priority 5, Holdtime 150
            p2 = re.compile(r'^\s*Priority +(?P<priority>\d+)'
                            ', +Holdtime +(?P<holdtime>\d+)$')
            m = p2.match(line)
            if m:
                priority = int(m.groupdict()['priority'])
                holdtime = int(m.groupdict()['holdtime'])
                continue

            # Advertisement interval 60 seconds
            p3 = re.compile(r'^\s*Advertisement +interval +(?P<interval>\d+) +seconds$')
            m = p3.match(line)
            if m:
                interval = int(m.groupdict()['interval'])
                continue

            # Next advertisement in 00:00:48
            p4 = re.compile(r'^\s*Next +advertisement +in +(?P<next_advertisement>[\d\:]+)$')
            m = p4.match(line)
            if m:
                next_advertisement = m.groupdict()['next_advertisement']
                continue

            if address:
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af_name not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af_name] = {}
                if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                if 'bsr' not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'] = {}
                if address not in ret_dict['vrf'][vrf]['address_family'] \
                    [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][address] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][address]['address'] = address

                if mode:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][address]['mode'] = mode

                if priority is not None:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']\
                        [address]['priority'] = priority

                if holdtime is not None:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']\
                        [address]['holdtime'] = holdtime

                if interval :
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']\
                        [address]['interval'] = interval
                if next_advertisement:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                        ['rp_candidate_next_advertisement'] = next_advertisement

            continue

        return ret_dict

# ==============================================
#  show ip pim interface
#  show ip pim vrf <vrf_name> interface
# ==============================================
class ShowIpPimInterfaceSchema(MetaParser):

    # Schema for 'show ip pim Interface'
    schema = {
        'vrf': {
            Any(): {
                'interfaces':{
                    Any():{
                        'address_family': {
                            Any(): {
                                Optional('dr_priority'): int,
                                Optional('hello_interval'): int,
                                Optional('neighbor_count'): int,
                                Optional('version'): int,
                                Optional('mode'): str,
                                Optional('dr_address'): str,
                                Optional('address'): list,
                            },
                        },
                    },
                },
            },
        }
    }

class ShowIpPimInterface(ShowIpPimInterfaceSchema):

    # Parser for 'show ip pim Interface'
    # Parser for 'show ip pim vrf <vrf_name> interface'
    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip pim vrf {} interface'.format(vrf)
        else:
            cmd = 'show ip pim interface'
            vrf = 'default'

        af_name = 'ipv4'

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            #Address          Interface                Ver/   Nbr    Query  DR         DR
            #                              Mode   Count  Intvl  Prior
            # 10.1.2.1         GigabitEthernet1         v2/S   1      30     1          10.1.2.2
            p1 = re.compile(r'^\s*(?P<address>[\w\:\.]+) +(?P<interface>[\w\d\S]+)'
                            ' +v(?P<version>[\d]+)\/(?P<mode>[\w]+)'
                            ' +(?P<nbr_count>[\d]+)'
                            ' +(?P<query_interval>[\d]+)'
                            ' +(?P<dr_priority>[\d]+)'
                            ' +(?P<dr_address>[\w\d\.\:]+)$')
            m = p1.match(line)
            if m:
                new_mode = ""
                address = m.groupdict()['address']
                intf_name = m.groupdict()['interface']
                nbr_count = int(m.groupdict()['nbr_count'])
                version = int(m.groupdict()['version'])
                mode = m.groupdict()['mode']
                query_interval = int(m.groupdict()['query_interval'])
                dr_priority = int(m.groupdict()['dr_priority'])
                dr_address = m.groupdict()['dr_address']

                if mode == 'S':
                    new_mode = 'sparse-mode'
                if mode == 'SD':
                    new_mode = 'sparse-dense-mode'
                if mode == 'D':
                    new_mode = 'dense-mode'

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'interfaces' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interfaces'] = {}
                if intf_name not in ret_dict['vrf'][vrf]['interfaces']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] = {}
                if intf_name not in ret_dict['vrf'][vrf]['interfaces']\
                        [intf_name]['address_family']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]\
                        ['address_family'][af_name] = {}

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name]\
                    ['address'] = address.split()
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name]\
                    ['neighbor_count'] = nbr_count
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name]\
                    ['version'] = version
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['mode'] = new_mode
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name]\
                    ['hello_interval'] = query_interval
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name]\
                    ['dr_priority'] = dr_priority
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name]\
                    ['dr_address'] = dr_address
                continue

        return ret_dict

# ==============================================
#  show ipv6 pim bsr election
#  show ipv6 pim vrf <vrf_name> bsr election
# ==============================================

class ShowIpv6PimBsrElectionSchema(MetaParser):

    # Schema for 'show ipv6 pim bsr election'
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'rp': {
                            'bsr': {
                                Optional('bsr_candidate'): {
                                    Optional('address'): str,
                                    Optional('hash_mask_length'): int,
                                    Optional('priority'): int,
                                },
                                Optional('bsr'): {
                                    Optional('address'): str,
                                    Optional('hash_mask_length'): int,
                                    Optional('scope_range_list'): str,
                                    Optional('priority'): int,
                                    Optional('up_time'): str,
                                    Optional('expires'): str,
                                    Optional('rpf_interface'): str,
                                    Optional('rpf_address'): str,

                                },
                            },
                        },
                    },
                },
            },
        },
    }
# ========================================================
#  parser for  'show ipv6 pim bsr election'
#  parser for  'show ipv6 pim vrf <vrf_name> bsr election'
# ========================================================
class ShowIpv6PimBsrElection(ShowIpv6PimBsrElectionSchema):
    # Parser for 'show ipv6 pim bsr election'
    # Parser for 'show ipv6 pim vrf <vrf_name> bsr election'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ipv6 pim vrf {} bsr election'.format(vrf)
        else:
            cmd = 'show ipv6 pim bsr election'
            vrf = 'default'

        # initial variables
        ret_dict = {}
        af_name = 'ipv6'
        address = can_address = can_hash_mask_lenght = can_priority = ""
        up_time = priority = rpf_interface = rpf_address = hash_mask = ""
        bs_timer = scope_range_list = ""

        # execute command to get output
        out = self.device.execute(cmd)

        for line in out.splitlines():
            line = line.strip()

            # BSR Election Information
            #  Scope Range List: ff00::/8
            p1 = re.compile(r'^\s*Scope +Range +List: +(?P<scope_range_list>[\w\:\.//]+)$')
            m = p1.match(line)
            if m:
                scope_range_list = m.groupdict()['scope_range_list']
                continue

            # BSR Address: 2001:1:1:1::1
            p2 = re.compile(r'^\s*BSR +Address: +(?P<bsr_address>[\w\:\.]+)$')
            m = p2.match(line)
            if m:
                address = m.groupdict()['bsr_address']
                continue

            # Uptime: 00:00:07, BSR Priority: 0, Hash mask length: 126
            p3 = re.compile(r'^\s*Uptime: +(?P<up_time>[\d\:]+),'
                            ' +BSR +Priority: +(?P<priority>\d+),'
                            ' +Hash +mask +length: +(?P<hash_mask_length>\d+)$')
            m = p3.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                priority = int(m.groupdict()['priority'])
                hash_mask = int(m.groupdict()['hash_mask_length'])
                continue

            # RPF: FE80::21E:F6FF:FE2D:3600,Loopback0
            p4 = re.compile(r'^\s*RPF: +(?P<rpf>[\w\:\.]+),(?P<interface>[\w\d\S]+)$')

            m = p4.match(line)
            if m:
                rpf_address = m.groupdict()['rpf']
                rpf_interface = m.groupdict()['interface']
                continue

            # BS Timer: 00:00:52
            p5 = re.compile(r'^\s*BS +Timer: +(?P<bs_timer>[\d\:]+)$')
            m = p5.match(line)
            if m:
                bs_timer = m.groupdict()['bs_timer']
                continue

            # Candidate BSR address: 2001:1:1:1::1, priority: 0, hash mask length: 126
            p6 = re.compile(r'^\s*Candidate +BSR +address: +(?P<can_address>[\w\d\:\.]+),'
                            ' +priority: +(?P<can_priority>\d+),'
                            ' +hash +mask +length: +(?P<can_hash_mask_lenght>\d+)$')
            m = p6.match(line)
            if m:
                can_address = m.groupdict()['can_address']
                can_priority = int(m.groupdict()['can_priority'])
                can_hash_mask_lenght = int(m.groupdict()['can_hash_mask_lenght'])
                continue

            if 'vrf' not in ret_dict:
                ret_dict['vrf'] = {}
            if vrf not in ret_dict['vrf']:
                ret_dict['vrf'][vrf] = {}
            if 'address_family' not in ret_dict['vrf'][vrf]:
                ret_dict['vrf'][vrf]['address_family'] = {}
            if af_name not in ret_dict['vrf'][vrf]['address_family']:
                ret_dict['vrf'][vrf]['address_family'][af_name] = {}
            if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
            if 'bsr' not in ret_dict['vrf'][vrf]['address_family'] \
                    [af_name]['rp']:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'] = {}

            if 'bsr' not in ret_dict['vrf'][vrf]['address_family'] \
                    [af_name]['rp']['bsr']:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr'] = {}
            if address:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['address'] = address

            if scope_range_list:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['scope_range_list'] = scope_range_list

            if up_time:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['up_time'] = up_time

            if hash_mask is not None:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['hash_mask_length'] = hash_mask
            if priority is not None:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['priority'] = priority
            if bs_timer:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['expires'] = bs_timer
            if rpf_address:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['rpf_address'] = rpf_address
            if rpf_interface:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['rpf_interface'] = rpf_interface

            if can_address:
                if 'bsr_candidate' not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bsr']['bsr_candidate'] = {}
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr_candidate']['address'] = can_address

            if can_priority is not None:
                if 'bsr_candidate' not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bsr']['bsr_candidate'] = {}
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['priority'] = can_priority

            if can_hash_mask_lenght is not None:
                if 'bsr_candidate' not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bsr']['bsr_candidate'] = {}
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['hash_mask_length'] = can_hash_mask_lenght
            continue

        return ret_dict



# ===================================================
#  schema for show ip pim rp mapping
#  schema for show ip pim vrf <vrf_name> rp mapping
# ====================================================
class ShowIpPimRpMappingSchema(MetaParser):

    # Schema for 'show ip pim rp mapping'

    schema = {'vrf':
        {Any(): {
                'address_family': {
                    Any(): {
                        'rp': {
                            'rp_mappings': {
                                Any(): {
                                    'group': str,
                                    'rp_address': str,
                                    'protocol': str,
                                    Optional('rp_address_host'): str,
                                    Optional('up_time'): str,
                                    Optional('expiration'): str,
                                    Optional('priority'): int,
                                    Optional('hold_time'): int,

                                },
                                'rp_list':{
                                    Any():{
                                        Optional('address'): str,
                                        Optional('info_source_address'): str,
                                        Optional('bsr_version'): int,
                                        Optional('up_time'): str,
                                        Optional('expiration'): str,
                                        Optional('info_source_type'): str,
                                    }
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ===================================================
#  parser for show ip pim rp mapping
#  parser for show ip pim vrf <vrf_name> rp mapping
# ====================================================
class ShowIpPimRpMapping(ShowIpPimRpMappingSchema):

    # Parser for 'show ip pim rp mapping'
    # Parser for 'show ip pim vrf <vrf_name> rp mapping'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip vrf {} rp mapping'.format(vrf)
        else:
            cmd = 'show ip pim rp mapping'
            vrf = 'default'

        protocol_static = ""
        af_name = 'ipv4'


        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Group(s) 224.0.0.0/4
            # Group(s) 224.0.0.0/4, Static
            p1 = re.compile(r'^\s*Group\(s\)\:? +(?P<group>[0-9a-zA-Z\:\.\/]+)(, +(?P<protocol>[\w\s\S]+))?$')
            m = p1.match(line)
            if m:
                rp_group_protocol = ""
                protocol_static = ""

                group = m.groupdict()['group']
                if m.groupdict()['protocol']:
                    protocol_static = m.groupdict()['protocol'].lower()
                continue

            # RP 3.3.3.3 (?), v2
            p2 = re.compile(r'^\s*RP\:? +(?P<rp_address>[\s\w\:\.]+)'
                            ' +\((?P<rp_address_host>[\w\d\.\:\?]+)\)?'
                            '(, +v(?P<rp_version>\d+))?$')
            m = p2.match(line)
            if m:
                rp_group_protocol = ""

                rp_address = m.groupdict()['rp_address']
                if m.groupdict()['rp_address_host']:
                    rp_address_host = m.groupdict()['rp_address_host']
                if m.groupdict()['rp_version']:
                    rp_version = int(m.groupdict()['rp_version'])
                if group:
                    rp_group = group + " " + rp_address
                if protocol_static:
                    rp_group_protocol = rp_group + " " + protocol_static

                if rp_group_protocol:
                    if 'vrf' not in ret_dict:
                        ret_dict['vrf'] = {}
                    if vrf not in ret_dict['vrf']:
                        ret_dict['vrf'][vrf] = {}
                    if 'address_family' not in ret_dict['vrf'][vrf]:
                        ret_dict['vrf'][vrf]['address_family'] = {}
                    if af_name not in ret_dict['vrf'][vrf]['address_family']:
                        ret_dict['vrf'][vrf]['address_family'][af_name] = {}

                    if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                    if 'rp_mappings' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'] = {}
                    if rp_group_protocol not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']['rp_mappings']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                            ['rp_mappings'][rp_group_protocol] = {}

                    if protocol_static:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['protocol'] = protocol_static
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                        ['rp_mappings'][rp_group_protocol]['group'] = group

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                        ['rp_mappings'][rp_group_protocol]['rp_address'] = rp_address
                    if m.groupdict()['rp_version']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                            ['rp_mappings'][rp_group_protocol]['rp_version'] = rp_version

                    if m.groupdict()['rp_address_host']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                            ['rp_mappings'][rp_group_protocol]['rp_address_host'] = rp_address_host
                continue

            # Info source: 4.4.4.4 (?), via bootstrap, priority 5, holdtime 150
            p3 = re.compile(r'^\s*Info +source: +(?P<info_source>[\w\:\.]+)'
                            ' +\((?P<rp_address_host>[\w\d\.\:\?]+)\)?'
                            '(, +via +(?P<protocol>[\w\S\-]+))?'
                            '(, +priority +(?P<priority>[\d]+))?'
                            '(, +holdtime +(?P<holdtime>[\d]+))?$')
            m = p3.match(line)
            if m:
                if rp_group:
                    if m.groupdict()['protocol']:
                        protocol_others = m.groupdict()['protocol'].lower().replace('-','')

                        rp_group_protocol = rp_group + " " + protocol_others

                        if 'vrf' not in ret_dict:
                            ret_dict['vrf'] = {}
                        if vrf not in ret_dict['vrf']:
                            ret_dict['vrf'][vrf] = {}
                        if 'address_family' not in ret_dict['vrf'][vrf]:
                            ret_dict['vrf'][vrf]['address_family'] = {}
                        if af_name not in ret_dict['vrf'][vrf]['address_family']:
                            ret_dict['vrf'][vrf]['address_family'][af_name] = {}

                        if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                        if 'rp_mappings' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'] = {}

                        if rp_group_protocol not in ret_dict['vrf'][vrf]['address_family'] \
                                [af_name]['rp']['rp_mappings']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                                ['rp_mappings'][rp_group_protocol] = {}

                        if m.groupdict()['info_source']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                            ['rp_mappings'][rp_group_protocol]['info_source'] = m.groupdict()['info_source']

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['protocol'] = protocol_others

                        if m.groupdict()['priority']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['priority'] = int(m.groupdict()['priority'])

                        if m.groupdict()['holdtime']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                            ['rp_mappings'][rp_group_protocol]['hold_time'] = int(m.groupdict()['holdtime'])

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['group'] = group

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['rp_address'] = rp_address

                        if rp_version:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                                ['rp_mappings'][rp_group_protocol]['rp_version'] = rp_version

                        if m.groupdict()['rp_address_host']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                                ['rp_mappings'][rp_group_protocol]['rp_address_host'] = rp_address_host
                continue

            # Uptime: 00:00:19, expires: 00:02:19
            p4 = re.compile(r'^\s*Uptime: +(?P<uptime>[\w\d\S\:]+),'
                            ' +expires: +(?P<expires>[\w\d\S\:]+)$')
            m = p4.match(line)
            if m:
                up_time = m.groupdict()['uptime']
                expiration = m.groupdict()['expires']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}

                if af_name not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af_name] = {}

                if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}

                if 'rp_mappings' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'] = {}

                if rp_group_protocol not in ret_dict['vrf'][vrf]['address_family']\
                        [af_name]['rp']['rp_mappings']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                        ['rp_mappings'][rp_group_protocol] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'][rp_group_protocol]\
                    ['up_time'] = up_time
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'][rp_group_protocol]\
                    ['expiration'] = expiration
        return ret_dict

