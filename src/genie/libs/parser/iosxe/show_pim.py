''' show_pim.py

IOSXE parsers for the following show commands:

    * show ipv6 pim interface
    * show ipv6 pim vrf <WORD> interface
    * show ipv6 pim bsr election
    * show ipv6 pim vrf <vrf> bsr election
    * show ipv6 pim bsr candidate-rp
    * show ipv6 pim vrf <vrf> bsr candidate-rp
    * show ip pim interface
    * show ip pim vrf <vrf> interface
    * show ip pim bsr-router
    * show ip pim vrf <vrf> bsr-router
    * show ip pim rp mapping
    * show ip pim vrf <vrf_name> rp mapping
    * show ip pim Interface detail
    * show ip pim vrf <vrf_name> interface detail
    * show ip pim neighbor
    * show ip pim [vrf <WORD>] neighbor
    * show ipv6 pim neighbor
    * show ipv6 pim [vrf <WORD>] neighbor
    * show ipv6 pim neighbor detail
    * show ipv6 pim [vrf <WORD>] neighbor detail
    * show ip pim [vrf <WORD>] interface df
    * show ip pim tunnel
    * show {addr_family} pim tunnel
    * show {addr_family} pim vrf {vrf} tunnel
    * show ip pim vrf {vrf} autorp
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


# =============================================
# Parser for 'show ipv6 pim interface'
# Parser for 'show ipv6 pim vrf <WORD> interface'
# =============================================

class ShowIpv6PimInterfaceSchema(MetaParser):
    """Schema for
        show ipv6 pim interface
        show ipv6 pim vrf <vrf> interface"""

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
    """Parser for:
        show ipv6 pim interface
        show ipv6 pim vrf <vrf> interface"""

    cli_command = ['show ipv6 pim vrf {vrf} interface','show ipv6 pim interface']
    exclude = ['(Tunnel.*)', 'address']


    def cli(self, vrf='',output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1   on    1     30     1
            p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+) +(?P<status>(on|off))'
                             r' +(?P<nbr_count>\d+) +(?P<hello_int>\d+) +(?P<dr_pri>\d+)$')
            m = p1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
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
                if re.search(r'\w+', address):
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

# ========================================================
#  schema for  'show ipv6 pim bsr election'
#  schema for  'show ipv6 pim vrf <vrf_name> bsr election'
# ========================================================
class ShowIpv6PimBsrElectionSchema(MetaParser):
    """Schema for
        show ipv6 pim bsr election
        show ipv6 pim vrf <vrf> bsr election"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'rp': {
                            'bsr': {
                                Optional('bsr_system'): str,
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
# ========================================================
#  parser for  'show ipv6 pim bsr election'
#  parser for  'show ipv6 pim vrf <vrf> bsr election'
# ========================================================
class ShowIpv6PimBsrElection(ShowIpv6PimBsrElectionSchema):
    """Parser for:
        show ipv6 pim bsr election
        show ipv6 pim vrf <vrf> bsr election"""

    cli_command = ['show ipv6 pim vrf {vrf} bsr election', 'show ipv6 pim bsr election']
    exclude = ['expires', 'up_time', 'rpf_address']


    def cli(self, vrf='', output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        af_name = 'ipv6'

        # This system is the Bootstrap Router (BSR)
        p7 = re.compile(r'^\s*This system is the Bootstrap Router \(BSR\)$')

        # This system is candidate BSR
        p8 = re.compile(r'^\s*This system is candidate BSR$')

        for line in out.splitlines():
            line = line.strip()

            # BSR Election Information
            #  Scope Range List: ff00::/8
            p1 = re.compile(r'^\s*Scope +Range +List: +(?P<scope_range_list>[\w\:\.//]+)$')
            m = p1.match(line)
            if m:
                scope_range_list = m.groupdict()['scope_range_list']
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

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['scope_range_list'] = scope_range_list
                continue

            # BSR Address: 2001:1:1:1::1
            p2 = re.compile(r'^\s*BSR +Address: +(?P<bsr_address>[\w\:\.]+)$')
            m = p2.match(line)
            if m:
                address = m.groupdict()['bsr_address']
                ret_dict['vrf'][vrf]['address_family'][af_name]\
                    ['rp']['bsr']['bsr']['address'] = address
                continue

            # Uptime: 00:00:07, BSR Priority: 0, Hash mask length: 126
            p3 = re.compile(r'^\s*Uptime: +(?P<up_time>[\d\:]+),'
                            r' +BSR +Priority: +(?P<priority>\d+),'
                            r' +Hash +mask +length: +(?P<hash_mask_length>\d+)$')
            m = p3.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                priority = int(m.groupdict()['priority'])
                hash_mask = int(m.groupdict()['hash_mask_length'])
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['up_time'] = up_time
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['hash_mask_length'] = hash_mask
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['priority'] = priority
                continue

            # RPF: FE80::21E:F6FF:FE2D:3600,Loopback0
            p4 = re.compile(r'^\s*RPF: +(?P<rpf>[\w\:\.]+),(?P<interface>[\w\d\S]+)$')

            m = p4.match(line)
            if m:
                rpf_address = m.groupdict()['rpf']
                rpf_interface = m.groupdict()['interface']
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['rpf_address'] = rpf_address
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['rpf_interface'] = rpf_interface
                continue

            # BS Timer: 00:00:52
            p5 = re.compile(r'^\s*BS +Timer: +(?P<bs_timer>[\d\:]+)$')
            m = p5.match(line)
            if m:
                bs_timer = m.groupdict()['bs_timer']
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['bsr']['expires'] = bs_timer
                continue

            # Candidate BSR address: 2001:1:1:1::1, priority: 0, hash mask length: 126
            p6 = re.compile(r'^\s*Candidate +BSR +address: +(?P<can_address>[\w\d\:\.]+),'
                            r' +priority: +(?P<can_priority>\d+),'
                            r' +hash +mask +length: +(?P<can_hash_mask_lenght>\d+)$')
            m = p6.match(line)
            if m:
                can_address = m.groupdict()['can_address']
                can_priority = int(m.groupdict()['can_priority'])
                can_hash_mask_lenght = int(m.groupdict()['can_hash_mask_lenght'])

                if 'bsr_candidate' not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bsr']['bsr_candidate'] = {}
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                    ['bsr']['bsr_candidate']['address'] = can_address

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['hash_mask_length'] = can_hash_mask_lenght

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['priority'] = can_priority
                continue

            # This system is the Bootstrap Router (BSR)
            m = p7.match(line)
            if m:
                continue
            # This system is candidate BSR
            m = p8.match(line)
            if m:
                continue


        return ret_dict

# ==============================================
#  schema for show ipv6 pim bsr candidate-rp
#  Schema for show ipv6 pim vrf <vrf_name> bsr candidate-rp
# ==============================================
class ShowIpv6PimBsrCandidateRpSchema(MetaParser):
    """schema for:
        show ipv6 pim bsr candidate-rp
        show ipv6 pim vrf <vrf> bsr candidate-rp"""
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
                                    Optional('scope'): str,
                                },
                                Optional('rp_candidate_next_advertisement'): str,
                            },
                        },
                    },
                },
            },
        }
    }

# ==============================================
#  parser for show ipv6 pim bsr candidate-rp
#  parser for show ipv6 pim vrf <vrf_name> bsr candidate-rp
# ==============================================
class ShowIpv6PimBsrCandidateRp(ShowIpv6PimBsrCandidateRpSchema):
    """Parser for:
        show ipv6 pim bsr candidate-rp
        show ipv6 pim vrf <vrf> bsr candidate-rp"""

    cli_command = ['show ipv6 pim vrf {vrf} bsr candidate-rp', 'show ipv6 pim bsr candidate-rp']
    exclude = ['rp_candidate_next_advertisement']


    def cli(self, vrf='', output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}
        af_name = 'ipv6'
        address = priority = holdtime = interval = mode = ""
        next_advertisement = scope =""

        for line in out.splitlines():
            line = line.strip()

            # PIMv2 C-RP information
            # Candidate RP: 2001:3:3:3::3 SM
            # Candidate RP: 2001:db8:100::1:1:3
            p1 = re.compile(r'^\s*Candidate RP: +(?P<candidate_rp_address>[\w\:\.]+)'
                            r'( +(?P<mode>\w+))?$')
            m = p1.match(line)
            if m:
                address = m.groupdict()['candidate_rp_address']
                mode = m.groupdict()['mode']
                continue

            # Priority 5, Holdtime 150
            # All Learnt Scoped Zones, Priority 192, Holdtime 150
            p2 = re.compile(r'^\s*((?P<scope>[\S\s]+), )?Priority +(?P<priority>\d+)'
                            r', +Holdtime +(?P<holdtime>\d+)$')
            m = p2.match(line)
            if m:
                priority = int(m.groupdict()['priority'])
                holdtime = int(m.groupdict()['holdtime'])
                if m.groupdict()['scope']:
                    scope = m.groupdict()['scope']
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

                if scope:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                        [address]['scope'] = scope


            continue

        return ret_dict

# ==============================================
#  show ip pim interface
#  show ip pim vrf <vrf_name> interface
# ==============================================
class ShowIpPimInterfaceSchema(MetaParser):
    """Schema for:
        show ip pim interface
        show ip pim vrf <vrf> interface"""
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
    """Parser for:
            show ip pim interface
            show ip pim vrf <vrf> interface"""

    cli_command = ['show ip pim vrf {vrf} interface', 'show ip pim interface']

    def cli(self, vrf='', output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        af_name = 'ipv4'

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # Address          Interface                Ver/   Nbr    Query  DR         DR
            #                              Mode   Count  Intvl  Prior
            # 10.1.2.1         GigabitEthernet1         v2/S   1      30     1          10.1.2.2
            p1 = re.compile(r'^\s*(?P<address>[\w\:\.]+) +(?P<interface>[\w\d\S]+)'
                            r' +v(?P<version>[\d]+)\/(?P<mode>[\w]+)'
                            r' +(?P<nbr_count>[\d]+)'
                            r' +(?P<query_interval>[\d]+)'
                            r' +(?P<dr_priority>[\d]+)'
                            r' +(?P<dr_address>[\w\d\.\:]+)$')
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

# ============================================
# schema for parser 'show ip pim bsr-router'
# schema for parser 'show ip pim vrf xxx bsr-router'
# ============================================
class ShowIpPimBsrRouterSchema(MetaParser):
    """Schema for:
        show ip pim bsr-router
        show ip pim vrf <vrf> bsr-router"""
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
                                Any(): {
                                    Optional('interface'): str,
                                    Optional('address'): str,
                                    Optional('holdtime'): int,
                                    Optional('next_advertisment'): str,
                                    Optional('priority'): int,
                                    Optional('interval'): int,
                                },
                                Optional('bsr'): {
                                    Optional('address'): str,
                                    Optional('hash_mask_length'): int,
                                    Optional('address_host'): str,
                                    Optional('priority'): int,
                                    Optional('up_time'): str,
                                    Optional('expires'): str,
                                },
                                Optional('bsr_next_bootstrap'): str,
                            },
                        },
                    },
                },
            },
        }
    }
# ============================================
# Parser for 'show ip pim bsr-router'
# Parser for 'show ip pim vrf xxx bsr-router'
# ============================================
class ShowIpPimBsrRouter(ShowIpPimBsrRouterSchema):
    '''Parser for:
        show ip pim bsr-router
        show ip pim vrf <vrf> bsr-router'''

    cli_command = ['show ip pim vrf {vrf} bsr-router', 'show ip pim bsr-router']
    exclude = ['next_advertisment', 'expires', 'up_time', 'bsr_next_bootstrap']

    def cli(self, vrf='', output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        af_name = 'ipv4'
        rp_can_interface = rp_can_address = rp_can_holdtime = rp_can_interval = ""
        rp_can_next_advertisment = rp_can_priority = ""


        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # PIMv2 Bootstrap information
            # BSR address: 10.64.4.4 (?)
            p1 = re.compile(r'^\s*BSR +address: +(?P<address>[\w\:\.]+) +\((?P<address_host>[\w\d\S]+)\)$')
            m = p1.match(line)
            if m:
                address = m.groupdict()['address']
                address_host = m.groupdict()['address_host']

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

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['address'] = address
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['address_host'] = address_host
                continue

            # Uptime:      00:01:23, BSR Priority: 0, Hash mask length: 0
            p2 = re.compile(r'^\s*Uptime: +(?P<up_time>[\w\d\:]+),'
                            r' +BSR +Priority: +(?P<priority>\d+),'
                            r' +Hash +mask +length: +(?P<hash_mask_length>\d+)$')
            m = p2.match(line)
            if m:
                bsr_up_time = m.groupdict()['up_time']
                bsr_priority = int(m.groupdict()['priority'])
                bsr_hash_mask = int(m.groupdict()['hash_mask_length'])

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

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['up_time'] = bsr_up_time

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['priority'] = bsr_priority

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['hash_mask_length'] = bsr_hash_mask
                continue

            # Expires:     00:01:46
            p3 = re.compile(r'^\s*Expires: +(?P<expires>[\d\:]+)$')

            m = p3.match(line)
            if m:
                bsr_expiration = m.groupdict()['expires']
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr']['expires'] = bsr_expiration
                continue

            # Next bootstrap message in 00:00:06
            p10 = re.compile(r'^\s*Next +bootstrap +message +in'
                             r' +(?P<next_bsr_message>[\w\d\S]+)$')
            m = p10.match(line)
            if m:
                next_bsr_meaasge = m.groupdict()['next_bsr_message']
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_next_bootstrap'] = next_bsr_meaasge
                continue

            # Candidate BSR address: 10.4.1.1, priority: 0, hash mask length: 0
            p4 = re.compile(r'^\s*Candidate +BSR +address: +(?P<can_address>[\w\d\:\.]+),'
                            r' +priority: +(?P<can_priority>\d+),'
                            r' +hash +mask +length: +(?P<can_hash_mask_length>\d+)$')
            m = p4.match(line)
            if m:
                can_address = m.groupdict()['can_address']
                can_priority = int(m.groupdict()['can_priority'])
                can_hash_mask = int(m.groupdict()['can_hash_mask_length'])

                if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                if 'bsr' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] = {}
                if 'bsr_candidate' not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['bsr']['bsr_candidate'] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['address'] = can_address

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['priority'] = can_priority

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['hash_mask_length'] = can_hash_mask
                continue

            # Candidate RP: 10.1.5.1(GigabitEthernet3)
            p5 = re.compile(r'^\s*Candidate +RP:'
                            r' +(?P<rp_can_address>[\w\d\.\:]+)\((?P<rp_can_interface>[\w\d\S]+)\)$')

            m = p5.match(line)
            if m:
                rp_can_address = m.groupdict()['rp_can_address']
                rp_can_interface = m.groupdict()['rp_can_interface']

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
                if 'bsr' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] = {}

                key = rp_can_interface if rp_can_interface else rp_can_address

                if key not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'][key] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['address'] = rp_can_address

                if rp_can_interface:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][key]['interface'] = rp_can_interface
                continue

            # Holdtime 150 seconds
            p6 = re.compile(r'^\s*Holdtime'
                            r' +(?P<holdtime>\d+) +seconds$')
            m = p6.match(line)
            if m:
                rp_can_holdtime = int(m.groupdict()['holdtime'])
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['holdtime'] = rp_can_holdtime
                continue

            # Advertisement interval 60 seconds
            p7 = re.compile(r'^\s*Advertisement +interval'
                            r' +(?P<interval>\d+) +seconds$')
            m = p7.match(line)
            if m:
                rp_can_interval = int(m.groupdict()['interval'])
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['interval'] = rp_can_interval
                continue

            # Next advertisement in 00:00:27
            p8 = re.compile(r'^\s*Next +advertisement +in'
                            r' +(?P<next_advertisment>[\d\:]+)$')
            m = p8.match(line)
            if m:
                rp_can_next_advertisment = m.groupdict()['next_advertisment']
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['next_advertisment'] = rp_can_next_advertisment
                continue

            # Candidate RP priority : 5
            p9 = re.compile(r'^\s*Candidate +RP +priority +:'
                            r' +(?P<rp_can_priority>[\d]+)$')
            m = p9.match(line)
            if m:
                rp_can_priority = int(m.groupdict()['rp_can_priority'])
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['priority'] = rp_can_priority
                continue

        return ret_dict

# ===================================================
#  schema for show ip pim rp mapping
#  schema for show ip pim vrf <vrf_name> rp mapping
# ====================================================
class ShowIpPimRpMappingSchema(MetaParser):
    # Schema for 'show ip pim rp mapping'
    schema = {
        'vrf':
            {Any(): {
                'address_family': {
                    Any(): {
                        'rp': {
                            'rp_mappings': {
                                Any(): {
                                    Optional('group'): str,
                                    Optional('rp_address'): str,
                                    Optional('protocol'): str,
                                    Optional('rp_address_host'): str,
                                    Optional('up_time'): str,
                                    Optional('expiration'): str,
                                    Optional('priority'): int,
                                    Optional('hold_time'): int,

                                },
                            },
                            'rp_list':{
                                Any():{
                                    Optional('address'): str,
                                    Optional('info_source_address'): str,
                                    Optional('bsr_version'): str,
                                    Optional('up_time'): str,
                                    Optional('mode'): str,
                                    Optional('expiration'): str,
                                    Optional('info_source_type'): str,
                                },
                            },
                            Optional('static_rp'):{
                                Any():{
                                    Optional('sm'): {
                                        Optional('policy_name'): str,
                                        Optional('override'): bool,
                                    },
                                    Optional('bidir'): {
                                    },
                                },
                            },
                            Optional('bsr'):{
                                'rp':{
                                    Optional('rp_address'): str,
                                    Optional('group_policy'): str,
                                    Optional('up_time'): str,
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

    cli_command = ['show ip pim vrf {vrf} rp mapping', 'show ip pim rp mapping']
    exclude = ['up_time', 'expiration']

    def cli(self, vrf='', output=None):
        if output is None:
            # set vrf infomation
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        protocol_static = ""
        af_name = 'ipv4'

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Group(s) 224.0.0.0/4
            # Group(s) 224.0.0.0/4, Static
            # Group(s): 224.0.0.0/4, Static, Bidir Mode
            p1 = re.compile(r'^\s*Group\(s\)\:? +(?P<group>[0-9a-zA-Z\:\.\/]+)'
                             r'(, +(?P<protocol>\S+))?'
                             r'(, +(?P<mode>[\w\s]+))?$')
            m = p1.match(line)
            if m:
                rp_group_protocol = ""
                acl = None

                group = m.groupdict()['group']
                if m.groupdict()['protocol']:
                    protocol_static = m.groupdict()['protocol'].lower()
                else:
                    protocol_static = ""
                mode = m.groupdict()['mode']
                if mode:
                    if 'bidir' in mode.lower():
                        mode = 'BIDIR'
                else:
                    mode = 'SM'
                continue

            # Acl: STATIC_RP_V4, Static-Override
            p1_1 = re.compile(r'^\s*Acl: +(?P<group>\S+)'
                             r'(, +(?P<protocol>\S+))?'
                             r'(, +(?P<mode>[\w\s]+))?$')
            m = p1_1.match(line)
            if m:
                rp_group_protocol = ""
                protocol_static = ""

                group = m.groupdict()['group']
                protocol = m.groupdict()['protocol']
                if protocol:
                    if 'static' in protocol.lower():
                        protocol_static = 'static'

                    if 'override' in protocol.lower():
                        override = True
                    else:
                        override = False

                mode = 'SM'
                acl = True
                continue

            # RP 10.36.3.3 (?), v2
            p2 = re.compile(r'^\s*RP\:? +(?P<rp_address>[\s\w\:\.]+)'
                            r' +\((?P<rp_address_host>[\w\d\.\:\?]+)\)?'
                            r'(, +(?P<rp_version>[\w\d]+))?$')
            m = p2.match(line)
            if m:
                rp_group_protocol = ""

                rp_address = m.groupdict()['rp_address']

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

                # static_rp
                if protocol_static and 'static' in protocol_static:

                    if acl:
                        if 'static_rp' not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                                ['static_rp'] = {}
                        if rp_address not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']['static_rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                                ['static_rp'][rp_address] = {}
                        if 'sm' not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']['static_rp'][rp_address]:
                            ret_dict['vrf'][vrf]['address_family']\
                                [af_name]['rp']['static_rp'][rp_address]['sm'] = {}

                        ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']['static_rp'][rp_address]['sm']\
                                ['policy_name'] = group
                        try:
                            ret_dict['vrf'][vrf]['address_family']\
                                [af_name]['rp']['static_rp'][rp_address]['sm']\
                                    ['override'] = override
                        except Exception:
                            pass

                    if 'bidir' in mode.lower():
                        if 'static_rp' not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                                ['static_rp'] = {}
                        if rp_address not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']['static_rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                                ['static_rp'][rp_address] = {}
                        if 'bidir' not in ret_dict['vrf'][vrf]['address_family']\
                            [af_name]['rp']['static_rp'][rp_address]:
                            ret_dict['vrf'][vrf]['address_family']\
                                [af_name]['rp']['static_rp'][rp_address]['bidir'] = {}


                if m.groupdict()['rp_address_host']:
                    rp_address_host = m.groupdict()['rp_address_host']

                if m.groupdict()['rp_version']:
                    rp_version = m.groupdict()['rp_version']

                if group:
                    rp_group = group + " " + rp_address
                if protocol_static:
                    rp_group_protocol = rp_group + " " + protocol_static

                if rp_group_protocol:
                    if 'rp_mappings' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'] = {}
                    if rp_group_protocol not in ret_dict['vrf'][vrf]['address_family'] \
                            [af_name]['rp']['rp_mappings']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol] = {}

                    if 'rp_list' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_list'] = {}

                    if protocol_static:
                        rp_address_protocol = rp_address + " " + mode + ' ' + protocol_static
                        if rp_address_protocol not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp'][
                            'rp_list']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_list'][
                                rp_address_protocol] = {}

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][rp_address_protocol]['info_source_type'] = protocol_static

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][rp_address_protocol]['address'] = rp_address

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][rp_address_protocol]['mode'] = mode

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['protocol'] = protocol_static

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mappings'][rp_group_protocol]['group'] = group

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mappings'][rp_group_protocol]['rp_address'] = rp_address

                    if m.groupdict()['rp_address_host']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['rp_address_host'] = rp_address_host
                continue

            # Info source: 10.64.4.4 (?), via bootstrap, priority 5, holdtime 150
            # Info source: 192.168.246.1 (?), elected via Auto-RP, via bootstrap, priority 0, holdtime 181
            p3 = re.compile(r'^\s*Info +source: +(?P<info_source>[\w\:\.]+)'
                            r' +\((?P<rp_address_host>[\w\d\.\:\?]+)\)?'
                            r'(, +elected +via +(?P<elected>\S+))?'
                            r'(, +via +(?P<protocol>[\w\S\-]+))?'
                            r'(, +priority +(?P<priority>[\d]+))?'
                            r'(, +holdtime +(?P<holdtime>[\d]+))?$')
            m = p3.match(line)
            if m:
                info_source_address = m.groupdict()['info_source']
                if rp_group:
                    protocol = m.groupdict()['protocol']
                    if protocol is None and  m.groupdict()['elected'] is not None:
                        protocol = m.groupdict()['elected']
                    protocol_others = protocol.lower().replace('-', '') if protocol else ''

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

                    # bsr  ---  rp
                    if 'bootstrap' in protocol_others:
                        if 'bsr' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] = {}
                        if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']['rp'] = {}
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']['rp']\
                            ['rp_address'] = rp_address
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']['rp']\
                            ['group_policy'] = group


                    if 'rp_mappings' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'] = {}

                    if rp_group_protocol not in ret_dict['vrf'][vrf]['address_family'] \
                            [af_name]['rp']['rp_mappings']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol] = {}

                    if info_source_address:
                        address_info_source_type = rp_address + " " + mode + ' ' + protocol_others

                        if 'rp_list' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                                ['rp_list'] = {}
                        if address_info_source_type not in ret_dict['vrf'][vrf]['address_family'][af_name][
                            'rp']:
                            ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                                ['rp_list'][address_info_source_type] = {}

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][address_info_source_type]['info_source_address'] \
                            = info_source_address

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][address_info_source_type]['address'] \
                            = rp_address

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][address_info_source_type]['mode'] \
                            = mode

                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][address_info_source_type]['info_source_type'] \
                            = protocol_others

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mappings'][rp_group_protocol]['protocol'] = protocol_others

                    if m.groupdict()['priority']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['priority'] = int(m.groupdict()['priority'])

                    if m.groupdict()['holdtime']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['hold_time'] = int(m.groupdict()['holdtime'])

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mappings'][rp_group_protocol]['group'] = group

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mappings'][rp_group_protocol]['rp_address'] = rp_address

                    if rp_version:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][address_info_source_type]['bsr_version'] = rp_version

                    if m.groupdict()['rp_address_host']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_mappings'][rp_group_protocol]['rp_address_host'] = rp_address_host
                continue

            # Uptime: 00:00:19, expires: 00:02:19
            p4 = re.compile(r'^\s*Uptime: +(?P<uptime>[\w\d\S\:]+),'
                            r' +expires: +(?P<expires>[\w\d\S\:]+)$')
            m = p4.match(line)
            if m:
                up_time = m.groupdict()['uptime']
                expiration = m.groupdict()['expires']

                try:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']['rp']\
                        ['up_time'] = up_time
                except Exception:
                    pass

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

                if 'rp_list' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_list'] = {}

                if rp_group_protocol not in ret_dict['vrf'][vrf]['address_family'] \
                        [af_name]['rp']['rp_mappings']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mappings'][rp_group_protocol] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'][rp_group_protocol] \
                    ['up_time'] = up_time
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mappings'][rp_group_protocol] \
                    ['expiration'] = expiration

                # the protocol is not exsited, then the address_info_source_type is not assgined
                try:
                    if address_info_source_type not in ret_dict['vrf'][vrf]['address_family'] \
                            [af_name]['rp']['rp_list']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                            ['rp_list'][address_info_source_type] = {}

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_list'][address_info_source_type] \
                        ['up_time'] = up_time
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_list'][address_info_source_type] \
                        ['expiration'] = expiration
                except Exception:
                    pass
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
                                 Optional('bfd'):{
                                   Optional('enable'): bool,
                                 },
                                 Optional('hello_interval'): int,
                                 Optional('hello_packets_in'): int,
                                 Optional('hello_packets_out'): int,
                                 Optional('oper_status'): str,
                                 Optional('enable'): bool,
                                 Optional('internet_protocol_processing'): bool,
                                 Optional('address'): list,
                                 Optional('multicast'):{
                                     Optional('switching'): str,
                                     Optional('packets_in'): int,
                                     Optional('packets_out'): int,
                                     Optional('ttl_threshold'): int,
                                     Optional('tag_switching'): bool,
                                 },
                                 Optional('pim_status'): str,
                                 Optional('version'): int,
                                 Optional('mode'): str,
                                 Optional('sm'): {
                                    Optional('passive'): bool,
                                 },
                                 Optional('dm'): {},
                                 Optional('dr_address'): str,
                                 Optional('neighbor_count'): int,
                                 Optional('jp_interval'): int,
                                 Optional('state_refresh_processing'): str,
                                 Optional('state_refresh_origination'): str,
                                 Optional('nbma_mode'): str,
                                 Optional('atm_multipoint_signalling'): str,
                                 Optional('bsr_border'): bool,
                                 Optional('neighbors_rpf_proxy_capable'): bool,
                                 Optional('none_dr_join'): bool,
                                 Optional('neighbor_filter'): str,
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

    cli_command = ['show ip pim vrf {vrf} interface detail', 'show ip pim interface detail']
    exclude = ['hello_packets_in', 'hello_packets_out', 'packets_in', 'packets_out']


    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        af_name = 'ipv4'

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet3 is up, line protocol is up
            p1 = re.compile(r'^\s*(?P<intf_name>[\w\d\S]+) +is +(?P<enable>\S+),'
                            r' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                intf_name = m.groupdict()['intf_name']
                oper_status = m.groupdict()['oper_status']
                enable = True if 'up' in m.groupdict()['enable'] else False

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

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['oper_status'] = oper_status

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['enable'] = enable
                continue

            # Internet protocol processing: disabled
            p23 = re.compile(r'^Internet protocol processing: (?P<disabled>\S+)$')
            m = p23.match(line)
            if m:

                able_val = m.groupdict()['disabled']
                able_bool = False if able_val == 'disabled' else True
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['internet_protocol_processing'] = able_bool
                continue

            # Internet address is 10.1.2.1/24
            p2 = re.compile(r'^\s*Internet +address +is +(?P<address>[\w\d\S]+)$')
            m = p2.match(line)
            if m:
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['address'] = m.groupdict()['address'].split()
                continue

            # Multicast switching: fast
            p3 = re.compile(r'^\s*Multicast +switching: +(?P<multi_switching>\w+)$')
            m = p3.match(line)
            if m:
                if 'multicast' not in ret_dict['vrf'][vrf]['interfaces']\
                    [intf_name]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                        [af_name]['multicast'] = {}
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['multicast']['switching'] = m.groupdict()['multi_switching']
                continue

            # Multicast packets in/out: 5/0
            p4 = re.compile(r'^\s*Multicast +packets +in/out:'
                            r' +(?P<in>\d+)/(?P<out>\d+)$')
            m = p4.match(line)
            if m:
                multi_packet_in = int(m.groupdict()['in'])
                multi_packet_out = int(m.groupdict()['out'])

                if 'multicast' not in ret_dict['vrf'][vrf]['interfaces']\
                    [intf_name]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast'] = {}

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['multicast']['packets_in'] = multi_packet_in

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['multicast']['packets_out'] = multi_packet_out
                continue

            # Multicast TTL threshold: 0
            p5 = re.compile(r'^\s*Multicast +TTL +threshold:'
                            r' +(?P<ttl_threshold>\d+)$')
            m = p5.match(line)
            if m:
                ttl_threshold = int(m.groupdict()['ttl_threshold'])
                if 'multicast' not in ret_dict['vrf'][vrf]['interfaces']\
                    [intf_name]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast'] = {}
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['multicast']['ttl_threshold'] = ttl_threshold
                continue

            # PIM: enabled
            p6 = re.compile(r'^\s*PIM:'
                            r' +(?P<status>\w+)$')
            m = p6.match(line)
            if m:
                pim_status = m.groupdict()['status']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['pim_status'] = pim_status
                continue

            # PIM version: 2, mode: sparse
            p7 = re.compile(r'^\s*PIM +version:'
                            r' +(?P<version>\d+), +mode: +(?P<mode>\w+)$')
            m = p7.match(line)
            if m:
                version = int(m.groupdict()['version'])
                mode = m.groupdict()['mode'].lower()

                ret_dict['vrf'][vrf]['interfaces'][intf_name]\
                    ['address_family'][af_name]['version'] = version

                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['mode'] = mode

                if mode == 'sparse':
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['sm'] = {}
                elif mode == 'dense':
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['dm'] = {}
                elif mode == 'passive':
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['sm'] = {}
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['sm']['passive'] = True
                continue

            # PIM DR: 10.1.2.2
            # PIM DR: 10.4.1.1 (this system)
            p8 = re.compile(r'^\s*PIM +DR:'
                            r' +(?P<dr_address>[\w\d\S]+)(\s+(?P<info>[\w\S\s]+))?$')
            m = p8.match(line)
            if m:
                dr_address = m.groupdict()['dr_address']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['dr_address'] = dr_address
                continue

            # PIM neighbor count: 1
            p9 = re.compile(r'^\s*PIM +neighbor +count:'
                            r' +(?P<nbr_count>\d+)$')
            m = p9.match(line)
            if m:
                nbr_count = int(m.groupdict()['nbr_count'])
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['neighbor_count'] = nbr_count
                continue

            # PIM Hello/Query interval: 30 seconds
            p10 = re.compile(r'^\s*PIM +[h|H]ello/[q|Q]uery +interval:'
                            r' +(?P<hello_interval>\d+) +seconds$')
            m = p10.match(line)
            if m:
                hello_interval = int(m.groupdict()['hello_interval'])
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['hello_interval'] = hello_interval
                continue

            # PIM Hello packets in/out: 8/10
            p11 = re.compile(r'^\s*PIM +Hello +packets +in/out:'
                             r' +(?P<h_in>\d+)/(?P<h_out>\d+)$')
            m = p11.match(line)
            if m:
                hello_packet_in = int(m.groupdict()['h_in'])
                hello_packet_out = int(m.groupdict()['h_out'])
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['hello_packets_in'] = hello_packet_in
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['hello_packets_out'] = hello_packet_out
                continue

            # PIM J/P interval: 60 seconds
            p12 = re.compile(r'^\s*PIM +J/P +interval:'
                             r' +(?P<jp_interval>\d+) +seconds$')
            m = p12.match(line)
            if m:
                jp_interval = int(m.groupdict()['jp_interval'])
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['jp_interval'] = jp_interval
                continue

            # PIM State-Refresh processing: enabled
            p13 = re.compile(r'^\s*PIM +[s|S]tate-[r|R]efresh +processing:'
                             r' +(?P<state_refresh_processing>\w+)$')
            m = p13.match(line)
            if m:
                state_refresh_processing = m.groupdict()['state_refresh_processing']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['state_refresh_processing'] = state_refresh_processing
                continue

            # PIM State-Refresh origination: disabled
            p14 = re.compile(r'^\s*PIM +[s|S]tate-[r|R]efresh +origination:'
                             r' +(?P<state_refresh_origination>\w+)$')
            m = p14.match(line)
            if m:
                state_refresh_origination = m.groupdict()['state_refresh_origination']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['state_refresh_origination'] = state_refresh_origination
                continue

            # PIM NBMA mode: disabled
            p15 = re.compile(r'^\s*PIM +NBMA +mode:'
                             r' +(?P<nbma_mode>\w+)$')
            m = p15.match(line)
            if m:
                nbma_mode = m.groupdict()['nbma_mode']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['nbma_mode'] = nbma_mode
                continue

            # PIM ATM multipoint signalling: disabled
            p16 = re.compile(r'^\s*PIM +ATM +multipoint +signalling:'
                             r' +(?P<atm_multipoint>\w+)$')
            m = p16.match(line)
            if m:
                atm_multipoint = m.groupdict()['atm_multipoint']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['atm_multipoint_signalling'] = atm_multipoint
                continue

            # PIM domain border: disabled
            p17 = re.compile(r'^\s*PIM +domain +border:'
                             r' +(?P<domain_border>\w+)$')
            m = p17.match(line)
            if m:
                bsr_border = m.groupdict()['domain_border']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['bsr_border'] = False if 'disabled' in bsr_border else True
                continue

            # PIM neighbors rpf proxy capable: TRUE
            p18 = re.compile(r'^\s*PIM +neighbors +rpf +proxy +capable:'
                             r' +(?P<neighbors_rpf_proxy_capable>\w+)$')
            m = p18.match(line)
            if m:
                nbr_val = m.groupdict()['neighbors_rpf_proxy_capable']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['neighbors_rpf_proxy_capable'] = True if nbr_val.lower() == 'true' \
                                                               else False
                continue

            # PIM BFD: disabled
            p19 = re.compile(r'^\s*PIM +BFD:'
                             r' +(?P<bfd>\w+)$')
            m = p19.match(line)
            if m:
                bfd = m.groupdict()['bfd']
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family']\
                    [af_name]['bfd'] ={}
                if bfd.lower() == 'enabled':
                    enable = True
                else:
                    enable = False
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['bfd']['enable'] = enable

            # PIM Non-DR-Join: FALSE
            p20 = re.compile(r'^\s*PIM +Non-DR-Join:'
                             r' +(?P<non_dr_join>\w+)$')
            m = p20.match(line)
            if m:
                non_dr_join = m.groupdict()['non_dr_join']
                if non_dr_join.lower() == 'true':
                    dr_join_val = True
                else:
                    dr_join_val = False
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['none_dr_join'] = dr_join_val
                continue

            # Multicast Tagswitching: disabled
            p21 = re.compile(r'^\s*Multicast +Tagswitching:'
                             r' +(?P<tagswitching>\w+)$')
            m = p21.match(line)
            if m:
                tagswitching = m.groupdict()['tagswitching']
                if 'multicast' not in ret_dict['vrf'][vrf]['interfaces']\
                    [intf_name]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                        [af_name]['multicast'] = {}
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['multicast']['tag_switching'] = False if 'disabled' \
                                                              in tagswitching else True
                continue

            # PIM neighbor filter: 7
            p22 = re.compile(r'^\s*PIM +neighbor +filter: +(?P<nei_filter>\d+)$')
            m = p22.match(line)
            if m:
                ret_dict['vrf'][vrf]['interfaces'][intf_name]['address_family'] \
                    [af_name]['neighbor_filter'] = m.groupdict()['nei_filter']
                continue

        return ret_dict


# ===========================================================
# schema Parser for 'show ip/ipv6 pim [vrf <WORD>] neighbor'
# ===========================================================
class ShowPimNeighborSchema(MetaParser):

    '''Schema for show ip/ipv6 pim [vrf <WORD>] neighbor'''

    schema = {
        'vrf':{
            Any():{
                'interfaces':{
                    Any():{
                        'address_family':{
                            Any():{
                                'neighbors':{
                                    Any():{
                                        Optional('expiration'): str,
                                        Optional('dr_priority'): int,
                                        Optional('up_time'): str,
                                        Optional('interface'): str,
                                        Optional('bidir_capable'): bool,
                                        Optional('designated_router'): bool,
                                        Optional('default_dr_prioirty'): bool,
                                        Optional('proxy_capable'): bool,
                                        Optional('state_refresh_capable'): bool,
                                        Optional('genid_capable'): bool,
                                        Optional('dr_load_balancing_capable'): bool,
                                        Optional('version'): str,
                                    },
                                    Optional('secondary_address'): list, # only for IPv6
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
# Parser Parser for 'show ip/ipv6 pim [vrf <WORD>] neighbor'
# Parser Parser for 'show ipv6 pim [vrf <WORD>] neighbor detail'
# ==========================================================
class ShowPimNeighbor(ShowPimNeighborSchema):
    '''Parser for show ip/ipv6 pim [vrf <WORD>] neighbor
                  show ipv6 pim [vrf <word>] neighbor detail'''

    cli_command = ['show {af} pim vrf {vrf} neighbor', 'show {af} pim neighbor']
    exclude = ['expiration', 'up_time']

    def cli(self, af='ip', vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(af=af, vrf=vrf)
            else:
                cmd = self.cli_command[1].format(af=af)
            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv4' if af == 'ip' else af
        vrf = 'default' if not vrf else vrf

        # Init dictionary
        ret_dict = {}
        sub_dict = {}

        # mode key mapping table
        mode_tbl = {'B': 'bidir_capable',
                    'DR': 'designated_router',
                    'N': 'default_dr_prioirty',
                    'P': 'proxy_capable',
                    'S': 'state_refresh_capable',
                    'G': 'genid_capable',
                    'L': 'dr_load_balancing_capable'}
        for line in out.splitlines():
            line = line.strip()

            # Neighbor          Interface                Uptime/Expires    Ver   DR
            # Address                                                            Prio/Mode
            # 192.168.154.1      Port-channel2.100       1d09h/00:01:39    v2    1 / S P G
            # 172.19.1.64       LISP0.4099               4d23h/00:01:11    v2    0 /
            p1 = re.compile(r'^(?P<nei_address>[\d\.]+) +'
                            r'(?P<intf>[\w\.\/\-]+) +'
                            r'(?P<uptime>[\w\.\:]+)\/(?P<expires>[\w\.\:]+) +'
                            r'(?P<ver>\w+) +'
                            r'(?P<dr_prio>\d+) *\/ *(?P<mode>[\w\s]+)?$')
            m1 = p1.match(line)

            # Neighbor Address           Interface          Uptime    Expires  Mode DR pri
            # FE80::21A:30FF:FE47:6EC1   Port-channel2.100  1d09h     00:01:17 B G     1
            # ::FFFF:4.4.4.4             Tunnel8            1d00h     00:01:31 B G     1
            p2 = re.compile(r'^(?P<nei_address>[\w\:.]+) +'
                            r'(?P<intf>[\w\.\/\-]+) +'
                            r'(?P<uptime>[\w\.\:]+) +'
                            r'(?P<expires>[\w\.\:]+) +'
                            r'(?P<mode>[\w\s]+) +'
                            r'(?P<dr_prio>\d+)$')
            m2 = p2.match(line)

            if m := m1 or m2:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                nei = m.groupdict()['nei_address']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'interfaces' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['interfaces'] = {}
                if intf not in ret_dict['vrf'][vrf]['interfaces']:
                    ret_dict['vrf'][vrf]['interfaces'][intf] = {}

                if 'address_family' not in ret_dict['vrf'][vrf]['interfaces'][intf]:
                    ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['interfaces'][intf]['address_family']:
                    ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'][af] = {}

                if 'neighbors' not in ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'][af]['neighbors'] = {}
                if nei not in ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'][af]['neighbors']:
                    ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'][af]['neighbors'][nei] = {}

                sub_dict = ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'][af]['neighbors'][nei]

                sub_dict['expiration'] = m.groupdict()['expires']
                sub_dict['dr_priority'] = int(m.groupdict()['dr_prio'])
                sub_dict['up_time'] = m.groupdict()['uptime']
                sub_dict['interface'] = intf
                try:
                    sub_dict['version'] = m.groupdict()['ver']
                except Exception:
                    pass

                mode_list = m.groupdict()['mode']
                if mode_list:
                    for mode in mode_list.strip().split():
                        sub_dict[mode_tbl[mode]] = True
                continue

            # 2001::2:1
            p3 = re.compile(r'^(?P<secondary_address>[\w\:]+)$')
            m = p3.match(line)
            if m:
                ret_dict['vrf'][vrf]['interfaces'][intf]['address_family'\
                    ][af]['neighbors']['secondary_address'] = m.groupdict()['secondary_address'].split()
                continue

        return ret_dict


# ==========================================================
#  parser for 'show ip pim [vrf <WORD>] neighbor'
# ==========================================================
class ShowIpPimNeighbor(ShowPimNeighbor):
    '''Parser for show ip pim [vrf <WORD>] neighbor'''
    cli_command = ['show ip pim vrf {vrf} neighbor', 'show ip pim neighbor']
    exclude = ['expiration', 'up_time']

    def cli(self, vrf='',output=None):
         # ip should be ip or ipv6
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(af='ip', vrf=vrf, output=out)

# ==========================================================
#  parser for 'show ipv6 pim [vrf <WORD>] neighbor'
# ==========================================================
class ShowIpv6PimNeighbor(ShowPimNeighbor):
    '''Parser for show ipv6 pim [vrf <WORD>] neighbor'''
    cli_command = ['show ipv6 pim vrf {vrf} neighbor', 'show ipv6 pim neighbor']
    exclude = ['expiration', 'up_time']

    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(af='ipv6', vrf=vrf,output=out)


# ==========================================================
#  parser for 'show ipv6 pim [vrf <WORD>] neighbor detail'
# ==========================================================
class ShowIpv6PimNeighborDetail(ShowPimNeighbor):
    '''Parser for show ipv6 pim [vrf <WORD>] neighbor detail'''
    cli_command = ['show ipv6 pim vrf {vrf} neighbor detail', 'show ipv6 pim neighbor detail']
    exclude = ['expiration', 'up_time']


    def cli(self, vrf='',output=None):
         # ip should be ip or ipv6
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(af='ipv6', vrf=vrf,output=out)


# ===========================================================
# schema Parser for 'show ip pim [vrf <WORD>] interface df'
# ===========================================================
class ShowIpPimInterfaceDfSchema(MetaParser):

    '''Schema for show ip pim [vrf <WORD>] interface df'''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('rp'): {
                            Optional('bidir'): {
                                Optional('interface_df_election'): {
                                    Any(): {
                                        Optional('address'): str,
                                        Optional('metric'): int,
                                        Optional('interface_name'): str,
                                        Optional('df_address'): str,
                                        Optional('df_uptime'): str,
                                        Optional('winner_metric'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
# Parser Parser for 'show ip pim [vrf <WORD>] interface df'
# ==========================================================
class ShowIpPimInterfaceDf(ShowIpPimInterfaceDfSchema):
    '''Parser for show ip pim [vrf <WORD>] interface df'''

    cli_command = ['show ip pim vrf {vrf} interface df', 'show ip pim interface df']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        af= 'ipv4'
        vrf = 'default' if not vrf else vrf

        # Init dictionary
        ret_dict = {}
        sub_dict = {}

        intf = None

        for line in out.splitlines():
            line = line.strip()

            # Interface          RP               DF Winner        Metric          Uptime
            # Ethernet3/3        10.10.0.2        10.4.0.2         0               00:03:49
            #                    10.10.0.3        10.4.0.3         0               00:01:49
            # Ethernet0/1        10.186.0.1      *10.4.0.4         20              00:00:39
            p1 = re.compile(r'^((?P<intf>[\w\.\/\-]+) +)?'
                             r'(?P<address>[\w\.\:]+) +'
                             r'(?P<df>\*)?(?P<df_address>[\w\.\:]+) +'
                             r'(?P<metric>\d+) +'
                             r'(?P<uptime>[\w\.\:]+)$')
            m = p1.match(line)
            if m:
                if m.groupdict()['intf']:
                    intf = m.groupdict()['intf']
                address = m.groupdict()['address']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}

                if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['rp'] = {}
                if 'bidir' not in ret_dict['vrf'][vrf]['address_family'][af]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af]['rp']['bidir'] = {}
                if 'interface_df_election' not in ret_dict['vrf'][vrf]\
                    ['address_family'][af]['rp']['bidir']:
                    ret_dict['vrf'][vrf]['address_family'][af]['rp']\
                        ['bidir']['interface_df_election'] = {}

                if intf:
                    key = address + ' ' + intf
                    if key not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['rp']['bidir']['interface_df_election']:
                        ret_dict['vrf'][vrf]['address_family'][af]['rp']\
                            ['bidir']['interface_df_election'][key] = {}
                        sub_dict = ret_dict['vrf'][vrf]['address_family'][af]['rp']\
                            ['bidir']['interface_df_election'][key]
                        sub_dict['interface_name'] = intf

                sub_dict['address'] = address
                sub_dict['metric'] = int(m.groupdict()['metric'])
                sub_dict['df_address'] = m.groupdict()['df_address']
                sub_dict['df_uptime'] = m.groupdict()['uptime']
                sub_dict['winner_metric'] = int(m.groupdict()['metric'])
                continue
        return ret_dict

# ========================================================
# Parser for 'show ip pim tunnel'
# ========================================================

class ShowIpPimTunnelSchema(MetaParser):
    """
    Schema for 'show ip pim tunnel'
    Schema for 'show {addr_family} pim tunnel'
    Schema for 'show {addr_family} pim vrf {vrf} tunnel'
    """

    schema = {
        'tunnels': {
            Any(): {
                'type': str,
                'rp': str,
                'source': str,
                Optional('state') : str,
                Optional('last_event'): str,
                Optional('uptime'): str
            },
        }
    }


class ShowIpPimTunnel(ShowIpPimTunnelSchema):
    """
    Parser for 'show ip pim tunnel'
    Parser for 'show {addr_family} pim tunnel'
    Parser for 'show {addr_family} pim vrf {vrf} tunnel'
    """
    cli_command = ['show ip pim tunnel', 'show {addr_family} pim tunnel', 'show {addr_family} pim vrf {vrf} tunnel']

    def cli(self, output=None, addr_family=None, vrf=None):
        if output is None:
            if addr_family and vrf:
                cmd = self.cli_command[2].format(addr_family = addr_family, vrf = vrf)
            elif addr_family:
                cmd = self.cli_command[1].format(addr_family = addr_family)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        ret_dict = {}

        #Tunnel0
        p1 = re.compile(r'Tunnel(?P<tunnel>\d+)')

        #Type       : PIM Encap
        p2 = re.compile(r'^Type\s+\:\s+(?P<type>.*)$')

        #RP         : 4.4.4.4
        #RP    : Embedded RP Tunnel
        p3 = re.compile(r'^RP\s+\:\s+(?P<rp>.*)$')

        #Source     : 87.1.1.1
        #Source: 77:77:77::77
        p4 = re.compile(r'^Source(\s+)?\:\s+(?P<source>\S+)$')

        #State      : UP
        p5 = re.compile(r'^State\s+\:\s+(?P<state>\S+)$')

        #Last event : RP address reachable (1d10h)
        p6 = re.compile(r'^Last\s+event\s+:\s+(?P<last_event>(.*?))\s+\((?P<uptime>\S+)\)$')

        for line in out.splitlines():
            line = line.strip()

            #Tunnel0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tunnel = group['tunnel']
                intf_dict = ret_dict.setdefault('tunnels', {})
                intf_dict[tunnel] = {}

            #Type       : PIM Encap
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict[tunnel]['type'] = group['type']
                continue

            #RP         : 4.4.4.4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict[tunnel]['rp'] = group['rp']
                continue

            #Source     : 87.1.1.1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict[tunnel]['source'] = group['source']
                continue

            #State      : UP
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict[tunnel]['state'] = group['state']
                continue

            #Last event : RP address reachable (1d10h)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf_dict[tunnel]['last_event'] = group['last_event']
                intf_dict[tunnel]['uptime'] = group['uptime']
                continue

        return ret_dict


# ==========================================================
# Schema Parser for 'show ip pim vrf {vrf ID} autorp'
# ==========================================================
class ShowIpPimAutorpSchema(MetaParser):
    """Schema for 'show ip pim vrf {vrf ID} autorp' """

    schema = {
        "autorp" : str,
        "mtu" : str,
        "group": str,
        "interface" : str,
        "mode" : str,
        "rp_announce_sent" : str,
        "rp_announce_received" : str,
        "rp_discovery_sent" : str,
        "rp_discovery_received" : str,
    }

# =======================================================================
# Parser for 'show ip pim vrf {vrf ID} autorp'
# =======================================================================
class ShowIpPimAutorp(ShowIpPimAutorpSchema):
    """parser for 'show ip pim vrf {vrf ID} autorp' """

    cli_command = "show ip pim vrf {vrf_ID} autorp"

    def cli(self, vrf_ID='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf_ID=vrf_ID))
        else:
            output = output

        ret_dict = {}

        #AutoRP is enabled.
        p1 = re.compile(r'^\s*AutoRP\s+is\s*(?P<autorp>\w+).+$')

        #RP Discovery packet MTU is 1496.
        p2 = re.compile(r'^\s*RP\s+Discovery\s+packet\s+MTU\s+is\s+(?P<mtu>\d+).+$')

        #224.0.1.40 is joined on Loopback0.
        p3 = re.compile(r'^\s*(?P<group>\d+.\d+.\d+.\d+)\s+is\s+joined\s+on\s+(?P<interface>[\w\/\.\-\:]+).+$')

        #AutoRP groups over sparse mode interface is enabled
        p4 = re.compile(r'^\s*AutoRP\s+groups\s+over\s+(?P<mode>\w+)\s+mode\s+interface\s+is\s+enabled$')

        #RP Announce: 3078/1303, RP Discovery: 3780/10412
        p5 = re.compile(r'^\s*RP\s+Announce:\s+(?P<rpas>\d+)\/(?P<rpar>\d+),\s+RP Discovery:\s+(?P<rpds>\d+)\/(?P<rpdr>\d+)$')

        for line in output.splitlines():
            if not line:
                continue

            #AutoRP is enabled.
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['autorp'] = groups['autorp']
                continue

            #RP Discovery packet MTU is 1496.
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['mtu'] = groups['mtu']
                continue

            #224.0.1.40 is joined on Loopback0.
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['group'] = groups['group']
                ret_dict['interface'] = groups['interface']
                continue

            #AutoRP groups over sparse mode interface is enabled
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['mode'] = groups['mode']
                continue

            #RP Announce: 3078/1303, RP Discovery: 3780/10412
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['rp_announce_sent'] = groups['rpas']
                ret_dict['rp_announce_received'] = groups['rpar']
                ret_dict['rp_discovery_sent'] = groups['rpds']
                ret_dict['rp_discovery_received'] = groups['rpdr']
                continue

        return ret_dict


# ===========================================================
# schema Parser for 'show ip pim vrf {vrf id} mdt bgp'
# ===========================================================
class ShowIpPimVrfMdtBgpSchema(MetaParser):
    """Schema for:
        show ip pim vrf {vrf} mdt bgp"""

    schema = {
        'mdt': {
            Any(): {
                Optional('rid'): str,
                Optional('next_hop'): str,
            }
        }
    }


# ===========================================================
# Parser for 'show ip pim vrf {vrf id} mdt bgp'
# ===========================================================
class ShowIpPimVrfMdtBgp(ShowIpPimVrfMdtBgpSchema):
    """Parser for:
        show ip pim vrf {vrf} mdt bgp"""

    cli_command = 'show ip pim vrf {vrf} mdt bgp'

    def cli(self, vrf='', output=None):
        if output is None:
            cmd = self.cli_command.format(vrf=vrf)
            output = self.device.execute(cmd)

        ret_dict = {}

        # MDT-default group 232.2.1.4
        p1 = re.compile(r'^MDT-default group (?P<mdt_default_group>[\d\.]+)$')

        # rid:1.1.1.1 next_hop:1.1.1.1
        p2 = re.compile(r'^rid:(?P<rid>[\d\.]+) +next_hop:(?P<next_hop>[\d\.]+)$')

        for line in output.splitlines():
            line = line.strip()

            # MDT-default group
            m = p1.match(line)
            if m:
                mdt_default_group = m.group('mdt_default_group')

                # Build VRF and MDT group structure
                mdt_dict = ret_dict.setdefault('mdt', {}).setdefault(mdt_default_group, {})
                continue

            # RID and next hop
            m = p2.match(line)
            if m:
                mdt_dict['rid'] = m.group('rid')
                mdt_dict['next_hop'] = m.group('next_hop')
                continue

        return ret_dict


# ==========================================================
# Schema Parser for 'show ip pim vrf {vrf_name} mdt send'
# ==========================================================
class ShowIpPimVrfMdtSendSchema(MetaParser):
    """Schema for 'show ip pim vrf {vrf_name} mdt send' """

    schema = {
        'mdt' : {
            Any(): {
                'source':str,
                'group':str,
                'mdt_data_group':str,
                'ref_count':int
            }
        }
    }


# =======================================================================
# Parser for 'show ip pim vrf {vrf_name} mdt send'
# =======================================================================
class ShowIpPimVrfMdtSend(ShowIpPimVrfMdtSendSchema):
    """Parser for 'show ip pim vrf {vrf} mdt send' """

    cli_command = "show ip pim vrf {vrf} mdt send"

    def cli(self, vrf='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        ret_dict = {}
        index=0
        # (source, group)             MDT-data group   ref_count
        # (10.100.8.10, 225.1.8.1)      232.2.8.0       1
        # (10.100.8.10, 225.1.8.2)      232.2.8.1       1
        # (10.100.8.10, 225.1.8.3)      232.2.8.2       1
        # (10.100.8.10, 225.1.8.4)      232.2.8.3       1
        # (10.100.8.10, 225.1.8.5)      232.2.8.4       1
        # (10.100.8.10, 225.1.8.6)      232.2.8.5       1
        # (10.100.8.10, 225.1.8.7)      232.2.8.6       1
        # (10.100.8.10, 225.1.8.8)      232.2.8.7       1
        # (10.100.8.10, 225.1.8.9)      232.2.8.8       1
        # (10.100.8.10, 225.1.8.10)     232.2.8.9       1

        p1 = re.compile(r'\((?P<source>[\d\.]+),\s+(?P<group>[\d\.]+)\)\s+(?P<mdt_data_group>[\d\.]+)\s+(?P<ref_count>\d+)')

        for line in output.splitlines():
            line = line.strip()

            #  source: 10.100.8.10  group: 225.1.8.1)    mdt_data_group: 232.2.8.0     ref_count: 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                if 'mdt' not in ret_dict:
                    ret_dict['mdt'] = {}
                sub_dict = ret_dict['mdt'].setdefault(index, {})
                sub_dict['source'] = groups['source']
                sub_dict['group'] = groups['group']
                sub_dict['mdt_data_group'] = groups['mdt_data_group']
                sub_dict['ref_count'] = int(groups['ref_count'])
                index+=1
                continue

        return ret_dict


# =================================================================
# Schema Parser for 'show ip pim vrf {vrf ID} mdt receive detail'
# =================================================================
class ShowIpPimVrfMdtReceiveDetailSchema(MetaParser):
    """Schema for 'show ip pim vrf {vrf} mdt receive detail'  """

    schema = {
        'data_mdt_source': str,
        'data_mdt_group': str,
        'reference_count': int,
        'source_group_pairs' : {
            Any() : {
                'source': str,
                'group': str,
                'oif_count': int,
                'flags':str
            }
        }
    }


# =================================================================
# Parser for 'show ip pim vrf {vrf ID} mdt receive detail'
# =================================================================
class ShowIpVrfMdtReceiveDetail(ShowIpPimVrfMdtReceiveDetailSchema):
    """Parser for 'show ip pim vrf {vrf} mdt receive detail'  """

    cli_command = 'show ip pim vrf {vrf} mdt receive detail'

    def cli(self, vrf='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        #   group:172.16.8.0 source:10.0.0.100 ref_count:13
        #  (10.101.8.10, 225.1.8.1), 1d13h/00:03:28/00:02:26, OIF count:1, flags:TY
        #  (10.102.8.10, 225.1.8.1), 1d13h/00:03:28/00:02:27, OIF count:1, flags:TY

        ret_dict = {}
        index= 0

        # group:172.16.8.0 source:10.0.0.100 ref_count:13
        p1 = re.compile(r'^\s*group\:(?P<group>\S+)\s+source\:(?P<source>\S+)\s+ref_count\:(?P<ref_count>\d+)$')

        # (10.101.8.10, 225.1.8.1), 1d13h/00:03:28/00:02:26, OIF count:1, flags:TY
        p2 = re.compile(r'^\((?P<source>\S+), +(?P<group>\S+)\), +\S+/+\S+/+\S+, +OIF +count:(?P<oif_count>\d+), +flags:(?P<flags>\S+)$')

        for line in output.splitlines():
            if not line:
                continue

            # group: 172.16.8.0  source: 10.0.0.100   ref_count: 13
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['data_mdt_group'] = groups['group']
                ret_dict['data_mdt_source'] = groups['source']
                ret_dict['reference_count'] = int(groups['ref_count'])
                continue

            # (10.102.8.10, 225.1.8.1),  1d13h/00:03:28/00:02:27,  OIF count:1,  flags:TY
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                source_group_pairs = ret_dict.setdefault('source_group_pairs', {})
                source_group_pairs[index] = {
                    'source': groups['source'],
                    'group': groups['group'],
                    'oif_count': int(groups['oif_count']),
                    'flags': groups['flags']
                }
                index += 1
                continue

        return ret_dict



# ==============================================================================
# Schema Parser for 'show ip pim vrf {vrf id} mdt history interval {interval}
# ==============================================================================
class ShowIpPimVrfMdtHistoryIntervalSchema(MetaParser):
    """Schema for:
        show ip pim vrf {vrf} mdt history interval {interval}"""
    schema = {
            'mdt_data_groups': {
                Any() : {
                    'mdt_data_group' : str,
                    'no_of_reuse' : int
                }
            }
        }


# ==============================================================================
# Parser for 'show ip pim vrf {vrf id} mdt history interval {interval}
# ==============================================================================
class ShowIpPimVrfMdtHistoryInterval(ShowIpPimVrfMdtHistoryIntervalSchema):
    """Parser for:
        show ip pim vrf {vrf} mdt history interval {interval}"""

    cli_command = 'show ip pim vrf {vrf} mdt history interval {interval}'

    def cli(self, vrf, interval, output=None):
        if output is None:
            cmd = self.cli_command.format(vrf=vrf, interval=interval)
            output = self.device.execute(cmd)

        ret_dict = {}
        index=0

        # MDT-data group        Number of reuse
        #     10.9.9.8           3
        #     10.9.9.9           2
        p1 = re.compile(r'^(?P<mdt_data_group>[\d\.]+)\s+(?P<no_of_reuse>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # MDT-data group, Number of reuse
            m = p1.match(line)
            if m:
                group = m.groupdict()

                mdt_data_group_dict = ret_dict.setdefault('mdt_data_groups', {})
                sub_dict = mdt_data_group_dict.setdefault(index, {})
                index += 1
                sub_dict['mdt_data_group'] = group['mdt_data_group']
                sub_dict['no_of_reuse'] = int(group['no_of_reuse'])

        return ret_dict


# ==============================================================================
# Schema Parser for 'show ip pim mdt receive'
# ==============================================================================
class ShowIpPimMdtReceiveSchema(MetaParser):
    """Schema for:
        show ip pim mdt receive"""
    schema = {
       'data_mdt_group' : {
            Any() : {
                    Optional('source') : str,
                    Optional('up_time') : str,
                    Optional('expires') : str,
            }
        }
    }

# ==============================================================================
# Parser for 'show ip pim mdt receive'
# ==============================================================================
class ShowIpPimMdtReceive(ShowIpPimMdtReceiveSchema):
    """Parser for:
        show ip pim mdt receive"""

    cli_command = 'show ip pim mdt receive'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Data MDT group:
        #  [239.192.20.32 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.33 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.34 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.35 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.36 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.37 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.38 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.39 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.40 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.41 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.42 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.43 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.44 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.45 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.46 : 2.2.2.2]  00:01:25/00:02:34
        #  [239.192.20.47 : 2.2.2.2]  00:01:25/00:02:34

        p1 = re.compile(r'^\s*\[(?P<data_mdt_group>\d+\.\d+\.\d+\.\d+)\s*:\s*(?P<source_address>\d+\.\d+\.\d+\.\d+)\]\s+(?P<up_time>\S+)/(?P<expires>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # [239.192.20.38 : 2.2.2.2]  00:01:25/00:02:34
            m = p1.match(line)
            if m:
                group = m.groupdict()

                data_mdt_group_dict = ret_dict.setdefault('data_mdt_group', {})
                sub_dict = data_mdt_group_dict.setdefault(group['data_mdt_group'], {})
                sub_dict['source'] = group['source_address']
                sub_dict['up_time'] = group['up_time']
                sub_dict['expires'] = group['expires']
                continue

        return ret_dict


# ==========================================================
# Schema parser for 'show ipv6 pim mdt send'
# Schema Parser for 'show ipv6 pim vrf {vrf_name} mdt send'
# ==========================================================
class ShowIpv6PimMdtSendSchema(MetaParser):
    """Schema for 'show ipv6 pim vrf {vrf_name} mdt send' """

    schema = {
        'vrf' : {
            Any(): {
                'mdt' : {
                    Any(): {
                        'source':str,
                        'group':str,
                        'mdt_data_group':str,
                        'ref_count':int
                    }
                }
            }
        }
    }
class ShowIpv6PimMdtSend(ShowIpv6PimMdtSendSchema):
    """Parser for:
    show ipv6 pim vrf {vrf_name} mdt send
    show ipv6 pim mdt send"""

    cli_command = ["show ipv6 pim mdt send", "show ipv6 pim vrf {vrf} mdt send"]

    def cli(self, vrf='', output=None):

        if output is None:
            if vrf:
                output = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[0])
                vrf = 'Default'

        ret_dict = {}
        index=0
        source_ip = None
        # MDT-data send list for VRF: vrf1
        # (source, group)                     MDT-data group/num   ref_count
        # (2001::2,
        # FF8E::)                            239.192.20.41        1
        # (2001::2,
        # FF8E::1)                           239.192.20.40        1
        # (2001::2,
        # FF8E::2)                           239.192.20.39        1

        # (2001::2,
        p1 = re.compile(r'\(\s*(?P<source>[0-9A-Fa-f:.]+),?\s*')

        # FF8E::)         239.192.20.41        1
        p2 = re.compile(r'(?P<group>[0-9A-Fa-f:.]+)\)\s+(?P<mdt_data_group>[\d\.]+)\s+(?P<ref_count>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # (2001::2,
            m1 = p1.match(line)
            if m1:

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                source_ip = m1.group("source")
                continue

            # FF8E::)         239.192.20.41        1
            m2 = p2.match(line)
            if m2 and source_ip:
                groups = m2.groupdict()
                if "mdt" not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]["mdt"] = {}

                sub_dict = ret_dict['vrf'][vrf]["mdt"].setdefault(index, {})
                sub_dict["source"] = source_ip
                sub_dict["group"] = groups["group"]
                sub_dict["mdt_data_group"] = groups["mdt_data_group"]
                sub_dict["ref_count"] = int(groups["ref_count"])

                index += 1
                source_ip = None  # Reset after processing a complete pair
                continue

        return ret_dict
    

# ==============================================================================
# Schema Parser for 'show ipv6 pim mdt receive'
# Schema Parser for 'show ipv6 pim vrf {vrf_name} mdt receive'
# ==============================================================================
class ShowIpv6PimMdtReceiveSchema(MetaParser):
    """Schema for:
        show ipv6 pim mdt receive
        show ipv6 pim vrf {vrf_name} mdt receive """
        
    schema = {
        'vrf' : {
            Any(): {
                'mdt' : {
                    Any(): {
                        Optional('source'):str,
                        Optional('group'):str,
                        Optional('up_time') : str,
                        Optional('expires') : str,
                    }
                }       
            }
        }       
    }
    
# ==============================================================================
# Parser for 'show ipv6 pim mdt receive'
# Parser for 'show ipv6 pim vrf {vrf_name} mdt receive'
# ==============================================================================
class ShowIpv6PimMdtReceive(ShowIpv6PimMdtReceiveSchema):
    """Parser for:
        show ipv6 pim mdt receive
        show ipv6 pim vrf {vrf} mdt receive """

    cli_command = ['show ipv6 pim mdt receive', 'show ipv6 pim vrf {vrf} mdt receive']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                output = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[0])
                vrf = 'Default'
                
        ret_dict = {}
        index=0

        # Joined MDT-data [group/mdt number : source]  uptime/expires for VRF: vrf1
        #  [239.192.20.32 : 2.2.2.2]  00:12:56/00:02:05
        #  [239.192.20.33 : 2.2.2.2]  00:12:56/00:02:05
        #  [239.192.20.34 : 2.2.2.2]  00:12:56/00:02:05
        #  [239.192.20.35 : 2.2.2.2]  00:12:56/00:02:05
        
        p1 = re.compile(r'^\s*\[(?P<data_mdt_group>\d+\.\d+\.\d+\.\d+)\s*:\s*(?P<source_address>\d+\.\d+\.\d+\.\d+)\]\s+(?P<up_time>\S+)/(?P<expires>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            #  [239.192.20.32 : 2.2.2.2]  00:12:56/00:02:05
            m = p1.match(line)
            if m:
                group = m.groupdict()
                
                ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('mdt', {})  
                sub_dict = ret_dict['vrf'][vrf]["mdt"].setdefault(index, {})
                sub_dict['source'] = group['source_address']
                sub_dict['group'] = group['data_mdt_group']
                sub_dict['up_time'] = group['up_time']
                sub_dict['expires'] = group['expires']
                
                index += 1
                continue  

        return ret_dict