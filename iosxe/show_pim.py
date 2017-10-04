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

class ShowIpPimBsrRouterSchema(MetaParser):

    # Schema for 'show ip pim bsr-router'
    schema = {
        'vrf': {
            Any(): {
                'address_family':{
                    Any():{
                        'rp': {
                            'bsr':{
                                Optional('bsr_candidate'): {
                                    Optional('address'): str,
                                    Optional('hash_mask_length'): int,
                                    Optional('priority'): int,
                                },
                                Optional('bsr_rp_candidate_interface'): {
                                    Optional('interface'): str,
                                    Optional('address'): str,
                                    Optional('holdtime'): int,
                                    Optional('next_advertisment'): str,
                                    Optional('priority'): int,
                                    Optional('interval'): int,
                                },
                                Optional('bsr_rp_candidate_address'): {
                                    Optional('interface'): str,
                                    Optional('address'): str,
                                    Optional('holdtime'): str,
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
                            },
                        },
                    },
                },
            },
        }
    }

class ShowIpPimBsrRouter(ShowIpPimBsrRouterSchema):

    # Parser for 'show ip pim bsr-router'
    # Parser for 'show ip pim vrf <vrf_name> bsr-router'

    def cli(self, vrf=""):

        # find cmd
        if vrf:
            cmd = 'show ip pim vrf {} bsr-router'.format(vrf)
        else:
            cmd = 'show ip pim bsr-router'
            vrf = 'default'

        af_name = 'ipv4'
        rp_can_interface = rp_can_address = rp_can_holdtime = rp_can_interval = ""
        rp_can_next_advertisment = rp_can_priority = ""

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # PIMv2 Bootstrap information
            # BSR address: 4.4.4.4 (?)
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
                if 'bsr' not in ret_dict['vrf'][vrf]['address_family']\
                        [af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]\
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

            #  Uptime:      00:01:23, BSR Priority: 0, Hash mask length: 0
            p2 = re.compile(r'^\s*Uptime: +(?P<up_time>[\d\:]+),'
                            ' +BSR +Priority: +(?P<priority>\d+),'
                            ' +Hash +mask +length: +(?P<hash_mask_length>\d+)$')
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

            # Candidate BSR address: 1.1.1.1, priority: 0, hash mask length: 0
            p4 = re.compile(r'^\s*Candidate +BSR +address: +(?P<can_address>[\w\d\:\.]+),'
                            ' +priority: +(?P<can_priority>\d+),'
                            ' +hash +mask +length: +(?P<can_hash_mask_length>\d+)$')
            m = p4.match(line)
            if m:
                can_address = m.groupdict()['can_address']
                can_priority = int(m.groupdict()['can_priority'])
                can_hash_mask = int(m.groupdict()['can_hash_mask_length'])

                if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                if 'bsr' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] = {}
                if 'bsr_candidate' not in ret_dict['vrf'][vrf]['address_family']\
                        [af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                        ['bsr']['bsr_candidate'] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['address'] = can_address

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['priority'] = can_priority

                ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr']['bsr_candidate']['hash_mask_length'] = can_hash_mask
                continue

            #  Candidate RP: 10.1.5.1(GigabitEthernet3)
            p5 = re.compile(r'^\s*Candidate +RP:'
                            ' +(?P<rp_can_address>[\w\d\.\:]+)\((?P<rp_can_interface>[\w\d]+)\)$')

            m = p5.match(line)
            if m:
                rp_can_address = m.groupdict()['rp_can_address']
                rp_can_interface = m.groupdict()['rp_can_interface']
                continue

            # Holdtime 150 seconds
            p6 = re.compile(r'^\s*Holdtime'
                            ' +(?P<holdtime>\d+) +seconds$')
            m = p6.match(line)
            if m:
                rp_can_holdtime = int(m.groupdict()['holdtime'])
                continue

            # Advertisement interval 60 seconds
            p7 = re.compile(r'^\s*Advertisement +interval'
                            ' +(?P<interval>\d+) +seconds$')
            m = p7.match(line)
            if m:
                rp_can_interval = int(m.groupdict()['interval'])
                continue

            # Next advertisement in 00:00:27
            p8 = re.compile(r'^\s*Next +advertisement +in'
                            ' +(?P<next_advertisment>[\d\:]+)$')
            m = p8.match(line)
            if m:
                rp_can_next_advertisment = m.groupdict()['next_advertisment']
                continue

            # Candidate RP priority : 5
            p9 = re.compile(r'^\s*Candidate +RP +priority +:'
                            ' +(?P<rp_can_priority>[\d]+)$')
            m = p9.match(line)
            if m:
                rp_can_priority = int(m.groupdict()['rp_can_priority'])
                continue

            if rp_can_address or rp_can_interface:
                if 'rp' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] = {}
                if 'bsr' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'] = {}

                if rp_can_interface:
                    key = 'bsr_rp_candidate_interface'
                else:
                    key = 'bsr_rp_candidate_address'

                if key not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['bsr'][key] = {}

                if rp_can_interface:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['interface'] = rp_can_interface

                if rp_can_address:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                    ['rp']['bsr'][key]['address'] = rp_can_address

                if rp_can_holdtime:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][key]['holdtime'] = rp_can_holdtime

                if rp_can_interval:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][key]['interval'] = rp_can_interval

                if rp_can_next_advertisment:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][key]['next_advertisment'] = rp_can_next_advertisment

                if rp_can_priority:
                    ret_dict['vrf'][vrf]['address_family'][af_name] \
                        ['rp']['bsr'][key]['priority'] = rp_can_priority
                continue

        return ret_dict

