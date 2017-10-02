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


class ShowIpPimRpMappingSchema(MetaParser):

    # Schema for 'show ip pim rp mapping'

    schema = {'vrf': {
                Any(): {
                    'address-family': {
                        Any(): {
                            'rp': {
                                'rp-mappings': {  # Ops from cmds [show ip pim rp vrf all|show ipv6 pim rp vrf all]
                                    Any(): {  # Ops '224.0.0.0/5 10.1.5.1'
                                        'group': str,  # Ops '224.0.0.0/5'
                                        'rp-address': str,  # Ops '10.1.5.1'
                                        'up-time': str,  # Ops '01:56:07'
                                        'expiration': str,  # Ops '00:02:05'
                                    }
                                },
                            },
                        },
                    }
                },
           },
    }

class ShowIpPimRpMapping(MetaParser):
    # Parser for 'show ip pim rp mapping'

    def cli(self):

        # find interface

        cmd = 'show ip pim rp mapping'
        vrf = 'default'
        af_name = 'ipv6'

        # excute command to get output
        out = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Group(s) 224.0.0.0/4
            p2 = re.compile(r'^\s*Group\(s\) +(?P<group>[0-9a-zA-Z\:\.\/]+)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()['group']

                continue

            # RP 3.3.3.3 (?), v2
            p2 = re.compile(r'^\s*RP +(?P<rp_address>[\s\w\:\.]+) +(\(\?\))?,'
                            ' +(?P<rp_version>\w+)$')
            m = p2.match(line)
            if m:
                rp_address = m.groupdict()['rp_address']
                rp_version = m.groupdict()['rp_version']
                if group:
                    rp_group = " ".join(group,rp_address)
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
                    if 'rp_mapping' not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mapping'] = {}
                    if rp_group not in ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mapping']:
                        ret_dict['vrf'][vrf]['address_family'][af_name]['rp']['rp_mapping'][rp_group] = {}

                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                        ['rp_mapping'][rp_group]['rp_address'] = rp_address
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp']\
                        ['rp_mapping'][rp_group]['rp_version'] = rp_version
                continue

            # Info source: 4.4.4.4 (?), via bootstrap, priority 5, holdtime 150
            p3 = re.compile(r'^\s*Info +source: +(?P<info_source>[\w\:\.]+) +(\(\?\),)?'
                            '( +(?P<learned_rp_via>[\w\s\S]+),)?'
                            '( +priority +(?P<priority>[\d]+),)?'
                            '( +holdtime +(?P<holdtime>[\d]+))?$')
            m = p3.match(line)
            if m:
                if rp_group:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['rp'] \
                        ['rp_mapping'][rp_group]['info_source'] = m.groupdict()['']

                ret_dict['vrf'][vrf]['interface'][intf]['dr_address'] = \
                    m.groupdict()['dr_address']
                continue

            # Uptime: 00:00:19, expires: 00:02:19
            p4 = re.compile(r'^\s*Uptime: +(?P<uptime>[\d\:]+),'
                            ' +expires: +(?P<expires>[\d\:]+)$')
            m = p4.match(line)
            if m:
                up_time = m.groupdict()['uptime']
                expiration = m.groupdict()['expires']
                ret_dict['vrf'][vrf]['rp']['rp_mapping'][group_rp_address]\
                    ['up_time'] = up_time
                ret_dict['vrf'][vrf]['rp']['rp_mapping'][group_rp_address] \
                    ['expiration'] = expiration
        return ret_dict

