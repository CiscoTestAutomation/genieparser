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


class ShowIpPimInterfaceSchema(MetaParser):

    # Schema for 'show ip pim Interface'
    schema = {
        'vrf': {
            Any(): {
                'address_family':{
                    Any():{
                        'interface': {
                            Any(): {
                                Optional('dr_priority'): int,
                                Optional('hello_interval'): int,
                                Optional('neighbor_count'): int,
                                Optional('version_mode'): str,
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

    def cli(self, vrf_name=""):

        # find cmd
        if vrf_name:
            cmd = 'show ip vrf {} interface'.format(vrf_name)
        else:
            cmd = 'show ip pim interface'
            vrf_name = 'default'

        vrf = vrf_name
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
            p1 = re.compile(r'^\s*(?P<address>[\w\:\.]+) +(?P<interface>[\w\d]+)'
                            ' +(?P<version_mode>[\w\d\/]+)'
                            ' +(?P<nbr_count>[\d]+)'
                            ' +(?P<query_interval>[\d]+)'
                            ' +(?P<dr_priority>[\d]+)'
                            ' +(?P<dr_address>[\w\d\.\:]+)$')
            m = p1.match(line)
            if m:
                address = m.groupdict()['address']
                intf_name = m.groupdict()['interface']
                nbr_count = int(m.groupdict()['nbr_count'])
                version_mode = m.groupdict()['version_mode']
                query_interval = int(m.groupdict()['query_interval'])
                dr_priority = int(m.groupdict()['dr_priority'])
                dr_address = m.groupdict()['dr_address']

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af_name not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af_name] = {}
                if 'interface' not in ret_dict['vrf'][vrf]['address_family'][af_name]:
                    ret_dict['vrf'][vrf]['address_family'][af_name]['interface'] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family']\
                        [af_name]['interface']:
                    ret_dict['vrf'][vrf]['address_family'][af_name]\
                        ['interface'][intf_name] = {}

                ret_dict['vrf'][vrf]['address_family'][af_name]['interface']\
                    [intf_name]['address'] = address.split()
                ret_dict['vrf'][vrf]['address_family'][af_name]['interface']\
                    [intf_name]['neighbor_count'] = nbr_count
                ret_dict['vrf'][vrf]['address_family'][af_name]['interface']\
                    [intf_name]['version_mode'] = version_mode
                ret_dict['vrf'][vrf]['address_family'][af_name]['interface']\
                    [intf_name]['hello_interval'] = query_interval
                ret_dict['vrf'][vrf]['address_family'][af_name]['interface']\
                    [intf_name]['dr_priority'] = dr_priority
                ret_dict['vrf'][vrf]['address_family'][af_name]['interface']\
                    [intf_name]['dr_address'] = dr_address
                continue

        return ret_dict
