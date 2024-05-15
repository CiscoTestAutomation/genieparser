"""show_dhcp.py

IOSXE parsers for the following show commands:

    * 'show dhcp lease'
    * 'show ipv6 dhcp interface'
    * 'show ipv6 dhcp interface {interface}'
    * 'show ip dhcp snooping statistics'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or

# ==============================================
# Schema Parser for 'show dhcp lease'
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

# ==============================================
# Parser for 'show dhcp lease'
# ==============================================
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


# ==============================================================================================
#  Schema Parser for
#     'show ipv6 dhcp interface'
#     'show ipv6 dhcp interface {interface}'
# ==============================================================================================
class ShowIpv6DhcpInterfaceSchema(MetaParser):
    """Schema for 
        'show ipv6 dhcp interface'
        'show ipv6 dhcp interface {interface}'
    """

    schema = {
        "interfaces" : {
            Any(): { #interface
                "mode"                                          : str,
                Optional("prefix_state")                        : str,
                Optional("address_state")                       : str,
                Optional("prefix_name")                         : str,
                Optional("prefix_rapid_commit")                 : str,
                Optional("address_rapid_commit")                : str,
                Optional("pool_name")                           : str,
                Optional("relay_destination")                   : str,
                Optional("preference_value")                    : int,
                Optional("hint_from_client")                    : str,
                Optional("rapid_commit")                        : str,
                Optional("known_servers") : {
                    Any () : { #servers
                        Optional("duid")                        : str,
                        Optional("preference")                  : int,
                        Optional("dns_server")                  : str,
                        Optional("domain_name")                 : str,
                        Optional("information_refresh_time")    : int,
                        Any() : { #address type IAPD or IANA
                            Optional("iaid")                    : str,
                            Optional("t1")                      : int,
                            Optional("t2")                      : int,
                            Optional("address")                 : str,
                            Optional("prefix")                  : str,
                            Optional("preferred_lifetime")      : int,
                            Optional("valid_lifetime")          : int,
                        },
                    },
                },
            },
        },
    }

# ==============================================
# Parser for 
#     'show ipv6 dhcp interface'
#     'show ipv6 dhcp interface {interface}'
# ==============================================
class ShowIpv6DhcpInterface(ShowIpv6DhcpInterfaceSchema):
    """Parser for: 
       'show ipv6 dhcp interface'
       'show ipv6 dhcp interface {interface}'
    """

    cli_command = ['show ipv6 dhcp interface', 'show ipv6 dhcp interface {interface}']

    def cli(self, interface=None, output=None):
        if output is None:
            if not interface:
                output = self.device.execute(self.cli_command[0])
            else:
                output = self.device.execute(self.cli_command[1].format(interface=interface))   

        ret_dict = {}

        #TenGigabitEthernet1/0/2.154 is in client mode
        p1 = re.compile(r'^(?P<interface>.*)\s+is\s+in\s+(?P<mode>.*)\s+mode\s*$')

        #Prefix State is OPEN
        p2 = re.compile(r'^Prefix\s+State\s+is\s+(?P<prefix_state>\w+)\s*$')

        #Address State is OPEN
        p3 = re.compile(r'^Address\s+State\s+is\s+(?P<address_state>\w+)\s*$')

        #Prefix name: TEST123
        p4 = re.compile(r'^Prefix\s+name:\s+(?P<prefix_name>\w+).*$')

        #Prefix Rapid-Commit: disabled
        p5 = re.compile(r'^Prefix\s+Rapid-Commit:\s+(?P<prefix_rapid_commit>\w+)\s*$')

        #Address Rapid-Commit: disabled
        p6 = re.compile(r'^Address\s+Rapid-Commit:\s+(?P<address_rapid_commit>\w+)\s*$')

        #Reachable via address: FE80::20C:29FF:FE22:1DA5
        p7 = re.compile(r'^Reachable\s+via\s+address:\s+(?P<known_servers>[0-9A-Fa-f:]+)\s*$')

        #DUID: 00030001001EE59BE700
        p8 = re.compile(r'^DUID:\s+(?P<duid>[0-9A-Fa-f]+)\s*$')

        #Preference: 0
        p9 = re.compile(r'^Preference:\s+(?P<preference>\d+)\s*$')

        #IA PD: IA ID 0x004C0001, T1 302400, T2 483840
        #IA NA: IA ID 0x004C0001, T1 43200, T2 69120
        p10 = re.compile(r'^(?P<type>IA PD|IA NA):\s+IA ID\s+(?P<iaid>[A-F0-9x]+),\s+T1\s+(?P<t1>.*),\s+T2\s+(?P<t2>.*)\s*$')

        #Prefix: 8881::/56
        #Address: 7772::6DBE:16C6:2F5:A636/128
        p11 = re.compile(r'^(?P<addr_or_prefix>Address|Prefix):\s+(?P<addr_or_prefix_value>[0-9A-F:\/]+)\s*$')

        #preferred lifetime 604800, valid lifetime 2592000
        p12 = re.compile(r'^preferred\s+lifetime\s+(?P<preferred_lifetime>\d+),\s+valid\s+lifetime\s+(?P<valid_lifetime>\d+).*$')

        #DNS server: 11::11
        p13 = re.compile(r'^DNS\s+server:\s+(?P<dns_server>[0-9A-Fa-f:]+)\s*$')

        #Domain name: cisco.com
        p14 = re.compile(r'^Domain\s+name:\s+(?P<domain_name>.*)\s*$')

        #Information refresh time: 0
        p15 = re.compile(r'^Information\s+refresh\s+time:\s+(?P<information_refresh_time>\d+)\s*$')

        #Using pool: A
        p16 = re.compile(r'^Using\s+pool:\s+(?P<pool_name>.*)\s*$')
       
        #    1::2
        p17 = re.compile(r'^(?P<relay_destination>[A-F0-9:]+)\s*$')

        #Preference value: 0
        p18 = re.compile(r'^Preference\s+value:\s+(?P<preference_value>\d+)\s*$')

        #Hint from client: ignored
        p19 = re.compile(r'^Hint\s+from\s+client:\s+(?P<hint_from_client>.*)\s*$')

        #Rapid-Commit: disabled
        p20 = re.compile(r'^Rapid-Commit:\s+(?P<rapid_commit>.*)\s*$')

        for line in output.splitlines():
            line = line.strip()
                
            #TenGigabitEthernet1/0/2.154 is in client mode
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(groups['interface'],{})
                dhcp_intf_dict["mode"] = groups['mode']
                continue

            #Prefix State is OPEN
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["prefix_state"] = groups['prefix_state']
                continue
            
            #Address State is OPEN
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["address_state"] = groups['address_state']
                continue

            #Prefix name: TEST123
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["prefix_name"] = groups['prefix_name']
                continue

            #Prefix Rapid-Commit: disabled
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["prefix_rapid_commit"] = groups['prefix_rapid_commit']
                continue

            #Address Rapid-Commit: disabled
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["address_rapid_commit"] = groups['address_rapid_commit']
                continue

            #Reachable via address: FE80::20C:29FF:FE22:1DA5
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                server_dict = dhcp_intf_dict.setdefault('known_servers',{}).setdefault(groups['known_servers'],{})
                continue

            #DUID: 00030001001EE59BE700
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                server_dict["duid"] = groups['duid']
                continue
        
            #Preference: 0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                server_dict["preference"] = int(groups['preference'])
                continue
            
            #IA PD: IA ID 0x004C0001, T1 302400, T2 483840
            #IA NA: IA ID 0x004C0001, T1 43200, T2 69120
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                addr_dict = server_dict.setdefault(groups['type'],{})
                addr_dict["iaid"] = groups['iaid']
                addr_dict["t1"] = int(groups['t1'])
                addr_dict["t2"] = int(groups['t2'])
                continue
            
            #Prefix: 8881::/56
            #Address: 7772::6DBE:16C6:2F5:A636/128
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                addr_dict[groups['addr_or_prefix'].lower()] = groups['addr_or_prefix_value']
                continue

            #preferred lifetime 604800, valid lifetime 2592000
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                addr_dict['preferred_lifetime'] = int(groups['preferred_lifetime'])
                addr_dict['valid_lifetime'] = int(groups['valid_lifetime'])
                continue
        
            #DNS server: 11::11
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                server_dict["dns_server"] = groups['dns_server']
                continue

            #Domain name: cisco.com
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                server_dict["domain_name"] = groups['domain_name']
                continue

            #Information refresh time: 0
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                server_dict["information_refresh_time"] = int(groups['information_refresh_time'])
                continue

            #Using pool: A
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["pool_name"] = groups['pool_name']
                continue
  
            #    1::2
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["relay_destination"] = groups['relay_destination']
                continue

            #Preference value: 0
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["preference_value"] = int(groups['preference_value'])
                continue
        
            #Hint from client: ignored
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["hint_from_client"] = groups['hint_from_client']
                continue
        
            #Rapid-Commit: disabled
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                dhcp_intf_dict["rapid_commit"] = groups['rapid_commit']
                continue

        return ret_dict

class ShowIpDhcpSnoopingBidingInterface(MetaParser):
    schema = {
        'count': int
    }


# ==========================================
# Parser for:
#   * 'show ip dhcp snooping binding interface {interface} | count {match}'
# ==========================================

class ShowIpDhcpSnoopingBibdingInterfaceCount(ShowIpDhcpSnoopingBidingInterface):
    """Parser for:
        show ip dhcp snooping binding interface {interface} | count {match}
    """
    cli_command = 'show ip dhcp snooping binding interface {interface} | count {match}'

    def cli(self, interface='', match='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface, match=match))    
        dict_count = {}

        # Number of lines which match regexp = 240
        p1 = re.compile(r"^Number of lines which match regexp\s*=\s*(?P<count>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 240
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['count'])
                dict_count['count'] = count

        return dict_count

# ==========================================
# Parser for:
#   * 'show ip verify source interface {interface} | count {match}'
# ==========================================

class ShowIpVerifySourceInterfaceCount(ShowIpDhcpSnoopingBidingInterface):
    """Parser for:
        show ip verify source interface {interface} | count {match}
    """
    cli_command = 'show ip verify source interface {interface} | count {match}'

    def cli(self, interface='', match='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface, match=match))
        dict_count = {}

        # Number of lines which match regexp = 240
        p1 = re.compile(r"^Number of lines which match regexp\s*=\s*(?P<count>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 240
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['count'])
                dict_count['count'] = count

        return dict_count

# ==========================
# Schema for 'show ip dhcp snooping statistics'
# ==========================
class ShowIpDhcpSnoopingStatisticsSchema(MetaParser):

    ''' Schema for "show ip dhcp snooping statistics" '''

    schema = {
        "packets_forwarded" : int,
        "packets_dropped" : int,
        "packets_dropped_from_untrusted_ports": int
        }

# ==========================
# Parser for 'show ip dhcp snooping statistics'
# ==========================
class ShowIpDhcpSnoopingStatistics(ShowIpDhcpSnoopingStatisticsSchema):

    ''' Parser for "show ip dhcp snooping statistics" '''

    cli_command = 'show ip dhcp snooping statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
       
        # Init vars
        ret_dict = {}

        # Packets Forwarded                                     = 122
        # Packets Dropped                                     = 0
        p1 = re.compile(r'^(?P<pattern>[\w\s]+)= +(?P<value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Packets Forwarded                                     = 122
            # Packets Dropped                                     = 0
            # Packets Dropped From untrusted ports                  = 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_')
                ret_dict.update({scrubbed.lower(): int(group['value'])})
                continue

        return ret_dict
