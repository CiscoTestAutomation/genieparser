"""show_platform_hardware_fed.py
    * 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance {protocol_options}'
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import ListOf
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And, ListOf


log = logging.getLogger(__name__)

class ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocolsSchema(MetaParser):
    """
    Schema for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance {protocol_options}
    """
    schema = {
        'destinationport': str,
        }

# ===================================================
# Superparser for
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-port-v6 {sourceipv6} {destinationipv6} {ipv6_flow_label} {next_header} {sour_port} {dest_port}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-v6 {sourcemac} {destinationmac} {flow_label} {next_header}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-port-v4 {source} {destinatio} {protocol} {sour_port} {dest_port}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-v4 {source} {destination} {protocol}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-port-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-v6 {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}'
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-v4 {sourcemac} {sourceip} {destinationip} {protocol}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-port-v4 {sourcemac} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-port-v6 {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-v6 {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-port-v4 {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-v4 {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol}',
  # *'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlanid {sourcemac} {vlan_id}',
  # ===================================================
  
class ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocolsSchema):
    """Parser for 'show platform software fed switch {switch} etherchannel {portchannelnum} 
    load-balance {protocol_options}' """

    def cli(self, output=None):

        # initial return dictionary
        ret_dict = {}
        
        #Dest Port: : GigabitEthernet1/0/4
        p1 = re.compile(r'^Dest\s+Port\S+\s+\S+\s(?P<destinationport>\S+)$')  
        
        for line in output.splitlines():
            line = line.strip()
            
            #Dest Port: : GigabitEthernet1/0/4
            m = p1.match(line)
            if m:
                group=m.groupdict()
                ret_dict['destinationport']= group['destinationport']
                continue
            
        return ret_dict


class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceIpflnhportv6(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for 'show platform software fed switch {switch} etherchannel {portchannelnum} 
    load-balance ip-fl-nh-port-v6 {sourceipv6} {destinationipv6} {ipv6_flow_label} {next_header} {sour_port} {dest_port}'
    """
    
    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-port-v6 '
    '{sourceipv6} {destinationipv6} {ipv6_flow_label} {next_header} {sour_port} {dest_port}')

    def cli(self, switch, portchannelnum, sourceipv6, destinationipv6, 
            ipv6_flow_label, next_header, sour_port, dest_port, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, 
                                    sourceipv6=sourceipv6, destinationipv6=destinationipv6, 
                                    ipv6_flow_label=ipv6_flow_label, next_header=next_header, 
                                    sour_port=sour_port, dest_port=dest_port)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceIpflnhv6(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for 'show platform software fed switch {switch} etherchannel {portchannelnum}
    load-balance ip-fl-nh-v6 {sourcemac} {destinationmac} {flow_label} {next_header}'
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-fl-nh-v6 '
    '{sourcemac} {destinationmac} {flow_label} {next_header}')

    def cli(self, switch, portchannelnum, sourcemac, destinationmac, flow_label, next_header, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    destinationmac=destinationmac, flow_label=flow_label, next_header=next_header)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)
    
class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceIpprotocolportv4(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for 'show platform software fed switch {switch} etherchannel {portchannelnum} 
    load-balance ip-protocol-port-v4 {source} {destination} {protocol} {sour_port} {dest_port}'
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-port-v4 '
    '{source} {destination} {protocol} {sour_port} {dest_port}')

    def cli(self, switch, portchannelnum, source, destination, protocol, 
            sour_port, dest_port, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, source=source, 
                                    destination=destination, protocol=protocol, sour_port=sour_port, dest_port=dest_port)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceIpprotocolv4(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-v4 
    {source} {destination} {protocol}'
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance ip-protocol-v4 '
    '{source} {destination} {protocol}')

    def cli(self, switch, portchannelnum, source, destination, protocol, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, 
                                    source=source, destination=destination, protocol=protocol)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacipflnhportv6(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-port-v6 {sourcemac} 
    {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-port-v6 '
    '{sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}')

    def cli(self, switch, portchannelnum, sourcemac, sourceipv6, destinationipv6, ipv6_fl, 
            next_header, sour_port, dest_port, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    sourceipv6=sourceipv6, destinationipv6=destinationipv6, ipv6_fl=ipv6_fl, 
                                    next_header=next_header, sour_port=sour_port, dest_port=dest_port)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)
        
class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacipflnhv6(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-v6 
    {sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-fl-nh-v6 ' 
    '{sourcemac} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}')

    def cli(self, switch, portchannelnum, sourcemac, sourceipv6, destinationipv6, ipv6_fl, next_header, output=None):
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    sourceipv6=sourceipv6, destinationipv6=destinationipv6, 
                                    ipv6_fl=ipv6_fl, next_header=next_header)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)
        
class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacipprotocolv4(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-v4 
    {sourcemac} {sourceip} {destinationip} {protocol}
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-v4 '
    '{sourcemac} {sourceip} {destinationip} {protocol}')

    def cli(self, switch, portchannelnum, sourcemac, sourceip, destinationip, protocol, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    sourceip=sourceip, destinationip=destinationip, protocol=protocol)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacipprotocolportv4(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-port-v4 
    {sourcemac} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-ip-protocol-port-v4 '
    '{sourcemac} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}')

    def cli(self, switch, portchannelnum, sourcemac, sourceip, destinationip, protocol, sour_port, 
            dest_port, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    sourceip=sourceip, destinationip=destinationip, protocol=protocol, 
                                    sour_port=sour_port, dest_port=dest_port)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacvlanipflnhportv6(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-port-v6 
    {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-port-v6 '
    '{sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header} {sour_port} {dest_port}')

    def cli(self, switch, portchannelnum, sourcemac, vlan_id, sourceipv6, destinationipv6, ipv6_fl, 
            next_header, sour_port, dest_port, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    vlan_id=vlan_id, sourceipv6=sourceipv6, destinationipv6=destinationipv6, 
                                    ipv6_fl=ipv6_fl, next_header=next_header, sour_port=sour_port, dest_port=dest_port)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacvlanipflnhv6(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-v6 
    {sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}'
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-fl-nh-v6 '
    '{sourcemac} {vlan_id} {sourceipv6} {destinationipv6} {ipv6_fl} {next_header}')

    def cli(self, switch, portchannelnum, sourcemac, vlan_id, sourceipv6, destinationipv6, ipv6_fl, next_header, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    vlan_id=vlan_id, sourceipv6=sourceipv6, destinationipv6=destinationipv6, 
                                    ipv6_fl=ipv6_fl, next_header=next_header)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacvlanipprotocolportv4(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-port-v4 
    {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}'
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-port-v4 '
    '{sourcemac} {vlan_id} {sourceip} {destinationip} {protocol} {sour_port} {dest_port}')

    def cli(self, switch, portchannelnum, sourcemac, vlan_id, sourceip, destinationip, protocol, 
            sour_port, dest_port, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    vlan_id=vlan_id, sourceip=sourceip, destinationip=destinationip, 
                                    protocol=protocol, sour_port=sour_port, dest_port=dest_port)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacvlanipprotocolv4(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-v4 
    {sourcemac} {vlan_id} {sourceip} {destinationip} {protocol}'
    """

    cli_command = ('show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlan-ip-protocol-v4 '
    '{sourcemac} {vlan_id} {sourceip} {destinationip} {protocol}')

    def cli(self, switch, portchannelnum, sourcemac, vlan_id, sourceip, destinationip, protocol, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, 
                                    vlan_id=vlan_id, sourceip=sourceip, destinationip=destinationip, protocol=protocol)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)

class ShowPlatformSoftwareFedSwitchEtherchannelLoadbalanceMacvlanid(ShowPlatformSoftwareFedSwitchActiveEtherchannelLoadbalanceProtocols):
    """Parser for show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlanid {sourcemac} {vlan_id}
    """
    cli_command = 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance mac-vlanid {sourcemac} {vlan_id}'

    def cli(self, switch, portchannelnum, sourcemac, vlan_id, output=None):
    
        cmd = self.cli_command.format(switch=switch, portchannelnum=portchannelnum, sourcemac=sourcemac, vlan_id=vlan_id)
        output = self.device.execute(cmd)
            
        return super().cli(output=output)
        


class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTableSchema(MetaParser):
    """Schema for 'show platform hardware fed {switch} {state} fwd-asic insight vrf_route_table'"""
    schema = {
        'vrf_route_table': {
            str: {  # This will be the IP prefix (like "10.1.1.0/24", "192.168.1.1/32", etc.)
                'vrf_gid': int,
                'ip_version': int,
                'ip_prefix': str,
                'dest_type': str,
                'dest_id': int,
                'dest_info': str,
                'class_id': int,
                'drop': bool,
                'route_user_data': str
            }
        }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTable(ShowPlatformHardwareFedSwitchActiveFwdAsicInsightVrfRouteTableSchema):
    """Parser for `show platform hardware fed {switch} {state} fwd-asic insight vrf_route_table`"""

    cli_command = 'show platform hardware fed {switch} {state} fwd-asic insight vrf_route_table'

    def cli(self, switch, state, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch, state=state))

        ret_dict = {}

        # +---------+------------+--------------------+--------------+---------+-----------+----------+-------+-----------------+
        # | Vrf GID | IP Version | IP Prefix          | Dest Type    | Dest ID | Dest Info | Class ID | Drop  | Route User Data |
        # +---------+------------+--------------------+--------------+---------+-----------+----------+-------+-----------------+
        # | 2       | 4          | 14.1.0.255/32      | for_us       | 0       | N/A       | 0        | False | 104865530382056 |
        p1 = re.compile(
            r'^\|\s*(?P<vrf_gid>\d*)\s*\|'
            r'\s*(?P<ip_version>\d*)\s*\|'
            r'\s*(?P<ip_prefix>[^|]*)\|'
            r'\s*(?P<dest_type>[^|]*)\|'
            r'\s*(?P<dest_id>\d*)\s*\|'
            r'\s*(?P<dest_info>[^|]*)\|'
            r'\s*(?P<class_id>\d*)\s*\|'
            r'\s*(?P<drop>\w*)\s*\|'
            r'\s*(?P<route_user_data>[^|]*)\|$'
        )

        current_vrf_gid = None
        current_ip_version = None

        for line in output.splitlines():
            line = line.strip()

            # +---------+------------+--------------------+--------------+---------+-----------+----------+-------+-----------------+
            # | Vrf GID | IP Version | IP Prefix          | Dest Type    | Dest ID | Dest Info | Class ID | Drop  | Route User Data |
            # +---------+------------+--------------------+--------------+---------+-----------+----------+-------+-----------------+
            # | 2       | 4          | 14.1.0.255/32      | for_us       | 0       | N/A       | 0        | False | 104865530382056 |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['vrf_gid'] and group['ip_version']:
                    current_vrf_gid = int(group['vrf_gid'])
                    current_ip_version = int(group['ip_version'])
                elif current_vrf_gid is not None and current_ip_version is not None:
                    pass
                else:
                    continue

                ip_prefix = group['ip_prefix'].strip()
                if not ip_prefix:
                    continue

                dest_type = group['dest_type'].strip()
                dest_id = int(group['dest_id']) if group['dest_id'] else 0
                dest_info = group['dest_info'].strip()
                class_id = int(group['class_id']) if group['class_id'] else 0
                drop = group['drop'].strip().lower() == 'true'
                route_user_data = group['route_user_data'].strip()

                # Use IP prefix as the key according to the schema
                route_dict = ret_dict.setdefault('vrf_route_table', {}).setdefault(ip_prefix, {})
                route_dict.update({
                    'vrf_gid': current_vrf_gid,
                    'ip_version': current_ip_version,
                    'ip_prefix': ip_prefix,
                    'dest_type': dest_type,
                    'dest_id': dest_id,
                    'dest_info': dest_info,
                    'class_id': class_id,
                    'drop': drop,
                    'route_user_data': route_user_data
                })

        return ret_dict


class ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatusSchema(MetaParser):
    """Schema for 'show platform hardware fed {switch} {switch_id} fwd-asic insight l2_attachment_circuit_status({sys_port_gid})'"""

    schema = {
        'l2_circuit_status': {
            'l2_ac_info': {
                Any(): {
                    'ac_type': str,
                    Optional('switch_gid'): int,
                    Optional('eth_port_oid'): int,
                    Optional('vlan_tag'): int,
                    'sysport_gid': int,
                    'ac_gid': int,
                    Optional('switch_cookie'): int,
                    'sysport_cookie': str,
                    Optional('ac_cookie'): str
                }
            }
        }
    }
    
class ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatus(ShowPlatformHardwareFedSwitchFwdAsicInsightL2AttachmentCircuitStatusSchema):
    """Parser for 'show platform hardware fed {switch} {switch_id} fwd-asic insight l2_attachment_circuit_status({sys_port_gid})'"""

    cli_command = 'show platform hardware fed {switch} {switch_id} fwd-asic insight l2_attachment_circuit_status({sys_port_gid})'
    def cli(self, switch='' , switch_id='', sys_port_gid= "", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(
                switch=switch,
                switch_id=switch_id,
                sys_port_gid=sys_port_gid
            ))

        parsed_data = {}
        current_entry = None
        entry_key = None

        # | ac_type: L2-DENSE  |             | vlan_tag: 1           | sysport_gid: 300        |
        # | ac_type: L2        | switch_gid: 300    | eth_port_oid: 1925    | sysport_gid: 320         |
        p1 = re.compile(r'^ac_type:\s+(?P<ac_type>\S+)\s*\|(?:\s*switch_gid:\s+(?P<switch_gid>\d+))?\s*\|(?:\s*vlan_tag:\s+(?P<vlan_tag>\d+)|\s*eth_port_oid:\s+(?P<eth_port_oid>\d+))?\s*\|(?:\s*sysport_gid:\s+(?P<sysport_gid>\d+))?\s*$')

        # | ac_gid: 122906     |             | eth_port_oid: 1677    | sysport_cookie: Gi2/0/2 |
        # | ac_gid: 6           | switch_cookie: 300 |                       | sysport_cookie: Gi2/0/24 |
        p2 = re.compile(r'^ac_gid:\s+(?P<ac_gid>\d+)\s*\|(?:\s*switch_cookie:\s+(?P<switch_cookie>\d+))?\s*\|(?:\s*eth_port_oid:\s+(?P<eth_port_oid>\d+))?\s*\|(?:\s*sysport_cookie:\s+(?P<sysport_cookie>\S+))?\s*$')

        # | ac_cookie: Gi2/0/2 |             |                       |                         |
        p3 = re.compile(r'^ac_cookie:\s+(?P<ac_cookie>\S+)$')

        for line in output.splitlines():
            line = line.strip('| ').strip()
            if not line:
                continue

            # | ac_type: L2-DENSE  |             | vlan_tag: 1           | sysport_gid: 300        |
            # | ac_type: L2        | switch_gid: 300    | eth_port_oid: 1925    | sysport_gid: 320         |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                # Use eth_port_oid, vlan_tag, or sysport_gid as entry key (in that order)
                if group.get('eth_port_oid'):
                    entry_key = int(group['eth_port_oid'])
                elif group.get('vlan_tag'):
                    entry_key = int(group['vlan_tag'])
                elif group.get('sysport_gid'):
                    entry_key = int(group['sysport_gid'])
                else:
                    continue

                current_entry = parsed_data.setdefault('l2_circuit_status', {}).setdefault('l2_ac_info', {}).setdefault(entry_key, {})
                current_entry['ac_type'] = group['ac_type']
                if group.get('switch_gid'):
                    current_entry['switch_gid'] = int(group['switch_gid'])
                if group.get('eth_port_oid'):
                    current_entry['eth_port_oid'] = int(group['eth_port_oid'])
                if group.get('vlan_tag'):
                    current_entry['vlan_tag'] = int(group['vlan_tag'])
                if group.get('sysport_gid'):
                    current_entry['sysport_gid'] = int(group['sysport_gid'])
                continue

            # | ac_gid: 122906     |             | eth_port_oid: 1677    | sysport_cookie: Gi2/0/2 |
            # | ac_gid: 6           | switch_cookie: 300 |                       | sysport_cookie: Gi2/0/24 |
            m = p2.match(line)
            if m and current_entry is not None:
                group = m.groupdict()
                current_entry['ac_gid'] = int(group['ac_gid'])
                if group.get('switch_cookie'):
                    current_entry['switch_cookie'] = int(group['switch_cookie'])
                if group.get('eth_port_oid'):
                    current_entry['eth_port_oid'] = int(group['eth_port_oid'])
                if group.get('sysport_cookie'):
                    current_entry['sysport_cookie'] = group['sysport_cookie']
                continue

            # | ac_cookie: Gi2/0/2 |             |                       |                         |
            m = p3.match(line)
            if m and current_entry is not None:
                group = m.groupdict()
                current_entry['ac_cookie'] = group['ac_cookie']
                continue

        return parsed_data

class ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDefSchema(MetaParser):
    """Schema for 'show platform hardware fed {switch} {state} fwd-asic insight acl_table_def()'"""
    schema = {
        'acl_entries': {
            int: {
                'acl_oid': int,
                Optional('acl_cookie'): str,
                'acl_key_profile_oid': int,
                Optional('acl_key_profile_cookie'): str,
                'acl_match_key_fields': ListOf(str),
                Optional('acl_range_cookie'): str,
                Optional('acl_range_direction'): str,
                Optional('acl_range_count'): str,
                Optional('acl_cmd_profile_oid'): int,
                Optional('acl_commands'): ListOf(str),
                Optional('source_pcl_info'): str,
                Optional('destination_pcl_info'): str,
            }
        }
    }


class ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDef(ShowPlatformHardwareFedSwitchFwdAsicInsightAclTableDefSchema):
    """Parser for 'show platform hardware fed {switch} {state} fwd-asic insight acl_table_def()'"""

    cli_command = "show platform hardware fed {switch} {state} fwd-asic insight acl_table_def()"

    def cli(self, switch, state, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(switch=switch, state=state)
            )

        result_dict = {}

        # |  acl_oid:583 | acl_key_profile_oid:511 | IPV4_SIP | acl_range_cookie: | 581 | DROP | | |
        # |  acl_oid:1319| acl_key_profile_oid:1227| IPV4_SIP | acl_range_cookie: |     |      | | |
        p1 = re.compile(
            r'^\|\s*acl_oid:(?P<acl_oid>\d+)\s*\|'
            r'\s*acl_key_profile_oid:(?P<acl_key_profile_oid>\d+)\s*\|'
            r'\s*(?P<acl_match_key_fields>\S*)\s*\|'
            r'\s*acl_range_cookie:(?P<acl_range_cookie>\S*)\s*\|'
            r'\s*(?P<acl_cmd_profile_oid>\S*)\s*\|'
            r'\s*(?P<acl_commands>\S*)\s*\|'
            r'\s*(?P<source_pcl_info>\S*)\s*\|'
            r'\s*(?P<destination_pcl_info>\S*)\s*\|$'
        )

        # |  acl_cookie: | acl_key_profile_cookie: | IPV4_DIP | acl_range_direction: | | FORCE_TRAP_WITH_EVENT | | |
        # |  acl_cookie: | acl_key_profile_cookie: | IPV4_DIP | acl_range_direction: | |                       | | |           
        p2 = re.compile(
            r'^\|\s*acl_cookie:(?P<acl_cookie>\S*)\s*\|'
            r'\s*acl_key_profile_cookie:(?P<acl_key_profile_cookie>\S*)\s*\|'
            r'\s*(?P<acl_match_key_fields>\S*)\s*\|'
            r'\s*acl_range_direction:(?P<acl_range_direction>\S*)\s*\|'
            r'\s*(?P<acl_cmd_profile_oid>\S*)\s*\|'
            r'\s*(?P<acl_commands>\S*)\s*\|'
            r'\s*(?P<source_pcl_info>\S*)\s*\|'
            r'\s*(?P<destination_pcl_info>\S*)\s*\|$'
        )

        # |              |                         | TOS | acl_range_count: | | COUNTER | | |
        # |              |                         | TOS | acl_range_count: | |         | | |       
        p3 = re.compile(
            r'^\|\s*\|\s*\|\s*(?P<acl_match_key_fields>\S*)\s*\|'
            r'\s*acl_range_count:(?P<acl_range_count>\S*)\s*\|'
            r'\s*\|\s*(?P<acl_commands>\S*)\s*\|'
            r'\s*(?P<source_pcl_info>\S*)\s*\|'
            r'\s*(?P<destination_pcl_info>\S*)\s*\|$'
        )

        # |              |                         | PROTOCOL | | | DO_MIRROR | | |
        # |              |                         | PROTOCOL | | |           | | |                    
        p4 = re.compile(
            r'^\|\s*\|\s*\|\s*(?P<acl_match_key_fields>\S*)\s*\|\s*\|\s*\|\s*(?P<acl_commands>\S*)\s*\|'
            r'\s*(?P<source_pcl_info>\S*)\s*\|'
            r'\s*(?P<destination_pcl_info>\S*)\s*\|$'
        )

        current_acl_oid = None

        for line in output.splitlines():
            line = line.strip()
            if not line or line.startswith('+') or line.startswith('|     ACL Info'):
                continue

            # |  acl_oid:583 | acl_key_profile_oid:511 | IPV4_SIP | acl_range_cookie: | 581 | DROP | | |
            # |  acl_oid:1319| acl_key_profile_oid:1227| IPV4_SIP | acl_range_cookie: |     |      | | |
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                current_acl_oid = int(group['acl_oid'])
                entry = result_dict.setdefault('acl_entries', {}).setdefault(current_acl_oid, {
                    'acl_oid': current_acl_oid,
                    'acl_key_profile_oid': int(group['acl_key_profile_oid']),
                    'acl_match_key_fields': [],
                    'acl_commands': [],
                })
                if group['acl_match_key_fields']:
                    entry['acl_match_key_fields'].append(group['acl_match_key_fields'])
                if group['acl_range_cookie'] and group['acl_range_cookie'] != 'None':
                    entry['acl_range_cookie'] = group['acl_range_cookie']
                if group['acl_cmd_profile_oid'] and group['acl_cmd_profile_oid'] != 'None':
                    entry['acl_cmd_profile_oid'] = int(group['acl_cmd_profile_oid'])
                if group['acl_commands']:
                    entry['acl_commands'].append(group['acl_commands'])
                if group['source_pcl_info'] and group['source_pcl_info'] != 'None':
                    entry['source_pcl_info'] = group['source_pcl_info']
                if group['destination_pcl_info'] and group['destination_pcl_info'] != 'None':
                    entry['destination_pcl_info'] = group['destination_pcl_info']
                continue

            # |  acl_cookie: | acl_key_profile_cookie: | IPV4_DIP | acl_range_direction: | | FORCE_TRAP_WITH_EVENT | | |
            # |  acl_cookie: | acl_key_profile_cookie: | IPV4_DIP | acl_range_direction: | |                       | | | 
            m2 = p2.match(line)
            if m2 and current_acl_oid is not None:
                group = m2.groupdict()
                entry = result_dict['acl_entries'][current_acl_oid]
                if group['acl_cookie'] and group['acl_cookie'] != 'None':
                    entry['acl_cookie'] = group['acl_cookie']
                if group['acl_key_profile_cookie'] and group['acl_key_profile_cookie'] != 'None':
                    entry['acl_key_profile_cookie'] = group['acl_key_profile_cookie']
                if group['acl_match_key_fields']:
                    entry['acl_match_key_fields'].append(group['acl_match_key_fields'])
                if group['acl_range_direction'] and group['acl_range_direction'] != 'None':
                    entry['acl_range_direction'] = group['acl_range_direction']
                if group['acl_commands']:
                    entry['acl_commands'].append(group['acl_commands'])
                continue

            # |              |                         | TOS | acl_range_count: | | COUNTER | | |
            # |              |                         | TOS | acl_range_count: | |         | | |
            m3 = p3.match(line)
            if m3 and current_acl_oid is not None:
                group = m3.groupdict()
                entry = result_dict['acl_entries'][current_acl_oid]
                if group['acl_match_key_fields']:
                    entry['acl_match_key_fields'].append(group['acl_match_key_fields'])
                if group['acl_range_count'] and group['acl_range_count'] != 'None':
                    entry['acl_range_count'] = group['acl_range_count']
                if group['acl_commands']:
                    entry['acl_commands'].append(group['acl_commands'])
                continue

            # |              |                         | PROTOCOL | | | DO_MIRROR | | |
            # |              |                         | PROTOCOL | | |           | | |
            m4 = p4.match(line)
            if m4 and current_acl_oid is not None:
                group = m4.groupdict()
                entry = result_dict['acl_entries'][current_acl_oid]
                if group['acl_match_key_fields']:
                    entry['acl_match_key_fields'].append(group['acl_match_key_fields'])
                if group['acl_commands']:
                    entry['acl_commands'].append(group['acl_commands'])
                continue
        
        # Iterate through all parsed ACL entries
        for acl_id, acl_data in result_dict.get('acl_entries', {}).items():
            # If 'acl_commands' key exists and its list is empty, delete the key
            if 'acl_commands' in acl_data and not acl_data['acl_commands']:
                del acl_data['acl_commands']

        return result_dict 

class ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAclSchema(MetaParser):
    """Schema for 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl'"""
    schema = {
        'acl_entries': {
            'priority': {
                Any(): {
                    Optional('ssp'): int,
                    Optional('ipv4_sip'): str,
                    Optional('ipv6_sip'): str,
                    Optional('source_mac'): str,
                    Optional('vlan'): int,
                    Optional('protocol'): int,
                    Optional('dport'): int,
                    Optional('sport'): int,
                    Optional('drop'): str,
                    Optional('icmp_v6_type'): int,
                    Optional('hit_count'): int,
                    Optional('counter_oid'): int,
                    Optional('ipv4_sip_mask'): str,
                    Optional('ipv6_sip_mask'): str,
                    Optional('source_mac_mask'): str
                }
            }
        }
    }

class ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAcl(ShowPlatformHardwareFedSwitchFwdAsicInsightIpSourceGuardAclSchema):
    """Parser for 'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl'"""

    cli_command = [
        'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl',
        'show platform hardware fed switch {switch} fwd-asic insight ip_source_guard_acl({devid})'
    ]

    def cli(self, switch, devid=None, output=None):
        if output is None:
            if devid:
                output = self.device.execute(self.cli_command[1].format(devid=devid, switch=switch))
            else:
                output = self.device.execute(self.cli_command[0].format(switch=switch))

        # Initialize the parsed dictionary
        ret_dict = {}

        # +----------+-----+----------+------------------------------------------------+--------------------------+------+----------+-------+-------+------+-------------+-----------+-------------+
        # | Priority | SSP | IPV4 SIP | IPV6 SIP                                       | Source mac               | Vlan | Protocol | DPort | SPort | Drop | ICMPV6 Type | Hit count | Counter oid |
        # +----------+-----+----------+------------------------------------------------+--------------------------+------+----------+-------+-------+------+-------------+-----------+-------------+
        # | 0        |     |          |                                                |                          |      | 17       | 67    | 68    |      |           | 4         | 1486        |
        p1 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<protocol>\d+)\s+\|\s+(?P<dport>\d+)\s+\|\s+(?P<sport>\d+)\s+\|\s+\|\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # | 20015    | 309 |          | IP   : fe80::200:ff:fe11:1111                  | Mac  : 00:00:00:11:11:11 | 100  |          |       |       |      |             | 0         | 3770        |
        p2 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+(?P<ssp>\d+)\s+\|\s+\|\s+IP\s*:\s*(?P<ipv6_sip>[a-fA-F0-9\:]+)\s+\|\s+Mac\s*:\s*(?P<source_mac>[\w:]+)\s+\|\s+(?P<vlan>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # |          |     |          | Mask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |             |           |             |
        p3 = re.compile(r'^\|\s+\|\s+\|\s+\|\s+Mask\s*:\s*(?P<ipv6_sip_mask>[a-fA-F0-9\:]+)\s+\|\s+Mask\s*:\s*(?P<source_mac_mask>[\w:]+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|$')

        # | 7        |     |          |                                                |                          |      |          |       |       |      | 134         | 0         | 1493        |
        p4 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<icmp_v6_type>\d+)\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # | 50015    | 309 |          |                                                |                          |      |          |       |       | true |             | 16363     | 3467        |
        p5 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+(?P<ssp>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<drop>\S*)\s+\|\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')
        
        # | 15       | 565 | IP   : 100.200.0.4     |                                                | Mac  : 00:00:00:22:22:22 | 200  |          |       |       |      |             | 15        | 3161        |
        p6 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+(?P<ssp>\d+)\s+\|\s+IP\s*:\s*(?P<ipv4_sip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\|\s+\|\s+Mac\s*:\s*(?P<source_mac>[\w:]+)\s+\|\s+(?P<vlan>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # |          |     | Mask : 255.255.255.255 |                                                | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |             |           |             |
        p7 = re.compile(r'^\|\s+\|\s+\|\s+Mask\s*:\s*(?P<ipv4_sip_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\|\s+\|\s+Mask\s*:\s*(?P<source_mac_mask>[\w:]+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|$')

        # | 0        |     |          |            |      | 17       | 67    | 68    |      | 0         | 1374        |
        p8 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<protocol>\d+)\s+\|\s+(?P<dport>\d+)\s+\|\s+(?P<sport>\d+)\s+\|\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # | 65533    |     |          |            |      |          |       |       | true | 0         | 1377        |
        p9 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<drop>\S*)\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # | 3        | 60  | IP   : 30.0.0.2        | Mac  : 00:12:01:00:00:01 | 30   |          |       |       |      | 0         | 2479        |
        p10 = re.compile(r'^\|\s+(?P<priority>\d+)\s+\|\s+(?P<ssp>\d+)\s+\|\s+IP\s*:\s*(?P<ipv4_sip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\|\s+Mac\s*:\s*(?P<source_mac>[\w:]+)\s+\|\s+(?P<vlan>\d+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+(?P<hit_count>\d+)\s+\|\s+(?P<counter_oid>\d+)\s+\|$')

        # |          |     | Mask : 255.255.255.255 | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |         |             |
        p11 = re.compile(r'^\|\s+\|\s+\|\s+Mask\s*:\s*(?P<ipv4_sip_mask>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\|\s+\|\s+Mask\s*:\s*(?P<source_mac_mask>[\w:]+)\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|\s+\|$')

        for line in output.splitlines():
            line = line.strip()

            # | 0        |     |          |                                                |                          |      | 17       | 67    | 68    |      |           | 4         | 1486        |
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['protocol'] = int(group['protocol'])
                result_dict['dport'] = int(group['dport'])
                result_dict['sport'] = int(group['sport'])
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # | 20015    | 309 |          | IP   : fe80::200:ff:fe11:1111                  | Mac  : 00:00:00:11:11:11 | 100  |          |       |       |      |             | 0         | 3770        |
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['ssp'] = int(group['ssp'])
                result_dict['ipv6_sip'] = group['ipv6_sip'] 
                result_dict['source_mac'] = group['source_mac']
                result_dict['vlan'] = int(group['vlan'])
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # |          |     |          | Mask : ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |             |           |             |
            m = p3.match(line)
            if m:
                group = m.groupdict()
                result_dict['ipv6_sip_mask'] = group['ipv6_sip_mask']
                result_dict['source_mac_mask'] = group['source_mac_mask']
                continue

            # | 7        |     |          |                                                |                          |      |          |       |       |      | 134         | 0         | 1493        |
            m = p4.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['icmp_v6_type'] = int(group['icmp_v6_type'])
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # | 50015    | 309 |          |                                                |                          |      |          |       |       | true |             | 16363     | 3467        |
            m = p5.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['ssp'] = int(group['ssp'])
                result_dict['drop'] = group['drop']
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # | 15       | 565 | IP   : 100.200.0.4     |                                                | Mac  : 00:00:00:22:22:22 | 200  |          |       |       |      |             | 15        | 3161        |
            m = p6.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['ssp'] = int(group['ssp'])
                result_dict['ipv4_sip'] = group['ipv4_sip']
                result_dict['source_mac'] = group['source_mac']
                result_dict['vlan'] = int(group['vlan'])
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # |          |     | Mask : 255.255.255.255 |                                                | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |             |           |             |
            m = p7.match(line)
            if m:
                group = m.groupdict()
                result_dict['ipv4_sip_mask'] = group['ipv4_sip_mask']   
                result_dict['source_mac_mask'] = group['source_mac_mask']
                continue

            # | 0        |     |          |            |      | 17       | 67    | 68    |      | 0         | 1374        |
            m = p8.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['protocol'] = int(group['protocol'])
                result_dict['dport'] = int(group['dport'])
                result_dict['sport'] = int(group['sport'])
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # | 65533    |     |          |            |      |          |       |       | true | 0         | 1377        |
            m = p9.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['drop'] = group['drop']
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # | 3        | 60  | IP   : 30.0.0.2        | Mac  : 00:12:01:00:00:01 | 30   |          |       |       |      | 0         | 2479        |
            m = p10.match(line)
            if m:
                group = m.groupdict()
                current_priority = int(group["priority"])
                result_dict = ret_dict.setdefault("acl_entries", {}).setdefault("priority", {}).setdefault(current_priority, {})
                result_dict['ssp'] = int(group['ssp'])
                result_dict['ipv4_sip'] = group['ipv4_sip']
                result_dict['source_mac'] = group['source_mac']
                result_dict['vlan'] = int(group['vlan'])
                result_dict['hit_count'] = int(group['hit_count'])
                result_dict['counter_oid'] = int(group['counter_oid'])
                continue

            # |          |     | Mask : 255.255.255.255 | Mask : ff:ff:ff:ff:ff:ff |      |          |       |       |      |         |             |
            m = p11.match(line)
            if m:
                group = m.groupdict()
                result_dict['ipv4_sip_mask'] = group['ipv4_sip_mask']   
                result_dict['source_mac_mask'] = group['source_mac_mask']
                continue

        return ret_dict
