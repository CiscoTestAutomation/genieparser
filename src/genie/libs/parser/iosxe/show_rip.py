'''
show_rip.py
    * show ip protocols | sec rip
    * show ip protocols vrf {vrf} | sec rip
'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional


# ====================================================
#  schema for show ip protocols | sec rip
# ====================================================
class ShowIpProtocolsSchema(MetaParser):
    """Schema for show ip protocols | sec rip"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('instance'): {
                            Any(): {
                                Optional('default_metric'): int,
                                Optional('distance'): int,
                                Optional('triggered_update_threshold'): int,
                                Optional('maximum_paths'): int,
                                Optional('output_delay'): int,
                                Optional('offset_list'): int,
                                Optional('redistribute'): {
                                    Any(): {
                                        Optional(Any()): {
                                            Optional('metric'): int,
                                            Optional('route_policy'): int,
                                            Optional('route_type'): str,
                                        },
                                        Optional('metric'): int,
                                        Optional('route_policy'): int,
                                    },
                                },
                                Optional('timers'):{
                                    Optional('update_interval'): int,
                                    Optional('invalid_interval'): int,
                                    Optional('holddown_interval'): int,
                                    Optional('flush_interval'): int,
                                },
                                Optional('interfaces'): {
                                    Any(): {
                                        Optional('neighbors'):{
                                            Any(): {
                                                Optional('address'): str,
                                                },
                                            },
                                        Optional('summary_address'): {
                                            Any(): {
                                                Optional('metric'): str,
                                            },
                                        },
                                        Optional('passive'): str,
                                        Optional('send'): int,
                                        Optional('receive'): int,
                                        Optional('triggered_rip'): str,
                                        Optional('key_chain'): str,
                                    },
                                },
                                Optional('neighbors'): {
                                    Any():{
                                         Optional('last_update'): str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    }


# ====================================================
#  parser for show ip route
# ====================================================
class ShowIpProtocols(ShowIpProtocolsSchema):
    """Parser for :
       show ip protocols | sec rip
       show ip protocols vrf {vrf} | sec rip
       """

    cli_command = ["show ip protocols | sec rip","show ip protocols vrf {vrf} | sec rip"]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        address_family = "ipv4"
        passive_interface_flag = False

        # Routing Protocol is "rip"
        p1 = re.compile(r'^\s*Routing Protocol +is +\"(?P<protocol>[\w]+)\"$')

        # Output delay 50 milliseconds between packets
        p2 = re.compile(r'^\s*Output +delay +(?P<output_delay>[\d]+) +milliseconds +between +packets$')

        # Outgoing update filter list for all interfaces is not set
        p3 = re.compile(r'^\s*Outgoing +update +filter +list +for all +interfaces +is +not +set$')

        # Incoming update filter list for all interfaces is not set
        p4 = re.compile(r'^\s*Incoming +update +filter +list +for all +interfaces +is +not +set$')

        # Incoming routes will have 10 added to metric if on list 21
        p5 = re.compile(r'^\s*Incoming +routes +will +have +(?P<number_of_incoming_route_added>\d+) +added +to +metric'
                         ' +if +on +list +(?P<list_number>\d+)$')

        # Sending updates every 10 seconds, next due in 8 seconds
        p6 = re.compile(r'^\s*Sending +updates every +(?P<update_interval>\d+) +seconds, +next +due +in (?P<next_update>\d+) +seconds$')

        # Invalid after 21 seconds, hold down 22, flushed after 23
        p7 = re.compile(r'^\s*Invalid +after +(?P<invalid_interval>\d+) +seconds, +hold +down +(?P<holddown_interval>\d+)'
                        ', +flushed +after +(?P<flush_interval>\d+)$')

        # Default redistribution metric is 3
        p8 = re.compile(r'^\s*Default redistribution metric is +(?P<number_of_redistributed_metric>\d+)$')

        # Redistributing: connected, static, rip
        p9 = re.compile(r'^\s*Redistributing: +(?P<Redistributing>[\w\,\s]+)$')

        # Neighbor(s):
        p10 = re.compile(r'^\s*Neighbor\(s\):$')

        #   10.1.2.2
        p11 = re.compile(r'^\s*(?P<neighbor>[\d\.]+)$')

        # Default version control: send version 2, receive version 2
        p12 = re.compile(r'^\s*Default +version +control: +send +version +(?P<send_version>\d+)'
                         ', receive version +(?P<recieve_version>\d+)$')

        #   Interface                           Send  Recv  Triggered RIP  Key-chain
        #   GigabitEthernet3.100                2     2          No        1
        p13 = re.compile(r'^\s*(?P<interface>[\w\.]+) +(?P<send>\d+) +(?P<receive>\d+) +(?P<triggered_rip>(Yes|No)) +(?P<key_chain>\w+)$')

        # Automatic network summarization is not in effect
        p14 = re.compile(r'^\s*Automatic +network +summarization +is +not +in +effect$')

        # Address Summarization:
        p15 = re.compile(r'^\s*Address +Summarization:$')

        #   172.16.0.0/17 for GigabitEthernet3.100
        p16 = re.compile(r'^\s*(?P<prefix>[\d\.\/]+) +for +(?P<interface>[\w\.]+)$')

        # Maximum path: 4
        p17 = re.compile(r'^\s*Maximum +path: +(?P<maximum_path>\d+)$')

        # Routing for Networks:
        p18 = re.compile(r'^\s*Routing +for +Networks:$')

        #   10.0.0.0
        p19 = re.compile(r'^\s*(?P<network>[\d\.]+)$')

        # Passive Interface(s):
        p20 = re.compile(r'^\s*Passive +Interface\(s\):$')

        #   GigabitEthernet2.100
        p21 = re.compile(r'^\s*(?P<passive_interface>[\w\.]+)$')

        # Routing Information Sources:
        p22 = re.compile(r'^\s*Routing +Information +Sources:$')

        #   Gateway         Distance      Last Update
        #   10.1.2.2             120      00:00:04
        p23 = re.compile(r'^\s*(?P<gateway>[\d\.]+) +(?P<distance>\d+) +(?P<last_update>[\w\:]+)$')

        # Distance: (default is 120)
        p24 = re.compile(r'^\s*Distance: +\(default +is +(?P<distance>\d+)\)$')


        result_dict = {}

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Routing Protocol is "rip"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group['protocol']
                rip_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{}). \
                    setdefault(address_family, {}).setdefault('instance', {}).setdefault(protocol, {})
                continue

            # Output delay 50 milliseconds between packets
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'output_delay': int(group['output_delay'])})
                continue
            # Sending updates every 10 seconds, next due in 8 seconds
            m = p6.match(line)
            if m:
                group = m.groupdict()
                timers_dict = rip_dict.setdefault('timers', {})
                timers_dict.update({'update_interval': int(group['update_interval'])})
                continue

            # Invalid after 21 seconds, hold down 22, flushed after 23
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if 'timers' not in rip_dict:
                    timers_dict = rip_dict.setdefault('timers', {})
                timers_dict.update({'invalid_interval': int(group['invalid_interval'])})
                timers_dict.update({'holddown_interval': int(group['holddown_interval'])})
                timers_dict.update({'flush_interval': int(group['flush_interval'])})
                continue

            # Redistributing: connected, static, rip
            m = p9.match(line)
            if m:
                group = m.groupdict()
                redistributes = group['Redistributing'].split(',')
                redistribute_dict = rip_dict.setdefault('redistribute', {})
                for key in redistributes:
                    redistribute_dict.setdefault(key.strip(),{})
                continue


            #   Interface                           Send  Recv  Triggered RIP  Key-chain
            #   GigabitEthernet3.100                2     2          No        1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                interface_dict = rip_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                interface_dict.update({'send': int(group['send'])})
                interface_dict.update({'receive': int(group['receive'])})
                interface_dict.update({'triggered_rip': group['triggered_rip'].lower()})
                interface_dict.update({'key_chain': group['key_chain']})
                continue

            # 172.16.0.0/17 for GigabitEthernet3.100
            m = p16.match(line)
            if m:
                group = m.groupdict()
                summary_dict = interface_dict.setdefault('summary_address', {})
                summary_dict.setdefault(group['prefix'],{})
                continue

            # Maximum path: 4
            m = p17.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'maximum_paths': int(group['maximum_path'])})
                continue

            # Passive Interface(s):
            m = p20.match(line)
            if m:
                passive_interface_flag = True
                continue

            #   GigabitEthernet2.100
            m = p21.match(line)
            if m:
                if passive_interface_flag == True:
                    group = m.groupdict()
                    interface_dict.update({'passive': group['passive_interface']})
                continue

            # Routing Information Sources:
            m = p22.match(line)
            if m:
                passive_interface_flag = False
                continue

            #   Gateway         Distance      Last Update
            #   10.1.2.2             120      00:00:04
            m = p23.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict = rip_dict.setdefault('neighbors',{}).setdefault(group['gateway'],{})
                neighbor_dict.update({'last_update': group['last_update']})
                continue

            # Distance: (default is 120)
            m = p24.match(line)
            if m:
                group = m.groupdict()
                rip_dict.update({'distance': int(group['distance'])})
                continue

        return result_dict

# ====================================================
#  schema for show ipv6 protocols | sec rip
# ====================================================
class ShowIpv6ProtocolsSchema(MetaParser):
    """Schema for
            show ipv6 protocols | sec rip
            show ipv6 protocols vrf {vrf} | sec rip"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('instance'): {
                            Any(): {
                                Optional('redistribute'): {
                                    Any(): {
                                        Optional('metric'): int,
                                        Optional('route_policy'): str,
                                    },
                                },
                                Optional('interfaces'): {
                                    Any():{},
                                },
                            },
                        },
                    },
                },
            },
        }
    }


# ======================================================
#  parser for show ipv6 protocols | sec rip
# =======================================================
class ShowIpv6Protocols(ShowIpv6ProtocolsSchema):
    """Parser for :
           show ipv6 protocols | sec rip
           show ipv6 protocols vrf {vrf} | sec rip
           """

    cli_command = ["show ipv6 protocols | sec rip", "show ipv6 protocols vrf {vrf} | sec rip"]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        address_family= "ipv6"

        #IPv6 Routing Protocol is "rip ripng"
        p1 = re.compile(r'^\s*IPv6 +Routing +Protocol +is +\"(?P<protocol>[\w\s]+)\"$')

        # Interfaces:
        p2 = re.compile(r'^\s*Interfaces$')

        #   GigabitEthernet3.200
        p3 = re.compile(r'^\s*(?P<interface>[\w\.\/]+)$')

        # Redistribution:
        #   Redistributing protocol connected with metric 3
        #   Redistributing protocol connected with transparent metric 3
        p4 = re.compile(r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with( +transparent)? +metric( +(?P<metric>\d+))?$')
        #   Redistributing protocol static with transparent metric route-map static-to-rip
        p5 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with +transparent +metric( +route-map +(?P<route_policy>[\w\-]+))?$')

        result_dict = {}

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Routing Protocol is "rip ripng"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                protocol = group['protocol']
                rip_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{}). \
                    setdefault(address_family, {}).setdefault('instance', {}).setdefault(protocol, {})
                continue

            #   GigabitEthernet2.100
            m = p3.match(line)
            if m:
                group = m.groupdict()
                rip_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                continue

            # Redistributing protocol connected with metric 3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']
                redistribute_dict = rip_dict.setdefault('redistribute', {}).setdefault(redistribute, {})

                if group['metric']:
                    redistribute_dict.update({'metric': int(group['metric'])})
                continue
            # Redistributing protocol static with transparent metric route-map static-to-rip
            m = p5.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']

                redistribute_dict = rip_dict.setdefault('redistribute', {}).setdefault(redistribute, {})
                redistribute_dict.update({'route_policy': group['route_policy']})
                continue

        return result_dict

# ====================================================
#  schema for show ip rip database
# ====================================================
class ShowIpRipDatabaseSchema(MetaParser):
    """Schema for
            show ip rip database
            show ip rip database vrf {vrf}"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'routes': {
                                    Any(): {
                                        'index': {
                                            Any(): {
                                                Optional('next_hop'): str,
                                                Optional('interface'): str,
                                                Optional('from'): str,
                                                Optional('metric'): int,
                                                Optional('redistributed'): bool,
                                                Optional('route_type'): str,
                                                Optional('summary_type'): str,
                                                Optional('expire_time'): str,
                                            }
                                        }
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    }

# ======================================================
#  parser for show ip rip database
# =======================================================
class ShowIpRipDatabase(ShowIpRipDatabaseSchema):
    """Parser for :
           show ip rip database
           show ip rip database vrf {vrf}
           """

    cli_command = ["show ip rip database", "show ip rip database vrf {vrf}"]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        address_family= "ipv4"
        instance = 'rip'
        index = 1
        summary_type_dict = {}
        rip_dict = {}

        redistributed_list = ['redistributed']
        summary_type_list = ['auto-summary','int-summary']
        route_type_list = ['connected','external','external-backup','rip']

        # 0.0.0.0/0    auto-summary
        p1 = re.compile(r'^\s*(?P<route>[\d\.\/]+)( +(?P<summary_type>\S+))?$')

        # 10.1.2.0/24    directly connected, GigabitEthernet2.100
        p2 = re.compile(r'^\s*(?P<route>[\d\.\/]+) +directly +connected, +(?P<interface>\S+)$')

        #    [1] via 172.16.1.254, from 0.0.0.0,
        p3 = re.compile(r'^\s*\[(?P<metric>\d+)\] +via +(?P<next_hop>[\d\.]+),( +from +(?P<from>[\d\.]+),)?$')

        #    [4] via 10.1.2.2, 00:00:00, GigabitEthernet2.100
        p4 = re.compile(r'^\s*\[(?P<metric>\d+)\] +via +(?P<next_hop>[\d\.\/]+),'
                        ' +(?P<expire_time>[\w\:]+), +(?P<interface>\S+)$')

        result_dict = {}

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue
            #  0.0.0.0/0    auto-summary
            m = p1.match(line)
            if m:
                group = m.groupdict()
                summary_type_dict = {}
                route = group['route']
                summary_type = group['summary_type']

                rip_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{}). \
                    setdefault(address_family, {}).setdefault('instance', {}).setdefault(instance, {})
                if 'routes' in rip_dict:
                    if route in rip_dict['routes'].keys():
                        index += 1
                    else:
                        index = 1
                        route_dict = rip_dict.setdefault('routes', {}).setdefault(route, {})
                else:
                    route_dict = rip_dict.setdefault('routes', {}).setdefault(route, {})
                if summary_type:
                    index_dict = route_dict.setdefault('index', {}).setdefault(index, {})
                    if summary_type in redistributed_list:
                        summary_type_dict.update({'redistributed': True})
                    if summary_type in summary_type_list:
                        summary_type_dict.update({'summary_type': summary_type})
                    if summary_type in route_type_list:
                        summary_type_dict.update({'route_type': summary_type})
                    index_dict.update(summary_type_dict)
                continue

            # 10.1.2.0/24    directly connected, GigabitEthernet2.100
            m = p2.match(line)
            if m:
                summary_type_dict = {}
                group = m.groupdict()
                route = group['route']
                rip_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}). \
                    setdefault(address_family, {}).setdefault('instance', {}).setdefault(instance, {})
                route_dict = rip_dict.setdefault('routes', {}).setdefault(route, {})
                index_dict = route_dict.setdefault('index', {}).setdefault(index, {})

                index_dict.update({'interface': group['interface']})
                index_dict.update({'route_type': 'connected'})
                continue

            #  [1] via 172.16.1.254, from 0.0.0.0,
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if 'routes' in rip_dict.keys():
                    if route in rip_dict['routes'].keys():
                        index_dict = route_dict.setdefault('index', {}).setdefault(index, {})
                        index += 1

                index_dict.update({'next_hop': group['next_hop']})
                if group['from']:
                    index_dict.update({'from': group['from']})
                index_dict.update({'metric': int(group['metric'])})
                if summary_type_dict:
                    index_dict.update(summary_type_dict)

                continue

            #  [4] via 10.1.2.2, 00:00:00, GigabitEthernet2.100
            m = p4.match(line)
            if m:
                group = m.groupdict()
                index_dict = route_dict.setdefault('index', {}).setdefault(index, {})
                index_dict.update({'next_hop': group['next_hop']})
                index_dict.update({'interface': group['interface']})
                index_dict.update({'expire_time': group['expire_time']})
                index_dict.update({'metric': int(group['metric'])})
                index += 1
                continue

        return result_dict

# =======================================================
#  schema for show ipv6 rip database
# =======================================================
class ShowIpv6RipDatabaseSchema(MetaParser):
    """Schema for
            show ipv6 rip database
            show ipv6 rip database vrf {vrf}"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'routes': {
                            Any(): {
                                'index': {
                                    Any(): {
                                        Optional('next_hop'): str,
                                        Optional('interface'): str,
                                        Optional('metric'): int,
                                        Optional('route_type'): str,
                                        Optional('expire_time'): str,
                                    }
                                }
                            },
                        },
                    },
                },
            },
        }
    }

# ======================================================
#  parser for show ipv6 rip database
# =======================================================
class ShowIpv6RipDatabase(ShowIpv6RipDatabaseSchema):
    """Parser for :
           show ipv6 rip database
           show ipv6 rip database vrf {vrf}
           """

    cli_command = ["show ipv6 rip database", "show ipv6 rip vrf {vrf} database"]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        address_family= "ipv6"
        index = 1

        # RIP VRF "Default VRF", local RIB
        # RIP VRF "VRF1", local RIB
        p1 = re.compile(r'^\s*RIP +VRF +"(?P<vrf>[\S\s]+)", +local +RIB$')

        # 2001:DB8:1:3::/64, metric 2
        # 2001:DB8:2:3::/64, metric 2, installed
        p2 = re.compile(r'^\s*(?P<route>[\w\:\/]+), +metric +(?P<metric>\d+)(, +(?P<installed>(installed)+))?$')

        #     GigabitEthernet3.100/FE80::F816:3EFF:FEFF:1E3D, expires in 179 secs
        p3 = re.compile(r'^\s*(?P<interface>\S+), +expires +in +(?P<expire_time>[\d]+) +secs$')

        result_dict = {}

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # RIP VRF "Default VRF", local RIB
            # RIP VRF "VRF1", local RIB
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                if 'default' in vrf.lower():
                    vrf = 'default'

                address_family_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',{}). \
                    setdefault(address_family, {})

                continue

            # 2001:DB8:2:3::/64, metric 2, installed
            m = p2.match(line)
            if m:
                index = 1
                group = m.groupdict()
                metric = int(group['metric'])
                installed = group['installed']
                route = group['route']
                route_dict = address_family_dict.setdefault('routes', {}).setdefault(route, {})
                index_dict = route_dict.setdefault('index', {}).setdefault(index, {})

                index_dict.update({'metric': metric})
                if installed:
                    index_dict.update({'route_type': installed})
                continue

            #  GigabitEthernet3.100/FE80::F816:3EFF:FEFF:1E3D, expires in 179 secs
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict = route_dict.setdefault('index', {}).setdefault(index, {})
                interface_nexthop = group['interface']
                if '/' in interface_nexthop:
                    interface = interface_nexthop.split('/')[0]
                    next_hop = interface_nexthop.split('/')[1]

                    index_dict.update({'interface': interface})
                    index_dict.update({'next_hop': next_hop})
                else:
                    index_dict.update({'interface': group['interface']})

                index_dict.update({'expire_time': group['expire_time']})
                if metric:
                    index_dict.update({'metric': metric})
                if installed:
                    index_dict.update({'route_type': installed})

                index +=1
                continue

        return result_dict

# ====================================================
#  schema for show ip rip
# ====================================================
class ShowIpv6RipSchema(MetaParser):
    """Schema for
            show ipv6 rip
            show ipv6 rip vrf {vrf}"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('distance'): int,
                        Optional('maximum_paths'): int,
                        Optional('pid'): int,
                        Optional('port'): int,
                        Optional('multicast_group'): str,
                        'redistribute':{
                            Any():{
                              Optional('metric'): int,
                              Optional('route_policy'): str,
                            },
                        },
                        'timers':{
                            Optional('update_interval'): int,
                            Optional('holddown_interval'): int ,
                            Optional('flush_interval'): int,
                            Optional('expire_time'):int,
                            },
                        'interfaces': {
                            Any(): {
                                Optional('split_horizon'): bool,
                                Optional('poison_reverse'): bool,
                                Optional('timers'): {
                                    Optional('update_interval'): int,
                                    Optional('holddown_interval'): int,
                                    Optional('trigger_interval'): int,
                                    Optional('full_advertisement'): int,
                                },
                            },
                        },
                    },
                },
            }
        },
    }


# ======================================================
#  parser for show ip rip neighbors
# ======================================================
class ShowIpv6Rip(ShowIpv6RipSchema):
    """Parser for :
           show ipv6 rip
           show ipv6 rip vrf {vrf}"""

    cli_command = ["show ipv6 rip","show ipv6 rip vrf {vrf}"]

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        address_family = "ipv6"

        # RIP VRF "Default VRF", port 521, multicast-group FF02::9, pid 635
        # RIP VRF "VRF1", port 521, multicast-group FF02::9, pid 635
        p1 = re.compile(r'^\s*RIP +VRF +(?P<vrf>[\S\s]+), +port +(?P<port>\d+),'
                        ' +multicast\-group +(?P<multicast_group>[\w\:]+), +pid +(?P<pid>\d+)$')
        #    Administrative distance is 120. Maximum paths is 16
        p2 = re.compile(r'^\s*Administrative +distance +is +(?P<distance>\d+). +Maximum +paths +is +(?P<maximum_path>\d+)$')
        #    Updates every 30 seconds, expire after 180
        p3 = re.compile(
            r'^\s*Updates +every +(?P<update>\d+) +seconds, +expire +after +(?P<expire_time>\d+)$')
        #    Holddown lasts 0 seconds, garbage collect after 120
        p4 = re.compile(
            r'^\s*Holddown +lasts +(?P<holddown>\d+) +seconds, +garbage +collect +after +(?P<flush_interval>\d+)$')
        #    Split horizon is on; poison reverse is off
        p5 = re.compile(
            r'^\s*Split +horizon +is +(?P<split_horizon>(on|off)+); +poison +reverse +is +(?P<poison_reverse>(on|off)+)$')
        #    Default routes are not generated
        p6 = re.compile(r'^\s*Default routes are not generated$')
        #    Periodic updates 399, trigger updates 8
        p7 = re.compile(
            r'^\s*Periodic +updates +(?P<perodic_update>\d+), +trigger +updates +(?P<trigger_update>\d+)$')
        #    Full Advertisement 0, Delayed Events 0
        p8 = re.compile(
            r'^\s*Full +Advertisement +(?P<full_advertisement>\d+), +Delayed +Events +(?P<delay_events>\d+)$')
        # Interfaces:
        p9 = re.compile(
            r'^\s*Interfaces:$')
        #   GigabitEthernet3.100
        p10 = re.compile(r'^\s*(?P<interface>[\w\/\.]+)$')

        # Redistribution:
        # Redistributing protocol connected with transparent metric
        p11 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with( +transparent)? +metric( +(?P<metric>\d+))?$')
        #   Redistributing protocol static with transparent metric route-map static-to-rip
        p12 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with +transparent +metric( +route-map +(?P<route_policy>[\w\-]+))?$')


        result_dict = {}
        intf_timers_dict = {}

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf'].strip('"')
                if 'default' in vrf.lower():
                    vrf = 'default'

                address_family_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).\
                                                  setdefault('address_family', {}).\
                                                  setdefault(address_family, {})
                address_family_dict.update({'pid': int(group['pid'])})
                address_family_dict.update({'port': int(group['port'])})
                address_family_dict.update({'multicast_group': group['multicast_group']})
                continue

            #    Administrative distance is 120. Maximum paths is 16
            m = p2.match(line)
            if m:
                group = m.groupdict()
                distance = int(group['distance'])
                maximum_paths = int(group['maximum_path'])
                address_family_dict.update({'distance': distance})
                address_family_dict.update({'maximum_paths': maximum_paths})
                continue

            #    Updates every 30 seconds, expire after 180
            m = p3.match(line)
            if m:
                group = m.groupdict()
                timers_dict = address_family_dict.setdefault('timers',{})
                timers_dict.update({'update_interval': int(group['update'])})
                timers_dict.update({'expire_time': int(group['expire_time'])})
                continue

            #    Holddown lasts 0 seconds, garbage collect after 120
            m = p4.match(line)
            if m:
                group = m.groupdict()
                timers_dict = address_family_dict.setdefault('timers', {})
                timers_dict.update({'holddown_interval': int(group['holddown'])})
                timers_dict.update({'flush_interval': int(group['flush_interval'])})
                continue

            #    Split horizon is on; poison reverse is off
            m = p5.match(line)
            if m:
                group = m.groupdict()
                split_horizon_dict = {}
                split_horizon_dict.update({'split_horizon': True if group['split_horizon'] =='on'  else False})
                split_horizon_dict.update({'poison_reverse': True if group['poison_reverse'] == 'on' else False})
                continue

            #    Periodic updates 399, trigger updates 8
            m = p7.match(line)
            if m:
                group = m.groupdict()
                periodic_update = int(group['perodic_update'])
                trigger_update = int(group['trigger_update'])

                intf_timers_dict.update({'update_interval': periodic_update})
                intf_timers_dict.update({'trigger_interval': trigger_update})
                continue

            #    Full Advertisement 0, Delayed Events 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                full_advertisement = int(group['full_advertisement'])
                delay_events = int(group['delay_events'])

                intf_timers_dict.update({'holddown_interval': delay_events})
                intf_timers_dict.update({'full_advertisement': full_advertisement})
                continue

            #   GigabitEthernet3.100
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict = address_family_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                if split_horizon_dict:
                    intf_dict.update(split_horizon_dict)
                if intf_timers_dict:
                    intf_dict.setdefault('timers',intf_timers_dict)

                continue

            # Redistributing protocol connected with metric 3
            m = p11.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']
                redistribute_dict = address_family_dict.setdefault('redistribute', {}).setdefault(redistribute, {})

                if group['metric']:
                    redistribute_dict.update({'metric': int(group['metric'])})
                continue

            # Redistributing protocol static with transparent metric route-map static-to-rip
            m = p12.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']
                redistribute_dict = address_family_dict.setdefault('redistribute', {}).setdefault(redistribute, {})
                redistribute_dict.update({'route_policy': group['route_policy']})
                continue

        return result_dict

