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
                'interfaces': {
                    Any(): {
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

# ==========================================================
# parser for  : show ip pim interface
# parser for  : show ip pim vrf <vrf_name> interface
# ==========================================================

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
            # Address          Interface                Ver/   Nbr    Query  DR         DR
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
                if intf_name not in ret_dict['vrf'][vrf]['interfaces'] \
                        [intf_name]['address_family']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name] \
                        ['address_family'][af_name] = {}

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['address'] = address.split()
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['neighbor_count'] = nbr_count
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['version'] = version
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['mode'] = new_mode
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['hello_interval'] = query_interval
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['dr_priority'] = dr_priority
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] \
                    ['dr_address'] = dr_address
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
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                            [address]['priority'] = priority

                    if holdtime is not None:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                            [address]['holdtime'] = holdtime

                    if interval:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                            [address]['interval'] = interval
                    if next_advertisement:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                            ['rp_candidate_next_advertisement'] = next_advertisement

                continue

            return ret_dict

# ==============================================
#  schema for show ipv6 pim bsr election
#  schema for show ipv6 pim vrf <vrf_name> bsr election
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
        }
    }

# ==============================================
#  parser for show ipv6 pim bsr election
#  parser for show ipv6 pim vrf <vrf_name> bsr election
# ==============================================
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

# =============================================================
# schema for : show ip pim interface detail
# schema for : show ip pim vrf <vrf_name> interface detail
# =============================================================
class ShowIpPimInterfaceDetailSchema(MetaParser):
     schema = {
         'vrf':{
             Any():{
                 'interfaces':{
                     Any():{
                         'address_family':{
                             Any():{
                                 'bfd':{
                                   Optional('enable'): bool,
                                 },
                                 Optional('hello_interval'): int,
                                 Optional('hello_packets_in'): int,
                                 Optional('hello_packets_out'): int,
                                 Optional('oper_status'): str,
                                 Optional('address'): list,
                                 Optional('multicast'):{
                                     Optional('switching'): str,
                                     Optional('packets_in'): int,
                                     Optional('packets_out'): int,
                                     Optional('ttl_threshold'): int,
                                     Optional('tag_switching'): str,
                                 },
                                 Optional('pim_status'): str,
                                 Optional('version'): int,
                                 Optional('mode'): str,
                                 Optional('dr_address'): str,
                                 Optional('neighbor_count'): int,
                                 Optional('jp_interval'): int,
                                 Optional('state_refresh_processing'): str,
                                 Optional('state_refresh_origination'): str,
                                 Optional('nbma_mode'): str,
                                 Optional('atm_multipoint_signalling'): str,
                                 Optional('domain_border'): str,
                                 Optional('neighbors_rpf_proxy_capable'): bool,
                                 Optional('none_dr_join'): bool,
                             },
                         },
                     },
                 },
             },
         },

     }
# =============================================================
# parser for : show ip pim interface detail
# parser for : show ip pim vrf <vrf_name> interface detail
# =============================================================
class ShowIpPimInterfaceDetail(ShowIpPimInterfaceDetailSchema):
    # Parser for 'show ip pim Interface detail'
    # Parser for 'show ip pim vrf <vrf_name> interface detail'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip pim vrf {} interface detail'.format(vrf)
        else:
            cmd = 'show ip pim interface detail'
            vrf = 'default'

        af_name = 'ipv4'

        # initial variables
        ret_dict = {}
        intf_name = oper_status = nbr_count = nbma_mode = hello_packet_in = ""
        hello_interval = hello_packet_out= address = dr_address = multi_packet_in= ""
        multi_packet_out = mode = version = pim_status = state_refresh_origination = ""
        state_refresh_processing = multi_switching = tagswitching = atm_multipoint = ""
        jp_interval = neighbors_rpf_proxy_capable = domain_border = bfd = ttl_threshold = ""
        non_dr_join = ""
        # excute command to get output
        out = self.device.execute(cmd)


        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet3 is up, line protocol is up
            p1 = re.compile(r'^\s*(?P<intf_name>[\w\d\S]+) +is +up,'
                            ' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                intf_name = ""
                intf_name = m.groupdict()['intf_name']
                oper_status = m.groupdict()['oper_status']

            # Internet address is 10.1.2.1/24
            p2 = re.compile(r'^\s*Internet +address +is +(?P<address>[\w\d\S]+)$')
            m = p2.match(line)
            if m:
                address = m.groupdict()['address']

            # Multicast switching: fast
            p3 = re.compile(r'^\s*Multicast +switching: +(?P<multi_switching>\w+)$')
            m = p3.match(line)
            if m:
                multi_switching = m.groupdict()['multi_switching']

            # Multicast packets in/out: 5/0
            p4 = re.compile(r'^\s*Multicast +packets +in/out:'
                            ' +(?P<in>\d+)/(?P<out>\d+)$')
            m = p4.match(line)
            if m:
                multi_packet_in = int(m.groupdict()['in'])
                multi_packet_out = int(m.groupdict()['out'])

            # Multicast TTL threshold: 0
            p5 = re.compile(r'^\s*Multicast +TTL +threshold:'
                            ' +(?P<ttl_threshold>\d+)$')
            m = p5.match(line)
            if m:
                ttl_threshold = int(m.groupdict()['ttl_threshold'])

            # PIM: enabled
            p6 = re.compile(r'^\s*PIM:'
                            ' +(?P<status>\w+)$')
            m = p6.match(line)
            if m:
                pim_status = m.groupdict()['status']

            # PIM version: 2, mode: sparse
            p7 = re.compile(r'^\s*PIM +version:'
                            ' +(?P<version>\d+), +mode: +(?P<mode>\w+)$')
            m = p7.match(line)
            if m:
                version = int(m.groupdict()['version'])
                mode = m.groupdict()['mode']

            # PIM DR: 10.1.2.2
            # PIM DR: 1.1.1.1 (this system)
            p8 = re.compile(r'^\s*PIM +DR:'
                            ' +(?P<dr_address>[\w\d\S]+)(\s+(?P<info>[\w\S\s]+))?$')
            m = p8.match(line)
            if m:
                dr_address = m.groupdict()['dr_address']

            # PIM neighbor count: 1
            p9 = re.compile(r'^\s*PIM +neighbor +count:'
                            ' +(?P<nbr_count>\d+)$')
            m = p9.match(line)
            if m:
                nbr_count = int(m.groupdict()['nbr_count'])

            # PIM Hello/Query interval: 30 seconds
            p10 = re.compile(r'^\s*PIM +[h|H]ello/[q|Q]uery +interval:'
                            ' +(?P<hello_interval>\d+) +seconds$')
            m = p10.match(line)
            if m:
                hello_interval = int(m.groupdict()['hello_interval'])

            # PIM Hello packets in/out: 8/10
            p11 = re.compile(r'^\s*PIM +Hello +packets +in/out:'
                             ' +(?P<h_in>\d+)/(?P<h_out>\d+)$')
            m = p11.match(line)
            if m:
                hello_packet_in = int(m.groupdict()['h_in'])
                hello_packet_out = int(m.groupdict()['h_out'])

            # PIM J/P interval: 60 seconds
            p12 = re.compile(r'^\s*PIM +J/P +interval:'
                             ' +(?P<jp_interval>\d+) +seconds$')
            m = p12.match(line)
            if m:
                jp_interval = int(m.groupdict()['jp_interval'])

            # PIM State-Refresh processing: enabled
            p13 = re.compile(r'^\s*PIM +[s|S]tate-[r|R]efresh +processing:'
                             ' +(?P<state_refresh_processing>\w+)$')
            m = p13.match(line)
            if m:
                state_refresh_processing = m.groupdict()['state_refresh_processing']

            # PIM State-Refresh origination: disabled
            p14 = re.compile(r'^\s*PIM +[s|S]tate-[r|R]efresh +origination:'
                             ' +(?P<state_refresh_origination>\w+)$')
            m = p14.match(line)
            if m:
                state_refresh_origination = m.groupdict()['state_refresh_origination']

            # PIM NBMA mode: disabled
            p15 = re.compile(r'^\s*PIM +NBMA +mode:'
                             ' +(?P<nbma_mode>\w+)$')
            m = p15.match(line)
            if m:
                nbma_mode = m.groupdict()['nbma_mode']

            # PIM ATM multipoint signalling: disabled
            p16 = re.compile(r'^\s*PIM +ATM +multipoint +signalling:'
                             ' +(?P<atm_multipoint>\w+)$')
            m = p16.match(line)
            if m:
                atm_multipoint = m.groupdict()['atm_multipoint']

            # PIM domain border: disabled
            p17 = re.compile(r'^\s*PIM +domain +border:'
                             ' +(?P<domain_border>\w+)$')
            m = p17.match(line)
            if m:
                domain_border = m.groupdict()['domain_border']

            # PIM neighbors rpf proxy capable: TRUE
            p18 = re.compile(r'^\s*PIM +neighbors +rpf +proxy +capable:'
                             ' +(?P<neighbors_rpf_proxy_capable>\w+)$')
            m = p18.match(line)
            if m:
                neighbors_rpf_proxy_capable = m.groupdict()['neighbors_rpf_proxy_capable']

            # PIM BFD: disabled
            p19 = re.compile(r'^\s*PIM +BFD:'
                             ' +(?P<bfd>\w+)$')
            m = p19.match(line)
            if m:
                bfd = m.groupdict()['bfd']

            # PIM Non-DR-Join: FALSE
            p20 = re.compile(r'^\s*PIM +Non-DR-Join:'
                             ' +(?P<non_dr_join>\w+)$')
            m = p20.match(line)
            if m:
                non_dr_join = m.groupdict()['non_dr_join']

            # Multicast Tagswitching: disabled
            p21 = re.compile(r'^\s*Multicast +Tagswitching:'
                             ' +(?P<tagswitching>\w+)$')
            m = p21.match(line)
            if m:
                tagswitching = m.groupdict()['tagswitching']

            if intf_name:
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
                if af_name not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'][af_name] = {}

                if bfd:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                        [af_name]['bfd'] ={}
                    if bfd.lower() == 'enabled':
                        enable = True
                    else:
                        enable = False
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['bfd']['enable'] = enable

                if hello_interval is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['hello_interval'] = hello_interval

                if hello_packet_in is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['hello_packets_in'] = hello_packet_in

                if hello_packet_out is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['hello_packets_out'] = hello_packet_out

                if oper_status:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['oper_status'] = oper_status
                if address:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['address'] = address.split()

                if multi_switching:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast']['switching'] = multi_switching

                if multi_packet_in is not None:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['packets_in'] = multi_packet_in

                if multi_packet_out is not None:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['packets_out'] = multi_packet_out

                if ttl_threshold is not None:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['ttl_threshold'] = ttl_threshold

                if tagswitching:
                    if 'multicast' not in ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]:
                        ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                            [af_name]['multicast'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast']['tag_switching'] = tagswitching

                if pim_status:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['pim_status'] = pim_status

                if version is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['version'] = version

                if mode is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['mode'] = mode

                if dr_address:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['dr_address'] = dr_address
                if nbr_count is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['neighbor_count'] = nbr_count

                if jp_interval is not None:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['jp_interval'] = jp_interval

                if  state_refresh_processing:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['state_refresh_processing'] = state_refresh_processing

                if state_refresh_origination:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['state_refresh_origination'] = state_refresh_origination

                if nbma_mode:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['nbma_mode'] = nbma_mode

                if atm_multipoint:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['atm_multipoint_signalling'] = atm_multipoint

                if  domain_border:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['domain_border'] = domain_border

                if neighbors_rpf_proxy_capable:
                    if neighbors_rpf_proxy_capable.lower() == 'true':
                        nbr_val = True
                    else:
                        nbr_val = False
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['neighbors_rpf_proxy_capable'] = nbr_val

                if non_dr_join:
                    if non_dr_join.lower() == 'true':
                        dr_join_val = True
                    else:
                        dr_join_val = False
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['none_dr_join'] = dr_join_val
                continue

        return ret_dict

