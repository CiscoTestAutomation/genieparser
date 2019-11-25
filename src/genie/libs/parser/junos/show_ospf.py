""" show_ospf.py

JunOs parsers for the following show commands:
    * show ospf interface brief
    * show ospf interface {interface} brief
    * show ospf interface brief instance {instance}
    * show ospf interface
    * show ospf interface {interface}
    * show ospf interface detail
    * show ospf interface {interface} detail
    * show ospf interface instance {instance}
    * show ospf interface detail instance {instance}
    * show ospf interface {interface} detail instance {instance}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowOspfInterfaceBriefSchema(MetaParser):
    """ Schema for:
            * show ospf interface brief
            * show ospf interface brief instance {instance}
            * show ospf interface {interface} brief
            * show ospf interface
            * show ospf interface instance {instance}
            * show ospf interface {interface}
    """

    schema = {
        'instance': {
            Any(): {
                'areas': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'state': str,
                                'dr_id': str,
                                'bdr_id': str,
                                'nbrs_count': int,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowOspfInterfaceBrief(ShowOspfInterfaceBriefSchema):
    """ Parser for:
            * show ospf interface brief
            * show ospf interface brief instance {instance}
            * show ospf interface {interface} brief
    """

    cli_command = [
        'show ospf interface {interface} brief',
        'show ospf interface brief',
        'show ospf interface brief instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if instance:
                out = self.device.execute(self.cli_command[2].format(instance=instance))
            elif interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = instance if instance else 'master'

        # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) '
            '+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                intf_dict = ret_dict.setdefault('instance', {}).\
                    setdefault(instance, {}).\
                    setdefault('areas', {}).\
                    setdefault(area, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})

                intf_dict.update({'state' : group['state']})
                intf_dict.update({'dr_id' : group['dr_id']})
                intf_dict.update({'bdr_id' : group['bdr_id']})
                intf_dict.update({'nbrs_count' : int(group['nbrs_count'])})
                continue

        return ret_dict


class ShowOspfInterface(ShowOspfInterfaceBrief):
    """ Parser for:
            * show ospf interface
            * show ospf interface {interface}
            * show ospf interface instance {instance}
    """

    cli_command = [
        'show ospf interface',
        'show ospf interface {interface}',
        'show ospf interface instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            elif instance:
                out = self.device.execute(self.cli_command[2].format(instance=instance))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


class ShowOspfInterfaceDetailSchema(MetaParser):
    """ Schema for:
           * show ospf interface detail
           * show ospf interface {interface} detail
           * show ospf interface detail instance {instance}
           * show ospf interface {interface} detail instance {instance}
    """

    schema = {
        'instance': {
            Any(): {
                'areas': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'state': str,
                                'dr_id': str,
                                'bdr_id': str,
                                'nbrs_count': int,
                                'type': str,
                                'address': str,
                                'mask': str,
                                'mtu': int,
                                Optional('dr_ip_addr'): str,
                                Optional('priority'): int,
                                'cost': int,
                                'adj_count': int,
                                'hello': int,
                                'dead': int,
                                'rexmit': int,
                                'ospf_stub_type': str,
                                'authentication_type': str,
                                'ospf_interface': {
                                    'protection_type': str,
                                    Optional('tilfa'): {
                                        'prot_link': str,
                                        'prot_srlg': str,
                                        'prot_fate': str,
                                        'prot_node': int
                                    },
                                    'topology': {
                                        Any(): {
                                            'id': int,
                                            'metric': int
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowOspfInterfaceDetail(ShowOspfInterfaceDetailSchema):
    """ Parser for:
           * show ospf interface detail
           * show ospf interface {interface} detail
           * show ospf interface detail instance {instance}
           * show ospf interface {interface} detail instance {instance}
    """

    cli_command = [
        'show ospf interface detail',
        'show ospf interface {interface} detail',
        'show ospf interface detail instance {instance}',
        'show ospf interface {interface} detail instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if interface and instance:
                out = self.device.execute(self.cli_command[3].format(interface=interface, instance=instance))
            elif interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            elif instance:
                out = self.device.execute(self.cli_command[2].format(instance=instance))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = 'master'

        # ge-0/0/2.0    BDR    0.0.0.1        10.64.4.4     5
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) '
                        r'+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$')

        # Type: P2P, Address: 172.16.76.25, Mask: 255.255.255.0, MTU: 1200, Cost: 100
        p2 = re.compile(r'^Type: +(?P<interface_type>\w+), +Address: +(?P<interface_address>[\d.]+)'
                        r', +Mask: +(?P<address_mask>[\d.]+), +MTU: +(?P<mtu>\d+), +Cost: +(?P<interface_cost>\d+)$')

        # Adj count: 4
        p3 = re.compile(r'^Adj +count: +(?P<adj_count>\d+)$')

        # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        p4 = re.compile(r'^Hello: +(?P<hello_interval>\d+), +Dead: +(?P<dead_interval>\d+), +'
                        r'ReXmit: +(?P<retransmit_interval>\d+), +(?P<ospf_stub_type>[\w ]+)$')

        # Auth type: None
        p5 = re.compile(r'^Auth +type: +(?P<authentication_type>[\w ]+)$')

        # Protection type: Post Convergence
        p6 = re.compile(r'^Protection +type: +(?P<protection_type>[\w ]+)$')

        # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 150
        p7 = re.compile(r'^Post +convergence +protection: +(?P<prot_link>\w+), +Fate +sharing: +'
                        r'(?P<prot_fate>\w+), +SRLG: +(?P<prot_srlg>\w+), +Node +cost: +(?P<prot_node>\d+)$')

        # Topology default (ID 0) -> Cost: 1000
        p8 = re.compile(r'^Topology +(?P<name>\w+) +\(ID +(?P<id>\d+)\) +-> +Cost: +(?P<metric>\d+)$')

        # DR addr: 10.16.2.2, Priority: 128
        p9 = re.compile(r'^DR +addr: +(?P<dr_address>[\d.]+), +Priority: +(?P<router_priority>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                intf_dict = ret_dict.setdefault('instance', {}).\
                    setdefault(instance, {}).\
                    setdefault('areas', {}).\
                    setdefault(area, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})

                intf_dict.update({'state' : group['state']})
                intf_dict.update({'dr_id' : group['dr_id']})
                intf_dict.update({'bdr_id' : group['bdr_id']})
                intf_dict.update({'nbrs_count' : int(group['nbrs_count'])})
                continue

            # Type: P2P, Address: 172.16.76.25, Mask: 255.255.255.0, MTU: 1200, Cost: 100
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'type': group['interface_type']})
                intf_dict.update({'address': group['interface_address']})
                intf_dict.update({'mask': group['address_mask']})
                intf_dict.update({'mtu': int(group['mtu'])})
                intf_dict.update({'cost': int(group['interface_cost'])})
                continue

            # Adj count: 4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'adj_count': int(group['adj_count'])})
                continue

            # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'hello': int(group['hello_interval'])})
                intf_dict.update({'dead': int(group['dead_interval'])})
                intf_dict.update({'rexmit': int(group['retransmit_interval'])})
                intf_dict.update({'ospf_stub_type': group['ospf_stub_type']})
                continue

            # Auth type: None
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_type': group['authentication_type']})
                continue

            # Protection type: Post Convergence
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_intf_dict = intf_dict.setdefault('ospf_interface', {})
                ospf_intf_dict.update({'protection_type': group['protection_type']})
                continue

            # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 150
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tilfa_dict = ospf_intf_dict.setdefault('tilfa', {})
                tilfa_dict.update({'prot_link': group['prot_link']})
                tilfa_dict.update({'prot_fate': group['prot_fate']})
                tilfa_dict.update({'prot_srlg': group['prot_srlg']})
                tilfa_dict.update({'prot_node': int(group['prot_node'])})
                continue

            # Topology default (ID 0) -> Cost: 1000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                topology_dict = ospf_intf_dict.setdefault('topology', {}).setdefault(group['name'], {})
                topology_dict.update({'id': int(group['id'])})
                topology_dict.update({'metric': int(group['metric'])})
                continue

            # DR addr: 10.16.2.2, Priority: 128
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'dr_ip_addr': group['dr_address']})
                intf_dict.update({'priority': int(group['router_priority'])})
                continue

        return ret_dict
