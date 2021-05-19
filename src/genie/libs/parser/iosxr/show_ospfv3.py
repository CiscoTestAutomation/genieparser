''' show_ospfv3.py

Parser for the following commands:
    * show ospfv3 neighbor
    * show ospfv3 {process} neighbor
    * show ospfv3 vrf {vrf} neighbor
    * show ospfv3 database
    * show ospfv3 {process_id} database
'''
import re
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
                        '(, +VRF (?P<vrf>[\w]+))?$')

        # Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
        # 95.95.95.95     1     FULL/  -        00:00:37    5               GigabitEthernet0/0/0/1
        # 100.100.100.100 1     FULL/  -        00:00:38    6               GigabitEthernet0/0/0/0
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
            # 95.95.95.95     1     FULL/  -        00:00:37    5               GigabitEthernet0/0/0/1
            # 100.100.100.100 1     FULL/  -        00:00:38    6               GigabitEthernet0/0/0/0
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

        #OSPFv3 Router with ID(25.97.1.1) (Process ID mpls1)
        p1 = re.compile(r'^OSPFv3 +Router +with +ID +\((?P<router_id>(\S+))\) '
                        r'+\(Process +ID +(?P<instance>(\S+))(?:, +VRF +(?P<vrf>(\S+)))?\)$')

        #Router Link States (Area 0)
        #Link (Type-8) Link States (Area 0)
        #Intra Area Prefix Link States (Area 0)
        p2 = re.compile(r'^(?P<lsa_type>([a-zA-Z0-9\s\D]+)) +Link +States +\(Area'
                        ' +(?P<area>(\S+))\)$')

        #25.97.1.1       2019        0x8000007d 0            2           E
        #95.95.95.95     607         0x80000097 0            2           E
        p3 = re.compile(r'^(?P<adv_router>(\S+)) +(?P<age>(\d+)) +(?P<seq_num>(\S+))'
                        r' +(?P<fragment_id>(\d+)) +(?P<link_count>(\d+)) +(?P<bits>(\w+))$')

        #25.97.1.1       1518        0x80000086 7          Gi0/0/0/0
        #100.100.100.100 1841        0x80000079 6          Gi0/0/0/0
        p4 = re.compile(r'^(?P<adv_router>(\S+)) +(?P<age>(\d+)) +(?P<seq_num>(\S+))'
                        r' +(?P<link_id>(\d+)) +(?P<interface>([a-zA-Z0-9\/])+)$')

        #25.97.1.1       2019        0x80000078 0          0x2001      0
        #95.95.95.95     1583        0x80000086 0          0x2001      0
        p5 = re.compile(r'^(?P<adv_router>(\S+)) +(?P<age>(\d+)) +(?P<seq_num>(\S+))'
                        r' +(?P<link_id>(\d+)) +(?P<ref_lstype>(\S)+)'
                        r' +(?P<ref_lsid>(\d)+)$')

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 Router with ID(25.97.1.1) (Process ID mpls1)
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

                ospf_dict['router_id']=router_id
                area_dict = ospf_dict.setdefault('area', {}). \
                    setdefault(area, {})
                area_dict['area_id'] = int(group['area'])

                lsa_type_dict = area_dict.setdefault('database', {}). \
                    setdefault('lsa_types', {}). \
                    setdefault(lsa_type, {})

                # Set lsa_type
                lsa_type_dict['lsa_type'] = lsa_type
                continue

            # 25.97.1.1       2019        0x8000007d 0            2           E
            # 95.95.95.95     607         0x80000097 0            2           E
            m = p3.match(line)
            if m:
                group = m.groupdict()
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                fragment_id = int(group['fragment_id'])
                link_count = group['link_count']
                bits = group['bits']
                frag_adv_router = str(fragment_id)+ " " +adv_router

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

            # 25.97.1.1       1518        0x80000086 7          Gi0/0/0/0
            # 100.100.100.100 1841        0x80000079 6          Gi0/0/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                adv_router = group['adv_router']
                age = int(group['age'])
                seq = group['seq_num']
                link_id = int(group['link_id'])
                interface = group['interface']
                link_adv_router = str(link_id)+ " " +adv_router

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

            # 25.97.1.1       2019        0x80000078 0          0x2001      0
            # 95.95.95.95     1583        0x80000086 0          0x2001      0
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

                #lsas dict
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
                                                            "lsa_id": str,
                                                            "adv_router": str,
                                                            "ospfv3": {
                                                                "header": {
                                                                    "lsa_id": str,
                                                                    "age": int,
                                                                    "type": str,
                                                                    "adv_router": str,
                                                                    "seq_num": str,
                                                                    "checksum": str,
                                                                    "length": int,
                                                                    "ref_lsa_type": str,
                                                                    "ref_lsa_id": str,
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
        af = "ipv6"

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
        #p1 = re.compile(r'^OSPFv3 +Router +with +ID +\((?P<router_id>(\S+))\) '
        #                r'+\(Process +ID +(?P<instance>(\S+))(?: +VRF +(?P<vrf>(\S+)))?\)$')

        p1 = re.compile(r'^OSPFv3 +Router +with +ID +\((?P<router_id>(\S+))\) +\(Process +ID +(?P<instance>(\S+))(?: +VRF +(?P<vrf>(\S+)))?\)$')

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
        p6 = re.compile(r'^Link +State +ID: +(?P<lsa_id>(\S+))' '(?: +\(.*\))?$')

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
        p12 = re.compile(r'^Referenced +Link +State +ID: +(?P<ref_lsa_id>(\S+))' '(?: +\(.*\))?$')

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
                    .setdefault(af, {})
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
                lsa_id = str(m.groupdict()["lsa_id"])
                continue

            # Advertising Router: 25.97.1.1
            m = p7.match(line)
            if m:
                adv_router = str(m.groupdict()["adv_router"])
                lsa = lsa_id + " " + adv_router

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
                header_dict["ref_lsa_id"] = str(m.groupdict()["ref_lsa_id"])
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
                       



