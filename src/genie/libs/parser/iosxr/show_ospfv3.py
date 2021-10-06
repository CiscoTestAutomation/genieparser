''' show_ospfv3.py

Parser for the following commands:
    * show ospfv3 neighbor
    * show ospfv3 {process} neighbor
    * show ospfv3 vrf {vrf} neighbor
    * show ospfv3 database
    * show ospfv3 {process_id} database
'''
import re

import genie.metaparser.util.exceptions
from netaddr import IPAddress, IPNetwork

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowOspfv3NeighborSchema(MetaParser):
    """ Schema for:
    * show ospfv3 neighbor
    """
    schema = {
        'process': str,
        'vrfs': {
            Any(): {
                'neighbors': {
                    Any(): {
                        'priority': str,
                        'state': str,
                        'dead_time': str,
                        'address': str,
                        'interface': str,
                        'up_time': str
                    }
                },
                Optional('total_neighbor_count'): int
            }
        }
    }


class ShowOspfv3Neighbor(ShowOspfv3NeighborSchema):
    """ Schema for:
    * show ospfv3 neighbor
    """
    cli_command = [
        'show ospfv3 neighbor',
        'show ospfv3 {process} neighbor',
        'show ospfv3 vrf {vrf} neighbor',
        'show ospfv3 {process} vrf {vrf} neighbor',
    ]

    def cli(self, process="", vrf="", output=None):
        if output is None:
            if process:
                if vrf:
                    out = self.device.execute(
                        self.cli_command[3].format(process=process, vrf=vrf))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(process=process))
            elif vrf:
                out = self.device.execute(
                    self.cli_command[2].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        result_dict = {}

        # Neighbors for OSPFv3 1
        # Neighbors for OSPFv3 1, VRF default
        # Neighbors for OSPFv3 1, VRF VRF1
        p1 = re.compile(r'^Neighbors +for +OSPFv3 +(?P<process>\w+)'
                        '(, +VRF (?P<vrf>[\w-]+))?$')

        # Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
        # 10.145.95.95     1     FULL/  -        00:00:37    5               GigabitEthernet0/0/0/1
        # 10.220.100.100 1     FULL/  -        00:00:38    6               GigabitEthernet0/0/0/0
        p2 = re.compile(r'^(?P<neighbor_id>\S+) +(?P<priority>\d+)'
                        ' +(?P<state>\S+\s*\S+) +(?P<dead_time>\S+)'
                        ' +(?P<address>\S+) +(?P<interface>\S+)$')

        # Neighbor is up for 2d18h
        # Neighbor is up for 2d19h
        p3 = re.compile(r'^Neighbor +is +up +for +(?P<up_time>\S+)$')

        # Total neighbor count: 2
        p4 = re.compile(r'^Total +neighbor +count:'
                        ' +(?P<total_neighbor_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF mpls1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict['process'] = group['process']

                vrfs_dict = result_dict.setdefault('vrfs', {})

                vrf_name = group['vrf'] if group['vrf'] \
                    else 'default'
                vrf_dict = vrfs_dict.setdefault(vrf_name, {})

                neighbors_dict = vrf_dict.setdefault('neighbors', {})
                continue

            # Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
            # 10.145.95.95     1     FULL/  -        00:00:37    5               GigabitEthernet0/0/0/1
            # 10.220.100.100 1     FULL/  -        00:00:38    6               GigabitEthernet0/0/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict = neighbors_dict.setdefault(
                    group['neighbor_id'], {})

                neighbor_dict.update({
                    'priority': group['priority'],
                    'state': group['state'],
                    'dead_time': group['dead_time'],
                    'address': group['address'],
                    'interface': group['interface']
                })
                continue

            # Neighbor is up for 2d18h
            m = p3.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict['up_time'] = group['up_time']
                continue

            # Total neighbor count: 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['total_neighbor_count'] = \
                    int(group['total_neighbor_count'])

        return result_dict


class ShowOspfv3DatabaseSchema(MetaParser):
    ''' Schema for:
        * 'show ospfv3 database'
        * 'show ospfv3 {process_id} database'
    '''

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                "router_id": str,
                                Optional('area'): {
                                    Any(): {
                                        "area_id": int,
                                        'database': {
                                            'lsa_types': {
                                                Any(): {
                                                    'lsa_type': int,
                                                    'lsas': {
                                                        Any(): {
                                                            'adv_router': str,
                                                            Optional('fragment_id'): int,
                                                            Optional('link_id'): int,
                                                            'ospfv3': {
                                                                'header': {
                                                                    'age': int,
                                                                    'seq_num': str,
                                                                    Optional('link_count'): int,
                                                                    Optional('link_id'): int,
                                                                    Optional('bits'): str,
                                                                    Optional('interface'): str,
                                                                    Optional('ref_lstype'): str,
                                                                    Optional('ref_lsid'): int,
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
                        },
                    },
                },
            },
        },
    }


class ShowOspfv3Database(ShowOspfv3DatabaseSchema):
    ''' Parser for:
        *'show ospfv3 database'
        *'show ospfv3 {process_id} database'
    '''

    cli_command = ['show ospfv3 database', 'show ospfv3 {process_id} database']

    def cli(self, process_id=None, output=None):

        if not output:
            if process_id:
                output = self.device.execute(self.cli_command[1].format(process_id=process_id))
            else:
                output = self.device.execute(self.cli_command[0])

        # Init vars
        ret_dict = {}
        address_family = 'ipv6'

        # Lsa Types
        # 1: Router
        # 2: Network Link
        # 3: Summary
        # 3: Summary Network
        # 3: Summary Net
        # 4: Summary ASB
        # 5: Type-5 AS External
        # 8: Link (Type-8)
        # 9: Intra Area Prefix'
        # 10: Opaque Area

        lsa_type_mapping = {
            'router': 1,
            'net': 2,
            'summary': 3,
            'summary net': 3,
            'summary asb': 4,
            'external': 5,
            'link (type-8)': 8,
            'intra area prefix': 9,
            'opaque': 10
        }

        # OSPFv3 Router with ID(10.94.1.1) (Process ID mpls1)
        p1 = re.compile(r'^OSPFv3 +Router +with +ID +\((?P<router_id>(\S+))\) '
                        r'+\(Process +ID +(?P<instance>(\S+))(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        # Router Link States (Area 0)
        # Link (Type-8) Link States (Area 0)
        # Intra Area Prefix Link States (Area 0)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z0-9\s\D]+)) +Link +States +\(Area'
                        ' +(?P<area>(\S+))\)$')

        # 10.94.1.1       2019        0x8000007d 0            2           E
        # 10.145.95.95     607         0x80000097 0            2           E
        p3 = re.compile(r'^(?P<adv_router>(\S+)) +(?P<age>(\d+)) +(?P<seq_num>(\S+))'
                        r' +(?P<fragment_id>(\d+)) +(?P<link_count>(\d+)) +(?P<bits>(\w+))$')

        # 10.94.1.1       1518        0x80000086 7          Gi0/0/0/0
        # 10.220.100.100 1841        0x80000079 6          Gi0/0/0/0
        p4 = re.compile(r'^(?P<adv_router>(\S+)) +(?P<age>(\d+)) +(?P<seq_num>(\S+))'
                        r' +(?P<link_id>(\d+)) +(?P<interface>([a-zA-Z0-9\/])+)$')

        # 10.94.1.1       2019        0x80000078 0          0x2001      0
        # 10.145.95.95     1583        0x80000086 0          0x2001      0
        p5 = re.compile(r'^(?P<adv_router>(\S+)) +(?P<age>(\d+)) +(?P<seq_num>(\S+))'
                        r' +(?P<link_id>(\d+)) +(?P<ref_lstype>(\S)+)'
                        r' +(?P<ref_lsid>(\d)+)$')

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 Router with ID(10.94.1.1) (Process ID mpls1)
            m = p1.match(line)

            if m:
                group = m.groupdict()
                router_id = group['router_id']
                instance = group['instance']
                if group['vrf']:
                    vrf = group['vrf']
                else:
                    vrf = 'default'

                # Create dict
                ospf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('instance', {}). \
                    setdefault(instance, {})
                continue

            # Router Link States (Area 0)
            # Link (Type-8) Link States (Area 0)
            # Intra Area Prefix Link States (Area 0)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lsa_type_key = group['lsa_type'].lower()
                if lsa_type_key in lsa_type_mapping:
                    lsa_type = lsa_type_mapping[lsa_type_key]

                # Set area
                if group['area']:
                    try:
                        int(group['area'])
                        area = str(IPAddress(str(group['area'])))
                    except Exception:
                        area = str(group['area'])
                else:
                    area = '0.0.0.0'

                ospf_dict['router_id'] = router_id
                area_dict = ospf_dict.setdefault('area', {}). \
                    setdefault(area, {})
                area_dict['area_id'] = int(group['area'])

                lsa_type_dict = area_dict.setdefault('database', {}). \
                    setdefault('lsa_types', {}). \
                    setdefault(lsa_type, {})

                # Set lsa_type
                lsa_type_dict['lsa_type'] = lsa_type
                continue

            # 10.94.1.1       2019        0x8000007d 0            2           E
            # 10.145.95.95     607         0x80000097 0            2           E
            m = p3.match(line)
            if m:
                group = m.groupdict()
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                fragment_id = int(group['fragment_id'])
                link_count = group['link_count']
                bits = group['bits']
                frag_adv_router = str(fragment_id) + " " + adv_router

                # Create lsas dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}). \
                    setdefault(frag_adv_router, {})
                lsas_dict['adv_router'] = adv_router
                lsas_dict['fragment_id'] = fragment_id

                # osfpv3 dict
                ospfv3_dict = lsas_dict.setdefault('ospfv3', {}). \
                    setdefault('header', {})
                ospfv3_dict['age'] = age
                ospfv3_dict['seq_num'] = seq
                ospfv3_dict['bits'] = group['bits']
                ospfv3_dict['link_count'] = int(group['link_count'])
                continue

            # 10.94.1.1       1518        0x80000086 7          Gi0/0/0/0
            # 10.220.100.100 1841        0x80000079 6          Gi0/0/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                link_id = int(group['link_id'])
                interface = group['interface']
                link_adv_router = str(link_id) + " " + adv_router

                # Create lsas dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}). \
                    setdefault(link_adv_router, {})
                lsas_dict['adv_router'] = adv_router
                lsas_dict['link_id'] = link_id

                # osfpv3 dict
                ospfv3_dict = lsas_dict.setdefault('ospfv3', {}). \
                    setdefault('header', {})
                ospfv3_dict['age'] = age
                ospfv3_dict['seq_num'] = seq
                ospfv3_dict['interface'] = interface
                continue

            # 10.94.1.1       2019        0x80000078 0          0x2001      0
            # 10.145.95.95     1583        0x80000086 0          0x2001      0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                link_id = int(group['link_id'])
                ref_lstype = group['ref_lstype']
                ref_lsid = int(group['ref_lsid'])
                link_adv_router = str(link_id) + " " + adv_router

                # lsas dict
                lsas_dict = lsa_type_dict.setdefault('lsas', {}). \
                    setdefault(link_adv_router, {})
                lsas_dict['adv_router'] = adv_router
                lsas_dict['link_id'] = link_id

                # osfpv3 dict
                ospfv3_dict = lsas_dict.setdefault('ospfv3', {}). \
                    setdefault('header', {})
                ospfv3_dict['age'] = age
                ospfv3_dict['seq_num'] = seq
                ospfv3_dict['ref_lstype'] = ref_lstype
                ospfv3_dict['ref_lsid'] = ref_lsid
                continue
        return ret_dict

class ShowOspfv3VrfAllInclusiveNeighborDetailSchema(MetaParser):
    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                "area": {
                                    Any(): {
                                        "neighbor_router_id": {
                                            Any(): {
                                                "interface": {
                                                    Any(): {
                                                        Optional("bfd_enable"): str or bool,
                                                        Optional("bfd_mode"): str,
                                                        'Neighbor': {
                                                            'interface-id': int,
                                                            'link-local_address': str
                                                        },
                                                        "priority": int,
                                                        "state": str,
                                                        'state_changes': int,
                                                        Optional("dr_ip_addr"): str,
                                                        Optional("bdr_ip_addr"): str,
                                                        Optional("options"): str,
                                                        Optional("dead_timer"): str,
                                                        Optional("neighbor_uptime"): str,
                                                        Optional("index"): str,
                                                        Optional("first"): str,
                                                        Optional("next"): str,
                                                        Optional("statistics"): {
                                                            Optional("retransmission_queue_length"): int,
                                                            Optional("number_of_retransmissions"): int,
                                                            Optional("last_retrans_scan_length"): int,
                                                            Optional("last_retrans_max_scan_length"): int,
                                                            Optional("last_retrans_scan_time_msec"): int,
                                                            Optional("last_retrans_max_scan_time_msec"): int,
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "total_neighbor_count": int,
                            }, }, }, }, }, }, }


class ShowOspfv3VrfAllInclusiveNeighborDetail(ShowOspfv3VrfAllInclusiveNeighborDetailSchema):
    """
    Parser for show ospfv3 vrf all-inclusive neighbor detail

    Parser picks the appropriate command and gets the device output,
    or it  takes the raw show output with output=.

    Parser then compiles regular expressions to deal with each line
    in the show command, after which it casts the pulled values into
    the appropriate place in the schema, defined the class above.
    """
    cli_command = ['show ospfv3 vrf all-inclusive neighbor detail']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}

        # OSPFv3 supports both ipv4 and ipv6 but the information is not in the show output provided.
        af = "ipv6"

        # Neighbors for OSPFv3 mpls1, VRF default
        p1 = re.compile(r"^Neighbors +for +OSPFv3 +(?P<instance>(\S+)), +(?P<vrf>(VRF \S+))$")

        # Neighbor 10.94.1.1
        p2 = re.compile(r"^Neighbor +(?P<neighbor>(\S+))$")

        # In the area 0 via interface GigabitEthernet0/0/0/0.1
        # In the area 0 via interface GigabitEthernet0/0/0/1.500     BFD enabled, Mode: Default
        p3 = re.compile(r"^In the area +(?P<area>([0-9]+)) via interface +(?P<interface>(\S+))"
                        "( +BFD (?P<enable>\w+), Mode: (?P<mode>\w+))*")

        # Neighbor: interface-id 14, link-local address fe80::20c:29ff:fe6b:1a0
        p4 = re.compile(r"^Neighbor: interface-id +(?P<interface_id>([0-9]+)), "
                        r"link-local address +(?P<link_local>(['a-z:0-9']+))$")

        # Neighbor priority is 1, State is FULL, 6 state changes
        p5 = re.compile(r"^Neighbor priority is +(?P<neighbor_priority>([0-9])+), "
                        r"State is +(?P<state>([A-Z]+)), "
                        r"+(?P<state_changes>([0-9]+)) state changes$")

        # Options is 0x13
        p6 = re.compile(r"^Options +is +(?P<options>(\S+))$")

        # Dead timer due in 00:00:38
        p7 = re.compile(r"^Dead timer due in (?P<time>[0-9:]+)$")

        # Neighbor is up for 00:31:44
        p8 = re.compile(r"^Neighbor is up for (?P<time>[0-9:]+)$")

        # Index 1/46/46, retransmission queue length 0, number of retransmission 0
        p9 = re.compile(r"^Index +(?P<index>(\S+)) +retransmission +queue +length +(?P<ql>(\d+)), "
                        r"+number +of +retransmission +(?P<num_retrans>(\d+))$")

        # First 0(0)/0(0)/0(0) Next 0(0)/0(0)/0(0)
        p10 = re.compile(r"^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$")

        # Last retransmission scan length is 0, maximum is 0
        p11 = re.compile(r"^Last retransmission scan length is +(?P<length>([0-9]+)), "
                         r"maximum is +(?P<maximum>([0-9]+))$")

        # Last retransmission scan time is 0 msec, maximum is 0 msec
        p12 = re.compile(r"^Last retransmission scan time is (?P<scan_time>([0-9]+)), "
                         r"maximum is (?P<max_time>([0-9]+))")

        # Total neighbor count: 24
        p13 = re.compile(r"^Total +neighbor +count: +(?P<num>(\d+))$")

        # loop through output and add to ret_dict
        for line in output.splitlines():
            line = line.strip()

            # Neighbors for OSPFv3 mpls1, VRF default
            m = p1.match(line)
            if m:
                instance = m.groupdict()["instance"]
                vrf = m.groupdict()['vrf']

                instance_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('address_family', {}).setdefault(af, {}). \
                    setdefault('instance', {}).setdefault(instance, {})

            # Neighbor 10.94.1.1
            m = p2.match(line)
            if m:
                neighbor_rid = m.groupdict()['neighbor']

            # In the area 0 via interface GigabitEthernet0/0/0/0.1
            # In the area 0 via interface GigabitEthernet0/0/0/1.500     BFD enabled, Mode: Default
            m = p3.match(line)
            if m:
                area = int(m.groupdict()['area'])
                interface = m.groupdict()['interface']
                interface_dict = instance_dict.setdefault('area', {}).setdefault(area, {}). \
                    setdefault('neighbor_router_id', {}).setdefault(neighbor_rid, {}). \
                    setdefault('interface', {}).setdefault(interface, {})
                
                if m.groupdict()['enable']:
                    interface_dict.update(
                        {
                            "bfd_enable": str(m.groupdict()['enable']),
                        })   

                if m.groupdict()['mode']:
                    interface_dict.update(
                        {
                            "bfd_mode": str(m.groupdict()['mode']),
                        })  

            # Neighbor: interface-id 14, link-local address fe80::20c:29ff:fe6b:1a0
            m = p4.match(line)
            if m:
                neighbor_dict = interface_dict.setdefault('Neighbor', {})
                neighbor_dict.update({'interface-id': int(m.groupdict()['interface_id']),
                                      'link-local_address': m.groupdict()['link_local']
                                      })

            # Neighbor priority is 1, State is FULL, 6 state changes
            m = p5.match(line)
            if m:
                p5info = {'priority': int(m.groupdict()['neighbor_priority']),
                          'state': m.groupdict()['state'].lower(),
                          'state_changes': int(m.groupdict()['state_changes'])}

                interface_dict.update(p5info)

            # Options is 0x13
            m = p6.match(line)
            if m:
                interface_dict.update({'options': m.groupdict()['options']})

            # Dead timer due in 00:00:38
            m = p7.match(line)
            if m:
                interface_dict.update({'dead_timer': m.groupdict()['time']})

            # Neighbor is up for 00:31:44
            m = p8.match(line)
            if m:
                interface_dict.update({'neighbor_uptime': m.groupdict()['time']})

            # Index 1/46/46, retransmission queue length 0, number of retransmission 0
            m = p9.match(line)
            if m:
                interface_dict.update({'index': m.groupdict()['index']})
                stats_dict = interface_dict.setdefault('statistics', {})
                stats_dict.update(
                    {
                        "retransmission_queue_length": int(m.groupdict()['ql']),
                        "number_of_retransmissions": int(m.groupdict()['num_retrans'])
                    })

            # First 0(0)/0(0)/0(0) Next 0(0)/0(0)/0(0)
            m = p10.match(line)
            if m:
                first = m.groupdict()['first']
                nxt = m.groupdict()['next']
                interface_dict.update({'first': first})
                interface_dict.update({'next': nxt})

            # Last retransmission scan length is 0, maximum is 0
            m = p11.match(line)
            if m:
                stats_dict.update({"last_retrans_scan_length": int(m.groupdict()['length']),
                                   "last_retrans_max_scan_length": int(m.groupdict()['maximum'])})

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            m = p12.match(line)
            if m:
                stats_dict.update({"last_retrans_scan_time_msec": int(m.groupdict()['scan_time']),
                                   "last_retrans_max_scan_time_msec": int(m.groupdict()['max_time'])})

            # Total neighbor count: 24
            m = p13.match(line)
            if m:
                instance_dict.update({'total_neighbor_count': int(m.groupdict()['num'])})

        return ret_dict


# ==================================
# Schema for 'show ospfv3 interface'
# ==================================
class ShowOspfv3InterfaceSchema(MetaParser):
    """Schema for show ospfv3 interface"""

    schema = {
        "vrf": {
            Any(): {  # default
                "address_family": {
                    Any(): {  # ipv6
                        "instance": {
                            Any(): {  # p3-- group[pid] --mpls1
                                "instance_id": {
                                    Any(): {  # p3-- int(group[instance])   --0
                                        "areas": {
                                            Any(): {  # p3-- int(group[area]) --0
                                                Optional("interfaces"): {
                                                    Any(): {  # p1-- group[interface] -- GigabitEthernet0/0/0/0
                                                        "enable": str,
                                                        "line_protocol": str,
                                                        "link_local_address": str,
                                                        "router_id": str,
                                                        "network_type": str,
                                                        "interface_id": int,
                                                        "cost": int,
                                                        Optional("adjacent_neighbors"): {
                                                            Optional("neighbor"): str,
                                                            Optional("nbr_count"): int,
                                                            Optional("adj_nbr_count"): int,
                                                        },
                                                        Optional("bfd"): {
                                                            Optional("bfd_status"): str,
                                                            Optional("interval"): int,
                                                            Optional("multiplier"): int,
                                                            Optional("mode"): str,
                                                        },
                                                        Optional("transmit_delay"): int,
                                                        Optional("state"): str,
                                                        Optional("hello_interval"): int,
                                                        Optional("dead_interval"): int,
                                                        Optional("wait_interval"): int,
                                                        Optional("retransmit_interval"): int,
                                                        Optional("hello_timer"): str,
                                                        Optional("index"): str,
                                                        Optional("flood_queue_length"): int,
                                                        Optional("next"): str,
                                                        Optional("last_flood_scan_length"): int,
                                                        Optional("max_flood_scan_length"): int,
                                                        Optional("last_flood_scan_time_msec"): int,
                                                        Optional("max_flood_scan_time_msec"): int,
                                                        Optional("statistics"): {
                                                            Optional("num_nbrs_suppress_hello"): int,
                                                            Optional("refrence_count"): int,
                                                        },
                                                        Optional("loopback_txt"): str,
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
            },
        },
    }


# ==================================
# Parser for 'show ospfv3 interface'
# ==================================
class ShowOspfv3Interface(ShowOspfv3InterfaceSchema):
    """Parser for show ospfv3 interface"""

    cli_command = [
        "show ospfv3 interface",
        "show ospfv3 interface {interface_name}",
        "show ospfv3 {process_name} interface",
        "show ospfv3 {process_name} interface {interface_name}",
        "show ospfv3 vrf all-inclusive interface",
        "show ospfv3 vrf all-inclusive interface {interface_name}",
    ]
    exclude = [
        "dead_timer",
        "hello_timer",
        "last_flood_scan_length",
        "max_flood_scan_length",
        "high_water_mark",
    ]

    def cli(self, vrf="", interface="", output=None):
        if output is None:
            if interface:
                if vrf:
                    out = self.device.execute(self.cli_command[2].format(interface=interface, vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                if vrf:
                    out = self.device.execute(self.cli_command[3].format(vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # GigabitEthernet0/0/0/0 is up, line protocol is up
        # Loopback0 is up, line protocol is up
        p1 = re.compile(
            r"^(?P<interface>(\S+)) +is( +administratively)?"
            " +(?P<enable>(unknown|up|down)), +line +protocol +is"
            " +(?P<line_protocol>(up|down))$")

        # Link Local address fe80:100:10::1, Interface ID 7
        p2 = re.compile(
            r"^Link +Local +address +(?P<link_local_address>(\S+)),"
            " +Interface ID +(?P<interface_id>(\S+))$")

        # Area 0, Process ID mpls1, Instance ID 0, Router ID 10.94.1.1
        p3 = re.compile(
            r"^Area +(?P<area>(\S+))"
            ", +Process +ID +(?P<pid>(\S+))"
            ", +Instance +ID +(?P<instance>(\S+))"
            ", +Router +ID +(?P<router_id>(\S+))$")

        # Network Type POINT_TO_POINT, Cost: 1
        p4 = re.compile(
            r"^Network +Type +(?P<network_type>(\S+))"
            ", +Cost: +(?P<cost>(\S+))$")

        # BFD enabled, interval 150 msec, multiplier 3, mode Default
        p5 = re.compile(
            r"^BFD +(?P<bfd_status>(\S+))"
            "(?:, +interval +(?P<interval>(\d+)) +msec)?"
            "(?:, +multiplier +(?P<multi>(\d+)))?"
            "(?:, +mode +(?P<mode>(\S+)))?$")

        # Transmit Delay is 1 sec, State POINT_TO_POINT,
        p6 = re.compile(
            r"^Transmit +Delay is +(?P<delay>(\d+)) +sec"
            ", +State +(?P<state>(\w)+),$")

        # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        p7 = re.compile(
            r"^Timer +intervals +configured"
            ", +Hello +(?P<hello>(\d+))"
            ", +Dead +(?P<dead>(\d+))"
            ", +Wait +(?P<wait>(\d+))"
            ", +Retransmit +(?P<retransmit>(\d+))$")

        # Hello due in 00:00:08
        p8 = re.compile(r"^Hello +due +in +(?P<hello_timer>(\S+))$")

        # Index 1/1/1, flood queue length 0
        p9 = re.compile(r"^Index +(?P<index>(\S+)), +flood +queue +length +(?P<flood_queue_length>(\d+))$")

        # Next 0(0)/0(0)/0(0)
        p10 = re.compile(r"^Next +(?P<next>(\S+))$")

        # Last flood scan length is 1, maximum is 4
        p11 = re.compile(r"^Last +flood +scan +length +is +(?P<last_flood_scan_length>(\d+))"
                         ", +maximum +is +(?P<max_flood_scan_length>(\d+))$")

        # Last flood scan time is 0 msec, maximum is 0 msec
        p12 = re.compile(
            r"^Last +flood +scan +time +is +(?P<last_flood_scan_time_msec>(\d+))"
            " +msec, +maximum +is +(?P<max_flood_scan_time_msec>(\d+)) +msec$")

        # Neighbor Count is 1, Adjacent neighbor count is 1
        p13 = re.compile(
            r"^Neighbor +Count +is +(?P<nbr_count>(\d+))"
            ", +Adjacent +neighbor +count +is"
            " +(?P<adj_nbr_count>(\d+))$")

        # Adjacent with neighbor 10.220.100.100
        p14 = re.compile(
            r"^Adjacent +with +neighbor +(?P<adj_with_nbr>(\S+))$")

        # Suppress hello for 0 neighbor(s)
        p15 = re.compile(r"^Suppress +hello +for +(?P<num_nbrs_suppress_hello>(\d+)) +neighbor\(s\)$")

        # Reference count is 6
        p16 = re.compile(r"^Reference +count +is +(?P<refrence_count>(\d+))$")

        # Loopback interface is treated as a stub Host
        p17 = re.compile(r"^(?P<loopback_txt>Loopback interface is treated as a stub Host)$")

        # Init vars
        ret_dict = {}

        # Address Family for ospfv3 is always ipv6
        af = "ipv6"

        for line in out.splitlines():
            line = line.strip()
            # GigabitEthernet0/0/0/0 is up, line protocol is up
            m = p1.match(line)
            if m:
                interface_dict = {}
                group = m.groupdict()

                # define vrf_dict dictionary and set to 'vrf'
                vrf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault('default', {})

                # define af_dict dictionary and set to 'address_family'
                af_dict = vrf_dict.setdefault('address_family', {}). \
                    setdefault(af, {})

                interface_name = group['interface']
                interface_dict.update({'enable': group['enable']})
                interface_dict.update({'line_protocol': group['line_protocol']})

            # Link Local address fe80:100:10::1, Interface ID 7
            m = p2.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'link_local_address': group['link_local_address']})
                interface_dict.update({'interface_id': int(group['interface_id'])})

            # Area 0, Process ID mpls1, Instance ID 0, Router ID 10.94.1.1
            m = p3.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'router_id': group['router_id']})

                instance_dict = af_dict.setdefault('instance', {}).setdefault(group['pid'], {})
                instance_id_dict = instance_dict.setdefault('instance_id', {}).setdefault(int(group['instance']), {})
                areas_dict = instance_id_dict.setdefault('areas', {}).setdefault(int(group['area']), {})
                interfaces_dict = areas_dict.setdefault('interfaces', {}).setdefault(interface_name, {})

            # Network Type POINT_TO_POINT, Cost: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'network_type': group['network_type']})
                interface_dict.update({'cost': int(group['cost'])})

            # BFD enabled, interval 150 msec, multiplier 3, mode Default
            m = p5.match(line)
            if m:
                group = m.groupdict()

                bfd_dict = interface_dict.setdefault('bfd', {})

                bfd_dict.update({'bfd_status': group['bfd_status']})
                bfd_dict.update({'interval': int(group['interval'])})
                bfd_dict.update({'multiplier': int(group['multi'])})
                bfd_dict.update({'mode': group['mode']})

            # Transmit Delay is 1 sec, State POINT_TO_POINT,
            m = p6.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'transmit_delay': int(group['delay'])})
                interface_dict.update({'state': group['state']})

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            m = p7.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'hello_interval': int(group['hello'])})
                interface_dict.update({'dead_interval': int(group['dead'])})
                interface_dict.update({'wait_interval': int(group['wait'])})
                interface_dict.update({'retransmit_interval': int(group['retransmit'])})

            # Hello due in 00:00:07:587
            m = p8.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'hello_timer': group['hello_timer']})

            # Index 1/1/1, flood queue length 0
            m = p9.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'index': group['index']})
                interface_dict.update({'flood_queue_length': int(group['flood_queue_length'])})

            # Next 0(0)/0(0)
            m = p10.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'next': group['next']})

            # Last flood scan length is 1, maximum is 3
            m = p11.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'last_flood_scan_length': int(group['last_flood_scan_length'])})
                interface_dict.update({'max_flood_scan_length': int(group['max_flood_scan_length'])})

            # Last flood scan time is 0 msec, maximum is 0 msec
            m = p12.match(line)
            if m:
                group = m.groupdict()

                interface_dict.update({'last_flood_scan_time_msec': int(group['last_flood_scan_time_msec'])})
                interface_dict.update({'max_flood_scan_time_msec': int(group['max_flood_scan_time_msec'])})

            # Neighbor Count is 1, Adjacent neighbor count is 1
            m = p13.match(line)
            if m:
                group = m.groupdict()

                neighbor_stats_dict = interface_dict.setdefault('statistics', {})
                neighbor_dict = interface_dict.setdefault('adjacent_neighbors', {})
                neighbor_dict.update({'nbr_count': int(group['nbr_count'])})
                neighbor_dict.update({'adj_nbr_count': int(group['adj_nbr_count'])})

            # Adjacent with neighbor 10.220.100.100
            m = p14.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict.update({'neighbor': group['adj_with_nbr']})

            # Suppress hello for 0 neighbor(s)
            m = p15.match(line)
            if m:
                group = m.groupdict()

                neighbor_stats_dict.update({'num_nbrs_suppress_hello': int(group['num_nbrs_suppress_hello'])})

            # Reference count is 6
            m1 = p16.match(line)
            m2 = p17.match(line)
            if m1:
                group = m1.groupdict()

                neighbor_stats_dict.update({'refrence_count': int(group['refrence_count'])})
                interfaces_dict.update(interface_dict)

            elif m2:
                group = m2.groupdict()

                loopback_keys = ['enable', 'line_protocol', 'link_local_address', 'interface_id',
                                 'network_type', 'cost', 'router_id']

                # prevents non-loopback interface information from carrying over into loopback interface
                temp_int_dict = interface_dict
                for k in list(interface_dict.keys()):
                    if k not in loopback_keys:
                        del temp_int_dict[k]
                interface_dict = temp_int_dict

                interface_dict.update({'loopback_txt': group['loopback_txt']})
                interfaces_dict.update(interface_dict)

        return ret_dict


class ShowOspfv3VrfAllInclusiveDatabaseRouterSchema(MetaParser):
    """Schema for show ospfv3 vrf all-inclusive database router"""
    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": int,
                                                            "adv_router": str,
                                                            "ospfv3": {
                                                                "header": {
                                                                    "options": str,
                                                                    "lsa_id": int,
                                                                    "age": int,
                                                                    "type": str,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    Optional(
                                                                        "routing_bit_enable"
                                                                    ): bool,
                                                                    Optional(
                                                                        "as_boundary_router"
                                                                    ): bool,
                                                                },
                                                                "body": {
                                                                    "num_of_links": int,
                                                                    "links": {
                                                                        Any(): {
                                                                            "type": str,
                                                                            "link_metric": int,
                                                                            "local_interface_id": int,
                                                                            "neighbor_interface_id": int,
                                                                            "neighbor_router_id": str,
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
                                },
                            },
                        },
                    },
                },
            },
        },
    }

class ShowOspfv3VrfAllInclusiveDatabaseRouter(ShowOspfv3VrfAllInclusiveDatabaseRouterSchema):
    ''' Parser for:
        *'show ospfv3 vrf all-inclusive database router'
    '''

    cli_command = ['show ospfv3 vrf all-inclusive database router']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        address_family = "ipv6"

        #Lsa Types
        # 1: Router
        # 2: Network Link
        # 3: Summary
        # 3: Summary Network
        # 3: Summary Net
        # 4: Summary ASB
        # 5: Type-5 AS External
        # 8: Link (Type-8)
        # 9: Intra Area Prefix'
        # 10: Opaque Area

        lsa_type_mapping = {
            'router': 1,
            'net': 2,
            'summary': 3,
            'summary net': 3,
            'summary asb': 4,
            'external': 5,
            'link (type-8)': 8,
            'intra area prefix': 9,
            'opaque': 10
        }

        # OSPFv3 Router with ID (96.96.96.96) (Process ID mpls1 VRF default)
        p1 = re.compile(r'^OSPFv3 +Router +with +ID +\((?P<router_id>(\S+))\) +\(Process +ID +(?P<instance>(\S+))(?: +VRF +(?P<vrf>(\S+)))?\)$')
        
        # Router Link States (Area 0)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z0-9\s\D]+)) +Link +States +\(Area'
                        ' +(?P<area>(\S+))\)$')

        # Routing Bit Set on this LSA
        p3 = re.compile(r"^Routing +Bit +Set +on +this +LSA$")

        # LS age: 1472
        p4 = re.compile(r"^LS +age: +(?P<age>(\d+))$")
 
        # Options: (V6-Bit E-Bit R-Bit DC-Bit)
        p5 = re.compile(r"^Options: +\((?P<options>(.*))\)$")

        # LS Type: Router Links
        p6 = re.compile(r"^LS +Type: +(?P<lsa_type>(.*))$")
        
        # Link State ID: 0
        p7 = re.compile(r"^Link +State +ID: +(?P<lsa_id>(\d+))" "(?: +\(.*\))?$")

        # Advertising Router: 25.97.1.1
        p8 = re.compile(r"^Advertising +Router: +(?P<adv_router>(\S+))$")

        # LS Seq Number: 80000007
        p9 = re.compile(r"^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$")

        # Checksum: 0x2132
        p10 = re.compile(r"^Checksum: +(?P<checksum>(\S+))$")

        # Length: 56
        p11 = re.compile(r"^Length: +(?P<length>(\d+))$")

        # AS Boundary Router
        p12 = re.compile(r"^AS +Boundary +Router$")

        # Number of Links: 2
        p13 = re.compile(r"^Number +of +(l|L)inks *: +(?P<num>(\d+))$")
   
        # Link connected to: a Transit Network
        p14_1 = re.compile(r"^Link +connected +to: +a +(?P<type>(.*))$")
        # Link connected to: another Router (point-to-point)
        p14_2 = re.compile(r"^Link +connected +to: +(?P<type>(.*))$")

        # Link Metric: 65535
        p15 = re.compile(r"^Link +Metric: +(?P<link_metric>(\d+))$")

        # Local Interface ID: 7
        p16 = re.compile(r"^Local +Interface +ID: +(?P<local_interface_id>(\d+))$")

        # Neighbor Interface ID: 6
        # Neighbor (DR) Interface ID: 6
        p17 = re.compile(r"^Neighbor.*Interface +ID: +(?P<neighbor_interface_id>(\d+))$")

        # Neighbor Router ID: 95.95.95.95
        # Neighbor (DR) Router ID: 96.96.96.96
        p18 = re.compile(r"^Neighbor.*Router +ID: +(?P<neighbor_router_id>(\S+))$")


        for line in out.splitlines():
            line = line.strip()

            # OSPFv3 Router with ID (96.96.96.96) (Process ID mpls1 VRF default)
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()["router_id"])
                instance = str(m.groupdict()["instance"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"

                inst_dict = (
                    ret_dict.setdefault("vrf", {})
                    .setdefault(vrf, {})
                    .setdefault("address_family", {})
                    .setdefault(address_family, {})
                    .setdefault("instance", {})
                    .setdefault(instance, {})
                )
                continue

            # Router Link States (Area 0)
            m = p2.match(line)
            if m:
                # get lsa_type
                lsa_type_key = m.groupdict()['lsa_type'].lower()
                if lsa_type_key in lsa_type_mapping:
                    lsa_type = lsa_type_mapping[lsa_type_key]

                # Set area
                if m.groupdict()["area"]:
                    try:
                        int(m.groupdict()["area"])
                        area = str(IPAddress(str(m.groupdict()["area"])))
                    except Exception:
                        area = str(m.groupdict()["area"])
                else:
                    area = "0.0.0.0"

                # Create dict structure
                type_dict = (
                    inst_dict.setdefault("areas", {})
                    .setdefault(area, {})
                    .setdefault("database", {})
                    .setdefault("lsa_types", {})
                    .setdefault(lsa_type, {})
                )

                # Set lsa_type
                type_dict["lsa_type"] = lsa_type
                continue

            # Routing Bit Set on this LSA
            m = p3.match(line)
            if m:
                routing_bit_enable = True
                continue

            # LS age: 1472
            m = p4.match(line)
            if m:
                age = int(m.groupdict()["age"])
                continue

            # Options: (V6-Bit E-Bit R-Bit DC-Bit)
            m = p5.match(line)
            if m:
                options = str(m.groupdict()["options"])
                continue

            # LS Type: Router Links
            m = p6.match(line)
            if m:
                lsa_type = str(m.groupdict()["lsa_type"])
                continue

            # Link State ID: 0
            m = p7.match(line)
            if m:
                lsa_id = int(m.groupdict()["lsa_id"])
                continue

            # Advertising Router: 25.97.1.1
            m = p8.match(line)
            if m:
                adv_router = str(m.groupdict()["adv_router"])
                lsa = str(lsa_id) + " " + adv_router

                # Reset counters for this lsa
                link_idx = 0

                # Create schema structure
                lsa_dict = type_dict.setdefault("lsas", {}).setdefault(lsa, {})

                # Set keys under 'lsa'
                lsa_dict["adv_router"] = adv_router
                try:
                    lsa_dict["lsa_id"] = lsa_id
                except Exception:
                    pass

                # Set header dict
                header_dict = lsa_dict.setdefault("ospfv3", {}).setdefault("header", {})

                # Set db_dict
                db_dict = lsa_dict.setdefault("ospfv3", {}).setdefault("body", {})

                # Set previously parsed values
                try:
                    header_dict["routing_bit_enable"] = routing_bit_enable
                    del routing_bit_enable
                except Exception:
                    pass
                try:
                    header_dict["age"] = age
                    del age
                except Exception:
                    pass
                try:
                    header_dict["options"] = options
                    del options
                except Exception:
                    pass
                try:
                    header_dict["type"] = lsa_type
                    del lsa_type
                except Exception:
                    pass
                try:
                    header_dict["lsa_id"] = lsa_id
                    del lsa_id
                except Exception:
                    pass
                try:
                    header_dict["adv_router"] = adv_router
                    del adv_router
                except Exception:
                    pass

            # LS Seq Number: 80000007
            m = p9.match(line)
            if m:
                header_dict["seq_num"] = str(m.groupdict()["ls_seq_num"])
                continue

            # Checksum: 0x2132
            m = p10.match(line)
            if m:
                header_dict["checksum"] = str(m.groupdict()["checksum"])
                continue

            # Length: 56
            m = p11.match(line)
            if m:
                header_dict["length"] = int(m.groupdict()["length"])
                continue
            
            # AS Boundary Router
            m = p12.match(line)
            if m:
                header_dict["as_boundary_router"] = True
                continue
            
            # Number of Links: 2
            m = p13.match(line)
            if m:
                db_dict["num_of_links"] = int(m.groupdict()["num"])
                continue

            # Link connected to: a Transit Network
            m = p14_1.match(line)
            if m:
                link_type = str(m.groupdict()["type"]).lower()
                continue

            # Link connected to: another Router (point-to-point)
            m = p14_2.match(line)
            if m:
                link_type = str(m.groupdict()["type"]).lower()
                continue

            # Link Metric: 65535
            m = p15.match(line)
            if m:
                link_idx = len(db_dict.get("links", {})) + 1
                link_dict = db_dict.setdefault("links", {}).setdefault(link_idx, {})

                link_dict["type"] = link_type
                link_dict["link_metric"] = int(m.groupdict()["link_metric"])
                continue

            # Local Interface ID: 7
            m = p16.match(line)
            if m:
                link_dict["local_interface_id"] = int(m.groupdict()["local_interface_id"])
                continue

            # Neighbor Interface ID: 6
            # Neighbor (DR) Interface ID: 6
            m = p17.match(line)
            if m:
                link_dict["neighbor_interface_id"] = int(m.groupdict()["neighbor_interface_id"])
                continue

            # Neighbor Router ID: 95.95.95.95
            # Neighbor (DR) Router ID: 96.96.96.96
            m = p18.match(line)
            if m:
                link_dict["neighbor_router_id"] = str(m.groupdict()["neighbor_router_id"])
                continue        

        return ret_dict


class ShowOspfv3VrfAllInclusiveDatabasePrefixSchema(MetaParser):
    ''' Schema for:
        * 'show ospfv3 vrf all-inclusive database prefix'
    '''
    schema = {
        "vrf": {
            Any(): {
                "address_family": {
                    Any(): {
                        "instance": {
                            Any(): {
                                Optional("areas"): {
                                    Any(): {
                                        "database": {
                                            "lsa_types": {
                                                Any(): {
                                                    "lsa_type": int,
                                                    "lsas": {
                                                        Any(): {
                                                            "lsa_id": int,
                                                            "adv_router": str,
                                                            "ospfv3": {
                                                                "header": {
                                                                    "lsa_id": int,
                                                                    "age": int,
                                                                    "type": str,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    "ref_lsa_type": str,
                                                                    "ref_lsa_id": int,
                                                                    "ref_adv_router": str,
                                                                    Optional("routing_bit_enable"): bool,
                                                                },
                                                                "body": {
                                                                    "number_of_prefix": int,
                                                                    "prefixes": {
                                                                        Any(): {
                                                                            "prefix_address": str,
                                                                            "prefix_length": int,
                                                                            "options": str,
                                                                            "metric": int,
                                                                            "priority": str,
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
                                },
                            },
                        },
                    },
                },
            },
        },
    }

class ShowOspfv3VrfAllInclusiveDatabasePrefix(ShowOspfv3VrfAllInclusiveDatabasePrefixSchema):
    ''' Parser for:
        *'show ospfv3 vrf all-inclusive database prefix'
    '''

    cli_command = ['show ospfv3 vrf all-inclusive database prefix']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}
        address_family = "ipv6"

        #Lsa Types
        # 1: Router
        # 2: Network Link
        # 3: Summary
        # 3: Summary Network
        # 3: Summary Net
        # 4: Summary ASB
        # 5: Type-5 AS External
        # 8: Link (Type-8)
        # 9: Intra Area Prefix'
        # 10: Opaque Area

        lsa_type_mapping = {
            'router': 1,
            'net': 2,
            'summary': 3,
            'summary net': 3,
            'summary asb': 4,
            'external': 5,
            'link (type-8)': 8,
            'intra area prefix': 9,
            'opaque': 10
        }

        # OSPFv3 Router with ID (25.97.1.1) (Process ID mpls1 VRF default)
        p1 = re.compile(r'^OSPFv3 +Router +with +ID +\(\S+\) +\(Process +ID +(?P<instance>(\S+))(?: +VRF +(?P<vrf>(\S+)))?\)$')

        # Intra Area Prefix Link States (Area 0)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z0-9\s\D]+)) +Link +States +\(Area'
                        ' +(?P<area>(\S+))\)$')

        # Routing Bit Set on this LSA
        p3 = re.compile(r'^Routing +Bit +Set +on +this +LSA$')
        # LS age: 852
        p4 = re.compile(r'^LS +age: +(?P<age>(\d+))$')

        # LS Type: Intra-Area-Prefix-LSA
        p5 = re.compile(r'^LS +Type: +(?P<lsa_type>(.*))$')

        # Link State ID: 0
        p6 = re.compile(r'^Link +State +ID: +(?P<lsa_id>(\d+))' '(?: +\(.*\))?$')

        # Advertising Router: 25.97.1.1
        p7 = re.compile(r'^Advertising +Router: +(?P<adv_router>(\S+))$')

        # LS Seq Number: 80000002
        p8 = re.compile(r'^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$')

        # Checksum: 0x66cb
        p9 = re.compile(r'^Checksum: +(?P<checksum>(\S+))$')

        # Length: 76
        p10 = re.compile(r'^Length: +(?P<length>(\d+))$')

        # Referenced LSA Type: 2001
        p11 = re.compile(r'^Referenced +LSA +Type: +(?P<ref_lsa_type>(.*))$')

        # Referenced Link State ID: 0
        p12 = re.compile(r'^Referenced +Link +State +ID: +(?P<ref_lsa_id>(\d+))' '(?: +\(.*\))?$')

        # Referenced Advertising Router: 25.97.1.1
        p13 = re.compile(r'^Referenced +Advertising +Router: +(?P<ref_adv_router>(\S+))$')

        # Number of Prefixes: 3
        p14 = re.compile(r'^Number +of +Prefixes: +(?P<number_of_prefix>(\S+))$')

        # Prefix Address: 2001:1100::1001
        p15 = re.compile(r'^Prefix +Address: +(?P<prefix_address>(\S+))$')

        # Prefix Length: 128, Options: None, Metric: 65535, Priority: Medium
        p16 = re.compile(
            r'^Prefix +Length: +(?P<prefix_length>(\d+))\s*,'
            ' +Options: +(?P<options>(\S+))\s*,'
            ' +Metric: +(?P<metric>(\d+))\s*,'
            ' +Priority: +(?P<priority>(\S+))$'
        )

        # OSPFv3 Router with ID (25.97.1.1) (Process ID mpls1 VRF default)
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                instance = str(m.groupdict()["instance"])
                if m.groupdict()["vrf"]:
                    vrf = str(m.groupdict()["vrf"])
                else:
                    vrf = "default"

                inst_dict = (
                    ret_dict.setdefault("vrf", {})
                    .setdefault(vrf, {})
                    .setdefault("address_family", {})
                    .setdefault(address_family , {})
                    .setdefault("instance", {})
                    .setdefault(instance, {})
                )
                continue

            # Intra Area Prefix Link States (Area 0)
            m = p2.match(line)
            if m:
                # get lsa_type
                lsa_type_key = m.groupdict()['lsa_type'].lower()
                if lsa_type_key in lsa_type_mapping:
                    lsa_type = lsa_type_mapping[lsa_type_key]

                # Set area
                if m.groupdict()["area"]:
                    try:
                        int(m.groupdict()["area"])
                        area = str(IPAddress(str(m.groupdict()["area"])))
                    except Exception:
                        area = str(m.groupdict()["area"])
                else:
                    area = "0.0.0.0"

                # Create dict structure
                type_dict = (
                    inst_dict.setdefault("areas", {})
                    .setdefault(area, {})
                    .setdefault("database", {})
                    .setdefault("lsa_types", {})
                    .setdefault(lsa_type, {})
                )

                # Set lsa_type
                type_dict["lsa_type"] = lsa_type
                continue

            # Routing Bit Set on this LSA
            m = p3.match(line)
            if m:
                routing_bit_enable = True
                continue

            # LS age: 1565
            m = p4.match(line)
            if m:
                age = int(m.groupdict()["age"])
                continue

            # LS Type: Intra-Area-Prefix-LSA
            m = p5.match(line)
            if m:
                lsa_type = str(m.groupdict()["lsa_type"])
                continue

            # Link State ID: 0
            m = p6.match(line)
            if m:
                lsa_id = int(m.groupdict()["lsa_id"])
                continue

            # Advertising Router: 25.97.1.1
            m = p7.match(line)
            if m:
                adv_router = str(m.groupdict()["adv_router"])
                lsa = str(lsa_id) + " " + adv_router

                # Reset counters for this lsa
                prefix_idx = 0

                # Create schema structure
                lsa_dict = type_dict.setdefault("lsas", {}).setdefault(lsa, {})

                # Set keys under 'lsa'
                lsa_dict["adv_router"] = adv_router
                try:
                    lsa_dict["lsa_id"] = lsa_id
                except Exception:
                    pass

                # Set header dict
                header_dict = lsa_dict.setdefault("ospfv3", {}).setdefault("header", {})

                # Set db_dict
                db_dict = (
                    lsa_dict.setdefault("ospfv3", {})
                    .setdefault("body", {})
                )

                # Set previously parsed values
                header_dict["routing_bit_enable"] = routing_bit_enable
                header_dict["age"] = age
                header_dict["type"] = lsa_type
                header_dict["lsa_id"] = lsa_id
                header_dict["adv_router"] = adv_router

            # LS Seq Number: 0x80000002
            m = p8.match(line)
            if m:
                header_dict["seq_num"] = str(m.groupdict()["ls_seq_num"])
                continue

            # Checksum: 0x7d61
            m = p9.match(line)
            if m:
                header_dict["checksum"] = str(m.groupdict()["checksum"])
                continue

            # Length: 36
            m = p10.match(line)
            if m:
                header_dict["length"] = int(m.groupdict()["length"])
                continue

            # Referenced LSA Type: 2001
            m = p11.match(line)
            if m:
                header_dict["ref_lsa_type"] = str(m.groupdict()["ref_lsa_type"])
                continue

            # Referenced Link State ID: 0
            m = p12.match(line)
            if m:
                header_dict["ref_lsa_id"] = int(m.groupdict()["ref_lsa_id"])
                continue

            # Referenced Advertising Router: 25.97.1.1
            m = p13.match(line)
            if m:
                header_dict["ref_adv_router"] = str(m.groupdict()["ref_adv_router"])
                continue

            # Number of Prefixes: 3
            m = p14.match(line)
            if m:
                db_dict["number_of_prefix"] = int(m.groupdict()["number_of_prefix"])
                continue

            # Prefix Address: 2001:1100::1001
            m = p15.match(line)
            if m:
                prefix_idx = len(db_dict.get("prefixes", {})) + 1
                prefix_dict = db_dict.setdefault("prefixes", {}).setdefault(prefix_idx, {})

                prefix_dict["prefix_address"] = str(m.groupdict()["prefix_address"])
                continue

            # Prefix Length: 128, Options: None, Metric: 65535, Priority: Medium
            m = p16.match(line)
            if m:
                prefix_dict["prefix_length"] = int(m.groupdict()["prefix_length"])
                prefix_dict["options"] = str(m.groupdict()["options"])
                prefix_dict["metric"] = int(m.groupdict()["metric"])
                prefix_dict["priority"] = str(m.groupdict()["priority"])
                continue

        return ret_dict
