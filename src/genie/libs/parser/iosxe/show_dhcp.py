"""show_dhcp.py

IOSXE parsers for the following show commands:

    * 'show dhcp lease'
    * 'show ipv6 dhcp interface'
    * 'show ipv6 dhcp interface {interface}'
    * 'show ip dhcp snooping statistics'
    * 'show ip dhcp snooping track server'
    * 'show ip dhcp snooping statistics detail'
    * show ip dhcp sip session detail
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

        # Lease: Infinite
        p5_1 = re.compile(r'^\s*Lease: +(?P<lease>Infinite)')

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

                # Lease: Infinite
                m = p5_1.match(line)
                if m:
                    groups = m.groupdict()
                    dhcp_dict[interface]['lease'] = groups['lease']
                    dhcp_dict[interface]['renewal'] = 'na'
                    dhcp_dict[interface]['rebind'] = 'na'
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

# ==========================
# Schema for 'show ip dhcp snooping track server'
# ==========================
class ShowIpDhcpSnoopingTrackServerSchema(MetaParser):

    ''' Schema for "show ip dhcp snooping track server" '''

    schema = {
        'vlan' : {
            Any():{
                'mac': {
                    Any():
                        {
                            'ip_address' : str,
                            'mac_address': str,
                            'client_subnet': str,
                            'subnet_mask': str,
                            'relay_agent_address': str,
                            'last_updated': str
                        }
                }
            }
        }
    }

# ==========================
# Parser for 'show ip dhcp snooping statistics'
# ==========================
class ShowIpDhcpSnoopingTrackServer(ShowIpDhcpSnoopingTrackServerSchema):

    ''' Parser for "show ip dhcp snooping track server" '''

    cli_command = 'show ip dhcp snooping track server'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
       
        # Init vars
        ret_dict = {}

        # 10   20.1.2.1        68ca.e423.b846 20.1.2.0        255.255.255.0   0.0.0.0           Jul 17 2024 14:53:41 
        p1 = re.compile(r'^(?P<vlan>\d+) +(?P<ip>\S+) +(?P<mac>\S+) +(?P<client>\S+) +(?P<mask>\S+) +(?P<relay>\S+) +(?P<time>[\S+\s+]+)$')

        for line in output.splitlines():

            line = line.strip()
            # 10   20.1.2.1        68ca.e423.b846 20.1.2.0        255.255.255.0   0.0.0.0           Jul 17 2024 14:53:41 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan = group['vlan']
                mac = group['mac']
                # Build Dict
                vlan_dict = ret_dict.setdefault('vlan', {}).setdefault(vlan, {})
                mac_dict = vlan_dict.setdefault('mac', {}).setdefault(mac, {})
                # Set values
                mac_dict.update({
                    'ip_address': group['ip'],
                    'mac_address': group['mac'],
                    'client_subnet': group['client'],
                    'subnet_mask': group['mask'],
                    'relay_agent_address': group['relay'],
                    'last_updated': group['time']
                })
                continue

        return ret_dict

# =====================================================
# Schema for 'show ip dhcp snooping statistics detail'
# =====================================================    
class ShowIpDhcpSnoopingStatisticsDetailSchema(MetaParser):

    ''' Schema for "show ip dhcp snooping statistics detail" '''

    schema = {
        "dhcp_snooping_packets" : int,
        "packets_dropped_because" : {
            Any() : int
            },        
        }

# =====================================================
# Parser for 'show ip dhcp snooping statistics detail'
# =====================================================
class ShowIpDhcpSnoopingStatisticsDetail(ShowIpDhcpSnoopingStatisticsDetailSchema):

    ''' Parser for "show ip dhcp snooping statistics detail" '''

    cli_command = 'show ip dhcp snooping statistics detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
       
        # Init vars
        ret_dict = {}

        # Packets Processed by DHCP Snooping                    = 0
        p1 = re.compile(r'^Packets\s+Processed\s+by\s+DHCP\s+Snooping\s+=\s+(?P<dhcp_snooping_packets>\d+)$')

        # Packets Dropped Because
        p2 = re.compile(r'^Packets\s+Dropped\s+Because$')

        # No binding entry                                    = 0
        # Insertion of opt82 fail                             = 0
        p3 = re.compile(r'^(?P<pattern>[\w\s]+)=\s+(?P<value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Packets Processed by DHCP Snooping                    = 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'dhcp_snooping_packets': int(group['dhcp_snooping_packets'])})
                continue

            # Packets Dropped Because
            m = p2.match(line)
            if m:
                process_dict = ret_dict.setdefault('packets_dropped_because',{})
                continue

            # Nonzero giaddr                                      = 0
            # Source mac not equal to chaddr                      = 0 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group['pattern'].strip()).replace(' ', '_')
                process_dict.update({scrubbed.lower(): int(group['value'])})
                continue

        return ret_dict    

class ShowIpDhcpSipSessionDetailSchema(MetaParser):
    """Schema for show ip dhcp sip session detail"""

    schema = {
        "total_dhcp_session_count": int,
        "sessions": {
            Any(): {
                "mac_address": str,
                "uid": int,
                "sss_handle": str,
                "aaa_uid": int,
                "access_ie_handle": str,
                "ip_session_handle": str,
                "shdb_handle": str,
                "current_state": str,
                "last_state": str,
                "last_event": str,
                "last_to_last_state": str,
                "last_to_last_event": str,
                "access_interface": str,
                "incoming_interface": str,
                "elapsed_time_start": str,
                "ip_address": str,
                "elapsed_time_since_addr_acked": str,
                "vrf_id": int,
                "ip_domain": int,
                "circuit_id": str,
                "remote_id": str,
                "session_type": str,
                "default_configs": {
                    "class_name": str,
                    "class_name_len": int,
                    "ip_domain": int,
                    "vrf_id": int
                },
                "session_updated": bool,
                "dynamic_sync": bool
            }
        }
    }


class ShowIpDhcpSipSessionDetail(ShowIpDhcpSipSessionDetailSchema):
    """Parser for show ip dhcp sip session detail"""

    cli_command = "show ip dhcp sip session detail"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        sessions_dict = None
        current_session = None
        in_default_configs = False

        # Total DHCP Session Count: 1
        p1 = re.compile(r'^\s*Total\s+DHCP\s+Session\s+Count\s*:\s*(?P<count>\d+)\s*$')

        # DHCP SIP Session context with MAC Address: 3010.e495.b058
        p2 = re.compile(r'^\s*DHCP\s+SIP\s+Session\s+context\s+with\s+MAC\s+Address\s*:\s*(?P<mac>\S+)\s*$')

        # UID                :851
        p3 = re.compile(r'^\s*UID\s*:\s*(?P<uid>\d+)\s*$')

        # SSS Hdl            :0x2A00095C
        p4 = re.compile(r'^\s*SSS\s+Hdl\s*:\s*(?P<sss>0x[0-9A-Fa-f]+)\s*$')

        # AAA Uid            :2871
        p5 = re.compile(r'^\s*AAA\s+Uid\s*:\s*(?P<aaa>\d+)\s*$')

        # Access IE Hdl      :0x31000B2B
        p6 = re.compile(r'^\s*Access\s+IE\s+Hdl\s*:\s*(?P<acc>0x[0-9A-Fa-f]+)\s*$')

        # IP Session Hdl     :0x200000B7
        p7 = re.compile(r'^\s*IP\s+Session\s+Hdl\s*:\s*(?P<iph>0x[0-9A-Fa-f]+)\s*$')

        # SHDB Hdl           :0xDC00001D
        p8 = re.compile(r'^\s*SHDB\s+Hdl\s*:\s*(?P<shdb>0x[0-9A-Fa-f]+)\s*$')

        # Current State      :Up
        p9 = re.compile(r'^\s*Current\s+State\s*:\s*(?P<val>.+?)\s*$')

        # Last State         :Address Authorization
        p10 = re.compile(r'^\s*Last\s+State\s*:\s*(?P<val>.+?)\s*$')

        # Last Event         :Address Authorization Done Ev
        p11 = re.compile(r'^\s*Last\s+Event\s*:\s*(?P<val>.+?)\s*$')

        # Last to Last State :Start-on-sync/reload
        p12 = re.compile(r'^\s*Last\s+to\s+Last\s+State\s*:\s*(?P<val>.+?)\s*$')

        # Last to Last Event :Author Done Ev
        p13 = re.compile(r'^\s*Last\s+to\s+Last\s+Event\s*:\s*(?P<val>.+?)\s*$')

        # Access interface   :Tunnel1
        p14 = re.compile(r'^\s*Access\s+interface\s*:\s*(?P<val>\S+)\s*$')

        # Incoming interface :Tunnel1
        p15 = re.compile(r'^\s*Incoming\s+interface\s*:\s*(?P<val>\S+)\s*$')

        # Elapsed-time(start):00:04:39
        p16 = re.compile(r'^\s*Elapsed-time\(start\)\s*:\s*(?P<val>\S+)\s*$')

        # IP Addr            :40.0.0.2
        p17 = re.compile(r'^\s*IP\s+Addr\s*:\s*(?P<val>\S+)\s*$')

        #   since Addr acked :00:04:36
        p18 = re.compile(r'^\s*since\s+Addr\s+acked\s*:\s*(?P<val>\S+)\s*$')

        # VRF ID               :0
        p19 = re.compile(r'^\s*VRF\s+ID\s*:\s*(?P<val>\d+)\s*$')

        # IP Domain            :0
        p20 = re.compile(r'^\s*IP\s+Domain\s*:\s*(?P<val>\d+)\s*$')

        # Circuit ID         :120.0.40.10
        p21 = re.compile(r'^\s*Circuit\s+ID\s*:\s*(?P<val>\S+)\s*$')

        # Remote ID          :unauthenticated
        p22 = re.compile(r'^\s*Remote\s+ID\s*:\s*(?P<val>.+?)\s*$')

        # Session Type       :Converted to Dedicated
        p23 = re.compile(r'^\s*Session\s+Type\s*:\s*(?P<val>.+?)\s*$')

        # Default Configs are set as:
        p24 = re.compile(r'^\s*Default\s+Configs\s+are\s+set\s+as\s*:\s*$')

        #     Class name     : (len = 0)
        p25 = re.compile(r'^\s*Class\s+name\s*:\s*(?P<class_name>.*?)\s*\(len\s*=\s*(?P<class_name_len>\d+)\)\s*$')

        #     IP Domain      :0
        p26 = re.compile(r'^\s*IP\s+Domain\s*:\s*(?P<val>\d+)\s*$')

        #     VRF ID         :0
        p27 = re.compile(r'^\s*VRF\s+ID\s*:\s*(?P<val>\d+)\s*$')

        # Session updated    :False
        p28 = re.compile(r'^\s*Session\s+updated\s*:\s*(?P<val>\w+)\s*$')

        # Dynamic sync       :False
        p29 = re.compile(r'^\s*Dynamic\s+sync\s*:\s*(?P<val>\w+)\s*$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Total DHCP Session Count: 1
            m = p1.match(line)
            if m:
                ret_dict["total_dhcp_session_count"] = int(m.groupdict()["count"])
                continue

            # DHCP SIP Session context with MAC Address: 3010.e495.b058
            m = p2.match(line)
            if m:
                mac = m.groupdict()["mac"]
                sessions_dict = ret_dict.setdefault("sessions", {})
                current_session = sessions_dict.setdefault(mac, {})
                current_session["mac_address"] = mac
                in_default_configs = False
                continue

            # UID                :851
            m = p3.match(line)
            if m and current_session is not None:
                current_session["uid"] = int(m.groupdict()["uid"])
                continue

            # SSS Hdl            :0x2A00095C
            m = p4.match(line)
            if m and current_session is not None:
                current_session["sss_handle"] = m.groupdict()["sss"]
                continue

            # AAA Uid            :2871
            m = p5.match(line)
            if m and current_session is not None:
                current_session["aaa_uid"] = int(m.groupdict()["aaa"])
                continue

            # Access IE Hdl      :0x31000B2B
            m = p6.match(line)
            if m and current_session is not None:
                current_session["access_ie_handle"] = m.groupdict()["acc"]
                continue

            # IP Session Hdl     :0x200000B7
            m = p7.match(line)
            if m and current_session is not None:
                current_session["ip_session_handle"] = m.groupdict()["iph"]
                continue

            # SHDB Hdl           :0xDC00001D
            m = p8.match(line)
            if m and current_session is not None:
                current_session["shdb_handle"] = m.groupdict()["shdb"]
                continue

            # Current State      :Up
            m = p9.match(line)
            if m and current_session is not None:
                current_session["current_state"] = m.groupdict()["val"]
                continue

            # Last State         :Address Authorization
            m = p10.match(line)
            if m and current_session is not None:
                current_session["last_state"] = m.groupdict()["val"]
                continue

            # Last Event         :Address Authorization Done Ev
            m = p11.match(line)
            if m and current_session is not None:
                current_session["last_event"] = m.groupdict()["val"]
                continue

            # Last to Last State :Start-on-sync/reload
            m = p12.match(line)
            if m and current_session is not None:
                current_session["last_to_last_state"] = m.groupdict()["val"]
                continue

            # Last to Last Event :Author Done Ev
            m = p13.match(line)
            if m and current_session is not None:
                current_session["last_to_last_event"] = m.groupdict()["val"]
                continue

            # Access interface   :Tunnel1
            m = p14.match(line)
            if m and current_session is not None:
                current_session["access_interface"] = m.groupdict()["val"]
                continue

            # Incoming interface :Tunnel1
            m = p15.match(line)
            if m and current_session is not None:
                current_session["incoming_interface"] = m.groupdict()["val"]
                continue

            # Elapsed-time(start):00:04:39
            m = p16.match(line)
            if m and current_session is not None:
                current_session["elapsed_time_start"] = m.groupdict()["val"]
                continue

            # IP Addr            :40.0.0.2
            m = p17.match(line)
            if m and current_session is not None:
                current_session["ip_address"] = m.groupdict()["val"]
                continue

            #   since Addr acked :00:04:36
            m = p18.match(line)
            if m and current_session is not None:
                current_session["elapsed_time_since_addr_acked"] = m.groupdict()["val"]
                continue

            # VRF ID               :0
            m = p19.match(line)
            if m and current_session is not None and not in_default_configs:
                current_session["vrf_id"] = int(m.groupdict()["val"])
                continue

            # IP Domain            :0
            m = p20.match(line)
            if m and current_session is not None and not in_default_configs:
                current_session["ip_domain"] = int(m.groupdict()["val"])
                continue

            # Circuit ID         :120.0.40.10
            m = p21.match(line)
            if m and current_session is not None:
                current_session["circuit_id"] = m.groupdict()["val"]
                continue

            # Remote ID          :unauthenticated
            m = p22.match(line)
            if m and current_session is not None:
                current_session["remote_id"] = m.groupdict()["val"]
                continue

            # Session Type       :Converted to Dedicated
            m = p23.match(line)
            if m and current_session is not None:
                current_session["session_type"] = m.groupdict()["val"]
                continue

            # Default Configs are set as:
            m = p24.match(line)
            if m and current_session is not None:
                current_session.setdefault("default_configs", {})
                in_default_configs = True
                continue

            #     Class name     : (len = 0)
            m = p25.match(line)
            if m and current_session is not None and in_default_configs:
                groups = m.groupdict()
                class_name = groups["class_name"].strip() if groups["class_name"] is not None else ""
                class_len = int(groups["class_name_len"])
                def_cfg = current_session.setdefault("default_configs", {})
                def_cfg["class_name"] = class_name
                def_cfg["class_name_len"] = class_len
                continue

            #     IP Domain      :0
            m = p26.match(line)
            if m and current_session is not None and in_default_configs:
                def_cfg = current_session.setdefault("default_configs", {})
                def_cfg["ip_domain"] = int(m.groupdict()["val"])
                continue

            #     VRF ID         :0
            m = p27.match(line)
            if m and current_session is not None and in_default_configs:
                def_cfg = current_session.setdefault("default_configs", {})
                def_cfg["vrf_id"] = int(m.groupdict()["val"])
                continue

            # Session updated    :False
            m = p28.match(line)
            if m and current_session is not None:
                current_session["session_updated"] = True if m.groupdict()["val"].strip().lower() == "true" else False
                continue

            # Dynamic sync       :False
            m = p29.match(line)
            if m and current_session is not None:
                current_session["dynamic_sync"] = True if m.groupdict()["val"].strip().lower() == "true" else False
                continue

        return ret_dict
