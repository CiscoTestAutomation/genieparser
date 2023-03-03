""" ShowOspfv3SummaryPrefix.py

IOSXE parser for the following show command:
    * show ospfv3 summary-prefix
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, Default

# ===============================================
# Schema for 'show ospfv3 summary-prefix'
# Optional: allowing either ipv4 or ipv6 or both
# ===============================================

class ShowOspfv3SummaryPrefixSchema(MetaParser):
    schema = {
        'process_id': {
            Any(): {
                'address_family': str,
                'router_id': str,
                'null_route': {
                    Any(): {
                        'null_metric': str,
                    },
                },
                'summary': {
                    Any(): {
                        'sum_type': str,
                        'sum_tag': int,
                        'sum_metric': int
                    },
                },
            },
        },
    }


# ====================================
# Parser for 'ShowOspfv3SummaryPrefix'
# ====================================

class ShowOspfv3SummaryPrefix(ShowOspfv3SummaryPrefixSchema):
    """
        Router#sh ospfv3 summary-prefix

                OSPFv3 10000 address-family ipv6 (router-id 10.2.2.21)

        10:2::/96           Metric <unreachable>
        10:2:2::/96         Metric 111, External metric type 2, Tag 111
        Router#
    """

    cli_command = 'show ospfv3 summary-prefix'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # init var
        ret_dict = {}
        ospf_id = ""

        # OSPFv3 10000 address-family ipv6 (router-id 10.2.2.21)
        p1 = re.compile(
            r'^OSPFv3 +(?P<ospf_id>(\d+)) +address-family +(?P<address_family>(\S+)) +\(router-id +(?P<router_id>(\S+))\)')

        # 10:2::/96           Metric <unreachable>
        p2 = re.compile(r'^(?P<null_prefix>(\S+)) +.* Metric\s+(?P<null_metric>(\S+$))')

        # 10:2:2::/96         Metric 111, External metric type 2, Tag 111
        p3 = re.compile(
            r'^(?P<sum_prefix>(\S+)) +.* Metric\s+(?P<sum_metric>(\d+)),.* +type +(?P<sum_type>(\d)),\s+Tag +(?P<sum_tag>(\S+))')

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['process_id'] = {}
                ospf_id = group['ospf_id']
                ret_dict['process_id'][ospf_id] = {}
                ret_dict['process_id'][ospf_id]['null_route'] = {}
                ret_dict['process_id'][ospf_id]['summary'] = {}
                ret_dict['process_id'][ospf_id]['address_family'] = group['address_family']
                ret_dict['process_id'][ospf_id]['router_id'] = group['router_id']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['null_prefix']:
                    n_prefix = group['null_prefix']
                    ret_dict['process_id'][ospf_id]['null_route'][n_prefix] = {}
                    ret_dict['process_id'][ospf_id]['null_route'][n_prefix]['null_metric'] = group['null_metric']
                    continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['sum_prefix']:
                    prefix = group['sum_prefix']
                    ret_dict['process_id'][ospf_id]['summary'][prefix] = {}
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_metric'] = int(group['sum_metric'])
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_type'] = group['sum_type']
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_tag'] = int(group['sum_tag'])
                    continue


        return ret_dict

# ===============================================
# schema for:
#   * show ospfv3 vrf {vrf_id} neighbor
# ======================================================
class ShowOspfv3vrfNeighborSchema(MetaParser):
    """Schema detail for:
          * show ospfv3 vrf {vrf_id} neighbor
     """
    schema = {
        'process_id': int,
        'address_family': str,
        'router_id': str,
        'vrfs': {
            int: {
                'neighbor_id': {
                    str: {
                        'priority': int,
                        'state': str,
                        'dead_time': str,
                        'address': int,
                        'interface': str
                        },
                   },
               },
            },
        }

# ======================================================
# parser for:
#   * show ospfv3 vrf {vrf_id} neighbor
# ======================================================
class ShowOspfv3vrfNeighbor(ShowOspfv3vrfNeighborSchema):
    """parser details for:
        * show ospfv3 vrf {vrf_id} neighbor
    """

    cli_command = 'show ospfv3 vrf {vrf_id} neighbor'

    def cli(self, vrf_id='', output=None):
        cmd = self.cli_command.format(vrf_id=vrf_id)

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # OSPFv3 2 address-family ipv6 vrf 2 (router-id 173.19.2.2)
        p1 = re.compile(
            r'^OSPFv3\s+(?P<process_id>\d+)+\s+address-family\s(?P<address_family>\w+)\s+vrf\s(?P<vrf_id>\d+)'
            r'\s+\(router-id\s+(?P<router_id>[\d\.\/]+)\)$')

        # Neighbor ID     Pri   State           Dead Time   Address         Interface
        # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
        # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
        # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
        p2 = re.compile(r'^(?P<neighbor_id>\S+)\s+(?P<priority>\d+) +(?P<state>[A-Z]+/\s*[A-Z-]*)'
                        r' +(?P<dead_time>(\d+:){2}\d+) +(?P<address>[\d\.\/]+) +(?P<interface>\w+\s*\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 2 address-family ipv6 vrf 2 (router-id 173.19.2.2)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_id = int(group['vrf_id'])
                ret_dict['process_id'] = int(group['process_id'])
                ret_dict['address_family'] = group['address_family']
                ret_dict['router_id'] = group['router_id']
                vrf_dict = ret_dict.setdefault('vrfs', {}).setdefault(vrf_id, {})

            # Neighbor ID     Pri   State           Dead Time   Address         Interface
            # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_id = group['neighbor_id']
                neighbor_dict = vrf_dict.setdefault('neighbor_id', {}).setdefault(neighbor_id, {})
                neighbor_dict['priority'] = int(group['priority'])
                neighbor_dict['state'] = group['state']
                neighbor_dict['dead_time'] = group['dead_time']
                neighbor_dict['address'] = int(group['address'])
                neighbor_dict['interface'] = group['interface']

                continue

        return ret_dict


class ShowOspfv3NeighborSchema(MetaParser):

    """Schema for show ospfv3 {pid} neighbor"""

    schema = {
        'pid': int,
        'address_family': str,
        'router_id': str,
        'interface_id': {
            Any(): {
                'priority': int,
                'neighbor_id': str,
                'state': str,
                'dead_time': str,
                'interface': str
            }
        }
    }


class ShowOspfv3Neighbor(ShowOspfv3NeighborSchema):

    """Parser for show ospfv3 {pid} neighbor"""

    cli_command = 'show ospfv3 {pid} neighbor'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\(router-id\s+("
                        r"?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$")
        
        # 2.200.33.3        1   FULL/BDR        00:00:33    4584            Vlan3892
        p2 = re.compile(r"^(?P<neighbor_id>(\d{1,3}\.){3}\d{1,3})\s+(?P<priority>\d+)\s+(?P<state>\S+)\s+("
                        r"?P<dead_time>\S+)\s+(?P<int_id>\d+)\s+(?P<interface>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['router_id'] = dict_val['router_id']
                continue

            # 2.200.33.3  1 FULL/BDR  00:00:33  4584  Vlan3892
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                int_id_var = dict_val['int_id']
                int_id_dict = ret_dict.setdefault('interface_id', {}).setdefault(int_id_var, {})
                int_id_dict['priority'] = int(dict_val['priority'])
                int_id_dict['neighbor_id'] = dict_val['neighbor_id']
                int_id_dict['state'] = dict_val['state']
                int_id_dict['dead_time'] = dict_val['dead_time']
                int_id_dict['interface'] = dict_val['interface']
                continue

        return ret_dict


class ShowOspfv3RetransmissionListSchema(MetaParser):

    """Schema for show ospfv3 {pid} retransmission-list"""

    schema = {
        'pid': int,
        'address_family': str,
        'router_id': str,
        'interface': {
            Any(): {
                'neighbor_id': str
            }
        }
    }


class ShowOspfv3RetransmissionList(ShowOspfv3RetransmissionListSchema):

    """Parser for show ospfv3 {pid} retransmission-list"""

    cli_command = 'show ospfv3 {pid} retransmission-list'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))
        
        # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\(router-id\s+("
                        r"?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$")
        
        # Neighbor 2.200.33.3, interface Vlan3892
        p2 = re.compile(r"^Neighbor\s+(?P<neighbor_id>(\d{1,3}\.){3}\d{1,3}),\s+interface\s+(?P<interface>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['router_id'] = dict_val['router_id']
                continue
            
            # Neighbor 2.200.33.3, interface Vlan3892
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_var = dict_val['interface']
                ret_dict.setdefault('interface', {}).setdefault(interface_var, {'neighbor_id': dict_val['neighbor_id']})
                continue

        return ret_dict


class ShowOspfv3RequestListSchema(MetaParser):

    """Schema for show ospfv3 {pid} request-list"""

    schema = {
        'pid': int,
        'address_family': str,
        'router_id': str,
        'interface': {
            Any(): {
                'neighbor_id': str,
                'address': str,
                'req_list_size': int,
                'max_list_size': int
            }
        }
    }


class ShowOspfv3RequestList(ShowOspfv3RequestListSchema):

    """Parser for show ospfv3 {pid} request-list"""

    cli_command = 'show ospfv3 {pid} request-list'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\(router-id\s+("
                        r"?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$")
        
        # Neighbor 2.200.33.3, interface Vlan3892 address FE80::3E57:31FF:FE04:6B05
        p2 = re.compile(r"^Neighbor\s+(?P<neighbor_id>(\d{1,3}\.){3}\d{1,3}),\s+interface\s+("
                        r"?P<interface>\S+)\s+address\s+(?P<address>\S+)$")
        
        # Request list size 0, maximum list size 1
        p2_1 = re.compile(r"^Request\s+list\s+size\s+(?P<req_list_size>\d+),\s+maximum\s+list\s+size\s+("
                          r"?P<max_list_size>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['router_id'] = dict_val['router_id']
                continue
            
            # Neighbor 2.200.33.3, interface Vlan3892 address FE80::3E57:31FF:FE04:6B05
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_var = dict_val['interface']
                interface_dict = ret_dict.setdefault('interface', {}).setdefault(interface_var, {})
                interface_dict['neighbor_id'] = dict_val['neighbor_id']
                interface_dict['address'] = dict_val['address']
                continue
            
            # Request list size 0, maximum list size 1
            match_obj = p2_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict = ret_dict.setdefault('interface', {}).setdefault(interface_var, {})
                interface_dict['req_list_size'] = int(dict_val['req_list_size'])
                interface_dict['max_list_size'] = int(dict_val['max_list_size'])
                continue

        return ret_dict


class ShowOspfv3StatisticDetailSchema(MetaParser):

    """Schema for show ospfv3 {pid} statistic detail"""

    schema = {
        'pid': int,
        'address_family': str,
        'router_id': str,
        'area': int,
        'spf_alg_executed_times': int,
        'spf': {
            Any(): {
                'executed_time': str,
                'spf_type': str,
                'spt': int,
                'sum': int,
                'ext': int,
                'total': int,
                'prefix': int,
                'd_sum': int,
                'd_ext': int,
                'd_int': int,
                'lsids': {
                    'r': int,
                    'n': int,
                    'prefix': int,
                    'sn': int,
                    'sa': int,
                    'x7': int
                },
                'lsa_changed': int,
                'change_record': str,
                'adv_routers_list': list,
            }
        }
    }


class ShowOspfv3StatisticDetail(ShowOspfv3StatisticDetailSchema):

    """Parser for show ospfv3 {pid} statistic detail"""

    cli_command = 'show ospfv3 {pid} statistic detail'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # OSPFv3 5 address-family ipv6 (router-id 1.1.1.1)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\("
                        r"router-id\s+(?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$") 
        
        # SPF 1 executed 16:03:11 ago, SPF type Full
        p2 = re.compile(r"^SPF\s+(?P<spf_id>\d+)\s+executed\s+(?P<executed_time>\S+)\s+ago,\s+SPF\s+type\s+("
                        r"?P<spf_type>\w+)$") 
        
        # SPT    Prefix D-Int  Sum    D-Sum  Ext    D-Ext  Total
        # 0      0      0      0      0      0      0      0
        p2_1 = re.compile(r"^(?P<spt>\d+)\s+(?P<prefix>\d+)\s+(?P<d_int>\d+)\s+(?P<sum>\d+)\s+(?P<d_sum>\d+)\s+("
                          r"?P<ext>\d+)\s+(?P<d_ext>\d+)\s+(?P<total>\d+)$") 
        
        # LSAs changed 1
        p2_2 = re.compile(r"^LSAs\s+changed\s+(?P<lsa_changed>\d+)$")

        # LSIDs processed R:1 N:0 Prefix:0 SN:0 SA:0 X7:0
        p2_3 = re.compile(r"^LSIDs\s+processed\s+R:(?P<r>\d+)\s+N:(?P<n>\d+)\s+Prefix:("
                          r"?P<prefix>\d+)\s+SN:(?P<sn>\d+)\s+SA:(?P<sa>\d+)\s+X7:(?P<x7>\d+)$") 
        
        # Change record R
        p2_4 = re.compile(r"^Change\s+record\s+(?P<change_record>\w+)$")
        
        # 1.1.1.1/0(R)
        p2_5 = re.compile(r"^(?P<adv_routers_list>.*\/.*)$")

        # Area 0: SPF algorithm executed 1 times
        p3 = re.compile(r"^Area\s+(?P<area>\d+):\s+SPF\s+algorithm\s+executed\s+("
                        r"?P<spf_alg_executed_times>\d+)\s+times$") 

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 5 address-family ipv6 (router-id 1.1.1.1)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['router_id'] = dict_val['router_id']
                continue

            # SPF 1 executed 16:03:11 ago, SPF type Full
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                spf_id_var = dict_val['spf_id']
                if 'spf' not in ret_dict:
                    ret_dict.setdefault('spf', {})
                if spf_id_var not in ret_dict['spf']:
                    spf_id_dict = ret_dict['spf'].setdefault(spf_id_var, {})
                spf_id_dict['executed_time'] = dict_val['executed_time']
                spf_id_dict['spf_type'] = dict_val['spf_type']
                continue

            # SPT    Prefix D-Int  Sum    D-Sum  Ext    D-Ext  Total
            # 0      0      0      0      0      0      0      0
            match_obj = p2_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'spf' not in ret_dict:
                    ret_dict.setdefault('spf', {})
                if spf_id_var not in ret_dict['spf']:
                    spf_id_dict = ret_dict['spf'].setdefault(spf_id_var, {})
                spf_id_dict['spt'] = int(dict_val['spt'])
                spf_id_dict['sum'] = int(dict_val['sum'])
                spf_id_dict['ext'] = int(dict_val['ext'])
                spf_id_dict['total'] = int(dict_val['total'])
                spf_id_dict['prefix'] = int(dict_val['prefix'])
                spf_id_dict['d_sum'] = int(dict_val['d_sum'])
                spf_id_dict['d_ext'] = int(dict_val['d_ext'])
                spf_id_dict['d_int'] = int(dict_val['d_int'])
                continue

            # LSAs changed 1
            match_obj = p2_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'spf' not in ret_dict:
                    ret_dict.setdefault('spf', {})
                if spf_id_var not in ret_dict['spf']:
                    spf_id_dict = ret_dict['spf'].setdefault(spf_id_var, {})
                spf_id_dict['lsa_changed'] = int(dict_val['lsa_changed'])
                continue

            # LSIDs processed R:1 N:0 Prefix:0 SN:0 SA:0 X7:0
            match_obj = p2_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'spf' not in ret_dict:
                    ret_dict.setdefault('spf', {})
                if spf_id_var not in ret_dict['spf']:
                    spf_id_dict = ret_dict['spf'].setdefault(spf_id_var, {})
                lsid_dict = spf_id_dict.setdefault('lsids', {})
                lsid_dict['r'] = int(dict_val['r'])
                lsid_dict['n'] = int(dict_val['n'])
                lsid_dict['prefix'] = int(dict_val['prefix'])
                lsid_dict['sn'] = int(dict_val['sn'])
                lsid_dict['sa'] = int(dict_val['sa'])
                lsid_dict['x7'] = int(dict_val['x7'])
                continue

            # Change record R
            match_obj = p2_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'spf' not in ret_dict:
                    ret_dict.setdefault('spf', {})
                if spf_id_var not in ret_dict['spf']:
                    spf_id_dict = ret_dict['spf'].setdefault(spf_id_var, {})
                spf_id_dict['change_record'] = dict_val['change_record']
                continue

            # 1.1.1.1/0(R)
            match_obj = p2_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'spf' not in ret_dict:
                    ret_dict.setdefault('spf', {})
                if spf_id_var not in ret_dict['spf']:
                    spf_id_dict = ret_dict['spf'].setdefault(spf_id_var, {})
                spf_id_dict['adv_routers_list'] = dict_val['adv_routers_list'].split()
                continue

            # Area 0: SPF algorithm executed 1 times
            match_obj = p3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['area'] = int(dict_val['area'])
                ret_dict['spf_alg_executed_times'] = int(dict_val['spf_alg_executed_times'])
                continue

        return ret_dict


class ShowOspfv3InterfaceSchema(MetaParser):

    """Schema for show ospfv3 {pid} interface"""

    schema = {
        'interfaces': {
            Any(): {
                'int_status': str,
                'line_protocol': str,
                'link_local_address': str,
                'int_id': int,
                'area': int,
                'pid': int,
                'instance_id': int,
                'router_id': str,
                'network_type': str,
                'cost': int,
                'state': str,
                'priority': int,
                'hello': int,
                'dead': int,
                'retransmit': int,
                'wait': int,
                'transmit_delay': int,
                Optional('bfd_status'): str,
                Optional('Designated_router'): str,
                Optional('dr_local_address'): str,
                Optional('backup_designated_router'): str,
                Optional('bdr_local_address'): str,
                Optional('hello_due'): str,
                Optional('gr_support'): str,
                Optional('index'): str,
                Optional('flood_queue_length'): int,
                Optional('next_index'): str,
                Optional('flood_scan_length'): int,
                Optional('flood_scan_length_maximum'): int,
                Optional('flood_scan_time'): int,
                Optional('flood_scan_time_maximum'): int,
                Optional('neighbor_count'): int,
                Optional('adj_neighbor_count'): int,
                Optional('neighbor_id'): str,
                Optional('dr_or_bdr'): str,
                Optional('suppress_hello'): int
            }
        }
    }


class ShowOspfv3Interface(ShowOspfv3InterfaceSchema):

    """Parser for show ospfv3 {pid} interface"""

    cli_command = 'show ospfv3 {pid} interface'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # TwoGigabitEthernet1/0/10 is down, line protocol is down (notconnect) 
        p1 = re.compile(r"^(?P<interface>\S+)\s+is\s+(?P<int_status>\w+),\s+line\s+protocol\s+is\s+("
                        r"?P<line_protocol>\w+)\s*(.*)?$")
        
        # Link Local Address FE80::E75:BDFF:FE6E:DB47, Interface ID 18 (snmp-if-index)
        p1_1 = re.compile(r"^Link\s+Local\s+Address\s+(?P<link_local_address>\S+),\s+Interface\s+ID\s+("
                          r"?P<int_id>\d+)\s+\(snmp-if-index\)$")
        
        # Area 0, Process ID 5, Instance ID 0, Router ID 1.1.1.1
        p1_2 = re.compile(r"^Area\s+(?P<area>\d+),\s+Process\s+ID\s+(?P<pid>\d+),\s+Instance\s+ID\s+("
                          r"?P<instance_id>\d+),\s+Router\s+ID\s+(?P<router_id>(\d{1,3}\.){3}\d{1,3})$")
        
        # Network Type BROADCAST, Cost: 1
        p1_3 = re.compile(r"^Network\s+Type\s+(?P<network_type>\w+),\s+Cost:\s+(?P<cost>\d+)$")
        
        # Transmit Delay is 1 sec, State DOWN, Priority 1
        p1_4 = re.compile(r"^Transmit\s+Delay\s+is\s+(?P<transmit_delay>\d+)\s+sec,\s+State\s+(?P<state>\w+),"
                          r"\s+Priority\s+(?P<priority>\d+)[,\s+BFD\s+]*(?P<bfd_status>\w*)$")
        
        # Designated Router (ID) 2.200.1.2, local address FE80::72B3:17FF:FE1E:A982
        p1_5 = re.compile(r"^Designated\s+Router\s+\(ID\)\s+(?P<Designated_router>(\d{1,3}\.){3}\d{1,3}),"
                          r"\s+local\s+address\s+(?P<dr_local_address>\S+)$")
        
        # Backup Designated router (ID) 2.200.33.3, local address FE80::3E57:31FF:FE04:6B05
        p1_6 = re.compile(r"^Backup\s+Designated\s+router\s+\(ID\)\s+(?P<backup_designated_router>(\d{1,"
                          r"3}\.){3}\d{1,3}),\s+local\s+address\s+(?P<bdr_local_address>\S+)$")
        
        # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
        p1_7 = re.compile(r"^Timer\s+intervals\s+configured,\s+Hello\s+(?P<hello>\d+),\s+Dead\s+(?P<dead>\d+),"
                          r"\s+Wait\s+(?P<wait>\d+),\s+Retransmit\s+(?P<retransmit>\d+)$")
        
        # Hello due in 00:00:04
        p1_8 = re.compile(r"^Hello\s+due\s+in\s+(?P<hello_due>\S+)$")
        
        # Graceful restart helper support enabled
        p1_9 = re.compile(r"^Graceful\s+restart\s+helper\s+support\s+(?P<gr_support>\w+)$")
        
        # Index 1/11/11, flood queue length 0
        p1_10 = re.compile(r"^Index\s+(?P<index>\S+),\s+flood\s+queue\s+length\s+(?P<flood_queue_length>\d+)$")
        
        # Next 0x0(0)/0x0(0)/0x0(0)
        p1_11 = re.compile(r"^Next\s+(?P<next_index>\S+)$")
        
        #  Last flood scan length is 28, maximum is 253
        p1_12 = re.compile(r"^Last\s+flood\s+scan\s+length\s+is\s+(?P<flood_scan_length>\d+),\s+maximum\s+is\s+("
                           r"?P<flood_scan_length_maximum>\d+)$")
        
        # Last flood scan time is 0 msec, maximum is 2 msec
        p1_13 = re.compile(r"^Last\s+flood\s+scan\s+time\s+is\s+(?P<flood_scan_time>\d+)\s+msec,"
                           r"\s+maximum\s+is\s+(?P<flood_scan_time_maximum>\d+)\s+msec$")
        
        # Neighbor Count is 1, Adjacent neighbor count is 1 
        p1_14 = re.compile(r"^Neighbor\s+Count\s+is\s+(?P<neighbor_count>\d+),"
                           r"\s+Adjacent\s+neighbor\s+count\s+is\s+(?P<adj_neighbor_count>\d+)$")
        
        # Adjacent with neighbor 2.200.33.3  (Backup Designated Router)
        p1_15 = re.compile(r"^Adjacent\s+with\s+neighbor\s+(?P<neighbor_id>(\d{1,3}\.){3}\d{1,3})\s+\(("
                           r"?P<dr_or_bdr>.*)\)$")
        
        # Suppress hello for 0 neighbor(s)
        p1_16 = re.compile(r"^Suppress\s+hello\s+for\s+(?P<suppress_hello>\d+)\s+neighbor\(s\)$")

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # TwoGigabitEthernet1/0/10 is down, line protocol is down (notconnect)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_var = dict_val['interface']
                if 'interfaces' not in ret_dict:
                    ret_dict.setdefault('interfaces', {})
                interface_dict = ret_dict['interfaces'].setdefault(interface_var, {})
                interface_dict['int_status'] = dict_val['int_status']
                interface_dict['line_protocol'] = dict_val['line_protocol']
                continue

            # Link Local Address FE80::E75:BDFF:FE6E:DB47, Interface ID 18 (snmp-if-index)
            match_obj = p1_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['link_local_address'] = dict_val['link_local_address']
                interface_dict['int_id'] = int(dict_val['int_id'])
                continue

            # Area 0, Process ID 5, Instance ID 0, Router ID 1.1.1.1
            match_obj = p1_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['area'] = int(dict_val['area'])
                interface_dict['pid'] = int(dict_val['pid'])
                interface_dict['instance_id'] = int(dict_val['instance_id'])
                interface_dict['router_id'] = dict_val['router_id']
                continue

            # Network Type BROADCAST, Cost: 1
            match_obj = p1_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['network_type'] = dict_val['network_type']
                interface_dict['cost'] = int(dict_val['cost'])
                continue

            # Transmit Delay is 1 sec, State DOWN, Priority 1
            match_obj = p1_4.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['state'] = dict_val['state']
                interface_dict['priority'] = int(dict_val['priority'])
                if dict_val['bfd_status']:
                    interface_dict['bfd_status'] = dict_val['bfd_status']
                interface_dict['transmit_delay'] = int(dict_val['transmit_delay'])
                continue

            # Designated Router (ID) 2.200.1.2, local address FE80::72B3:17FF:FE1E:A982
            match_obj = p1_5.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['Designated_router'] = dict_val['Designated_router']
                interface_dict['dr_local_address'] = dict_val['dr_local_address']
                continue

            # Backup Designated router (ID) 2.200.33.3, local address FE80::3E57:31FF:FE04:6B05
            match_obj = p1_6.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['backup_designated_router'] = dict_val['backup_designated_router']
                interface_dict['bdr_local_address'] = dict_val['bdr_local_address']
                continue

            # Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
            match_obj = p1_7.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['hello'] = int(dict_val['hello'])
                interface_dict['dead'] = int(dict_val['dead'])
                interface_dict['retransmit'] = int(dict_val['retransmit'])
                interface_dict['wait'] = int(dict_val['wait'])
                continue

            # Hello due in 00:00:04
            match_obj = p1_8.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['hello_due'] = dict_val['hello_due']
                continue

            # Graceful restart helper support enabled
            match_obj = p1_9.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['gr_support'] = dict_val['gr_support']
                continue

            # Index 1/11/11, flood queue length 0
            match_obj = p1_10.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['index'] = dict_val['index']
                interface_dict['flood_queue_length'] = int(dict_val['flood_queue_length'])
                continue

            # Next 0x0(0)/0x0(0)/0x0(0)
            match_obj = p1_11.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['next_index'] = dict_val['next_index']
                continue

            #  Last flood scan length is 28, maximum is 253
            match_obj = p1_12.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['flood_scan_length'] = int(dict_val['flood_scan_length'])
                interface_dict['flood_scan_length_maximum'] = int(dict_val['flood_scan_length_maximum'])
                continue

            # Last flood scan time is 0 msec, maximum is 2 msec
            match_obj = p1_13.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['flood_scan_time'] = int(dict_val['flood_scan_time'])
                interface_dict['flood_scan_time_maximum'] = int(dict_val['flood_scan_time_maximum'])
                continue

            # Neighbor Count is 1, Adjacent neighbor count is 1 
            match_obj = p1_14.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['neighbor_count'] = int(dict_val['neighbor_count'])
                interface_dict['adj_neighbor_count'] = int(dict_val['adj_neighbor_count'])
                continue

            # Adjacent with neighbor 2.200.33.3  (Backup Designated Router)
            match_obj = p1_15.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['neighbor_id'] = dict_val['neighbor_id']
                interface_dict['dr_or_bdr'] = dict_val['dr_or_bdr']
                continue

            # Suppress hello for 0 neighbor(s)
            match_obj = p1_16.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_dict['suppress_hello'] = int(dict_val['suppress_hello'])
                continue

        return ret_dict


class ShowOspfv3GracefulrestartSchema(MetaParser):
    """Schema for show ospfv3 {pid} graceful-restart"""

    schema = {
        'address_family': str,
        'pid': int,
        'router_id': str,
        'graceful_restart': {
            Optional('router_mode'): str,
            Optional('limit_in_sec'): int,
            'neighbors': int
        }
    }


class ShowOspfv3Gracefulrestart(ShowOspfv3GracefulrestartSchema):
    """Parser for show ospfv3 {pid} graceful-restart"""

    cli_command = 'show ospfv3 {pid} graceful-restart'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # OSPFv3 5 address-family ipv6 (router-id 1.1.1.1)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\("
                        r"router-id\s+(?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$")
        
        # Router is running in SSO mode
        p2 = re.compile(r"^Router\s+is\s+running\s+in\s+(?P<router_mode>\w+)\s+mode$")

        # restart-interval limit: 3 sec
        p2_1 = re.compile(r"^restart-interval\s+limit:\s+(?P<limit_in_sec>\d+)\s+sec$")

        # Number of neighbors performing Graceful Restart is 4
        p3 = re.compile(r"^Number\s+of\s+neighbors\s+performing\s+Graceful\s+Restart\s+is\s+(?P<neighbors>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 5 address-family ipv6 (router-id 1.1.1.1)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['router_id'] = dict_val['router_id']
                continue
            
            # Router is running in SSO mode
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'graceful_restart' not in ret_dict:
                    graceful_restart = ret_dict.setdefault('graceful_restart', {})
                graceful_restart['router_mode'] = dict_val['router_mode']
                continue
            
            # restart-interval limit: 3 sec
            match_obj = p2_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'graceful_restart' not in ret_dict:
                    graceful_restart = ret_dict.setdefault('graceful_restart', {})
                graceful_restart['limit_in_sec'] = int(dict_val['limit_in_sec'])
                continue
            
            # Number of neighbors performing Graceful Restart is 4
            match_obj = p3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'graceful_restart' not in ret_dict:
                    graceful_restart = ret_dict.setdefault('graceful_restart', {})
                graceful_restart['neighbors'] = int(dict_val['neighbors'])
                continue
        return ret_dict


class ShowOspfv3FloodListSchema(MetaParser):

    """Schema for show ospfv3 {pid} flood-list"""

    schema = {
        'pid': int,
        'address_family': str,
        'router_id': str,
        'interfaces': {
            Any(): { 
                'queue_length': int
            }
        }
    }


class ShowOspfv3FloodList(ShowOspfv3FloodListSchema):

    """Parser for show ospfv3 {pid} flood-list"""

    cli_command = 'show ospfv3 {pid} flood-list'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\("
                        r"router-id\s+(?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$") 
        
        # Interface Vlan3892, Queue length 0
        p2 = re.compile(r"^Interface\s+(?P<interface>\S+),\s+Queue\s+length\s+(?P<queue_length>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 50 address-family ipv6 (router-id 2.200.1.2)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['router_id'] = dict_val['router_id']
                continue

            # Interface Vlan3892, Queue length 0
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                interface_var = dict_val['interface']
                if 'interfaces' not in ret_dict:
                    ret_dict.setdefault('interfaces', {})
                if interface_var not in ret_dict['interfaces']:
                    interface_dict = ret_dict['interfaces'].setdefault(interface_var, {})
                interface_dict['queue_length'] = int(dict_val['queue_length'])
                continue

        return ret_dict


class ShowOspfv3EventsSchema(MetaParser):

    """Schema for show ospfv3 {pid} events"""

    schema = {
        'pid': int,
        'address_family': str,
        'router_id': str,
        'events': {
            Any(): { 
                'date': str, 
                'message': str
            }
        }
    }


class ShowOspfv3Events(ShowOspfv3EventsSchema):

    """Parser for show ospfv3 {pid} events"""

    cli_command = 'show ospfv3 {pid} events'

    def cli(self, pid='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(pid=pid))

        # OSPFv3 5 address-family ipv6 (router-id 1.1.1.1)
        p1 = re.compile(r"^OSPFv3\s+(?P<pid>\d+)\s+address-family\s+(?P<address_family>\S+)\s+\(router-id\s+("
                        r"?P<router_id>(\d{1,3}\.){3}\d{1,3})\)$")
        
        # 1    *Oct 10 13:19:29.499: End of SPF, SPF time 0ms, next wait-interval 200ms
        p2 = re.compile(r"^(?P<index>\d+)\s+(?P<date>\S+\s+\S+\s+\S+):\s+(?P<message>.*)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 5 address-family ipv6 (router-id 1.1.1.1)
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                ret_dict['pid'] = int(dict_val['pid'])
                ret_dict['address_family'] = dict_val['address_family']
                ret_dict['router_id'] = dict_val['router_id']
                continue

            # 1    *Oct 10 13:19:29.499: End of SPF, SPF time 0ms, next wait-interval 200ms
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                index_var = dict_val['index']
                if 'events' not in ret_dict:
                    ret_dict.setdefault('events', {})
                if index_var not in ret_dict['events']:
                    index_dict = ret_dict['events'
                            ].setdefault(index_var, {})
                index_dict['date'] = dict_val['date']
                index_dict['message'] = dict_val['message']
                continue

        return ret_dict

# =================================================================
# Schema for:
#   * 'show ospfv3 database database-summary detail'
#   * 'show ospfv3 vrf {vrf_id} database database-summary detail'
# =================================================================
 
class ShowOspfv3DatabaseSummaryDetailSchema(MetaParser):
 
    ''' Schema for:
        * 'show ospfv3 database database-summary detail'
        * 'show ospfv3 vrf {vrf_id} database database-summary detail'
    '''
 
    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        'instance':{
                            Any():{
                                Any():{
                                    'router':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'network':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'inter_area_prefix':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'inter_area_router':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'type_5_ext':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'type_7_external':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'link':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'prefix':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'te':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'gr':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },
                                    'total':{
                                        'count': int,
                                        'delete': int,
                                        'maxage': int,
                                    },  
                                },
                            },
                        },
                    },
                },
            },
        },
    }
 
# ================================================================
# Parser for:
#   * 'show ospfv3 database database-summary detail'
#   * 'show ospfv3 vrf {vrf_id} database database-summary detail'
# ================================================================
class ShowOspfv3DatabaseSummaryDetail(ShowOspfv3DatabaseSummaryDetailSchema):
 
    ''' Parser for:
        * 'show ospfv3 database database-summary detail'
        * 'show ospfv3 vrf {vrf_id} database database-summary detail'
    '''
 
    cli_command = ['show ospfv3 database database-summary detail', 'show ospfv3 vrf {vrf_id} database database-summary detail']
 
    def cli(self, vrf_id=None, output=None):
 
        if not output:
            if vrf_id:
                output = self.device.execute(self.cli_command[1].format(vrf_id=vrf_id))
            else:
                output = self.device.execute(self.cli_command[0])
 
        # Init variables
        ret_dict = {}
 
        # OSPFv3 5 address-family ipv4 (router-id 21.1.1.1)
        # OSPFv3 5 address-family ipv6 vrf red (router-id 12.1.1.2)
 
        p0 = re.compile(r'^OSPFv3 +(?P<instance>(\d+)) +address\-family +(?P<address_family>(\S+))'
                r'(?: +vrf +(?P<vrf>(\S+)))? +\(router\-id +(?P<router_id>(\S+))\)$')
 
        # Router 21.1.1.1 LSA summary
        p1 = re.compile(r'^Router +(?P<router_ip>(\S+)) +LSA +summary$')
 
        #LSA Type      Count    Delete   Maxage
        #Router              1        0        0
        #Network             1        0        0
        #Inter-area Prefix   0        0        0
        #Inter-area Router   0        0        0
        #Type-5 Ext          3        0        0
        #Type-7 External     0        0        0
        #Link                1        0        0
        #Prefix              1        0        0
        #TE                  0        0        0
        #GR                  0        0        0
        #Total               7        0        0
 
        p2 = re.compile(r'^(?P<lsa_type>(Router|Network|Inter-area Prefix|Inter-area Router|'
                r'Type-5 Ext|Type-7 External|Link|Prefix|TE|GR|Total))'
                r' +(?P<count>(\d+)) +(?P<delete>(\d+)) +(?P<maxage>(\d+))')
 
        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 5 address-family ipv4 (router-id 21.1.1.1)
            # OSPFv3 5 address-family ipv6 vrf red (router-id 12.1.1.2)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance']
                address_family = group['address_family']
                #if group['vrf']:
                #    vrf = group['vrf']
                #else:
                #    vrf = 'default'
                vrf = group.get('vrf', 'default')
 
                # create dict
                ospf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('instance', {}). \
                    setdefault(instance, {})
                continue
            
            # Router 21.1.1.1 LSA summary
            m = p1.match(line)
            if m:
                group = m.groupdict()
                item = group['router_ip']
                lsa_dict = ospf_dict.setdefault(item, {})
                continue
            
            #LSA Type      Count    Delete   Maxage
            #Router              1        0        0
            #Network             1        0        0
            #Inter-area Prefix   0        0        0
            #Inter-area Router   0        0        0
            #Type-5 Ext          3        0        0
            #Type-7 External     0        0        0
            #Link                1        0        0
            #Prefix              1        0        0
            #TE                  0        0        0
            #GR                  0        0        0
            #Total               7        0        0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lsa_type = group['lsa_type'].strip().lower().replace(" ", "_").replace("-", "_")
                tmp_dict = lsa_dict.setdefault(lsa_type, {})
                tmp_dict['count'] = int(group['count'])
                tmp_dict['delete'] = int(group['delete'])
                tmp_dict['maxage'] = int(group['maxage'])
 
        return ret_dict

# =================================================================
# Schema for:
#   * 'show ospfv3'
#   * 'show ospfv3 vrf {vrf_id}'
# =================================================================
 
class ShowOspfv3Schema(MetaParser):
 
    ''' Schema for:
        * 'show ospfv3'
        * 'show ospfv3 vrf {vrf_id}'
    '''
 
    schema = {
        'vrf':{
            Any():{
                'address_family':{
                    Any():{
                        'instance':{
                            Any():{
                                'router_id': str,
                                Optional('enable'): bool,
                                Optional('database_control'):{
                                    'max_lsa': int,
                                    Optional('max_lsa_current'): int,
                                    Optional('max_lsa_threshold_value'): int,
                                    Optional('max_lsa_ignore_count'): int,
                                    Optional('max_lsa_current_count'): int,
                                    Optional('max_lsa_ignore_time'): int,
                                    Optional('max_lsa_reset_time'): int,
                                    Optional('max_lsa_limit'): int,
                                    Optional('max_lsa_warning_only'): bool
                                    },
                                Optional('redistribution'):{
                                    Optional('max_prefix'):{
                                        Optional('num_of_prefix'): int,
                                        Optional('prefix_thld'): int,
                                        Optional('warn_only'): bool,
                                        },
                                    Optional('connected'): 
                                        {'enabled': bool,
                                        Optional('subnets'): str,
                                        Optional('metric'): int
                                        },
                                    Optional('static'): 
                                        {'enabled': bool,
                                        Optional('subnets'): str,
                                        Optional('metric'): int},
                                    Optional('bgp'): 
                                        {'bgp_id': int,
                                        Optional('metric'): int,
                                        Optional('subnets'): str,
                                        Optional('nssa_only'): str,
                                        },
                                    Optional('isis'): 
                                        {'isis_pid': str,
                                        Optional('subnets'): str,
                                        Optional('metric'): int}
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
 
# ================================================================
# Parser for:
#   * 'show ospfv3'
#   * 'show ospfv3 vrf {vrf_id}'
# ================================================================
class ShowOspfv3(ShowOspfv3Schema):
 
    ''' Parser for:
        * 'show ospfv3'
        * 'show ospfv3 vrf {vrf_id}'
    '''
 
    cli_command = ['show ospfv3', 'show ospfv3 vrf {vrf_id}']
 
    def cli(self, vrf_id=None, output=None):
 
        if not output:
            if vrf_id:
                output = self.device.execute(self.cli_command[1].format(vrf_id=vrf_id))
            else:
                output = self.device.execute(self.cli_command[0])
 
        # Init variables
        ret_dict = {}
        max_lsa_warn = False
        redist_max_prefix = False

        # OSPFv3 5 address-family ipv6 vrf red
        # OSPFv3 5 address-family ipv6
        p0 = re.compile(r'^OSPFv3 +(?P<instance>(\d+)) +address\-family +(?P<address_family>(\S+))'
                        r'(?: +vrf +(?P<vrf>(\S+)))?$')
 
        # Router ID 21.1.1.1
        p1 = re.compile(r'^Router +ID +(?P<router_id>(\S+))$')
 
        # Maximum number of non self-generated LSA allowed 500000
        # Maximum number of non self-generated LSA allowed 500000 (warning-only)
        p2 = re.compile(r'^Maximum +number +of +non +self-generated +LSA'
                                    r' +allowed +(?P<max_lsa>(\d+))'
                                    r'(?: +\((?P<max_lsa_warning_only>(warning-only))\))?')
 
        # Current number of non self-generated LSA 3                           
        p3_1 = re.compile(r'^Current +number +of +non +self\-generated +LSA +(?P<max_lsa_current>\d+)$')
 
        # Threshold for warning message 75%
        p3_2 = re.compile(r'^Threshold +for +warning +message +(?P<max_lsa_threshold_value>\d+)\%$')
 
        # Ignore-time 5 minutes, reset-time 10 minutes
        p3_3 = re.compile(r'^Ignore\-time +(?P<max_lsa_ignore_time>\d+) +minutes,'
                                    r' +reset\-time +(?P<max_lsa_reset_time>\d+) +minutes$')
 
        # Ignore-count allowed 5, current ignore-count 0
        p3_4 = re.compile(r'^Ignore\-count +allowed +(?P<max_lsa_ignore_count>\d+),'
                                    r' +current ignore\-count +(?P<max_lsa_current_count>\d+)$')
 
        # Redistributing External Routes from,
        p4 = re.compile(r'^Redistributing +External +Routes +from,$')

        # connected 
        # connected with metric mapped to 10
        # static
        # static with metric mapped to 10
        p4_1_1 = re.compile(r'^(?P<type>(connected|static))(?: +with +metric +mapped +to +(?P<metric>(\d+)))?$')

        # connected, includes subnets in redistribution
        # static, includes subnets in redistribution
        # isis, includes subnets in redistribution
        p4_1_2 = re.compile(r'^(?P<type>(connected|static|isis))'
                                r', +includes +(?P<redist>(subnets)) +in +redistribution')

        # bgp 100 with metric mapped to 111
        # isis 10 with metric mapped to 3333
        # bgp 100 with metric mapped to 100, includes subnets in redistribution, nssa areas only
        # bgp 100, includes subnets in redistribution
        p4_1_3 = re.compile(r'^(?P<prot>(bgp|isis)) +(?P<pid>(\d+))'
                            '(?: +with +metric +mapped +to +(?P<metric>(\d+)))?'
                            '(?:, +includes +(?P<redist>(subnets)) +in +redistribution)?'
                            '(?:, +(?P<nssa>(nssa areas only)))?$')
        # Maximum limit of redistributed prefixes 100000
        # Maximum limit of redistributed prefixes 100000 (warning-only)
        p4_2 = re.compile(r'^Maximum +limit +of +redistributed +prefixes'
                                    r' +(?P<num_prefix>(\d+))'
                                    r'(?: +\((?P<warn>(warning-only))\))?')
 
        # Threshold for warning message 85%
        p4_3 = re.compile(r'^Threshold +for +warning +message'
                                    r' +(?P<thld>(\d+))\%$')
 
        for line in output.splitlines():
            line = line.strip()
            # OSPFv3 5 address-family ipv6
            # OSPFv3 5 address-family ipv6 vrf red
            m = p0.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance']
                af = group['address_family']
                #if group['vrf']:
                #    vrf = group['vrf']
                #else:
                #    vrf = 'default'
                vrf = group.get('vrf', 'default')
 
                # Set structure
                sub_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(af, {}).setdefault('instance', {}). \
                    setdefault(instance, {})
                sub_dict['enable'] = True

            # Router ID 21.1.1.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub_dict['router_id'] = group['router_id']
                continue

            # Maximum number of non self-generated LSA allowed 40000
            # Maximum number of non self-generated LSA allowed 500000 (warning-only)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                max_lsa_warn = True
                max_lsa_dict = sub_dict.setdefault('database_control', {})
                max_lsa_dict['max_lsa'] = int(group['max_lsa'])
                max_lsa_dict['max_lsa_warning_only'] = \
                    group['max_lsa_warning_only'] == "warning-only"
 
            # Current number of non self-generated LSA 0
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                max_lsa_dict = sub_dict.setdefault('database_control', {})
                max_lsa_dict['max_lsa_current'] = int(group['max_lsa_current'])

            # Threshold for warning message 75%
            m = p3_2.match(line)
            if m and max_lsa_warn:
                group = m.groupdict()
                max_lsa_warn = False
                max_lsa_dict = sub_dict.setdefault('database_control', {})
                max_lsa_dict['max_lsa_threshold_value'] = \
                     int(group['max_lsa_threshold_value'])
 
            # Ignore-time 5 minutes, reset-time 10 minutes
            m = p3_3.match(line)
            if m:
                group = m.groupdict()
                max_lsa_dict = sub_dict.setdefault('database_control', {})
                max_lsa_dict['max_lsa_ignore_time'] =  \
                    int(group['max_lsa_ignore_time']) * 60
                max_lsa_dict['max_lsa_reset_time'] =  \
                    int(group['max_lsa_reset_time']) * 60
 
            # Ignore-count allowed 5, current ignore-count 0
            m = p3_4.match(line)
            if m:
                group = m.groupdict()
                max_lsa_dict = sub_dict.setdefault('database_control', {})
                max_lsa_dict['max_lsa_ignore_count'] =  \
                    int(group['max_lsa_ignore_count'])
                max_lsa_dict['max_lsa_current_count'] =  \
                    int(group['max_lsa_current_count'])
 
            # Redistributing External Routes from,
            m = p4.match(line)
            if m:
                redist_dict = sub_dict.setdefault('redistribution', {})

            # connected 
            # connected with metric mapped to 10
            # static
            # static with metric mapped to 10
            m = p4_1_1.match(line)
            if m:
                group = m.groupdict()
                the_type = group['type']
                type_dict = redist_dict.setdefault(the_type, {})
                type_dict['enabled'] = True
                if group['metric']:
                    type_dict['metric'] = int(group['metric'])
                continue

            # connected, includes subnets in redistribution
            # static, includes subnets in redistribution
            # isis, includes subnets in redistribution
            m = p4_1_2.match(line)
            if m:
                group = m.groupdict()
                the_type = group['type']
                type_dict = redist_dict.setdefault(the_type, {})
                type_dict['enabled'] = True
                type_dict['subnets'] = group['redist']
            # bgp 100 with metric mapped to 111
            # isis 10 with metric mapped to 3333
            # bgp 100 with metric mapped to 100, includes subnets in redistribution, nssa areas only
            # bgp 100, includes subnets in redistribution
            m = p4_1_3.match(line)
            if m:
                group = m.groupdict()
                prot = group['prot']
                type_dict = redist_dict.setdefault(prot, {})
                if prot == 'bgp':
                    type_dict['bgp_id'] = int(group['pid'])
                else:
                    type_dict['isis_pid'] = group['pid']

                # Set parsed values
                if group['metric']:
                    type_dict['metric'] = int(group['metric'])
                if group['redist']:
                    type_dict['subnets'] = group['redist']
                if group['nssa']:
                    type_dict['nssa_only'] = True
                continue

            # Maximum number of redistributed prefixes 4000
            # Maximum number of redistributed prefixes 3000 (warning-only)
            m = p4_2.match(line)
            if m:
                group = m.groupdict()
                redist_max_prefix = True
                type_dict = redist_dict.setdefault('max_prefix', {})
                type_dict['num_of_prefix'] = int(group['num_prefix'])
                type_dict['warn_only'] = group['warn'] == "warning-only"

            # Threshold for warning message 70%
            m = p4_3.match(line)
            if m and redist_max_prefix:
                group = m.groupdict()
                redist_max_prefix = False
                type_dict = redist_dict.setdefault('max_prefix', {})
                type_dict['prefix_thld'] = int(group['thld'])
    
        return ret_dict

# =================================================================
# Schema for:
#   * 'show running-config | section ospfv3'
# =================================================================
 
class ShowRunSectionOspfv3Schema(MetaParser):
 
    ''' Schema for:
        * 'show running-config | section ospfv3'
    '''
 
    schema = {
        'ospfv3':{
            'instance':{
                Any():{
                    Optional('database_control'):{
                        Optional('max_lsa'): int,
                        Optional('threshold'): int,
                        Optional('warn'): bool,
                        Optional('ignore_count'): int,
                        Optional('ignore_time'): int,
                        Optional('reset_time'): int,
                    },
                    'vrf':{
                        Any():{
                            'address_family':{
                                Any():{
                                    Optional('max_control'):{
                                        Optional('max_lsa'): int,
                                        Optional('threshold'): int,
                                        Optional('warn'): bool,
                                        Optional('ignore_count'): int,
                                        Optional('ignore_time'): int,
                                        Optional('reset_time'): int,
                                        },
                                    Optional('redist_max'):{
                                        Optional('max_redist'): int,
                                        Optional('threshold'): int,
                                        Optional('warn'): bool,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
 
# ==================================================
# Parser for:
#   * 'show running-config | section ospfv3'
# ===================================================
class ShowRunSectionOspfv3(ShowRunSectionOspfv3Schema):
    """Parser for show running-config | section ospfv3"""
 
    cli_command = 'show running-config | section ospfv3'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Init Variables
        ret_dict = {}
        max_value = False
        redist_value = False
        router_level = 1
        address_level = 0
 
        # router ospfv3 5
        p1 = re.compile(r'^router +ospfv3 +(?P<instance>(\d+))$')
 
        # address-family ipv4 unicast
        # address-family ipv6 unicast vrf red
        p2 = re.compile(r'^address\-family +(?P<address_family>(\S+)) +unicast(?: +vrf +(?P<vrf>(\S+)))?')
 
        # max-lsa 300000
        p3_1 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+))')
 
        # max-lsa 300000 76
        p3_2 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+)) +(?P<threshold>(\d+))$')
 
        # max-lsa 500000 warning-only
        p3_3 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+)) +(?P<warn>(\S+))$')
 
        # max-lsa 500000 89 warning-only
        p3_4 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+))(:? +(?P<threshold>(\d+))?)(:? +(?P<warn>(\S+))?)$')
 
        # max-lsa 500000 ignore-count 2
        p3_5 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+)) +ignore-count +(?P<ignore_count>(\d+))')
 
        # max-lsa 500000 ignore-time 5
        p3_6 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+)) +ignore-time +(?P<ignore_time>(\d+))')
 
        # max-lsa 300000 reset-time 11
        p3_7 = re.compile(r'^max-lsa +(?P<max_lsa>(\d+)) +reset-time +(?P<reset_time>(\d+))')
 
        # redistribute maximum-prefix 388899
        p4_1 = re.compile(r'^redistribute maximum-prefix +(?P<max_redist>(\d+))')
 
        # redistribute maximum-prefix 388899 76
        p4_2 = re.compile(r'^redistribute maximum-prefix +(?P<max_redist>(\d+))(:? +(?P<threshold>(\d+))?)$')
 
        # redistribute maximum-prefix 388899 warning-only
        p4_3 = re.compile(r'^redistribute maximum-prefix +(?P<max_redist>(\d+))(:? +(?P<warn>(warning-only)))$')
 
        for line in output.splitlines():
            line = line.strip()

            # router ospfv3 5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance = int(group.pop('instance'))
                sub_dict = ret_dict.setdefault('ospfv3', {}).setdefault('instance', {}).setdefault(instance, {})
                continue

            # max-lsa 300000
            m = p3_1.match(line)
            if router_level:
                if m:
                    group = m.groupdict()
                    max_value = True
                    max_lsa_dict = sub_dict.setdefault('database_control', {})
                    max_lsa_dict['max_lsa'] = int(group['max_lsa'])
                    router_level = 0
 
                    if m and max_value:
                        max_value = False

                        # max-lsa 300000 76
                        m = p3_2.match(line)
                        if m:
                            group = m.groupdict()
                            max_lsa_dict = sub_dict.setdefault('database_control', {})
                            max_lsa_dict['threshold'] = int(group['threshold'])
                        # max-lsa 500000 warning-only
                        m = p3_3.match(line)
                        if m:
                            group = m.groupdict()
                            max_lsa_dict = sub_dict.setdefault('database_control', {})
                            max_lsa_dict['warn'] = group['warn'] == "warning-only"
                        # max-lsa 500000 89 warning-only        
                        m = p3_4.match(line)
                        if m:
                            group = m.groupdict()
                            max_lsa_dict = sub_dict.setdefault('database_control', {})
                            max_lsa_dict['threshold'] = int(group['threshold'])
                            max_lsa_dict['warn'] = group['warn'] == "warning-only"
                        # max-lsa 500000 ignore-count 2
                        m = p3_5.match(line)
                        if m:
                            group = m.groupdict()
                            max_lsa_dict = sub_dict.setdefault('database_control', {})
                            max_lsa_dict['ignore_count'] = int(group['ignore_count'])
                        # max-lsa 500000 ignore-time 5
                        m = p3_6.match(line)
                        if m:
                            group = m.groupdict()
                            max_lsa_dict = sub_dict.setdefault('database_control', {})
                            max_lsa_dict['ignore_time'] = int(group['ignore_time'])
                        # max-lsa 300000 reset-time 11
                        m = p3_7.match(line)
                        if m:
                            group = m.groupdict()
                            max_lsa_dict = sub_dict.setdefault('database_control', {})
                            max_lsa_dict['reset_time'] = int(group['reset_time'])

            # address-family ipv4 unicast
            # address-family ipv6 unicast vrf red
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group["vrf"]:
                    vrf = group["vrf"]
                else:
                    vrf = "default"
                address_family = group["address_family"]
                af_dict = (
                    sub_dict.setdefault("vrf", {})
                    .setdefault(vrf, {})
                    .setdefault("address_family", {})
                    .setdefault(address_family, {})
                )
                address_level = 1
            if address_level:
                # max-lsa 300000
                m = p3_1.match(line)
                if m:
                    group = m.groupdict()
                    max_value = True
                    max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                    max_control_dict['max_lsa'] = int(group['max_lsa'])

                if m and max_value:
                    max_value = False
                    # max-lsa 300000 76
                    m = p3_2.match(line)
                    if m:
                        group = m.groupdict()
                        max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                        max_control_dict['max_lsa'] = int(group['max_lsa'])
                        max_control_dict['threshold'] = int(group['threshold'])
                    # max-lsa 500000 warning-only
                    m = p3_3.match(line)
                    if m:
                        group = m.groupdict()
                        max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                        max_control_dict['max_lsa'] = int(group['max_lsa'])
                        max_control_dict['warn'] = group['warn'] == "warning-only"
                    # max-lsa 500000 89 warning-only
                    m = p3_4.match(line)
                    if m:
                        group = m.groupdict()
                        max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                        max_control_dict['max_lsa'] = int(group['max_lsa'])
                        max_control_dict['threshold'] = int(group['threshold'])
                        max_control_dict['warn'] = group['warn'] == "warning-only"
                    # max-lsa 500000 ignore-count 2
                    m = p3_5.match(line)
                    if m:
                        group = m.groupdict()
                        max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                        max_control_dict['max_lsa'] = int(group['max_lsa'])
                        max_control_dict['ignore_count'] = int(group['ignore_count'])
                    # max-lsa 500000 ignore-time 5
                    m = p3_6.match(line)
                    if m:
                        group = m.groupdict()
                        max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                        max_control_dict['max_lsa'] = int(group['max_lsa'])
                        max_control_dict['ignore_time'] = int(group['ignore_time'])
                    # max-lsa 300000 reset-time 11
                    m = p3_7.match(line)
                    if m:
                        group = m.groupdict()
                        max_control_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('max_control', {})
                        max_control_dict['max_lsa'] = int(group['max_lsa'])
                        max_control_dict['reset_time'] = int(group['reset_time'])
                # redistribute maximum-prefix 388899
                m = p4_1.match(line)
                if m:
                    group = m.groupdict()
                    redist_value = True
                    redist_max_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('redist_max', {})
                    redist_max_dict['max_redist'] = int(group['max_redist'])

                if m and redist_value:
                    redist_value = False
                    # redistribute maximum-prefix 388899 76
                    m = p4_2.match(line)
                    if m:
                        group = m.groupdict()
                        redist_max_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('redist_max', {})
                        redist_max_dict['max_redist'] = int(group['max_redist'])
                        redist_max_dict['threshold'] = int(group['threshold'])

                    # redistribute maximum-prefix 388899 warning-only
                    m = p4_3.match(line)
                    if m:
                        group = m.groupdict()
                        redist_max_dict = sub_dict['vrf'][vrf]['address_family'][address_family].setdefault('redist_max', {})
                        redist_max_dict['max_redist'] = int(group['max_redist'])
                        redist_max_dict['warn'] = group['warn'] == "warning-only"

        return ret_dict