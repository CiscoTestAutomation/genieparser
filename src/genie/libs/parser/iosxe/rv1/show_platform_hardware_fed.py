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
        p1 = re.compile('^ac_type:\s+(?P<ac_type>\S+)\s*\|(?:\s*switch_gid:\s+(?P<switch_gid>\d+))?\s*\|(?:\s*vlan_tag:\s+(?P<vlan_tag>\d+)|\s*eth_port_oid:\s+(?P<eth_port_oid>\d+))?\s*\|(?:\s*sysport_gid:\s+(?P<sysport_gid>\d+))?\s*$')

        # | ac_gid: 122906     |             | eth_port_oid: 1677    | sysport_cookie: Gi2/0/2 |
        # | ac_gid: 6           | switch_cookie: 300 |                       | sysport_cookie: Gi2/0/24 |
        p2 = re.compile('^ac_gid:\s+(?P<ac_gid>\d+)\s*\|(?:\s*switch_cookie:\s+(?P<switch_cookie>\d+))?\s*\|(?:\s*eth_port_oid:\s+(?P<eth_port_oid>\d+))?\s*\|(?:\s*sysport_cookie:\s+(?P<sysport_cookie>\S+))?\s*$')

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
