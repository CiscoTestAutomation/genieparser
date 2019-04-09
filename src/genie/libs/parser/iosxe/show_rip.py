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
                        Optional('split_horizon'): bool,
                        Optional('poison_reverse'): bool,
                        'originate_default_route':{
                            'enabled': bool,
                        },
                        Optional('redistribute'):{
                            Any(): {
                              Optional('metric'): int,
                              Optional('route_policy'): str,
                            },
                            Optional('bgp'): {
                                Any() : {
                                    Optional('metric'): int,
                                    Optional('route_policy'): str,
                                }
                            },
                        },
                        'timers':{
                            Optional('update_interval'): int,
                            Optional('holddown_interval'): int ,
                            Optional('flush_interval'): int,
                            Optional('expire_time'):int,
                            },
                        Optional('interfaces'): {
                            Any(): {
                            },
                        },
                        Optional('statistics'): {
                            Optional('periodic_updates'): int,
                            Optional('delayed_events'): int,
                            Optional('trigger_updates'): int,
                            Optional('full_advertisement'): int,
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
        # RIP VRF "red", port 521, multicast-group 2001:DB8::/32, pid 295
        # RIP process "one", port 521, multicast-group FF02::9, pid 55
        p1 = re.compile(r'^\s*RIP +(VRF|process)+ +(?P<vrf>[\S\s]+), +port +(?P<port>\d+),'
                        ' +multicast\-group +(?P<multicast_group>[\w\:\/]+), +pid +(?P<pid>\d+)$')
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
        #    Default routes are generated
        p6 = re.compile(r'^\s*Default +routes +are +((?P<default_routes_generated>\w+) )?generated$')
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
        p10 = re.compile(r'^\s*(?P<interface>^(?!None)[\w\/\.]+)$')

        # Redistribution:
        # Redistributing protocol connected with transparent metric
        p11 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with( +transparent)? +metric( +(?P<metric>\d+))?$')
        #   Redistributing protocol static with transparent metric route-map static-to-rip
        p12 = re.compile(
            r'^\s*Redistributing +protocol +(?P<redistribute>\w+) +with +transparent +metric( +route-map +(?P<route_policy>[\w\-]+))?$')

        # Redistributing protocol bgp 65001 route-map bgp-to-rip
        p13 = re.compile(r'^Redistributing +protocol +(?P<redistribute>\w+) +(?P<protocol_number>\d+) +route\-map +(?P<route_policy>[\w\-]+)$')

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
                address_family_dict.update({'split_horizon': True if group['split_horizon'] =='on'  else False})
                address_family_dict.update({'poison_reverse': True if group['poison_reverse'] == 'on' else False})
                continue

            # Default routes are not generated
            # Default routes are generated
            m = p6.match(line)
            if m:
                group = m.groupdict()
                originate_dict = address_family_dict.setdefault('originate_default_route',{})
                if group['default_routes_generated']:
                    enabled = False
                else:
                    enabled = True
                originate_dict.update({'enabled': enabled})

                continue

            #    Periodic updates 399, trigger updates 8
            m = p7.match(line)
            if m:
                group = m.groupdict()
                statistics_dict = address_family_dict.setdefault('statistics', {})
                periodic_update = int(group['perodic_update'])
                trigger_update = int(group['trigger_update'])

                statistics_dict.update({'periodic_updates': periodic_update})
                statistics_dict.update({'trigger_updates': trigger_update})
                continue

            #    Full Advertisement 0, Delayed Events 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                statistics_dict = address_family_dict.setdefault('statistics', {})
                full_advertisement = int(group['full_advertisement'])
                delay_events = int(group['delay_events'])

                statistics_dict.update({'delayed_events': delay_events})
                statistics_dict.update({'full_advertisement': full_advertisement})
                continue

            #   GigabitEthernet3.100
            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict = address_family_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
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

            # Redistributing protocol bgp 65001 route-map bgp-to-rip
            m = p13.match(line)
            if m:
                group = m.groupdict()
                redistribute = group['redistribute']
                redistribute_dict = address_family_dict.setdefault('redistribute', {}).setdefault(redistribute, {}). \
                    setdefault(int(group['protocol_number']), {})
                redistribute_dict.update({'route_policy': group['route_policy']})
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
                                        Optional('installed'): bool,
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
                    index_dict.update({'installed': True})
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
                    index_dict.update({'installed': True})

                index +=1
                continue

        return result_dict
