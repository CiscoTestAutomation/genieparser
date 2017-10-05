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
                                Optional('bsr_rp_candidate_address'): {
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
    # Parser for 'show ipv6 pim bsr election'
    # Parser for 'show ipv6 pim vrf <vrf_name> bsr election'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip pim vrf {} bsr candidate-rp'.format(vrf)
        else:
            cmd = 'show ip pim bsr candidate-rp'
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

            if 'bsr_rp_candidate_address' not in ret_dict['vrf'][vrf]['address_family'] \
                    [af_name]['rp']['bsr']:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_rp_candidate_address'] = {}
            if address:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_rp_candidate_address']['address'] = address

            if mode:
                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_rp_candidate_address']['mode'] = mode

            if priority is not None:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']\
                    ['bsr_rp_candidate_address']['priority'] = priority

            if holdtime is not None:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']\
                    ['bsr_rp_candidate_address']['holdtime'] = holdtime

            if interval :
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']\
                    ['bsr_rp_candidate_address']['interval'] = interval
            if next_advertisement:
                ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] \
                    ['rp_candidate_next_advertisement'] = next_advertisement

            continue

        return ret_dict

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
