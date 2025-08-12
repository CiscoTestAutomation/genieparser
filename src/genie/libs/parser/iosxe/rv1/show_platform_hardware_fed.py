"""show_platform_hardware_fed.py
    * 'show platform software fed switch {switch} etherchannel {portchannelnum} load-balance {protocol_options}'
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import ListOf

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
        