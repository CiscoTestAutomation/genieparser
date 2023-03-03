import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie import parsergen
from genie.libs.parser.utils.common import Common

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

class ShowIpv6MldSnoopingVlanSchema(MetaParser):
    """
    Schema for 'show ipv6 mld snooping vlan {vlan_id}'
    """
    schema = {
        'mld': str,
        'pim': str,
        'mldv2': str,
        'suppression': str,
        'solicit_query': str,
        'flood_query': int,
        'robustness': int,
        'query_count': int,
        'query_interval': int,
        'vlan': {
            Any(): {
                'mld': str,
                'pim': str,
                'mld_leave': str,
                'host_tracking': str,
                'robustness': int,
                'query_count': int,
                'query_interval': int,
            }
        }
    }

class ShowIpv6MldSnoopingVlan(ShowIpv6MldSnoopingVlanSchema):
    """
    Parser for 'show ipv6 mld snooping vlan {vlan_id}'
    """
    cli_command = 'show ipv6 mld snooping vlan {vlan_id}'

    def cli(self, vlan_id, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vlan_id=vlan_id))
        
        # MLD snooping                 : Disabled
        p0 = re.compile(r'^MLD\s+snooping\s+:\s+(?P<mld>\w+)$')

        # Global PIM Snooping          : Disabled
        p1 = re.compile(r'^[Global\s]*(PIM|Pim)\s+Snooping\s+:\s+(?P<pim>\w+)$')

        # MLDv2 snooping               : Disabled
        p2 = re.compile(r'^MLDv2\s+snooping\s+:\s+(?P<mldv2>\w+)$')
        
        # Listener message suppression : Disabled
        p3 = re.compile(r'^Listener\s+message\s+suppression\s+:\s+(?P<suppression>\w+)$')
        
        # TCN solicit query            : Disabled
        p4 = re.compile(r'^TCN\s+solicit\s+query\s+:\s+(?P<solicit_query>\w+)$')
        
        # TCN flood query count        : 2
        p5 = re.compile(r'^TCN\s+flood\s+query\s+count\s+:\s+(?P<flood_query>\d+)$')
        
        # Robustness variable          : 2
        p6 = re.compile(r'^Robustness\s+variable\s+:\s+(?P<robustness>\d+)$')
        
        # Last listener query count    : 2
        p7 = re.compile(r'^Last\s+listener\s+query\s+count\s+:\s+(?P<query_count>\d+)$')
        
        # Last listener query interval : 1000
        p8 = re.compile(r'^Last\s+listener\s+query\s+interval\s+:\s+(?P<query_interval>\d+)$')

        # Vlan 1:
        p9 = re.compile(r'^Vlan\s+(?P<vlan>\d+):$')

        # MLD immediate leave                 : Disabled
        p10 = re.compile(r'^MLD\s+immediate\s+leave\s+:\s+(?P<mld_leave>\w+)$')

        # Explicit host tracking              : Enabled
        p11 = re.compile(r'^Explicit\s+host\s+tracking\s+:\s+(?P<host_tracking>\w+)$')

        ret_dict = dict()
        vlan_flag = False
        for line in output.splitlines():
            line = line.strip()

            # MLD snooping                 : Disabled
            m = p0.match(line)
            if m:
                ret_dict['vlan'][vlan_id].update(m.groupdict()) if vlan_flag else ret_dict.update(m.groupdict())
                continue
            
            # Global PIM Snooping          : Disabled
            m = p1.match(line)
            if m:
                ret_dict['vlan'][vlan_id].update(m.groupdict()) if vlan_flag else ret_dict.update(m.groupdict())
                continue

            # MLDv2 snooping               : Disabled
            m = p2.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue
            
            # Listener message suppression : Disabled
            m = p3.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue
            
            # TCN solicit query            : Disabled
            m = p4.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue
            
            # TCN flood query count        : 2
            m = p5.match(line)
            if m:
                ret_dict.setdefault('flood_query', int(m.groupdict()['flood_query']))
                continue
            
            # Robustness variable          : 2
            m = p6.match(line)
            if m:
                robustness = int(m.groupdict()['robustness'])
                ret_dict['vlan'][vlan_id].setdefault(
                    'robustness', robustness
                    ) if vlan_flag else ret_dict.setdefault('robustness', robustness)
                continue
            
            # Last listener query count    : 2
            m = p7.match(line)
            if m:
                query_count = int(m.groupdict()['query_count'])
                ret_dict['vlan'][vlan_id].setdefault(
                    'query_count', query_count
                    ) if vlan_flag else ret_dict.setdefault('query_count', query_count)
                continue
            
            # Last listener query interval : 1000
            m = p8.match(line)
            if m:
                query_interval = int(m.groupdict()['query_interval'])
                ret_dict['vlan'][vlan_id].setdefault(
                    'query_interval', query_interval
                    ) if vlan_flag else ret_dict.setdefault('query_interval', query_interval)
                continue
            
            # Vlan 1:
            m = p9.match(line)
            if m:
                vlan_id = m.groupdict()['vlan']
                ret_dict.setdefault('vlan', {}).setdefault(vlan_id, {})
                vlan_flag = True
                continue
            
            # MLD immediate leave                 : Disabled
            m = p10.match(line)
            if m:
                ret_dict['vlan'][vlan_id].update(m.groupdict())
                continue

            # Explicit host tracking              : Enabled
            m = p11.match(line)
            if m:
                ret_dict['vlan'][vlan_id].update(m.groupdict())
                continue     

        return ret_dict


class ShowIpv6MldSnoopingMrouterSchema(MetaParser):
    """Schema for show ipv6 mld snooping mrouter"""
    schema = {
        'vlan': {
            Any(): {
                'ports': str
            }
        }
    }


class ShowIpv6MldSnoopingMrouter(ShowIpv6MldSnoopingMrouterSchema):
    """Parser for show ipv6 mld snooping mrouter"""

    cli_command = 'show ipv6 mld snooping mrouter'

    def cli(self, vlan=int(), output=None):
        if output is None:
            output = self.device.execute(f'{self.cli_command} vlan {vlan}' if vlan else self.cli_command)
        
        ret_dict = dict()

        res = parsergen.oper_fill_tabular(device_output=output,
                                    device_os='iosxe',
                                    table_terminal_pattern=r"^\n",
                                    header_fields=
                                    [ "Vlan",
                                        "ports" ],
                                    label_fields=
                                    [ "vlan",
                                        "ports" ],
                                    index=[0])

        # Building the schema out of the parsergen output
        if res.entries:
            for vlan, vlan_dict in res.entries.items():
                del vlan_dict['vlan']
                ret_dict.setdefault('vlan', {}).update({vlan: vlan_dict})
        
        return ret_dict

class ShowIpv6MldSnoopingMrouterVlanSchema(MetaParser):
    """Schema for show ipv6 mld snooping mrouter vlan {vlanid}"""

    schema = {
        'mld': {
            Any(): {
                'vlan': str
            },
        },
    }

class ShowIpv6MldSnoopingMrouterVlan(ShowIpv6MldSnoopingMrouterVlanSchema):

    """Parser for show ipv6 mld snooping mrouter vlan {vlanid}"""

    cli_command = ['show ipv6 mld snooping mrouter vlan {vlanid}']

    def cli(self, vlanid="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(vlanid=vlanid))

        #  100    Tw1/0/13(static)
        p1 = re.compile(r"^(?P<vlan>\d+)\s+(?P<ports>[\w\/\.]+)[\(\)\w]+$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            #  100    Tw1/0/13(static)
            m = p1.match(line)
            if m:
                ports_var = Common.convert_intf_name(m.groupdict()['ports'])
                ports_dict = ret_dict.setdefault('mld', {}).setdefault(ports_var, {})
                ports_dict['vlan'] = m.groupdict()['vlan']
                continue
        return ret_dict
