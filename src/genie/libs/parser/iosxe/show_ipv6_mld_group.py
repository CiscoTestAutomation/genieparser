import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowIpv6MldSnoopingGroupsSchema(MetaParser):
    """
    Schema for 'show ipv6 mld snooping address vlan {vlan_id}'
    """

    schema = {
        'mld_groups': {
            Any(): {
                'vlan_id': str,
                'type': str,
                'versions': list,
                'ports': list
            },
        }
    }


class ShowIpv6MldSnoopingGroups(ShowIpv6MldSnoopingGroupsSchema):
    """
    Parser for 'show ipv6 mld snooping address vlan {vlan_id}'
    """
    cli_command = [ 
        'show ipv6 mld snooping address vlan {vlan_id}'
    ]

    def cli(self, vlan_id="", output=None):
        if output is None:
            if vlan_id:
                cmd = self.cli_command[0].format(vlan_id=vlan_id) 
                out = self.device.execute(cmd)
            else:
                out = output

        # initial return dictionary
        mld_dict = {}

        # initial regexp pattern
        #100       FF1E:11::5               mld         v1          Twe1/0/30
        p1 = re.compile(r'^(?P<vlan_id>\d+)\s+(?P<group_ip>[0-9a-fA-F\.:]+)\s+(?P<type>\w+)\s+(?P<versions>\w+)\s+(?P<ports>[a-zA-Z\d\/\.]+)$')
        #100       FF1E:11::2               mld         v1,v2       Twe1/0/30
        p2 = re.compile(r'^(?P<vlan_id>\d+)\s+(?P<group_ip>[0-9a-fA-F\.:]+)\s+(?P<type>\w+)\s+(?P<versions>\w+\,\w+)\s+(?P<ports>[a-zA-Z\d\/\.]+)$')
        #100       FF1E:11::21              mld         v2          Twe1/0/30, Tu0
        p3 = re.compile(r'^(?P<vlan_id>\d+)\s+(?P<group_ip>[0-9a-fA-F\.:]+)\s+(?P<type>\w+)\s+(?P<versions>\w+)\s+(?P<ports>[a-zA-Z\d\/\.]+\,\s+[a-zA-Z\d\/\.]+)$')
        #100       FF1E:11::1               mld         v1,v2       Twe1/0/30, Tu0
        p4 = re.compile(r'^(?P<vlan_id>\d+)\s+(?P<group_ip>[0-9a-fA-F\.:]+)\s+(?P<type>\w+)\s+(?P<versions>\w+\,\w+)\s+(?P<ports>[a-zA-Z\d\/\.]+\,\s+[a-zA-Z\d\/\.]+)$')

        for line in out.splitlines():
            line = line.strip()
       
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict = mld_dict.setdefault('mld_groups', {})

                group_ip = group['group_ip']
                vlan_id = group['vlan_id']
                type = group['type']
                ports = group['ports']
                port_list = list(ports.split(','))
                versions = group['versions']
                version_list = list(versions.split(','))

                ret_dict[group_ip] = {}
                ret_dict[group_ip]['vlan_id'] = vlan_id
                ret_dict[group_ip]['type'] = type
                ret_dict[group_ip]['versions'] = version_list
                ret_dict[group_ip]['ports'] = port_list
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict = mld_dict.setdefault('mld_groups', {})

                group_ip = group['group_ip']
                vlan_id = group['vlan_id']
                type = group['type']
                ports = group['ports']
                port_list = list(ports.split(','))
                versions = group['versions']
                version_list = list(versions.split(','))

                ret_dict[group_ip] = {}
                ret_dict[group_ip]['vlan_id'] = vlan_id
                ret_dict[group_ip]['type'] = type
                ret_dict[group_ip]['versions'] = version_list
                ret_dict[group_ip]['ports'] = port_list
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()

                ret_dict = mld_dict.setdefault('mld_groups', {})

                group_ip = group['group_ip']
                vlan_id = group['vlan_id']
                type = group['type']
                ports = group['ports']
                port_list = list(ports.split(','))
                versions = group['versions']
                version_list = list(versions.split(','))

                ret_dict[group_ip] = {}
                ret_dict[group_ip]['vlan_id'] = vlan_id
                ret_dict[group_ip]['type'] = type
                ret_dict[group_ip]['versions'] = version_list
                ret_dict[group_ip]['ports'] = port_list
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict = mld_dict.setdefault('mld_groups', {})

                group_ip = group['group_ip']
                vlan_id = group['vlan_id']
                type = group['type']
                ports = group['ports']
                port_list = list(ports.split(','))
                versions = group['versions']
                version_list = list(versions.split(','))

                ret_dict[group_ip] = {}
                ret_dict[group_ip]['vlan_id'] = vlan_id
                ret_dict[group_ip]['type'] = type
                ret_dict[group_ip]['versions'] = version_list
                ret_dict[group_ip]['ports'] = port_list
                continue


        return mld_dict
