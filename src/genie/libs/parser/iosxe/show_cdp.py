import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowCdpNeighborsSchema(MetaParser):

    schema = {
        'cdp':
            {'device_id':
                {Any():
                    {'local_interface': str,
                     'hold_time': int,
                     Optional('capability'): str,
                     'platform': str,
                     'port_id': str, }, }, },
    }

class ShowCdpNeighborsSchemaDetail(MetaParser):

    schema = {
        'entries': int,
        'devices': 
            {'device_id':
                {Any():
                    {'platform': str,
                     'capabilities': str,
                     'local_interface': str,
                     'port_id': str,
                     'hold_time': int,
                     'version': str,
                     'entry_addresses':
                        {Any(): str},
                     'management_addresses':
                        {Any(): str},
                     Optional('duplex'): str,
                     'advertisement_ver': int,},
                },

            },
        }

# ================================
# Parser for 'show cdp neighbors'
# ================================
class ShowCdpNeighbors(ShowCdpNeighborsSchema):

    cli_command = 'show cdp neighbors'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        p1 = re.compile('^(?P<device_id>(\S+)) +'
                        '(?P<local_interface>([a-zA-Z0-9\s]+)) +'
                        '(?P<hold_time>(\d+))'
                        '(?: +(?P<capability>([A-Z\s]+)))? +'
                        '(?P<platform>([A-Z0-9\-]+)) +'
                        '(?P<port_id>([a-zA-Z0-9\/\s]+))$')

        p2 = re.compile('^(?P<device_id>(\S+)) +'
                        '(?P<local_interface>([a-zA-Z0-9\s\/]+)) +'
                        '(?P<hold_time>(\d+))'
                        '(?: +(?P<capability>([A-Z\s]+)))? +'
                        '(?P<platform>([a-zA-Z0-9\-]+)) +'
                        '(?P<port_id>([a-zA-Z0-9\/\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            result = p1.match(line)

            if not result:
                result = p2.match(line)

            if result:

                if not parsed_dict:

                    device_id_dict = parsed_dict.setdefault('cdp', {}).\
                                        setdefault('device_id', {})

                group = result.groupdict()
                device_id = group['device_id'].lower().strip()

                devices_dict = device_id_dict.setdefault(device_id, {})

                devices_dict['local_interface'] = \
                    group['local_interface'].lower().strip()
                devices_dict['hold_time'] = int(group['hold_time'])
                devices_dict['capability'] = \
                    group['capability'].lower().strip()
                devices_dict['platform'] = group['platform'].lower().strip()
                devices_dict['port_id'] = group['port_id'].lower().strip()

        return parsed_dict


# =======================================
# Parser for 'show cdp neighbors details'
# =======================================
class  ShowCdpNeighborsDetail(ShowCdpNeighborsSchemaDetail):
    cli_command = 'show cdp neighbors detail'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        deviceid_re   = re.compile(r'Device\s+ID:\s*(?P<device_id>\S+)')

        platf_cap_re  = re.compile(r'Platform:\s*(?P<platform>[a-zA-Z\d +\-]+)'
                                    '\s*\,\s*Capabilities:\s*'
                                    '(?P<capabilities>[a-zA-Z\d\s*\-\/]+)')

        interface_port_re  = re.compile(r'Interface:\s*'
                                         '(?P<interface>[\w\s\-\/\/]+)\s*\,'
                                         '*\s*Port\s*ID\s*[\(\w\)\s]+:\s*'
                                         '(?P<port_id>\w+)')

        holdtime_re   = re.compile(r'Holdtime\s*:\s*\s*(?P<holdtime>\d+)')

        ipaddress_re  = re.compile(r'\S*IP\s*address:\s*(?P<id_adress>\S*)')

        advertver_re  = re.compile(r'advertisement\s*version:\s*'
                                    '(?P<advertisement_ver>\d+)')

        entries_re    = re.compile(r'Total\s*cdp\s*entries\s*displayed\s*:\s*'
                                    '(?P<total_entries>\d*)')

        duplex_re     = re.compile(r'Duplex\s*:\s*(?P<duplex>\w+)')

        mngaddress_re = re.compile(r'Management\s*address\s*\([\w]+\)\s*\:\s*')
        entryaddress_re = re.compile(r'Entry\s*address\s*\(\w+\)\s*\:\s*')

        entry_address_flag = 0
        management_address_flag = 0

        parsed_dict = {'entries' : 0}

        for line in out.splitlines():
            line = line.strip()

            result = deviceid_re.match(line)

            if result:                
                device_id = result.group('device_id')
                device_dict = {}
                device_dict[device_id] = {}
                management_address_flag = 0
                continue

            result = platf_cap_re.match(line)

            if result:                
                platf_cap_dict = result.groupdict()
                device_dict[device_id]['capabilities'] = platf_cap_dict['capabilities']
                device_dict[device_id]['platform'] = platf_cap_dict['platform']

                entry_address_flag = 0

                continue

            result = interface_port_re.match(line)

            if result:
                interface_port_dict = result.groupdict()
                device_dict[device_id]['port_id'] = interface_port_dict['port_id']
                device_dict[device_id]['interface'] = interface_port_dict['interface']
                continue

            result = holdtime_re.match(line)

            if result:
                device_dict[device_id]['holdtime'] = int(result.group('holdtime'))
                continue

            if mngaddress_re.match(line): management_address_flag = 1

            if entryaddress_re.match(line): entry_address_flag = 1

            result = ipaddress_re.match(line)

            if result:              
            
                ip_adress = result.group('id_adress')

                if management_address_flag:                    
                    ip_list = device_dict[device_id].get('entry_addresses', [])
                    ip_list.append(ip_adress)
                    device_dict[device_id]['entry_addresses'] = ip_list

                if entry_address_flag:
                    ip_list = device_dict[device_id].get('management_addresses', [])
                    ip_list.append(ip_adress)
                    device_dict[device_id]['management_addresses'] = ip_list
                
                continue

            result = advertver_re.match(line)

            if result:
                device_dict[device_id]['advertisement_ver'] = result.group('advertisement_ver')
                continue

            result = entries_re.match(line)

            if result:
                parsed_dict['entries'] = int(result.group('total_entries'))
                continue

            result = duplex_re.match(line)

            if result:
                device_dict[device_id]['duplex'] = result.group('duplex')
                continue

        return parsed_dict
