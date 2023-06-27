"""show_dhcp.py

IOSXE parsers for the following show commands:

    * show dhcp lease

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

# ==============================================
# Parser for 'show dhcp lease'
# ==============================================

class ShowDhcpLeaseSchema(MetaParser):
    """Schema for: show dhcp lease"""

    schema = {
        "interfaces": {
            Any(): {
                "ip_addr": str,
                "subnet_mask": str,
                "lease_server": str,
                "state": str,
                "transaction_id": str,
                "lease": str,
                "renewal": str,
                "rebind": str,
                "default_gw": str,
                "retry_count": str,
                "client_id": str,
                "client_id_hex": str,
                "hostname": str,
            },
        },
    }

class ShowDhcpLease(ShowDhcpLeaseSchema):
    """Parser for: show dhcp lease"""

    cli_command = 'show dhcp lease'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        dhcp_dict = {}

        # Temp IP addr: 40.187.4.1  for peer on Interface: TenGigabitEthernet1/0/6
        p1 = re.compile(r'^\s*Temp +IP +addr: +(?P<ip_addr>\d+.\d+.\d+.\d+)\s+for +peer +on +Interface:\s+(?P<interface>[\w\/\.\-\:]+)')
        
        # Temp  sub net mask: 255.255.255.252
        p2 = re.compile(r'^\s*Temp  +sub +net +mask: +(?P<subnet_mask>\d+.\d+.\d+.\d+)')

        # DHCP Lease server: 40.187.4.2, state: 5 Bound
        p3 = re.compile(r'^\s*DHCP Lease server: +(?P<lease_server>\d+.\d+.\d+.\d+),\s+state: +(?P<state>\d+\s+\w+)')

        # DHCP transaction id: 6AAAF114
        p4 = re.compile(r'^\s*DHCP transaction id: +(?P<transaction_id>\w+)')

        # Lease: 86400 secs,  Renewal: 43200 secs,  Rebind: 75600 secs
        p5 = re.compile(r'^\s*Lease: +(?P<lease>\d+) secs,\s+Renewal: +(?P<renewal>\d+) secs,\s+Rebind: +(?P<rebind>\d+) secs')

        # Temp default-gateway addr: 40.187.4.2
        p6 = re.compile(r'^\s*Temp default-gateway addr: +(?P<default_gw>\d+.\d+.\d+.\d+)')

        # Retry count: 0   Client-ID: cisco-00fd.22bc.b846-Te1/0/6
        p7 = re.compile(r'^\s*Retry count:\s+(?P<retry_count>\d+)\s+Client-ID: +(?P<client_id>(.*))')

        # Client-ID hex dump: 636973636F2D303066642E323262632E
        p8 = re.compile(r'^\s*Client-ID hex dump: (?P<client_id_hex>[0-9A-Fa-f]+)')

        # 623834362D5465312F302F36
        p8_1 = re.compile(r'^\s*(?P<client_id_hex_ext>[A-Fa-f0-9]+$)')

        # Hostname: SM-Hub2
        p9 = re.compile(r'^\s*Hostname: +(?P<hostname>.*)')

        delimiter = 'Temp IP addr:'
        output_list = [str(delimiter+x) for x in out.split(delimiter) if x]

        for i in range(len(output_list)):
            current_output = output_list[i]
            for line in current_output.splitlines():
                if not line:
                    continue
                
                # Temp IP addr: 40.187.4.1  for peer on Interface: TenGigabitEthernet1/0/6
                m = p1.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict = ret_dict.setdefault('interfaces', {})
                    interface = groups['interface']
                    dhcp_dict[interface] = {}
                    dhcp_dict[interface]['ip_addr'] = groups['ip_addr']
                    continue

                # Temp  sub net mask: 255.255.255.252
                m = p2.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['subnet_mask'] = groups['subnet_mask']
                    continue

                # DHCP Lease server: 40.187.4.2, state: 5 Bound
                m = p3.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['lease_server'] = groups['lease_server']
                    dhcp_dict[interface]['state'] = groups['state']
                    continue

                # DHCP transaction id: 6AAAF114
                m = p4.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['transaction_id'] = groups['transaction_id']
                    continue

                # Lease: 86400 secs,  Renewal: 43200 secs,  Rebind: 75600 secs
                m = p5.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['lease'] = groups['lease']
                    dhcp_dict[interface]['renewal'] = groups['renewal']
                    dhcp_dict[interface]['rebind'] = groups['rebind']
                    continue

                # Temp default-gateway addr: 40.187.4.2
                m = p6.match(line)
                if m:
                    groups = m.groupdict()
                    default_gw = groups['default_gw']
                    continue

                # Retry count: 0   Client-ID: cisco-00fd.22bc.b846-Te1/0/6
                m = p7.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['retry_count'] = groups['retry_count']
                    dhcp_dict[interface]['client_id'] = groups['client_id']
                    continue

                # Client-ID hex dump: 636973636F2D303066642E323262632E
                m = p8.match(line)
                if m:
                    groups = m.groupdict()
                    client_id_hex  = groups['client_id_hex']
                    continue

                # 623834362D5465312F302F36 
                m = p8_1.match(line)
                if m:
                    groups = m.groupdict()
                    client_id_hex_ext = groups['client_id_hex_ext']
                    continue

                # Hostname: SM-Hub2
                m = p9.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['hostname'] = groups['hostname']
                    continue
            
            if 'client_id_hex_ext' in locals():
                dhcp_dict[interface]['client_id_hex'] = client_id_hex+client_id_hex_ext
                del client_id_hex_ext
            else:
                dhcp_dict[interface]['client_id_hex'] = client_id_hex
                del client_id_hex
            
            if 'default_gw' in locals():
                dhcp_dict[interface]['default_gw'] = default_gw
                del default_gw
            else:
                dhcp_dict[interface]['default_gw'] = 'na'

        return ret_dict