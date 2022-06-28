''' show_access_list.py

Parser for the following show commands:
    * show access-list
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================
# Schema for 'show access-list'
# =============================================
class ShowAccessListSchema(MetaParser):
    """Schema for
        * show access-list
    """

    schema = {
    	Optional('access-list'): {
            Any(): {
                Optional('elements'): int,
                Optional('name_hash'): str,
                'entry': {
                    Any(): {
                        Optional('controls_flows'): bool,
                        Optional('is_expandable'): bool,
                        Optional('action'): str,
                        Optional('protocol'): str,
                        Optional('log'): bool,
                        Optional('informational_interval'): int,
                        Optional('hitcnt'): int,
                        Optional('acl_hash'): str,
                        Optional('object_group'): str,
                        Optional('source'): {
                            Optional('object_group'): str,
                            Optional('object'): str,
                            Optional('any'): str,
                            Optional('network'): str,
                            Optional('mask'): str,
                            Optional('port'): str,
                            # eq lt neq range
                            Optional('port_op'): str,
                            Optional('from_port'): str,
                            Optional('to_port'): str
                        },
                        Optional('destination'): {
                            Optional('object_group'): str,
                            Optional('object'): str,
                            Optional('any'): str,
                            Optional('network'): str,
                            Optional('mask'): str,
                            Optional('port'): str,
                            Optional('port_op'): str,
                            Optional('from_port'): str,
                            Optional('to_port'): str
                        },
                        Optional('group-expansion'): {
                            Any(): {
                                Optional('controls_flows'): bool,
                                'action': str,
                                'protocol': str,
                                'log': bool,
                                Optional('informational_interval'): int,
                                'hitcnt': int,
                                'acl_hash': str,
                                Optional('source'): {
                                    Optional('any'): str,
                                    Optional('network'): str,
                                    Optional('mask'): str,
                                    Optional('port'): str,
                                    Optional('port_op'): str,
                                    Optional('from_port'): str,
                                    Optional('to_port'): str
                                },
                                Optional('destination'): {
                                    Optional('any'): str,
                                    Optional('network'): str,
                                    Optional('mask'): str,
                                    Optional('port'): str,
                                    Optional('port_op'): str,
                                    Optional('from_port'): str,
                                    Optional('to_port'): str
                                },
                            }
                        },
                        Optional('remark'): str
                    }
                }
            }
        },
        Optional('cached_acl_log_flows'): {
            Optional('total'): int,
            Optional('denied'): int,
            Optional('deny_flow_max'): int
        },
        Optional('alert_interval'): int
    }

# =============================================
# Parser for 'show access-list'
# =============================================
class ShowAccessList(ShowAccessListSchema):
    """Parser for
        * show access-list
    """

    cli_command = 'show access-list'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # access-list acl1; 8 elements; name hash: 0xffffffff
        # access-list acl2; 50 elements; name hash: 0xffffffff
        # access-list acl3; 236 elements; name hash: 0xffffffff
        # access-list acl4; 5 elements; name hash: 0xffffffff
        # access-list acl5; 5 elements; name hash: 0xffffffff

        p1 = re.compile(r'^access-list (?P<name>\S+); +(?P<elements>\d+) +elements; +name +hash\: +(?P<namehash>0x[0-9a-fA-F]+)')

        # access-list acl1 line 1 extended permit udp host 10.38.193.26 host 9.0.128.50 eq domain log informational interval 300 (hitcnt=0) 0xffffffff
        # access-list acl1 line 2 extended permit tcp object-group group-In object-group group-Out eq bgp log disable (hitcnt=0) 0xffffffff 
        # access-list acl1 line 3 extended deny ip any any log informational interval 300 (hitcnt=60) 0xffffffff
        # access-list acl1 line 4 extended deny ip any4 any4 log informational interval 300 (hitcnt=0) 0xffffffff
        # access-list acl1 line 5 extended deny ip any6 any6 log informational interval 300 (hitcnt=0) 0xffffffff
        # access-list al_iga_to_sl line 2 extended permit tcp 10.1.1.0 255.255.255.224 range 1 10 10.2.1.0 255.255.255.0 informational interval 300 (hitcnt=0) 0xb5386dd9
        p2 = re.compile(r'(?P<tabbed> +)?access-list +(?P<name>\S+) +line +(?P<entry>\d+) +extended +(?P<action>(permit|deny)) +(object-group (?P<svc_obj_group>\S+)|(?P<protocol>\S+)) +(host (?P<src_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|object-group +(?P<src_object_group>\S+)|(?P<src_any>any4|any6|any)|((?P<src_network>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) +(?P<src_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))|(object (?P<src_object>\S+)))( +(?P<src_port_op>eq|lt|neq|range) +(?P<src_port>\S+))?( +(?P<src_to_port>(?!host|object-group|any4|any6|any)[0-9a-zA-Z]+))? +(host (?P<dst_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|object-group +(?P<dst_object_group>\S+)|(?P<dst_any>any4|any6|any)|((?P<dst_network>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) +(?P<dst_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))|(object (?P<dst_object>\S+)))( +(?P<dst_port_op>eq|lt|neq|range) +(?P<dst_port>[0-9a-zA-Z]+))?( +(?P<dst_to_port>((?!log)\S+)))?( +log(?P<log_disable> +disable)?)?( +informational +interval +(?P<informational_interval>\d+))? +\(hitcnt=(?P<hitcnt>\d+)\) +(?P<acl_hash>0x[0-9a-fA-F]+)')

        # access-list acl1 line 6 remark this is a remark
        p3 = re.compile(r' *access-list +(?P<name>\S+) +line +(?P<entry>\d+) +remark (?P<remark>.*)')

        # access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
        p4 = re.compile(r' *access-list +cached +ACL +log +flows: +total +(?P<total>\d+), +denied +(?P<denied>\d+) +\(deny-flow-max +(?P<deny_flow_max>\d+)\)')
        # alert-interval 300
        p5 = re.compile(r' *alert-interval +(?P<alert_interval>\d+)')

        previous_line_num = -1
        previous_acl_name = ''
        line_sub = -1
        for line in output.splitlines():
            line = line.strip()

            if line == '':
                continue

            # access-list acl1; 8 elements; name hash: 0xffffffff
            # access-list acl2; 50 elements; name hash: 0xffffffff
            # access-list acl3; 236 elements; name hash: 0xffffffff
            # access-list acl4; 5 elements; name hash: 0xffffffff
            # access-list acl5; 5 elements; name hash: 0xffffffff

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                acl_name = groups['name']
                acl_dict = ret_dict.setdefault('access-list', {}).setdefault(acl_name, {})
                acl_dict.update({'elements': int(groups['elements']) })
                acl_dict.update({'name_hash': groups['namehash'] })
                continue
            
            # access-list acl1 line 1 extended permit udp host 10.38.193.26 host 9.0.128.50 eq domain log informational interval 300 (hitcnt=0) 0xffffffff
            # access-list acl1 line 2 extended permit udp 10.38.0.0 255.255.0.0 9.0.0.0 255.0.0.0 eq domain log informational interval 300 (hitcnt=0) 0xffffffff
            # access-list acl1 line 3 extended permit object-group obj-gr1 10.38.0.0 255.255.0.0 9.0.0.0 255.0.0.0 eq domain log informational interval 300 (hitcnt=0) 0xffffffff
            # access-list acl1 line 4 extended permit tcp object-group group-In object-group group-Out eq bgp log disable (hitcnt=0) 0xffffffff 
            # access-list acl1 line 5 extended deny ip any any log informational interval 300 (hitcnt=60) 0xffffffff
            # access-list acl1 line 6 extended deny ip any4 any4 log informational interval 300 (hitcnt=0) 0xffffffff
            # access-list acl1 line 7 extended deny ip any6 any6 log informational interval 300 (hitcnt=0) 0xffffffff

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                acl_name = groups['name']
                line_num = groups['entry']
                if line_num == previous_line_num and acl_name == previous_acl_name:
                    parent_entry.update({'is_expandable': True})
                    parent_entry.update({'controls_flows': False})
                    line_entry = ret_dict.setdefault('access-list', {}).setdefault(acl_name, {}).setdefault('entry', {}).setdefault(int(line_num), {}).setdefault('group-expansion', {}).setdefault(line_sub, {})
                    line_sub = line_sub + 1
                else:
                    previous_line_num = line_num
                    previous_acl_name = acl_name
                    line_entry = ret_dict.setdefault('access-list', {}).setdefault(acl_name, {}).setdefault('entry', {}).setdefault(int(line_num), {})
                    parent_entry = line_entry
                    line_sub = 0
                    line_entry.update({'is_expandable': False})
                line_entry.update({'controls_flows': True})

                src_dict = line_entry.setdefault('source', {})
                dst_dict = line_entry.setdefault('destination', {})

                if 'src_host' in groups and not groups['src_host'] is None:
                    src_dict.update({'network' : groups['src_host'] })
                    src_dict.update({'mask' : '255.255.255.255' })
                if 'dst_host' in groups and not groups['dst_host'] is None:
                    dst_dict.update({'network' : groups['dst_host'] })
                    dst_dict.update({'mask' : '255.255.255.255' })
                if 'src_to_port' in groups and not groups['src_to_port'] is None:
                    src_dict.update({'from_port': groups['src_port']})
                    src_dict.update({'to_port': groups['src_to_port']})
                else:
                    if 'src_port' in groups and not groups['src_port'] is None:
                        src_dict.update({'port': groups['src_port']})
                if 'dst_to_port' in groups and not groups['dst_to_port'] is None:
                    dst_dict.update({'from_port': groups['dst_port']})
                    dst_dict.update({'to_port': groups['dst_to_port']})
                else:
                    if 'dst_port' in groups and not groups['dst_port'] is None:
                        dst_dict.update({'port': groups['dst_port']})
                if 'action' in groups and not groups['action'] is None:
                    line_entry.update({'action' : groups['action'] })
                if 'svc_obj_group' in groups and not groups['svc_obj_group'] is None:
                    line_entry.update({'object_group' : groups['svc_obj_group'] })
                if 'protocol' in groups and not groups['protocol'] is None:
                    line_entry.update({'protocol': groups['protocol'] })
                if 'log_disable' in groups and not groups['log_disable'] is None:
                    line_entry.update({'log': False})
                else:
                    line_entry.update({'log': True})
                if 'informational_interval' in groups and not groups['informational_interval'] is None:
                    line_entry.update({'informational_interval': int(groups['informational_interval']) })
                if 'hitcnt' in groups and not groups['hitcnt'] is None:
                    line_entry.update({'hitcnt': int(groups['hitcnt']) })
                if 'acl_hash' in groups and not groups['acl_hash'] is None:
                    line_entry.update({'acl_hash': groups['acl_hash'] })

                for name in ['any', 'object_group', 'network', 'mask', 'port_op', 'object' ]:
                    src_prefixed_name = 'src_' + name
                    if src_prefixed_name in groups and not groups[src_prefixed_name] is None:
                        src_dict.update({ name: groups[src_prefixed_name] })
                    dst_prefixed_name = 'dst_' + name
                    if dst_prefixed_name in groups and not groups[dst_prefixed_name] is None:
                        dst_dict.update({ name: groups[dst_prefixed_name] })

                continue

            # access-list acl1 line 6 remark this is a remark
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                acl_name = groups['name']
                line_num = groups['entry']
                previous_line_num = line_num
                previous_acl_name = acl_name
                acl_remark_dict = ret_dict.setdefault('access-list', {}).setdefault(acl_name, {}).setdefault('entry', {}).setdefault(int(line_num), {})
                acl_remark_dict.update({'remark': groups['remark']})
                continue


            # access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                flows = ret_dict.setdefault('cached_acl_log_flows', {})
                flows.update({'total': int(groups['total']) })
                flows.update({'denied': int(groups['denied']) })
                flows.update({'deny_flow_max': int(groups['deny_flow_max']) })
                continue


            # alert-interval 300
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({'alert_interval': int(groups['alert_interval']) })

        return ret_dict
