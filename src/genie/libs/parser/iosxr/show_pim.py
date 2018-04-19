"""show_pim.py

IOSXR parsers for the following show commands:
    * 'show pim vrf <WORD> <WORD> mstatic'
    * 'show pim vrf <WORD> <WORD> interface detail'
    * 'show pim vrf <WORD> <WORD> rpf summary'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# ===============================================
# Schema for 'show pim vrf <vrf> <address_family> mstatic'
# ===============================================

class ShowPimVrfMstaticSchema(MetaParser):
    """Schema for show pim vrf <vrf> <address_family> mstatic"""

    schema = {
        'vrf':
            {Any():
                {'address_family': 
                    {Any(): 
                        {'mroute': 
                            {Any(): 
                                {'path': 
                                    {Any(): 
                                        {'neighbor_address': str,
                                        'interface_name': str,
                                        'admin_distance': int,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowPimVrfMstatic(ShowPimVrfMstaticSchema):
    """Parser for show pim vrf <vrf> <address_family> mstatic"""

    def cli(self, vrf='default', af='ipv4'):
        out = self.device.execute('show pim vrf {vrf} {af} mstatic'.\
                                  format(vrf=vrf, af=af))
        
        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # * 10.10.10.10/32 via GigabitEthernet0/0/0/0 with nexthop 192.168.1.1 and distance 0 
            p1 = re.compile(r'^\s*(?P<var>(\*))'
                             ' *(?P<address>(\S+))'
                             '\/(?P<prefix_mask>[0-9]+) +via'
                             ' +(?P<interface_name>(\S+)) +with +nexthop'
                             ' +(?P<neighbor_address>(\S+)) +and +distance'
                             ' +(?P<admin_distance>[0-9]+)$')
            m = p1.match(line)
            if m:
                # Get values
                address = str(m.groupdict()['address'])
                prefix_mask = int(m.groupdict()['prefix_mask'])
                interface_name = str(m.groupdict()['interface_name'])
                neighbor_address = str(m.groupdict()['neighbor_address'])
                admin_distance = int(m.groupdict()['admin_distance'])
                # Sub values
                mroute_address = address + '/' + str(prefix_mask)
                path = neighbor_address + ' ' + interface_name + ' ' + str(admin_distance)

                # Init dicts
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['address_family'] = {}
                if af not in parsed_dict['vrf'][vrf]['address_family']:
                    parsed_dict['vrf'][vrf]['address_family'][af] = {}
                if 'mroute' not in parsed_dict['vrf'][vrf]['address_family'][af]:
                    parsed_dict['vrf'][vrf]['address_family'][af]['mroute'] = {}

                # Set sub dict
                mroute_dict = parsed_dict['vrf'][vrf]['address_family'][af]['mroute']

                # Set values
                if mroute_address not in mroute_dict:
                    mroute_dict[mroute_address] = {}
                if 'path' not in mroute_dict[mroute_address]:
                    mroute_dict[mroute_address]['path'] = {}
                if path not in mroute_dict[mroute_address]['path']:
                    mroute_dict[mroute_address]['path'][path] = {}
                mroute_dict[mroute_address]['path'][path]['neighbor_address'] = \
                    neighbor_address
                mroute_dict[mroute_address]['path'][path]['interface_name'] = \
                    interface_name
                mroute_dict[mroute_address]['path'][path]['admin_distance'] = \
                    admin_distance
                continue

        return parsed_dict


# ========================================================
# Schema for 'show pim vrf <vrf> <address_family> interface detail'
# ========================================================
class ShowPimVrfInterfaceDetailSchema(MetaParser):
    """Schema for show pim vrf <vrf> <address_family> interface detail"""

    schema = {
        'vrf':
            {Any():
                {'interfaces': 
                    {Any(): 
                        {'address_family': 
                            {Any(): 
                                {'oper_status': str,
                                'nbr_count': int,
                                'nbr_count': int,
                                'hello_interval': int,
                                'dr_priority': int,
                                'primary_address': str,
                                'address': list,
                                'flags': str,
                                'bfd': 
                                    {'enable': bool,
                                    'interval': float,
                                    'detection_multiplier': int,
                                    },
                                'dr': str,
                                'propagation_delay': int,
                                'override_interval': int,
                                'hello_expiration': str,
                                'neighbor_filter': str,
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowPimVrfInterfaceDetail(ShowPimVrfInterfaceDetailSchema):
    """Parser for show pim vrf <vrf> <address_family> interface detail"""

    def cli(self, vrf='default', af='ipv4'):
        out = self.device.execute('show pim vrf {vrf} {af} interface detail'.\
                                  format(vrf=vrf, af=af))
        
        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # PIM interfaces in VRF default
            p1 = re.compile(r'^\s*PIM +interfaces +in +VRF'
                             ' +(?P<vrf_name>[a-zA-Z0-9\-]+)$')
            m = p1.match(line)
            if m:
                vrf_name = str(m.groupdict()['vrf_name'])
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf == vrf_name and vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                continue

            # IP PIM Multicast Interface State
            p2 = re.compile(r'^\s*IP +PIM +Multicast +Interface +State$')
            m = p2.match(line)
            if m:
                continue

            # Flag: B - Bidir enabled, NB - Bidir disabled
            #       P - PIM Proxy enabled, NP - PIM Proxy disabled
            #       A - PIM Assert batching capable, NA - PIM Assert batching incapable
            #       V - Virtual Interface
            # Interface                  PIM  Nbr   Hello  DR
            #                                 Count Intvl  Prior

            # Loopback0                   on   1     30     1
            p3 = re.compile(r'^\s*(?P<interface>(\S+)) +(?P<oper_status>(\S+))'
                             ' +(?P<nbr_count>[0-9]+)'
                             ' +(?P<hello_interval>[0-9]+)'
                             ' +(?P<dr_priority>[0-9]+)$')
            m = p3.match(line)
            if m:
                # Get values
                interface = m.groupdict()['interface']
                oper_status = m.groupdict()['oper_status']
                nbr_count = int(m.groupdict()['nbr_count'])
                hello_interval = int(m.groupdict()['hello_interval'])
                dr_priority = int(m.groupdict()['dr_priority'])
                address_list = []
                if 'interfaces' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['interfaces'] = {}
                if interface not in parsed_dict['vrf'][vrf_name]['interfaces']:
                    parsed_dict['vrf'][vrf_name]['interfaces'][interface] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]\
                        ['interfaces'][interface]:
                    parsed_dict['vrf'][vrf_name]['interfaces'][interface]\
                        ['address_family'] = {}
                if af not in parsed_dict['vrf'][vrf_name]['interfaces']\
                        [interface]['address_family']:
                    parsed_dict['vrf'][vrf_name]['interfaces'][interface]\
                        ['address_family'][af] = {}
                    sub_dict = parsed_dict['vrf'][vrf_name]['interfaces']\
                        [interface]['address_family'][af]
                # Set values
                sub_dict['oper_status'] = oper_status
                sub_dict['nbr_count'] = nbr_count
                sub_dict['hello_interval'] = hello_interval
                sub_dict['dr_priority'] = dr_priority
                continue

            # Primary Address : fe80::85c6:bdff:fe62:61e
            p4 = re.compile(r'^\s*Primary +Address *:'
                             ' +(?P<primary_address>(\S+))$')
            m = p4.match(line)
            if m:
                if m.groupdict()['primary_address']:
                    address_list.append(m.groupdict()['primary_address'])
                sub_dict['primary_address'] = m.groupdict()['primary_address']
                sub_dict['address'] = address_list
                continue
            
            # Address : 2001:db8:2:2::2
            p5 = re.compile(r'^\s*Address *: +(?P<address>(\S+))$')
            m = p5.match(line)
            if m:
                if m.groupdict()['address']:
                    address_list.append(m.groupdict()['address'])
                sub_dict['address'] = address_list
                continue

            # Flags : B P NA V
            p6 = re.compile(r'^\s*Flags *: +(?P<flags>[a-zA-Z\s]+)$')
            m = p6.match(line)
            if m:
                sub_dict['flags'] = m.groupdict()['flags']
                continue

            # BFD : Off/150 ms/3
            p7 = re.compile(r'^\s*BFD *: (?P<enable>(Off|On))'
                             '\/(?P<interval>[0-9]+)'
                             ' *ms\/(?P<dmultiplier>[0-9]+)$')
            m = p7.match(line)
            if m:
                # Get values
                enable = m.groupdict()['enable']
                interval = float(int(m.groupdict()['interval'])/1000)
                dmultiplier = int(m.groupdict()['dmultiplier'])
                # Set values
                if 'bfd' not in sub_dict:
                    sub_dict['bfd'] = {}
                    if enable == 'On':
                        sub_dict['bfd']['enable'] = True
                    else:
                        sub_dict['bfd']['enable'] = False
                    sub_dict['bfd']['interval'] = interval
                    sub_dict['bfd']['detection_multiplier'] = dmultiplier
                    continue

            # DR : this system
            p8 = re.compile(r'^\s*DR *: (?P<dr>[a-zA-Z\s]+)$')
            m = p8.match(line)
            if m:
                sub_dict['dr'] = m.groupdict()['dr']
                continue

            # Propagation delay : 500
            p9 = re.compile(r'^\s*Propagation +delay *:'
                             ' +(?P<propagation_delay>[0-9]+)$')
            m = p9.match(line)
            if m:
                sub_dict['propagation_delay'] = \
                    int(m.groupdict()['propagation_delay'])
                continue

            # Override Interval : 2500
            p10 = re.compile(r'^\s*Override +Interval *:'
                              ' +(?P<override_interval>[0-9]+)$')
            m = p10.match(line)
            if m:
                sub_dict['override_interval'] = \
                    int(m.groupdict()['override_interval'])
                continue

            # Hello Timer : 00:00:19
            p11 = re.compile(r'^\s*Hello +Timer *: +(?P<hello_expiration>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['hello_expiration'] = m.groupdict()['hello_expiration']
                continue

            # Neighbor Filter : -
            p12 = re.compile(r'^\s*Neighbor +Filter *:'
                              ' +(?P<neighbor_filter>(\S+))$')
            m = p12.match(line)
            if m:
                sub_dict['neighbor_filter'] = m.groupdict()['neighbor_filter']
                continue

        return parsed_dict


# ========================================================
# Schema for 'show pim vrf <vrf> <address_family> rpf summary'
# ========================================================

class ShowPimVrfRpfSummarySchema(MetaParser):
    """Schema for show pim vrf <vrf> <address_family> rpf summary"""

    schema = {
        'vrf':
            {Any():
                {'address_family': 
                    {Any(): 
                        {Optional('isis_mcast_topology'): bool,
                        Optional('mo_frr_flow_based'): bool,
                        Optional('mo_frr_rib'): bool,
                        Optional('rump_mu_rib'): bool,
                        Optional('pim_rpfs_registered'): str,
                        Optional('default_rpf_table'): str,
                        Optional('rib_convergence_timeout'): str,
                        Optional('rib_convergence_time_left'): str,
                        Optional('multipath'): bool,
                        Optional('table'): 
                            {Any(): 
                                {'pim_rpf_registrations': int,
                                'rib_table_converged': bool,
                                },
                            },
                        },
                    },
                },
            },
        }

class ShowPimVrfRpfSummary(ShowPimVrfRpfSummarySchema):
    """Parser for show pim vrf <vrf> <address_family> rpf summary"""

    def cli(self, vrf='default', af='ipv4'):
        out = self.device.execute('show pim vrf {vrf} {af} rpf summary'.\
                                  format(vrf=vrf, af=af))
        
        # Init vars
        parsed_dict = {}
        created = False

        for line in out.splitlines():
            line = line.rstrip()

            if not created:
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['address_family'] = {}
                if af not in parsed_dict['vrf'][vrf]['address_family']:
                    parsed_dict['vrf'][vrf]['address_family'][af] = {}
                    sub_dict = parsed_dict['vrf'][vrf]['address_family'][af]
                created = True

            # ISIS Mcast Topology Not configured
            p1 = re.compile(r'^\s*ISIS +Mcast +Topology'
                             ' +(?P<status>[a-zA-Z0-9\s\_\-]+)$')
            m = p1.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'Not configured':
                    sub_dict['isis_mcast_topology'] = False
                else:
                    sub_dict['isis_mcast_topology'] = True
                continue

            # MoFRR Flow-based    Not configured
            p2 = re.compile(r'^\s*MoFRR +Flow-based'
                             ' +(?P<status>[a-zA-Z0-9\s\_\-]+)$')
            m = p2.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'Not configured':
                    sub_dict['mo_frr_flow_based'] = False
                else:
                    sub_dict['mo_frr_flow_based'] = True
                continue
            
            # MoFRR RIB           Not configured
            p3 = re.compile(r'^\s*MoFRR +RIB +(?P<status>[a-zA-Z0-9\s\_\-]+)$')
            m = p3.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'Not configured':
                    sub_dict['mo_frr_rib'] = False
                else:
                    sub_dict['mo_frr_rib'] = True
                continue
            
            # RUMP MuRIB          Not enabled
            p4 = re.compile(r'^\s*RUMP +MuRIB +(?P<status>[a-zA-Z0-9\s\_\-]+)$')
            m = p4.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'Not enabled':
                    sub_dict['rump_mu_rib'] = False
                else:
                    sub_dict['rump_mu_rib'] = True
                continue

            # PIM RPFs registered with Unicast RIB table
            p5 = re.compile(r'^\s*PIM +RPFs +registered +with'
                             ' +(?P<table>[a-zA-Z0-9\s\_\-]+)$')
            m = p5.match(line)
            if m:
                if m.groupdict()['table']:
                    sub_dict['pim_rpfs_registered'] = \
                        str(m.groupdict()['table'])
                continue

            # Default RPF Table: IPv4-Unicast-default
            p6 = re.compile(r'^\s*Default +RPF +Table:'
                             ' +(?P<table>[a-zA-Z0-9\s\_\-]+)$')
            m = p6.match(line)
            if m:
                if m.groupdict()['table']:
                    sub_dict['default_rpf_table'] = str(m.groupdict()['table'])
                continue
            
            # RIB Convergence Timeout Value: 00:30:00
            p7 = re.compile(r'^\s*RIB +Convergence +Timeout +Value:'
                             ' +(?P<time>(\S+))$')
            m = p7.match(line)
            if m:
                if m.groupdict()['time']:
                    sub_dict['rib_convergence_timeout'] = \
                        str(m.groupdict()['time'])
                continue
            
            # RIB Convergence Time Left:     00:00:00
            p8 = re.compile(r'^\s*RIB +Convergence +Time Left:'
                             ' +(?P<time>(\S+))$')
            m = p8.match(line)
            if m:
                if m.groupdict()['time']:
                    sub_dict['rib_convergence_time_left'] = \
                        str(m.groupdict()['time'])
                continue
            
            # Multipath RPF Selection is Enabled
            p9 = re.compile(r'^\s*Multipath +RPF +Selection +is'
                             ' +(?P<status>[a-zA-Z0-9\s\_\-]+)$')
            m = p9.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'Enabled':
                    sub_dict['multipath'] = True
                else:
                    sub_dict['multipath'] = False
                continue

            # Table: IPv6-Unicast-default
            p10 = re.compile(r'^\s*Table: +(?P<table>[a-zA-Z0-9\s\_\-]+)$')
            m = p10.match(line)
            if m:
                if m.groupdict()['table']:
                    table = m.groupdict()['table']
                    if 'table' not in sub_dict:
                        sub_dict['table'] = {}
                    if table not in sub_dict['table']:
                        sub_dict['table'][table] = {}
                    continue
            
            # PIM RPF Registrations = 0
            p10 = re.compile(r'^\s*PIM +RPF +Registrations += (?P<var>[0-9]+)$')
            m = p10.match(line)
            if m:
                sub_dict['table'][table]['pim_rpf_registrations'] = \
                    int(m.groupdict()['var'])
                continue
            
            # RIB Table converged
            p11 = re.compile(r'^\s*RIB +Table'
                              ' +(?P<status>[a-zA-Z0-9\s\_\-]+)$')
            m = p11.match(line)
            if m:
                status = m.groupdict()['status']
                if status == 'converged':
                    sub_dict['table'][table]['rib_table_converged'] = True
                else:
                    sub_dict['table'][table]['rib_table_converged'] = False
                continue

        return parsed_dict
