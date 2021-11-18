''' show_access_list.py

Parser for the following show commands:
    * show access-list
'''

# Python
import re
import logging

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
    	'access-list': {
            Any(): {
                Optional('elements'): int,
#               'name_hash': str,
                'entry': {
                    Any(): {
                      Optional('action'): str, 
                      Optional('protocol'): str,
                      Optional('source'): {
                          Optional('host'): str,
                          Optional('object_group'): str,
                          Optional('any'): str,
                          Optional('port'): str,
                      },
                      Optional('destination'): {
                          Optional('host'): str,
                          Optional('object_group'): str,
                          Optional('any'): str,
                          Optional('port'): str,
                      },
                      Optional('log'): bool,
                      Optional('disable'): bool,
                      Optional('hitcnt'): int,
                      Optional('acl_hash'): str,
                      Optional('remark'): str,
                    }
                },
            },
        },
        Optional('cached_acl_log_flows'): {
            'total': int,
            'denied': int,
            'deny_flow_max': int,
        },
        Optional('alert_interval'): int,
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
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        ret_dict['access-list'] = {}

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
        p2 = re.compile(r' *access-list +(?P<name>\S+) +line +(?P<entry>\d+) +extended +(?P<action>(permit|deny)) +(?P<protocol>\S+) +(host (?P<src_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|object-group +(?P<src_object_group>\S+)|(?P<dst_any>any|any4|any6))( +eq +(?P<src_port>\S+))? +(host (?P<dst_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|object-group +(?P<dst_object_group>\S+)|(?P<src_any>any|any4|any6))( +eq +(?P<dst_port>\S+))?( +(?P<log>log))?( +(?P<disable>disable))?( +informational +interval +(?P<informational_interval>\d+))? +\(hitcnt=(?P<hitcnt>\d+)\) +(?P<acl_hash>0x[0-9a-fA-F]+)')

        # access-list acl1 line 6 remark this is a remark
        p3 = re.compile(r' *access-list +(?P<name>\S+) +line +(?P<entry>\d+) +remark+(?P<remark>.*)')

        # access-list cached ACL log flows: total 0, denied 0 (deny-flow-max 4096)
        p4 = re.compile(r' *access-list +cached +ACL +log +flows: +total +(?P<total>\d+), +denied +(?P<denied>\d+) +\(deny-flow-max +(?P<deny_flow_max>\d+)\)')
        # alert-interval 300
        p5 = re.compile(r' *alert-interval +(?P<alert_interval>\d+)')

        for line in out.splitlines():
            line = line.strip()

            if line == '':
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                acl_name = groups['name']
                ret_dict['access-list'][acl_name] = {}
                ret_dict['access-list'][acl_name]['elements'] = int(groups['elements'])
#                ret_dict['access-list'][acl_name]['name_hash'] = groups['namehash']
                continue
            
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                acl_name = groups['name']
                line_num = groups['entry']
                if not acl_name in ret_dict['access-list'].keys() :
                    ret_dict['access-list'][acl_name] = {}
                if not 'entry' in ret_dict['access-list'][acl_name].keys():
                    ret_dict['access-list'][acl_name]['entry'] = {}
                line_entry = {}
                self.add_if_in_groups(line_entry, groups, ['action', 'protocol', 'hitcnt', 'acl_hash'])
                line_entry['source'] = {}
                line_entry['destination'] = {}

                self.add_host(line_entry['source'], groups, 'src_')
                self.add_host(line_entry['destination'], groups, 'dst_')

                if 'hitcnt' in line_entry:
                    line_entry['hitcnt'] = int(line_entry['hitcnt'])
                ret_dict['access-list'][acl_name]['entry'][line_num] = line_entry
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                line_num = groups['entry']
                if not acl_name in ret_dict['access-list'].keys() :
                    ret_dict['access-list'][acl_name] = {}
                if not 'entry' in ret_dict['access-list'][acl_name].keys():
                    ret_dict['access-list'][acl_name]['entry'] = {}
                ret_dict['access-list'][acl_name]['entry'][line_num] = {}
                ret_dict['access-list'][acl_name]['entry'][line_num]['remark'] = groups['remark']
                continue


            m = p4.match(line)
            if m:
                groups = m.groupdict()
                flows = {}
                flows['total'] = int(groups['total'])
                flows['denied'] = int(groups['denied'])
                flows['deny_flow_max'] = int(groups['deny_flow_max'])
                ret_dict['cached_acl_log_flows'] = flows
                continue


            m = p5.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['alert_interval'] = int(groups['alert_interval'])
#            else:
#                print('Not matching line: {}'.format(line))


        if not(bool(ret_dict['access-list'])):
            ret_dict = {}
        return ret_dict

    def add_if_in_groups(self, line_dict, groups, names):
        for name in names:
            if name in groups and not groups[name] is None:
                line_dict[name] = groups[name]

    def add_host(self, line_dict, groups, prefix):
        names = ['host', 'any', 'object_group']
        for name in names:
            prefixed_name = prefix + name
            if prefixed_name in groups and not groups[prefixed_name] is None:
                line_dict[name] = groups[prefixed_name]
